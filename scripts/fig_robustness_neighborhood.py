"""Generate a schematic input neighborhood for continuity evaluation."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "slides/figures"
OUT.mkdir(parents=True, exist_ok=True)
points = np.array([[0.2, 0.1], [-0.3, 0.4], [0.5, -0.2], [-0.5, -0.25]])
fig, ax = plt.subplots(figsize=(5.8, 5.2))
ax.add_patch(Circle((0, 0), 1, fill=False, linestyle="--", color="#687987"))
ax.scatter([0], [0], s=90, label="$x$")
ax.scatter(points[:, 0], points[:, 1], s=50, label="Perturbations $x'$")
for point in points:
    ax.plot([0, point[0]], [0, point[1]], linewidth=0.8, color="#687987")
ax.set(xlim=(-1.3, 1.3), ylim=(-1.3, 1.3), xlabel="Feature 1", ylabel="Feature 2")
ax.set_aspect("equal")
ax.spines[["top", "right"]].set_visible(False)
ax.legend(frameon=False)
fig.tight_layout()
fig.savefig(OUT / "robustness_neighborhood.pdf", bbox_inches="tight")
plt.close(fig)
