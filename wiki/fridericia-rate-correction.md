---
tags: [method, rate-correction, fridericia]
---

# Fridericia and other rate corrections of FPD in the reviewed papers

Method page, written 2026-10-24 from the wiki paper pages (each checked against its source text). It lists what each page records about rate correction; where a page says nothing, the paper is not listed.

| Source | What it does |
|---|---|
| [[wiki/papers/blinova-2018-multisite.md]] | Fridericia's formula was used to correct FPD (MEA) and APD (optical); the paper states that the formula is "not thoroughly validated for hiPSC-CMs"; no alternative correction compared; ddFPDc is an absolute change in ms |
| [[wiki/papers/altrocchi-2023-chronic.md]] | FPDc with the Fridericia formula (p. 5) |
| [[wiki/papers/hwang-2023-spheroids.md]] | FPD corrected with Fridericia's formula (p. 5) |
| [[wiki/papers/maurissen-2024-mutation.md]] | FPDcF = FPD divided by the cube root of the inter-spike interval (s); main.md writes this as FPD/RR^0.33, which is the review's notation |
| [[wiki/papers/park-2026-genotype-ml.md]] | Fridericia FPDc, used as an ML feature as a percent change; quiescence coded as a 100 % FPDc change; the page notes that disease lines differ in beat rate and action potential duration, so FPDc differences may partly reflect rate correction |
| [[wiki/papers/park-2025-cardiotoxicity.md]] | corrected FPD (FPDc) computed by the vendor software; the formula is not named |
| [[wiki/papers/clements-2025-aims-poster.md]] | proposed acceptance criteria include an FPDc window of 200–700 ms and a spontaneous beat period of 750–3000 ms (20–80 bpm) |
| [[wiki/papers/pramudito-2026-ensemble.md]] | ML on ΔFPDc values already corrected in the public multisite CiPA dataset; the correction is taken as given |
| [[wiki/papers/lee-2024-cardiomea.md]] | the published CardioMEA feature set contains FPD but no rate-corrected FPD |
| [[wiki/papers/matsuda-2025-uhd.md]] | no FPD or FPDc in its own recordings (FPDc appears only in a table of thresholds from earlier studies) |
| [[wiki/papers/guerrelli-2024-hipscm.md]] | not a correction study, but beating rate rose 22.6 % and FPD fell 7.7 % during a 20-minute recording equilibration, so recordings taken before rate stabilises bias FPDc whichever formula is used; 15–20 minutes of equilibration recommended |

## Observations (ours, not from a single source)
- Among the papers that name a formula, Fridericia is the only one used; none of the reviewed papers tested an alternative correction or a hiPSC-CM-specific formula (this is the basis of Gap 1 in main.md, which is an opinion built on Blinova's statement, the accepted rate ranges and the equilibration drift).
- The units of "ΔFPDc" differ between the two ML papers' sources (absolute ms in Blinova's dataset, percent in Park 2026), so the term is not interchangeable.

## See also
- [[wiki/fpd-end-conventions.md]]
- [[wiki/cipa.md]]
