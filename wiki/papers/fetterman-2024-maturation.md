---
tags: [maturation, high-throughput, in-vitro-maturation-media, electromechanical]
---

# Independent compartmentalization of functional, metabolic, and transcriptional maturation of hiPSC-derived cardiomyocytes

**Authors:** K. Ashley Fetterman, Malorie Blancard, Davi M. Lyra-Leite, Carlos G. Vanoye, Hananeh Fonoudi, Mariam Jouni, Jean-Marc L. DeKeyser, Brian Lenny, Yadav Sapkota, Alfred L. George Jr., Paul W. Burridge
**Year:** 2024
**Venue:** Cell Reports 43, 114160
**File:** [[raw/fetterman-2024.pdf]]
**DOI:** 10.1016/j.celrep.2024.114160

## Contribution
A systematic, high-throughput dissection of which individual cell-culture-medium components drive hiPSC-CM maturation, and along which axis. The central finding is that functional (electrophysiology/excitation–contraction coupling), metabolic, and transcriptional maturation are induced largely **independently** by different medium components — no single intervention (and, by extension, no single assay) moves all three together.

## Methodology
Three hiPSC lines, nine medium formulations (a complete maturation medium MMc and systematic component addition/subtraction from it), assessed with parallel high-throughput assays:
- **Ca²⁺ transient imaging** — kinetics, transient duration at 75% repolarization (CTD75), upstroke/downstroke velocity.
- **Impedance recordings on a CardioExcyte96 (Nanion)** — an MEA-family, electrode-based platform, but used here for impedance (contractility surrogate: pulse width at 50%, beat rate, up/downstroke velocity), **not** extracellular field-potential (FP) voltage recording.
- **Manual and automated patch-clamp** — action potential (maximum diastolic potential, upstroke velocity Vmax, APD90, peak amplitude) and voltage-gated Na⁺ (Nav) current density/kinetics.
- **Seahorse extracellular flux assay** — mitochondrial oxygen consumption rate (basal/maximal respiration, spare respiratory capacity).
- **Bulk RNA-seq** — transcriptomic profiling across formulations.

Individual medium components (galactose vs. glucose, fatty acids, T3, dexamethasone, insulin, ascorbic acid, sodium selenite, transferrin, carnitine/creatine/taurine) were added to a minimal base medium or subtracted from the complete formulation to isolate each component's contribution.

## Findings
- The complete maturation medium (MMc) produced a more hyperpolarized maximum diastolic potential (−68.1 vs. −51.7 mV), faster AP upstroke velocity (30.2 vs. 7.3 mV/ms), and higher Nav current density (130.6 vs. 80.7 pA/pF at 0 mV) than control medium — but **APD90 and peak AP amplitude were unchanged**, showing maturation-associated shifts are metric-specific even within a single modality.
- Ascorbic acid, dexamethasone, insulin, sodium selenite, T3, and transferrin were individually necessary for more mature Ca²⁺-transient/AP-related ("functional") phenotypes.
- Galactose (vs. glucose) and fatty acids, together with carnitine/creatine/taurine, drove mitochondrial respiration ("metabolic" maturation) but had **no effect** on Ca²⁺ transients, impedance, or Nav current — the functional and metabolic axes dissociate.
- Energy substrate (galactose vs. glucose) caused the largest transcriptomic shift (~4,000 differentially expressed genes) without further improving functional assay readouts.
- Overall conclusion: hiPSC-CM "maturation" is not a single scalar quantity — it fractionates into at least electrophysiological/EC-coupling, metabolic, and transcriptional compartments that respond to different, largely non-overlapping biochemical cues.

## Limitations
- Did not screen for novel maturation inducers — used only components already established in the literature as a baseline.
- Did not examine structural correlates of maturation (t-tubules, sarcomere organization, cell-cycle exit, multinucleation) that often accompany functional/metabolic changes.
- Monolayer culture only; no 3D tissue format, which the authors note could mask or alter component effects.
- No extracellular field-potential (FP/MEA) voltage recording was performed — the electrophysiology-adjacent readouts were impedance (CardioExcyte96) and patch-clamp AP/Nav, not FPD. The paper's "electrophysiological maturation" axis is therefore not directly expressed in MEA-FP units.

## Relevance to our paper
This paper does not itself provide MEA-derived reference values for hiPSC-CM maturation, but it is directly relevant to the gap: it shows that maturation status cannot be captured by a single reference value or index, since the electrophysiological/functional axis it measures (AP kinetics, Nav current) is regulated independently of metabolic and transcriptional maturation. This means an MEA-FP-derived maturation benchmark — even if validated — could only characterize the electrophysiological compartment of maturity, not the metabolic or transcriptional state of the preparation. It also supplies concrete, quantitative functional reference points (MDP, AP upstroke velocity, Nav current density) from patch-clamp that a future MEA-FP surrogate would need to correlate against, and reinforces the culture-age/maturation link already noted via ion-channel gene expression in Guerrelli et al. (2024).

## See also
- [[wiki/papers/ismaili-2023-hamburg.md]]
- [[wiki/papers/guerrelli-2024-hipscm.md]]
- [[wiki/papers/maki-2023-opinion.md]]
- [[wiki/papers/correia-2024-acc2.md]]
- [[wiki/papers/scheurer-2025-optical-ai.md]]
- [[wiki/hipsc-cm-maturation.md]]
