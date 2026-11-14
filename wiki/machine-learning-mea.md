---
tags: [type/concept, machine-learning]
---

# Machine learning in the reviewed MEA and cardiomyocyte studies

Concept page, written 2026-11-14 from the wiki paper pages. It lists where machine learning is used in the sources and on what input. The author's own proposals (sensor fusion, a separated cellular signal as model input) are hypotheses in main.md, not findings, and are not repeated here.

| Source | Model | Input | Notes |
|---|---|---|---|
| [[wiki/papers/pramudito-2026-ensemble.md]] | stacking ensemble (RF, XGBoost, ANN, meta-classifier) | two ΔFPDc predictors from the public Blinova et al. (2018) CiPA dataset | TdP risk; AUC 1.000 reported on 16 held-out drugs, but resampling gives pseudo-replicates and leakage is not excluded |
| [[wiki/papers/park-2026-genotype-ml.md]] | ANN, random forest, XGBoost | MEA FPD, FPDc, beat period, amplitude from long QT, Brugada and normal lines | genotype-specific risk models; quiescence coded as 100 % FPDc change |
| [[wiki/papers/lee-2024-cardiomea.md]] | AutoML (auto-sklearn) with permutation importance | extracellular HD-MEA features | ranks the features that separate an SQT5 line from its corrected control |
| [[wiki/papers/scheurer-2025-optical-ai.md]] | SVM with SHAP | video-based beating features (no MEA) | separates immature from more mature cultures |
| [[wiki/papers/lin-2023-nanoelectronics.md]] | unsupervised pseudotime (PHATE + Slingshot) | whole channel-averaged extracellular waveforms from tissue-embedded electrodes | orders recordings along an electrical-maturation trajectory; not an MEA plate |
| [[wiki/papers/hu-2026-tft-mea-multimodal.md]] | k-means labels, supervised check, SHAP | field potential and video features on a transparent TFT-MEA | proof of concept in fetal mouse cardiomyocytes, 10 electrodes |

- **Raw signals versus extracted parameters:** the opinion paper doubts that raw MEA signals would work as model input given how much FP amplitude, frequency and shape differ between cultures, and proposes extracting parameters first ([[wiki/papers/maki-2023-opinion.md]]); Lin et al. (2023) used whole waveforms, but from tissue-embedded electrodes.
- **Small datasets:** the classifiers of Scheurer et al. (2025), Park et al. (2026) and Pramudito et al. (2026) were trained on small datasets.
- **Inputs inherit analysis choices:** ΔFPDc inputs depend on the FPD definition and the rate correction used ([[wiki/fpd-end-conventions.md]], [[wiki/fridericia-rate-correction.md]]).

## See also
- [[wiki/hipsc-cm-maturation.md]]
- [[wiki/multimodal-measurement.md]]
- [[wiki/cipa.md]]
- [[wiki/open-analysis-platforms.md]]
