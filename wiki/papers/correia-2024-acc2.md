---
tags: [maturation, in-vitro-maturation-media, electromechanical, 3d-model, disease-model]
---

# Enhancing Maturation and Translatability of Human Pluripotent Stem Cell-Derived Cardiomyocytes through a Novel Medium Containing Acetyl-CoA Carboxylase 2 Inhibitor

**Authors:** Cláudia Correia, Jonas Christoffersson, Sandra Tejedor, Saïd El-Haou, Meztli Matadamas-Guzman, Syam Nair, Pierre Dönnes, Gentian Musa, Mattias Rohman, Monika Sundqvist, Rebecca B. Riddle, Bramasta Nugraha, Ioritz Sorzabal Bellido, Markus Johansson, Qing-Dong Wang, Alejandro Hidalgo, Karin Jennbacken, Jane Synnergren, Daniela Später
**Year:** 2024
**Venue:** Cells 13, 1339
**File:** [[raw/correia-2024-acc2.pdf]] (+ [[raw/correia-2024-acc2-supplementary.pdf]])
**DOI:** 10.3390/cells13161339

## Contribution
A pharma-industry (AstraZeneca) maturation-medium study combining established metabolic/hormonal maturation inducers (glucose-depleted, galactose- and fatty-acid-enriched base + a T3/IGF1/dexamethasone hormone cocktail) with a small-molecule inhibitor of Acetyl-CoA carboxylase 2 (ACC2i, CP-640186) to further drive fatty-acid oxidation. The medium broadly improves metabolic, electrophysiological, structural, and molecular maturation of hPSC-CMs (3 hiPSC lines + 1 hESC line), and — distinctively — demonstrates that this maturation improves downstream translational validity: a more physiologically faithful hypertrophy disease model and a validated in vitro-to-in vivo pharmacokinetic correlation.

## Methodology
- 4 cell lines (iCell CMs2, ChiPS22, iPSC C32, hESC SA121), maturation medium applied for ~2 weeks.
- **Metabolism:** Seahorse XF96 extracellular flux (OCR/ECAR, spare respiratory capacity, FA-oxidation via etomoxir).
- **Transcriptomics:** RNA-seq (3 hiPSC lines) + qPCR validation; IPA pathway enrichment.
- **Structure:** immunofluorescence/confocal imaging (Cx43, α-sarcomeric actinin, PLN, SERCA2, cTNT) + TEM ultrastructure; sarcomere FFT anisotropy/length; SarcGraph Z-disk quantification.
- **Calcium:** Fluo-4 and EarlyTox calcium-dye imaging (amplitude, upstroke/decay velocity, PWD70%).
- **Electrophysiology:** perforated/ruptured whole-cell patch-clamp (spontaneous AP: MDP, dV/dt max, APD90; voltage-clamp: I_Na, I_Ca,L, I_K1) and FluoVolt single-cell voltage imaging for ventricular/atrial/pacemaker subtype classification. **No MEA or extracellular field-potential recording is used anywhere in this study** — all electrophysiology is patch-clamp/optical-voltage based.
- **3D:** engineered heart tissue microtissues (Novoheart µCTScreen) — force, contraction/relaxation kinetics, pacing-capture up to 4 Hz.
- **Translatability:** in vitro BCKDK-inhibitor dose-response (LC-MS/MS ketovaline) correlated against in vivo rat plasma PK/PD IC50 values for 21 compounds; ET-1-induced acute hypertrophy as a disease-model readout.

## Findings
- Matured hPSC-CMs: more hyperpolarized MDP (−79.2 vs. −74.3 mV), faster AP upstroke (dV/dt max 68.6 vs. 23.4 V/s), shorter APD90 (357 vs. 829 ms), 2-fold I_Na, +40% I_Ca,L, and a 6-fold increase in I_K1 — reaching levels comparable to adult human/rabbit ventricular CMs and exceeding several other published maturation protocols (including the carnitine/creatine/taurine-based formulation characterized in Fetterman et al. 2024, cited directly by this paper).
- Ventricular subpopulation in hESC-CMs increased from 60% to 80% under maturation medium (voltage-imaging classification).
- 3D microtissues in maturation medium showed faster contraction/relaxation kinetics and could follow pacing up to 4 Hz, vs. failure beyond 1 Hz for standard-medium tissues.
- ET-1 hypertrophic stimulation produced a markedly stronger structural, transcriptional, and metabolic response in matured cells (2× more DEGs) — matured hPSC-CMs act as a more sensitive disease model.
- BCKDK-inhibitor in vitro IC50 values correlated significantly with in vivo rat plasma IC50 across 21 compounds **only** in matured cells (Figure 7F, visually verified: Pearson r = 0.85, R² = 0.72, p < 0.0001, log-log scale spanning ~4 orders of magnitude); standard-medium cells showed no usable in vitro-to-in vivo correlation at all — not a weaker correlation, but no computable one, since standard-medium cells largely failed to respond to BCKDK inhibition (Figure 7D–E).
- Explicitly cites Fetterman et al. 2024's finding that functional/metabolic/transcriptional maturation are not inherently linked, and frames ACC2i as a mechanistically distinct, additive lever on top of existing maturation cocktails rather than a replacement for them.
- **Table S2 (supplementary) cross-compares 8 published maturation-medium formulations**, including Fetterman et al. 2024's, component by component. Notably, Correia's own medium omits creatine, taurine, and dedicated sodium selenite — all present in Fetterman's optimized formulation — consistent with Correia's own citation of Fetterman's finding that these three components are "dispensable" for Ca²⁺/impedance/Nav-current maturation. The two media otherwise overlap substantially (glucose-free base, galactose, palmitic/oleic acid, dexamethasone, T3); ACC2i (5 µM) is unique to Correia's formulation and IGF1 (100 ng/mL) is shared only with Birket et al. 2015's much earlier formulation.

## Limitations
- The mechanistic link between ACC2i and the observed downstream Ca²⁺-handling/electrophysiology improvements is not established — the authors explicitly note they have not determined whether these are direct ACC2i effects or indirect consequences of enhanced metabolic maturity.
- The MYH6:MYH7 isoform shift moves in the direction associated with physiological hypertrophy (T3-induced), which is *opposite* to the shift seen in adult CM maturation — a caveat on how "adult-like" the transcriptional profile really is.
- Electrophysiological maturation is assessed entirely via patch-clamp and voltage-imaging; despite describing the improvement as "electrophysiological maturation," the study provides no extracellular/MEA field-potential data and cannot speak to MEA-derived metrics directly.
- Benchmarking against other maturation protocols is a literature-table comparison (Table S2), not a head-to-head experimental comparison.

## Relevance to our paper
A second maturation-medium study for the wiki's maturation-gap thread, directly cross-referencing Fetterman et al. 2024. Its distinct contribution to our argument: it is the first source in this wiki to show a *quantitative, validated link* between improved (patch-clamp-defined) electrophysiological/functional maturity and downstream translational validity (an in vitro-to-in vivo PK/PD correlation achieved only in matured cells) — direct empirical support for the gap section's claim that maturation staging matters for clinical translation, not just an assertion. It remains, however, entirely non-MEA: the electrophysiological maturation it documents is inaccessible to an MEA-only pipeline, reinforcing that the specific MEA-derived reference-value gap is still open.

## See also
- [[wiki/papers/fetterman-2024-maturation.md]]
- [[wiki/hipsc-cm-maturation.md]]
- [[wiki/papers/maurissen-2024-mutation.md]]
