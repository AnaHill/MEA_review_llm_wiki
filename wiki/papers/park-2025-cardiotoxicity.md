---
tags: [cardiac-safety, disease-model, lqts]
---

# Human induced pluripotent stem cell-cardiomyocytes for cardiotoxicity assessment: a comparative study of arrhythmia-inducing drugs with multi-electrode array analysis

**Authors:** Na Kyeong Park, Yun-Gwi Park, Ji-Hee Choi, Hyung Kyu Choi, Sung-Hwan Moon, Soon-Jung Park, Seong Woo Choi  
**Year:** 2025  
**Venue:** Korean Journal of Physiology & Pharmacology 29(2):257–269  
**File:** [[raw/park-2025-cardiotoxicity.pdf]]  
**DOI:** 10.4196/kjpp.24.413

## Contribution
Comparative cardiotoxicity study using three healthy hiPSC-CM lines and one patient-derived LQTS line (KCNH2 c.453delC) with eight arrhythmogenic drugs (concentrations from the blinded CiPA pilot study of Millard et al.), defining FPD20/FPDc20 (the lowest tested concentration producing a >20% change in FPD/FPDc) to compare drug responses across lines.

Note: page checked against the source text on 2026-10-24; statements not supported by the paper were removed or reworded.

## Methodology
- **Platform:** Axion MEA (96-well plate); fibronectin-coated; Axion Cardiac Analysis Tool
- **Cell lines:**
  - CMC-006, CMC-011, CMC-016 (healthy; cord blood; Korea Stem Cell Bank)
  - DPHC01i-AR (LQTS2; KCNH2 c.453delC frameshift; peripheral blood; patient-derived)
- **Drug panel (8 arrhythmogenic drugs at concentrations from Millard et al. 2018):**
  E4031, nifedipine, mexiletine, JNJ303, flecainide, moxifloxacin, quinidine, ranolazine
- **Endpoints:** FPD, corrected FPD (FPDc, computed by the vendor software; the paper does not name the correction formula), beat period and amplitude, % change from baseline; FPD20/FPDc20 (lowest tested concentration with >20% change, not a fitted EC20)
- **Complementary:** Single-cell AP recordings by patch clamp to confirm cellular phenotype
- FPD % change formula: (post-drug FPD / baseline FPD) × 100

## Findings
- **E-4031:** FPD20 was 0.003 µM in the LQTS line (DPHC01i-AR) vs. 0.01 (CMC-006) and 0.03 µM (CMC-011, CMC-016), i.e. 3.3- to 10-fold; in FPDc20, CMC-006 was also 0.003 µM. No statistical test is reported. The authors note that certain healthy lines respond like patient-derived lines to E-4031 and nifedipine (p. 11).
- **Mexiletine** (FPD): FPD20 = 1 µM for DPHC01i-AR; no >20% change in any healthy line. In FPDc20, mexiletine was 30 µM in CMC-006 and CMC-011 and no change in DPHC01i-AR.
- **JNJ303** (described in the paper as a calcium channel modulator) produced no significant FPD change in any line
- **DPHC01i-AR:** the authors describe prolonged APD80/APD50 and distinct arrhythmic characteristics in patch clamp, although Table 4 shows APD values within the range of the control lines and no test is reported
- **>70% ventricular-like** action potentials confirmed in CMC cell lines by patch clamp
- FPD20/FPDc20 were defined to compare drug-induced responses across cell lines (p. 8); the authors call for standardised differentiation protocols and lines (p. 11), not for this metric

## Limitations
Stated by the authors (pp. 10–11): hiPSC-CMs are immature, lines vary, and toxicity readouts depend on the line.

Our observations (not from the paper): a single LQTS line was tested, and the FPD20 metric itself does not include waveform morphology (arrhythmic beats are reported separately in the Fig. 4 and 5 captions).

## Relevance to our paper
Cited in main.md for MEA use in disease modelling and CiPA (Introduction), for reporting corrected FPD without naming the formula and using the vendor Cardiac Analysis Tool, and in the chronic/longitudinal passage on eight arrhythmia-inducing drugs across healthy and LQTS-derived lines. main.md does not use the FPD20/FPDc20 metric. The disease-line effect holds clearly for mexiletine and nifedipine in FPD20; E-4031 sensitivity is also visible in the healthy lines.

Overlap note (added 2026-10-18, checked 2026-10-24): the same group's later paper [[wiki/papers/park-2026-genotype-ml.md]] very probably uses the same KCNH2 c.453delC LQT2 line (DPHC01i-AR here, DPHCi01 there; the 2025 tables themselves use both spellings), the normal line CMC-011, mexiletine, nifedipine, quinidine and ranolazine, and the same Axion 96-well MEA platform (model unnamed in 2025; Maestro Pro, Cytoview 96-well and Fridericia FPDc named in 2026), and extends FPD20/FPDc20 with BP20 and Amp20 and risk levels 0–4. Do not cite the two as independent confirmation of the disease-line result.

## See also
- [[wiki/papers/park-2026-genotype-ml.md]]
- [[wiki/papers/maurissen-2024-mutation.md]]
- [[wiki/papers/altrocchi-2023-chronic.md]]
- [[wiki/papers/ismaili-2023-hamburg.md]]
- [[wiki/papers/pramudito-2026-ensemble.md]]
- [[wiki/papers/guerrelli-2024-hipscm.md]]
