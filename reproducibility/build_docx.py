"""Build the synchronized DOCX from the canonical Markdown with Pandoc.

Usage: python build_docx.py <candidate_root> <reference_styles.docx>

Pandoc converts $...$ math to native Word (OMML) equations. Pandoc drops \\tag{n}, so for the
DOCX only, each \\tag{n} is rewritten as a visible "(n)" at the end of the equation; the
canonical Markdown is not changed. Post-processing adds the PNG content-type default (absent
from the style-only reference), any styles Pandoc references that the reference lacks
(copied from Pandoc's default reference document), and the keywords document property.
"""
import copy
import io
import re
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

from lxml import etree

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
WP = "http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing"
A = "http://schemas.openxmlformats.org/drawingml/2006/main"
R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
PR = "http://schemas.openxmlformats.org/package/2006/relationships"
NS = {"w": W, "wp": WP, "a": A, "r": R}

root, ref = Path(sys.argv[1]), Path(sys.argv[2])
md = root / "manuscript" / "Manuscript_Source.md"
out = root / "manuscript" / "Grinberg_Transferred_Potential_Research_Paper.docx"
tmp = out.with_suffix(".tmp.docx")

text = md.read_text(encoding="utf-8")
docx_text, ntags = re.subn(r"\\tag\{(\d+)\}", r"\\qquad\\qquad (\1)", text)
if ntags != 7:
    sys.exit(f"expected 7 numbered equations, found {ntags}")

with tempfile.TemporaryDirectory() as td:
    src = Path(td) / "Manuscript_Source_docx.md"
    src.write_text(docx_text, encoding="utf-8")
    subprocess.run(["pandoc", str(src), "--from=markdown+tex_math_dollars+autolink_bare_uris", "--to=docx",
                    "--toc", "--toc-depth=2", f"--reference-doc={ref}", f"--resource-path={root}",
                    "-o", str(tmp)], check=True)

kw = re.search(r"^keywords:(.*?)(?=^\w+:|^---)", text, re.S | re.M).group(1)
kw = " ".join(kw.split())

# Styles that Pandoc references but the style-only reference lacks (for example Author, Date,
# Hyperlink) are copied from Pandoc's own default reference document so no reference dangles.
default_ref = subprocess.run(["pandoc", "--print-default-data-file", "reference.docx"],
                             capture_output=True, check=True).stdout
with zipfile.ZipFile(io.BytesIO(default_ref)) as dz:
    default_styles = dz.read("word/styles.xml").decode("utf-8")
default_by_id = {m.group(1): m.group(0) for m in
                 re.finditer(r'<w:style\b[^>]*w:styleId="([^"]+)"[^>]*>.*?</w:style>', default_styles, re.S)}

with zipfile.ZipFile(tmp) as zin:
    document_xml = zin.read("word/document.xml").decode("utf-8")
used = set(re.findall(r'<w:(?:pStyle|rStyle|tblStyle) w:val="([^"]+)"', document_xml))

with zipfile.ZipFile(tmp) as zin, zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zout:
    for item in zin.infolist():
        data = zin.read(item.filename)
        if item.filename == "word/document.xml":
            document = etree.fromstring(data)
            date_paragraphs = document.xpath('.//w:p[w:pPr/w:pStyle[@w:val="Date"]]', namespaces=NS)
            source_runs = document.xpath(".//w:r[w:drawing]", namespaces=NS)
            if len(date_paragraphs) != 1 or not source_runs:
                sys.exit("could not identify the DOCX cover insertion point or an image template")
            cover_paragraph = etree.Element(f"{{{W}}}p")
            properties = etree.SubElement(cover_paragraph, f"{{{W}}}pPr")
            etree.SubElement(properties, f"{{{W}}}jc").set(f"{{{W}}}val", "center")
            cover_run = copy.deepcopy(source_runs[0])
            for blip in cover_run.xpath(".//a:blip", namespaces=NS):
                blip.set(f"{{{R}}}embed", "rIdCoverImage")
            for extent in cover_run.xpath(".//wp:inline/wp:extent | .//a:xfrm/a:ext", namespaces=NS):
                extent.set("cx", "5943600")
                extent.set("cy", "3962400")
            drawing_ids = [int(value) for value in document.xpath(".//wp:docPr/@id", namespaces=NS)]
            for properties in cover_run.xpath(".//wp:docPr", namespaces=NS):
                properties.set("id", str(max(drawing_ids, default=0) + 1))
                properties.set("name", "Human brain cover illustration")
                properties.set("descr", "Black-and-white engraved illustration of a human brain")
            cover_paragraph.append(cover_run)
            page_break = etree.Element(f"{{{W}}}p")
            break_run = etree.SubElement(page_break, f"{{{W}}}r")
            etree.SubElement(break_run, f"{{{W}}}br").set(f"{{{W}}}type", "page")
            date_paragraphs[0].addnext(cover_paragraph)
            cover_paragraph.addnext(page_break)
            for table in document.xpath(".//w:tbl", namespaces=NS):
                widths = [int(col.get(f"{{{W}}}w")) for col in
                          table.xpath("./w:tblGrid/w:gridCol", namespaces=NS)]
                if not widths or any(width <= 0 for width in widths):
                    continue
                table_width = table.find("./w:tblPr/w:tblW", NS)
                if table_width is not None:
                    table_width.set(f"{{{W}}}type", "dxa")
                    table_width.set(f"{{{W}}}w", str(sum(widths)))
                for row_index, row in enumerate(table.xpath("./w:tr", namespaces=NS)):
                    row_properties = row.find("./w:trPr", NS)
                    if row_properties is None:
                        row_properties = etree.Element(f"{{{W}}}trPr")
                        row.insert(0, row_properties)
                    if row_properties.find("./w:cantSplit", NS) is None:
                        etree.SubElement(row_properties, f"{{{W}}}cantSplit")
                    if row_index == 0 and row_properties.find("./w:tblHeader", NS) is None:
                        etree.SubElement(row_properties, f"{{{W}}}tblHeader")
                    column = 0
                    for cell in row.xpath("./w:tc", namespaces=NS):
                        properties = cell.find("./w:tcPr", NS)
                        if properties is None:
                            properties = etree.Element(f"{{{W}}}tcPr")
                            cell.insert(0, properties)
                        span_element = properties.find("./w:gridSpan", NS)
                        span = int(span_element.get(f"{{{W}}}val")) if span_element is not None else 1
                        cell_width = properties.find("./w:tcW", NS)
                        if cell_width is None:
                            cell_width = etree.SubElement(properties, f"{{{W}}}tcW")
                        cell_width.set(f"{{{W}}}type", "dxa")
                        cell_width.set(f"{{{W}}}w", str(sum(widths[column:column + span])))
                        column += span
            data = etree.tostring(document, xml_declaration=True, encoding="UTF-8", standalone=True)
        if item.filename == "word/_rels/document.xml.rels":
            relationships = etree.fromstring(data)
            if any(rel.get("Id") == "rIdCoverImage" for rel in relationships):
                sys.exit("DOCX cover relationship identifier is already in use")
            relationship = etree.SubElement(relationships, f"{{{PR}}}Relationship")
            relationship.set("Id", "rIdCoverImage")
            relationship.set("Type", R + "/image")
            relationship.set("Target", "media/brain_cover.png")
            data = etree.tostring(relationships, xml_declaration=True, encoding="UTF-8", standalone=True)
        if item.filename == "word/styles.xml":
            styles = data.decode("utf-8")
            defined = set(re.findall(r'<w:style\b[^>]*w:styleId="([^"]+)"', styles))
            added = [default_by_id[s] for s in sorted(used - defined) if s in default_by_id]
            styles = styles.replace("</w:styles>", "".join(added) + "</w:styles>")
            data = styles.encode("utf-8")
        if item.filename == "[Content_Types].xml" and b'Extension="png"' not in data:
            data = re.sub(rb"(<Types[^>]*>)", rb'\1<Default Extension="png" ContentType="image/png"/>', data, count=1)
        if item.filename == "docProps/core.xml":
            data = data.replace(b"<cp:keywords></cp:keywords>", f"<cp:keywords>{kw}</cp:keywords>".encode("utf-8"))
        zout.writestr(item, data)
    zout.writestr("word/media/brain_cover.png", (root / "cover" / "brain_cover.png").read_bytes())
tmp.unlink()
print(f"wrote {out} ({ntags} numbered equations)")
