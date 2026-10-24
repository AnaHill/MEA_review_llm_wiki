---
tags: [open-platform, fiducial-definition, waveform-morphology, spatial-analysis, brv]
---

# PhysioMEA: Signal processing platform for rate and rhythm analysis of multi-electrode array cardiac electrophysiological recordings

**Authors:** Weiser-Bitoun, I., Mazgaoker, S., Assayag, S., Davoodi, M., Alexandrovich, A., Yaniv, Y.  
**Year:** 2026  
**Venue:** *Journal of Molecular and Cellular Cardiology*, 210, pp. 137–149  
**File:** [[raw/weiser-bitoun-2026-physiomea.pdf]]  
**DOI:** 10.1016/j.yjmcc.2025.11.006  
**Affiliation:** Technion – Israel Institute of Technology, Israel (the first author also at Rambam Health Care Campus)

Note: page checked against the source text on 2026-10-24; statements not supported by the paper were removed or reworded.

## Contribution

Introduces **PhysioMEA**, an open-source platform (MATLAB 2023b or standalone .exe) for rate and rhythm analysis of hiPSC-CM-derived cardiac organoids on MEAs. Three methodological contributions: (1) one-dimensional biomarker algorithms (FPD, spike amplitude, peak-to-peak duration, inter-beat interval) for selected electrodes; (2) two-dimensional spatiotemporal biomarker heatmaps showing electrode-to-electrode variability in AMP, Slope, PPD and FPD; (3) beat rate variability (BRV) analysis with 45 measures adapted from heart rate variability (HRV). The authors call it the first comprehensive BRV analysis in cardiac organoids (earlier BRV work on iPSC pacemaker cells: Ben-Ari et al. 2014, cited in §4.4).

## Methodology

- **Model:** hiPSC-CM-derived cardiac organoids on MEA chips, formed through a seeding guide ring with a 1.5 mm² hole (§2.2); hiPSC line from a 46-year-old female volunteer (§2.1)
- **1D biomarkers:** FPD, AMP (spike amplitude), Slope (maximum dV/dt of the depolarization spike), PPD (peak-to-peak duration), IBI (inter-beat interval). The 1D and BRV analyses used one selected electrode per organoid.
- **FPD definition:** R-peak (depolarization maximum) to T-wave peak (repolarization maximum), not baseline return; this differs from the convention advocated by Mäki (2023)
- **2D analysis:** spatiotemporal heatmaps of AMP, Slope, PPD, FPD per electrode per beat; coefficient of variation (CV) of the spatial variability; only the 2D analysis uses many electrodes
- **BRV analysis:** 45 measures (time-domain, frequency-domain, non-linear); VLF/LF cutoffs adjusted for organoids (0.025 Hz vs 0.046 Hz for humans)
- **Morphology handling (p. 3):** for low-amplitude R peaks the minimum peaks of the signal are found on the inverted signal; for inverted T waves the inverse segment of the signal is used to detect the inverted T peaks; electrode data with inconsistent biomarker value counts are excluded.
- **Cohorts:** 15 organoids from 8 differentiation batches: 10 organoids (5 batches) for basal-state BRV and 1D/2D analysis (Figs. 3–5) and 5 organoids (3 batches) for the carbachol (CCh) comparison (Figs. 6–7). The representative organoid of Figs. 3–4 is not stated to belong to either cohort.
- **Brugada Syndrome comparison:** previously published hiPSC-CM recordings (not organoids) from two Brugada patients (SCN5A p.S1812X) vs controls, seeded on 60MEA200/30iR-Ti-gr MEAs (200 µm electrode spacing) and recorded with Cardio 2D; 42 samples (BrS1 + BrS2) vs 30 control samples. PhysioMEA was used only for biomarker computation.
- **Pharmacology:** 1 µM carbachol (parasympathetic stimulation) only; no sympathetic stimulation
- **2D heatmap construction:** missing electrode values are filled by moving-average interpolation (window = 5) before rendering, so maps are partly interpolated

## Findings

- Under basal conditions in ten organoids, the beat-to-beat CVs of IBI, AMP, Slope, PPD and FPD (8–20%; e.g. IBI 8.11 ± 1.26%, FPD 18.32 ± 3.11%) were statistically similar between biomarker types (Kolmogorov-Smirnov test, p > 0.209 for IBI vs PPD and AMP vs FPD).
- In 2D, the spatial CVs were substantial for one representative beat of one organoid: AMP 39%, Slope 47%, PPD 23%, FPD 25%. The authors conclude similarity holds in 1D but not in 2D.
- BRV frequency content was dominated by VLF (63.4%), with LF 15.6% and HF about 21.0%; the authors interpret this as intrinsic rather than extrinsic mechanisms (§4.4).
- Brugada hiPSC-CM samples showed lower AMP and Slope and higher PPD than controls (P < 0.001, Fig. 8); the spatial CoV did not differ.
- Carbachol increased mean IBI (1497.24 ± 89.43 ms basal vs 2002.77 ± 138.37 ms, 134.68 ± 8.63% of basal; p = 0.019/0.016 appear in Fig. 6B/C). Frequency-domain bands, SD1/SD2 and MSE showed no significant change.
- Across the five CCh organoids, mean Slope decreased (0.13 ± 0.03 → 0.07 ± 0.02 V/s), PPD increased (6.74 ± 0.58 → 8.63 ± 0.67 ms) and FPD decreased (405.33 ± 21.36 → 354.75 ± 21.69 ms). The P < 0.001 in Fig. 7 refers to electrode-level differences in a single representative organoid, not to these means.

## Limitations

Stated by the authors (§4.6):
- A 10 kHz sampling rate is needed for propagation mapping.
- The organoid must lie inside the electrode area, so the seeding ring constrains its size.
- hiPSC-CMs are not biologically identical to native cardiomyocytes.
- Only one hiPSC line was used; the authors call for additional lines.

Our observations (not from the paper):
- FPD is R-to-T-peak, and the paper offers no systematic comparison with baseline-return definitions.
- The Brugada comparison used externally sourced recordings from a different MEA geometry and a single SCN5A variant.
- 2D heatmaps include interpolated values at missing electrodes.

## Relevance to our paper

Cited in main.md as an open-source platform (MATLAB) with 2D spatial analysis and BRV, and as an example of the R-to-T-peak FPD convention. The paper compares MultiElec, CardioMDA, Cardio PyMEA, Cardio2D, Axion and EMapScope; it does not mention CardioMEA. The "post-2022 shift away from vendor tools" framing is ours, not the paper's.

## See also

- [[wiki/papers/maki-2023-opinion.md]]
- [[wiki/papers/dunham-2022-cardiopyemea.md]]
- [[wiki/papers/lee-2024-cardiomea.md]]
- [[wiki/papers/ernault-2024-interpretation.md]]
- [[wiki/papers/kabanov-2026-cardioscripts.md]]
- [[wiki/papers/guerrelli-2024-hipscm.md]]
- [[wiki/papers/ismaili-2023-hamburg.md]]
