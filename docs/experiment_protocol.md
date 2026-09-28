# Experiment Protocol

## Default benchmark

- Dataset: scikit-learn Breast Cancer Wisconsin; no external download.
- Split: stratified 75/25 train/test, `random_state=42`.
- Preprocessing: standardization fitted on the training split only.
- Models: logistic regression, random forest, and one-hidden-layer MLP.
- Explanations: model-agnostic single-feature replacement, linear coefficient contributions for logistic regression, and a seeded random control. No global tree importance is presented as a local attribution.
- Target: class-1 probability.
- Baseline: training-set feature-wise median.
- Sample: 25 reproducibly selected test instances.
- Perturbation metrics: feature replacement by the declared median baseline; local sensitivity uses normalized random directions within radius 0.05 in standardized L2 input space.

## Report

Retain per-instance rows in `results/raw/benchmark.csv`; summarize grouped mean and standard deviation with `experiments/aggregate_results.py`. Do not interpret this small teaching benchmark as a statistically powered comparison or claim general method superiority. Predictive metrics are context, not explanation-quality scores.

## Controls and limitations

- Include the random attribution ranking as a negative control.
- Compare multiple properties; do not aggregate them into an unmotivated score.
- Perturbation and baseline sensitivity are part of the evaluated protocol.
- The benchmark is tabular and model-relative. It does not establish human comprehension, coherence, or application utility.
- Repeating a stochastic explainer across seeds and reporting paired uncertainty is recommended before scientific claims.

## Reproduction

```bash
python experiments/run_benchmark.py --config experiments/config.yaml
python experiments/aggregate_results.py
python scripts/fig_benchmark_results.py
```
