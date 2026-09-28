# Metric Map

Metrics answer operational questions under a specified protocol. They are not interchangeable definitions of explanation quality.

| Property | Evaluation method | Mathematical metric | Explanation types | Perturbation | Ground truth | Users | Main caveat |
|---|---|---|---|---:|---:|---:|---|
| Correctness | Deletion | Deletion AUC | Attribution / heatmap | Yes | No | No | Baseline and OOD behavior |
| Correctness | Subset agreement | Faithfulness correlation | Attribution | Yes | No | No | Subset sampling, sign, and correlation degeneracy |
| Completeness | Remove selected features | Comprehensiveness | Attribution / selected set | Yes | No | No | Baseline and selected-set size |
| Completeness | Keep selected features | Sufficiency | Attribution / selected set | Yes | No | No | Baseline and output scale |
| Continuity | Local perturbation | Max-sensitivity | Any vectorizable explanation | Yes | No | No | Radius, norms, and valid neighborhood |
| Consistency | Equivalent conditions | Explanation distance | Representation-dependent | Sometimes | No | No | Define equivalence and distance |
| Compactness | Concentration proxy | Entropy / Gini | Attribution vector | No | No | No | May reward oversimplification |
| Coherence | Domain alignment | Expert judgment / similarity | Any | No | Sometimes | Often | Plausibility is not faithfulness |
| Context | Task utility | Task performance | Any | No | No | Yes | Application-specific and costly |
| Controllability | Interaction study | Change in task utility | Interactive | No | No | Yes | Protocol- and interface-specific |

Direction conventions in this package:

- `deletion_auc`: lower is generally preferred for score-preserving outputs under the selected deletion setup.
- `aopc`, `comprehensiveness`, and positive faithfulness correlation: higher is generally preferred.
- `sufficiency`, `max_sensitivity`, and `entropy_complexity`: lower is generally preferred.
- `gini_sparsity`: higher indicates more concentrated attribution, not necessarily better explanation quality.

Always specify target output, baseline, grouping, sample set, perturbation distribution, and aggregation procedure.
