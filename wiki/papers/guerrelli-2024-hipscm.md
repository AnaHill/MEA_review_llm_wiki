---
tags: [temporal-confounder, maturation, equilibration, reproducibility, well-position]
---

# hiPSC-CM electrophysiology: impact of temporal changes and study parameters on experimental reproducibility

**Authors:** Devon Guerrelli, Jenna Pressman, Shatha Salameh, Nikki Posnack  
**Year:** 2024  
**Venue:** American Journal of Physiology–Heart and Circulatory Physiology 327(1):H12–H27  
**File:** [[raw/guerrelli-2024-hipscm.pdf]]  
**DOI:** 10.1152/ajpheart.00631.2023

## Contribution
Systematic quantification of how temporal factors (equilibration time, days post-thaw, days in culture) and spatial factors (well-plate position) affect hiPSC-CM electrophysiological measurements, providing evidence-based recommendations for standardizing MEA recording protocols.

Note: page checked against the source text on 2026-10-24; statements not supported by the paper were removed or reworded.

## Methodology
- Platform: Axion Maestro Edge MEA; 24-well plates with 16 electrodes per well (the paper never discusses rate correction)
- Cell line: iCell Cardiomyocytes² (Fujifilm Cellular Dynamics, Cat. No. 01434); Cor.4U (Ncardia) used for key experiments
- Daily MEA recordings 2–14 days post-defrost (paced 3–14 days; LEAP/drug 4–10 days); equilibration recorded continuously for 20 min at day 4
- Spatial analysis comparing outer vs. inner well rows on the same plate
- Drug treatments at day 4 vs. day 10 post-plating
- qRT-PCR for cardiac genes (including KCNJ2, SCN5A, CACNA1C, CASQ2, TNNI3) on days 2, 7, 14 and 30

## Findings
- **Equilibration effect:** Beating rate increases 22.6% and FPD decreases 7.7% over a 20-minute recording window; the beating rate was still significantly lower than its 20-min value up to 12 min (FPD up to 7 min); the authors recommend 15–20 min of equilibration.
- **Spatial heterogeneity:** Outer well rows beat 8.8 bpm faster than inner rows at 20 min (53.7 vs 44.9 bpm); the authors suggest temperature distribution differences as a possible cause but could not confirm it.
- **Longitudinal drift:** FPD increases by ~257 ms over days 2–14 in culture; beating rate decreases over the same period.
- **Drug responsiveness differs by age:** E-4031 prolonged FPD more at day 4 than at day 10 (+31.2% vs +17.2%); isoproterenol and nifedipine responses also changed with culture time. The authors say culture time should be considered in drug screening.
- **Gene expression:** KCNJ2 increases 27.5-fold over 30 days in iCell² (vs 5.0-fold in Cor.4U), suggesting continued maturation in culture.

## Practical recommendations
- Allow **15–20 min equilibration** before recording baselines.
- Use cells **within 6–8 days post-thaw** for consistency.
- Disperse treatment groups across the plate rather than grouping a treatment in a single row (p. 4).
- Report raw data values and key experimental conditions (cell line, culture time, equilibration time, stimulation settings).

## Limitations
Stated by the authors (p. 13): a mixed ventricular/atrial/nodal population with phenotype differences between lines, a single MEA device, and only the first weeks post-defrost.

Two lines were tested (iCell², main; Cor.4U for key experiments). Cor.4U showed similar but not identical trends (stable beating rate, minimal paced FPD change, no equilibration effect, a smaller KCNJ2 rise), and the authors caution that results may not transfer to other lines or MEA systems.

## Relevance to our paper
Cited in main.md in the FPDc rate-correction, maturation-confound and longitudinal-assay passages (line 142 gives the 22.6%/7.7% figures explicitly). The paper does not discuss FPDc; that recording-time standardisation matters for rate-corrected endpoints is our inference.

## See also
- [[wiki/papers/ismaili-2023-hamburg.md]]
- [[wiki/papers/altrocchi-2023-chronic.md]]
- [[wiki/papers/park-2025-cardiotoxicity.md]]
- [[wiki/papers/maki-2023-opinion.md]]
- [[wiki/papers/fetterman-2024-maturation.md]]
- [[wiki/hipsc-cm-maturation.md]]
- [[wiki/papers/blinova-2018-multisite.md]]
