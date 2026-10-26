#!/usr/bin/env python3
"""Independent, fail-closed checks for the final-review release candidate."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path
from statistics import NormalDist

from lxml import etree
from PIL import Image
from pypdf import PdfReader

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
M = "http://schemas.openxmlformats.org/officeDocument/2006/math"
NS = {"w": W, "m": M}
FIGURE_STEMS = [
    "figure1_syntergic_theory",
    "figure2_brain_measurement_chain",
    "figure3_historical_timeline",
    "figure4_endpoint_taxonomy",
    "figure5_apparatus_audit",
    "figure6_identifiability",
    "figure7_synthetic_fpr",
    "figure8_reanalysis_pipeline",
    "figure9_multilab_protocol",
]
EXPECTED = [
    {"band_hz": [13, 35], "naive_rejections": 2164, "circular_shift_rejections": 227,
     "naive_false_positive_rate": 0.4328, "circular_shift_false_positive_rate": 0.0454},
    {"band_hz": [4, 12], "naive_rejections": 3103, "circular_shift_rejections": 254,
     "naive_false_positive_rate": 0.6206, "circular_shift_false_positive_rate": 0.0508},
]
EXPECTED_CONSOLE = (
    "BAND 13-35Hz n=5000 naive_p<.05 0.4328 nullshift_p<=.05 0.0454 "
    "naive_median=0.0908 shift_median=0.4961\n"
    "BAND 4-12Hz n=5000 naive_p<.05 0.6206 nullshift_p<=.05 0.0508 "
    "naive_median=0.0087 shift_median=0.4922\n"
)

checks: list[dict] = []


def record(name: str, passed: bool, detail: str = "") -> None:
    checks.append({"name": name, "passed": bool(passed), "detail": detail})


def group(name: str, fn, *args) -> None:
    try:
        fn(*args)
    except Exception as exc:
        record(name, False, f"{type(exc).__name__}: {exc}")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def normalized(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def wilson(k: int, n: int) -> tuple[float, float]:
    z = NormalDist().inv_cdf(0.975)
    p = k / n
    den = 1 + z * z / n
    center = (p + z * z / (2 * n)) / den
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
    return 100 * (center - half), 100 * (center + half)


def check_manuscript(root: Path) -> None:
    path = root / "manuscript/Manuscript_Source.md"
    source = path.read_text(encoding="utf-8")
    required = [
        "25 ordered pairings formed from six adults",
        "20 ordered pairings formed from five adults",
        "Each dyad is weighted equally",
        "recorded covariate history $H_t$",
        "multiplicity control must be registered",
        "41.91%–44.66%", "4.00%–5.15%", "60.71%–63.40%", "4.51%–5.72%",
        "1/128 = 0.0078125", "6/128 = 4.6875%",
        "accepted-event criteria must be fixed",
        "no epoch with missing baseline or primary-interval samples is silently imputed",
        "**Pair-held-out**", "**Participant-held-out**",
        "participant-held-out primary reanalysis",
        "May, Spottiswoode, and Faith (2010)",
        "windows of 16 consecutive points", "48 correlations per pair",
        "**42.82%**", "**60.97%**",
        "**primary statistic is template projection**",
        "exact paired-$t$ calculation gives **199**",
        "80% at about **215 pairs**",
        "pre-space structure", "AI-based assistants were used",
        "stimulus-locked leakage proxies", "maximum power",
        "*Subtle Energies*, 3(3), 25–43",
        "selected chronology",
        "| Does validation match the generalization unit? |",
        "author: Thor Thor", "**Author affiliation:** Independent Open-Source Researcher",
    ]
    missing = [text for text in required if text not in source]
    record("Manuscript contains every approved scientific correction", not missing, str(missing))
    stale = [
        "ML reanalysis of 25- and 20-pair datasets",
        "Twenty-five pairs; EEG ERP",
        "recorded covariates $Z_t$",
        "receiver data in previously unseen pairs",
        "before public versioning", "6/128 = 0.046875", "space-time lattice",
        "RESEARCH DRAFT", "Draft_v", "TODO", "FIXME",
    ]
    present = [text for text in stale if text in source]
    record("No stale scientific wording or draft markers in source", not present, str(present))
    order = [source.index("## 12.1."), source.index("## 12.2."), source.index("## 12.3.")]
    record("Section 12.2 occupies the correct position", order == sorted(order))
    figure_refs = re.findall(r"\]\((figures/[^)]+\.png)\)", source)
    record("Source references exactly nine unique figures",
           len(figure_refs) == 9 and len(set(figure_refs)) == 9, str(figure_refs))
    record("Manuscript retains full explanatory length", len(source.split()) >= 15000,
           f"{len(source.split())} whitespace-delimited tokens")
    body, reference_block = re.split(r"(?m)^# References\s*$", source, maxsplit=1)
    references = [int(value) for value in re.findall(r"^\[(\d+)\]", reference_block, re.MULTILINE)]
    record("Reference list is complete and sequentially numbered", references == list(range(1, 47)),
           f"count={len(references)}")
    cited_numbers = set()
    for content in re.findall(r"\[([^\]\n]+)\]", body):
        citation = content.strip().replace("–", "-").replace("—", "-")
        if not re.fullmatch(r"\d+(?:\s*(?:,|;|-)\s*\d+)*", citation):
            continue
        for item in re.split(r"\s*[,;]\s*", citation):
            bounds = [int(value) for value in re.split(r"\s*-\s*", item)]
            if len(bounds) == 1:
                cited_numbers.add(bounds[0])
            elif len(bounds) == 2 and bounds[0] <= bounds[1]:
                cited_numbers.update(range(bounds[0], bounds[1] + 1))
    uncited = sorted(set(references) - cited_numbers)
    undefined = sorted(cited_numbers - set(references))
    record("All 46 references are cited and no citation is undefined",
           not uncited and not undefined,
           f"uncited={uncited}; undefined={undefined}")
    intervals = []
    for row in EXPECTED:
        for key in ("naive_rejections", "circular_shift_rejections"):
            lo, hi = wilson(row[key], 5000)
            intervals.append(f"{lo:.2f}%–{hi:.2f}%")
    record("Independent Wilson-interval recomputation matches manuscript",
           intervals == ["41.91%–44.66%", "4.00%–5.15%", "60.71%–63.40%", "4.51%–5.72%"],
           str(intervals))
    n = (NormalDist().inv_cdf(0.975) + NormalDist().inv_cdf(0.80)) ** 2 / 0.20 ** 2
    record("Normal-approximation planning calculation is numerically consistent",
           math.ceil(n) == 197 and abs(n - 196.221993) < 1e-6, f"n={n:.8f}")
    record("Shift-test attainable size is exact", abs(6 / 128 - 0.046875) < 1e-15)
    from scipy import stats
    def paired_power(sample_size: int) -> float:
        df = sample_size - 1
        critical = stats.t.ppf(0.975, df)
        noncentrality = 0.20 * math.sqrt(sample_size)
        return float(stats.nct.sf(critical, df, noncentrality) +
                     stats.nct.cdf(-critical, df, noncentrality))
    exact_n = next(value for value in range(2, 1000) if paired_power(value) >= 0.80)
    record("Exact paired-t planning calculation gives 199 pairs", exact_n == 199,
           f"n={exact_n}; power197={paired_power(197):.8f}")
    def tost_power(sample_size: int) -> float:
        limit = 0.20 * math.sqrt(sample_size) - stats.norm.ppf(0.95)
        return float(max(0.0, 2 * stats.norm.cdf(limit) - 1))
    tost_n = next(value for value in range(2, 2000) if tost_power(value) >= 0.80)
    record("Equivalence planning calculation gives 215 pairs",
           tost_n == 215 and abs(100 * tost_power(197) - 75.4878) < 0.001,
           f"n={tost_n}; power197={100 * tost_power(197):.6f}%")
    critical_r = stats.t.ppf(0.975, 126) / math.sqrt(stats.t.ppf(0.975, 126) ** 2 + 126)
    analytic = [200 * stats.t.sf(critical_r * math.sqrt(d - 1) /
                                 math.sqrt(1 - critical_r ** 2), d - 1) for d in (22, 10)]
    record("Analytic naive-rate expectations match the manuscript",
           abs(analytic[0] - 42.8199) < 0.001 and abs(analytic[1] - 60.9668) < 0.001,
           f"13-35Hz={analytic[0]:.6f}%; 4-12Hz={analytic[1]:.6f}%")
    nominal = [200 * stats.t.sf(value * math.sqrt(14) / math.sqrt(1 - value ** 2), 14)
               for value in (0.70, 0.62)]
    record("Nominal 16-point correlation probabilities are correct",
           abs(nominal[0] - 0.2535) < 0.001 and abs(nominal[1] - 1.0407) < 0.001,
           f"r=.70: {nominal[0]:.6f}%; r=.62: {nominal[1]:.6f}%")


def check_figures(root: Path) -> None:
    cover = root / "cover/brain_cover.png"
    with Image.open(cover) as image:
        image.verify()
    with Image.open(cover) as image:
        record("Cover brain illustration is readable at full resolution",
               image.size == (1536, 1024), f"{image.width}x{image.height}")
    figure_dir = root / "figures"
    for stem in FIGURE_STEMS:
        png, pdf = figure_dir / f"{stem}.png", figure_dir / f"{stem}.pdf"
        record(f"{stem}: PNG and PDF exist", png.is_file() and pdf.is_file())
        with Image.open(png) as image:
            image.verify()
        with Image.open(png) as image:
            record(f"{stem}: PNG dimensions are usable", image.width >= 1000 and image.height >= 500,
                   f"{image.width}x{image.height}")
        reader = PdfReader(str(pdf))
        record(f"{stem}: vector PDF is readable", len(reader.pages) == 1)
    record("Figure directory contains exactly nine PNG/PDF pairs",
           len(list(figure_dir.glob("*.png"))) == 9 and len(list(figure_dir.glob("*.pdf"))) == 9)
    figure_results = json.loads((figure_dir / "figure7_results.json").read_text(encoding="utf-8"))
    expected_figure_results = [[f"{r['band_hz'][0]}-{r['band_hz'][1]} Hz",
                                100 * r["naive_false_positive_rate"],
                                100 * r["circular_shift_false_positive_rate"]] for r in EXPECTED]
    record("Figure 7 values match the benchmark", figure_results == expected_figure_results,
           str(figure_results))


def check_docx(root: Path) -> None:
    path = root / "manuscript/Grinberg_Transferred_Potential_Research_Paper.docx"
    with zipfile.ZipFile(path) as archive:
        record("DOCX ZIP integrity", archive.testzip() is None)
        names = archive.namelist()
        doc = etree.fromstring(archive.read("word/document.xml"))
        styles = etree.fromstring(archive.read("word/styles.xml"))
        footer = etree.fromstring(archive.read("word/footer1.xml"))
        comments = etree.fromstring(archive.read("word/comments.xml"))
        revision_tags = ("ins", "del", "moveFrom", "moveTo", "pPrChange", "rPrChange", "sectPrChange")
        revision_count = sum(len(doc.xpath(f".//w:{tag}", namespaces=NS)) for tag in revision_tags)
        record("DOCX contains no tracked revisions", revision_count == 0, f"count={revision_count}")
        record("DOCX contains no comments", len(comments.xpath(".//w:comment", namespaces=NS)) == 0)
        all_xml = b"\n".join(archive.read(name) for name in names if name.endswith(".xml"))
        record("DOCX contains no draft/version marker", b"RESEARCH DRAFT" not in all_xml and b"Draft_v" not in all_xml)
        record("DOCX retains page-number field",
               len(footer.xpath(".//w:fldSimple[contains(@w:instr, 'PAGE')]", namespaces=NS)) == 1)
        defined = {e.get(f"{{{W}}}styleId") for e in styles.xpath(".//w:style", namespaces=NS)}
        referenced = {e.get(f"{{{W}}}val") for e in
                      doc.xpath(".//w:pStyle | .//w:rStyle | .//w:tblStyle", namespaces=NS)}
        record("DOCX has no dangling paragraph/character/table style references", referenced <= defined,
               str(sorted(referenced - defined)))
        bad_dpr = []
        for dpr in doc.xpath(".//m:dPr[m:sepChr]", namespaces=NS):
            order = [etree.QName(child).localname for child in dpr]
            if "begChr" in order and not order.index("begChr") < order.index("sepChr"):
                bad_dpr.append(order)
            if "endChr" in order and not order.index("sepChr") < order.index("endChr"):
                bad_dpr.append(order)
        record("OMML delimiter properties follow schema order", not bad_dpr, str(bad_dpr[:3]))
        bad_rpr = [rpr for rpr in doc.xpath(".//m:rPr[m:scr and m:sty]", namespaces=NS)
                   if rpr.index(rpr.find(f"{{{M}}}scr")) > rpr.index(rpr.find(f"{{{M}}}sty"))]
        record("OMML script/style properties follow schema order", not bad_rpr)
        rows = doc.xpath(".//w:tbl/w:tr", namespaces=NS)
        record("DOCX table rows cannot split across pages",
               len(rows) > 0 and all(row.find("./w:trPr/w:cantSplit", NS) is not None for row in rows))
        table_headers = doc.xpath(".//w:tbl/w:tr[1]/w:trPr/w:tblHeader", namespaces=NS)
        record("DOCX table headers repeat on continuation pages", len(table_headers) == 6,
               f"headers={len(table_headers)}")
        paragraphs = ["".join(p.xpath(".//w:t/text()", namespaces=NS)) for p in doc.xpath(".//w:p", namespaces=NS)]
        text = normalized("\n".join(paragraphs))
        for phrase in ["25 ordered pairings formed from six adults", "participant-held-out validation",
                       "41.91%–44.66%", "May, Spottiswoode, and Faith (2010)", "4.6875%",
                       "primary statistic is template projection", "AI-based assistants were used",
                       "Does validation match the generalization unit?", "Thor Thor",
                       "Independent Open-Source Researcher"]:
            record(f"DOCX synchronized text: {phrase[:45]}", phrase in text)
        media = {name: hashlib.sha256(archive.read(name)).hexdigest()
                 for name in names if name.startswith("word/media/")}
        figure_hashes = {sha256(root / f"figures/{stem}.png") for stem in FIGURE_STEMS}
        expected_media = figure_hashes | {sha256(root / "cover/brain_cover.png")}
        record("DOCX embeds nine figures and the exact cover illustration",
               len(media) == 10 and set(media.values()) == expected_media, f"media={len(media)}")


def check_pdf(root: Path) -> None:
    path = root / "manuscript/Grinberg_Transferred_Potential_Research_Paper.pdf"
    reader = PdfReader(str(path))
    record("Final PDF is readable and retains full length", len(reader.pages) >= 30,
           f"pages={len(reader.pages)}")
    record("PDF cover contains the brain illustration", len(reader.pages[0].images) == 1,
           f"cover_images={len(reader.pages[0].images)}")
    text = normalized("\n".join(page.extract_text() or "" for page in reader.pages))
    for phrase in ["Reassessing the Transferred-Potential Hypothesis", "43.28%", "62.06%", "4.54%", "5.08%",
                   "41.91%–44.66%", "4.6875%", "42.82%", "60.97%",
                   "Spottiswoode, and Faith (2010)", "Confound Audit Matrix",
                   "Thor Thor", "Independent Open-Source Researcher",
                   "Expected output, rounded: 13 35 0.4328 0.0454 and 4 12 0.6206 0.0508"]:
        record(f"PDF contains: {phrase[:55]}", phrase in text)
    record("PDF has no visible draft/version markers",
           not re.search(r"RESEARCH DRAFT|Draft_v|\bV[1-4]\b", text, re.IGNORECASE))
    title = reader.metadata.title if reader.metadata else None
    record("PDF metadata has clean title", title == "Reassessing the Transferred-Potential Hypothesis", str(title))


def check_package(root: Path) -> None:
    required = [
        "README.md", "ENVIRONMENT.md", "RELEASE_STATUS.md", "RIGHTS_MANIFEST.md",
        "VERIFICATION_REPORT.md", "AUDIT_DISPOSITION.md",
        "metadata/ZENODO_METADATA_PROPOSED.md", "reproducibility/run_all.sh",
        "reproducibility/README.md", "reproducibility/requirements_executed.txt",
        "reproducibility/results.json", "reproducibility/simulation_check.txt",
        "reproducibility/make_figures.py", "reproducibility/refine_figures.py",
        "reproducibility/synthetic_null_demo.py", "reproducibility/manuscript.template",
        "reproducibility/build_docx.py", "reproducibility/reference_styles.docx",
        "cover/brain_cover.png",
    ]
    record("All release documentation and reproduction files exist",
           all((root / rel).is_file() for rel in required))
    allowed_pdfs = {"manuscript/Grinberg_Transferred_Potential_Research_Paper.pdf",
                    *(f"figures/{stem}.pdf" for stem in FIGURE_STEMS)}
    actual_pdfs = {str(p.relative_to(root)) for p in root.rglob("*.pdf")}
    record("No third-party or unexpected source PDFs are included", actual_pdfs == allowed_pdfs,
           str(sorted(actual_pdfs - allowed_pdfs)))
    bad_names = [str(p.relative_to(root)) for p in root.rglob("*")
                 if re.search(r"draft|_v[1-4](?:\b|_)", p.name, re.IGNORECASE)]
    record("No draft/versioned filenames remain in candidate", not bad_names, str(bad_names))
    forbidden_parts = {"adversarial_review", "revision_tier1_2", "docx_build", "docx_work", "verification"}
    private_material = [str(p.relative_to(root)) for p in root.rglob("*")
                        if forbidden_parts & set(p.relative_to(root).parts)]
    record("Private audit and temporary build materials are excluded", not private_material,
           str(private_material))
    record("Candidate contains no symbolic links", not any(p.is_symlink() for p in root.rglob("*")))
    private_paths = []
    for path in root.rglob("*"):
        if path.is_file() and path.name != "verify_release.py" and path.suffix in {".py", ".sh", ".md", ".template", ".txt", ".json"}:
            text = path.read_text(encoding="utf-8")
            if re.search(r"/Users/[^/]+/|/home/[^/]+/|/mnt/data/", text):
                private_paths.append(str(path.relative_to(root)))
    record("Portable release files contain no private absolute paths", not private_paths, str(private_paths))
    for script in (root / "reproducibility").glob("*.py"):
        compile(script.read_text(encoding="utf-8"), str(script), "exec")
    record("All Python sources compile", True)
    shell = subprocess.run(["sh", "-n", str(root / "reproducibility/run_all.sh")], capture_output=True, text=True)
    record("run_all.sh passes shell syntax check", shell.returncode == 0, shell.stderr)
    requirements = (root / "reproducibility/requirements_executed.txt").read_text(encoding="utf-8")
    record("Document-builder dependency is pinned", "lxml==6.1.0" in requirements)
    metadata = (root / "metadata/ZENODO_METADATA_PROPOSED.md").read_text(encoding="utf-8")
    record("Deposit metadata uses corrected terminology and author identity",
           "pre-space structure" in metadata and "space-time lattice" not in metadata
           and "**Creator:** Thor, Thor" in metadata
           and "**Affiliation:** Independent Open-Source Researcher" in metadata)
    release = (root / "RELEASE_STATUS.md").read_text(encoding="utf-8")
    record("License and author-approval gates remain explicit",
           "License selection" in release and "Author release approval" in release)
    record("Candidate does not claim to be Zenodo-ready", "Zenodo-ready" not in release)


def check_recorded_results(root: Path) -> None:
    results = json.loads((root / "reproducibility/results.json").read_text(encoding="utf-8"))
    record("Recorded benchmark design is exact",
           results["seed"] == 20261025 and results["simulated_pairs_per_band"] == 5000
           and results["samples_per_recording"] == 128 and results["sampling_rate_hz"] == 256
           and results["nominal_alpha"] == 0.05)
    for actual, expected in zip(results["results"], EXPECTED):
        for key, value in expected.items():
            record(f"Recorded {actual['band_hz']} {key}", actual[key] == value, str(actual[key]))
    console = (root / "reproducibility/simulation_check.txt").read_text(encoding="utf-8")
    record("Recorded console output is exact", console == EXPECTED_CONSOLE)


def check_clean_benchmark(root: Path, scratch_parent: Path) -> None:
    with tempfile.TemporaryDirectory(prefix="benchmark-", dir=scratch_parent) as tmp:
        tmp_path = Path(tmp)
        script = tmp_path / "synthetic_null_demo.py"
        shutil.copy2(root / "reproducibility/synthetic_null_demo.py", script)
        env = os.environ.copy()
        env["PYTHONHASHSEED"] = "0"
        run = subprocess.run([sys.executable, str(script)], cwd=tmp_path, env=env,
                             capture_output=True, text=True, timeout=180)
        record("Clean-directory benchmark exits successfully", run.returncode == 0, run.stderr)
        record("Clean-directory benchmark console output is exact", run.stdout == EXPECTED_CONSOLE, run.stdout)
        rerun = json.loads((tmp_path / "results.json").read_text(encoding="utf-8"))
        for actual, expected in zip(rerun["results"], EXPECTED):
            for key, value in expected.items():
                record(f"Clean rerun {actual['band_hz']} {key}", actual[key] == value, str(actual[key]))


def check_visual_reports(root: Path, audit_dir: Path) -> None:
    expected_pdf_pages = len(PdfReader(str(
        root / "manuscript/Grinberg_Transferred_Potential_Research_Paper.pdf")).pages)
    pdf = json.loads((audit_dir / "pdf_inspect.json").read_text(encoding="utf-8"))["data"]
    record("Rendered PDF inspection covers the final PDF with zero warnings",
           pdf["pageCount"] == expected_pdf_pages and len(pdf["pages"]) == expected_pdf_pages
           and not pdf["warnings"] and all(not p["warnings"] for p in pdf["pages"]),
           f"pages={pdf['pageCount']}; final={expected_pdf_pages}")
    docx = json.loads((audit_dir / "docx_render/report.json").read_text(encoding="utf-8"))
    pages = docx["pages"]
    record("Rendered DOCX inspection includes every reported page",
           pages > 0 and docx["rendered"] == pages and len(docx["pageFiles"]) == pages,
           f"pages={pages}; rendered={docx['rendered']}")
    record("Rendered DOCX inspection: no blank/clipped pages or content loss",
           not docx["nearBlankPages"] and docx["fidelity"]["byCategory"]["content-loss"] == 0
           and all(not p["nearBlank"] and not p["clipped"] for p in docx["pageFiles"]))


def check_full_docx_gate(root: Path, validator: Path) -> None:
    docx = root / "manuscript/Grinberg_Transferred_Potential_Research_Paper.docx"
    before = sha256(docx)
    run = subprocess.run([sys.executable, str(validator), "validate", str(docx)], capture_output=True, text=True, timeout=180)
    record("Full-file DOCX OOXML/XSD gate passes", run.returncode == 0 and "PASSED" in run.stdout,
           normalized(run.stdout + "\n" + run.stderr))
    record("Full-file DOCX gate leaves the sealed artifact unchanged", sha256(docx) == before)


def check_manifest(root: Path) -> None:
    manifest = root / "SHA256SUMS.txt"
    expected = {str(p.relative_to(root)): p for p in root.rglob("*") if p.is_file() and p != manifest}
    lines = [line for line in manifest.read_text(encoding="utf-8").splitlines() if line]
    entries = {}
    malformed = []
    for line in lines:
        match = re.fullmatch(r"([0-9a-f]{64})  (.+)", line)
        if not match:
            malformed.append(line)
            continue
        digest, rel = match.groups()
        entries[rel] = digest
    record("Checksum manifest syntax and coverage are exact",
           not malformed and set(entries) == set(expected) and len(entries) == len(lines),
           f"entries={len(entries)} expected={len(expected)} malformed={len(malformed)}")
    bad = [rel for rel, digest in entries.items() if rel in expected and sha256(expected[rel]) != digest]
    record("Every candidate file matches its SHA-256 manifest entry", not bad, str(bad))


def check_zip(root: Path, zip_path: Path) -> None:
    prefix = root.name + "/"
    expected = {prefix + str(p.relative_to(root)): p for p in root.rglob("*") if p.is_file()}
    with zipfile.ZipFile(zip_path) as archive:
        record("Release ZIP integrity", archive.testzip() is None)
        names = {name for name in archive.namelist() if not name.endswith("/")}
        record("Release ZIP has exact file coverage", names == set(expected),
               f"zip={len(names)} candidate={len(expected)}")
        bad = [name for name, path in expected.items()
               if name in names and hashlib.sha256(archive.read(name)).hexdigest() != sha256(path)]
        record("Every archived file is byte-identical to the candidate", not bad, str(bad))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--audit-dir", type=Path)
    parser.add_argument("--docx-validator", type=Path)
    parser.add_argument("--zip", dest="zip_path", type=Path)
    parser.add_argument("--scratch-parent", type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    group("manuscript group", check_manuscript, root)
    group("figure group", check_figures, root)
    group("DOCX group", check_docx, root)
    group("PDF group", check_pdf, root)
    group("package group", check_package, root)
    group("recorded results group", check_recorded_results, root)
    args.scratch_parent.mkdir(parents=True, exist_ok=True)
    group("clean benchmark group", check_clean_benchmark, root, args.scratch_parent.resolve())
    if args.audit_dir:
        group("visual audit group", check_visual_reports, root, args.audit_dir.resolve())
    if args.docx_validator:
        group("full DOCX gate group", check_full_docx_gate, root, args.docx_validator.resolve())
    if (root / "SHA256SUMS.txt").exists():
        group("manifest group", check_manifest, root)
    if args.zip_path:
        group("ZIP group", check_zip, root, args.zip_path.resolve())
    passed = sum(c["passed"] for c in checks)
    failed = len(checks) - passed
    report = {"status": "PASS" if failed == 0 else "FAIL", "root": str(root),
              "checks_passed": passed, "checks_failed": failed, "checks": checks}
    payload = json.dumps(report, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload, encoding="utf-8")
    print(payload, end="")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
