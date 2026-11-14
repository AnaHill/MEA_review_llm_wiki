---
tags: [multimodal, machine-learning]
---

# Unsupervised machine learning-assisted multimodal characterization of cardiomyocytes on a thin-film-transistor microelectrode array (TFT-MEA)

**Authors:** Xingzhuo Hu, Junichi Sugita, Katsuhito Fujiu, Agnès Tixier-Mita, Hiroshi Toshiyoshi  
**Year:** 2026  
**Venue:** Biomedical Physics & Engineering Express 12, 045036 (received 7 January 2026, published 22 July 2026; the issue number is not printed in the PDF)  
**File:** [[raw/hu-2026-tft-mea-multimodal.pdf]] (not open access; git-ignored)  
**Supplementary:** [[raw/hu-2026-tft-mea-multimodal-supplementary.pdf]] (git-ignored)  
**DOI:** 10.1088/2057-1976/ae87aa

Note: ingested 2026-11-01 from the full text (11 pages, text extraction) and the 4-page supplement; Figures 2–7 viewed (pages 3, 5–7 rendered). The PDF carries "© 2026 IOP Publishing Ltd"; not open access (all rights reserved by the publisher). Affiliations: Institute of Industrial Science and Graduate School of Medicine, The University of Tokyo. It cites Ryynänen et al. (2018) as its reference [11].

## Contribution
A proof-of-concept framework that records extracellular field potentials and bright-field video of the same cardiomyocyte culture on a transparent thin-film-transistor MEA (TFT-MEA), extracts spike-related features from both, labels the recording into two states with k-means clustering, checks the labels with supervised classifiers and interprets them with SHAP. Isoprenaline is the main test; nifedipine is shown in the supplement. The authors call the workflow "a sensor fusion technique" (section 2.6) and state that "true sensor fusion ... remains underdeveloped" in the field (Introduction).

## Methodology
- **Cells:** primary prenatal (fetal) mouse cardiomyocytes, "rather than iPSC-derived cells" (section 2.1.2); seeded at 8.0 × 10⁶ cells/ml, 25 µl on the electrode area. No hiPSC-CMs are used.
- **Device:** TFT-MEA made with Sharp: 22,500 transparent ITO electrodes (150 × 150, 100 µm pitch, 15 × 15 mm² active area), one switching TFT per electrode, one culture chamber per chip. In this study only one gate line was powered and **10 adjacent electrodes** were recorded (USB-ME32-FAI, Multi Channel Systems, 10 kHz) for more than 4 min. Impedance can be measured with the same electrodes but is not used in the analysis.
- **Video:** inverted microscope, 30 fps; dense optical flow (Farnebäck), median motion magnitude per frame as a contraction trace. Videos were much shorter than the electrical recordings "due to software limitations" (about 18 s versus about 250 s in Fig. 4).
- **Time alignment:** not hardware-synchronised; the drug-addition time was recorded and used with the frame timestamps to align the two signals (section 2.3).
- **Features (Fig. 3):** peak-to-peak interval, R90 and R50 time to peak, R90 and R50 time from peak, peak width, defined on the fast spike. The text says they "quantify both depolarization and repolarization kinetics", but in Fig. 3 all time markers sit on the depolarization spike; there is no FPD or T-wave feature. Spike detection used a negative threshold "typically set at –70 mV" (as printed; probably µV).
- **ML:** k-means into two classes (normal; isoprenaline-influenced) with a window of 5 and smoothing of 15; supervised LR, random forest, naive Bayes, XGBoost and SVM trained on the k-means labels (random 80/20 split of feature vectors) "to assess the internal consistency of the k-means clusters ... rather than to provide an independent ground truth"; SHAP for feature importance.

## Findings
- **Fig. 4:** k-means applied to the peak-to-peak value separately for the optical (a) and the electrical (b) data; both switch from class 0 to class 1 after isoprenaline (shorter interval, faster beating).
- **Fig. 5:** LR accuracy 0.97 (F1 0.95), SVM 0.91 (0.87), random forest 0.83 (0.81), naive Bayes 0.85 (0.79), XGBoost 0.80 (0.70).
- **Fig. 6:** in the SHAP plots of LR and SVM, R50 time to peak ranks first, followed by R90 time from peak and R90 time to peak; peak-to-peak time and peak width rank low. All six features listed are electrical spike features; no optical feature appears in the plot. Example waveforms (Fig. 6c, d) show a slower, larger repolarization wave before than under isoprenaline.
- **Fig. 7:** SHAP importance vectors correlate between models (0.86–1.00).
- **Supplement (response letter and Figs S1–S4):** nifedipine lowered the beating rate and the number of events in a fixed recording, which made the unsupervised analysis "less stable and less statistically convincing"; it is therefore given only as supportive evidence.
- **Throughput:** one recording (>4 min, 10 kHz, 10 electrodes) processed in under 1 min on a laptop.

## Limitations
Stated by the authors: a proof of concept; "broader validation across larger numbers of independent replicates and batches will be required"; one well per chip limits throughput; mouse fetal cells, with developmental-stage and preparation variability; future work should use CiPA-style reference compounds, repolarization and proarrhythmia endpoints and viability assays.

Our observations (not from the paper): the number of cultures, chips or recordings is not reported; the labels are derived from the same recording and checked against the drug-addition time, so the 97 % accuracy measures agreement with k-means clusters on one dataset, not prediction on independent data; the "fusion" is shown as separate clustering of each modality (Fig. 4), and the SHAP plots list electrical features only, so how far optical and electrical features were combined in one model is unclear from the paper; the features are depolarization- and rate-based, not FPD; the cells are not hiPSC-CMs.

## Relevance to our paper
Cited in main.md from 2026-11-01: in the sensor-fusion part of the Discussion and future outlook (with its limits stated) and in Limitations (ii) as evidence in fetal mouse cells.

Directly relevant to the sensor-fusion part of the Discussion and future outlook: it is a published attempt to analyse simultaneous MEA and video recordings of the same culture jointly with interpretable machine learning, on a transparent MEA in the line of Ryynänen et al. (2018). It qualifies the outlook's observation that the modalities "are mostly analysed separately", but it does not settle the hypothesis: mouse fetal cells, 10 electrodes, a single proof-of-concept experiment, labels tied to one drug's onset, no repolarization features, and an unclear degree of feature-level fusion. Outside the hiPSC-CM scope of the review, so it belongs in the outlook as an example, not among the reviewed hiPSC-CM developments.

## See also
- [[wiki/papers/ryynanen-2018-single-cell-mea.md]]
- [[wiki/papers/hayakawa-2014-motion-fp.md]]
- [[wiki/papers/scheurer-2025-optical-ai.md]]
- [[wiki/papers/lin-2023-nanoelectronics.md]]
- [[wiki/multimodal-measurement.md]]
- [[wiki/machine-learning-mea.md]]
