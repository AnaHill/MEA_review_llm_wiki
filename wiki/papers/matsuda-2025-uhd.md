---
tags: [spatial-analysis, cardiac-safety]
---

# Advanced cardiotoxicity profiling using field potential imaging with UHD-CMOS-MEA in human iPSC-derived cardiomyocytes

**Authors:** Naoki Matsuda, N. Nagafuku, K. Matsuda, Y. Ishibashi, T. Taniguchi, Y. Matsushita, N. Miyamoto, T. Yoshinaga, I. Suzuki  
**Year:** 2025  
**Venue:** Toxicological Sciences 208(2):384–400  
**File:** [[raw/matsuda-2025-uhd.pdf]]  
**Supplementary:** [[raw/matsuda-2025-uhd-supplementary.docx]] (Supplementary Figure 1, legends of Movies 1–4; the movies themselves are not in raw/)  
**DOI:** 10.1093/toxsci/kfaf134

## Contribution
Demonstrates that a Sony ultra-high-density CMOS-MEA (UHD-CMOS-MEA) with 236,880 electrodes over a 5.9 × 5.5 mm active area can generate field potential images (FPI) at near single-cell resolution from hiPSC-CM monolayers, enabling endpoints (excitation origins, propagation area, conduction velocity) that the authors could not calculate in 46.5–78% of wells on a 16-electrode conventional MEA. The authors call FPI a "next-generation" myocardial MEA assay and note that CiPA primarily targets acute toxicity (p. 2); they do not propose adding the endpoints to CiPA.

Note: page checked against the source text on 2026-10-24; statements not supported by the paper were removed or reworded. Checked claim by claim 2026-11-14; page numbers in the text below are PDF pages (PDF p. 1 = journal p. 384).

## Methodology
- Platform: Sony UHD-CMOS-MEA (236,880 electrodes over 5.9 × 5.5 mm; 11 µm electrodes, 0.25 µm spacing, 91.9% coverage; 2 kHz sampling, 2-min recordings); cells seeded on a single chip (100,000 cells per chip)
- Cells: cryopreserved iCell Cardiomyocytes (FUJIFILM Cellular Dynamics), tested at DIV 7–10
- Endpoints derived from FPI:
  - **Excitation origins** — earliest activated electrode clusters, reported as the average number of origins per beat
  - **Propagation area** — number of electrodes that detected field potentials during each beat (mm²)
  - **Conduction velocity (CV)** — mean CV and beat-to-beat variability
- Pharmacology: 11 compounds (9 cardiotoxic, 2 negative controls: aspirin and amoxicillin), grouped as hERG, hERG+CaV, hERG+NaV, CaV, IKs and isoproterenol; classified by 17 parameters (PCA/MANOVA). Only the 7 compounds used on the conventional MEA are called commonly included in CiPA assessments (p. 3).
- Direct comparison with a conventional 16-electrode MEA system (beat frequency, inter-beat interval, spike amplitude); the paper does not report FPD or rate-corrected FPD for its own recordings (FPDc appears only in a table of thresholds taken from earlier studies)

### Supplementary material
Viewed 2026-11-14 (text and the one figure extracted from the .docx).
- **Supplementary Figure 1:** raw values over 72 h of 0.1 µM doxorubicin on the conventional MEA (n = 4) and the CMOS-MEA (n = 5). (A) Conduction velocity: CMOS-MEA about 0.13 mm/ms at baseline, falling significantly from 24 h (to about 0.09 mm/ms at 72 h); conventional MEA about 0.21 mm/ms, no significant change. (B) Spike amplitude: conventional MEA about 1.65 mV, falling significantly at 48 h and 72 h (to about 1.0 mV); CMOS-MEA about 0.65 mV at baseline with a very large SD, falling to about 0.27 mV without a significance mark. This is the figure behind the Discussion sentence on p. 395.
- **Absolute values differ between the platforms** in the same experiment design (conduction velocity about 0.21 versus 0.13 mm/ms; spike amplitude about 1.65 versus 0.65 mV at baseline). The paper does not comment on this; our observation.
- **Movie legends 1–4:** propagation of one beat (2 kHz, shown at 10 frames/s); isoproterenol 30 nM raising the number of excitation origins; mexiletine 10 µM lowering conduction velocity and amplitude; EAD-like and arrhythmic propagation after E-4031 at **30 nM**, whereas the main-text Fig. 4C caption gives 100 nM for the EAD-like waveforms (p. 391), so the source is inconsistent on the E-4031 concentration.
- **Affiliation:** the supplement names the second affiliation as Eisai Co., Ltd. (Tsukuba); the article gives only the unit name.

## Findings
- Isoproterenol raised the mean number of excitation origins per beat (1.51 at 10 nM, 1.61 at 30 nM, versus one origin at baseline), which the authors say suggests EAD/DAD-type effects (p. 9); the paper does not mention re-entry.
- Propagation area fell with E-4031 (17.98 to 6.51 mm²; the paragraph starts at 100 nM and gives the CV of the area "at 30 nM", so the concentration of the mean value is ambiguous, p. 388) and with mexiletine, disopyramide and quinidine; isoproterenol decreased its variability (p. 5).
- Mexiletine lowered mean CV from 0.147 to 0.109 m/s with increased beat-to-beat variability (p. 5).
- Bepridil effects (IBI, amplitude and CV variability) and mexiletine CV/area reductions seen on the CMOS-MEA were not detected on the conventional 16-electrode MEA (p. 6). No FPD was measured.
- Doxorubicin: the abstract states that 0.03 µM was detected within 24 h by reductions in conduction velocity and propagation area, whereas the Results (p. 9) and Discussion (p. 15) name only beat area (propagation area) and peak potential at 0.03 µM and CV at 0.1 µM, so the source is internally inconsistent on CV at 0.03 µM. The authors describe 0.03 µM as 10-fold lower than earlier studies and detected earlier (p. 398); those earlier studies used other readouts and partly other species (Ca²⁺ handling and contractility in mouse and rat cardiomyocytes at micromolar concentrations, force in iPSC-derived engineered heart tissue at 1 µM, deep-learning morphology of hiPSC-CMs above 0.3 µM), not MEA. At 0.1 µM the conventional MEA detected a spike amplitude reduction at 48 h and the CMOS-MEA a CV decline at 24 h (p. 12).

## Limitations
Stated by the authors (p. 15): all recordings were spontaneous beating without pacing, so rate-dependent endpoints may be confounded; a stimulation upgrade is under way. Disclosed (p. 16): the system is from Sony Semiconductor Solutions, the work was funded by Sony, and some authors are VitroVo employees or board members; the supplement names the second affiliation as Eisai Co., Ltd.

Our observations (not from the paper): the paper defines risk zones from the SD of the negative controls rather than validated regulatory cut-offs, and does not discuss data volume.

## Relevance to our paper
Cited in main.md for the multi-parameter feature-set shift and for the UHD-CMOS-MEA with about 236,880 electrodes, its spatial endpoints and the 0.03 µM doxorubicin result. The "state of the art" framing is ours.

## See also
- [[wiki/papers/botti-2026-insilico.md]]
- [[wiki/papers/maurissen-2024-mutation.md]]
- [[wiki/papers/altrocchi-2023-chronic.md]]
- [[wiki/papers/pramudito-2026-ensemble.md]]
- [[wiki/papers/lee-2024-cardiomea.md]]
- [[wiki/cipa.md]]
- [[wiki/fridericia-rate-correction.md]]
