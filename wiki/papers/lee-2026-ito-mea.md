---
tags: [multimodal, rate-correction, cardiac-safety]
---

# Integrated electrophysiological and optical analysis of human iPSC-derived cardiomyocytes using transparent ITO microelectrode chip

**Authors:** Seul-Gi Lee, Shinhye Park, C-Yoon Kim, Hyung Min Chung  
**Year:** 2026  
**Venue:** International Journal of Stem Cells 19(2):146–156 (received 29 August 2025, published online 3 February 2026)  
**File:** [[raw/lee-2026-ito-mea.pdf]] (open access, CC BY-NC 4.0)  
**Supplementary:** [[raw/lee-2026-ito-mea-supplementary.pdf]] (captions of two videos; the videos are not in the repository)  
**DOI:** 10.15283/ijsc25077

Note: ingested 2026-11-01 from the full text (11 pages, text extraction) and the supplement; Figure 4 viewed (page 8 rendered), other figures not viewed. Affiliation: Konkuk University, Seoul. Found through Karami et al. (2026). Not to be confused with Lee et al. (2024), CardioMEA ([[wiki/papers/lee-2024-cardiomea.md]]); the first authors are J. Lee and S.-G. Lee.

## Contribution
Tests a commercial MEA with transparent indium tin oxide (ITO) electrodes (CFPS-ITO-16W2E plates, CFPS-32 system, Cellames) for hiPSC-CM cardiotoxicity testing, combining field potentials with optical observation of the same wells (morphology, Ca²⁺ imaging) and end-point viability and sarcomere staining. The authors present it as a platform "capable of real-time monitoring of both drug-induced electrophysiological responses and optical cellular changes".

## Methodology
- **Cells:** in-house hiPSC-CMs from BJ fibroblasts (episomal reprogramming), CHIR/C59 differentiation, lactate selection, matured to day 30; 97.06 % cTnT-positive; mostly MLC2v-positive (ventricular-like). One line.
- **MEA:** 16-well ITO plates, 50,000 cells per well, 5–6 days of stabilisation; medium changed to AD-MEM 1 h before recording, 17 min of stabilisation, 3-min recordings; analysis in the vendor software (CFPS-32). Parameters: spike amplitude, beat period, FPD and FPDc "corrected by Fridericia's formula, the most widely used correction method in cardiotoxicity testing". A change of at least 20 % was taken as a meaningful response.
- **Optical:** bright-field morphology through the electrodes; Fluo-4 Ca²⁺ imaging at baseline (n = 3). The optical and FP analyses are reported side by side; no joint analysis.
- **Drugs:** acute stepwise dosing of E-4031 (0.003–0.03 µM) and nifedipine (0.008–0.8 µM), 17 min per step (n = 4–5 wells); doxorubicin 3 µM for 2 days, recorded on days 0, 1 and 2 (n = 5).

## Findings
- **Baseline (n = 12):** beat period 1.498 s, FPD 0.320 s, FPDc 0.280 s, spike amplitude 1.712 mV; vehicle (0.1 % DMSO) changed the FP parameters by less than 5 %.
- **E-4031:** FPD +17.9, +56.3 and +154.3 % and FPDc +18.8, +54.6 and +125.8 % with dose; beat period +43.7 % only at 0.03 µM; spike amplitude down to −40.9 %. **Nifedipine:** beat period, FPD and FPDc shortened with dose (FPDc −62.4 % at 0.8 µM); no amplitude change. No visible morphological change after acute dosing.
- **Doxorubicin (Fig. 4, viewed):** beat period rose sharply on day 1 (8.213 s against 1.961 s in controls) and less on day 2 (4.177 s); FPD lengthened over time (0.382, 0.448 and 0.495 s); **FPDc fell markedly on day 1 "due to the sharp BP prolongation"** and partly recovered on day 2, so FPD and FPDc moved in opposite directions; spike amplitude dropped from day 1; cell density fell, viability decreased (about 83 % against 95 %, Fig. 4G) and sarcomeres were disrupted.
- **Discussion:** "differences in MEA chip composition and recording hardware may alter absolute signal values" (citing Millard et al., 2018, Blinova et al., 2018, and Jahnke et al., 2019), so QC thresholds are needed; the baseline met CiPA QC (spike amplitude ≥ 0.3 mV, about 40 bpm). Chronic effects need assessment beyond acute dosing (citing Altrocchi et al., 2023).

## Limitations
Stated by the authors: immature hiPSC-CMs and 2D monolayers; contractility and Ca²⁺ handling should be added for translational fidelity.

Our observations (not from the paper): one line, small n (4–5 wells per drug); the optical readouts are not synchronised with or analysed jointly with the FP; Ca²⁺ imaging only at baseline; the FPD definition is the vendor software's and not described; the beat period on doxorubicin day 1 (about 8 s, about 7 bpm) lies far outside the 20–90 bpm range accepted in the multisite CiPA study, which is where a Fridericia correction is least trustworthy.

## Relevance to our paper
Cited in main.md from 2026-11-01: rate-correction paragraph (doxorubicin example), sensor-fusion paragraph (side by side), device-separation paragraph (hardware alters absolute values).

(1) Rate correction: a concrete case in hiPSC-CMs where Fridericia-corrected FPD moved opposite to FPD when the beating rate slowed sharply (doxorubicin day 1), illustrating that the correction can mislead at extreme rates. (2) Device separation: the authors' statement that MEA chip composition and recording hardware may alter absolute signal values. (3) Sensor fusion: a hiPSC-CM example of FP and optical readouts from the same wells on a transparent MEA, analysed side by side rather than jointly, which supports the outlook's observation that modalities are mostly analysed separately.

## See also
- [[wiki/papers/hu-2026-tft-mea-multimodal.md]]
- [[wiki/papers/karami-2026-mea-cardiotoxicity.md]]
- [[wiki/papers/ryynanen-2018-single-cell-mea.md]]
- [[wiki/papers/altrocchi-2023-chronic.md]]
- [[wiki/fridericia-rate-correction.md]]
- [[wiki/multimodal-measurement.md]]
- [[wiki/signal-separation.md]]
