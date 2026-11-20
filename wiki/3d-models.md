---
tags: [type/concept, 3d-model]
---

# 3D cardiomyocyte models and MEA recording

Concept page, written 2026-11-14 from the wiki paper pages and the three-dimensional models section of main.md. 3D models here include spheroids, organoids, engineered tissue sheets and microtissues.

| Source | What it adds |
|---|---|
| [[wiki/papers/maki-2023-opinion.md]] | caution that analysis frameworks optimised for 2D monolayers may not transfer directly to 3D models |
| [[wiki/papers/hwang-2023-spheroids.md]] | simulations of hiPSC-CM spheroids on MEAs (human ventricular cell model): FP shape varied strongly with stimulation and electrode locations even with a single cell type; the authors infer that three-dimensionality contributes to FP variability |
| [[wiki/papers/maurissen-2024-mutation.md]] | gene-edited KCNH2 lines recorded as 2D monolayers and as 3D cardiac tissue sheets on MEAs; Fridericia-corrected FPD close in both formats; TdP-like waveforms reported in the 3D sheets (cardiomyocyte purity 25–41 %) |
| [[wiki/papers/lin-2023-nanoelectronics.md]] | tissue-embedded stretchable electrodes in 3D microtissues; the authors argue that conventional MEAs contact a 3D microtissue only at one surface and lose contact as it contracts |
| [[wiki/papers/kim-2026-organoid-mea.md]] | a 4 µm conformable six-electrode MEA in the concave floor of a scoop well, so a patient-derived hiPSC organoid settles on it under gravity; contact confirmed by an impedance drop at 300 Hz, channels differ in amplitude and shape, and E-4031 prolonged FPD — but no FPD fiducial definition is stated anywhere in the paper or its supplement, and repolarization metrics are reported only where the morphology was judged to allow it |
| [[wiki/papers/weiser-bitoun-2026-physiomea.md]] | PhysioMEA, an open analysis platform designed for cardiac organoids on MEAs; the organoids are seeded directly onto the plate inside a 1.5 mm² ring and the analysis is planar, and the paper never describes the construct as three-dimensional |
| [[wiki/papers/correia-2024-acc2.md]] | engineered heart tissue microtissues in maturation medium (force and kinetics, not MEA) |
| [[wiki/papers/vuorenpaa-2023-mps-building-blocks.md]] | review of cardiac microphysiological systems, which can monitor several modalities concurrently |
| [[wiki/papers/botti-2026-insilico.md]] | for contrast: an in silico model of a 2D MEA well, not a 3D geometry |

**Open point (main.md, Conclusion gap 3):** no study examined compared fiducial definitions between 2D and 3D recordings systematically. Kim et al. (2026), added 2026-11-20, sharpens rather than closes this: the recording geometry advances while the analysis convention is left unstated, so acquisition is ahead of analytical validation.

## See also
- [[wiki/open-analysis-platforms.md]]
- [[wiki/fpd-end-conventions.md]]
- [[wiki/hipsc-cm-maturation.md]]
