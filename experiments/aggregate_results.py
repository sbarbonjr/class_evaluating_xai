"""Aggregate per-instance benchmark results into mean and standard deviation."""

import argparse
from pathlib import Path

import pandas as pd


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, nargs="?", default=Path("results/raw/benchmark.csv"))
    parser.add_argument("--output", type=Path, default=Path("results/tables/benchmark_summary.csv"))
    args = parser.parse_args()
    results = pd.read_csv(args.input)
    metrics = [
        "accuracy", "roc_auc", "deletion_auc", "faithfulness_correlation",
        "comprehensiveness", "sufficiency", "max_sensitivity",
        "entropy_complexity", "gini_sparsity",
    ]
    summary = results.groupby(["model", "explainer"])[metrics].agg(["mean", "std"])
    args.output.parent.mkdir(parents=True, exist_ok=True)
    summary.to_csv(args.output)
    print(f"Wrote summary to {args.output}")


if __name__ == "__main__":
    main()
