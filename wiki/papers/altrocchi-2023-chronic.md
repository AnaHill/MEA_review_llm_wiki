---
tags: [cardiac-safety, chronic-assay, impedance]
---

# Evaluation of chronic drug-induced electrophysiological and cytotoxic effects using human-induced pluripotent stem cell-derived cardiomyocytes (hiPSC-CMs)

**Authors:** C. Altrocchi, K. Van Ammel, M. Steemans, M. Kreir, F. Tekle, A. Teisman, D.J. Gallacher, H.R. Lu  
**Year:** 2023  
**Venue:** Frontiers in Pharmacology 14:1229960  
**File:** [[raw/altrocchi-2023-chronic.pdf]]  
**DOI:** 10.3389/fphar.2023.1229960  
**Affiliation:** Janssen Pharmaceutica NV, Beerse, Belgium


## Contribution
Establishes a chronic MEA cardiotoxicity assay (up to 96 h) using hiPSC-CMs, tested against 13 reference compounds. Combined FP and background impedance monitoring helps to separate electrophysiological effects from cytotoxicity, and tolerance intervals from pooled DMSO wells (N = 81, 15 plates, 4 batches) serve as cut-offs for judging the physiological relevance of compound effects (p. 5). Baseline well-quality criteria are separate: CV of beat period below 5%, FP amplitude at least 300 µV, beat rate 18–90 bpm.

Note: page checked against the source text on 2026-10-24; statements not supported by the paper were removed or reworded.

## Methodology
- **Platform:** Axion Maestro Pro MEA (48-well, M768-tMEA-48B)
- **Cell line:** iCell-Cardiomyocytes2 (Fujifilm CDI, Donor 01434); four lots (105464, 105170, 105567, 105998)
- **Recording:** baseline, then 2 h (acute) and 24, 48, 72, 96 h (chronic) after compound addition; 50% medium/compound refresh at 48 h
- **Endpoints:** FP (FPD, FPDc by the Fridericia formula, FP amplitude, beat rate) + background impedance (Ohm) as a cytotoxicity readout
- **Tolerance intervals:** non-parametric intervals (80% of vehicle values at 95% confidence) of the percent change from baseline, per parameter and timepoint, from N=81 DMSO wells
- **13 reference compounds (groups as in the paper):**
  - **Negative controls:** aspirin, cetirizine, amoxicillin, captopril
  - **Direct cytotoxics:** doxorubicin, BMS-986094
  - **Trafficking inhibitors:** pentamidine, arsenic trioxide, probucol (probucol also affects KV7.1 trafficking)
  - **Tyrosine kinase inhibitors (TKi):** sunitinib, vandetanib, nilotinib, erlotinib

## Findings
- **Trafficking inhibitors:**
  - Pentamidine: prolongation of FPD/FPDc from 24 h at 3 µM and 48 h at 1 µM; at 3 µM beating ceased in 3/6 wells at 72 h and 6/6 at 96 h, with arrhythmic-like events in 2/6 wells at 72 h. (Literature, not this study: hERG trafficking IC50 5–8 µM after at least 24 h.)
  - Arsenic trioxide: similarly delayed FPDc prolongation
  - Probucol: no significant FPD or FPDc prolongation at any concentration or time; beat rate increased at 10 µM. The assay did not reproduce its reported hERG-trafficking effect.
- **Direct cytotoxics:**
  - Doxorubicin: impedance drop from 24 h plus cessation of beating and T-wave loss at 3 µM; the authors say impedance showed that cytotoxicity drove the FP changes
  - BMS-986094: T-wave flattening in FP + impedance drop
- **TKi:**
  - Sunitinib, vandetanib, nilotinib: FPD prolongation + arrhythmic events at pharmacologically relevant concentrations
  - Erlotinib: no relevant FPD/FPDc prolongation or arrhythmic events; a borderline impedance decrease at 10 µM (24 h only)
- **FP amplitude (Amp FP):** its tolerance interval was computed (−23.5% to +99.6% at 24 h, Table 2) but the authors judged Amp FP not useful for assessing chronic drug-induced effects (p. 5)
- **Combined FP + impedance:** illustrated by sunitinib (FP effects without an impedance change), vandetanib (both) and doxorubicin (cytotoxicity-driven) (pp. 13–14); the paper does not present a formal three-way taxonomy

## Limitations
Stated by the authors (p. 14): a single donor, no 3D heart complexity or immune/inflammatory interactions, hiPSC-CM immaturity (low Kir2.x, high HCN, sarcomere structure), and well concentrations that were not measured and may be lower than nominal (10% serum), which affects the fCmax margin comparison. The paper calls the platform medium-throughput.

## Relevance to our paper
Cited in main.md for MEA use in general (Introduction), for Fridericia-corrected FPD, and for the chronic design (48-well plates, acute under 2 h and delayed effects of 24 h or more over four days, TKi, doxorubicin and trafficking inhibitors, FP plus impedance, multi-parameter feature sets). main.md does not discuss the tolerance intervals or individual compound results (pentamidine, BMS-986094); the 0.03 µM doxorubicin value belongs to Matsuda et al.

## See also
- [[wiki/papers/guerrelli-2024-hipscm.md]]
- [[wiki/papers/park-2025-cardiotoxicity.md]]
- [[wiki/papers/matsuda-2025-uhd.md]]
- [[wiki/papers/pramudito-2026-ensemble.md]]
