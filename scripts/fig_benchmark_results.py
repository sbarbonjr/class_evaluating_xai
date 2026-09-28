"""Generate benchmark heatmap, rank disagreement, correlation, and Pareto plots."""

from pathlib import Path
import sys

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results/raw/benchmark.csv"
OUT = ROOT / "slides/figures"
OUT.mkdir(parents=True, exist_ok=True)
if not RESULTS.exists():
    raise SystemExit("Run experiments/run_benchmark.py before generating result plots.")
data = pd.read_csv(RESULTS)
metrics = ["deletion_auc", "faithfulness_correlation", "comprehensiveness",
           "sufficiency", "max_sensitivity", "entropy_complexity", "gini_sparsity"]
summary = data.groupby(["model", "explainer"])[metrics].mean()

fig, ax = plt.subplots(figsize=(11, 4.8))
scaled = summary.copy()
for column in metrics:
    values = scaled[column]
    span = values.max() - values.min()
    scaled[column] = (values - values.min()) / span if span else 0.5
im = ax.imshow(scaled.to_numpy(), aspect="auto", cmap="viridis", vmin=0, vmax=1)
ax.set_xticks(range(len(metrics)), labels=metrics, rotation=35, ha="right")
ax.set_yticks(range(len(summary)), labels=[f"{m} / {e}" for m, e in summary.index])
ax.set_title("Benchmark metrics scaled within each column (higher is not uniformly better)")
fig.colorbar(im, ax=ax, label="Column-wise normalized value")
fig.tight_layout(); fig.savefig(OUT / "benchmark_heatmap.pdf", bbox_inches="tight"); plt.close(fig)

directions = {"deletion_auc": "min", "faithfulness_correlation": "max",
              "comprehensiveness": "max", "sufficiency": "min",
              "max_sensitivity": "min", "entropy_complexity": "min", "gini_sparsity": "max"}
ranks = summary.copy()
for metric, direction in directions.items():
    ranks[metric] = summary[metric].rank(ascending=(direction == "min"), method="average")
rank_means = ranks.mean(axis=1).sort_values()
fig, ax = plt.subplots(figsize=(9, 4.4))
for index, metric in enumerate(metrics):
    order = ranks.loc[rank_means.index, metric].to_numpy()
    ax.plot(range(len(order)), order, marker="o", label=metric)
ax.set_xticks(range(len(rank_means)), [f"{m}\n{e}" for m, e in rank_means.index])
ax.set_ylabel("Rank within metric (1 is preferred)"); ax.invert_yaxis()
ax.legend(frameon=False, ncol=2, fontsize=8); ax.set_title("Method order changes with the selected property")
fig.tight_layout(); fig.savefig(OUT / "rank_disagreement.pdf", bbox_inches="tight"); plt.close(fig)

correlation = data[metrics].corr(method="spearman")
fig, ax = plt.subplots(figsize=(7.0, 5.8))
im = ax.imshow(correlation, cmap="coolwarm", vmin=-1, vmax=1)
ax.set_xticks(range(len(metrics)), labels=metrics, rotation=45, ha="right")
ax.set_yticks(range(len(metrics)), labels=metrics)
for i in range(len(metrics)):
    for j in range(len(metrics)):
        ax.text(j, i, f"{correlation.iloc[i, j]:.2f}", ha="center", va="center", fontsize=7)
fig.colorbar(im, ax=ax, label="Spearman correlation")
fig.tight_layout(); fig.savefig(OUT / "metric_correlation.pdf", bbox_inches="tight"); plt.close(fig)

pareto = summary.reset_index()
fig, ax = plt.subplots(figsize=(7, 4.8))
for model, group in pareto.groupby("model"):
    ax.scatter(group["faithfulness_correlation"], group["gini_sparsity"], label=model, s=55)
    for _, row in group.iterrows():
        ax.annotate(row["explainer"], (row["faithfulness_correlation"], row["gini_sparsity"]),
                    xytext=(4, 3), textcoords="offset points", fontsize=7)
ax.set(xlabel="Faithfulness correlation (higher preferred)", ylabel="Gini sparsity (higher preferred)")
ax.set_title("Measured benchmark trade-off; interpret with controls")
ax.legend(frameon=False)
fig.tight_layout(); fig.savefig(OUT / "pareto_xai.pdf", bbox_inches="tight"); plt.close(fig)
