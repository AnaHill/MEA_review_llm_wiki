---
tags: [maturation, mea]
---

# Comprehensive promotion of iPSC-CM maturation by integrating metabolic medium with nanopatterning and electrostimulation

**Authors:** Wener Li, Xiaojing Luo, Anna Strano, Shakthi Arun, Oliver Gamm, Mareike S. Poetsch, Marcel Hasse, Robert-Patrick Steiner, Konstanze Fischer, Jessie Pöche, Ying Ulbricht, Mathias Lesche, Giulia Trimaglio, Ali El-Armouche, Andreas Dahl, Peter Mirtschink, Kaomei Guan, Mario Schubert  
**Year:** 2025  
**Venue:** Nature Communications 16, 2785 (received 27 March 2024, accepted 3 March 2025; open access, CC BY)  
**File:** [[raw/li-2025-maturation.pdf]] (+ [[raw/li-2025-maturation-supplementary.pdf]], [[raw/li-2025-maturation-supplementary-description.txt]]; Supplementary Data 1–3 and Supplementary Movie 1 not downloaded)  
**DOI:** 10.1038/s41467-025-58044-6

## Contribution
A stepwise test of three maturation stimuli for 2D iPSC-CM cultures: a fatty-acid-enriched maturation medium (MM) with a high calcium concentration (1.8 mM, against 0.4 mM in the RPMI-based B27 control), nanopatterned culture surfaces (NP) and 2 Hz electrostimulation (ES). The authors report that ES is the key driver of mitochondrial development, metabolic maturation and improved electrophysiology, that the high calcium concentration strongly promotes electrophysiological maturation, and that NP mainly improves sarcomere organisation (abstract, p. 1). The combined approach changed the cells' responses to verapamil, E-4031 and isoprenaline on the MEA, which the authors present as pharmacological responses closer to those of adult cardiomyocytes. The same group's Scheurer et al. (2025) rests its "mature" and "less mature" labels on this paper (see Relevance).

## Methodology
- **Cells:** ventricular-like iPSC-CMs from three healthy-donor lines (isWT7.22, iWTD2.1, iBM76.3), differentiated with CHIR/IWP2; on day 15–16 digested and split into four groups, B27, MM, MM+NP and MM+NP+ES, cultured to day 42 (Fig. 1a). A fifth MM+ES group was compared with MM later (Fig. 10).
- **Media:** B27 medium = RPMI 1640 + 1× B27, 11.1 mM glucose, 0.4 mM Ca²⁺. MM = glucose-free DMEM with 7 mM glucose, 0.8 mM lactate, B27 minus insulin, 50 nM insulin, ascorbic acid, taurine, creatine, carnitine, AlbuMax (lipid-rich BSA), NEAA, KOSR, vitamin B12, 1.8 mM Ca²⁺, modified from Feyen et al. (2020) (Supplementary Table 1). A DMEM+B27 control (1.8 mM Ca²⁺) separated the calcium effect.
- **MEA:** Axion Maestro Edge with AxIS Navigator, 37 °C, 12,500 Hz sampling (p. 15). On day 42 cells were replated onto Geltrex-coated CytoView 6-well MEA plates (about 200,000 cells, baseline FP parameters) or 24-well plates (25,000 cells/well, drug tests) and recovered for 7 days in their maturation-period medium; all groups were incubated in MM for one hour before recording "to avoid the influence of different media". Metrics: conduction velocity (CV), spike amplitude, spike slope, inter-beat interval, Fridericia-corrected FPD (FPDc), analysed with AxIS Navigator, Cardiac Analysis Tool and AxIS Metric Plotting tool. Drugs added sequentially, 12 min incubation, 2 min recording. The Methods do not say whether ES continued during the 7-day recovery on the MEA plates.
- **Other assays:** manual and automated patch clamp (AP parameters spontaneous and paced at 0.5 Hz; INa, Ito, IK1, IKr, ICa-L), Fura-2 Ca²⁺ imaging, video motion analysis, immunostaining, flow cytometry, Seahorse respirometry, bulk RNA-seq compared with published human foetal ventricle and adult heart datasets (Supplementary Fig. 6).
- **Statistics:** Kruskal–Wallis with Dunn's test for AP and FP parameters, comparisons against the B27 group only (Fig. 2 legend).

## Findings
- **Field potential parameters (Supplementary Table 3, mean ± SD, n = 24 cultures/group from 4 differentiations of 2 lines):**

  | Group | CV (cm/s) | Spike amplitude (mV) | Spike slope (V/s) |
  |---|---|---|---|
  | B27 | 12.5 ± 5.8 | 3.2 ± 1.2 | −3.6 ± 1.8 |
  | MM | 22.3 ± 3.7 | 10.4 ± 4.9 | −21.2 ± 11.3 |
  | MM+NP | 25.6 ± 4.3 | 10.7 ± 4.8 | −23.6 ± 11.1 |
  | MM+NP+ES | 27.8 ± 7.3 | 13.6 ± 5.3 | −29.1 ± 12.6 |

  The text calls the change in CV "stepwise" and links it to increased Cx43 membrane localisation (p. 2). The largest step is from B27 to MM; between the three MM groups the SDs overlap widely. Baseline FPDc and beat rate are not reported per group; FPDc is used only for drug effects.
- **Action potentials (Supplementary Table 2, mean ± SD):** RMP −44.1 (B27), −49.7 (MM), −58.2 (MM+NP), −65.6 mV (MM+NP+ES); Vmax 4.2, 5.0, 6.6, 11.0 V/s; APA 70.6, 78.7, 88.4, 97.8 mV; APD90 at 0.5 Hz pacing 980.5, 732.3, 752.5, 539.3 ms. A "notch-and-dome" AP shape appeared in 43 % of MM+NP+ES cells and in no other group.
- **Ion currents:** INa peak density −42.3 (B27), −81.6 (MM), −92.1 (MM+NP), −135.7 pA/pF (MM+NP+ES); IK1 −2.1, −5.3, −11.7, −16.0 pA/pF at −130 mV; Ito and IKr increased; ICa-L decreased. The authors state that the INa data "are consistent with the AP- (Vmax, APA) and FP-metrics (CV, spike amplitude and slope)" (p. 3). This is agreement in direction between group means; patch clamp and MEA were done on different cells (single cells versus replated monolayers).
- **Calcium:** DMEM+B27 (1.8 mM Ca²⁺) reproduced most of the MM effects on Ca²⁺ handling, INa (−90.4 pA/pF) and ICa-L, so the authors attribute the MM effect on INa, ICa-L and Ca²⁺ cycling largely to the high calcium concentration (p. 8).
- **Drug responses on MEA:** 1 µM verapamil stopped beating in 17/17 B27, 6/17 MM and 6/18 MM+NP cultures and had no effect on beating or spike amplitude in MM+NP+ES; verapamil-induced FPDc shortening was larger in the three MM groups than in B27; E-4031 gave only minor FPDc changes in B27 but concentration-dependent prolongation in the MM groups; isoprenaline EC50 for the chronotropic effect 6.8 nM (B27), 4.3 nM (MM), 1.9 nM (MM+NP), 1.8 nM (MM+NP+ES) (Fig. 6). No significant arrhythmias with any of the three drugs.
- **Transcriptome:** NP added little to MM (163 differentially expressed genes), ES much more (1370 up, 1657 down against MM). Against published foetal and adult heart datasets, the MM+NP+ES cells were "intermediate between that of human foetal and adult CMs" (p. 11; Supplementary Fig. 6).
- **ES alone:** MM+ES reproduced most of the electrophysiological and polyploidy effects of MM+NP+ES, to a lesser extent (Fig. 10).

## Limitations
- Authors' own: the NP surface is far stiffer than diastolic adult myocardium (8–15 kPa; the modulus is printed as "~7 mPa", presumably MPa, since the authors call it "much higher"), and structural maturation remains below that of 3D tissues (p. 8); automaticity of the MM+NP+ES cells was not studied (p. 10).
- Our observations: the FP parameters are reported as group means only, with no thresholds, reference values or comparison with adult FP data; the authors do not propose them as maturity markers. MEA recordings were made after replating and 7 days of recovery, so the cells on the MEA had been off the NP surface for that time, and possibly off ES (not stated). All groups were recorded in MM, which differs from the B27 group's culture medium (1.8 vs 0.4 mM Ca²⁺); the spike amplitude and CV of the B27 group may therefore partly reflect an acute medium change. Statistics compare each group only with B27, so the steps between the MM groups are not tested. MEA data come from two of the three lines.
- The spike slope values (−3.6 to −29.1 V/s) are as printed in Supplementary Table 3; we did not check whether "V/s" is the unit Axion's software reports for this metric.

## Relevance to our paper
Cited in main.md from 2026-10-30 (Maturation section and the Conclusion's fourth gap) for points 1 and 2; point 3 is not used in main.md.

1. **MEA field-potential parameters separate maturation conditions (2022 onward).** CV, spike amplitude and spike slope differ between B27 and maturation-medium cultures, in the same direction as the patch-clamp markers of maturity (RMP, Vmax, INa, IK1). With Guerrelli et al. (2024), whose evidence is culture-time drift, this is the in-scope MEA evidence that FP parameters change with maturation. It does not propose reference values, so the gap stated in main.md remains.
2. **Source of the labels in Scheurer et al. (2025).** Scheurer et al. (2025), from the same group (Schubert, Steiner, Gamm and Guan are authors of both), call cells in MM "more mature" than cells in B27 "based on previous reports demonstrating an enhanced electrophysiological function, calcium handling, metabolic activity [11]", and attribute the lower maturation of B27 cultures to the same reference [11], which is this paper (Scheurer text, pp. 5–6). The media match: Scheurer's B27 medium is RPMI 1640 with 2 % B27, and its MM lists the same components as this paper's MM (Supplementary Table 1; Scheurer also lists 82 nM biotin). The schedules differ: here MM started on day 15–16, in Scheurer on day 21; both groups are read on day 42 (this paper's MEA about a week later, after replating). Our reading: the culture conditions that Scheurer's video classifier separates already have MEA field-potential data from the same group, with B27-versus-MM differences in CV (12.5 vs 22.3 cm/s), spike amplitude (3.2 vs 10.4 mV) and spike slope; no one has trained a classifier on those FP features.
3. **Maturation changes MEA drug responses.** Verapamil arrest and the absent E-4031 FPDc prolongation in B27 cultures support main.md's point that maturation status is a confound for MEA-derived endpoints. The FPDc here is Fridericia-corrected, as in most of the reviewed MEA studies.

## See also
- [[wiki/hipsc-cm-maturation.md]]
- [[wiki/papers/scheurer-2025-optical-ai.md]]
- [[wiki/papers/fetterman-2024-maturation.md]]
- [[wiki/papers/correia-2024-acc2.md]]
- [[wiki/papers/guerrelli-2024-hipscm.md]]
- [[wiki/fridericia-rate-correction.md]]
- Search that selected this source: docs/maturation-mea-search.md
