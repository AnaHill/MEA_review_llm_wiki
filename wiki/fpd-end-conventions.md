---
tags: [method, fiducial-definition, fpd]
---

# FPD start and end conventions in the reviewed papers

Method page, written 2026-10-24 from the wiki paper pages (each of which was checked against its source text). It lists only conventions that those pages document; papers whose FPD definition is not recorded on their page (for example Altrocchi, Hwang, Maurissen, Park, Blinova) are not listed. This page backs Table 2 of main.md; it adds nothing new to the evidence.

| Source | FPD start | FPD end | What the source says about it |
|---|---|---|---|
| [[wiki/papers/maki-2023-opinion.md]] (DatAnalyzer) | depolarization onset (threshold relative to FP amplitude, beat-averaged) | return of the signal toward baseline | argues that the first positive peak in a propagating monolayer reflects neighbouring cells and that the end should be the baseline return, not the repolarization peak; the author's own, not peer-reviewed opinion |
| [[wiki/papers/dunham-2022-cardiopyemea.md]] (Cardio PyMEA) | R wave (field potential peak) | T-wave endpoint from a fitted trapezoid | maximum first derivative between the T peak and baseline and a point 50–200 ms past the T peak fit a trapezoid with a mobile point; maximising the area gives the endpoint; not validated against APD |
| [[wiki/papers/lee-2024-cardiomea.md]] (CardioMEA) | R spike | T-wave peak | R-to-T-peak FPD correlated only minimally with APD50 and APD90 from intracellular-like signals on the same electrodes (small, noisy T waves) |
| [[wiki/papers/weiser-bitoun-2026-physiomea.md]] (PhysioMEA) | R peak | T-wave peak | inverted T waves are analysed on the inverted signal; electrodes with inconsistent biomarker counts are excluded |
| [[wiki/papers/hayakawa-2014-motion-fp.md]] | initial negative peak | peak of the positive deflection | notes two end points used earlier (peak of the positive deflection; return to baseline), which appear to match the upstroke and the peak of the relaxation motion, and that an accurate end point proved difficult to establish |
| [[wiki/papers/ernault-2024-interpretation.md]] | — (tests T-wave landmarks, not an FPD definition) | T-wave peak (and T-wave upstroke) tested as APD surrogates | in neonatal rat monolayers the T-wave peak coincided with APD90 and the upstroke with APD50 only for biphasic T waves, a minority morphology |

## Observations (ours, not from a single source)
- Four different end conventions are documented (baseline return, trapezoid T-wave endpoint, T-wave peak, positive-deflection peak), so FPD values are not directly comparable across tools without the convention (main.md, Fiducial section).
- Two independent observations (Ernault in rat cells, Hayakawa in iCell monolayers with simultaneous video) point to the T-wave peak and the baseline return measuring different phases of repolarization/relaxation; neither validates one of them for hiPSC-CMs.
- No reviewed paper compared the conventions on the same data.

## See also
- [[wiki/fridericia-rate-correction.md]]
- [[wiki/critical-assessment-maki-claims.md]]
