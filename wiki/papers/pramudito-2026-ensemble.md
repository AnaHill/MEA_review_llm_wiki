---
tags: [machine-learning, cardiac-safety]
---

# Stacking ensemble machine learning for cardiac safety assessment using hiPSC-CM MEA data

**Authors:** Muhammad Adnan Pramudito, Yunendah Nur Fuadah, Yoo Seok Kim, Ki Moo Lim  
**Year:** 2026  
**Venue:** Annals of Biomedical Engineering 54:1334–1344 (received 23 Sep 2025, accepted 5 Jan 2026, published online 26 Jan 2026)  
**DOI:** 10.1007/s10439-026-03978-1  
**PubMed:** https://pubmed.ncbi.nlm.nih.gov/41586860/  
**File:** [[raw/pramudito-2026-ensemble.pdf]]  
**Affiliations:** Kumoh National Institute of Technology (Gumi, Korea); Telkom University (Bandung); Keimyung College University (Daegu); Meta Heart Co., Ltd. Competing interest declared: Lim is employed by Meta Heart.

> **Note:** Full text read 2026-10-18 (11 pages, figures viewed as rendered page images). Replaces the earlier abstract-only stub.

## Contribution
Asks whether a two-level stacking ensemble can make Torsades de Pointes (TdP) risk classification from hiPSC-CM MEA data more robust when only two simple ΔFPDc-derived predictors are available. Claims the stacking ensemble outperforms every single classifier and that the XGBoost-based meta-classifier reaches perfect discrimination on 16 held-out CiPA reference drugs.

## Methodology
- **Data:** the public CiPA MEA dataset of Blinova et al. 2018 (*Cell Reports* 24:3582–3592; their ref. 10), 28 CiPA reference compounds with 1–4 concentrations and replicate ΔFPDc values, plus clinical TdP risk labels (high / intermediate / low). **Raw MEA signals were not reanalysed**; the curated ΔFPDc values were used as provided. Only "normal cell-type" data were used. The paper does not state which FPD rate-correction formula underlies the dataset's ΔFPDc.
- **Predictors:** (1) maximum ΔFPDc over all tested concentrations; (2) ΔFPDc at clinical Cmax by linear interpolation (not computed when a drug has only one concentration).
- **Split:** by drug, 12 training drugs (4 high: sotalol, dofetilide, bepridil, quinidine; 4 intermediate: cisapride, chlorpromazine, terfenadine, ondansetron; 4 low: verapamil, ranolazine, diltiazem, mexiletine) and 16 test drugs (4 high, 7 intermediate, 5 low; Table 1).
- **Level 1:** random forest (200 trees), XGBoost (200 trees), and a small ANN (two hidden layers of 4 units, 15 weights listed in Table 5); grid search with 10-fold cross-validation split by drug. Each outputs three class probabilities; the nine probabilities form the level-2 features.
- **Level 2:** meta-classifier RF, XGBoost or SVM, same tuning strategy.
- **Evaluation:** 10,000 resamplings drawing one ΔFPDc sample per test drug; AUC1 (high+intermediate vs low), AUC2 (high vs intermediate+low), positive/negative likelihood ratios (epsilon added to avoid division by zero), pairwise accuracy, classification error. Overfitting check via train–validation ΔAUC with paired t-test and Wilcoxon. Computational benchmark on a MacBook M3.
- **Comparators:** Blinova 2018 logistic regression on ΔdFPDc (AUC 0.872–0.862) and Serrano et al. (deep-learning platform, AUC 0.95), taken from those papers' reported values.

### Figure and table notes
- **Fig. 1** (workflow): MEA ΔFPDc → preprocessing → 12 training drugs → level-1 RF/XGBoost/ANN → "new training dataset" of stacked predictions → level-2 meta-classifier → evaluation on the 16 test drugs → final prediction. The caption says "the best-performing base models" generate the test-set predictions.
- **Fig. 2**: generic schematics of RF (bootstrap, majority vote), gradient boosting (200 sequential trees fitted to residuals) and the ANN (2 inputs, 2×4 hidden units, 3 risk-class outputs). No data.
- **Fig. 3**: schematic of the 10,000-times resampling, listing the 16 test drugs by risk class (high: azimilide, disopyramide, ibutilide, vandetanib; intermediate: astemizole, clarithromycin, clozapine, domperidone, droperidol, pimozide, risperidone; low: loratadine, metoprolol, nifedipine, nitrendipine, tamoxifen). Each trial is a (16,1) vector, one sample per drug. This matches Table 1.
- **Tables 2–5** hold all quantitative results; there are no data plots (no ROC curves, no ΔFPDc dose-response plots, no feature importance).

## Findings
- **Base classifiers (16 test drugs, Table 3):** RF AUC1 = AUC2 = 0.817; XGBoost AUC1 0.883, AUC2 0.767; ANN AUC1 1.000 but with interval 0.250–1.000 and AUC2 0.750 (0.000–1.000), i.e. unstable. Pairwise accuracy 0.735 (RF), 0.676 (XGB), 0.667 (ANN).
- **Stacking (Table 4):** XGBoost-meta AUC1 = AUC2 = 1.000 (AUC1 interval 0.980–1.000), pairwise accuracy 1.000, classification error 0.000 (0.000–0.125). RF-meta AUC1 1.000, AUC2 1.000 (0.312–1.000). SVM-meta AUC1 1.000, AUC2 0.889 (0.675–1.000). Likelihood ratios reach about 10⁶ because of the epsilon term and are not meaningful as magnitudes.
- **Overfitting (Table 2):** RF and XGBoost fit training drugs clearly better than validation drugs (ΔAUC 0.253 and 0.148); ANN ΔAUC slightly negative (−0.021).
- **Cost (Table 5):** XGBoost-meta trains in 1.48 s, inference 0.0004 ms per sample, model 0.56 MB.
- **Practical-use claim:** ANN for early sensitive screening, RF/XGB for confirmatory work, stacked model for compound prioritisation.

## Limitations
Acknowledged by the authors: small dataset; the 10,000 resamplings of the same 16 drugs are pseudo-replicates, so the intervals describe within-drug variability, not generalisation to new compounds; only two predictors; single experimental condition and normal cell types; reduced interpretability; heavy training pipeline relative to inference; external validation on other MEA datasets still needed.

Our observations (from the text and tables as printed; none of these are claims by the authors):
- **"Perfect" AUC on 16 drugs is weak evidence.** With 4/7/5 drugs per class, one ordering change would change AUC visibly, and the resampling cannot add independent test drugs. The intervals therefore say little about performance on new compounds.
- **Possible leakage in the meta-features is not excluded.** The text says the base classifiers were "retrained using the 12 training drugs", their probabilities concatenated, and the meta-classifier trained on those. It does not say the meta-features were out-of-fold. RF fits its training drugs at AUC ≈ 0.99, so in-sample base predictions would be near-perfect inputs for the meta-learner. The paper does not clarify this.
- **Internal inconsistencies in the paper.** (a) RF training AUC is 0.9442 ± 0.0224 in the Results text but 0.9942 ± 0.0024 in Table 2; ΔAUC 0.2532 matches the table. (b) The ablation text gives the standalone XGBoost AUC1 as 0.833, Table 3 says 0.883. (c) Serrano et al. is labelled 2024 in Tables 3–4 but the reference list gives 2023 (Cell Stem Cell 30:86–95).
- **Comparison with Blinova 2018 is not like-for-like.** The logistic-regression figures are quoted from the original paper, not re-run on these 16 test drugs, and the base classifiers here (RF 0.817) score below that benchmark. "Significantly outperforming" is used without a statistical test.
- **The ML sits downstream of FPDc.** ΔFPDc comes pre-computed from a multisite dataset in which, per this paper's own introduction, responses varied substantially between facilities; the paper does not model platform or site. Any bias in the FPD definition or rate correction passes unexamined into the classifier.
- **Self-citation and novelty.** The stacking design follows the same group's earlier in-silico-biomarker stacking model (their ref. 26); the new element is applying it to two MEA ΔFPDc features.

## Relevance to our paper
Cited in main.md only as an example of ML integration with MEA data for TdP risk prediction (timeline entry and closing paragraph). That use is supported. Two cautions for the draft: (1) do not quote the perfect AUC as evidence of robust performance, given the limitations above; (2) the paper is an ML study on already-extracted ΔFPDc, not a signal-analysis study, so it supports our methodological argument only indirectly: classifier performance rests entirely on the FPDc definition and correction used upstream, which links to our FPDc rate-correction gap section (interpretation, not stated by the authors).

Possible leads from its reference list (taken from the paper's reference list; existence and details not independently checked, not ingested): Blinova et al. 2018 (*Cell Rep* 24:3582–3592, source of the dataset); Serrano et al. 2023 (*Cell Stem Cell* 30:86–95, deep-learning proarrhythmia platform); Park Y.G. et al. 2025 (*J Adv Res*, ML platform for genotype-specific cardiotoxicity with patient-derived iPSC-CMs; a different paper from our Park et al. 2025).

## See also
- [[wiki/papers/matsuda-2025-uhd.md]]
- [[wiki/papers/altrocchi-2023-chronic.md]]
- [[wiki/papers/park-2025-cardiotoxicity.md]]
- [[wiki/papers/weiser-bitoun-2026-physiomea.md]]
