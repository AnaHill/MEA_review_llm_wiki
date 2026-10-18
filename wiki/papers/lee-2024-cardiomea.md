---
tags: [open-platform, disease-model, high-throughput, machine-learning]
---

# CardioMEA: comprehensive data analysis platform for studying cardiac diseases and drug responses

**Authors:** Jihyun Lee, Eliane Duperrex, Ibrahim El-Battrawy, Alyssa Hohn, Ardan M. Saguner, Firat Duru, Vishalini Emmenegger, Lukas Cyganek, Andreas Hierlemann, Hasan Ulusan  
**Year:** 2024  
**Venue:** Frontiers in Physiology 15:1472126 (published 30 Oct 2024; open access, CC BY)  
**File:** [[raw/lee-2024-cardiomea.pdf]]  
**DOI:** 10.3389/fphys.2024.1472126  
**Affiliations:** ETH Zürich; Ruhr-University Bochum; University Heart Center and University of Zürich; University Medical Center Göttingen; German Centre for Cardiovascular Research. Financial support: ETH Domain PHRT and the Swiss National Science Foundation. One author declares industry fees and grants; the other authors declare no conflicts. English editing used ChatGPT 4 (disclosed).

> **Note:** Full text read 2026-10-18 from the Europe PMC version (PMC11557525, CC BY); the 62 MB PDF in raw/ was not machine-readable and figures were not inspected. Replaces the earlier metadata-only stub.

## Contribution
An open-source Python platform designed for **high-density MEA (HD-MEA)** data from iPSC-CMs. It processes recordings in parallel into an SQL database, provides a web-based interactive dashboard, extracts features from both extracellular field potentials and **intracellular-like signals** (obtained by electroporation on the same chip), and adds an automated machine-learning module for ranking features that separate diseased from control lines. The authors state it is the first open-source platform to process intracellular-like HD-MEA signals, and compare it with CardioMDA, MultiElec and Cardio PyMEA (Table 3 of the paper).

## Methodology
- **Software:** Kedro pipelines, parallel processing on several CPUs, PostgreSQL storage of features with timestamps, web dashboard (no-code); code on GitHub, data on Zenodo.
- **Hardware and cells:** MaxWell HD-MEA, 26,400 electrodes and 1,024 readout channels (the 1,020 electrodes with the largest signals were used for extracellular data, 200 for electroporation). SQT5 iPSC line (CACNB2 variant) with its CRISPR-corrected isogenic control, plus commercial iCell cardiomyocytes.
- **Features (Table 1):** extracellular — R-spike amplitude and width, **FPD defined as the distance between the R spike and the T-wave peak**, conduction speed (cone-shaped surface fit), heart-rate-variability measures, number of beats, active area; intracellular-like — AP amplitude, depolarization time, APD50, APD90. The table contains **no rate-corrected FPD**.
- **Drugs:** seven antiarrhythmics on SQT5 cultures with sequential additive dosing at 45-min intervals (quinidine, flecainide, disopyramide, ivabradine, amiodarone, sotalol, ranolazine); nifedipine, quinidine and sotalol on iCell cardiomyocytes using intracellular-like signals.
- **ML demonstration:** auto-sklearn (ensembles disabled) with permutation feature importance on 93 SQT5 and 33 corrected cultures, after removing redundant features (correlation >0.8, multicollinearity >5, visual similarity).

## Findings
- **Pharmacology:** quinidine, disopyramide and sotalol prolonged FPD in SQT5 cultures, flecainide, ivabradine, amiodarone and ranolazine had little or no effect; quinidine slowed conduction. In iCell cardiomyocytes nifedipine shortened APD50/APD90, quinidine lengthened depolarization time and APD90, sotalol raised APD50/APD90.
- **FPD versus action potential features:** using 3,987 electrodes from 29 iCell cultures with both signal types, FPD (R-to-T-peak) correlated minimally with APD50, APD90 and the other AP features; the authors attribute this to noise and very small T-waves that make T-wave detection imprecise. By contrast APD50 and APD90 from the HD-MEA and from patch clamp agreed strongly in simultaneous recordings of two cells.
- **ML demonstration:** the best model (multilayer perceptron) reached 98.9 % training and 92.0 % test accuracy (3-fold stratified cross-validation) against 71.8 % ± 1.8 % for a majority-class baseline and 80.1 % ± 5.3 % for a default perceptron. R-spike width and FPD were the most important features; the median R-spike width was lower in SQT5, opposite to the authors' expectation, and the statistics were inconclusive because of large spread.

## Limitations
Stated by the authors: electrode-level values should not be treated as independent replicates (use biological replicates); R spikes clip at high gain and lower gain would shrink the already small T wave; T-wave and FPD detection is hard in small-T-wave preparations; 3D models and T-wave shape analysis are future modules.

Our observations:
- The demonstration rests on a single isogenic pair and one commercial line; the number of independent differentiations behind the 126 cultures and how train and test cultures were separated are not stated in the text read.
- The platform targets HD-MEA hardware and signal types that most MEA studies in this wiki do not use, so it complements rather than replaces tools for conventional MEAs.
- The feature set offers no rate-corrected FPD, so users must add FPDc themselves.

## Relevance to our paper
(1) An open platform with an explicit FPD convention (R spike to T-wave peak, the same as PhysioMEA), which corrects the earlier Table 1 entry "FPD end: NA". (2) Direct evidence in hiPSC-CMs that R-to-T-peak FPD tracked action potential duration poorly in iCell HD-MEA recordings, which bears on the T-peak-versus-baseline-return debate (Ernault's correlation was shown for biphasic T waves in NRVM). (3) No rate correction in the shipped feature set, consistent with the FPDc gap. (4) The comparison table of open platforms is a useful cross-check for our Table 1.

## See also
- [[wiki/papers/dunham-2022-cardiopyemea.md]]
- [[wiki/papers/matsuda-2025-uhd.md]]
- [[wiki/papers/weiser-bitoun-2026-physiomea.md]]
- [[wiki/papers/kabanov-2026-cardioscripts.md]]
- [[wiki/papers/ernault-2024-interpretation.md]]
