---
tags: [type/concept, multimodal]
---

# Multimodal measurement of hiPSC-CMs in the reviewed sources

Concept page, written 2026-10-24 from the wiki paper pages. It lists where MEA or field-potential recording is combined with another measurement in the reviewed sources. The sensor-fusion and digital-twin ideas of main.md (Discussion and future outlook) are hypotheses of the author and are not on this page as findings.

| Source | Combination |
|---|---|
| [[wiki/papers/altrocchi-2023-chronic.md]] | FP with background impedance as a cytotoxicity readout (up to 96 h) |
| [[wiki/papers/lee-2024-cardiomea.md]] | extracellular signals and intracellular-like signals from electroporation through the same electrodes; FPD (R-to-T-peak) correlated minimally with APD |
| [[wiki/papers/kabanov-2026-cardioscripts.md]] | simultaneous AFM and MEA (synchronous validation on embryoid bodies only); electromechanical delay |
| [[wiki/papers/hayakawa-2014-motion-fp.md]] | simultaneous video motion analysis and MEA field potential, with traction force and Ca²⁺ imaging in separate experiments; FPD and contraction–relaxation duration linearly related per drug |
| [[wiki/papers/ryynanen-2018-single-cell-mea.md]] | MEA field potential and video-based motion analysis of the same single hPS-CM through transparent electrodes (recorded at the same time but not automatically synchronised; FPD, beating rate and beat-to-beat interval comparable between MEA and video where compared) |
| [[wiki/papers/hu-2026-tft-mea-multimodal.md]] | simultaneous field potentials and video on a transparent TFT-MEA (fetal mouse cardiomyocytes, 10 electrodes), aligned by the drug-addition timestamp; k-means labels per modality, supervised check and SHAP on spike features; called sensor fusion by the authors, but the degree of feature-level fusion is unclear |
| [[wiki/papers/lee-2026-ito-mea.md]] | hiPSC-CMs on a transparent ITO MEA: FP with bright-field morphology and baseline Ca²⁺ imaging of the same wells, plus end-point viability and sarcomere staining; reported side by side, not analysed jointly |
| [[wiki/papers/vuorenpaa-2023-mps-building-blocks.md]] | review: heart microphysiological systems can monitor several modalities concurrently; multimodal measurements give data for parameterising and validating computational models |
| [[wiki/papers/karami-2026-mea-cardiotoxicity.md]] | review: transparent TFT-MEAs that record optical, voltage and impedance signals (citing Hu et al., 2025 and 2026); impedance is sensitive to cell–electrode distance, cell morphology and viability, so it carries information on coupling as well as on the cells (our reading) |
| [[wiki/papers/scheurer-2025-optical-ai.md]] | video-only (no MEA) classification of maturation status, for contrast |

## Observation (ours)
Since 2026-11-01: Hu et al. (2026) is the one source that analyses MEA and video data of the same culture with machine learning, as a proof of concept in fetal mouse cells; see its page for the limits. In these sources the modalities are mostly analysed separately or side by side. Whether the feature-ranking module of Lee et al. (2024), which handles features from extracellular and intracellular-like signals, combines them in one model was not checked. No source discusses AI-assisted fusion of MEA with another modality as such (web searches on 2026-10-24 found none either, but they were not systematic).

## See also
- [[wiki/papers/botti-2026-insilico.md]] (forward model of the MEA and tissue)
- [[wiki/signal-separation.md]] (device and tissue contributions to the FP; the outlook's second hypothesis)
