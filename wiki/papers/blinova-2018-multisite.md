---
tags: [cardiac-safety, rate-correction, high-throughput, 2d-culture]
---

# International multisite study of human-induced pluripotent stem cell-derived cardiomyocytes for drug proarrhythmic potential assessment

**Authors:** Ksenia Blinova, Qianyu Dang, Daniel Millard, Godfrey Smith, Jennifer Pierson, Liang Guo, Mathew Brock, Hua Rong Lu, Udo Kraushaar, Haoyu Zeng, Hong Shi, Xiaoyu Zhang, Kohei Sawada, Tomoharu Osada, Yasunari Kanda, Yuko Sekino, Li Pang, Tromondae K. Feaster, Ralf Kettenhofen, Norman Stockbridge, David G. Strauss, Gary Gintant  
**Year:** 2018  
**Venue:** Cell Reports 24(13):3582–3592 (published 25 Sep 2018; open access, CC BY-NC-ND). Issue number taken from the reference list of Park et al. 2026 (supplementary); the PDF itself prints only "24".  
**File:** [[raw/blinova-2018-multisite.pdf]]  
**DOI:** 10.1016/j.celrep.2018.08.079  
**Affiliations:** US FDA (CDRH, CDER, NCTR), AbbVie, Axion BioSystems, Genentech, Janssen, Merck, Bristol-Myers Squibb, ACEA, Eisai, Cellular Dynamics, Ncardia, University of Glasgow and others (10 test sites).

> **Note:** Full text read 2026-10-18 via text extraction; main-article figures were not inspected visually. Outside our primary 2022–present window; kept as foundational context because it is the source dataset of [[wiki/papers/pramudito-2026-ensemble.md]] and states the FPD rate-correction convention behind that dataset.

## Contribution
First large blinded multisite validation of hiPSC-CMs within the CiPA initiative: 28 drugs of known clinical TdP risk, two commercial cell lines, five electrophysiology platforms across ten sites. Builds logistic regression models that predict TdP risk category from hiPSC-CM drug responses. The authors state that the advance is the scale and the combination of MEA and optical methods, not a new assay.

## Methodology
- **Drugs:** 28 CiPA reference compounds (9 low, 11 intermediate, 8 high TdP risk), supplied blinded by the NCI repository, four concentrations each, mostly single concentration per well (sequential dosing at site 10 only).
- **Cells and platforms:** iCell Cardiomyocytes² (Cellular Dynamics) and Cor.4U (Ncardia). Four MEA platforms (Axion Maestro, ACEA CardioECR, Multichannel Systems Multiwell, Alpha MED AlphaMED64) and one voltage-sensing optical platform (Clyde CellOPTIQ). Fifteen complete site/cell datasets.
- **Protocol:** recordings at 37 °C, media change 2–24 h before baseline, baseline recording, drug addition, then re-equilibration of at least 30 min before recording. At least 5 replicate wells for 97 % of data points.
- **Quality criteria (pre-specified):** baseline beating rate 20–90 bpm; within 6 SD of the plate's wells; coefficient of variation of baseline beat period <5 %; depolarization spike amplitude >0.3 mV (MEA only). At most 3 % of wells excluded.
- **Endpoints:** baseline- and vehicle-controlled, Fridericia rate-corrected ddFPDc (MEA) or ddAPD90c (optical), counted arrhythmia-like events in four categories (A–D, "A" called mild) and quiescence. ddFPDc was not computed where ≥50 % of wells were arrhythmic.
- **Rate correction:** Fridericia's formula "was used to correct" APD and FPD for beating rate. The paper states that the formula is "not thoroughly validated for hiPSC-CMs" but widely used in these assays.
- **Modelling:** seven candidate predictors; logistic regression model 1 (low vs intermediate+high) and model 2 (high vs low and intermediate vs low). For modelling, ddFPDc (MEA) and ddAPD90c (optical) were treated as equivalent. Validation by 10-fold cross-validation and 500 bootstrap runs.

## Findings
- **Predictors retained:** arrhythmia-like events at any concentration (predictor 1), maximum ddFPDc/ddAPD90c at any tested concentration (predictor 4), and estimated ddFPDc/ddAPD90c at clinical Cmax (predictor 7). The two last are exactly the ones reused as the two features in [[wiki/papers/pramudito-2026-ensemble.md]] (maximum and at Cmax).
- **Performance:** model 1 AUC 0.872 (bootstrap 0.865, 10-fold CV 0.862); model 2 AUC 0.826 in one passage and 0.819 (bootstrap 0.808) in another (the paper is not consistent). Somers' D 0.74 and 0.65. At a 0.8 threshold in model 1: specificity 0.89, sensitivity 0.63.
- **Misclassified drugs:** bepridil (high risk, little arrhythmia), ranolazine and mexiletine (low risk but repolarization effects/arrhythmia, attributed to low late sodium current in hiPSC-CMs), metoprolol (beta-blocker in uninnervated cells), and intermediate risperidone, terfenadine, chlorpromazine, clozapine fell below the 0.8 threshold.
- **Variability:** site contributed less variability (root mean squared error 170 ms) than cell line (245 ms) and much less than concentration (482 ms); most sites correlated 78–88 %, sites 2 (the only optical, serum-free site) and 4 about 69–70 %. Site 4 saw no dofetilide effect, which the authors take as an argument for a positive-control drug on every plate. Cell line was not significant (p = 0.089). The design had no power to compare platforms.

## Limitations
Stated by the authors: free drug concentration not measured and some drugs poorly soluble in DMSO; drug metabolites not covered; measuring FPD of hERG blockers is hard because T-wave amplitude falls as FPD lengthens; only 30-minute exposures (no trafficking effects); not powered to compare devices; only two cell lines; hiPSC-CM immaturity (depolarized membrane potential, low late sodium current, high calcium channel expression) limits prediction for multichannel blockers.

Our observations:
- The rate correction is Fridericia only; no alternative correction was compared, and a single formula was applied across five platforms and two cell lines.
- Pooling FPD (MEA) and APD90 (optical) as equivalent in the regression is a strong assumption that matters to anyone reusing the dataset as "MEA ΔFPDc".
- Cross-validated and bootstrap AUCs are model-fit estimates on the same 28 drugs, not held-out performance, so they are not directly comparable with test-set AUCs in later ML papers.

## Relevance to our paper
(1) **Rate correction:** a primary-source statement that Fridericia is not thoroughly validated for hiPSC-CMs but is the field's convention, which supports the FPDc gap section in main.md. (2) **Dataset provenance:** it is the dataset behind [[wiki/papers/pramudito-2026-ensemble.md]], so Pramudito's ΔFPDc features are Fridericia-corrected and may pool MEA and optical readouts; also behind the 28-drug design of [[wiki/papers/park-2026-genotype-ml.md]] (concentrations taken from this study). (3) **Quality criteria and equilibration:** concrete inclusion criteria (20–90 bpm, beat-period CV <5 %, spike >0.3 mV, ≥30 min re-equilibration); whether that equilibration is sufficient in light of the drift reported in [[wiki/papers/guerrelli-2024-hipscm.md]] is an open question (interpretation, not tested here). Cite only as 2018 background; it is not a 2022+ methodological advance.

## See also
- [[wiki/papers/pramudito-2026-ensemble.md]]
- [[wiki/papers/park-2026-genotype-ml.md]]
- [[wiki/papers/guerrelli-2024-hipscm.md]]
- [[wiki/papers/ismaili-2023-hamburg.md]]
- [[wiki/papers/altrocchi-2023-chronic.md]]
