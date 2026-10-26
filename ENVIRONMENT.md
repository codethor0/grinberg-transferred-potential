# Executed environment record

The following versions were measured in the environment used for the final numerical rerun, figure generation, PDF build, and package verification on October 25, 2026.

| Component | Observed version |
|---|---|
| Operating system | macOS 27.0.1; Darwin 27.0.0 arm64 |
| Python | 3.12.15 (Clang 23.1.3 build) |
| NumPy | 2.4.4 |
| SciPy | 1.18.1 |
| Matplotlib | 3.10.9 |
| lxml | 6.1.0 |
| Pandoc | 3.12.1 |
| XeTeX | 3.141592653-2.6-0.999998, TeX Live 2026 / kpathsea 6.4.2 |
| Info-ZIP | 3.0 |

Python dependencies are pinned in `reproducibility/requirements_executed.txt`. The DOCX was validated with the bundled Kimi Word OOXML/XSD gate and rendered through doc-k for visual inspection. Those validation utilities are audit tools, not runtime dependencies of the synthetic benchmark.

The numerical benchmark is deterministic under the recorded seed and pinned numerical stack. Rejection counts must match exactly. Floating-point diagnostics such as median $p$ values can differ in their last digits across NumPy and SciPy versions. PDF layout can vary with operating-system fonts and TeX installations; Palatino, Helvetica, and `xurl` were available in the observed build environment. No claim of byte-identical PDF output across platforms is made. File hashes identify the exact candidate artifacts, while `run_all.sh` reproduces their content from source in a compatible environment.
