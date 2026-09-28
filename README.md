# Evaluating Explainable AI

PhD lecture and reproducible examples on evaluating XAI from quality properties to metrics.

## Learning objectives

- Distinguish notions, quality properties, metrics, protocols, and measurements.
- Interpret faithfulness, completeness, continuity, and compactness metrics with their assumptions visible.
- Separate model-relative correctness from human coherence and usefulness.
- Design a multi-metric protocol with negative controls rather than a single-score leaderboard.

## Repository structure

- `slides/`: Beamer source, references, and generated figures.
- `src/xai_eval/`: small reusable metric, data, model, and explainer functions.
- `experiments/`: YAML configuration and command-line benchmark.
- `notebooks/`: executable end-to-end benchmark notebook.
- `scripts/`: standalone conceptual and result-plot generators.
- `tests/`: deterministic unit-style checks for metric behavior.
- `docs/`: metric map and experiment protocol.

## Installation

Python 3.11 or newer is required.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Optional XAI adapters can be installed with `pip install -e '.[xai]'`. The default benchmark does not require SHAP or LIME and does not download data.

## Quick start

```bash
pytest
python experiments/run_benchmark.py
python experiments/aggregate_results.py
```

The run writes per-instance observations to `results/raw/benchmark.csv` and the aggregation script writes mean and standard deviation to `results/tables/benchmark_summary.csv`.

## Lecture slides

Generate the figures and compile the deck:

```bash
python scripts/fig_xai_sankey.py
python scripts/fig_deletion_curve.py
python scripts/fig_ood_perturbation.py
python scripts/fig_robustness_neighborhood.py
python scripts/fig_teaching_schematics.py
python scripts/fig_baseline_sensitivity.py
python scripts/fig_benchmark_results.py
cd slides
pdflatex main.tex
pdflatex main.tex
```

Benchmark-result figures require `results/raw/benchmark.csv`; generate it first using the benchmark command. `pdflatex` and the Beamer LaTeX packages must be installed on the system.

## Notebooks

`notebooks/05_implementation_pipeline.ipynb` executes the pipeline milestone by milestone and includes assertions and artifact export.

## Main metrics

The package implements deletion curves/AUC, AOPC, faithfulness correlation, comprehensiveness, sufficiency, max-sensitivity, entropy complexity, Gini sparsity, and random-attribution controls. Metric parameterization is part of the scientific claim; see [docs/metric_map.md](docs/metric_map.md) and [docs/experiment_protocol.md](docs/experiment_protocol.md).

## References

The slide bibliography is in `slides/references.bib`. Toolkit packages are optional and do not define the meaning of a metric in this project.
