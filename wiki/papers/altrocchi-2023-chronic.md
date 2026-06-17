# Evaluation of chronic drug-induced electrophysiological and cytotoxic effects using human-induced pluripotent stem cell-derived cardiomyocytes (hiPSC-CMs)

**Authors:** C. Altrocchi, K. Van Ammel, M. Steemans, M. Kreir, F. Tekle, A. Teisman, D.J. Gallacher, H.R. Lu  
**Year:** 2023  
**Venue:** Frontiers in Pharmacology 14:1229960  
**File:** [[raw/steemans-2023-chronic.pdf]]  
**DOI:** 10.3389/fphar.2023.1229960  
**Affiliation:** Janssen Pharmaceutica NV, Beerse, Belgium

> **Citation note:** main.md cites as "Steemans et al. 2023." Actual first author is C. Altrocchi; Steemans is third author. Minor author-order error in the review draft.

## Contribution
Establishes a chronic MEA cardiotoxicity assay (up to 96 h) using hiPSC-CMs, validating it against 13 mechanistically diverse reference compounds. Demonstrates that combined FP and impedance monitoring distinguishes electrophysiological cardiotoxicity from cytotoxicity, and that tolerance intervals derived from large DMSO datasets provide objective QC thresholds.

## Methodology
- **Platform:** Axion Maestro Pro MEA (48-well, M768-tMEA-48B)
- **Cell line:** iCell-Cardiomyocytes2 (Fujifilm CDI, Donor 01434)
- **Recording:** Acute (0.5, 1, 2, 4 h) and chronic (24, 48, 72, 96 h) timepoints
- **Combined endpoints:** FP (FPD, FPDcF, FP amplitude) + impedance (cell impedance, beating impedance)
- **Tolerance intervals:** N=81 DMSO vehicle-control wells from 4 batches, 15 plates; 90%/95% tolerance intervals per endpoint per timepoint
- **13 reference compounds across 5 classes:**
  - **Negative controls:** aspirin, cetirizine, amoxicillin, captopril
  - **Direct cytotoxics:** doxorubicin, BMS-986094
  - **hERG trafficking inhibitors:** pentamidine, arsenic trioxide, probucol
  - **Tyrosine kinase inhibitors (TKi):** sunitinib, vandetanib, nilotinib, erlotinib

## Findings
- **hERG trafficking inhibitors show delayed FPD effects:**
  - Pentamidine: FPD prolongation appears only after ≥24 h at 1–3 µM (IC50 hERG trafficking 5–8 µM); acute timepoints appear clean
  - Arsenic trioxide: similarly delayed FPDc prolongation
  - Probucol: equivocal; some wells showed mild prolongation
- **Direct cytotoxics:**
  - Doxorubicin: dose-dependent impedance drop + cessation of beating (cytotoxicity precedes FP changes)
  - BMS-986094: T-wave flattening in FP + impedance drop (combined signature)
- **TKi (cardiovascular liability drugs):**
  - Sunitinib, vandetanib, nilotinib: FPD prolongation + arrhythmic events at pharmacologically relevant concentrations
  - Erlotinib: no significant effects (correctly identified as safe)
- **FP amplitude (AmpFP) was excluded** from tolerance intervals: its TI at 24 h was −23.5% to +99.6%, making it uninformative as a QC gate
- **Combined FP + impedance** distinguishes: (a) pure electrophysiology cardiotoxicity (FP changes, no impedance), (b) pure cytotoxicity (impedance drop, FP cessation), (c) mixed (both)

## Limitations
- Single cell line, single lot; donor variability not assessed
- Chronic assay requires cells to remain healthy on MEA for 96 h (challenging for some cell lines)
- Tolerance interval thresholds are platform- and lot-specific; cannot be transferred directly to other labs without recalibration

## Relevance to our paper
Cited in main.md as the primary source for chronic assay design, tolerance interval methodology, and the multi-endpoint (FP + impedance) paradigm. Also cited for specific compound results (pentamidine, doxorubicin, BMS-986094, TKi panel).

## See also
- [[wiki/papers/guerrelli-2024-hipscm.md]]
- [[wiki/papers/park-2025-cardiotoxicity.md]]
- [[wiki/papers/matsuda-2025-uhd.md]]
