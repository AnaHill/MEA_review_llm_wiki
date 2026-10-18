---
tags: [machine-learning, disease-model, lqts, cardiac-safety, rate-correction]
---

# A machine learning platform for genotype-specific cardiotoxicity risk prediction using patient-derived iPSC-CMs

**Authors:** Yun-Gwi Park, Na Kyeong Park, Youngsun Lee, Muhammad Adnan Pramudito, Yeo-Jin Son, Hyeyeon Park, Ali Ikhsanul Qauli, Seong Woo Choi, Kiwon Ban, Jong-Il Choi, Soon-Jung Park, Hun-Jun Park, Ki Moo Lim, Soo Kyung Koo, Jung-Hyun Kim, Sung-Hwan Moon (first three authors contributed equally)  
**Year:** 2026 (volume 82; published online 22 Jul 2025, received 11 May 2025, accepted 16 Jul 2025)  
**Venue:** Journal of Advanced Research 82:381–396 (open access, CC BY-NC-ND). Year follows the volume year; the paper itself and Pramudito 2026 (ref. 20) use 2025 as the online year, so check the target style.  
**File:** [[raw/park-2026-genotype-ml.pdf]] (+ [[raw/park-2026-genotype-ml-supplementary-methods.docx]], [[raw/park-2026-genotype-ml-supplementary-dataset-s1.pdf]])  
**DOI:** 10.1016/j.jare.2025.07.030  
**Affiliations:** Chung-Ang University, Biosolvix, Korea National Institute of Health / Korea National Stem Cell Bank, Kumoh National Institute of Technology, Dongguk University, Catholic University of Korea, Ajou University and others. Lim is listed with Metaheart Co. Ltd; the paper declares no competing interests.

> **Note:** Full text and the two supplementary files read 2026-10-18 (text extraction plus all eight main-article figures viewed as rendered pages; supplementary Data set S1 page 4, mexiletine, viewed as an image; the 11 videos and csv files were not downloaded). **Overlaps with [[wiki/papers/park-2025-cardiotoxicity.md]]** from the same group; see Relevance.

## Contribution
Builds a machine-learning platform for TdP risk prediction on MEA data from patient-derived iPSC-CMs with long QT syndrome (LQTS) and Brugada syndrome (BrS), plus normal lines. Claims that disease-matched training gives the best prediction (ANN, AUC 0.94) and that disease lines reveal hypersensitivities (BrS to calcium channel blockers, LQTS to potassium channel blockers) and reclassify several drugs.

## Methodology
- **Cell lines:** from the Korean Inherited Arrhythmia Registry, 4 LQTS and 4 BrS patients (QTc ≥ 460 ms and/or documented TdP, VF or arrest), reprogrammed from blood, differentiated with a CHIR/Wnt-C59 protocol and lactate purification. Genotyped (variants in KCNH2, KCNQ1 for LQTS; SCN5A, KCNE1, CACNB2b, ANK2 for BrS) and functionally screened by patch clamp at day 15. Three of the eight mutation-carrying lines (DPHCi02, DPHKi08, DPHKi11) failed to show a disease phenotype and were excluded. Retained: LQTS DPHCi01 (KCNH2 c.453delC frameshift), DPHCi08 and DPHKi20 (KCNQ1 substitutions); BrS DPHCi15 and DPHKi09. Normal lines: iCell, CMC-011, PB01, TnR-4F.
- **MEA:** Axion Maestro Pro, 96-well Cytoview plates; two independent 5-min recordings around 30 min of drug exposure; one concentration per well, at least 3 replicates; analysed with Axion's Cardiac Analysis Tool; FPD corrected with Fridericia's formula (FPDc). Concentrations taken from Blinova et al. 2018.
- **Drugs:** 28 compounds: 12 ion-channel blockers, 14 non-cardiovascular drugs with reported cardiotoxicity (26 with a classified TdP risk) plus amiodarone and remdesivir with no official classification, four concentrations each.
- **Quiescence rule:** where a drug stopped beating, FPDc was not measurable and was entered as a 100 % change ("Q").
- **ML input:** percent change in four biomarkers (FPD, FPDc, beat period, amplitude), averaged over the four concentrations ("data augmentation"); binary label high vs low/no TdP risk. ANN (Keras, two hidden layers), random forest and XGBoost tuned by grid search with 5-fold cross-validation. In each cell group 11 drugs train and 15 test.
- **Evaluation:** 10,000 test sets of the 15 drugs, median and 95 % interval; accuracy, AUC, sensitivity, specificity, F1, likelihood ratios (epsilon added). Scenarios: train/test within normal, LQTS, BrS, inherited arrhythmia, all lines; and normal-trained models tested on disease lines. A separate FPD20/FPDc20/BP20/Amp20 score (lowest concentration with ≥ 20 % change) converted to risk levels 0–4.

### Figure notes
- **Fig. 1:** table of all lines with sex, age, gene and variant (normal: CMC-hiPS-011 male, PB01-EiPS21 male age 50, TnR-hiPS-4F female age 19; LQTS: DPHCi01 female 55 KCNH2 c.453delC p.Thr152fs, DPHCi08 female 27 KCNQ1 c.569G>A, DPHKi20 male 20 KCNQ1 c.464T>G, DPHCi02 male 76 KCNH2 duplication; BrS, all male: DPHCi15 SCN5A two variants, DPHKi09 ANK2, DPHKi08 KCNE1, DPHKi11 CACNB2b), Sanger traces and karyotypes. The identical c.453delC variant supports that DPHCi01 is the line of Park 2025.
- **Fig. 2:** differentiation protocol timeline, TNNT2/MYH6 expression and flow cytometry; all lines >90 % TNNT2-positive.
- **Fig. 3:** patch-clamp subtype classification. The two retained BrS lines are atrial-like: DPHCi15 100 % and DPHKi09 87.5 % atrial-like, with no ventricular-like cells; normal lines about 70 % ventricular-like. LQTS APD80 prolonged (587, 308, 556 ms), BrS lines show short APD80 (119, 94 ms) and spike-and-dome loss.
- **Fig. 4:** MEA waveform cartoon defining FPD, FPDc, beat period and amplitude, then FPDc heatmaps for 12 ion-channel blockers. The colour scale runs 0–100 % change, so FPDc shortening (as with mexiletine and calcium blockers in the supplement) cannot be distinguished from no change, and quiescence appears as full 100 %.
- **Fig. 5:** the same heatmap format for 14 non-cardiovascular drugs.
- **Fig. 6:** workflow and model schematics (no data); training/test splits for eight scenarios (11 train drugs, 15 test drugs; normal-trained models tested on LQTS, BrS or both).
- **Fig. 7:** resampling schematic, accuracy/AUC/sensitivity boxplots, score distributions for training and test drugs, and a table of FPD20-type risk levels (0–4) per drug and line group. Labels used: 16 drugs high, 10 low (see below).
- **Fig. 8:** amiodarone and remdesivir FPDc heatmaps and ANN scores (boxes about 0.9–1.0, all lines); risk levels remdesivir 2.3 normal, 3.7 LQTS, 3.0 BrS.

## Findings
- **Headline performance (Table S4):** ANN trained and tested on LQTS lines: AUC 0.94 (95 % interval 0.81–1.0), accuracy 0.80 (0.67–0.93); same for LQTS+BrS combined; normal lines AUC 0.84–0.86 (0.63–1.0), accuracy 0.75; normal-trained models on disease lines AUC 0.74–0.78, accuracy 0.67–0.69. RF best for BrS-only, XGBoost best on all lines combined. Likelihood ratios reach about 750,000 because of the epsilon term.
- **Disease sensitivities (FPDc heatmaps):** potassium blockers (azimilide, sotalol) prolong FPDc in all lines; BrS lines are more sensitive to nifedipine, nitrendipine and diltiazem; ibutilide and quinidine behave differently across LQTS/BrS/normal; many low-risk drugs score higher in disease lines.
- **Reclassification claims:** clarithromycin, clozapine and loratadine (labelled low in this paper) scored high with the LQTS-trained ANN, and the authors read this as hidden risk in disease backgrounds; amiodarone and remdesivir scored high in all lines, highest in LQTS (≥ 0.8).
- **Phenotype penetrance:** three of eight mutation lines did not express the disease phenotype, so genotype alone was not sufficient.

## Limitations
Stated by the authors: MEA captures only extracellular field potentials (not re-entry or local conduction block); model quality depends on data quantity and quality; need for correlation with real-world clinical datasets.

Our observations (not claims by the authors):
- **Quiescence coded as a 100 % FPDc change.** The Data set S1 heatmap for mexiletine shows DPHCi08 quiescent at 10 and 100 µM; the main text's "exception" for mexiletine in DPHCi08 therefore reflects this coding, not repolarization prolongation. It also feeds the ML averages if included (not stated).
- **Averaging over concentrations is not augmentation.** One averaged sample per drug and line reduces data and mixes subtherapeutic and toxic effects.
- **Headline AUC rests on 15 test drugs and 2–3 lines**, intervals come from resampling the same test set (as in [[wiki/papers/pramudito-2026-ensemble.md]], co-authored by Pramudito); the intervals for normal and LQTS training overlap, so "genotype-specific" gains are not established statistically.
- **The binary labels differ from the CiPA three-class scheme and are not explained.** Fig. 7 labels 16 drugs high and 10 low. Nine CiPA-intermediate drugs (astemizole, chlorpromazine, cisapride, domperidone, droperidol, ondansetron, pimozide, risperidone, terfenadine) count as high, but clarithromycin and clozapine, also intermediate in [[wiki/papers/blinova-2018-multisite.md]], count as low. "Reclassified as high risk" therefore means "predicted high against this binary label"; the paper gives no mapping rule for intermediate drugs (it cites Passini 2017 for the labels). The Discussion also calls disopyramide "low risk", while its label, Fig. 7E and its median score (0.991) treat it as high.
- **The BrS lines are atrial-like cultures.** DPHCi15 and DPHKi09 have no ventricular-like cells (Fig. 3), and these two lines carry all the BrS-versus-normal comparisons (calcium-blocker hypersensitivity, ibutilide, ranolazine). Differences may reflect cell identity (atrial-like ICaL/IK balance) rather than the BrS variants. The authors argue from MYL2/MYL7 qPCR that the cells were not directed to an atrial fate and attribute the atrial-like action potentials to BrS itself. The lines were also selected because their action potentials looked BrS-like.
- **"Validation" on amiodarone and remdesivir has no ground truth.** Both drugs lack a risk classification, and the model returns "high" (about 0.9–1.0) for both in every line group; with a binary classifier trained on drugs that prolong FPDc, a high score cannot be checked against anything here.
- **The FPD20-type risk level (Fig. 7E) does not clearly separate classes in normal lines.** Low-risk verapamil and nitrendipine reach level 3.3, above several high-risk drugs (risperidone 1.3, pimozide and azimilide 1.8). The paper does not say whether shortening counts toward the ≥ 20 % threshold, which would explain this for calcium blockers.
- **Rate correction** is Fridericia without validation for hiPSC-CMs; disease lines have prolonged action potentials and different beat rates, so FPDc differences across lines may partly reflect the correction.
- Mutation lines were retained or dropped according to the phenotype the model later tries to predict, which can bias the disease-line results; sample sizes are small (2–3 lines per disease).

## Relevance to our paper
An MEA-based use of disease lines and ML, with FPDc as the core feature, so it fits the paragraph on machine learning in MEA workflows and the disease-model angle, but it is a safety-pharmacology paper rather than a signal-analysis one. Two cautions for the draft. (1) **Do not cite together with [[wiki/papers/park-2025-cardiotoxicity.md]] as independent confirmation:** same group, very probably the same KCNH2 c.453delC LQT2 line (Park 2025: DPHC01i-AR / DPHCi-01; here DPHCi01, supplementary refs 1 and 3), shared normal line CMC-011, four shared drugs (nifedipine, mexiletine, quinidine, ranolazine), same Axion Maestro Pro and Fridericia FPDc; this paper also extends Park 2025's FPD20/FPDc20 metric to four parameters. Whether recordings were reused is not stated, and neither paper cites the other. (2) Same lab and evaluation design as Pramudito 2026 (Pramudito is co-author). Concentrations and drug panel come from [[wiki/papers/blinova-2018-multisite.md]].

## See also
- [[wiki/papers/park-2025-cardiotoxicity.md]]
- [[wiki/papers/pramudito-2026-ensemble.md]]
- [[wiki/papers/blinova-2018-multisite.md]]
- [[wiki/papers/maurissen-2024-mutation.md]]
- [[wiki/papers/ismaili-2023-hamburg.md]]
