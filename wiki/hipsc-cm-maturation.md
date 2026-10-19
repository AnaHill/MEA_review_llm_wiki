---
tags: [maturation, concept, research-gap]
---

# hiPSC-CM maturation status as a confound for MEA-derived metrics

## Why this matters
hiPSC-CMs are widely acknowledged to resemble fetal rather than adult cardiomyocytes (Ismaili et al. 2023): they express funny current (If) and T-type Ca²⁺ current not present in mature adult ventricular myocytes, and show heterogeneous ventricular-, atrial-, and nodal-like subtypes within the same preparation. Every MEA metric discussed elsewhere in this wiki — FPD, its rate correction, waveform morphology, conduction velocity — is measured on cells whose maturation state is rarely quantified, only assumed or loosely controlled via culture duration.

This creates two linked problems this review otherwise treats separately:
1. **Inter-study comparability.** Two labs reporting different FPDc values for the same compound may simply differ in how mature their cultures are, not in methodology.
2. **Clinical translation.** MEA endpoints are ultimately meant to stand in for adult human myocardial electrophysiology; the less mature the model, the less licensed that inference is. Correia et al. (2024) give this concrete empirical weight outside the MEA context: their ACC2-inhibitor maturation medium produced a significant in vitro-to-in vivo PK/PD correlation across 21 BCKDK-inhibitor compounds — but **only** in matured cells; standard-medium cells produced no usable correlation at all. Maturation status was the difference between a translatable and a non-translatable in vitro assay.

## What maturation is not
Fetterman et al. (2024) is the clearest demonstration that "maturation" is not one thing. Using high-throughput assays across nine culture-medium formulations, they showed that **functional (electrophysiology/EC-coupling), metabolic, and transcriptional maturation are induced largely independently** — components that improved AP kinetics and Na⁺ current density had no effect on mitochondrial respiration, and vice versa. A single scalar "maturation score" derived from any one modality — including MEA — can therefore only ever describe one compartment of maturity, not the whole phenotype.

This directly bears on the colleague-suggested idea of deriving MEA-based reference values for maturation staging: such a metric would be a legitimate and useful reference for the *electrophysiological* axis specifically, but would need to be explicitly scoped as such rather than presented as a general maturity index.

## What partial evidence already exists
- **Culture-age effects on baseline electrophysiology are already quantified in MEA terms.** Guerrelli et al. (2024) found FPD lengthens by ~257 ms and beating rate falls over days 2–14 in culture, alongside a 27.5-fold increase in KCNJ2 (I_K1) expression over 30 days — i.e., a maturation-associated electrophysiological drift that current FPDc practice does not control for or report against a maturity axis.
- **Adult reference points exist from non-MEA electrophysiology.** Ismaili et al. (2023) and Fetterman et al. (2024) both report adult/mature benchmark values (e.g. resting/maximum diastolic potential, AP upstroke velocity, APD) from patch-clamp — but these are intracellular, not extracellular FP, measurements, so they cannot be applied to MEA data without a validated conversion.
- **No validated MEA-only maturation reference values or index were found in the 2022+ literature** (scoped via PubMed/bioRxiv/Scopus web search, 2026-07-02). The closest development is an industry/consortium effort (Axion Biosystems "AIMS \#CM01", presented at ISSCR 2025) proposing minimum well-acceptance criteria for spontaneous-beating hiPSC-ventricular-CM MEA assays (beat rate, spike amplitude, FPD, syncytial synchronization) — but this targets assay quality control, not maturation staging specifically, and has not yet appeared as a peer-reviewed, citable methods paper.
- **A validated maturity classifier already exists for an adjacent, non-MEA modality.** Scheurer et al. (2025) trained an interpretable SVM/SHAP classifier on video-based beating features alone, reaching >99% accuracy staging iPSC-CM maturity (immature vs. lipid-medium-matured) and correctly resolving an intermediate condition as partially mature rather than forcing a binary call. Crucially, the paper cites prior work (Hayakawa et al.) showing MEA-derived FPD correlates strongly with contraction duration in iPSC-CMs — i.e., the literature already links an MEA-native quantity (FPD) to the same underlying maturation process this optical classifier detects, but no one has built the FPD-based equivalent of Scheurer's classifier.

## The gap
No study reviewed here proposes or validates MEA-derived reference values that stage hiPSC-CM maturation status on the electrophysiological axis specifically, in a form that would let independent labs report "how mature" their preparation was at time of recording — analogous to how FPDc lets them report "how rate-corrected" a measurement is. Given Fetterman et al. (2024)'s finding that maturation compartments are independent, any such index should be explicitly scoped to the electrophysiological/FP-observable axis rather than framed as a general maturity score. Scheurer et al. (2025) sharpens this from an absence-of-evidence gap to a concrete, addressable one: the methodology (interpretable ML on beat-derived features), the validation approach (cross-validated accuracy + SHAP), and the physiological link (FPD–contraction-duration correlation) all already exist in the literature — they simply have not been assembled into an MEA-native maturity classifier analogous to Scheurer's video-based one.

## See also
- [[wiki/papers/fetterman-2024-maturation.md]]
- [[wiki/papers/ismaili-2023-hamburg.md]]
- [[wiki/papers/guerrelli-2024-hipscm.md]]
- [[wiki/papers/correia-2024-acc2.md]]
- [[wiki/papers/scheurer-2025-optical-ai.md]]
