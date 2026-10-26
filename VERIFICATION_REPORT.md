# Final manuscript and release-candidate verification report

**Verification date:** October 25, 2026  
**Automated release gate:** **PASS: 127 checks passed, 0 failed**  
**Regression suite:** **PASS: 3 tests, 0 failures**  
**Release state:** Author-approved public release; manuscript files unchanged by the final licensing update

## Scope and result

The gate checked the canonical manuscript, final PDF and DOCX, cover illustration, all figure assets, recorded and freshly executed benchmark results, numerical derivations, citation coverage, document structure, visual-inspection reports, package exclusions, SHA-256 manifest, and byte identity between the candidate directory and release ZIP. The 127-check result includes the external visual-inspection reports. The previously passed full-file DOCX validator remains applicable because the DOCX hash is unchanged. The verifier included in the package can also run the scientific, numerical, structural, benchmark, manifest, and ZIP checks without those external tools.

The independent adversarial audit contained 46 findings. The disposition record accounts for every finding: 43 incorporated, one confirmed without correction, one not applied because the underlying source was not inspected, and one retained as an author-controlled release gate.

## Manuscript and references

- Canonical source: 18,303 whitespace-delimited tokens, retaining the full methodological explanation and appendices.
- References: 46 sequential entries; all 46 are cited and no numeric citation is undefined.
- Scientific corrections include the 1994 selection procedures, 16-point correlations and 48 reported overlapping windows, May et al.'s empirical-null critique, exact shift-test size, analytic naive-rate expectations, template-projection endpoint, participant-held-out validation, paired-test and equivalence planning, corrected no-signaling interpretation, pre-space terminology, and actual AI-use disclosure.
- Post-audit manuscript changes were limited to the approved black-and-white brain cover illustration and the established author identity: Thor Thor and Independent Open-Source Researcher. PDF text is otherwise identical to the approved pre-identity build, and the scientific body, equations, citations, and appendices are unchanged.
- No draft labels, tracked revisions, comments, or visible revision markers were detected.

## PDF and DOCX

- PDF: 38 pages. Automated inspection covered all 38 pages with zero warnings. Full contact-sheet review found no blank pages, clipping, broken equations, figure collisions, or visible revision markers. The first page contains the title, subtitle, byline, date, and large brain illustration.
- DOCX: 42 rendered pages out of 42 reported pages. Inspection found no near-blank pages, clipping, or content loss. The cover illustration and following page break render correctly.
- DOCX validation: `PASSED (19 parts XSD + semantic checks; gen: 6 checks clean)`.
- The renderer's `degraded` fidelity label concerns unmodeled theme, style, and related metadata. Its measured `content-loss` count is zero.
- All six DOCX tables have repeating header rows and rows marked not to split across pages. The DOCX embeds exact copies of the nine final PNG figures and the cover illustration.

## Numerical and reproduction checks

The clean-directory benchmark used seed 20261025, 5,000 independent synthetic pairs per band, 128 samples per recording, and a sampling rate of 256 Hz. It reproduced the recorded output exactly:

```text
BAND 13-35Hz n=5000 naive_p<.05 0.4328 nullshift_p<=.05 0.0454 naive_median=0.0908 shift_median=0.4961
BAND 4-12Hz n=5000 naive_p<.05 0.6206 nullshift_p<=.05 0.0508 naive_median=0.0087 shift_median=0.4922
```

The corresponding rejection counts are 2,164 and 227 in the 13–35 Hz condition, and 3,103 and 254 in the 4–12 Hz condition. Independent recomputation confirmed:

- Wilson 95% intervals: 41.91%–44.66%, 4.00%–5.15%, 60.71%–63.40%, and 4.51%–5.72%.
- Exact attainable circular-shift size: 6/128 = 4.6875%.
- Analytic naive-rate expectations: 42.819901% and 60.966757%, reported as 42.82% and 60.97%.
- Nominal 16-point correlation probabilities: 0.253509% at r = 0.70 and 1.040707% at r = 0.62.
- Normal-approximation planning value: 196.221993, giving 197 pairs after rounding up.
- Exact paired-t calculation: 199 pairs for at least 80% power under the declared assumptions; power at 197 pairs is 79.768861%.
- Equivalence planning approximation: 215 pairs for 80% power; power at 197 pairs is 75.487831%.

These are synthetic or analytic methodological results, not human EEG findings.

## Figures and package integrity

- Nine readable PNG/PDF figure pairs are present, plus the Figure 7 JSON data and the 1536 × 1024 cover PNG.
- Figure 7 values match the executed benchmark.
- The repository contains 45 files including `SHA256SUMS.txt`, `LICENSE.md`, and the low-maintenance GitHub Actions verification workflow.
- The manifest covers every candidate file except itself, and every listed digest matches.
- Every archived file is byte-identical to its candidate-directory counterpart; ZIP integrity and exact file coverage pass.
- Third-party source PDFs, raw independent-audit material, private review folders, temporary render files, symbolic links, and private absolute paths are excluded.

## Manuscript SHA-256 hashes

```text
PDF   78b3d662bf8e5d78a859e6cef648773e1aebb8cddd74838796b50da25fcce085
DOCX  608fc1e0674cf2449e0331e150efd2047586c6990879e5698efd93c23939ac26
MD    211f186a0bf7803c196006e5480a1ccfce9f833635daed280bbea6f73e1ead13
```

The complete file-level manifest is `SHA256SUMS.txt`.

## External release decisions

Technical verification does not establish the historical claim, replace missing raw EEG or uninspected sources, or constitute journal peer review. The author confirmed the byline and metadata and selected CC BY 4.0 for the manuscript, figures, cover, documentation, and synthetic outputs, plus the MIT License for original code. No DOI is printed in this package; Zenodo supplies the genuine identifier upon publication.

**At verification time, the GitHub package was public and the Zenodo record awaited final publication.**
