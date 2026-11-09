---
tags: [open-platform, electromechanical]
---

# A comprehensive system of algorithms for characterization of cardiomyocyte mechanical and electrical function

**Authors:** Kabanov, D.A., Vrana, S., Beckerová, D., Rotrekl, V., Pesl, M., Přibyl, J.  
**Year:** 2026  
**Venue:** *Biomedical Signal Processing and Control*, 120, 110125  
**File:** [[raw/kabanov-2026-cardioscripts.pdf]]  
**Supplementary:** [[raw/kabanov-2026-cardioscripts-supplementary.docx]] (Figures S1–S6, example traces)  
**DOI:** 10.1016/j.bspc.2026.110125  
**Affiliation:** CEITEC MU, Masaryk University, Brno (Kabanov, Vrana, Přibyl); Faculty of Medicine and ICRC, St. Anne's University Hospital, Brno (Beckerová, Rotrekl, Pesl)

Note: page checked against the source text on 2026-10-24; statements not supported by the paper were removed or reworded. Checked claim by claim 2026-11-09: aminophylline concentrations and cell types corrected, the QT-interval scheme of Fig. 5 and the paper's inconsistent QT error added, page numbers of the limitations corrected, supplementary material added.

## Contribution

Introduces **CardioScripts** (also called **myopyth**), Python scripts for analysing atomic force microscopy (AFM) mechanocardiograms and MEA field potentials, separately or from simultaneous AFM-MEA recordings, including the electromechanical timing between the two. The authors present it as a systematic, modality-agnostic framework that also works on AFM-only or MEA-only recordings.

## Methodology

- **Cell lines:** HL-1 mouse cardiomyocytes (immortalized) and hESC-derived embryoid bodies (EBs, CCTL14 line)
- **Platform:** Synchronous AFM-MEA validation was performed on EBs; HL-1 monolayers were used primarily for MEA-based electrophysiology (p. 6)
- **Analysis implemented in CardioScripts:** QRST/T-peak detection on MEA signals (QT and T-peak, not FPD; the text describes how Q, R, S and the T peak are found as local extrema around the S peak, p. 5, but no algorithm for the end of the T wave), beat rate and beat-to-beat intervals, arrhythmia metrics on AFM recordings, contraction force from AFM traces, and the timing offset between electrical events on MEA and mechanical events on AFM
- **QT interval and T-offset (Fig. 5, p. 5):** the schematic of the myopythMEA settings draws the QT interval from the Q peak to the end of the T wave, where the signal has returned to baseline, and a separate "T-offset" interval that ends at the T peak. The figure is a schematic and carries no data. The text describes no T-end detection, the only T point found is the T peak (p. 5), Table 1 evaluates only Q, R, S, T and "QT interval", and in Fig. 6D (artificial MEA data, p. 7) the Q marker sits just before the R peak and the T marker on the T-wave peak (read from the zoomed figure by the researcher, 2026-11-09). So in practice QT runs from the Q point to the T peak; main.md Table 1 says so.
- **Validation on artificial data:** T-peak and QT detection tested on artificially generated signals only (Table 1, p. 7: T-peak precision 0.635, QT mean absolute error 19.4 ms, MAE given in ms; at least 500 R-R cycles, additive Gaussian noise σ = 5). The text gives a different QT error for the same test, "0.06719 seconds" (p. 6), and the Fig. 9 caption says the QT values "were subtracted by 0.2 as the script MAE" (p. 8), so the paper is internally inconsistent on the size of the QT error.
- **Drugs:** isoproterenol (positive chronotropic; beat rate and contraction force changed, Fig. 7), metoprolol (negatively chronotropic), aminophylline (positive inotropic effect, p < 0.01, concentration not stated, p. 7; arrhythmic patterns in EBs at 10 µM, Fig. 8; QT prolongation in HL-1 cells at 128 µM, p < 0.05 with a large dispersion, Fig. 9), lidocaine (known to cause electromechanical decoupling, citing the literature)
- **Arrhythmia analysis (Fig. 8):** AFM-only on EBs (N = 10), by the frequency of beat-to-beat intervals longer than 3 s and by SDSD; aminophylline increased both
- **Electromechanical decoupling (Fig. 10):** quantified as an increased delay between the MEA and AFM events; lidocaine increased the delay in a dose-dependent manner. The text reports significance at 25 and 30 µM (p < 0.001), whereas the Fig. 10C caption lists 15 and 25 µM (p < 0.001 and p < 0.0001) and no 30 µM, so the paper is internally inconsistent on the concentrations. Both signals were still present at 25 µM lidocaine, only displaced.

### Supplementary material
Viewed 2026-11-09 (images extracted from the .docx). Six figures of example data, no tables and no numbers beyond the traces:
- **Figure S1:** AFM vertical deflection of an EB in Tyrode solution and after 1 mM aminophylline, "which caused arrhythmic behavior" (irregular beat intervals, higher baseline). The concentration differs from the 10 µM of Fig. 8.
- **Figure S2:** AFM traces of an EB in Tyrode, with 1 µM isoprenaline and with 70 µM metoprolol.
- **Figure S3:** HL-1 field potentials on MEA, control (Claycomb medium) and 128 µM aminophylline, with the detected R, Q, S and T markers over 10 s.
- **Figure S4:** HL-1 field potentials, control and 0.1 µM isoprenaline, with detected markers.
- **Figure S5:** a 3-minute HL-1 recording before and after filtering (50 Hz notch, Q ≈ 35; 0.8–35 Hz 6th-order Butterworth band-pass), matching Section 2.6.
- **Figure S6:** cantilever position on an EB (border, centre, right, left) against the variance of amplitude and of beat rate over 3 min; the authors judge the border position optimal.
- The MEA amplitudes in S3–S5 are labelled mV with values of about ±150–300, which looks like a unit slip (field potentials are usually in µV).

The supplement adds no data that bear on the claims in main.md.

## Findings

- A working set of algorithms for rate, QT/T-peak, force and electromechanical delay, with the delay increase under lidocaine described as consistent with electromechanical decoupling.
- Cross-correlation is used only to align the AFM and MEA streams (within ±5 ms), not to define decoupling.
- Open-source Python implementation.

## Limitations

Stated by the authors (pp. 6–9):
- Synchronous validation was done only on EBs, not on HL-1 (Section 3.4, p. 9).
- The scripts need fine-tuning (p. 7), there is no automatic parameter optimisation, and they are not optimised for large data volumes (p. 8).
- A low sample rate causes a systematic amplitude error (p. 6).
- T-peak precision was modest on artificial data (Table 1) and QT data from HL-1 had a large dispersion (p. 7).

Our observation (not from the paper): the cells are mouse HL-1 and hESC-derived EBs (line CCTL14), not hiPSC-CMs, so use on hiPSC-CM MEA data may need adaptation. In the synchronous AFM–MEA recordings the paper analyses timing (the delay between field potential and contraction), not force; contraction force was measured with AFM alone (Fig. 7).

## Relevance to our paper

Cited in main.md as an example of expanding the feature set beyond purely electrical endpoints (electromechanical timing from combined AFM-MEA recordings) and in the open-pipelines table. The paper reports QT and T-peak, not FPD, and evaluates T-peak detection only on artificial data. The paper makes no comparison showing that the combined analysis reveals effects invisible to either modality alone.

## See also

- [[wiki/papers/dunham-2022-cardiopyemea.md]]
- [[wiki/papers/lee-2024-cardiomea.md]]
- [[wiki/papers/weiser-bitoun-2026-physiomea.md]]
- [[wiki/papers/matsuda-2025-uhd.md]]
