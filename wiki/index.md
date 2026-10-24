# Wiki Index

Content catalog for this wiki. The LLM updates this on every ingest. When answering a query or updating the draft, read this file first to find relevant pages.

---

## Papers

<!-- One entry per ingested source paper. Link to wiki/papers/<firstauthor-year-keyword>.md -->

- [Altrocchi et al. 2023](papers/altrocchi-2023-chronic.md) — Chronic (up to 96 h) FP + impedance assay; 13 reference compounds incl. hERG trafficking inhibitors (delayed effects), TKi, cytotoxics; tolerance-interval QC. Janssen, *Front Pharmacol*.
- [Blinova et al. 2018](papers/blinova-2018-multisite.md) — Blinded 10-site, 5-platform (4 MEA, 1 optical) CiPA study of 28 drugs in iCell2 and Cor.4U hiPSC-CMs; Fridericia ddFPDc/ddAPD90c ("not thoroughly validated for hiPSC-CMs"); logistic models AUC 0.87/0.83; QC criteria; source dataset of Pramudito 2026. Context (2018). *Cell Rep* 24(13):3582–3592.
- [Botti et al. 2026](papers/botti-2026-insilico.md) — 2D bidomain model of a six-well MEA with ventricular-like and atrial-like hiPSC-CM ionic models (30 % atrial-like standard); simulates activation, repolarization, conduction velocity, two Brugada cases and four blockers, compared qualitatively with published MEA data (no new experiments). *J Physiol* 604(19):8141–8166.
- [Clements et al. 2025](papers/clements-2025-aims-poster.md) — ISSCR 2025 poster of Axion's proposed AIMS \#CM01 acceptance standard for spontaneous-beating hiPSC-ventricular-CM MEA assays (spike ≥ 0.5 mV, synchrony, beat period 750–3000 ms, FPDc 200–700 ms with Fridericia). Grey literature, vendor proposal.
- [Correia et al. 2024](papers/correia-2024-acc2.md) — ACC2-inhibitor maturation medium improves metabolic/electrophysiological/structural maturity (patch-clamp, not MEA); in vitro-to-in vivo BCKDK-inhibitor PK/PD correlation achieved only in matured cells. AstraZeneca, *Cells* 13:1339.
- [Dunham et al. 2022](papers/dunham-2022-cardiopyemea.md) — Cardio PyMEA open-source Python tool: beat detection, LAT mapping, CV, FPD, power-law stats. UCLA, *PLOS ONE*.
- [Ernault et al. 2024](papers/ernault-2024-interpretation.md) — FP and LEAP interpretation from hiPSC-CM monolayers; T-wave biphasic morphology required for APD90 correlation; LEAP reflects spatial average APD. *Am J Physiol* 326:H800–H811.
- [Fetterman et al. 2024](papers/fetterman-2024-maturation.md) — Functional, metabolic, and transcriptional maturation of hiPSC-CMs are induced independently by different medium components; CardioExcyte96 impedance + patch-clamp AP/Nav + Seahorse OCR + RNA-seq. Northwestern, *Cell Reports* 43:114160.
- [Guerrelli et al. 2024](papers/guerrelli-2024-hipscm.md) — Temporal and spatial confounders in hiPSC-CM MEA; 22.6% beating rate drift in 20 min; outer rows 8.8 bpm faster; FPD increases 257 ms over 14 days; KCNJ2 up 27.5× over 30 days. *Am J Physiol* 327:H12–H27.
- [Hwang et al. 2023](papers/hwang-2023-spheroids.md) — 3D spheroid geometry (electrode contact area, size) is a primary FP variability source; in silico models; E-4031 IC50 8 nM. *Front Physiol* 14:1123190.
- [Ismaili et al. 2023](papers/ismaili-2023-hamburg.md) — Hamburg perspective review: hiPSC-CM If/ICa,T expression, AP heterogeneity, FPDc limitations, automated patch clamp. *Front Physiol* 14:1132165.
- [Kabanov et al. 2026](papers/kabanov-2026-cardioscripts.md) — CardioScripts/Myopyth: open-source Python for combined AFM+MEA electromechanical analysis; electromechanical coupling/decoupling; lidocaine validation. CEITEC MU, *Biomed Signal Process Control* 120:110125.
- [Lee et al. 2024](papers/lee-2024-cardiomea.md) — CardioMEA: open-source Python platform for HD-MEA data (parallel processing, SQL, web dashboard, extracellular and intracellular-like features, AutoML feature importance); FPD = R spike to T-wave peak, no FPDc; FPD tracked APD poorly in iCell recordings. ETH Zürich / UZH, *Front Physiol* 15:1472126.
- [Mäki 2023](papers/maki-2023-opinion.md) — Opinion: first positive FP peak is neighbor-cell artifact; FPD end = baseline return not repolarization peak; morphology-aware handling for pacemaker/inverted signals; DatAnalyzer. Zenodo v2.
- [Matsuda et al. 2025](papers/matsuda-2025-uhd.md) — Sony UHD-CMOS-MEA (236,880 electrodes, 13.5 µm pitch): field potential imaging (FPI), excitation origin count, propagation area, CV maps. *Toxicol Sci* 208(2):384–400.
- [Maurissen et al. 2024](papers/maurissen-2024-mutation.md) — Isogenic KCNH2 N588D (LQTS) / N588K (SQTS) compound-heterozygous mutations; 3D CTSs with mesenchymal cells required for TdP-like waveforms; FPDcF 82–323 ms across genotypes. *Sci Rep* 14:2586.
- [Park et al. 2025](papers/park-2025-cardiotoxicity.md) — Healthy vs. LQTS (KCNH2 c.453delC) hiPSC-CMs with 8 CiPA drugs; FPD20/FPDc20 metric; 10× LQTS sensitivity to E-4031. *Korean J Physiol Pharmacol* 29(2):257–269.
- [Park et al. 2026](papers/park-2026-genotype-ml.md) — ANN/RF/XGBoost on MEA FPD/FPDc/beat period/amplitude from LQTS and BrS patient lines plus normal lines, 28 drugs; AUC 0.94 for LQTS-trained ANN; quiescence coded as 100 % FPDc change; overlaps with Park 2025 (same group, probably same LQT2 line). *J Adv Res* 82:381–396.
- [Pramudito et al. 2026](papers/pramudito-2026-ensemble.md) — Stacking ensemble (RF/XGBoost/ANN → meta-classifier) on two ΔFPDc predictors from the public Blinova 2018 CiPA MEA dataset; reports AUC 1.000 on 16 held-out drugs, but resampling gives pseudo-replicates and meta-feature leakage is not excluded; ML runs on pre-computed ΔFPDc, no signal analysis. *Ann Biomed Eng* 54:1334–1344.
- [Scheurer et al. 2025](papers/scheurer-2025-optical-ai.md) — Video-based SVM/SHAP classifier stages iPSC-CM maturity from beating features (99.5% accuracy); not MEA, but cites an FPD–contraction-duration correlation linking it to MEA-observable quantities. TU Dresden, *Comput Struct Biotechnol J* 27:3719–3728.
- [Hayakawa et al. 2014](papers/hayakawa-2014-motion-fp.md) — Simultaneous video motion analysis and MEA field potentials in iCell monolayers; contraction–relaxation duration and FPD linearly related per drug (E-4031, verapamil, isoproterenol), non-arrhythmic conditions. *J Mol Cell Cardiol* 77:178–191. Pre-2022 background.
- [Välimäki et al. 2021](papers/valimaki-2021-hypoxia-video-mea.md) — Conference contribution (EUROOoCs 2021): combined electrophysiological and video-based motion analysis of hiPSC-CMs in hypoxia; record only, not read. Researcher is a co-author.
- [Vuorenpää et al. 2023](papers/vuorenpaa-2023-mps-building-blocks.md) — Review of cardiac microphysiological system building blocks (cells, matrix, stimulation, functional measurements, computational modelling); multimodal concurrent measurements give data for parameterising and validating models. *Front Physiol* 14:1213959. Two authors co-authored Välimäki 2021.
- [Weiser-Bitoun et al. 2026](papers/weiser-bitoun-2026-physiomea.md) — PhysioMEA: open-source MATLAB for cardiac organoid MEA; 1D/2D biomarker heatmaps (AMP, Slope, PPD, FPD); BRV with 45 HRV-adapted measures; Brugada Syndrome (SCN5A) validation. Technion, *J Mol Cell Cardiol* 210:137–149.

---

## Concepts

<!-- Core theoretical or conceptual ideas that recur across multiple papers. -->
<!-- Create a dedicated page only when a concept appears in 2+ papers or is central to the argument. -->

- [hiPSC-CM maturation status as a confound for MEA-derived metrics](hipsc-cm-maturation.md) — Maturation fractionates into independent functional/metabolic/transcriptional axes (Fetterman et al. 2024); maturation status gates in vitro-to-in vivo translatability (Correia et al. 2024); a validated non-MEA maturity classifier exists (Scheurer et al. 2025, video-based, 99.5% accuracy) but no MEA-native equivalent; culture-age electrophysiological drift already quantified (Guerrelli et al. 2024) but not linked to a maturity metric.

*(other candidates: FPDcF, CiPA, hERG trafficking, 3D vs 2D cultures)*

---

## Methods

<!-- Methodological approaches worth their own page — when a method appears across multiple papers. -->
<!-- Single-paper methods belong in the paper page, not here. -->

*(none yet — candidates: FPD measurement conventions, Fridericia correction, LEAP recording, tolerance intervals)*

---

## Research Gaps

<!-- Gaps, open questions, and contradictions identified across the literature. -->
<!-- This section directly feeds the contribution and introduction sections of the draft. -->

- **No MEA-derived reference values for hiPSC-CM maturation staging.** See [hiPSC-CM maturation status](hipsc-cm-maturation.md). Raised by a colleague of the researcher (2026-07-02); limits inter-study comparability and clinical translation, and any future index should be scoped to the electrophysiological axis only, since maturation compartments are independently regulated (Fetterman et al. 2024).

---

## Analyses

- [Critical assessment: Mäki 2023 claims](critical-assessment-maki-claims.md) — All four methodological claims checked against post-2022 literature. Claim 1 holds with "propagating monolayer" qualifier. Claim 2 reframed (baseline-return and T-peak measure different quantities). Claim 3 correctly states different fiducial logic is needed. Claim 4 internally validated; typographic error corrected in HTML source.

---

*Last updated: 2026-07-02*
