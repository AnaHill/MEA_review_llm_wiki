# The three-dimensionality of the hiPSC-CM spheroid contributes to the variability of the field potential

**Authors:** Minki Hwang, Su-Jin Lee, Chul-Hyun Lim, Eun Bo Shim, Hyang-Ae Lee  
**Year:** 2023  
**Venue:** Frontiers in Physiology 14:1123190  
**File:** [[raw/hwang-2023-spheroids.pdf]]  
**DOI:** 10.3389/fphys.2023.1123190

> **Citation note:** main.md cites this as "Tsai, Y.-H., Cho, S.K. and Boheler, K.R. 2023" with a slightly different title. The actual authors (Hwang et al., Korea) are completely different. This appears to be a hallucinated citation in the review draft; the paper title points to the correct paper but the author attribution is fabricated.

## Contribution
Uses in silico modeling to demonstrate that the geometric and physical properties of 3D spheroid structures — not just cell-to-cell heterogeneity — are a primary source of field potential variability when hiPSC-CM spheroids are placed on MEA electrodes.

## Methodology
- Platform: Axion Maestro MEA
- Cell line: Cardiosight-S hiPSC-CMs (NEXEL, Korea)
- 3D spheroid formation; spheroids placed on MEA electrodes
- In silico finite element models of spheroid geometry (varying size, position, contact angle relative to electrode)
- hERG pharmacology: E-4031 concentration-response in 2D vs. 3D preparations
- IC50 determination for FPD prolongation

## Findings
- **FP variability in spheroids is largely attributable to spheroid geometry** (electrode coverage, spheroid diameter, contact angle) rather than to intrinsic biological heterogeneity.
- In silico simulations reproduce the variability patterns seen experimentally when varying spheroid-electrode geometry.
- IC50 for E-4031 FPD prolongation: 8 nM (spheroid preparation).
- 3D spheroids show different FP morphologies than 2D monolayers for equivalent drug concentrations, complicating direct comparisons.

## Limitations
- Geometric variability is experimentally hard to control without custom microwell arrays or standardized seeding; practical recommendations for reducing it are limited.
- 2D vs. 3D pharmacological comparisons require careful normalization of geometry effects.

## Relevance to our paper
Cited in main.md as evidence that 3D cultures introduce geometric confounders beyond the biological variability already present in 2D monolayers. Supports the argument that preparation geometry must be considered when interpreting FP variability across studies.

## See also
- [[wiki/papers/maurissen-2024-mutation.md]]
- [[wiki/papers/ernault-2024-interpretation.md]]
- [[wiki/citation-issues.md]]
