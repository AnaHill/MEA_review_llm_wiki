---
tags: [maturation, machine-learning, high-throughput]
---

# Non-invasive maturity assessment of iPSC-CMs based on optical maturity characteristics using interpretable AI

**Authors:** Fabian Scheurer, Alexander Hammer, Mario Schubert, Robert-Patrick Steiner, Oliver Gamm, Kaomei Guan, Frank Sonntag, Hagen Malberg, Martin Schmidt
**Year:** 2025
**Venue:** Computational and Structural Biotechnology Journal 27, 3719–3728
**File:** [[raw/scheurer-2025-optical-ai.pdf]] (+ [[raw/scheurer-2025-optical-ai-supplementary.docx]])
**DOI:** 10.1016/j.csbj.2025.08.024

## Contribution
An interpretable-AI (SVM + SHAP) classifier that stages iPSC-CM maturation status purely from non-invasive, video-based beating/motion analysis, achieving >99% accuracy discriminating immature (day 21) from lipid-medium-matured (day 42, MM) cultures — and, notably, correctly resolving an intermediate condition (day 42, B27 medium) as partially matured rather than forcing a binary call. This is the clearest existing precedent for what an MEA-derived maturation reference value/classifier would need to look like, just built on a different (optical) modality.

## Methodology
- 362 phase-contrast videos (60 fps, Hamamatsu ORCA Flash 4.0 V3, 0.65 µm/pixel) from 4 iPSC donor lines, analyzed with Maia motion-analysis software (block-matching, comparable to MUSCLEMOTION/OpenHeartWare).
- Three groups: immature (day 21, n=130), mature (day 42, lipid-supplemented maturation medium MM, n=115), intermediate (day 42, B27 medium — lower fatty-acid content, n=117).
- Balanced/stratified subsampling to 230 videos; 80/20 train–test split; 5-fold cross-validation; grid-search hyperparameter optimization.
- 10 extracted beating features: displacement, contraction time (C time), relaxation time (R time), contraction–relaxation interval, beating duration (0–1 time), contraction-rise time, relaxation-rise time, max. contraction velocity (Max C), max. relaxation velocity (Max R), spontaneous beating rate.
- Support vector machine (SVM) classifier; SHAP (Shapley Additive Explanations) for per-feature and per-sample interpretability; decision-function distance from the SVM hyperplane analyzed as a continuous maturity proxy (not just the binary class label).

## Findings
- Test-set accuracy 99.5 ± 1.1% (precision 100%, recall 98.8%, F1 99.4%); full-dataset 5-fold CV accuracy 99.1 ± 1.1% — high accuracy achieved from a comparatively small dataset (230 videos).
- SHAP identified **displacement, relaxation-rise time, beating duration (0–1 time), max. contraction velocity (Max C), and relaxation time (R time)** as the five most informative features for maturity classification; contraction-rise time, contraction–relaxation interval, and beating rate contributed little.
- Applying the trained model to the untrained intermediate (B27) group produced a heterogeneous, non-binary distribution across the immature/mature hyperplane boundary — evidence the model captures a maturity *gradient*, not just a two-class label.
- Cites Hayakawa et al. (prior literature, not yet in this wiki) reporting that MEA-derived field potential duration (FPD) and contraction duration are strongly correlated in iPSC-CMs — the paper explicitly uses this as grounds to interpret its beating-duration-related features as plausible proxies for FPD-based electrophysiological maturity, without measuring FPD itself.

## Limitations (authors' own)
- Absolute feature values are acquisition-setup-dependent (camera, resolution, block width, frame offset); applying the trained model elsewhere requires matching the training acquisition parameters (0.65 µm/pixel, 60 fps).
- Only 4 healthy-donor iPSC lines tested; generalization to other lines/genetic backgrounds is untested. Higher-beating-rate phenotypes (e.g. atrial-like cells) would likely need higher frame rates than used here.
- The "mature" (day 42, MM) label is relative to day-21 cells, not to adult cardiomyocytes — the authors explicitly caveat that maturation under MM is "still very limited compared to adult CMs."
- The mechanistic link between the winning beating features and underlying electrophysiology/Ca²⁺ handling is inferred from separate prior studies on the same medium system, not measured directly in the same cells within this study.

## Relevance to our paper
The single strongest piece of external evidence for the wiki's maturation-reference-value gap. It shows a rigorously validated (99%+ accuracy, SHAP-explained, cross-validated), non-invasive maturity classifier already exists in the 2022+ literature — just for an adjacent modality (video/optical beating dynamics) rather than MEA field potentials. Its own cited FPD–contraction-duration correlation (Hayakawa et al.) is the missing link: the literature already contains evidence that MEA-derived FPD tracks the same underlying maturation process this classifier detects optically, but no one has assembled an equivalent SVM/SHAP-style classifier from FPD or FP-morphology features directly. This sharpens the gap from "no maturation reference values exist" to the more specific and actionable "the ingredients for an MEA-native maturity classifier exist in the literature but have not been assembled."

## See also
- [[wiki/hipsc-cm-maturation.md]]
- [[wiki/papers/fetterman-2024-maturation.md]]
- [[wiki/papers/pramudito-2026-ensemble.md]]
- [[wiki/papers/guerrelli-2024-hipscm.md]]
