---
tags: [fiducial-definition, waveform-morphology]
---

# Interpretation of field and LEAP potentials recorded from cardiomyocyte monolayers

**Authors:** Auriane C. Ernault, Rushd F. M. Al-Shama, Jiuru Li, Harsha D. Devalla, Joris R. de Groot, Ruben Coronel, Edward Vigmond, Bastiaan J. Boukens  
**Year:** 2024  
**Venue:** American Journal of Physiology–Heart and Circulatory Physiology 326(3):H800–H811  
**File:** [[raw/ernault-2024-interpretation.pdf]]  
**DOI:** 10.1152/ajpheart.00463.2023

## Contribution
Provides a mechanistic electrophysiological interpretation of field potential (FP) and LEAP (Local Extracellular Action Potential) signals recorded from hiPSC-CM monolayers using combined experimental and in silico approaches, establishing when FP features correspond to action potential duration (APD).

## Methodology
- **FP–APD/conduction-velocity analysis (Figs. 1–4):** neonatal rat ventricular myocyte (NRVM) monolayers on a 60-electrode MEA, with simultaneous sharp-microelectrode action potential recordings, calibrated against an in silico NRVM monodomain model (Wang/Sobie ionic model) and cross-checked against an O'Hara human ventricular model. 15 monolayers, spontaneous cycle length 450–1,000 ms. gNa was swept 0.35–5.15× baseline (49 simulations) to generate a range of conduction velocities; local CV also measured experimentally at baseline (S1, 600 ms) vs. after premature stimulation (S2, 10 ms above refractory period).
- **LEAP analysis (Figs. 5–6):** separate experiments using human iPSC-derived cardiomyocytes (atrial and ventricular subtype), with LEAP generated via high-frequency stimulation at a single electrode; also modeled in silico by clamping a small membrane region to −55 mV.
- Correlation analysis between FP T-wave landmarks (Tup, Tpeak) and APD at multiple repolarization percentages (APD20/50/80/90)

## Findings
- **T-wave peak (Tpeak) correlates with APD90, and T-wave upstroke (Tup) with APD50 — but only when the FP shows a biphasic T-wave** (starting negative, ending positive). Monophasic (positive-only) T-waves — which the paper reports as the **majority** of recorded monolayers, not a minority edge case — cannot be reliably used to infer APD from FPD at all. This is a stronger and more consequential caveat than "morphology assessment is required": in most experimental FPs, no reliable APD surrogate is available via FPD regardless of which fiducial point is chosen.
- **LEAP signals reflect APD90 but not local APD**; they represent a spatial average over the monolayer rather than the action potential duration of cells directly on the electrode. The direction of the FPD-vs-APD offset is cell-type dependent: FPD(Tpeak) is *shorter* than APD in atrial iPSC-CMs but *longer* than APD in ventricular iPSC-CMs, and the fast early repolarization phase visible in atrial LEAPs is absent in ventricular LEAPs.
- **RS amplitude and dV/dtmin correlate with conduction velocity (CV) in silico** (r=0.96, r=0.90, P<0.001) but only in the lower CV range (<30 cm/s) — the correlation is lost at higher, more physiological CVs. In vitro the correlation is much weaker and not statistically significant (r=0.22, r=0.29). Critically, **after premature (ectopic-like) stimulation, local CV was unchanged while amplitude and dV/dtmin dropped significantly** — meaning these FP-shape parameters can fail as CV surrogates specifically under altered excitability, not just generically "in vitro."
- These findings require morphology assessment of individual FP waveforms before FPD-based analysis can be interpreted as an APD surrogate, and even then a majority of real recordings may not qualify.

## Limitations
- Experiments performed on 2D monolayers; findings may not generalize to 3D tissues or spheroids.
- LEAP utility may be limited to preparations where spatial averaging is acceptable.
- **The core FP-shape/APD/CV correlation analysis (Figs. 1–4) uses neonatal rat ventricular myocytes (NRVM), not hiPSC-CMs** — species generalizability to the hiPSC-CM systems this review focuses on is not directly demonstrated; only the separate LEAP experiments (Figs. 5–6) use human iPSC-CMs.
- Biphasic T-waves — required for any Tpeak/Tup-based APD surrogate — occurred in only a minority of recorded monolayers, limiting the practical applicability of the paper's central fiducial-timing findings.

## Relevance to our paper
Cited in main.md as direct empirical support for the morphology-aware analysis argument: the finding that Tpeak↔APD90 correlation depends on T-wave morphology underscores the importance of waveform classification before fiducial-point-based analysis. Also relevant to LEAP as an alternative recording modality.

**main.md updated (2026-07-02):** the "Increasing emphasis on..." section now specifies NRVM (rat) rather than generic "cardiomyocyte monolayers," and notes that the biphasic T-wave morphology required for the Tpeak↔APD90 correlation was observed in only a minority of recorded monolayers.

## See also
- [[wiki/papers/ismaili-2023-hamburg.md]]
- [[wiki/papers/guerrelli-2024-hipscm.md]]
- [[wiki/papers/maki-2023-opinion.md]]
- [[wiki/papers/weiser-bitoun-2026-physiomea.md]]
- [[wiki/papers/dunham-2022-cardiopyemea.md]]
