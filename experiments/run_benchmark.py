"""Run a small download-free benchmark and save raw metric observations."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

import numpy as np
import pandas as pd
import yaml
from sklearn.metrics import accuracy_score, roc_auc_score

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from xai_eval.data import breast_cancer_split
from xai_eval.explainers import local_perturbation_attribution, model_specific_attribution
from xai_eval.metrics import (
    comprehensiveness,
    deletion_auc,
    entropy_complexity,
    faithfulness_correlation,
    gini_sparsity,
    max_sensitivity,
    random_attribution,
    sufficiency,
)
from xai_eval.models import make_models, positive_probability


def run(config_path: Path, output_path: Path) -> pd.DataFrame:
    """Run configured models, explainers, and metrics; return per-instance rows."""
    config = yaml.safe_load(config_path.read_text(encoding="utf-8"))
    seed = int(config["seed"])
    settings = config["benchmark"]
    x_train, x_test, y_train, y_test, _ = breast_cancer_split(random_state=seed)
    baseline = np.median(x_train, axis=0)
    n_instances = min(int(settings["n_instances"]), x_test.shape[0])
    rng = np.random.default_rng(seed)
    selected_rows = np.sort(rng.choice(x_test.shape[0], size=n_instances, replace=False))
    results: list[dict[str, object]] = []

    for model_name, model in make_models(random_state=seed).items():
        model.fit(x_train, y_train)
        probabilities = model.predict_proba(x_test)[:, 1]
        model_summary = {
            "accuracy": accuracy_score(y_test, model.predict(x_test)),
            "roc_auc": roc_auc_score(y_test, probabilities),
        }
        explainers = {
            "LocalPerturbation": lambda x, fitted=model: local_perturbation_attribution(
                fitted, x, baseline=baseline
            ),
            "RandomControl": lambda x, fitted=model: random_attribution(x.size, random_state=seed),
        }
        if hasattr(model, "coef_"):
            explainers["ModelSpecific"] = lambda x, fitted=model: model_specific_attribution(fitted, x)

        for row_index in selected_rows:
            x = x_test[row_index]
            score_fn = lambda candidate, fitted=model: positive_probability(fitted, candidate)
            for explainer_name, explain in explainers.items():
                attribution = np.asarray(explain(x), dtype=float)
                n_top = max(1, int(round(0.2 * x.size)))
                top_features = np.argsort(-np.abs(attribution), kind="stable")[:n_top]
                directions = rng.normal(size=(int(settings["sensitivity_perturbations"]), x.size))
                norms = np.linalg.norm(directions, axis=1, keepdims=True)
                directions /= np.maximum(norms, np.finfo(float).eps)
                perturbed = x + directions * float(settings["sensitivity_radius"])
                row = {
                    "model": model_name,
                    "explainer": explainer_name,
                    "instance": int(row_index),
                    **model_summary,
                    "deletion_auc": deletion_auc(
                        score_fn, x, attribution, baseline=baseline, steps=int(settings["deletion_steps"])
                    ),
                    "faithfulness_correlation": faithfulness_correlation(
                        score_fn,
                        x,
                        attribution,
                        baseline=baseline,
                        n_subsets=int(settings["n_subsets"]),
                        random_state=seed + int(row_index),
                    ),
                    "comprehensiveness": comprehensiveness(
                        score_fn, x, top_features, baseline=baseline
                    ),
                    "sufficiency": sufficiency(score_fn, x, top_features, baseline=baseline),
                    "max_sensitivity": (
                        np.nan
                        if explainer_name == "RandomControl"
                        else max_sensitivity(
                            explain,
                            x,
                            perturbed,
                            radius=float(settings["sensitivity_radius"]),
                        )
                    ),
                    "entropy_complexity": entropy_complexity(attribution),
                    "gini_sparsity": gini_sparsity(attribution),
                }
                results.append(row)

    frame = pd.DataFrame(results)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    frame.to_csv(output_path, index=False)
    return frame


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=ROOT / "experiments/config.yaml")
    parser.add_argument("--output", type=Path, default=ROOT / "results/raw/benchmark.csv")
    args = parser.parse_args()
    frame = run(args.config, args.output)
    print(f"Wrote {len(frame)} instance-level rows to {args.output}")
    print(frame.groupby(["model", "explainer"])[["deletion_auc", "max_sensitivity"]].mean().round(4))


if __name__ == "__main__":
    main()
