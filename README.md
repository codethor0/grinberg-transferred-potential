# Reassessing the Transferred-Potential Hypothesis

**Subtitle:** Syntergic Theory, Isolated-Brain EEG Evidence, and Reproducible Tests  
**Author:** Thor Thor  
**Status:** Clean final manuscript for author release approval; independent adversarial review incorporated

## Read the paper

- `manuscript/Grinberg_Transferred_Potential_Research_Paper.pdf` — final-review reading copy.
- `manuscript/Grinberg_Transferred_Potential_Research_Paper.docx` — editable copy with native Word equations.
- `manuscript/Manuscript_Source.md` — canonical text, mathematics, tables, captions, references, and appendices.

The article is a source-traced critical methodological review with an original synthetic demonstration. It does not claim a new human EEG experiment, a completed retrospective EEG reanalysis, external peer review, or demonstrated anomalous brain-to-brain communication.

## Reproduce the computational work

Run:

```sh
sh reproducibility/run_all.sh
```

This regenerates the synthetic benchmark, all nine figures in PNG and PDF formats, and the manuscript PDF. The expected false-positive rates are 43.28% and 4.54% for naive and circular-shift tests in the 13–35 Hz condition, and 62.06% and 5.08% in the 4–12 Hz condition. See `reproducibility/README.md` for dependencies, interpretation limits, expected counts, and the Word-build boundary.

## Review and release documents

- `VERIFICATION_REPORT.md` — observed final verification results and scope.
- `AUDIT_DISPOSITION.md` — disposition of all 46 independent-audit findings.
- `ENVIRONMENT.md` — measured software environment.
- `RIGHTS_MANIFEST.md` — original-asset and third-party-rights boundaries.
- `RELEASE_STATUS.md` — remaining license, metadata, and author-approval gates.
- `metadata/ZENODO_METADATA_PROPOSED.md` — proposed metadata for a later deposit; not a published record.
- `SHA256SUMS.txt` — SHA-256 hashes for every candidate file except the checksum file itself.

No third-party source PDFs are included. No DOI or public license has been assigned or selected. The independent adversarial review is complete and incorporated; do not upload until the author explicitly approves the exact final files, byline, metadata, and license or licenses.
