"""Generate clean conceptual figures used by the lecture slides."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "slides/figures"
OUT.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False})


def save(name):
    plt.tight_layout()
    plt.savefig(OUT / f"{name}.pdf", bbox_inches="tight")
    plt.close()


fig, ax = plt.subplots(figsize=(10, 1.7))
labels = ["Notion", "Property", "Metric", "Measurement"]
for i, label in enumerate(labels):
    ax.text(i, 0.5, label, ha="center", va="center", fontsize=14,
            bbox={"boxstyle": "square,pad=0.45", "facecolor": "#e9eef2", "edgecolor": "#687987"})
    if i < len(labels) - 1:
        ax.annotate("", xy=(i + 0.63, 0.5), xytext=(i + 0.35, 0.5), arrowprops={"arrowstyle": "->"})
ax.set(xlim=(-0.5, 3.5), ylim=(0, 1)); ax.axis("off"); save("notion_property_metric")

fig, ax = plt.subplots(figsize=(8, 2.8))
groups = {"Content": ["Correctness", "Completeness", "Consistency", "Continuity", "Contrastivity", "Covariate complexity"],
          "Presentation": ["Compactness", "Composition", "Confidence"],
          "User": ["Context", "Coherence", "Controllability"]}
for x, (group, values) in enumerate(groups.items()):
    ax.text(x, 1.0, group, ha="center", weight="bold", fontsize=12)
    ax.text(x, 0.5, "\n".join(values), ha="center", va="center", linespacing=1.5,
            bbox={"boxstyle": "square,pad=0.55", "facecolor": "#f5f6f7", "edgecolor": "#687987"})
ax.set(xlim=(-0.5, 2.5), ylim=(0, 1.25)); ax.axis("off"); save("co12_structure")

fig, axes = plt.subplots(1, 2, figsize=(8.4, 3.1), sharey=True)
axes[0].bar(["Full", "Remove top"], [0.8, 0.3], color=["#687987", "#9ba9b4"])
axes[0].set_title("Comprehensiveness\nRemove selected features")
axes[1].bar(["Full", "Keep top"], [0.8, 0.74], color=["#687987", "#9ba9b4"])
axes[1].set_title("Sufficiency\nKeep selected features")
for ax in axes:
    ax.set_ylabel("Model score (illustrative)"); ax.set_ylim(0, 1)
save("comprehensiveness_sufficiency")

fig, ax = plt.subplots(figsize=(6, 3.7))
ax.bar(["Concentrated", "Diffuse"], [0.0, np.log(5)], color=["#526a7a", "#c47742"])
ax.set_ylabel("Attribution entropy (illustrative)")
ax.set_title("Concentration is a compactness proxy, not correctness")
save("complexity_examples")

fig, ax = plt.subplots(figsize=(7, 2.4))
steps = ["Train $f_\\theta$", "Explain", "Randomize $\\theta$", "Explain again", "Compare"]
for i, label in enumerate(steps):
    ax.text(i, 0.5, label, ha="center", va="center", fontsize=10,
            bbox={"boxstyle": "square,pad=0.4", "facecolor": "#e9eef2", "edgecolor": "#687987"})
    if i < len(steps) - 1:
        ax.annotate("", xy=(i + 0.62, 0.5), xytext=(i + 0.37, 0.5), arrowprops={"arrowstyle": "->"})
ax.set(xlim=(-0.5, 4.5), ylim=(0, 1)); ax.axis("off"); save("randomization_check")

workflow = ["Who is it for?", "What claim?", "Which property?", "Which metric?", "Which protocol?", "What evidence?"]
fig, ax = plt.subplots(figsize=(9, 2.4))
for i, label in enumerate(workflow):
    ax.text(i, 0.5, label, ha="center", va="center", fontsize=9,
            bbox={"boxstyle": "square,pad=0.4", "facecolor": "#e9eef2", "edgecolor": "#687987"})
    if i < len(workflow) - 1:
        ax.annotate("", xy=(i + 0.61, 0.5), xytext=(i + 0.38, 0.5), arrowprops={"arrowstyle": "->"})
ax.set(xlim=(-0.5, 5.5), ylim=(0, 1)); ax.axis("off"); save("evaluation_workflow")
