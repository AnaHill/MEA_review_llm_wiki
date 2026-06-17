# Advanced cardiotoxicity profiling using field potential imaging with UHD-CMOS-MEA in human iPSC-derived cardiomyocytes

**Authors:** Noriaki Matsuda, N. Nagafuku, K. Matsuda, Y. Ishibashi, T. Taniguchi, Y. Matsushita, N. Miyamoto, T. Yoshinaga, I. Suzuki  
**Year:** 2025  
**Venue:** Toxicological Sciences 208(2):384–400  
**File:** [[raw/matsuda-2025-uhd.pdf]]  
**DOI:** 10.1093/toxsci/kfaf134

## Contribution
Demonstrates that a Sony ultra-high-density CMOS-MEA (UHD-CMOS-MEA) with 236,880 electrodes per 6.5 mm² can generate spatially resolved field potential images (FPI) from hiPSC-CM preparations, enabling novel endpoints (excitation origin count, propagation area, conduction velocity maps) beyond what conventional MEAs provide. Proposes these endpoints as improved cardiac safety assessment tools for CiPA.

## Methodology
- Platform: Sony UHD-CMOS-MEA (6.5 mm² sensing area; 236,880 electrodes at 13.5 µm pitch; 48-well format)
- Cell line: hiPSC-CMs (specific commercial line not specified in summary; standard preparation)
- Recording: Full-plate FP images at single-cell resolution, enabling propagation mapping
- Novel endpoints derived from FPI:
  - **Excitation origin count** — number of independent pacemaker foci per preparation
  - **Propagation area** — fraction of the preparation participating in synchronized activation
  - **Conduction velocity (CV) maps** — spatial heterogeneity and mean CV
- Pharmacological validation: CiPA reference compounds (hERG blockers, INa blockers, L-type Ca channel modulators)
- Comparison with conventional FPD and FPDcF endpoints

## Findings
- FPI resolves individual cell activation sequences not visible on conventional 64–256 electrode MEAs.
- **Excitation origin count** detects re-entrant or multi-focal arrhythmic behavior not captured by FPD.
- **Propagation area** declines predictably with conduction-slowing drugs (e.g., INa blockers), providing a direct pharmacodynamic endpoint.
- **CV maps** reveal heterogeneous conduction slowing that precedes detected arrhythmic events.
- FPDcF values from the UHD-MEA correlate with conventional MEA values but provide spatial FPD heterogeneity maps as an additional dimension.
- These novel endpoints can detect proarrhythmic risk profiles that are invisible to single-well FPD metrics.

## Limitations
- Hardware is research-grade (Sony prototype/early commercial); widespread laboratory availability is limited at time of publication.
- Novel endpoints lack validated regulatory cut-off thresholds; not yet in CiPA guidelines.
- High data volume per experiment requires dedicated processing pipelines.

## Relevance to our paper
Central to the main.md review. Represents the state of the art in MEA spatial resolution (2025). The novel FPI endpoints (excitation origin count, propagation area, CV maps) are discussed in main.md as the frontier of what MEA analysis can achieve, contrasting with the FPD/FPDcF metrics that dominate the literature.

## See also
- [[wiki/papers/botti-2025-insilico.md]]
- [[wiki/papers/maurissen-2024-mutation.md]]
- [[wiki/papers/altrocchi-2023-chronic.md]]
