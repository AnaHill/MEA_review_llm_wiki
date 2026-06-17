# Human induced pluripotent stem cell-cardiomyocytes for cardiotoxicity assessment: a comparative study of arrhythmia-inducing drugs with multi-electrode array analysis

**Authors:** Na Kyeong Park, Yun-Gwi Park, Ji-Hee Choi, Hyung Kyu Choi, Sung-Hwan Moon, Soon-Jung Park, Seong Woo Choi  
**Year:** 2025  
**Venue:** Korean Journal of Physiology & Pharmacology 29(2):257–269  
**File:** [[raw/park-2025-cardiotoxicity.pdf]]  
**DOI:** 10.4196/kjpp.24.413

## Contribution
Comparative cardiotoxicity study using three healthy hiPSC-CM lines and one patient-derived LQTS line (KCNH2 c.453delC) with eight CiPA reference compounds, introducing the FPD20/FPDc20 metric (minimum concentration for >20% FPD change) as a standardizable pharmacological endpoint.

## Methodology
- **Platform:** Axion MEA (96-well plate); fibronectin-coated; Axion Cardiac Analysis Tool
- **Cell lines:**
  - CMC-006, CMC-011, CMC-016 (healthy; cord blood; Korea Stem Cell Bank)
  - DPHC01i-AR (LQTS2; KCNH2 c.453delC frameshift; peripheral blood; patient-derived)
- **Drug panel (8 CiPA drugs at concentrations from Millard et al. 2018):**
  E4031, nifedipine, mexiletine, JNJ303, flecainide, moxifloxacin, quinidine, ranolazine
- **Endpoints:** FPD, FPDcF (Fridericia), % change from baseline; FPD20/FPDc20 as EC20-type metric
- **Complementary:** Single-cell AP recordings by patch clamp to confirm cellular phenotype
- FPD % change formula: (post-drug FPD / baseline FPD) × 100

## Findings
- **LQTS line (DPHC01i-AR)** is significantly more sensitive to E-4031: FPD20 = 0.003 µM vs. 0.01–0.03 µM for healthy lines (10× more sensitive)
- **Mexiletine** shows differential response: FPD20 = 1 µM for DPHC01i-AR; no >20% change in any healthy line
- **JNJ303** (IKs blocker) does not induce significant FPD changes in any line — suggests IKs contribution may be modest or masked in these conditions
- **DPHC01i-AR** has prolonged APD80 and distinct arrhythmic AP morphologies in patch clamp
- **>70% ventricular-like** action potentials confirmed in CMC cell lines by patch clamp
- FPD20/FPDc20 metric provides a standardizable pharmacological sensitivity index across lines

## Limitations
- Only 8 of the CiPA compound set tested; no mechanistically diverse panel beyond ion channel drugs
- FPD20 metric does not capture waveform morphology changes or arrhythmic event counts
- Korean cord-blood cell lines (CMC series) are not internationally commercialized; cross-lab comparison requires effort

## Relevance to our paper
Cited in main.md as: (1) a use case for patient-specific LQTS hiPSC-CMs in MEA cardiotoxicity screening, and (2) the FPD20/FPDc20 metric as an example of a threshold-based quantitative endpoint beyond raw FPDcF. Also provides comparative data showing that disease lines reveal pharmacological sensitivities invisible in healthy lines.

## See also
- [[wiki/papers/maurissen-2024-mutation.md]]
- [[wiki/papers/altrocchi-2023-chronic.md]]
- [[wiki/papers/ismaili-2023-hamburg.md]]
