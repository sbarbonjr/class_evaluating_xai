# PhD Class Plan — Evaluating Explainable AI: From Quality Properties to Metrics

## 0. Purpose of this document

This document is the **master specification** for creating a 1h30 PhD-level class on **XAI evaluation metrics**.

It is intended to guide an AI-based content generation agent in producing:

1. a **Beamer slide deck**;
2. a **GitHub repository** with reproducible examples;
3. **Python-generated figures** for the slides;
4. a small set of **hands-on experiments**;
5. supporting material such as references, metric tables, and optional exercises.

The class should not look like a generic AI-generated lecture. The visual and textual style must be simple, academic, restrained, and close to what a researcher would prepare manually.

The central pedagogical idea is:

> **Do not start from a metric. Start from the claim you want to make about an explanation.**

The lecture should repeatedly reinforce the hierarchy:

\[
\text{Notion} \rightarrow \text{Quality property} \rightarrow \text{Metric} \rightarrow \text{Measurement}
\]

and distinguish:

- **what explainability means conceptually**;
- **which quality property is relevant**;
- **how that property can be operationalized**;
- **what assumptions the metric introduces**;
- **how the result changes with data, model, explainer, perturbation strategy, baseline, and user context**.

---

# 1. Class title and positioning

## Recommended title

**Evaluating Explainable AI: From Quality Properties to Metrics**

### Subtitle

**What does a “good explanation” actually mean?**

Alternative title if a slightly more technical tone is desired:

**Evaluation of Explainable AI: Properties, Metrics, and Experimental Design**

The first is preferable for the lecture because it naturally motivates the discussion.

---

# 2. Learning objectives

At the end of the 1h30 session, PhD students should be able to:

1. distinguish **notions**, **properties**, **metrics**, and **measurements**;
2. identify how **data modality**, **model family**, and **explanation representation** constrain evaluation;
3. understand the three main evaluation perspectives:
   - functionally grounded;
   - human-grounded;
   - application-grounded;
4. explain the **Co-12 quality properties** and their organization into:
   - Content;
   - Presentation;
   - User;
5. explain and calculate representative metrics for:
   - correctness / faithfulness;
   - completeness;
   - consistency;
   - continuity / robustness;
   - compactness / complexity;
   - coherence;
6. identify important limitations of perturbation-based metrics;
7. explain why:
   - a faithful explanation may be difficult to understand;
   - a plausible explanation may be unfaithful;
   - different metrics measuring the same property may disagree;
8. design a defensible experimental evaluation protocol for a new XAI method;
9. use existing libraries such as Quantus / OpenXAI / BEExAI while understanding that the library API is not the scientific definition of the metric;
10. reason about XAI evaluation as a **multi-objective problem**, not a one-score leaderboard problem.

---

# 3. Central thesis of the lecture

The lecture should be organized around the following statement:

> **XAI evaluation is not the problem of selecting a metric. It is the problem of translating a scientific claim about an explanation into measurable evidence.**

Use the following chain repeatedly:

```text
Scientific goal
    ↓
Claim about explanation quality
    ↓
Quality property
    ↓
Operational metric
    ↓
Experimental protocol
    ↓
Measured evidence
    ↓
Interpretation + limitations
```

Example:

```text
Claim:
"The explanation is faithful to the predictive model."

        ↓

Property:
Correctness / Faithfulness

        ↓

Possible metrics:
Deletion AUC
Faithfulness correlation
Comprehensiveness
Infidelity

        ↓

Experimental choices:
baseline
perturbation strategy
feature grouping
normalization
number of samples
random seed

        ↓

Observed value:
0.73

        ↓

Interpretation:
Evidence of faithfulness under THIS protocol,
not a universal measure of explanation correctness.
```

---

# 4. Scientific basis of the class

The lecture should be primarily grounded in the attached papers.

The main conceptual backbone should come from:

- Nauta et al., **From Anecdotal Evidence to Quantitative Evaluation Methods: A Systematic Review on Evaluating Explainable AI**;
- Vilone & Longo, **Notions of explainability and evaluation approaches for explainable artificial intelligence**;
- Quantus;
- OpenXAI;
- BEExAI;
- XAIB;
- BenchXAI;
- the recent multi-dimensional evaluation paper for uncertainty attributions;
- the general XAI taxonomy / manifesto papers.

The class should preserve the terminology used by the papers.

Important source-derived points to preserve:

- explainability is **multi-faceted**, not binary;
- Co-12 organizes quality into **Content, Presentation, User**;
- correctness is not model predictive accuracy;
- plausibility/coherence is not the same as faithfulness;
- multiple metrics are needed for multi-dimensional evaluation;
- evaluation results can depend strongly on metric parameterization;
- current toolkits cover only subsets of explanation quality;
- quantitative metrics must be interpreted within their assumptions;
- human-centered evaluation remains necessary for several properties.

---

# 5. Recommended 90-minute schedule

| Time | Section | Main goal |
|---:|---|---|
| 0–8 min | Motivation | Why XAI evaluation is hard |
| 8–18 min | XAI landscape | Data → model → XAI method → explanation representation |
| 18–28 min | Vocabulary | Notion → Property → Metric → Measurement |
| 28–40 min | Co-12 | Content, Presentation, User |
| 40–65 min | Technical metrics | Faithfulness, completeness, robustness, consistency, compactness |
| 65–75 min | Human perspective | Coherence, context, controllability |
| 75–85 min | Benchmark experiment | Compare explainers with multiple metrics |
| 85–90 min | Final discussion | Why no single metric is enough |

Do not spend equal time on every Co-12 property.

The deeper mathematical treatment should focus on:

1. correctness / faithfulness;
2. completeness;
3. continuity / robustness;
4. consistency;
5. compactness / complexity;
6. coherence / human perspective.

The remaining properties can be presented more briefly in the Co-12 overview and final mapping table.

---

# 6. Slide-by-slide content blueprint

Target approximately **36–42 slides**.

The deck should have a natural research-seminar rhythm: some slides are conceptual, some mathematical, some visual, some discussion slides.

Avoid dense bullets on every slide.

---

## Section A — Opening and motivation

### Slide 1 — Title

**Evaluating Explainable AI**  
*From Quality Properties to Metrics*

Footer:
- PhD Program
- lecturer name
- institution
- date

No decorative AI artwork.

Use a plain white background with one subtle horizontal rule.

---

### Slide 2 — Provocation

Large text:

> **“SHAP is better than LIME.”**

Below:

**Better according to what?**

Small prompts at bottom:

- more faithful?
- more stable?
- more compact?
- more useful to humans?
- more coherent with domain knowledge?

Purpose: establish that XAI comparison is inherently multidimensional.

---

### Slide 3 — Model performance ≠ explanation quality

Show:

\[
\text{Predictive performance} \neq \text{Explanation quality}
\]

Then distinguish:

```text
Model question:
"Does f predict correctly?"

Explanation question:
"Does E correctly describe f?"
```

Mention:

Correctness / faithfulness concerns the explanation relative to the model, not the model relative to the ground truth.

---

### Slide 4 — The object we are evaluating

Show the pipeline:

\[
x \rightarrow f(x) \rightarrow E(f,x) \rightarrow e
\]

with:

- \(x\): input
- \(f\): predictive model
- \(E\): explanation method
- \(e\): produced explanation

Then add:

\[
Q(e, f, x, D, \theta_Q)
\]

where \(Q\) is an evaluation procedure.

Main message:

> We evaluate an explanation **under a protocol**, not in isolation.

---

# 7. Section B — XAI landscape and Sankey diagram

### Slide 5 — Why data type matters

Introduce common data modalities:

- tabular;
- image;
- text;
- time series / signal;
- graph.

Important message:

> The same conceptual property may require different metrics depending on the explanation representation and data structure.

Examples:

- deletion of a tabular feature;
- masking an image region;
- removing a token;
- perturbing a time interval;
- deleting a graph edge.

---

### Slide 6 — XAI landscape: Sankey diagram

Generate a Sankey-style diagram using Python.

Conceptual flow:

```text
DATA
Tabular
Image
Text
Time series / signal
Graph

        ↓

MODEL FAMILY
Linear / additive
Tree / ensemble
Neural network
Other black box

        ↓

XAI FAMILY
Feature attribution
Rule / structure
Counterfactual
Example-based
Concept-based
Localization
Textual explanation

        ↓

EXPLANATION OUTPUT
Attribution vector
Heatmap
Rule set
Graph
Counterfactual sample
Prototype / example
Concept score
Text

        ↓

EVALUATION
Content
Presentation
User
```

Important:
- do not imply every data type connects equally to every method;
- use a schematic, not empirical flow widths;
- label the figure **Conceptual map — not frequency data**.

---

### Python specification for Sankey figure

Prefer Plotly only for generation, then export to PDF/SVG if available.

If static vector export becomes inconvenient, use matplotlib + custom curved connectors.

Suggested script:

```python
# scripts/fig_xai_sankey.py

from pathlib import Path
import plotly.graph_objects as go

OUT = Path("slides/figures")
OUT.mkdir(parents=True, exist_ok=True)

labels = [
    "Tabular", "Image", "Text", "Time series", "Graph",
    "Linear / additive", "Tree / ensemble", "Neural network", "Other black box",
    "Feature attribution", "Rule / structure", "Counterfactual",
    "Example-based", "Concept-based", "Localization", "Textual explanation",
    "Attribution vector", "Heatmap", "Rules", "Graph explanation",
    "Counterfactual", "Prototype / example", "Concept score", "Text",
    "Content", "Presentation", "User"
]

# Keep widths schematic and simple.
# The purpose is structure, not quantitative frequency.
# Define only meaningful representative links.

fig = go.Figure(
    go.Sankey(
        arrangement="snap",
        node=dict(
            label=labels,
            pad=14,
            thickness=14,
            line=dict(width=0.5),
        ),
        link=dict(
            source=[...],
            target=[...],
            value=[...],
        )
    )
)

fig.update_layout(
    width=1400,
    height=720,
    margin=dict(l=10, r=10, t=20, b=10),
    font=dict(size=13)
)

fig.write_image(OUT / "xai_sankey.pdf")
fig.write_image(OUT / "xai_sankey.svg")
```

Visual requirements:
- white background;
- no gradients;
- no 3D effects;
- no neon palette;
- no icons unless absolutely necessary;
- 2–3 muted colors maximum;
- readable labels at Beamer scale.

---

# 8. Section C — Notion, property, metric, measurement

### Slide 7 — Why terminology becomes confusing

Show examples from the literature:

```text
Explainability
Interpretability
Understandability
Transparency
Faithfulness
Stability
Robustness
Comprehensibility
Actionability
```

Main message:

> The literature contains overlapping notions, partially synonymous terms, and different evaluation traditions.

---

### Slide 8 — Four levels

Central diagram:

\[
\boxed{
\text{Notion}
\rightarrow
\text{Property}
\rightarrow
\text{Metric}
\rightarrow
\text{Measurement}
}
\]

Definitions:

**Notion**  
Broad conceptual idea related to explainability.

**Property**  
A desired quality of an explanation.

**Metric**  
A formal operationalization of a property.

**Measurement**  
The observed metric value under a concrete experimental protocol.

---

### Slide 9 — Example

Use:

```text
Notion:
Explainability

Property:
Correctness / faithfulness

Metric:
Deletion AUC

Measurement:
0.31 on RandomForest + SHAP + Adult,
median baseline, k=20%, seed=42
```

Main message:

> A scalar without the protocol is incomplete scientific evidence.

---

### Slide 10 — Another example: robustness

```text
Property:
Continuity

Claim:
Similar inputs with similar predictions
should have similar explanations.

Metric:
Max-Sensitivity

Measurement:
0.14 under radius r=0.05
and L2 attribution distance
```

---

# 9. Section D — Evaluation perspectives

### Slide 11 — Three evaluation perspectives

Show three columns:

#### Functionally grounded
- no human participants;
- computational proxy;
- reproducible;
- scalable.

#### Human-grounded
- lay users;
- simplified tasks;
- tests human comprehension / usability.

#### Application-grounded
- domain experts;
- real task;
- expensive but most directly relevant.

Bottom message:

> These levels answer different questions.

---

### Slide 12 — Why functional metrics are attractive

Advantages:

- repeatable;
- cheap;
- scalable;
- suitable for automated benchmarks;
- useful for regression tests.

Limitations:

- proxies;
- perturbation assumptions;
- often explanation-type specific;
- may not measure usefulness;
- may not predict human understanding.

---

# 10. Section E — Co-12 framework

### Slide 13 — Co-12 overview

Three visually separated blocks.

#### CONTENT
- Correctness
- Completeness
- Consistency
- Continuity
- Contrastivity
- Covariate complexity

#### PRESENTATION
- Compactness
- Composition
- Confidence

#### USER
- Context
- Coherence
- Controllability

Use simple typography, no infographic-style decorations.

---

### Slide 14 — Co-12: Content

Table:

| Property | Question |
|---|---|
| Correctness | Does the explanation faithfully reflect the model? |
| Completeness | How much of the model behavior is explained? |
| Consistency | Do identical cases produce equivalent explanations? |
| Continuity | Do similar cases produce similar explanations? |
| Contrastivity | Does the explanation distinguish alternatives? |
| Covariate complexity | Are the explanatory concepts understandable? |

---

### Slide 15 — Co-12: Presentation and User

Presentation:

| Property | Question |
|---|---|
| Compactness | Is the explanation sufficiently concise? |
| Composition | Is it represented in an appropriate form? |
| Confidence | Is uncertainty/confidence properly represented? |

User:

| Property | Question |
|---|---|
| Context | Is it useful for the actual task? |
| Coherence | Does it align with domain/user knowledge? |
| Controllability | Can the user interact with the explanation? |

---

### Slide 16 — Co-12 is not a list of 12 metrics

Show:

```text
PROPERTY
Correctness
    │
    ├── Deletion
    ├── Insertion
    ├── Faithfulness correlation
    ├── Infidelity
    ├── Randomization checks
    └── White-box / synthetic checks
```

Then:

> One property may require multiple complementary metrics.

---

# 11. Section F — Correctness / Faithfulness

This should be the deepest technical part of the class.

---

### Slide 17 — Faithfulness principle

Let:

\[
a = E(f,x)
\]

where \(a_i\) represents feature importance.

If feature \(i\) is highly important, perturbing \(i\) should strongly affect:

\[
f(x)
\]

This motivates perturbation-based metrics.

---

### Slide 18 — Single deletion

Define:

\[
\Delta_i = f(x)-f(x_{\setminus i})
\]

where \(x_{\setminus i}\) is obtained by replacing feature \(i\) with a baseline.

Compare:

\[
|a_i|
\quad\text{vs}\quad
|\Delta_i|
\]

Discuss:
- signed vs absolute attribution;
- output probability vs logit;
- regression vs classification;
- feature dependencies.

---

### Slide 19 — Faithfulness correlation

Introduce:

\[
\operatorname{FC}(x)
=
\operatorname{corr}_{S}
\left(
\sum_{i\in S} a_i,
f(x)-f(x_{\setminus S})
\right)
\]

Interpretation:
- high positive correlation → attribution mass agrees with model sensitivity;
- depends on subset construction;
- depends on perturbation strategy;
- depends on baseline.

---

### Slide 20 — Deletion / MoRF curve

Sort features:

\[
|a_{(1)}| \ge |a_{(2)}| \ge \ldots \ge |a_{(d)}|
\]

Progressively delete the most relevant features.

Plot:

\[
k \mapsto f(x^{(k)})
\]

where \(x^{(k)}\) has the first \(k\) ranked features perturbed.

---

### Python figure — deletion curve

Generate a clean illustrative figure.

```python
# scripts/fig_deletion_curve.py

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

OUT = Path("slides/figures")
OUT.mkdir(parents=True, exist_ok=True)

pct = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

good = np.array([0.92, 0.78, 0.61, 0.45, 0.32, 0.24, 0.18, 0.14, 0.11, 0.09, 0.08])
weak = np.array([0.92, 0.88, 0.82, 0.77, 0.70, 0.63, 0.55, 0.45, 0.35, 0.24, 0.14])
random = np.array([0.92, 0.89, 0.86, 0.81, 0.76, 0.68, 0.60, 0.53, 0.43, 0.32, 0.18])

fig, ax = plt.subplots(figsize=(7.2, 4.2))
ax.plot(pct, good, marker="o", label="More faithful ranking")
ax.plot(pct, weak, marker="o", label="Less faithful ranking")
ax.plot(pct, random, linestyle="--", label="Random ranking")

ax.set_xlabel("Top-ranked features removed (%)")
ax.set_ylabel("Model score for original class")
ax.set_xlim(0, 100)
ax.set_ylim(0, 1)
ax.spines[["top", "right"]].set_visible(False)
ax.legend(frameon=False)
fig.tight_layout()
fig.savefig(OUT / "deletion_curve.pdf", bbox_inches="tight")
fig.savefig(OUT / "deletion_curve.png", dpi=220, bbox_inches="tight")
```

Note:
Illustrative data must be explicitly labeled as **illustrative** in the slide caption.

---

### Slide 21 — AOPC / Deletion AUC

Explain:

\[
AUC_{\text{del}}
=
\int_0^1 f(x^{(\alpha)})\,d\alpha
\]

or discrete approximation.

Then introduce average output drop:

\[
AOPC
=
\frac{1}{K}
\sum_{k=1}^{K}
\left[
f(x)-f(x^{(k)})
\right]
\]

Clarify direction:
- depending on formulation, lower deletion AUC can be better;
- higher AOPC can be better.

Important:
always define direction in slide and code.

---

### Slide 22 — Comprehensiveness

For selected important set \(S\):

\[
\mathrm{Comp}(x,S)
=
f(x)-f(x_{\setminus S})
\]

Question:

> What happens when the features identified as important are removed?

High drop generally indicates that the selected features matter.

---

### Slide 23 — Sufficiency

Keep only selected features:

\[
\mathrm{Suff}(x,S)
=
f(x)-f(x_S)
\]

Question:

> Are the selected features sufficient to preserve the prediction?

Small difference is generally preferable.

Show the complementarity:

```text
Comprehensiveness:
REMOVE explanation features.

Sufficiency:
KEEP explanation features.
```

---

### Slide 24 — Infidelity

Introduce conceptually:

\[
\operatorname{Infid}(E,f,x)
=
\mathbb{E}_I
\left[
\left(
I^\top E(f,x)
-
(f(x)-f(x-I))
\right)^2
\right]
\]

Explain:
- compares attribution-predicted output change with actual output change;
- result depends on perturbation distribution \(I\);
- lower is better.

No need for proof.

---

# 12. The perturbation problem

### Slide 25 — The hidden variable: baseline

Show:

```text
Feature:
Age = 63

Possible "removal":
0
mean = 48.2
median = 47
sample from conditional distribution
```

Question:

> Which one represents “feature absence”?

Main message:

> Feature deletion is not a natural operation for many data domains.

---

### Slide 26 — Out-of-distribution perturbation

Show two clouds of points in 2D.

Original data distribution: elliptical cloud.

Original point \(x\): inside cloud.

Perturbed point \(x'\): outside cloud.

Then:

\[
x' \not\sim p_{\text{data}}(X)
\]

Main question:

> Are we measuring the explanation or the model's extrapolation behavior?

---

### Python code — OOD perturbation figure

```python
# scripts/fig_ood_perturbation.py

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

rng = np.random.default_rng(42)

mean = np.array([0.0, 0.0])
cov = np.array([[1.0, 0.8], [0.8, 1.0]])
X = rng.multivariate_normal(mean, cov, size=300)

x = np.array([0.7, 0.6])
x_zero = np.array([0.0, 0.6])
x_extreme = np.array([-2.4, 0.6])

fig, ax = plt.subplots(figsize=(6.4, 4.8))
ax.scatter(X[:, 0], X[:, 1], s=14, alpha=0.35, label="Observed data")
ax.scatter(*x, s=70, marker="o", label="Original instance")
ax.scatter(*x_zero, s=70, marker="s", label="Baseline replacement")
ax.scatter(*x_extreme, s=70, marker="x", label="OOD perturbation")

ax.set_xlabel("$x_1$")
ax.set_ylabel("$x_2$")
ax.spines[["top", "right"]].set_visible(False)
ax.legend(frameon=False)
fig.tight_layout()
fig.savefig("slides/figures/ood_perturbation.pdf", bbox_inches="tight")
```

---

# 13. Correctness vs completeness

### Slide 27 — Nothing but the truth / the whole truth

Two axes:

```text
                 Completeness
                      ↑
                      |
      concise but     |     complete and
      incomplete      |     faithful
                      |
----------------------+--------------→ Correctness
                      |
      misleading      |     verbose but
                      |     partly faithful
```

Use this to introduce the fact that properties may conflict.

---

# 14. Consistency and continuity

### Slide 28 — Consistency

Definition:

> Equivalent input/model conditions should produce equivalent explanations.

Possible tests:
- repeated explanation with different seeds;
- implementation invariance;
- repeated runs;
- model-equivalent implementations.

Important distinction:
consistency is not continuity.

---

### Slide 29 — Continuity

Given:

\[
x' = x + \delta
\]

with:

\[
f(x') \approx f(x),
\]

we expect:

\[
E(f,x') \approx E(f,x).
\]

This is the conceptual basis of explanation stability.

---

### Slide 30 — Max-Sensitivity

\[
\mathrm{Sens}_{\max}
=
\max_{\|x'-x\|\le r}
\|E(f,x)-E(f,x')\|
\]

Discuss:
- perturbation radius \(r\);
- input norm;
- attribution distance;
- preserving model decision;
- valid vs invalid perturbations.

---

### Python figure — robustness neighborhood

Create a simple 2D diagram.

```python
# scripts/fig_robustness_neighborhood.py

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

fig, ax = plt.subplots(figsize=(5.8, 5.2))

x = np.array([0.0, 0.0])
circle = Circle(x, 1.0, fill=False, linestyle="--")
ax.add_patch(circle)

pts = np.array([
    [0.2, 0.1],
    [-0.3, 0.4],
    [0.5, -0.2],
    [-0.5, -0.25],
])

ax.scatter([0], [0], s=90, label="$x$")
ax.scatter(pts[:, 0], pts[:, 1], s=50, label="Perturbations $x'$")

for p in pts:
    ax.plot([0, p[0]], [0, p[1]], linewidth=0.8)

ax.set_xlim(-1.3, 1.3)
ax.set_ylim(-1.3, 1.3)
ax.set_aspect("equal")
ax.set_xlabel("Feature 1")
ax.set_ylabel("Feature 2")
ax.spines[["top", "right"]].set_visible(False)
ax.legend(frameon=False)
fig.tight_layout()
fig.savefig("slides/figures/robustness_neighborhood.pdf", bbox_inches="tight")
```

---

# 15. Compactness and complexity

### Slide 31 — Two explanations

Show:

\[
a=
[0.91,0.04,0.03,0.01,0.01]
\]

versus:

\[
b=
[0.21,0.20,0.20,0.20,0.19]
\]

Ask:

> Which one is easier to inspect?

Then:

> Does easier necessarily mean more faithful?

---

### Slide 32 — Entropy-based complexity

Normalize:

\[
p_i = \frac{|a_i|}{\sum_j |a_j|}
\]

Then:

\[
H(a)
=
-\sum_i p_i \log p_i
\]

Interpretation:
- concentrated attribution → lower entropy;
- diffuse attribution → higher entropy.

---

### Slide 33 — Sparsity / Gini

Explain conceptually:
- high concentration on few variables;
- low concentration when importance is evenly distributed.

No need for a long derivation unless desired.

Optional formula:

\[
G(v)
=
1
-
2
\sum_{k=1}^{d}
\frac{v_k}{\|v\|_1}
\left(
\frac{d-k+0.5}{d}
\right)
\]

where \(v\) is non-negative and sorted.

---

# 16. Randomization and sanity checks

### Slide 34 — Model parameter randomization

Procedure:

```text
Train model fθ
      ↓
Compute E(fθ, x)
      ↓
Randomize θ
      ↓
Compute E(fθ_random, x)
      ↓
Compare explanations
```

If explanation barely changes, that is suspicious.

Important scientific point:

> Passing a sanity check is necessary evidence, not proof of correctness.

---

### Slide 35 — Synthetic / white-box checks

Two strategies:

#### White-box check
Use a model whose reasoning is known or directly interpretable.

#### Controlled synthetic data
Construct data with known relevant variables.

Compare explanation with known "gold" structure.

Discuss limitation:
synthetic ground truth may not capture complexity of real-world data.

---

# 17. Presentation and human perspective

### Slide 36 — Faithfulness is not usefulness

Large equation:

\[
\text{Faithful}
\not\Rightarrow
\text{Understandable}
\]

Example:
- explanation with 120 exact predicates;
- technically faithful;
- practically unusable.

---

### Slide 37 — Coherence is not faithfulness

Large equation:

\[
\text{Plausible}
\not\Rightarrow
\text{Faithful}
\]

Example:

> “Age and smoking increase cardiovascular risk.”

A physician may find this coherent.

But the model may actually rely on a spurious variable.

Then:

\[
\text{Coherence with human knowledge}
\neq
\text{Correctness relative to model}
\]

---

### Slide 38 — Human-grounded evaluation

Possible tasks:
- predict model output;
- detect model failure;
- identify influential variables;
- compare two explanations;
- answer comprehension questions;
- estimate decision time;
- measure confidence calibration.

Important:
avoid only asking:
> “Which explanation do you prefer?”

Preference alone is not sufficient evidence.

---

### Slide 39 — Application-grounded evaluation

Examples:

Physician:
- does explanation improve diagnosis or error detection?

Engineer:
- does it help debug the model?

Auditor:
- does it reveal unacceptable dependencies?

Regulator:
- can the explanation support an accountability task?

Domain scientist:
- does it generate useful hypotheses?

---

# 18. Benchmark section

### Slide 40 — A minimal benchmark

Dataset:
- Breast Cancer Wisconsin or Adult.

Models:
- Logistic Regression;
- Random Forest;
- MLP.

Explainers:
- SHAP;
- LIME;
- permutation importance / local perturbation;
- random attribution as negative control.

Metrics:
- faithfulness correlation;
- deletion AUC;
- comprehensiveness;
- sufficiency;
- max-sensitivity;
- sparsity.

---

### Slide 41 — Why include a random explanation?

Because a benchmark without controls may produce scores without context.

Controls:
- random feature ranking;
- random attribution vector;
- model randomization;
- label randomization where appropriate.

Main message:

> An evaluation protocol should be capable of rejecting obviously bad explanations.

---

### Slide 42 — Results matrix

Use a matrix, not only a radar chart.

Example layout:

| Method | Faith. Corr. ↑ | Del. AUC ↓ | Comp. ↑ | Suff. ↓ | Sens. ↓ | Sparse ↑ |
|---|---:|---:|---:|---:|---:|---:|
| SHAP | ... | ... | ... | ... | ... | ... |
| LIME | ... | ... | ... | ... | ... | ... |
| Permutation | ... | ... | ... | ... | ... | ... |
| Random | ... | ... | ... | ... | ... | ... |

Do not hard-code fabricated values in the final lecture.

The agent should compute them from the notebook.

---

### Slide 43 — Metric disagreement

Show a rank comparison.

Example conceptual table:

```text
             Faithfulness   Robustness   Compactness
Method A          1              3              2
Method B          2              1              3
Method C          3              2              1
```

Question:

> Which method is best?

Answer:

> There is no answer without a defined evaluation objective.

---

### Slide 44 — Multi-objective view

Use a 2D Pareto plot:

x-axis:
Faithfulness

y-axis:
Robustness

point size:
Complexity or explanation size

Show that different methods may lie on a Pareto frontier.

Do not aggregate immediately to one score.

---

### Python figure — Pareto plot

```python
# scripts/fig_pareto_xai.py

import matplotlib.pyplot as plt

methods = ["A", "B", "C", "D"]
faith = [0.82, 0.74, 0.68, 0.51]
robust = [0.52, 0.76, 0.61, 0.42]
size = [60, 95, 45, 30]

fig, ax = plt.subplots(figsize=(6.2, 4.6))
ax.scatter(faith, robust, s=size)

for x, y, m in zip(faith, robust, methods):
    ax.annotate(m, (x, y), xytext=(5, 4), textcoords="offset points")

ax.set_xlabel("Faithfulness")
ax.set_ylabel("Robustness")
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
fig.savefig("slides/figures/pareto_xai.pdf", bbox_inches="tight")
```

Label clearly:
**Illustrative multi-objective example**.

---

# 19. Final slides

### Slide 45 — Evaluation workflow

Show:

```text
1. Who is the explanation for?
           ↓
2. What question should it answer?
           ↓
3. What explanation representation is produced?
           ↓
4. Which quality properties matter?
           ↓
5. Which metrics operationalize them?
           ↓
6. Which assumptions do these metrics make?
           ↓
7. Which controls and baselines are required?
           ↓
8. Do multiple metrics agree?
           ↓
9. Is human evaluation also necessary?
```

---

### Slide 46 — Final message

Large text:

> **Do not evaluate an explanation.**

Below:

> **Evaluate claims about an explanation.**

Then:

```text
"Our method is faithful."
→ faithful according to which metric?
→ under which perturbation?
→ under which baseline?
→ on which model and data?
→ compared with what control?
```

---

### Slide 47 — Take-home points

Keep to five items:

1. XAI quality is multidimensional.
2. Property and metric are not the same thing.
3. Metrics encode assumptions.
4. Technical validity and human usefulness are different questions.
5. Strong XAI evaluation requires complementary evidence.

---

# 20. Optional advanced slide: DPG as a non-attribution explanation

Use Decision Predicate Graphs only as an example that not all explanations are attribution vectors.

Purpose:

```text
Feature attribution
    → vector

Counterfactual
    → modified sample

Rule explanation
    → rules

DPG
    → graph / predicate structure
```

Then ask:

> Can the same evaluation metric be applied to all four?

Answer:
not necessarily.

Use this to reinforce representation-dependent evaluation.

Do not turn the class into a DPG-centered lecture.

---

# 21. Optional advanced slide: normalized faithfulness / NAOPC

This can be presented as an open research discussion.

Problem:

Raw perturbation-based scores may be difficult to compare across:

- models;
- datasets;
- output scales;
- explanation sparsity;
- baseline choices.

Research question:

> Can we normalize perturbation-based faithfulness relative to reference curves or controls?

Possible structure:

\[
\text{Normalized Faithfulness}
=
\frac{
S(E)-S_{\text{random}}
}{
S_{\text{ideal/reference}}-S_{\text{random}}
}
\]

Do not present this as a universally established standard unless explicitly supported by the corresponding paper.

Label it:

**Open problem / research direction**

This is a suitable bridge to future work.

---

# 22. GitHub repository specification

Recommended repository:

```text
class_evaluating_xai/
│
├── README.md
├── LICENSE
├── pyproject.toml
├── environment.yml
├── requirements.txt
│
├── slides/
│   ├── main.tex
│   ├── references.bib
│   ├── sections/
│   │   ├── 01_motivation.tex
│   │   ├── 02_xai_landscape.tex
│   │   ├── 03_notions_properties_metrics.tex
│   │   ├── 04_co12.tex
│   │   ├── 05_faithfulness.tex
│   │   ├── 06_robustness.tex
│   │   ├── 07_human_evaluation.tex
│   │   ├── 08_benchmark.tex
│   │   └── 09_takeaways.tex
│   └── figures/
│
├── notebooks/
│   ├── 01_data_models_explainers.ipynb
│   ├── 02_faithfulness_metrics.ipynb
│   ├── 03_robustness_metrics.ipynb
│   ├── 04_complexity_metrics.ipynb
│   └── 05_multi_metric_benchmark.ipynb
│
├── src/
│   └── xai_eval/
│       ├── __init__.py
│       ├── data.py
│       ├── models.py
│       ├── explainers.py
│       ├── perturbations.py
│       ├── metrics/
│       │   ├── __init__.py
│       │   ├── faithfulness.py
│       │   ├── completeness.py
│       │   ├── robustness.py
│       │   ├── complexity.py
│       │   └── controls.py
│       └── plotting.py
│
├── scripts/
│   ├── fig_xai_sankey.py
│   ├── fig_deletion_curve.py
│   ├── fig_ood_perturbation.py
│   ├── fig_robustness_neighborhood.py
│   ├── fig_metric_matrix.py
│   ├── fig_rank_disagreement.py
│   └── fig_pareto_xai.py
│
├── experiments/
│   ├── config.yaml
│   ├── run_benchmark.py
│   └── aggregate_results.py
│
├── results/
│   ├── raw/
│   ├── tables/
│   └── figures/
│
├── tests/
│   ├── test_faithfulness.py
│   ├── test_robustness.py
│   ├── test_complexity.py
│   └── test_controls.py
│
└── docs/
    ├── metric_map.md
    ├── experiment_protocol.md
    └── references.md
```

Important design principle:

> Notebooks demonstrate. `src/` implements.

Avoid burying the scientific implementation inside notebook cells.

---

# 23. Repository coding principles

The AI agent generating the code should follow these rules.

## Python

- Python 3.11+.
- type hints where useful;
- docstrings for public functions;
- deterministic seeds;
- no unnecessary class hierarchy;
- small functions;
- avoid premature abstraction;
- metric functions should expose scientific parameters explicitly.

Example:

```python
def deletion_auc(
    model,
    x,
    attribution,
    *,
    baseline,
    output_index=None,
    steps=20,
    feature_groups=None,
):
    ...
```

Bad API:

```python
metric = Metric(config)
metric.run()
```

unless a library requires it.

The educational code should make assumptions visible.

---

# 24. Manual implementations required

The repository should manually implement at least:

1. single deletion;
2. deletion curve;
3. deletion AUC / AOPC;
4. faithfulness correlation;
5. comprehensiveness;
6. sufficiency;
7. max-sensitivity;
8. entropy-based complexity;
9. sparsity / Gini;
10. random attribution control.

Then compare a subset against external libraries.

The goal is not to replace Quantus or BEExAI.

The goal is to expose what the libraries abstract away.

---

# 25. Libraries

Recommended:

```text
numpy
pandas
scipy
scikit-learn
matplotlib
shap
lime
quantus
captum              # only if a PyTorch example is included
plotly              # Sankey generation only
kaleido             # static Plotly export
jupyter
pytest
```

Optional:
- openxai;
- beexai;
- seaborn is unnecessary;
- avoid heavyweight frameworks unless needed.

---

# 26. Experimental benchmark

## Dataset

Default:

**Breast Cancer Wisconsin** from scikit-learn.

Reasons:
- small;
- no download dependency;
- numerical tabular variables;
- easy to reproduce;
- runs quickly in class.

Optional second dataset:

**Adult Income**, only if a cached/downloaded source is included.

---

## Models

Use:

```python
LogisticRegression
RandomForestClassifier
MLPClassifier
```

Purpose:

- linear baseline;
- tree ensemble;
- nonlinear neural model.

Performance does not need to be state-of-the-art.

---

## Explainers

Use approximately:

```text
SHAP
LIME
Permutation / local perturbation attribution
Random attribution control
```

For speed:
- TreeSHAP for Random Forest;
- LinearSHAP if desired for Logistic Regression;
- KernelSHAP only on a small sample.

---

# 27. Benchmark protocol

For each model:

1. train model;
2. evaluate predictive performance;
3. select \(N\) test instances;
4. compute explanation;
5. calculate all supported metrics;
6. repeat stochastic explainers across seeds;
7. aggregate mean + standard deviation;
8. compare ranks;
9. compare with random explanation control.

Recommended:

```text
N = 50 or 100 test instances
seeds = [0, 1, 2, 3, 4]
```

If runtime is excessive:

```text
N = 25
seeds = [0, 1, 2]
```

---

# 28. Metric configuration must be explicit

The experiment configuration should include:

```yaml
seed: 42

benchmark:
  n_instances: 50

deletion:
  steps: 20
  baseline: median

faithfulness_correlation:
  subset_fraction: 0.2
  n_subsets: 30
  baseline: median

comprehensiveness:
  top_fraction: 0.2
  baseline: median

sufficiency:
  top_fraction: 0.2
  baseline: median

max_sensitivity:
  radius: 0.05
  n_perturbations: 20
  norm: l2

complexity:
  use_absolute_attributions: true
```

Do not hide these in code.

---

# 29. Negative and sanity controls

Required:

## Random attribution

\[
a_i \sim U(0,1)
\]

or random permutation of a valid explanation ranking.

## Model parameter randomization

If feasible for the MLP:
- store original explanation;
- reinitialize model;
- recompute;
- compare.

## Optional label randomization

Train a model on randomized labels and check whether explanation structure changes.

---

# 30. Metric map document

Create:

`docs/metric_map.md`

with columns:

| Co-12 property | Evaluation method | Mathematical metric | Explanation types | Needs perturbation | Needs GT | Needs users | Main caveat |
|---|---|---|---|---:|---:|---:|---|
| Correctness | Deletion | Deletion AUC | Attribution / heatmap | yes | no | no | baseline/OOD |
| Correctness | Faithfulness correlation | correlation | Attribution | yes | no | no | subset design |
| Completeness | Sufficiency | output difference | Attribution | yes | no | no | baseline |
| Continuity | Max-Sensitivity | max explanation distance | many | yes | no | no | radius |
| Consistency | Implementation invariance | explanation similarity | attribution | no | no | no | equivalent models needed |
| Compactness | Sparsity | Gini / nonzero count | many | no | no | no | may reward oversimplification |
| Coherence | Domain alignment | similarity / expert score | many | no | sometimes | often | plausibility ≠ faithfulness |
| Context | task utility | task performance | any | no | no | yes | expensive |
| Controllability | feedback impact | before/after utility | interactive | no | no | yes | protocol-specific |

---

# 31. Figures to generate automatically

All scientific figures should be generated with Python and stored under:

```text
slides/figures/
```

Required figures:

1. `xai_sankey.pdf`
2. `notion_property_metric.pdf`
3. `co12_structure.pdf`
4. `deletion_curve.pdf`
5. `comprehensiveness_sufficiency.pdf`
6. `ood_perturbation.pdf`
7. `robustness_neighborhood.pdf`
8. `complexity_examples.pdf`
9. `randomization_check.pdf`
10. `benchmark_heatmap.pdf`
11. `rank_disagreement.pdf`
12. `pareto_xai.pdf`
13. `evaluation_workflow.pdf`

Avoid generated illustrations that look like marketing diagrams.

Preferred visual language:
- boxes;
- arrows;
- lines;
- simple scatter plots;
- tables;
- restrained labels.

---

# 32. Plot style

Use matplotlib defaults as a base.

Recommended helper:

```python
def setup_axes(ax):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(labelsize=10)
```

General rules:

- no gradients;
- no shadows;
- no rounded glossy boxes;
- no excessive color;
- no synthetic icons;
- no unnecessary background grids;
- no 3D;
- no “AI aesthetic”.

Use color only when it conveys meaning.

Prefer:
- black;
- dark gray;
- one muted blue;
- one muted orange when contrast is needed.

For printing and academic projection, figures must remain understandable in grayscale when possible.

---

# 33. Beamer template

Use a **simple standard Beamer theme**.

Recommended:

```latex
\documentclass[aspectratio=169]{beamer}

\usetheme{default}
\usefonttheme{professionalfonts}

\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage{amsmath,amssymb}
\usepackage{booktabs}
\usepackage{graphicx}
\usepackage{microtype}
\usepackage{mathtools}
\usepackage{hyperref}

\setbeamertemplate{navigation symbols}{}
\setbeamertemplate{footline}[frame number]

\setbeamercolor{normal text}{fg=black,bg=white}
\setbeamercolor{frametitle}{fg=black,bg=white}
\setbeamercolor{title}{fg=black}
\setbeamercolor{structure}{fg=black}

\setbeamertemplate{itemize item}{--}
\setbeamertemplate{itemize subitem}{\textbullet}
```

Optional subtle accent:

```latex
\definecolor{accent}{RGB}{45,75,105}
\setbeamercolor{structure}{fg=accent}
```

Use only one accent color.

---

# 34. Beamer design rules

The slides should look like they were made by a researcher, not a design agent.

Rules:

- white background;
- black text;
- no giant decorative title boxes;
- no emojis;
- no clipart;
- no synthetic people;
- no gradients;
- no “futuristic AI” graphics;
- no random colored rectangles behind text;
- no excessive section divider slides;
- no animations required;
- no more than 5–6 bullet lines on ordinary slides;
- equations centered;
- figure captions short;
- references small at bottom where appropriate.

Typography:

- frame title: 25–28 pt equivalent;
- body: 18–22 pt equivalent;
- captions: 12–14 pt equivalent;
- avoid text smaller than necessary.

---

# 35. Slide writing style

Avoid generic AI phrases such as:

- “In today's rapidly evolving world...”
- “Let us embark on a journey...”
- “The power of explainability...”
- “Unlocking the black box...”
- “Revolutionizing AI trust...”

Use research language:

- “We distinguish...”
- “This metric estimates...”
- “The result depends on...”
- “This evaluation tests the claim that...”
- “A limitation is...”
- “The comparison is not invariant to...”

Use short slide titles:

Good:
- `Faithfulness`
- `The perturbation problem`
- `Consistency vs continuity`
- `Metric disagreement`

Bad:
- `Exploring the Complex and Fascinating World of Faithfulness Evaluation`

---

# 36. Citation strategy in slides

Do not overload every slide with references.

Use:
- one or two small citations on relevant slides;
- one final references section.

Core references to cite explicitly:

- Nauta et al. — Co-12 / quantitative evaluation survey;
- Vilone & Longo — notions and evaluation;
- Hedström et al. — Quantus;
- Agarwal et al. — OpenXAI;
- Sithakoul et al. — BEExAI;
- Moiseev et al. — XAIB;
- relevant perturbation / infidelity / sanity-check original papers if included.

Create BibTeX entries in:

```text
slides/references.bib
```

---

# 37. README structure

`README.md` should contain:

```markdown
# Evaluating Explainable AI

PhD lecture and reproducible examples on XAI evaluation.

## Learning objectives

## Repository structure

## Installation

## Quick start

## Lecture slides

## Notebooks

## Reproducing figures

## Running benchmark

## Main metrics

## References
```

Commands:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Figure generation:

```bash
python scripts/fig_deletion_curve.py
python scripts/fig_ood_perturbation.py
...
```

Benchmark:

```bash
python experiments/run_benchmark.py
```

Slides:

```bash
cd slides
latexmk -pdf main.tex
```

---

# 38. Notebook design

Each notebook should be short and focused.

## `01_data_models_explainers.ipynb`

- load data;
- train 3 models;
- predictive performance;
- generate one explanation from each explainer;
- visually compare.

## `02_faithfulness_metrics.ipynb`

- manual single deletion;
- faithfulness correlation;
- deletion curve;
- AOPC / AUC;
- comprehensiveness;
- sufficiency;
- baseline comparison.

## `03_robustness_metrics.ipynb`

- local perturbations;
- max-sensitivity;
- repeated explainer seeds;
- consistency vs continuity.

## `04_complexity_metrics.ipynb`

- sparsity;
- entropy;
- Gini;
- compactness-faithfulness trade-off.

## `05_multi_metric_benchmark.ipynb`

- load experiment outputs;
- rank methods;
- correlation between metrics;
- heatmap;
- Pareto plot;
- discuss whether a global score is justified.

---

# 39. Important experiment: baseline sensitivity

Required teaching experiment:

For one model + explainer, calculate deletion score with:

```text
zero
mean
median
sampled baseline
```

Plot four deletion curves.

Purpose:

> Demonstrate that the same explanation can receive different scores because the evaluation protocol changed.

Suggested output:

`baseline_sensitivity.pdf`

---

# 40. Important experiment: metric disagreement

Calculate, for each method:

```text
faithfulness correlation
deletion AUC
comprehensiveness
max-sensitivity
sparsity
```

Rank the explainers per metric.

Then compute:

- Spearman rank correlation among metrics.

Plot correlation matrix.

Purpose:

> Metrics intended to characterize explanation quality need not produce identical rankings.

---

# 41. Python code for rank correlation heatmap

Use matplotlib only.

```python
import numpy as np
import matplotlib.pyplot as plt

corr = results[metric_columns].corr(method="spearman")

fig, ax = plt.subplots(figsize=(6.6, 5.4))
im = ax.imshow(corr.to_numpy(), vmin=-1, vmax=1)

ax.set_xticks(range(len(corr.columns)))
ax.set_xticklabels(corr.columns, rotation=45, ha="right")
ax.set_yticks(range(len(corr.columns)))
ax.set_yticklabels(corr.columns)

for i in range(len(corr)):
    for j in range(len(corr)):
        ax.text(j, i, f"{corr.iloc[i,j]:.2f}",
                ha="center", va="center", fontsize=9)

fig.colorbar(im, ax=ax, label="Spearman correlation")
fig.tight_layout()
fig.savefig("slides/figures/metric_correlation.pdf",
            bbox_inches="tight")
```

---

# 42. Discussion prompts for class

Insert 3–4 short discussion interruptions.

## Prompt 1

> If SHAP has better deletion AUC but worse stability than LIME, which is better?

Expected answer:
depends on the intended quality claim and application.

---

## Prompt 2

> If an explanation agrees with a physician but not with model behavior, is it a good explanation?

Expected:
high coherence, potentially low correctness.

---

## Prompt 3

> If an explanation is perfectly faithful but uses 150 variables, is it interpretable?

Expected:
faithfulness does not guarantee compactness or usability.

---

## Prompt 4

> If deletion creates out-of-distribution samples, what are we evaluating?

Expected:
possibly a mixture of explanation quality and model extrapolation behavior.

---

# 43. Optional exercise

Ask students to design an evaluation protocol for:

> “We propose a new local feature-attribution method for credit scoring.”

They must specify:

```text
Claim
Property
Metric
Baseline
Control
Dataset
Model
Statistical aggregation
Human evaluation requirement
```

Expected structure:

```text
Claim:
The method is faithful and stable.

Properties:
Correctness + continuity.

Metrics:
Deletion AUC + faithfulness correlation + max-sensitivity.

Controls:
Random ranking + SHAP/LIME.

Baselines:
Median + conditional sampling sensitivity analysis.

Human part:
Optional coherence / actionability study with domain expert.
```

---

# 44. Statistical reporting

Avoid only reporting means.

For stochastic metrics/explainers:

report:

\[
\text{mean} \pm \text{std}
\]

or median + IQR where appropriate.

If comparing methods across samples:

- paired tests where appropriate;
- bootstrap confidence intervals;
- effect sizes;
- multiple-comparison correction if many methods are compared.

Do not make statistical testing the focus of this lecture, but mention it as part of responsible evaluation.

---

# 45. Things the content-generation agent should NOT do

Do not:

- fabricate benchmark results;
- present illustrative numbers as experimental evidence;
- create figures with fake empirical precision;
- call all robustness metrics “stability” without defining the distinction;
- equate plausibility with faithfulness;
- treat Co-12 as 12 interchangeable scalar scores;
- aggregate all metrics into one score without justification;
- claim one toolkit is “the best”;
- use a visually heavy Beamer theme;
- add stock AI imagery;
- make every slide a 3-column infographic;
- use icons merely to decorate;
- produce equations without explaining assumptions.

---

# 46. Deliverables expected from the generation agent

The next agent should produce:

## A. Slide source

```text
slides/main.tex
slides/sections/*.tex
slides/references.bib
```

## B. Figure scripts

```text
scripts/*.py
```

and generated:

```text
slides/figures/*.pdf
```

## C. Educational code

```text
src/xai_eval/
```

## D. Notebooks

```text
notebooks/*.ipynb
```

## E. Experiment runner

```text
experiments/run_benchmark.py
```

## F. Documentation

```text
README.md
docs/metric_map.md
docs/experiment_protocol.md
```

## G. Tests

At least basic tests for:

- deletion;
- faithfulness correlation;
- sufficiency;
- comprehensiveness;
- max-sensitivity;
- entropy;
- random control.

---

# 47. Suggested content-generation order

The AI agent should create the project in this order:

### Phase 1 — repository scaffold

Create directories and environment files.

### Phase 2 — metric implementations

Implement the small manual metric library.

### Phase 3 — benchmark

Run a reproducible small benchmark.

### Phase 4 — plots

Generate figures from real benchmark outputs whenever possible.

### Phase 5 — Beamer

Build slides around those figures and results.

### Phase 6 — notebooks

Convert the central examples into educational notebooks.

### Phase 7 — validation

Check:

- all figures exist;
- all references compile;
- all equations match the code;
- metric direction is consistent;
- no fabricated values remain;
- slide text fits without overflow.

---

# 48. Quality-control checklist for the final class

## Scientific

- [ ] Correctness and predictive accuracy are distinguished.
- [ ] Property and metric are distinguished.
- [ ] Consistency and continuity are distinguished.
- [ ] Faithfulness and coherence are distinguished.
- [ ] Baseline dependency is discussed.
- [ ] OOD perturbation is discussed.
- [ ] Negative controls are included.
- [ ] Multiple metrics are used.
- [ ] Human evaluation is included conceptually.
- [ ] Metric disagreement is shown.

## Pedagogical

- [ ] One central example is used throughout.
- [ ] Equations are introduced gradually.
- [ ] At least three audience discussion prompts exist.
- [ ] The benchmark can run in less than ~15–20 minutes.
- [ ] The final workflow is memorable.

## Visual

- [ ] Simple white Beamer.
- [ ] No AI-art aesthetic.
- [ ] Python-generated figures.
- [ ] Figures remain readable in grayscale.
- [ ] No unnecessary colors.
- [ ] No text overflow.
- [ ] No decorative icons.

## Reproducibility

- [ ] Fixed random seeds.
- [ ] Environment documented.
- [ ] Benchmark config committed.
- [ ] Results reproducible.
- [ ] Figure scripts independent from notebook state.
- [ ] Slide figures regenerated by scripts.

---

# 49. Final pedagogical message

The class should end with:

> **Do not evaluate explanations with metrics selected by convenience.**

Instead:

> **Define the claim, identify the relevant quality property, select complementary metrics, expose their assumptions, and interpret the measurements in context.**

The final conceptual chain is:

\[
\boxed{
\text{Goal}
\rightarrow
\text{Claim}
\rightarrow
\text{Property}
\rightarrow
\text{Metric}
\rightarrow
\text{Protocol}
\rightarrow
\text{Evidence}
}
\]

This should be the intellectual structure connecting the slides, code, experiments, and discussion.

---

# 50. Minimal bibliography to include in the project

The content-generation agent should create BibTeX entries for at least the following source groups:

1. Co-12 systematic review on XAI evaluation;
2. Vilone & Longo on notions and evaluation approaches;
3. Quantus;
4. OpenXAI;
5. BEExAI;
6. XAIB;
7. BenchXAI;
8. XAI 2.0 manifesto;
9. general taxonomy of interpretable AI;
10. original papers for:
   - infidelity/sensitivity;
   - sanity checks / randomization;
   - SHAP;
   - LIME;
   - Integrated Gradients if used.

The attached papers should remain the primary conceptual source for the lecture.

---

# 51. Suggested opening and closing scripts

## Opening

> We often compare explanation methods as if “explainability” were a single measurable quantity. It is not. An explanation may be faithful but unstable, compact but incomplete, plausible but wrong, or technically correct but useless to its intended user. Today we will focus on how to turn claims about explanations into measurable evidence.

## Closing

> The most important question in XAI evaluation is not “Which metric should I use?” It is “Which claim am I trying to validate?” Only after that question is explicit does the choice of a quality property, a metric, and an experimental protocol become scientifically meaningful.
