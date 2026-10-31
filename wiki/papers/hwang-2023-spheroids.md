---
tags: [3d-model, in-silico, waveform-morphology]
---

# The three-dimensionality of the hiPSC-CM spheroid contributes to the variability of the field potential

**Authors:** Minki Hwang, Su-Jin Lee, Chul-Hyun Lim, Eun Bo Shim, Hyang-Ae Lee  
**Year:** 2023  
**Venue:** Frontiers in Physiology 14:1123190 (published 21 Mar 2023; open access, CC BY)  
**File:** [[raw/hwang-2023-spheroids.pdf]]  
**DOI:** 10.3389/fphys.2023.1123190

> **Note:** Page rewritten 2026-10-24 after checking the full text; the earlier version described the study as experimental, listed geometry factors (contact angle, size) and a 2D-versus-3D drug comparison that the paper does not report.

## Contribution
Builds in silico three-dimensional models of hiPSC-CM spheroids on an MEA (spherical and discoidal shapes) to simulate field potential measurement, and compares the simulations with in vitro MEA data from spheroids exposed to E-4031 and nifedipine. The authors conclude that the three-dimensionality of the spheroid contributes to the variability of field potentials.

## Methodology
- **In vitro part:** commercial hiPSC-CMs (Cardiosight-S, NEXEL) formed into spheroids (spherical in microwells, discoidal on the plate), recorded on a 12-well Axion Maestro MEA at 37 °C; E-4031 and nifedipine concentration series; FPD corrected with Fridericia's formula.
- **In silico part:** tetrahedral meshes of spherical and discoidal models, action potential propagation by the monodomain reaction–diffusion equation, an electrical model of the electrode, and field potentials computed from extracellular potentials; drug effects simulated by matching simulated FPD to the in vitro data and deriving IC50 values.

## Findings
- Simulated field potentials from the 3D models had highly variable shapes depending on the stimulation site and the measurement (electrode) location, even when only a single cell type was present in the model; the authors infer that the three-dimensionality of the spheroid on the MEA contributes to variability, in addition to differences in cell types and differentiation level.
- The IC50 values of E-4031 and nifedipine obtained by matching simulated FPD to the in vitro data were in line with values reported in the literature.
- The simulated variability resembled the variability seen in vitro.

## Limitations
No separate limitations section was found. Our observations: the evidence is a simulation matched to a limited in vitro data set; only one cell source, two drugs and two idealised shapes were modelled; the paper does not compare spheroids with 2D monolayers.

## Relevance to our paper
Since 2026-10-31 also cited in the Conclusion's third gap; the 3D section now states the simulation's limits (one cell source, two drugs).

Cited in main.md for the statement that three-dimensionality contributes to field potential variability; the corrected wording says that this comes from in silico models compared with in vitro recordings, with variability depending on stimulation and electrode locations. It also adds a study that uses Fridericia correction (FPDc) to the list in the rate-correction section.

## See also
- [[wiki/papers/maurissen-2024-mutation.md]]
- [[wiki/papers/ernault-2024-interpretation.md]]
- [[wiki/papers/botti-2026-insilico.md]]
- [[wiki/papers/maki-2023-opinion.md]]
