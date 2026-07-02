---
tags: [open-platform, fiducial-definition, waveform-morphology, spatial-analysis, brv]
---

# PhysioMEA: Signal processing platform for rate and rhythm analysis of multi-electrode array cardiac electrophysiological recordings

**Authors:** Weiser-Bitoun, I., Mazgaoker, S., Assayag, S., Davoodi, M., Alexandrovich, A., Yaniv, Y.  
**Year:** 2026  
**Venue:** *Journal of Molecular and Cellular Cardiology*, 210, pp. 137–149  
**File:** [[raw/weiser-bitoun-2026-physiomea.pdf]]  
**DOI:** 10.1016/j.yjmcc.2025.11.006  
**Affiliation:** Technion – Israel Institute of Technology, Israel

## Contribution

Introduces **PhysioMEA**, an open-source MATLAB platform for rate and rhythm analysis of hiPSC-CM-derived cardiac organoids on MEAs. Three main methodological contributions: (1) standardised one-dimensional biomarker algorithms (FPD, spike amplitude, peak-to-peak duration, inter-beat interval) across all recording electrodes; (2) two-dimensional spatiotemporal biomarker heatmaps showing electrode-to-electrode variability in AMP, Slope, PPD, and FPD; (3) beat rate variability (BRV) analysis with 45 measures adapted from heart rate variability (HRV) frameworks to the cardiac organoid context.

## Methodology

- **Model:** hiPSC-CM-derived cardiac organoids (~500 µm spheroids) on MEA chips
- **Platform:** Open-source MATLAB (PhysioMEA)
- **1D biomarkers:** FPD, AMP (spike amplitude), Slope (maximum dV/dt of depolarization spike), PPD (peak-to-peak duration), IBI (inter-beat interval)
- **FPD definition:** R-peak (depolarization maximum) to T-wave peak (repolarization maximum) — **NOT** baseline return; this differs from the convention advocated by Mäki (2023)
- **2D analysis:** Spatiotemporal heatmaps of AMP, Slope, PPD, FPD per electrode per beat; coefficient of variation (CV) quantifying spatial variability
- **BRV analysis:** 45 measures covering time-domain, frequency-domain, and non-linear HRV-analogues; VLF/LF/HF power decomposition
- **Validation cohort 1:** Wild-type hiPSC-CMs — 1D biomarker variability (CV) reported. 15 cardiac organoids total from 8 independent differentiation batches, split into two non-overlapping cohorts: 10 organoids for basal-state BRV/2D analysis (Figs. 3–5), 5 organoids for parasympathetic (CCh) comparison (Figs. 6–7).
- **Validation cohort 2:** Brugada Syndrome patient hiPSC-CMs (SCN5A p.S1812X variant) vs. healthy controls — **externally sourced, previously published 2D hiPSC-CM monolayer data** (not cardiac organoids), recorded on a different MEA geometry (60MEA200/30iR-Ti-gr, 200 µm inter-electrode distance) than the organoid work (100 µm). PhysioMEA was applied only for biomarker computation, not data acquisition. ~42 hiPSC-CM samples (BrS1+BrS2 combined) vs. ~30 (control lines combined) analyzed.
- **Pharmacological validation:** Parasympathetic simulation (carbachol) and sympathetic simulation (noradrenaline) effects on BRV
- **2D heatmap construction:** Per-electrode biomarker values are assembled into an XY(electrode)×Z(value) matrix; missing electrode values (excluded or inconsistent counts) are filled via a moving-average interpolation (window = 5) before rendering as a heatmap — i.e., 2D maps are partly interpolated, not purely measured, at gap locations.

## Findings

- 1D biomarkers are highly similar across electrodes within a well (CV not significantly different across wells, p > 0.209).
- 2D spatial CVs are substantial: AMP 39%, Slope 47%, PPD 23%, FPD 25% — indicating that single-electrode or averaged biomarkers mask important spatial information.
- BRV is dominated by VLF content (63.4%) with smaller LF (15.6%) and HF (21.0%) contributions; VLF dominance suggests intrinsic automaticity rather than autonomic input, consistent with immature hiPSC-CMs.
- Brugada Syndrome validation: SCN5A-mutant organoids show decreased AMP and Slope (consistent with reduced INa) and increased PPD relative to healthy controls.
- Carbachol (CCh) significantly increased mean IBI (1497±89 ms basal vs. 2003±138 ms CCh, i.e. slower beating; 134.7±8.6% of basal, p=0.019/0.016) — a clear **time-domain** BRV effect. **Frequency-domain content (VLF/LF/HF) and non-linear Poincaré measures (SD1, SD2) showed no significant difference** between basal and CCh states (correcting an earlier draft of this note, which incorrectly stated CCh increased HF power).
- At the 2D biomarker level, CCh produced significant (p<0.001) changes in a representative organoid: Slope decreased (0.13→0.07 V/s), PPD increased (6.74→8.63 ms), FPD decreased (405→355 ms) — so autonomic-like pharmacological effects are detectable spatially/2D even where whole-organoid BRV frequency content is not.

## Limitations

- FPD defined as R-to-T-peak, which underestimates repolarization duration relative to baseline-return conventions (Mäki 2023); systematic comparison between the two definitions is not provided.
- Cardiac organoids (~500 µm spheroids) are immature; BRV interpretation differs from in vivo HRV due to absent autonomic innervation.
- Platform is MATLAB-based (not Python), limiting accessibility in Python-centric workflows.
- Brugada validation uses a single patient-derived SCN5A variant, on externally sourced 2D monolayer data (different MEA geometry than the organoid platform) rather than the organoid model itself; broader genetic validation on the organoid platform is needed.
- Conduction-velocity/propagation mapping requires the organoid to be physically positioned within the electrode area; a seeding guide ring is used to enforce this alignment, which also constrains organoid size — a hardware/protocol constraint on the 2D spatial analysis, acknowledged by the authors (§4.6).
- 2D heatmaps include moving-average-interpolated values at electrodes with missing/excluded data, so spatial patterns are not purely raw per-electrode measurements.

## Relevance to our paper

Directly relevant to the review's core argument on transparent, open analysis platforms. PhysioMEA is a 2026 open-source platform joining Cardio PyMEA and CardioMEA as examples of the post-2022 shift away from vendor black-box analysis. The 2D spatiotemporal heatmaps are a methodological advance in spatial MEA analysis.

**Key tension with Mäki 2023 framework:** PhysioMEA defines FPD as R-to-T-peak (not baseline return). This is a concrete example of how fiducial definitions remain inconsistent across platforms, illustrating the ongoing standardisation gap identified in main.md.

**BRV:** Introduces BRV as a rhythm descriptor for cardiac organoids — a novel feature category beyond conventional beat-interval and FPD analysis, relevant to the multi-parameter feature set expansion discussed in the "High-throughput and longitudinal assays" section.

## See also

- [[wiki/papers/maki-2023-opinion.md]]
- [[wiki/papers/dunham-2022-cardiopyemea.md]]
- [[wiki/papers/lee-2024-cardiomea.md]]
- [[wiki/papers/ernault-2024-interpretation.md]]
- [[wiki/papers/kabanov-2026-cardioscripts.md]]
- [[wiki/papers/guerrelli-2024-hipscm.md]]
- [[wiki/papers/ismaili-2023-hamburg.md]]
