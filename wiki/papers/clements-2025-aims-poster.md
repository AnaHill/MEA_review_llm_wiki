---
tags: [high-throughput, rate-correction, maturation, 2d-culture]
---

# Standards for hiPSC-derived cardiomyocyte electrophysiology using the MEA assay (AIMS #CM01 poster)

**Authors:** Mike Clements, Cristina Altrocchi, Devon Guerrelli, Adam P. Hill, Nikki Posnack, Chris Strock, Takashi Yoshinaga  
**Year:** 2025  
**Venue:** Poster W1284, presented at ISSCR 2025, Hong Kong, 11 June 2025 (not peer reviewed; vendor-hosted)  
**File:** [[raw/clements-2025-aims-poster.pdf]] (vendor material; git-ignored, not redistributed)  
**URL:** https://axionbiosystems.com/resources/poster/standards-hipsc-derived-cardiomyocyte-electrophysiology-using-mea-assay  
**Affiliations:** Axion BioSystems; Johnson & Johnson (Belgium); Children's National Hospital; Victor Chang Cardiac Research Institute; Cyprotex; Eisai.

> **Note:** Grey literature. The poster PDF was read in full on 2026-10-18 (one page; text extracted, layout not inspected visually). The underlying standard document "AIMS #CM01: Spontaneous beating wild type hiPSC-ventricular cardiomyocyte field potential assay", published by Axion BioSystems (last revised 2 December 2024), was retrieved from https://axionbiosystems.com/aims-cm01 through a web-fetch summary only and no local copy was saved; it agrees with the poster on the criteria below.

## Contribution
Proposes minimum acceptance criteria, the Axion iPSC Model Standards (AIMS) #CM01, for a spontaneous-beating wild-type hiPSC-ventricular cardiomyocyte field potential assay used for compound testing or disease modelling, drawing on academic and industry experience, published data and the CiPA and JiCSA consortia.

## Methodology
- A cell source meets the proposed standard when at least 80 % of MEA wells meet all four well criteria.
- **Well criteria:** (1) spike amplitude ≥ 0.5 mV on ≥ 50 % of electrodes; (2) synchronized beating across ≥ 50 % of electrodes; (3) spontaneous beat period 750–3000 ms (20–80 beats per minute); (4) corrected field potential duration (FPDc) of 200–700 ms, with Fridericia correction FPDc = FPD/(beat period)^1/3. Optional: beat period irregularity < 0.2 %.
- The specification range was inferred from the CiPA pilot study (Millard et al., 2018) and shown against three vendor cell sources that met it.
- Stated considerations: ventricular cells only (not atrial); competing pacemakers confound analysis and beating should start from a single origin; a spike amplitude ≥ 1.0 mV would widen the assay window for drug effects on spike amplitude; spontaneous beating is often attributed to immaturity, and a paced assay is left to a possible future AIMS.

## Findings
The poster presents the proposal and the three-vendor comparison; no new experimental results are reported beyond that figure. It states that although the basal activity of the vendor cell sources differed significantly, consistent concentration-dependent effects were observed in the cited pilot study.

## Limitations
Our observations: it is a proposal from a MEA vendor with academic and industry co-authors, not a consensus standard; no validation statistics or peer review; the poster does not address maturation staging; FPDc acceptance is tied to the Fridericia formula even though that formula is described as not thoroughly validated for hiPSC-CMs ([[wiki/papers/blinova-2018-multisite.md]]).

## Relevance to our paper
(1) A citable source for the industry-led acceptance criteria mentioned in main.md, which target assay quality control and not maturation staging. (2) A source for the accepted spontaneous rate range of hiPSC-CM MEA assays (20–80 bpm here, 20–90 bpm in Blinova et al. 2018), used in the FPDc section. (3) Shows the Fridericia correction being built into a proposed acceptance standard (FPDc window of 200–700 ms), which reinforces the rate-correction gap. Two of the poster's authors share names with first authors of reviewed studies (Altrocchi et al., 2023; Guerrelli et al., 2024); same-person identity was not verified.

## See also
- [[wiki/papers/blinova-2018-multisite.md]]
- [[wiki/papers/altrocchi-2023-chronic.md]]
- [[wiki/papers/guerrelli-2024-hipscm.md]]
- [[wiki/hipsc-cm-maturation.md]]
