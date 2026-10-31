---
tags: [maturation, machine-learning, 3d]
---

# Tissue-embedded stretchable nanoelectronics reveal endothelial cell–mediated electrical maturation of human 3D cardiac microtissues

**Authors:** Zuwan Lin, Jessica C. Garbern, Ren Liu, Qiang Li, Estela Mancheño Juncosa, Hannah L.T. Elwell, Morgan Sokol, Junya Aoyama, Undine-Sophie Deumer, Emma Hsiao, Hao Sheng, Richard T. Lee, Jia Liu  
**Year:** 2023  
**Venue:** Science Advances 9(10), eade8513 (published 8 March 2023; open access, CC BY-NC 4.0)  
**File:** [[raw/lin-2023-nanoelectronics.pdf]] (+ [[raw/lin-2023-nanoelectronics-supplementary.pdf]])  
**DOI:** 10.1126/sciadv.ade8513

## Contribution
The authors record extracellular field potentials from 3D hiPSC-CM microtissues, with and without hiPSC-derived endothelial cells (hiPSC-ECs), through stretchable mesh nanoelectronics embedded in the tissue, over days 15–37 of differentiation. They apply machine-learning pseudotime trajectory inference (PHATE + Slingshot, methods from single-cell transcriptomics) to the whole recorded spike waveforms and report that hiPSC-ECs accelerate the electrical maturation of the hiPSC-CMs. Single-cell RNA sequencing of separate cocultures is used to propose mechanisms (ion channel expression, ligand–receptor pathways). The authors present the combination of tissue-embedded electronics, machine-learning analysis of high-dimensional electrical recordings and scRNA-seq as a general method "for charting of cell functional and transcriptional types and states" (p. 12).

## Methodology
- **Cells:** one iPSC line (UCSD142i-86-1, adult female donor). hiPSC-CMs by CHIR/IWP-4 differentiation (seeded on day 11); hiPSC-ECs by the Patsch et al. protocol, CD144-sorted (seeded on day 14). Flow cytometry screen of CM:EC seeding ratios (1:1 to 4:1) after 7 days of coculture; 3:1 chosen for the later experiments. Both conditions kept in StemPro-34 + VEGF (50 ng/ml) after replating (p. 12).
- **Recording device:** custom stretchable mesh nanoelectronics (SU-8 mesh, Cr/Au/Cr interconnects, Pt-black-plated Pt electrodes) released from the substrate, a Matrigel layer cured beneath it, 5 million cells per device seeded on top; the cell sheet contracts into a 3D patch around the mesh. Electrode impedance stable over 50 days in PBS (fig. S2). Recording with a BlackRock CerePlex Direct amplifier and 32-channel headstage at 30 kHz. Not an MEA plate: the authors argue that classic MEAs touch 3D microtissues only on one surface and lose contact as the tissue contracts (p. 2; table S1).
- **Time points:** days 15, 18, 23, 30 and 37 of differentiation (days 4–26 of coculture), same samples. The Methods say recordings were made "weekly" (p. 14), which does not match these intervals.
- **Features (custom MATLAB):** spikes detected at 3 SD above the mean of the smoothed trace and averaged per channel; amplitude = maximum minus minimum of the averaged spike; maximum dV/dt; minimum dV/dt (absolute value); **spike duration = time between maximum and minimum dV/dt**, i.e. the width of the depolarization spike, not the field potential duration (p. 14). Activation time delay across channels (fig. S5); table S1 gives an estimated conduction velocity of 0.01–0.23 m/s for this device. No repolarization feature, FPD, beat rate or drug test is reported.
- **Pseudotime:** all channel-averaged waveforms from both conditions and all days pooled and used directly as the features for PHATE (default parameters), the first two PHATE dimensions passed to Slingshot (default parameters), and each waveform assigned a pseudotime by its position on the curve (p. 14). Unsupervised; there is no classifier, training/test split or external maturity label.
- **scRNA-seq:** separate cocultures in 24-well plates (1 million cells/well), days 11–24 of differentiation, 10x Genomics, Seurat, Harmony, CellChat, NicheNet; data in GEO GSE210513.
- **Statistics:** two-tailed unpaired t-tests; in Fig. 3 "Each dot represents averaged features from one group of samples, n = 8. Every group has 16 channels, and every four groups of samples are cultured in one well" (Fig. 3 legend); in Fig. 2D and Fig. 4J a dot is a channel or a channel-averaged waveform.

## Findings
- **Coculture markers:** hiPSC-ECs increased the percentage of hiPSC-CMs expressing TNNI3, Kir2.1, Cx43 and CD36, dose-dependently, and their mean fluorescence intensity (Fig. 1).
- **Waveform features:** at each time point, cocultures had higher amplitude, maximum and minimum dV/dt and shorter spike duration than CMs alone (Fig. 3C–F; at day 37 also Fig. 2D); CMs next to ECs had more "mature" features than CMs far from ECs within the coculture (fig. S3). Sarcomere alignment was better in cocultures (Fig. 2E–G). Maximum activation time delay across channels decreased over development and was lower in cocultures, especially early (fig. S5).
- **Pseudotime:** amplitude and dV/dt increased and spike duration decreased along the inferred trajectory, which the authors take as validation that the trajectory follows the feature dynamics (Fig. 4C–F). CMs alone occupied the beginning to middle of the trajectory and cocultures the middle to end, with overlap; pseudotime rose from day 15 to day 37 and was higher in cocultures at each time point (Fig. 4G–L). Waveforms of one time point did not form isolated clusters but spread along the trajectory. The authors argue that single features are limiting and that pseudotime over whole waveforms "fills an important gap for quantifying cardiac electrical phenotype" (p. 12).
- **Transcriptome:** CMs in cocultures had higher ACTC1, TNNI3, SCN5A, GJA1 and HOPX and more of a CM5 subcluster (NPPA, SMPX, PRRX1, HOPX), CMs alone more of a proliferative CM4 subcluster; ion channel genes for phase 0/1 (SCN5A, KCND3, KCNA4, KCNA5) up, KCNQ1, KCNJ12, KCNJ5, CACNA1G down (fig. S9); the largest waveform difference between conditions lay in the upstroke and downstroke window right after spike initiation (fig. S9B).

## Limitations
- Authors' own: none stated as such; the Introduction notes that patch clamp is hard to apply to 3D microtissues (p. 2), and the Discussion calls for systems that include further cell types (p. 12).
- Our observations:
  - **Not MEA in the sense of this review.** Custom tissue-embedded mesh electronics in 3D microtissues, not commercial MEA plates with 2D monolayers; absolute amplitudes and slopes are not comparable with MEA-plate values.
  - **Depolarization only.** All four features describe the depolarization spike; there is no FPD or repolarization feature, so the paper says nothing about the FPD and FPDc endpoints central to our review.
  - **No external maturity reference on the same samples.** "Maturation" along the trajectory is inferred from recording day and from the direction of the features; the transcriptomic evidence comes from separate cultures in another format and time window, and there is no patch clamp, no drug response and no comparison with adult tissue. The Discussion's statement that ion channel expression "correlated with measured electrical signals" (p. 12) is a qualitative match between separate experiments, not a paired analysis.
  - **Unsupervised, one line.** The pseudotime is a relative ordering of the recordings that were pooled to build it; it gives no reference values or thresholds, and it is not tested on held-out samples, other lines or other protocols. One iPSC line, one culture medium (StemPro-34 + VEGF).
  - **Units of analysis.** The t-tests treat channels or 16-channel "groups" as observations, four groups per well; how many independent devices or differentiations underlie each condition is not clear from the text.

## Relevance to our paper
Since 2026-10-31 also cited in the 3D section and the Conclusion's third gap for the authors' argument that conventional MEAs contact a 3D microtissue only at one surface (p. 2; table S1).

Cited in main.md from 2026-10-30 (Maturation section synthesis and the Conclusion's fourth gap) as the closest step towards an FP-based maturity classifier, with the limits in point 2 (a)-(c) stated in the text.

1. **Closest existing analogue of an FP-based maturity metric.** It shows that machine learning on extracellular field-potential waveforms can order recordings along an electrical maturation trajectory and separate two culture conditions. The Conclusion of main.md says the components of an MEA-native maturity classifier exist but "have not yet been combined"; this paper is the nearest combination found in the documented search (docs/maturation-mea-search.md), so the claim must be stated more precisely.
2. **What it leaves open, i.e. the remaining gap.** (a) Standard MEA plates and 2D monolayers, the format of almost all reviewed studies; (b) repolarization features (FPD, FPDc); (c) a supervised classifier or reference values validated against an external maturity measure on the same cultures, as Scheurer et al. (2025) did for video features with labels that rest on Li et al. (2025); (d) more than one line and protocol.
3. **Methodological point for the review.** The authors argue that single extracted features are limiting and analyse whole waveforms, which links to the morphology-aware analysis theme of main.md; their "spike duration" is a depolarization width, which should not be confused with FPD if the paper is cited.

## See also
- [[wiki/hipsc-cm-maturation.md]]
- [[wiki/papers/scheurer-2025-optical-ai.md]]
- [[wiki/papers/li-2025-maturation.md]]
- [[wiki/papers/hwang-2023-spheroids.md]] — another 3D hiPSC-CM FP study
