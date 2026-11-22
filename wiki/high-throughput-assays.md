---
tags: [type/concept, high-throughput, cardiac-safety]
---

# High-throughput and long-term MEA assays

Concept page, written 2026-11-22 from the wiki paper pages and the "High-throughput and long-term assays" section of main.md. It covers what changes when an MEA assay is run over days rather than minutes, or over many wells and compounds rather than one plate: the recording conditions themselves start to move, and the analysis has to stay fixed while they do.

This was the one section of main.md with no concept page and no tag of its own; both were added on 2026-11-22 (see `wiki/log.md`).

| Source | What it adds |
|---|---|
| [[wiki/papers/altrocchi-2023-chronic.md]] | chronic assay, repeated recordings over four days, FP with impedance; vehicle wells drifted too — by 96 h mean beat rate had fallen 5.8 % and mean FPDc risen 7.9 % **despite** Fridericia correction, so compound effects were judged against per-time-point tolerance intervals from vehicle wells |
| [[wiki/papers/guerrelli-2024-hipscm.md]] | quantifies the confounds directly: a 20-minute equilibration window (rate up, FPD down) and 2–14 days in culture (rate down, FPD up). Recommends reporting culture and equilibration time — but its example datasheet has no field for the FPD definition or the rate correction |
| [[wiki/papers/matsuda-2025-uhd.md]] | ultra-high-density platform (about a quarter million electrodes): excitation origin counts, propagation area and conduction velocity maps alongside beat rate and inter-beat interval; doxorubicin detected at lower concentrations than in earlier studies, per the authors |
| [[wiki/papers/clements-2025-aims-poster.md]] | proposed acceptance criteria for wells in such assays (spike amplitude, synchronised beating, beat period, FPDc 200–700 ms); quality control, not maturation staging, and not peer reviewed |
| [[wiki/papers/lee-2026-ito-mea.md]] | two-day doxorubicin exposure where the beating slowed so much that Fridericia-corrected FPD fell while uncorrected FPD rose — the sharpest example of a long assay breaking a correction |
| [[wiki/papers/fetterman-2024-maturation.md]] | high-throughput dissection of medium components; not an MEA study, but the source of the finding that functional, metabolic and transcriptional maturation are induced largely independently |
| [[wiki/papers/park-2025-cardiotoxicity.md]], [[wiki/papers/park-2026-genotype-ml.md]] | screening applications: 8 drugs on healthy and long QT lines, then 28 compounds on patient-derived long QT and Brugada lines |

## Why this bears on the review's argument

Scale makes the analysis conventions matter more, not less. Three of these sources show a measured endpoint moving without the cells being treated: vehicle drift over four days (Altrocchi), equilibration and culture-time drift (Guerrelli), and a rate correction reversing the direction of a drug effect (Lee et al., 2026). Each is a case where the number changes because of when and how it was measured.

**Our observation, not the sources':** the same three sources also show that rate correction does not absorb these effects — Altrocchi's drift is in the Fridericia-corrected value, Guerrelli's FPD lengthened under fixed-rate pacing too, and in Lee et al. (2026) the correction is what flipped the sign. This is why the high-throughput material supports gap 1 rather than standing apart from it.

## See also
- [[wiki/fridericia-rate-correction.md]] — the correction these assays apply, and where it does not hold
- [[wiki/hipsc-cm-maturation.md]] — culture-time drift is the same phenomenon seen as maturation
- [[wiki/cipa.md]] — the multisite screening precedent
- [[wiki/multimodal-measurement.md]] — impedance recorded alongside the field potential (Altrocchi)
- [[wiki/machine-learning-mea.md]] — the large datasets these assays produce are what the classifiers are trained on
