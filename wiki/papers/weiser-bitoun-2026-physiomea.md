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
- **Validation cohort 1:** Wild-type hiPSC-CMs — 1D biomarker variability (CV) reported
- **Validation cohort 2:** Brugada Syndrome patient hiPSC-CMs (SCN5A p.S1812X variant) vs. healthy controls
- **Pharmacological validation:** Parasympathetic simulation (carbachol) and sympathetic simulation (noradrenaline) effects on BRV

## Findings

- 1D biomarkers are highly similar across electrodes within a well (CV not significantly different across wells, p > 0.209).
- 2D spatial CVs are substantial: AMP 39%, Slope 47%, PPD 23%, FPD 25% — indicating that single-electrode or averaged biomarkers mask important spatial information.
- BRV is dominated by VLF content (63.4%) with smaller LF (15.6%) and HF (21.0%) contributions; VLF dominance suggests intrinsic automaticity rather than autonomic input, consistent with immature hiPSC-CMs.
- Brugada Syndrome validation: SCN5A-mutant organoids show decreased AMP and Slope (consistent with reduced INa) and increased PPD relative to healthy controls.
- BRV frequency content shifts with autonomic-like pharmacological stimulation (carbachol increases HF component).

## Limitations

- FPD defined as R-to-T-peak, which underestimates repolarization duration relative to baseline-return conventions (Mäki 2023); systematic comparison between the two definitions is not provided.
- Cardiac organoids (~500 µm spheroids) are immature; BRV interpretation differs from in vivo HRV due to absent autonomic innervation.
- Platform is MATLAB-based (not Python), limiting accessibility in Python-centric workflows.
- Brugada validation uses a single patient-derived SCN5A variant; broader genetic validation is needed.

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
