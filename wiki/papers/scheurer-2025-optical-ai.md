---
tags: [maturation, machine-learning]
---

# Non-invasive maturity assessment of iPSC-CMs based on optical maturity characteristics using interpretable AI

**Authors:** Fabian Scheurer, Alexander Hammer, Mario Schubert, Robert-Patrick Steiner, Oliver Gamm, Kaomei Guan, Frank Sonntag, Hagen Malberg, Martin Schmidt
**Year:** 2025
**Venue:** Computational and Structural Biotechnology Journal 27, 3719–3728
**File:** [[raw/scheurer-2025-optical-ai.pdf]] (+ [[raw/scheurer-2025-optical-ai-supplementary.docx]])
**DOI:** 10.1016/j.csbj.2025.08.024

## Contribution
An interpretable-AI (SVM + SHAP) classifier that stages iPSC-CM maturation status purely from non-invasive, video-based beating/motion analysis, achieving >99% accuracy discriminating immature (day 21) from lipid-medium-matured (day 42, MM) cultures. Applied to B27 cultures (day 42), which a previous study found less mature, the binary classifier gave a heterogeneous distribution between the two clusters (p. 8). Acquisition is non-invasive, but peaks and start/end points of contraction and relaxation were adjusted manually (p. 3). The paper's only claim about prior art is that AI had been used but not for iPSC-CM maturity assessment (p. 2).

Note: page checked against the source text on 2026-10-24; statements not supported by the paper were removed or reworded.

## Methodology
- 362 phase-contrast videos (60 fps, Hamamatsu ORCA Flash 4.0 V3, 0.65 µm/pixel) from 4 iPSC donor lines, analyzed with Maia motion-analysis software (block-matching, comparable to MUSCLEMOTION/OpenHeartWare).
- Three groups: immature (day 21, n=130), mature (day 42, lipid-supplemented maturation medium MM, n=115), intermediate (day 42, B27 medium — lower fatty-acid content, n=117).
- Balanced/stratified subsampling to 230 videos; 80/20 train–test split; 5-fold cross-validation; grid-search hyperparameter optimization.
- 10 extracted beating features: displacement, contraction time (C time), relaxation time (R time), contraction–relaxation interval, beating duration (0–1 time), contraction-rise time, relaxation-rise time, max. contraction velocity (Max C), max. relaxation velocity (Max R), spontaneous beating rate.
- Support vector machine (SVM) classifier; SHAP (Shapley Additive Explanations) for per-feature and per-sample interpretability; decision-function distance from the SVM hyperplane analyzed as a continuous maturity proxy (not just the binary class label).

## Findings
- Test-set accuracy 99.5 ± 1.1% (precision 100%, recall 98.8%, F1 99.4%); full-dataset 5-fold CV accuracy 99.1 ± 1.1% — high accuracy achieved from a comparatively small dataset (230 videos).
- SHAP: the paper is inconsistent on the number of top features. The abstract names displacement, relaxation-rise time and beating duration (0–1 time); the Results list the first six (adding Max C, R time and Max R, p. 6); the Discussion names five (displacement, relaxation-rise time, 0–1 time, Max C, R time). Contraction-rise time, contraction–relaxation interval, beating rate and contraction time had little impact.
- B27 group: the heterogeneous distribution between the immature and mature clusters indicates a lower degree of maturation; the authors suggest the SVM can distinguish multiple levels of maturity (p. 8). The less-mature status of B27 comes from the authors' earlier study, and a sample B27 culture in Fig. 6C was classified as mature.
- The Discussion notes, as background, that Hayakawa et al. simultaneously measured field potentials and motion in iPSC-CMs and observed strong correlations between FPD and contraction duration (p. 9; the paper does not state that MEA was used, but the cited Hayakawa et al. (2014) used MEA, see [[wiki/papers/hayakawa-2014-motion-fp.md]]). The authors do not use this to interpret their features; they link 0–1 time to calcium transient duration ("may correlate", p. 9).

## Limitations (authors' own)
- Absolute feature values are acquisition-setup-dependent (camera, resolution, block width, frame offset); applying the trained model elsewhere requires matching the training acquisition parameters (0.65 µm/pixel, 60 fps).
- Only 4 healthy-donor iPSC lines tested; generalization to other lines/genetic backgrounds is untested. Higher-beating-rate phenotypes (e.g. atrial-like cells) would likely need higher frame rates than used here.
- The "mature" (day 42, MM) label is relative to day-21 cells, not to adult cardiomyocytes — the authors explicitly caveat that maturation under MM is "still very limited compared to adult CMs."
- How the beating features correlate with molecular cellular properties, particularly calcium handling and electrophysiology, is left to future studies (p. 8); the hypotheses cite several earlier studies, not measurements in the same cells.
- Some mature cultures sat near the hyperplane, which the authors link to line-specific backgrounds (p. 8). The 0–1 time was missing in 33.1% of samples and was calculated from other features (p. 3). It remains unclear whether the SVM classifies iPSC-CMs from other lines correctly (p. 9).

## Relevance to our paper
Cited in main.md as an optical, video-based maturity classifier (99.5% test accuracy; hold-out of 46 videos; 5-fold cross-validation on 230 videos from four healthy lines, 2025), with generalisation to other lines untested. Our reading, not the paper's: a classifier of this kind has not, to our knowledge, been assembled from MEA field-potential features, which would need a separate literature check; the paper itself does not discuss MEA reference values, and the FPD–contraction-duration correlation it cites does not show that FPD tracks maturation.

## See also
- [[wiki/hipsc-cm-maturation.md]]
- [[wiki/papers/fetterman-2024-maturation.md]]
- [[wiki/papers/pramudito-2026-ensemble.md]]
- [[wiki/papers/guerrelli-2024-hipscm.md]]
