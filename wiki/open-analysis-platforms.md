---
tags: [type/concept, open-platform]
---

# Open analysis platforms for cardiomyocyte MEA data

Concept page, written 2026-11-14 from the wiki paper pages and the open-pipelines section of main.md. It gathers the open tools examined in the review in one place; details and caveats are on the paper pages.

| Tool | Source | Language | FPD or interval end | Notes |
|---|---|---|---|---|
| Cardio PyMEA | [[wiki/papers/dunham-2022-cardiopyemea.md]] | Python | T-wave endpoint located with a trapezoid-area algorithm | beat detection, pacemaker origin, local activation time mapping, conduction velocity; analysis presupposes the polarity of its recordings (see [[wiki/fp-polarity.md]]) |
| DatAnalyzer | [[wiki/papers/maki-2023-opinion.md]] | MATLAB | return to baseline | the author's own tool; released in 2022, method described in the opinion paper |
| CardioMEA | [[wiki/papers/lee-2024-cardiomea.md]] | Python | T-wave peak (from the R peak) | high-density MEA; extracellular and intracellular-like (electroporation) features; AutoML feature ranking; no FPDc |
| CardioScripts / Myopyth | [[wiki/papers/kabanov-2026-cardioscripts.md]] | Python | T peak (QT from the Q point to the T peak; no FPD) | combined atomic force microscopy and MEA; electromechanical delay |
| PhysioMEA | [[wiki/papers/weiser-bitoun-2026-physiomea.md]] | MATLAB (or standalone) | T-wave peak (from the R peak) | cardiac organoids; per-electrode biomarkers, 2D heatmaps, beat rate variability |

- **Earlier open tools:** MultiElec and CardioMDA existed before 2022; Lee et al. (2024) compare them with Cardio PyMEA and CardioMEA (their Table 3), which compares language, GUI and pipeline features, not FPD definitions.
- **Vendor software still in use:** Park et al. (2025) and Park et al. (2026) analysed their recordings with the vendor's Cardiac Analysis Tool ([[wiki/papers/park-2025-cardiotoxicity.md]], [[wiki/papers/park-2026-genotype-ml.md]]); no usage data exist to estimate adoption of the open tools.
- **Why it matters for the review:** the open tools state how they define the waveform landmarks, and these definitions differ; see [[wiki/fpd-end-conventions.md]] and [[wiki/critical-assessment-maki-claims.md]]. Open tools are also where machine learning enters the analysis pipeline ([[wiki/machine-learning-mea.md]]).

## See also
- [[wiki/fpd-end-conventions.md]]
- [[wiki/machine-learning-mea.md]]
- [[wiki/3d-models.md]]
