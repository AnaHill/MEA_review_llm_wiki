---
tags: [multimodal, video, contractility, field-potential]
---

# Image-based evaluation of contraction–relaxation kinetics of human-induced pluripotent stem cell-derived cardiomyocytes: Correlation and complementarity with extracellular electrophysiology

**Authors:** Tomohiro Hayakawa, Takeshi Kunihiro, Tomoko Ando, Seiji Kobayashi, Eriko Matsui, Hiroaki Yada, Yasunari Kanda, Junko Kurokawa, Tetsushi Furukawa  
**Year:** 2014  
**Venue:** Journal of Molecular and Cellular Cardiology 77:178–191  
**File:** [[raw/hayakawa-2014-motion-fp.pdf]]  
**DOI:** 10.1016/j.yjmcc.2014.09.010

Note: ingested 2026-10-24 from the full text (14 pages, text extraction; figures not viewed, supplementary materials not available). Open access (CC BY-NC-ND 4.0). Before 2022, so it is background in main.md (Limitations vi). Several authors are Sony employees (stated in the paper). It is the primary source of the FPD and contraction link that Scheurer et al. (2025) cite (their p. 9).

## Contribution
Combines phase-contrast high-speed video with motion vector analysis, traction force microscopy, Ca²⁺ imaging and simultaneous MEA field potential (FP) recording to characterise the contraction of hiPSC-CM monolayers and to relate the motion to the FP. The authors state that their results "indicate that the electrophysiological and functional behaviors of hiPS-CMs are quantitatively reflected in the contractile motion" and that motion gives complementary information to FP (inotropic and lusitropic effects of isoproterenol). Their highlights call it the first simultaneous measurement of motion and FP in hiPS-CMs; that priority claim is the authors' own and was not checked.

## Methodology
- **Cells:** iCell Cardiomyocytes (Cellular Dynamics International), seeded as sparse single cells (traction force, motion parameters; n = 40) or monolayers (MEA, Ca²⁺).
- **Video and motion:** phase-contrast video at 150 fps (2048 × 2048 pixels, 10× objective); block-matching motion vectors; parameters: maximum contraction speed (MCS), maximum relaxation speed (MRS), average deformation distance (ADD) and contraction–relaxation duration (CRD).
- **Simultaneous FP and motion:** MED-P515A probes (Alpha MED Sciences, 64 planar platinum-black microelectrodes, 8 × 8 grid), 20 kHz sampling, 1–1000 Hz bandwidth, at least 10 consecutive FP waveforms averaged, FPD detected with Mobius software; imaging and MEA synchronised through the MEA system's external trigger; motion evaluated in a 150 × 150 µm region next to the recording electrode.
- **Traction force microscopy** on polyacrylamide gels (12 and 50 kPa); **Ca²⁺ imaging** with Fluo-5F in a 96-well plate (recorded independently of the motion data).
- **Drugs:** tetrodotoxin (3–30 µM), E-4031 (10–100 nM), verapamil (30–270 nM), isoproterenol (0.1–10 µM), applied in increasing concentrations for 10 min each; paired t-tests, means ± SEM.

## Findings
- **Motion versus force and Ca²⁺:** ADD correlated with traction force (R = 0.737 at 12 kPa, n = 13; R = 0.595 at 50 kPa, n = 12); isoproterenol and verapamil changed Ca²⁺ transient and motion parameters in the same direction (percentages in Fig. 3; the two were recorded independently).
- **FP versus motion (non-arrhythmic conditions):** the CRD was longer than the FPD; the contraction onset followed the Na⁺ peak of the FP; the slow negative component of the FP (FPslow) coincided with contraction in hiPS-CMs but not in neonatal rat cells.
- **FPD versus CRD in drug experiments:** linear relationships for E-4031 (10–50 nM; R = 0.915, slope 1.362 FPD/CRD), verapamil (R = 0.970, slope 0.633) and isoproterenol (R = 0.943, slope 0.738), with a different slope for each drug; the authors conclude the CRD "can be a surrogate of the FPD in non-arrhythmic conditions". For TTX there were no major increases in FPD or CRD, but the delay from the FP spike onset to the Na⁺ peak correlated with the delay to contraction onset (R = 0.856).
- **EAD-like events:** 100 nM E-4031 produced EAD-like negative deflections in the FP that matched a two-step relaxation in the motion; those waveforms were excluded from the FPD–CRD correlation because the FPD could not be defined.
- **Conventions:** the paper notes that the FPD end was defined earlier either as the peak of the positive deflection or as the return of the positive deflection to baseline, that the former appears to match the upstroke of relaxation and the latter the peak of relaxation, and that determining an accurate FP end point "proved difficult". The FPD here was measured from the initial negative peak to the peak of the positive deflection (TTX section).
- **Variability:** absolute MCS and MRS varied between monolayer regions (8–15 and 4–10 µm/s), but percent-of-control values varied little.

## Limitations
Stated by the authors: the findings hold for non-arrhythmic conditions (excitation–contraction decoupling and proarrhythmic conditions were left to future work); the time resolution of the motion data (about 6 ms) is lower than that of the FP (0.05 ms); an accurate FPD is hard to determine when the waveform broadens, and the beating rate was not considered in the FPD–CRD relation (left to further study); the monolayers contain a few non-cardiac cells (about 2%) and several cardiomyocyte types.

Our observations (not from the paper): one commercial cell line (iCell) in 2D culture; the slopes differ between drugs, so the linear link holds within a drug, not as a single FPD-to-CRD conversion; the FPD is not rate-corrected; maturation is not studied.

## Relevance to our paper
Cited in main.md (1) for the link between FPD and contraction duration, as the primary source in place of the secondary citation through Scheurer et al. (2025): linear relationships across drug concentrations, with drug-specific slopes, under non-arrhythmic conditions; (2) in the future-outlook section as simultaneous MEA field potential and image-based motion recording in iCell monolayers; (3) in Limitations (vi) as pre-2022 background; (4) in the fiducial-definitions section as an independent, mechanical observation that the two FPD end points (peak of the positive deflection, return to baseline) appear to match different phases of the relaxation motion and that an accurate end point is hard to establish. The paper says nothing about maturation, so it supports the "components exist" argument about maturity classifiers only through the FPD–contraction link itself.

## See also
- [[wiki/papers/scheurer-2025-optical-ai.md]]
- [[wiki/papers/valimaki-2021-hypoxia-video-mea.md]]
- [[wiki/papers/kabanov-2026-cardioscripts.md]]
- [[wiki/papers/maki-2023-opinion.md]]
