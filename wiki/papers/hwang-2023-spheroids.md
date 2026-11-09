---
tags: [3d-model, in-silico, waveform-morphology]
---

# The three-dimensionality of the hiPSC-CM spheroid contributes to the variability of the field potential

**Authors:** Minki Hwang, Su-Jin Lee, Chul-Hyun Lim, Eun Bo Shim, Hyang-Ae Lee  
**Year:** 2023  
**Venue:** Frontiers in Physiology 14:1123190 (published 21 Mar 2023; open access, CC BY)  
**File:** [[raw/hwang-2023-spheroids.pdf]]  
**Supplementary:** [[raw/hwang-2023-spheroids-supplementary.pdf]] (Figures S1 and S2)  
**DOI:** 10.3389/fphys.2023.1123190

> **Note:** Page rewritten 2026-10-24 after checking the full text; the earlier version described the study as experimental, listed geometry factors (contact angle, size) and a 2D-versus-3D drug comparison that the paper does not report. Supplementary Figures S1 and S2 added and viewed 2026-11-09; Limitations and Methods corrected the same day after the claim check.

## Contribution
Builds in silico three-dimensional models of hiPSC-CM spheroids on an MEA (spherical and discoidal shapes) to simulate field potential measurement, and compares the simulations with in vitro MEA data from spheroids exposed to E-4031 and nifedipine. The authors conclude that the three-dimensionality of the spheroid contributes to the variability of field potentials.

## Methodology
- **In vitro part:** commercial hiPSC-CMs (Cardiosight-S, NEXEL; four differentiation batches) formed into spheroids (spherical in microwells, discoidal on the plate), recorded on a 12-well Axion Maestro MEA at 37 °C; E-4031 and nifedipine concentration series; FPD corrected with Fridericia's formula.
- **In silico part:** the cell model is the O'Hara–Rudy dynamic (ORd) human ventricular cell model (mid-myocardial variant), not an hiPSC-CM model (the paper calls the whole model an "in silico 3-D model of hiPSC-CM spheroids": geometry, size and conduction velocity follow the in vitro spheroids), with a single cell type in the whole spheroid; tetrahedral meshes of spherical and discoidal models, action potential propagation by the monodomain reaction–diffusion equation, an electrical model of the electrode, and field potentials computed from extracellular potentials; drug effects simulated by matching simulated FPD to the in vitro data and deriving IC50 values.

## Findings
- Simulated field potentials from the 3D models had highly variable shapes depending on the stimulation site and the measurement (electrode) location, even when only a single cell type was present in the model; the authors infer that the three-dimensionality of the spheroid on the MEA contributes to variability, in addition to differences in cell types and differentiation level.
- The IC50 values of E-4031 and nifedipine obtained by matching simulated FPD to the in vitro data were in line with values reported in the literature.
- The simulated variability resembled the variability seen in vitro.
- At higher drug concentrations the FP repolarization peak no longer reflected AP repolarization: with E-4031 the simulated AP failed to repolarize, and with nifedipine the FP repolarization peaks were hardly recognizable (p. 8; Supplementary Figures S1 and S2). The authors conclude that FP signals "should be interpreted with great caution, especially at higher concentrations of drugs".

### Supplementary material
Viewed 2026-11-09 (rendered pages). Two figures, each with three panels for a concentration series: experimental FP traces (vertical ticks mark the detected repolarization peak), simulated FP traces and simulated APs (traces offset vertically).
- **Figure S1 (E-4031, 0–0.1 µM):** the experimental repolarization peak moves later with concentration; in the simulated FP the repolarization deflection broadens and flattens; the simulated AP prolongs and, at 0.03 and 0.1 µM, does not repolarize (it stays near −10 mV), matching the main text (Fig. 6 caption).
- **Figure S2 (nifedipine, 0–1 µM):** in the experiment the beat period shortens markedly (about 1.55 s to 0.55 s) and the repolarization peak moves earlier; the simulated FP repolarization deflection fades at 0.3 and 1 µM; the simulated AP shortens moderately with a lower plateau.
- The voltage axes are labelled "mV" with a ×10⁻⁴ multiplier, which looks like a unit labelling slip (probably volts); the figures carry no numbers beyond the traces.

## Limitations
Stated by the authors (Discussion, p. 8): because of the large FP variability a correlation between FPD and APD was not easy to establish; FP shape depended on the stimulation and measurement locations; at higher drug concentrations the FP repolarization peaks did not correspond to AP repolarization; the cell model is not an hiPSC-CM model and only one cell type was used; the spherical and discoidal shapes are simplified; the percentage of channel block cannot be known a priori and was fitted to the FPD data. They also write that "More study seems to be needed to clarify the role of three-dimensionality" (p. 8).

Our observations: the in vitro data come from one commercial cell source and two drugs; the paper has no 2D simulation of its own as a control (the 2D comparison is to Abbate et al., 2018), so the role of the 3D geometry is the authors' inference ("This implies …"); it does not compare spheroids with 2D monolayers.

## Relevance to our paper
Since 2026-10-31 also cited in the Conclusion's third gap. Since 2026-11-09 both sentences follow the authors' wording ("implies … contributes", FP shape varying within a 3D geometry) and the 3D section names the human ventricular cell model of the simulated cells.

Cited in main.md for the statement that three-dimensionality contributes to field potential variability; the corrected wording says that this comes from in silico models compared with in vitro recordings, with variability depending on stimulation and electrode locations. It also adds a study that uses Fridericia correction (FPDc) to the list in the rate-correction section.

## See also
- [[wiki/papers/maurissen-2024-mutation.md]]
- [[wiki/papers/ernault-2024-interpretation.md]]
- [[wiki/papers/botti-2026-insilico.md]]
- [[wiki/papers/maki-2023-opinion.md]]
