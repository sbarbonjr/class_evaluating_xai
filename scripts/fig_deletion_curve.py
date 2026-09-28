"""Generate an explicitly illustrative deletion-curve figure."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "slides/figures"
OUT.mkdir(parents=True, exist_ok=True)

percent = np.arange(0, 101, 10)
curves = {
    "More faithful ranking": [0.92, 0.78, 0.61, 0.45, 0.32, 0.24, 0.18, 0.14, 0.11, 0.09, 0.08],
    "Less faithful ranking": [0.92, 0.88, 0.82, 0.77, 0.70, 0.63, 0.55, 0.45, 0.35, 0.24, 0.14],
    "Random ranking": [0.92, 0.89, 0.86, 0.81, 0.76, 0.68, 0.60, 0.53, 0.43, 0.32, 0.18],
}

fig, ax = plt.subplots(figsize=(7.2, 4.2))
for label, values in curves.items():
    ax.plot(percent, values, marker="o", label=label)
ax.set_xlabel("Top-ranked features removed (%)")
ax.set_ylabel("Model score for original class")
ax.set_title("Illustrative deletion curves (not experimental results)")
ax.set_xlim(0, 100)
ax.set_ylim(0, 1)
ax.spines[["top", "right"]].set_visible(False)
ax.legend(frameon=False)
fig.tight_layout()
fig.savefig(OUT / "deletion_curve.pdf", bbox_inches="tight")
plt.close(fig)
