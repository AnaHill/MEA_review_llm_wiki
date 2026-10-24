---
tags: [review, microphysiological-system, multimodal, in-silico]
---

# Building blocks of microphysiological system to model physiology and pathophysiology of human heart

**Authors:** Hanna Vuorenpää, Miina Björninen, Hannu Välimäki, Antti Ahola, Mart Kroon, Laura Honkamäki, Jussi T. Koivumäki, Mari Pekkanen-Mattila  
**Year:** 2023  
**Venue:** Frontiers in Physiology 14:1213959 (review; published 6 July 2023)  
**File:** [[raw/vuorenpaa-2023-mps-building-blocks.pdf]]  
**DOI:** 10.3389/fphys.2023.1213959

Note: ingested 2026-10-24 from the full text (28 pages, text extraction; figures and tables not viewed). Open access (CC BY). Funding stated: Academy of Finland Centre of Excellence in Body-on-Chip Research, among others. Pekkanen-Mattila is also an author of [[wiki/papers/ryynanen-2018-single-cell-mea.md]]; the Declarations of main.md mention that several authors of both belong to the research group in which the researcher previously worked.

## Contribution
A review of the building blocks of cardiac microphysiological systems (MPS): relevant cardiac cell types, supporting matrix, mechanical stimulation, functional measurements and computational modelling, with the stated aim of giving insight for MPS that recapitulate human physiology better. It is not a review of MEA analysis methods.

## Methodology
Narrative review (sections: cardiomyocytes and their maturation; other cell types, vascularisation and innervation; matrix and mechanical/electrical stimulation; 6 functional measurements, with 6.1 electrodes, indicators and contractility and 6.2 (bio-)chemical measurements; 7 computational modelling and simulation; 8 outlook). Table 5 summarises recent studies with perfusion and contraction-cycle measurements in hiPSC-CMs. No search method was looked for in the text read.

## Findings
Statements relevant to this project (all from the full text):
- **Multiple modalities (section 6.1):** "An advantage of heart MPS is the capability to include multiple sensors and electrodes for continuous measurement and monitoring of multiple measurement modalities, even concurrently"; the authors conclude that "the reviewed studies show the potential of combining different measurement modalities, which may be fruitful for perfusion-enabled heart-on-chip studies as the field matures", and that the most novel methods have yet to be evaluated in hiPSC-CM disease models and drug studies.
- **MEA (section 6.1.1):** microelectrode arrays are an accessible option, measure the field potential without perforating the cell membrane, give less accurate electrical information than intracellular recording, have lower instrumentation requirements and can track electrical propagation. The text states that several software tools exist for the signal processing (Pradhapan et al., 2013; Dunham et al., 2022), that MEA is "a well-established means of measurement", and that "the parametrization of APs and field potentials has been well established, enabling clear comparison of results between studies" (citing Kussauer et al., 2019). In disease studies of heart-on-chip models that need electromechanical coupling, electrical measurements and/or calcium imaging were included, with MEAs typically used.
- **Contractility (section 6.1.3):** impedance-based measurement is "another option for indirect force measurement"; video-based measures are an accessible way of quantifying contraction.
- **Computational modelling (section 7):** "the capability for continuous/long-term and multimodal measurements and concurrent sensing of the central functional readouts ... generate unprecedently holistic dataset for parameterization and validation of computational models"; models "generate hypothesis, integrate and interpret data". hiPSC-CM models were extended to contractile mechanics (first hiPSC-CM-specific electromechanical models: Forouzandehmehr et al., 2021, 2022). "To our knowledge, multiphysics models that would put together all the building blocks of MPS in integrative simulations have not yet been published."
- **Outlook (section 8):** some building blocks are "still in their infancy"; the need for "validated and standardized test systems with high throughput capacity"; computer modelling and simulation may help compare results from different test systems.
- Not found in the text: artificial intelligence, machine learning, deep learning or digital twins.

## Limitations
Stated by the authors: the efficacy of the most novel measurement methods has yet to be evaluated in hiPSC-CM disease models and drug studies; some building blocks are still in infancy (for example innervation in 3D); integrative multiphysics models had not been published to their knowledge.

Our observations (not from the paper): it is a 2023 review, so it does not cover the 2024–2026 work in main.md; it contains no discussion of AI-assisted analysis or digital twins; its statement that FP parametrization is well established is a contrast to the claim in main.md that analysis methods are a major source of inter-study variability (see synthesis item 1 in docs/claims-by-source.md).

## Relevance to our paper
Cited in main.md (Discussion and future outlook) in two places: as a review that sees potential in combining measurement modalities (sensor-fusion paragraph) and as stating that continuous, multimodal measurements give a holistic data set for parameterising and validating computational models, with integrative models not yet published (digital-twin sentence). It is also a counterpoint to synthesis item 1.

## See also
- [[wiki/papers/ryynanen-2018-single-cell-mea.md]]
- [[wiki/papers/hayakawa-2014-motion-fp.md]]
- [[wiki/papers/kabanov-2026-cardioscripts.md]]
- [[wiki/papers/botti-2026-insilico.md]]
- [[wiki/papers/dunham-2022-cardiopyemea.md]]
- [[wiki/papers/maki-2023-opinion.md]]
