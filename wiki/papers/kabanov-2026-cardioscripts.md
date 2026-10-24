---
tags: [open-platform, electromechanical]
---

# A comprehensive system of algorithms for characterization of cardiomyocyte mechanical and electrical function

**Authors:** Kabanov, D.A., Vrana, S., Beckerová, D., Rotrekl, V., Pesl, M., Přibyl, J.  
**Year:** 2026  
**Venue:** *Biomedical Signal Processing and Control*, 120, 110125  
**File:** [[raw/kabanov-2026-cardioscripts.pdf]]  
**DOI:** 10.1016/j.bspc.2026.110125  
**Affiliation:** CEITEC MU, Masaryk University, Brno (Kabanov, Vrana, Přibyl); Faculty of Medicine and ICRC, St. Anne's University Hospital, Brno (Beckerová, Rotrekl, Pesl)

Note: page checked against the source text on 2026-10-24; statements not supported by the paper were removed or reworded.

## Contribution

Introduces **CardioScripts** (also called **myopyth**), Python scripts for analysing atomic force microscopy (AFM) mechanocardiograms and MEA field potentials, separately or from simultaneous AFM-MEA recordings, including the electromechanical timing between the two. The authors present it as a systematic, modality-agnostic framework that also works on AFM-only or MEA-only recordings.

## Methodology

- **Cell lines:** HL-1 mouse cardiomyocytes (immortalized) and hESC-derived embryoid bodies (EBs, CCTL14 line)
- **Platform:** Synchronous AFM-MEA validation was performed on EBs; HL-1 monolayers were used primarily for MEA-based electrophysiology (p. 6)
- **Analysis implemented in CardioScripts:** QRST/T-peak detection on MEA signals (QT and T-peak, not FPD), beat rate and beat-to-beat intervals, arrhythmia metrics on AFM recordings, contraction force from AFM traces, and the timing offset between electrical events on MEA and mechanical events on AFM
- **Validation on artificial data:** T-peak and QT detection tested on artificial signals (Table 1: T-peak precision 0.635, QT mean absolute error 19.4 ms)
- **Drugs:** isoproterenol (positive chronotropic; beat rate and contraction force changed, Fig. 7), metoprolol (negatively chronotropic), aminophylline (10 µM on EBs: positive inotropic effect, arrhythmic patterns, QT prolongation), lidocaine (known to cause electromechanical decoupling, citing the literature)
- **Arrhythmia analysis (Fig. 8):** AFM-only on EBs (N = 10), by the frequency of beat-to-beat intervals longer than 3 s and by SDSD; aminophylline increased both
- **Electromechanical decoupling (Fig. 10):** quantified as an increased delay between the MEA and AFM events; lidocaine increased the delay in a dose-dependent manner. The text reports significance at 25 and 30 µM (p < 0.001), whereas the Fig. 10C caption lists 15 and 25 µM (p < 0.001 and p < 0.0001) and no 30 µM, so the paper is internally inconsistent on the concentrations. Both signals were still present at 25 µM lidocaine, only displaced.

## Findings

- A working set of algorithms for rate, QT/T-peak, force and electromechanical delay, with the delay increase under lidocaine described as consistent with electromechanical decoupling.
- Cross-correlation is used only to align the AFM and MEA streams (within ±5 ms), not to define decoupling.
- Open-source Python implementation.

## Limitations

Stated by the authors (pp. 7–8):
- Synchronous validation was done only on EBs, not on HL-1.
- The scripts need fine-tuning, there is no automatic parameter optimisation, and they are not optimised for large data volumes.
- A low sample rate causes a systematic amplitude error.
- T-peak precision was modest on artificial data and QT data from HL-1 had a large dispersion.

Our observation (not from the paper): the cells are mouse HL-1 and hESC-derived EBs, not patient hiPSC-CMs, so use on hiPSC-CM MEA data may need adaptation.

## Relevance to our paper

Cited in main.md as an example of expanding the feature set beyond purely electrical endpoints (electromechanical timing from combined AFM-MEA recordings) and in the open-pipelines table. The paper reports QT and T-peak, not FPD, and evaluates T-peak detection only on artificial data. The paper makes no comparison showing that the combined analysis reveals effects invisible to either modality alone.

## See also

- [[wiki/papers/dunham-2022-cardiopyemea.md]]
- [[wiki/papers/lee-2024-cardiomea.md]]
- [[wiki/papers/weiser-bitoun-2026-physiomea.md]]
- [[wiki/papers/matsuda-2025-uhd.md]]
