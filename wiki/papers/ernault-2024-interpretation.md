# Interpretation of field and LEAP potentials recorded from cardiomyocyte monolayers

**Authors:** Auriane C. Ernault, Rushd F. M. Al-Shama, Jiuru Li, Harsha D. Devalla, Joris R. de Groot, Ruben Coronel, Edward Vigmond, Bastiaan J. Boukens  
**Year:** 2024  
**Venue:** American Journal of Physiology–Heart and Circulatory Physiology 326(3):H800–H811  
**File:** [[raw/ernault-2024-interpretation.pdf]]  
**DOI:** 10.1152/ajpheart.00463.2023

## Contribution
Provides a mechanistic electrophysiological interpretation of field potential (FP) and LEAP (Local Extracellular Action Potential) signals recorded from hiPSC-CM monolayers using combined experimental and in silico approaches, establishing when FP features correspond to action potential duration (APD).

## Methodology
- Simultaneous MEA field potential recordings and sharp-microelectrode action potential recordings from cardiomyocyte monolayers
- LEAP recordings (local extracellular AP, a spatially averaged signal)
- In silico monodomain simulations to interpret signal correlations
- Human iPSC-derived cardiomyocyte monolayers (specific line not prominently stated)
- Correlation analysis between FP T-wave peak time and APD90

## Findings
- **T-wave peak correlates with APD90 only when the T-wave is biphasic.** Monophasic T-waves cannot be reliably used to infer APD90 from FPD.
- **LEAP signals reflect APD90 but not local APD**; they represent a spatial average over the monolayer rather than the action potential duration of cells directly on the electrode.
- **RS amplitude correlates with conduction velocity (CV) in silico** but this correlation does not hold robustly in vitro, limiting RS amplitude as a CV surrogate in practice.
- These findings require morphology assessment of individual FP waveforms before FPD-based analysis can be interpreted as an APD surrogate.

## Limitations
- Experiments performed on 2D monolayers; findings may not generalize to 3D tissues or spheroids.
- LEAP utility may be limited to preparations where spatial averaging is acceptable.

## Relevance to our paper
Cited in main.md as direct empirical support for the morphology-aware analysis argument: the finding that Tpeak↔APD90 correlation depends on T-wave morphology underscores the importance of waveform classification before fiducial-point-based analysis. Also relevant to LEAP as an alternative recording modality.

## See also
- [[wiki/papers/ismaili-2023-hamburg.md]]
- [[wiki/papers/guerrelli-2024-hipscm.md]]
- [[wiki/papers/maki-2023-opinion.md]]
