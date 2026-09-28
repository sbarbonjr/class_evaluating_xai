"""Generate a reproducible illustration of potentially out-of-distribution replacement."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "slides/figures"
OUT.mkdir(parents=True, exist_ok=True)
rng = np.random.default_rng(42)
data = rng.multivariate_normal([0, 0], [[1, 0.8], [0.8, 1]], size=300)

fig, ax = plt.subplots(figsize=(6.4, 4.8))
ax.scatter(data[:, 0], data[:, 1], s=14, alpha=0.35, label="Observed data")
ax.scatter(0.7, 0.6, s=70, marker="o", label="Original instance")
ax.scatter(0.0, 0.6, s=70, marker="s", label="Baseline replacement")
ax.scatter(-2.4, 0.6, s=70, marker="x", label="Potential OOD perturbation")
ax.set_xlabel("Feature 1")
ax.set_ylabel("Feature 2")
ax.set_title("Illustrative perturbations, not empirical data")
ax.spines[["top", "right"]].set_visible(False)
ax.legend(frameon=False)
fig.tight_layout()
fig.savefig(OUT / "ood_perturbation.pdf", bbox_inches="tight")
plt.close(fig)
