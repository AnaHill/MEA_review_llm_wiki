---
tags: [in-silico, 3d-model, disease-model, conduction-velocity]
---

# In silico modelling of multi-electrode arrays for enhancing cardiac drug testing on hiPSC-CM heterogeneous tissues

**Authors:** Sofia Botti, Rolf Krause, Luca F. Pavarino  
**Year:** 2026 (volume 604, issue 19, issue date 1 Oct 2026; received 14 Nov 2024, accepted 25 Mar 2025, published online 11 May 2025)  
**Venue:** The Journal of Physiology 604(19):8141–8166 (open access, CC BY). The year follows the issue year, as for the other entries; the online date is 2025.  
**File:** [[raw/botti-2026-insilico.pdf]] (+ [[raw/botti-2026-insilico-peer-review-history.pdf]]; CC BY)  
**DOI:** 10.1113/JP287276  
**Affiliations:** Euler Institute, Università della Svizzera Italiana; University of Pavia; UniDistance Brig; KAUST. No competing interests declared.

> **Note:** Full text read 2026-10-18 from the open-access Europe PMC version of the article (PMC13628577) before the version-of-record PDF (J Physiol 604.19, pp. 8141–8166) was added to raw/; the PDF's title page was checked against it, and the page's statements should be verified against the PDF. Figures not inspected. The published peer review history (submitted 14 Nov 2024, accepted 25 Mar 2025, two referees, one of them named) was only skimmed. Replaces the earlier metadata-only stub, whose method details were guesses.

## Contribution
A computational framework that couples a two-dimensional bidomain model with a model of the electrode (the Multi Channel Systems 60-6well MEA: six wells of nine electrodes) and phenotype-specific hiPSC-CM ionic models, to simulate field potentials, activation, repolarization and conduction velocity in heterogeneous monolayers. It is used to study the effect of the atrial-like (AL) / ventricular-like (VL) mixture, two Brugada syndrome (BrS) cases and four ion-channel blockers.

## Methodology
- **Tissue model:** parabolic–elliptic bidomain formulation in 2D, isotropic conductivity (σi 0.01 and σe 0.1 mS/cm, chosen so that conduction velocity is about 4 cm/s, matching earlier MEA data); electrode current from a resistor–capacitor equation; finite elements with 30 µm mesh; about 3 h per simulation on 32 threads.
- **Cells:** VL cells with the Paci2020 ionic model; AL cells with the authors' own Botti2024 model (atrial IKur and IKCa, reduced gK1 to allow spontaneous firing). The standard culture is taken as 30 % AL cells (from Altomare et al.), randomly placed; a pacemaker group in one corner starts the wave.
- **Brugada cases:** BrS1 (SCN5A-like: INa 70 %, ICaL 90 %, Ito 110 % of normal) and BrS2 (CACNA1C V2014I loss of function with shifted gating), both applied to VL cells.
- **Drugs:** mexiletine, nifedipine, dofetilide and E-4031 as IC50 pore-block models with Hill coefficient 1. The simulated effects are compared with **published** experimental MEA data from Abbate et al. and Millard et al.; no new experiments were done. Drug simulations use the fixed 30 % AL culture.

## Findings
- **Heterogeneity:** conduction velocity rises with the AL fraction; AL tissue repolarizes about 100 ms earlier than homogeneous VL tissue; heterogeneous mixtures give less smooth activation, repolarization and APD isochrones.
- **Brugada:** both cases give ST-segment elevation and a markedly positive T wave in the simulated FP; average conduction velocity falls from 4.27 to 3.59 cm/s for BrS1 and is unchanged for BrS2.
- **Drugs:** simulated mexiletine reduces spike amplitude and shortens APD (via ICaL block) with little FPD effect at the highest concentrations; dofetilide and E-4031 prolong APD/FPD; nifedipine shortens FPD. For the AL cell model the effects of ICaL and IKr block are almost imperceptible. The agreement with the published data is described qualitatively; no error metric is given in the text read.

## Limitations
Stated by the authors: no newly acquired experimental data; isotropic tissue only; uniform random AL/VL distribution only; quantitative FP analysis needs precisely defined biomarkers; the bidomain model is less accurate than cell-by-cell EMI models at the micrometre scale.

Our observations:
- It models a 2D monolayer MEA well, not 3D tissue, so it is not evidence about 3D heuristics.
- The drug simulations use a single heterogeneity setting (30 % AL), and the heterogeneity simulations contain no drugs; it does not predict drug effects across AL/VL mixtures.
- The model validation is qualitative and against earlier data.

## Relevance to our paper
Cited in main.md as an in silico approach for MEA signals. Its value for the review is that (1) the model predicts different conduction and repolarization behaviour for atrial-like and ventricular-like monolayers, which is relevant to the cell-identity confound of the atrial-like Brugada lines in [[wiki/papers/park-2026-genotype-ml.md]] (a modelling prediction, not data), and (2) it states that FP analysis remains hard to standardize because of variability from cell density, culture conditions, electrode placement and heterogeneity.

## See also
- [[wiki/papers/matsuda-2025-uhd.md]]
- [[wiki/papers/hwang-2023-spheroids.md]]
- [[wiki/papers/ernault-2024-interpretation.md]]
- [[wiki/papers/maurissen-2024-mutation.md]]
- [[wiki/papers/park-2026-genotype-ml.md]]
