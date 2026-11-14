---
tags: [cardiac-safety, rate-correction]
---

# International multisite study of human-induced pluripotent stem cell-derived cardiomyocytes for drug proarrhythmic potential assessment

**Authors:** Ksenia Blinova, Qianyu Dang, Daniel Millard, Godfrey Smith, Jennifer Pierson, Liang Guo, Mathew Brock, Hua Rong Lu, Udo Kraushaar, Haoyu Zeng, Hong Shi, Xiaoyu Zhang, Kohei Sawada, Tomoharu Osada, Yasunari Kanda, Yuko Sekino, Li Pang, Tromondae K. Feaster, Ralf Kettenhofen, Norman Stockbridge, David G. Strauss, Gary Gintant  
**Year:** 2018  
**Venue:** Cell Reports 24(13):3582–3592 (published 25 Sep 2018; open access, CC BY-NC-ND). Issue number taken from the reference list of Park et al. 2026 (supplementary); the PDF itself prints only "24".  
**File:** [[raw/blinova-2018-multisite.pdf]]  
**DOI:** 10.1016/j.celrep.2018.08.079  
**Affiliations:** US FDA (CDRH, CDER, NCTR), AbbVie, Axion BioSystems, Genentech, Janssen, Merck, Bristol-Myers Squibb, ACEA, Eisai, Cellular Dynamics, Ncardia, University of Glasgow and others (10 test sites).

> **Note:** Full text read 2026-10-18 via text extraction; main-article Figures 1, 2, 5, 6 and 7 viewed as rendered pages (Figures 3 and 4 follow the format of Figure 2). The Supplemental Information (Tables S1–S8, Figures S1–S3) is included as pages 13–23 of the raw PDF. Supplemental Data S1–S3 were checked separately on 2026-11-02 (see "Supplementary material" below). Outside our primary 2022–present window; kept as foundational context because it is the source dataset of [[wiki/papers/pramudito-2026-ensemble.md]] and states the FPD rate-correction convention behind that dataset.

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

### Figure notes
- **Fig. 1:** representative MEA and optical traces for the four arrhythmia-like event types (A, mild, to D) next to a control trace.
- **Fig. 2 (and 3, 4 in the same format):** per drug, per site/cell panel: drug-induced change in repolarization duration in **milliseconds** (Fridericia ddFPDc/ddAPD90c, left axis) against the four concentrations, with bars showing the fraction of wells with arrhythmic or quiescent events. For verapamil (low risk) the change is negative (shortening, up to about −300 ms) and the sites differ visibly in slope and in whether events occur at the top concentration.
- **Fig. 5:** dot plots of predictors 1, 4 (maximum repolarization change, up to about 1,400 ms) and 7 (change at Cmax, up to about 300 ms) for every drug and dataset; the spread within a drug across the 15 datasets is large compared with the separation between risk classes.
- **Fig. 6 and 7:** predicted risk per drug with 95 % intervals for models 1 and 2. In model 1 bepridil (about 0.64) and ranolazine (about 0.77) fall just below the 0.8 threshold, with risperidone, terfenadine, chlorpromazine, clozapine and mexiletine lower still.
- **Units:** ddFPDc here is an absolute change in ms, whereas [[wiki/papers/park-2026-genotype-ml.md]] works with percent change in FPDc, so the "ΔFPDc" of the two ML papers built on these concentrations are different quantities.

### Supplementary material
Checked 2026-11-02. The publisher's supplementary files are mmc1–mmc5. mmc5 is identical to the raw PDF, and mmc1 duplicates its pages 13–23, so neither adds anything. mmc2–mmc4 are not stored in `raw/`.
- **Table S1 (site conditions):** sites differed in plating density (8,000–72,000 cells per well), culture age on test day (5–10 days), recording medium (two serum-free media at sites 2, one per cell line; maintenance media elsewhere), time in recording medium (2–26 h) and maintenance antibiotics. Only site 10 used sequential dosing.
- **Table S3 (site variability):** root mean squared error 170 ms with site as a fixed effect, 36 ms with site as a random effect, against 67 ms for other errors. These are the numbers summarised under Findings.
- **Table S6 (cross-site correlation, iCell²):** Pearson correlations of ddFPDc/ddAPD90c between the 10 sites ranged from 0.37 (sites 2 and 4) to 0.95. Site averages were 0.69 for site 2, 0.70 for site 4 and 0.76–0.88 for the other sites.
- **Table S7 (solubility):** up to 7 of 10 sites reported solubility problems for a drug (clarithromycin 7, disopyramide 6, azimilide and ondansetron 5). Sites addressed them with sonication, 37 °C incubation or doubled DMSO (0.2 %).
- **Table S8 (model 1 by platform):** percent of drugs classified correctly per platform and cell line at cut-offs 0.6, 0.7 and 0.8. The authors state that platform effects cannot be separated from site effects, so the table does not compare platforms.
- **Figures S1–S3:** a worked prediction example, ROC curves for models 1 and 2, and drug-induced action-potential morphology changes. Figure S3 was not viewed.
- **Data S1–S3 (mmc2–mmc4):** one page per drug in the format of Fig. 2. Data S1 covers the 9 low-risk drugs, S2 the 11 intermediate-risk drugs and S3 the 8 high-risk drugs. Each page shows ddFPDc/ddAPD90c in ms and the fraction of wells with arrhythmia-like events at four concentrations for all 15 site/cell datasets. (The figures were not analysed: only the extracted text, the drug names, the axes and the concentrations were read.) They support no claim in main.md beyond what Tables S3 and S6 already give.

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
- [[wiki/papers/park-2025-cardiotoxicity.md]] — Fridericia-corrected FPD in drug testing of hiPSC-CMs
- [[wiki/papers/maurissen-2024-mutation.md]] — both report Fridericia-corrected FPD
- [[wiki/cipa.md]]
- [[wiki/fridericia-rate-correction.md]]
