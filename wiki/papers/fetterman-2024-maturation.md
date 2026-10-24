---
tags: [maturation, high-throughput, in-vitro-maturation-media]
---

# Independent compartmentalization of functional, metabolic, and transcriptional maturation of hiPSC-derived cardiomyocytes

**Authors:** K. Ashley Fetterman, Malorie Blancard, Davi M. Lyra-Leite, Carlos G. Vanoye, Hananeh Fonoudi, Mariam Jouni, Jean-Marc L. DeKeyser, Brian Lenny, Yadav Sapkota, Alfred L. George Jr., Paul W. Burridge
**Year:** 2024
**Venue:** Cell Reports 43, 114160
**File:** [[raw/fetterman-2024-maturation.pdf]]
**DOI:** 10.1016/j.celrep.2024.114160

## Contribution
A systematic, high-throughput dissection of which individual cell-culture-medium components drive hiPSC-CM maturation, and along which axis. The authors report that functional (electrophysiology/excitation–contraction coupling), metabolic, and transcriptional maturation are induced largely **independently** by different medium components (Summary, p. 2); the combined formulation MMc improved all three.

Note: page checked against the source text on 2026-10-24; statements not supported by the paper were removed or reworded.

## Methodology
Eight hiPSC lines were used across the study (three lines for the RNA-seq of nine medium formulations); media ranged from a minimal base (MMb) to the complete maturation medium (MMc), with systematic component addition/subtraction, assessed with parallel high-throughput assays:
- **Ca²⁺ transient imaging** — kinetics, transient duration at 75% (CTD75), upstroke/downstroke velocity.
- **Impedance recordings on a CardioExcyte96 (Nanion)** — an MEA-family, electrode-based platform, but used here for impedance (contractility surrogate: pulse width at 50%, beat rate, up/downstroke velocity), **not** extracellular field-potential (FP) voltage recording.
- **Manual and automated patch-clamp** — action potential (maximum diastolic potential, upstroke velocity Vmax, APD90, peak amplitude) and voltage-gated Na⁺ (Nav) current density/kinetics.
- **Seahorse extracellular flux assay** — mitochondrial oxygen consumption rate (basal/maximal respiration, spare respiratory capacity).
- **Bulk RNA-seq** — transcriptomic profiling across formulations.

Individual medium components (galactose vs. glucose, fatty acids, T3, dexamethasone, insulin, ascorbic acid, sodium selenite, transferrin, carnitine/creatine/taurine) were added to a minimal base medium or subtracted from the complete formulation to isolate each component's contribution.

## Findings
- The complete maturation medium (MMc) produced a more hyperpolarized maximum diastolic potential (−68.1 vs. −51.7 mV), faster AP upstroke velocity (30.2 vs. 7.3 mV/ms), and higher Nav current density (130.6 vs. 80.7 pA/pF at 0 mV) than control medium — but **APD90 and peak AP amplitude were unchanged**, showing maturation-associated shifts are metric-specific even within a single modality.
- Single-addition and single-subtraction Ca²⁺-imaging screens showed that ascorbic acid, dexamethasone, insulin, sodium selenite, T3 and transferrin each contributed to viability and/or Ca²⁺-transient kinetics (p. 5, p. 12). In the additive test only transferrin, insulin, dexamethasone and T3 shortened CTD75; in the subtractive test only ascorbic acid and T3 were needed (their removal lengthened CTD75). Action potential and Nav comparisons were made only for RBAI vs MMc and for glucose vs galactose and ± fatty acids, not component by component.
- Replacing glucose with galactose raised basal respiration only (maximal respiration and spare capacity unchanged), and removing fatty acids lowered respiration in MMc (not in MMs), without changing viability, Ca²⁺ transients or impedance in the glucose/galactose comparison. Nav current density was unchanged by glucose vs galactose, but removing fatty acids from MMs gave a lower peak density and a different V1/2 of inactivation (p. 6); MMc without carnitine/creatine/taurine had lower Ca²⁺ up- and downstroke velocities.
- Energy substrate (galactose vs. glucose) caused the largest transcriptomic shift (~4,000 differentially expressed genes) without further improving functional assay readouts; the metabolic and transcriptional axes are therefore not shown to be separable.
- The authors report that electrophysiological/EC-coupling, metabolic and gene-expression maturation are induced largely independently (p. 2) and recommend MMc as a balanced formulation (p. 12).

## Limitations
- Did not screen for novel maturation inducers — used only components already established in the literature as a baseline.
- Did not examine structural correlates of maturation (t-tubules, sarcomere organization, cell-cycle exit, multinucleation) that often accompany functional/metabolic changes.
- Monolayer culture only; no 3D tissue format, which the authors note could mask or alter component effects.
- The authors note possible galactose toxicity (p. 12).
- No extracellular field-potential (FP/MEA) voltage recording was performed — the electrophysiology-adjacent readouts were impedance (CardioExcyte96) and patch-clamp AP/Nav, not FPD. The paper's "electrophysiological maturation" axis is therefore not directly expressed in MEA-FP units.

## Relevance to our paper
This paper does not itself provide MEA-derived reference values for hiPSC-CM maturation. Its own conclusion is that functional, metabolic and transcriptional maturation are induced largely independently. Our inference, not the paper's: an MEA-FP-derived maturation benchmark could then characterise only the electrophysiological compartment. Its patch-clamp values (MMc vs RBAI, specific lines, day 30, one protocol: MDP, Vmax, Nav density) are not proposed by the authors as reference values. Its RNA-seq shows medium-dependent ion-channel expression (higher KCNJ2, CACNA1C and KCNQ1, lower HCN4, no SCN5A change in MMc vs RBAI), which parallels the culture-age changes of Guerrelli et al. (2024), although this paper did not vary culture age.

## See also
- [[wiki/papers/ismaili-2023-hamburg.md]]
- [[wiki/papers/guerrelli-2024-hipscm.md]]
- [[wiki/papers/maki-2023-opinion.md]]
- [[wiki/papers/correia-2024-acc2.md]]
- [[wiki/papers/scheurer-2025-optical-ai.md]]
- [[wiki/hipsc-cm-maturation.md]]
