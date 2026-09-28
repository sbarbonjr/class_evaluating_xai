"""Draw a schematic map of the XAI evaluation pipeline."""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "slides/figures"
OUT.mkdir(parents=True, exist_ok=True)

columns = [
    ("DATA", ["Tabular", "Image", "Text", "Time series", "Graph"]),
    ("MODEL FAMILY", ["Linear / additive", "Tree / ensemble", "Neural network", "Other black box"]),
    ("XAI FAMILY", ["Attribution", "Rules / structure", "Counterfactual", "Examples", "Concepts"]),
    ("EXPLANATION", ["Vector", "Heatmap", "Rule set", "Modified sample", "Prototype"]),
    ("EVALUATION", ["Content", "Presentation", "User"]),
]
fig, ax = plt.subplots(figsize=(13, 5.6))
ax.set_xlim(0, len(columns))
ax.set_ylim(0, 1)
ax.axis("off")
for col_index, (heading, labels) in enumerate(columns):
    ax.text(col_index + 0.5, 0.94, heading, ha="center", va="center", fontsize=10, fontweight="bold")
    y_positions = [0.78 - index * (0.62 / max(1, len(labels) - 1)) for index in range(len(labels))]
    for y_pos, label in zip(y_positions, labels):
        ax.add_patch(Rectangle((col_index + 0.08, y_pos - 0.045), 0.84, 0.09,
                               facecolor="#e9eef2", edgecolor="#687987", linewidth=0.8))
        ax.text(col_index + 0.5, y_pos, label, ha="center", va="center", fontsize=8)
    if col_index < len(columns) - 1:
        ax.add_patch(FancyArrowPatch((col_index + 0.94, 0.48), (col_index + 1.06, 0.48),
                                     arrowstyle="->", mutation_scale=12, color="#687987"))
ax.text(2.5, 0.06, "Conceptual map — not frequency data", ha="center", fontsize=10, style="italic")
fig.tight_layout()
fig.savefig(OUT / "xai_sankey.pdf", bbox_inches="tight")
plt.close(fig)
