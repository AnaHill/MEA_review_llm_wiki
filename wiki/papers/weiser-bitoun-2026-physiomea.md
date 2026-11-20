---
tags: [open-platform, fiducial-definition, spatial-analysis, 3d-model]
---

# PhysioMEA: Signal processing platform for rate and rhythm analysis of multi-electrode array cardiac electrophysiological recordings

**Authors:** Weiser-Bitoun, I., Mazgaoker, S., Assayag, S., Davoodi, M., Alexandrovich, A., Yaniv, Y.  
**Year:** 2026  
**Venue:** *Journal of Molecular and Cellular Cardiology*, 210, pp. 137–149  
**File:** [[raw/weiser-bitoun-2026-physiomea.pdf]]  
**DOI:** 10.1016/j.yjmcc.2025.11.006  
**Affiliation:** Technion – Israel Institute of Technology, Israel (the first author also at Rambam Health Care Campus)

**Software** (checked 2026-11-20):
- Source code: <https://github.com/PhysioMEA/PhysioMEA> — MATLAB sources (`PhysioMEA_GUI.m`, `PhysioMEABatch_GUI.m`, `Config`, `GUI` and a bundled `mhrv` folder, the toolbox behind the BRV measures), **GPL-3.0**. No tagged releases and no installer in the repository; the standalone .exe is distributed from the lab site instead.
- Documentation: <https://bioelectric-bioenergetic-lab.net.technion.ac.il/documentation/> — a step-by-step user manual in four parts (loading and saving raw .mcd or .h5 data and selecting channels and time ranges; peak detection and biomarker parameters; 2D heatmap frames, videos and 3D views; batch BRV analysis). Separate Download, About and Novelty pages are linked from its menu.
- Novelty page: <https://bioelectric-bioenergetic-lab.net.technion.ac.il/novelty/> — the lab's own two novelty claims, 2D biomarker analysis with heatmaps and batch BRV analysis of cardiac constructs, both "presented for the first time on PhysioMEA Platform". It names no competing tool, so it is weaker than the Discussion of the paper (§4.5), which does compare MultiElec, CardioMDA, Cardio PyMEA, Cardio2D, Axion Maestro and EMapScope.

The paper's own pointer is the lab site root (Programs > PhysioMEA, p. 2); the GitHub repository is not named in the paper.

**Year.** Cited here as **2026**, from the article header "Journal of Molecular and Cellular Cardiology 210 (2026) 137–149". Several places give 2025 instead: the article was available online 17 November 2025, the copyright line reads "© 2025 The Author(s)", the DOI contains `2025`, Elsevier's own Cite widget gives "2025; 210, 137-149", and the authors' GitHub README cites their paper as "(2025)". This is the ordinary Elsevier split between online-first year and issue year; the issue year is used here, as for [[wiki/papers/botti-2026-insilico.md]] and [[wiki/papers/park-2026-genotype-ml.md]].

Note: page checked against the source text on 2026-10-24; statements not supported by the paper were removed or reworded. Checked claim by claim against the full text, Results included, 2026-11-19.

## Contribution

Introduces **PhysioMEA**, an open-source platform (MATLAB 2023b or standalone .exe) for rate and rhythm analysis of hiPSC-CM-derived cardiac organoids on MEAs. Three methodological contributions: (1) one-dimensional biomarker algorithms (FPD, spike amplitude, peak-to-peak duration, inter-beat interval) for selected electrodes; (2) two-dimensional spatiotemporal biomarker heatmaps showing electrode-to-electrode variability in AMP, Slope, PPD and FPD; (3) beat rate variability (BRV) analysis with 45 measures adapted from heart rate variability (HRV). The authors call it the first comprehensive BRV analysis in cardiac organoids (earlier BRV work on iPSC pacemaker cells: Ben-Ari et al. 2014, cited in §4.4).

## Methodology

- **Model:** hiPSC-CM-derived cardiac organoids on MEA chips, formed through a seeding guide ring with a 1.5 mm² hole (§2.2); hiPSC line from a 46-year-old female volunteer (§2.1)
- **1D biomarkers:** FPD, AMP (spike amplitude), Slope (maximum dV/dt of the depolarization spike), PPD (peak-to-peak duration), IBI (inter-beat interval). The 1D and BRV analyses used one selected electrode per organoid.
- **FPD definition:** R-peak to T-wave peak (repolarization maximum), not baseline return; this differs from the convention advocated by Mäki (2023). The R-peak here is the **positive** sharp spike, detected by a positive-amplitude threshold (default 50 µV, §2.5), followed by a negative S-peak (§1) — the opposite polarity to the initial negative peak that Hayakawa et al. (2014) call the R peak, although Table 2 of main.md groups both under the same R-to-T-peak convention.
- **2D analysis:** spatiotemporal heatmaps of AMP, Slope, PPD, FPD per electrode per beat; coefficient of variation (CV) of the spatial variability; only the 2D analysis uses many electrodes
- **BRV analysis:** 45 measures (time-domain, frequency-domain, non-linear); VLF/LF cutoffs adjusted for organoids (0.025 Hz vs 0.046 Hz for humans)
- **Morphology handling (p. 3):** for low-amplitude R peaks the minimum peaks of the signal are found on the inverted signal; for inverted T waves the inverse segment of the signal is used to detect the inverted T peaks; electrode data with inconsistent biomarker value counts are excluded (a data-consistency rule, not a morphology rule). These are the only places where waveform variation enters: the paper does not state that morphology varies, gives no prevalence for either case, and describes a canonical waveform in §1 — "It generally consists of a positive sharp spike (R-peak) followed by a negative sharp spike (S-peak) … then … a smooth, hill-like segment (T-wave)" — with the branches as exceptions to it. So the awareness main.md credits to this paper is read off its algorithm, not stated by its authors.
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
- The construct is called a cardiac organoid but is never described as three-dimensional: the only "three-dimensional" in the text is the X/Y/beat-number matrix behind the heatmaps (§2.7), the dimensional language is 1D versus 2D in the electrode plane ("the 2D cardiac sample", §4.3), and the cells are seeded directly onto the plate inside a 1.5 mm² ring. Treat it as evidence about organoid-labelled constructs, not about recording from thick 3D tissue.
- The Brugada comparison used externally sourced recordings from a different MEA geometry and a single SCN5A variant.
- 2D heatmaps include interpolated values at missing electrodes.

## Relevance to our paper

Cited in main.md as an open-source platform (MATLAB) with 2D spatial analysis and BRV, and as an example of the R-to-T-peak FPD convention. The paper compares MultiElec, CardioMDA, Cardio PyMEA, Cardio2D, Axion and EMapScope; it does not mention CardioMEA. The "post-2022 shift away from vendor tools" framing is ours, not the paper's.

## See also

- [[wiki/papers/maki-2023-opinion.md]]
- [[wiki/papers/dunham-2022-cardiopyemea.md]]
- [[wiki/papers/lee-2024-cardiomea.md]]
- [[wiki/papers/ernault-2024-interpretation.md]]
- [[wiki/papers/hayakawa-2014-motion-fp.md]] — opposite R-peak polarity inside the same R-to-T-peak convention (positive spike versus initial negative peak; Table 2)
- [[wiki/papers/kabanov-2026-cardioscripts.md]]
- [[wiki/papers/guerrelli-2024-hipscm.md]]
- [[wiki/papers/ismaili-2023-hamburg.md]]
- [[wiki/critical-assessment-maki-claims.md]]
- [[wiki/fpd-end-conventions.md]]
- [[wiki/open-analysis-platforms.md]]
- [[wiki/3d-models.md]]
