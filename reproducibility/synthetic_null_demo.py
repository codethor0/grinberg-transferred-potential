"""Synthetic null illustration. No human EEG or historical recording used."""
import json
from pathlib import Path

import numpy as np
from scipy.stats import t

SEED = 20261025
FS, T, RUNS = 256, 128, 5000
rng = np.random.default_rng(SEED)
records = []

for low, high in ((13, 35), (4, 12)):
    freqs = np.fft.rfftfreq(T, 1 / FS)
    keep = (freqs >= low) & (freqs <= high)
    a = rng.normal(size=(RUNS, T))
    b = rng.normal(size=(RUNS, T))
    A = np.fft.rfft(a, axis=-1)
    B = np.fft.rfft(b, axis=-1)
    A *= keep
    B *= keep
    ax = np.fft.irfft(A, n=T, axis=-1)
    by = np.fft.irfft(B, n=T, axis=-1)
    ax -= ax.mean(axis=-1, keepdims=True)
    by -= by.mean(axis=-1, keepdims=True)
    ax /= np.linalg.norm(ax, axis=-1, keepdims=True)
    by /= np.linalg.norm(by, axis=-1, keepdims=True)
    r = np.sum(ax * by, axis=-1)
    with np.errstate(divide="ignore"):
        statistic = np.abs(r) * np.sqrt((T - 2) / (1 - r * r))
    naive_p = 2 * t.sf(statistic, T - 2)
    CC = np.fft.irfft(
        np.conjugate(np.fft.rfft(ax, axis=-1)) * np.fft.rfft(by, axis=-1),
        n=T,
        axis=-1,
    )
    circ_p = np.mean(np.abs(CC) >= np.abs(CC[:, 0:1]) - 1e-12, axis=-1)
    naive_rate = float(np.mean(naive_p < 0.05))
    shift_rate = float(np.mean(circ_p <= 0.05))
    records.append({
        "band_hz": [low, high],
        "naive_rejections": int(np.count_nonzero(naive_p < 0.05)),
        "circular_shift_rejections": int(np.count_nonzero(circ_p <= 0.05)),
        "naive_false_positive_rate": naive_rate,
        "circular_shift_false_positive_rate": shift_rate,
        "naive_median_p": float(np.median(naive_p)),
        "circular_shift_median_p": float(np.median(circ_p)),
    })
    print(
        f"BAND {low}-{high}Hz n={RUNS} naive_p<.05 {naive_rate:.4f} "
        f"nullshift_p<=.05 {shift_rate:.4f} "
        f"naive_median={np.median(naive_p):.4f} "
        f"shift_median={np.median(circ_p):.4f}"
    )

output = {
    "seed": SEED,
    "simulated_pairs_per_band": RUNS,
    "samples_per_recording": T,
    "sampling_rate_hz": FS,
    "nominal_alpha": 0.05,
    "results": records,
}
Path(__file__).with_name("results.json").write_text(
    json.dumps(output, indent=2) + "\n", encoding="utf-8"
)
