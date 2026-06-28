---
tags: [temporal-confounder, maturation, rate-correction, 2d-culture]
---

# hiPSC-CM electrophysiology: impact of temporal changes and study parameters on experimental reproducibility

**Authors:** Devon Guerrelli, Jenna Pressman, Shatha Salameh, Nikki Posnack  
**Year:** 2024  
**Venue:** American Journal of Physiology–Heart and Circulatory Physiology 327(1):H12–H27  
**File:** [[raw/guerrelli-2024-hipscm.pdf]]  
**DOI:** 10.1152/ajpheart.00631.2023

## Contribution
Systematic quantification of how temporal factors (equilibration time, days post-thaw, days in culture) and spatial factors (well-plate position) affect hiPSC-CM electrophysiological measurements, providing evidence-based recommendations for standardizing MEA recording protocols.

## Methodology
- Platform: Axion Maestro MEA; 48-well plates
- Cell line: iCell Cardiomyocytes² (Fujifilm CDI, lot-controlled); validated with Cor.4U (Ncardia)
- Longitudinal recordings across equilibration windows (0–20 min), days post-thaw (1–14), and days in culture (up to 30 days)
- Spatial analysis comparing outer vs. inner well rows on the same plate
- Drug treatments at day 4 vs. day 10 post-plating
- qPCR for ion channel gene expression (KCNJ2, HCN4, SCN5A) at multiple time points

## Findings
- **Equilibration effect:** Beating rate increases 22.6% and FPD decreases 7.7% over a 20-minute recording window; rate does not plateau within 10 minutes for most wells.
- **Spatial heterogeneity:** Outer well rows beat 8.8 bpm faster than inner rows, attributable to temperature gradients on the MEA plate.
- **Longitudinal drift:** FPD increases by ~257 ms over days 2–14 in culture; beating rate decreases over the same period.
- **Drug responsiveness differs by age:** E-4031 prolongation response is significantly different at day 4 vs. day 10, limiting cross-study comparability when recording day is not standardized.
- **Gene expression maturation:** KCNJ2 (IK1-encoding) increases 27.5-fold over 30 days, indicating progressive maturation that alters baseline electrophysiology.

## Practical recommendations
- Allow **15–20 min equilibration** before recording baselines.
- Use cells **within 6–8 days post-thaw** for consistency.
- **Distribute treatment groups across all row positions** to avoid spatial confounding.
- Report raw FPD values and recording day in addition to rate-corrected values.

## Limitations
- Single cell line (iCell²) tested; different hiPSC-CM lines may show different temporal dynamics.
- The Cor.4U validation was confirmatory rather than a full cross-line comparison.

## Relevance to our paper
Cited repeatedly in main.md. Provides key quantitative evidence for the temporal confounders section (equilibration and longitudinal drift) and supports the argument that recording time standardization is a prerequisite for reliable FPDc pharmacological endpoints. The 22.6%/7.7% figures are cited explicitly.

## See also
- [[wiki/papers/ismaili-2023-hamburg.md]]
- [[wiki/papers/altrocchi-2023-chronic.md]]
- [[wiki/papers/park-2025-cardiotoxicity.md]]
- [[wiki/papers/maki-2023-opinion.md]]
