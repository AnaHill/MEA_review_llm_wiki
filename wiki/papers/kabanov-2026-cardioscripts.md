# A comprehensive system of algorithms for characterization of cardiomyocyte mechanical and electrical function

**Authors:** Kabanov, D.A., Vrana, S., Beckerová, D., Rotrekl, V., Pesl, M., Přibyl, J.  
**Year:** 2026  
**Venue:** *Biomedical Signal Processing and Control*, 120, 110125  
**File:** [[raw/kabanov-2026-cardioscripts.pdf]]  
**DOI:** 10.1016/j.bspc.2026.110125  
**Affiliation:** CEITEC MU, Masaryk University, Brno, Czech Republic

## Contribution

Introduces **CardioScripts** (also referred to as **Myopyth**), an open-source Python toolbox for simultaneous analysis of cardiomyocyte mechanical and electrical function using combined atomic force microscopy (AFM) and multielectrode array (MEA) recordings. The central claim is that combined electromechanical analysis — not MEA alone — is needed to fully characterize arrhythmic and contractile drug responses, and that electromechanical coupling and decoupling can be detected and quantified computationally.

## Methodology

- **Cell lines:** HL-1 mouse cardiomyocytes (immortalized) and hESC-derived embryoid bodies (CCTL14 line)
- **Platform:** Combined AFM (contraction force) + MEA (extracellular FP) simultaneous recording
- **Analysis algorithms implemented in CardioScripts:**
  - QRST complex detection and characterization (Q, R, S, T fiducial points)
  - Beat rate and inter-beat interval
  - Arrhythmia classification
  - Contraction force extraction from AFM deflection traces
  - Electromechanical coupling delay (time from electrical event to mechanical peak)
  - Electromechanical decoupling detection (loss of correlation between electrical and mechanical signals)
- **Drugs tested:** aminophylline (positive chronotrope), metoprolol (β-blocker), isoproterenol (positive chronotrope/inotrope), lidocaine (sodium channel blocker)
- **Key validation:** Lidocaine produces dose-dependent electromechanical decoupling (significant at 25 µM and 30 µM, p < 0.001), detected by divergence between FP and contraction force signals.

## Findings

- Combined AFM+MEA analysis reveals drug effects invisible to either modality alone: lidocaine suppresses electrical activity and completely abolishes mechanical contraction at high doses, demonstrating full electromechanical decoupling.
- Electromechanical coupling delay quantified; drug effects on both rate and delay are separable.
- Arrhythmia classification based on beat regularity derived from the combined signal.
- Open-source Python implementation with documented algorithms enables reproducibility.

## Limitations

- Cell lines are HL-1 (mouse, immortalized) and hESC-derived EBs — not hiPSC-CMs from patient donors; direct translation to human iPSC-CM MEA data may require adaptation.
- Simultaneous AFM+MEA setup is specialized equipment not widely available in pharmacology labs.
- CardioScripts is validated on a limited drug panel; broader pharmacological coverage is needed.

## Relevance to our paper

Represents an extension of MEA-based feature sets beyond electrical endpoints into the electromechanical domain. Relevant to the "High-throughput and longitudinal assays" section as an example of expanded multi-parameter analysis, and to the "Transition to open pipelines" section as another open-source Python platform for MEA analysis. The electromechanical coupling/decoupling feature is a novel biomarker category not captured by conventional FPD-centric workflows.

Not currently in main.md citation list (as of June 2026 ingest); warrant addition in the feature-set expansion discussion.

## See also

- [[wiki/papers/dunham-2022-cardiopyemea.md]]
- [[wiki/papers/lee-2024-cardiomea.md]]
- [[wiki/papers/weiser-bitoun-2026-physiomea.md]]
