# Lint fixes of 2026-10-24: what changed and why

Written for: the researcher, who asked for a summary good enough to judge each change. Every change below was applied by one script that recorded the text before and after, so the quotes are exact copies, not retellings. Wiki pages, the index and the claims list are tools for you; the only file that is the paper itself is `main.md` (group 7), so read that group first.

## How to check quickly

1. Read group 7 (the paper): six sets of sentences in `main.md` that were softened because no source supports them. For each, the reason is stated and the new wording only claims what the sources show.

2. Read groups 1 to 3 (maturation page, critical assessment, Weiser-Bitoun page): corrections of statements that the 2026-10-24 source verification had already shown to be wrong elsewhere. Highest-risk edit: group 2, Claim 4 (inversion), because it reverses an earlier statement.

3. Skim group 4 (index lines) and group 6 (four new pages built only from facts already on the verified paper pages).

4. Commands: `git diff --stat`, `git diff main.md`, `python -I scripts/check.py` (0 errors expected; 3 known warnings).

## Summary

| Group | Entries |
|---|---|
| 1. wiki/hipsc-cm-maturation.md | 6 |
| 2. wiki/critical-assessment-maki-claims.md | 12 |
| 3. wiki/papers/weiser-bitoun-2026-physiomea.md | 2 |
| 4. wiki/index.md | 14 |
| 5. Limitations (v) and Välimäki (no change, by your decision) | 0 |
| 6. new concept and method pages | 4 |
| 7. main.md: softened generalisations (synthesis items 1, 3, 9, 10, 14, 15) | 11 |
| 8. docs/claims-by-source.md: claims and synthesis items brought in line with the softened text | 20 |
| 9. Licence, README, export notes, ToDo | 7 |

## Not changed (your decisions or later)

- Lint item 5 (Limitations (v) and Välimäki): no change, as you decided; the full texts were read wherever available and Välimäki was not available.

- Synthesis items 2, 4, 5, 6, 7, 8, 11, 12, 13 in `docs/claims-by-source.md` and the Abstract's mention of the outlook (you decided it is not needed).

- Your `<!-- needs citation(s) -->` comment in the Motivation section and the style markers in the Abstract.

- `raw/` files, `notes.md`, the reference list and `wiki/references.md`.

## Points to look at

- The new multimodal page says that the feature-ranking module of Lee et al. (2024) handles features from extracellular and intracellular-like signals and that it was not checked whether it combines them in one model. If it does, the sentence in `main.md` (Discussion and future outlook) that 'in these studies the modalities are mostly analysed separately or side by side' needs a qualification for Lee et al.

- The index summary for Välimäki (2021) was left as set earlier the same day (MEA use confirmed by you, content not read).

- `LICENSE` is the official CC BY 4.0 text and covers the written content. After the first version of this summary you chose MIT for the code, so `scripts/LICENSE` (standard MIT text, copyright holder "Antti-Juhana Mäki", year 2026) was added and the README Licence section now says that `scripts/` is MIT. The README entry in group 9 below shows the earlier wording; the final wording is in `README.md`. Check that the copyright holder name is the one you want.

## Group 1. wiki/hipsc-cm-maturation.md

### 1. `wiki/hipsc-cm-maturation.md`: Opening paragraph: fetal-like phenotype and subtypes

**Why:** The old sentence cited Ismaili et al. for the 'fetal' statement and presented heterogeneous subtypes as established; Ismaili et al. say the mixed-population question is debated and that ICa,T presence is not necessarily a sign of immaturity. The wording now matches main.md (maturation paragraph), where 'fetal-like' is cited to Correia and Scheurer and the subtype proportions to Park et al. (2026).

**Before:**

> hiPSC-CMs are widely acknowledged to resemble fetal rather than adult cardiomyocytes (Ismaili et al. 2023): they express funny current (If) and T-type Ca²⁺ current not present in mature adult ventricular myocytes, and show heterogeneous ventricular-, atrial-, and nodal-like subtypes within the same preparation.

**After:**

> hiPSC-CMs are widely described as resembling fetal rather than adult cardiomyocytes (Correia et al. 2024; Scheurer et al. 2025). They express the funny current (If) and occasionally the T-type Ca²⁺ current, which are absent from adult human working myocardium (although the presence of ICa,T is not necessarily a sign of immaturity); whether ventricular-, atrial- and nodal-like cells form distinct subpopulations within one preparation is debated (Ismaili et al. 2023), but patch-clamp data show them in the lines of Park et al. (2026).

### 2. `wiki/hipsc-cm-maturation.md`: Clinical translation bullet: Correia

**Why:** 'PK/PD correlation' and 'translatable vs non-translatable assay' generalised a single-target result; main.md had already been corrected to 'target-engagement correlation ... for one drug target' (correction 7 of the 2026-10-24 verification). The page now says the same, with the figures from Figure 7F (r = 0.85, 21 inhibitors).

**Before:**

> Correia et al. (2024) give this concrete empirical weight outside the MEA context: their ACC2-inhibitor maturation medium produced a significant in vitro-to-in vivo PK/PD correlation across 21 BCKDK-inhibitor compounds — but **only** in matured cells; standard-medium cells produced no usable correlation at all. Maturation status was the difference between a translatable and a non-translatable in vitro assay.

**After:**

> Correia et al. (2024) give this concrete empirical weight outside the MEA context, for one drug target: with their ACC2-inhibitor maturation medium, in vitro IC50 values of 21 BCKDK inhibitors correlated with in vivo rat plasma IC50 values (a target-engagement correlation, r = 0.85), whereas standard-medium cells largely failed to respond to BCKDK inhibition, so no correlation could be computed. For this target, maturation status was the difference between a usable and an unusable in vitro-to-in vivo correlation.

### 3. `wiki/hipsc-cm-maturation.md`: Fetterman paragraph

**Why:** This is the passage that was replaced in main.md on 2026-10-24 (correction 6): 'nine formulations' applies to the RNA-seq comparison only, and the 'no effect ... and vice versa' statement was not what the paper shows. The page now carries the verified example and marks the last sentence as our inference.

**Before:**

> Fetterman et al. (2024) is the clearest demonstration that "maturation" is not one thing. Using high-throughput assays across nine culture-medium formulations, they showed that **functional (electrophysiology/EC-coupling), metabolic, and transcriptional maturation are induced largely independently** — components that improved AP kinetics and Na⁺ current density had no effect on mitochondrial respiration, and vice versa. A single scalar "maturation score" derived from any one modality — including MEA — can therefore only ever describe one compartment of maturity, not the whole phenotype.

**After:**

> Fetterman et al. (2024) is a clear demonstration that "maturation" is not one thing. By adding and removing individual components of a defined medium, and comparing nine medium formulations by RNA-seq, they found that **functional (electrophysiology/EC-coupling), metabolic, and transcriptional maturation are induced largely independently** by different medium components — for example, removing fatty acids lowered mitochondrial respiration without changing Ca²⁺ dynamics (summary, p. 2; p. 7). A single scalar "maturation score" derived from any one modality — including MEA — could therefore describe only one compartment of maturity (our inference), not the whole phenotype.

### 4. `wiki/hipsc-cm-maturation.md`: Bullet on adult/mature reference values

**Why:** The old bullet said that Ismaili et al. and Fetterman et al. 'both report adult/mature benchmark values'. The Ismaili page records no such values, and Fetterman et al. compare media, not adult cells. The bullet now lists only values that the Fetterman and Correia pages record (medium versus control; Correia compares IK1 with adult cells).

**Before:**

> - **Adult reference points exist from non-MEA electrophysiology.** Ismaili et al. (2023) and Fetterman et al. (2024) both report adult/mature benchmark values (e.g. resting/maximum diastolic potential, AP upstroke velocity, APD) from patch-clamp — but these are intracellular, not extracellular FP, measurements, so they cannot be applied to MEA data without a validated conversion.

**After:**

> - **Patch-clamp values for more mature hiPSC-CMs exist, but not for MEA.** Fetterman et al. (2024) report, for their complete maturation medium versus a control medium, a maximum diastolic potential of −68.1 versus −51.7 mV and an AP upstroke velocity of 30.2 versus 7.3 mV/ms; Correia et al. (2024) report −79.2 versus −74.3 mV and a six-fold higher IK1, which they compare with adult human and rabbit ventricular cells (p. 24). These are intracellular, not extracellular FP, measurements, so they cannot be applied to MEA data without a validated conversion.

### 5. `wiki/hipsc-cm-maturation.md`: Gap paragraph: FPD–contraction link

**Why:** Aligns the wording with the Hayakawa et al. (2014) paper as read in full on 2026-10-24 (linear relationship per drug with different slopes, non-arrhythmic conditions only) and with main.md.

**Before:**

> the physiological link (FPD–contraction-duration correlation) all already exist in the literature

**After:**

> the physiological link (FPD related to contraction duration within a drug, in non-arrhythmic conditions; Hayakawa et al., 2014) all already exist in the literature

### 6. `wiki/hipsc-cm-maturation.md`: See also: link to the Hayakawa page

**Why:** The page cites Hayakawa et al. (2014), so it now links to its wiki page.

**Before:**

> (end of list)

**After:**

> - [[wiki/papers/hayakawa-2014-motion-fp.md]]

## Group 2. wiki/critical-assessment-maki-claims.md

### 7. `wiki/critical-assessment-maki-claims.md`: Date line

**Why:** Records that the page was revised after the 2026-06-22 draft.

**Before:**

> **Date:** 2026-06-22  

**After:**

> **Date:** 2026-06-22 (updated 2026-10-24 after the source verification; the sentences changed then are listed in docs/lint-fixes-2026-10-24.md)  

### 8. `wiki/critical-assessment-maki-claims.md`: Claim 2, species gap: Figs. 5–6

**Why:** Ernault et al.: only Fig. 5A–C uses hiPSC-CM recordings; Fig. 6 is entirely simulation (human atrial and ventricular and NRVM models).

**Before:**

> Ernault's separate hiPSC-CM experiments (LEAP, Figs. 5–6) test a different question

**After:**

> Ernault's separate hiPSC-CM experiments (LEAP, Fig. 5A–C; Fig. 6 is a simulation) test a different question

### 9. `wiki/critical-assessment-maki-claims.md`: Claim 2, prevalence

**Why:** The old text called positive-only T waves 'the majority'. Ernault et al. report only that biphasic T waves were a minority and that positive-only T waves occurred 'often'; a counted majority is not stated.

**Before:**

> 2. **Prevalence.** Biphasic T-waves — the precondition for the correlation to hold at all — occurred in only a **minority** of the monolayers Ernault et al. recorded. For the majority (monophasic T-waves), T-wave peak does **not** reliably indicate APD90 either. So even setting the species gap aside, "T-peak is better anchored to APD90" is true only for a minority of real recordings; for most, neither T-peak nor baseline-return is an empirically validated APD90 surrogate.

**After:**

> 2. **Prevalence.** Biphasic T-waves — the precondition for the correlation to hold at all — occurred in only a **minority** of the monolayers Ernault et al. recorded; the other monolayers often showed only a positive T wave that ended before the end of the action potential, which gave an unreliable assessment of local repolarization. So even setting the species gap aside, "T-peak is better anchored to APD90" holds only where a biphasic T wave is present, which was a minority of the recordings; elsewhere neither T-peak nor baseline-return was shown to be a validated APD90 surrogate.

### 10. `wiki/critical-assessment-maki-claims.md`: Claim 2: 'field is converging on T-peak'

**Why:** The claim of convergence is not supported by the reviewed platforms (three different end conventions) and conflicts with Lee et al.'s own finding. Replaced by what the pages document.

**Before:**

> Weiser-Bitoun et al. (2026, PhysioMEA) adopting R-to-T-peak operationally is a second data point: the field is converging on T-peak as standard, consistent with Ernault's APD90 finding.

**After:**

> Weiser-Bitoun et al. (2026, PhysioMEA) and Lee et al. (2024, CardioMEA) both use R-to-T-peak operationally, whereas Dunham et al. (2022) use a T-wave endpoint from a fitted trapezoid and Mäki (2023) the baseline return (Table 2 in main.md), so the conventions remain diverse. Two platforms adopting the T peak does not by itself validate it as an APD90 surrogate: Lee et al. found R-to-T-peak FPD to correlate only minimally with APD50 and APD90 in iCell recordings.

### 11. `wiki/critical-assessment-maki-claims.md`: Claim 2: Hayakawa 2014 added

**Why:** New evidence from the Hayakawa et al. (2014) ingest (p. 3), phrased with the paper's own hedge ('appears'). It supports the 'different quantities' reading that the page already argued.

**Before:**

> These are genuinely different quantities. The claim as written implies baseline return is simply more correct; the literature says it measures something *different*, not something better in all contexts.

**After:**

> These are genuinely different quantities. The claim as written implies baseline return is simply more correct; the literature says it measures something *different*, not something better in all contexts. Independent support comes from a mechanical measurement: in simultaneous video and MEA recordings of iCell monolayers, Hayakawa et al. (2014) noted that the two FPD end points in use at the time (the peak of the positive deflection and the return of the positive deflection to baseline) appeared to match different phases of the relaxation motion (its upstroke and its peak) and that an accurate end point was difficult to establish.

### 12. `wiki/critical-assessment-maki-claims.md`: Claim 2: 'majority' of non-biphasic

**Why:** Same correction as for the prevalence caveat: the paper gives a minority of biphasic T waves, not a counted majority of non-biphasic ones.

**Before:**

> For non-biphasic T-waves — which Ernault et al. (2024) report as the *majority* of recorded monolayers, not an edge case — T-wave peak does *not* reliably indicate APD90 either. In those cases,

**After:**

> Because biphasic T waves were found in only a minority of the monolayers in Ernault et al. (2024), the T-wave peak does *not* reliably indicate APD90 in many recordings either. In those cases,

### 13. `wiki/critical-assessment-maki-claims.md`: Claim 3: existence of nodal-like cells

**Why:** The old sentence said Ismaili et al. note 'the coexistence of nodal-like subtypes in typical preparations'; they call the mixed-population question debated. Park et al. (2026) now provides the patch-clamp proportion (about 70 %, 20 % and 9 % ventricular-, atrial-, nodal-like).

**Before:**

> The *existence* of pacemaker-like cells in hiPSC-CM cultures is well-supported: Ismaili et al. (2023) explicitly note If and ICa,T expression and the coexistence of nodal-like subtypes in typical preparations. The methodological point

**After:**

> The *existence* of pacemaker-like cells in hiPSC-CM cultures is supported in part: Ismaili et al. (2023) note If (HCN4) expression but call it debated whether ventricular-, atrial- and nodal-like cells form distinct subpopulations within one preparation, and patch-clamp data in Park et al. (2026) show about 9 % nodal-like cells in the normal lines. The methodological point

### 14. `wiki/critical-assessment-maki-claims.md`: Claim 3: broader observation

**Why:** Weiser-Bitoun et al. were listed among papers that say nothing about morphology handling, but their Methods describe inverted-signal branches and electrode exclusion (checked in the extracted text: low-amplitude R peaks, inverted T waves, inconsistent biomarker counts). The sentence now says what each paper does.

**Before:**

> **Broader observation from the available literature:** Guerrelli et al. (2024), Dunham et al. (2022), Weiser-Bitoun et al. (2026), and other tool/methods papers describe analysis frameworks without mentioning pacemaker-like morphology handling — consistent with the waveform type being silently excluded or filtered by vendor defaults, though this is not directly documented.

**After:**

> **Broader observation from the available literature:** Guerrelli et al. (2024) and Dunham et al. (2022) describe analysis frameworks without mentioning pacemaker-like morphology handling; Weiser-Bitoun et al. (2026) handle inverted T waves and low-amplitude R peaks via the inverted signal and exclude electrodes with inconsistent biomarker counts (p. 3) but do not describe pacemaker-like signals as such. This is consistent with the waveform type being excluded or filtered silently, though it is not directly documented.

### 15. `wiki/critical-assessment-maki-claims.md`: Claim 4: external corroboration

**Why:** The old text said that no other paper, including Weiser-Bitoun 2026, uses inversion. PhysioMEA does use an inverted-signal branch, for a different purpose; the sentence now states the related case and its limits.

**Before:**

> 2. *External corroboration is absent.* No other paper in the available literature (including Ernault 2024, Dunham 2022, Weiser-Bitoun 2026) describes this waveform type or validates the inversion approach.

**After:**

> 2. *External corroboration is largely absent.* No other paper in the wiki describes the "only high peak" waveform type or validates its inversion (Ernault 2024 and Dunham 2022 do not mention it). Weiser-Bitoun et al. (2026) do analyse an inverted signal for inverted T waves and low-amplitude R peaks (p. 3), a related but different case that shows the idea of analysing inverted signals outside the opinion paper without validating the "only high peak" case.

### 16. `wiki/critical-assessment-maki-claims.md`: Summary table, row 4

**Why:** Keeps the summary table consistent with the Claim 4 correction.

**Before:**

> | 4. Only-high-peak → inversion | Credible internal observation | Typographic error corrected; diagnosis criterion and external replication still needed | Medium — criterion to be specified in future work |

**After:**

> | 4. Only-high-peak → inversion | Credible internal observation | Typographic error corrected; diagnosis criterion and external replication still needed (PhysioMEA uses a related inverted-signal branch for other cases) | Medium — criterion to be specified in future work |

### 17. `wiki/critical-assessment-maki-claims.md`: References list: Ismaili

**Why:** Matches the Claim 3 correction.

**Before:**

> - [[wiki/papers/ismaili-2023-hamburg.md]] — If/ICa,T expression and nodal-like subtypes (supports existence of pacemaker-like cells, Claim 3)

**After:**

> - [[wiki/papers/ismaili-2023-hamburg.md]] — If/ICa,T expression; the mixed-population question is debated (Claim 3)

### 18. `wiki/critical-assessment-maki-claims.md`: References list: Weiser-Bitoun, plus Hayakawa and Park 2026

**Why:** Corrects the PhysioMEA line and adds the two pages that the updated text now relies on.

**Before:**

> - [[wiki/papers/weiser-bitoun-2026-physiomea.md]] — PhysioMEA adopts R-to-T-peak (field convergence against Claim 2; silent on Claims 3 and 4)
>

**After:**

> - [[wiki/papers/weiser-bitoun-2026-physiomea.md]] — PhysioMEA uses R-to-T-peak (one convention among several, Claim 2) and an inverted-signal branch for inverted T waves and low R peaks (related to Claim 4); silent on pacemaker-like signals (Claim 3)
> - [[wiki/papers/hayakawa-2014-motion-fp.md]] — two FPD end points appear to match different phases of the relaxation motion (supports the 'different quantities' reading of Claim 2)
> - [[wiki/papers/park-2026-genotype-ml.md]] — patch-clamp proportions of ventricular-, atrial- and nodal-like cells in the normal lines (Claim 3)
>

## Group 3. wiki/papers/weiser-bitoun-2026-physiomea.md

### 19. `wiki/papers/weiser-bitoun-2026-physiomea.md`: Front matter tag

**Why:** Restores the waveform-morphology tag, which fits now that the page records the inverted-signal handling.

**Before:**

> tags: [open-platform, fiducial-definition, spatial-analysis, brv]

**After:**

> tags: [open-platform, fiducial-definition, waveform-morphology, spatial-analysis, brv]

### 20. `wiki/papers/weiser-bitoun-2026-physiomea.md`: Methodology bullet on morphology handling

**Why:** The page did not mention the inverted-signal branches or the electrode exclusion, although main.md cites the paper for morphology-dependent analysis branches and claims-by-source.md records them. Wording from the paper's Methods (verified in the extracted text).

**Before:**

> - **Cohorts:** 15 organoids

**After:**

> - **Morphology handling (p. 3):** for low-amplitude R peaks the minimum peaks of the signal are found on the inverted signal; for inverted T waves the inverse segment of the signal is used to detect the inverted T peaks; electrode data with inconsistent biomarker value counts are excluded.
> - **Cohorts:** 15 organoids

## Group 4. wiki/index.md

### 21. `wiki/index.md`: Correia

**Why:** 'PK/PD correlation' replaced by the verified 'target-engagement correlation for 21 BCKDK inhibitors' (one target).

**Before:**

> - [Correia et al. 2024](papers/correia-2024-acc2.md) — ACC2-inhibitor maturation medium improves metabolic/electrophysiological/structural maturity (patch-clamp, not MEA); in vitro-to-in vivo BCKDK-inhibitor PK/PD correlation achieved only in matured cells. AstraZeneca, *Cells* 13:1339.

**After:**

> - [Correia et al. 2024](papers/correia-2024-acc2.md) — ACC2-inhibitor maturation medium improves metabolic/electrophysiological/structural maturity (patch-clamp, not MEA); in vitro-to-in vivo target-engagement correlation for 21 BCKDK inhibitors obtained only in matured cells. AstraZeneca, *Cells* 13:1339.

### 22. `wiki/index.md`: Dunham

**Why:** The old 'power-law stats' hid that the analysis concerns quiescent periods between pacemaker translocations, and 'FPD' omitted the T-wave endpoint convention that Table 2 relies on.

**Before:**

> - [Dunham et al. 2022](papers/dunham-2022-cardiopyemea.md) — Cardio PyMEA open-source Python tool: beat detection, LAT mapping, CV, FPD, power-law stats. UCLA, *PLOS ONE*.

**After:**

> - [Dunham et al. 2022](papers/dunham-2022-cardiopyemea.md) — Cardio PyMEA open-source Python tool (PyQt5 GUI; input from Multichannel Systems exports): beat detection, pacemaker origin, LAT mapping, conduction velocity, FPD with a trapezoid-area T-wave endpoint; power-law analysis of pacemaker translocations. UCLA, *PLOS ONE* 17(5):e0266647.

### 23. `wiki/index.md`: Ernault

**Why:** The old line said 'hiPSC-CM monolayers' (the T-wave work is in rat cells) and 'LEAP reflects spatial average APD' (the paper does not say so).

**Before:**

> - [Ernault et al. 2024](papers/ernault-2024-interpretation.md) — FP and LEAP interpretation from hiPSC-CM monolayers; T-wave biphasic morphology required for APD90 correlation; LEAP reflects spatial average APD. *Am J Physiol* 326:H800–H811.

**After:**

> - [Ernault et al. 2024](papers/ernault-2024-interpretation.md) — FP and LEAP interpretation: in NRVM monolayers the T-wave peak tracks APD90 (and the T-wave upstroke APD50) only for biphasic T waves, a minority morphology; LEAP (hiPSC-CM recordings and simulations) is generated by neighbouring-cell current and matches local APD90 only in its terminal duration. *Am J Physiol Heart Circ Physiol* 326:H800–H811.

### 24. `wiki/index.md`: Hwang

**Why:** The old line ('electrode contact area, size ... primary FP variability source; E-4031 IC50 8 nM') came from the pre-verification page; the page now says stimulation and electrode locations, and gives no single IC50 value.

**Before:**

> - [Hwang et al. 2023](papers/hwang-2023-spheroids.md) — 3D spheroid geometry (electrode contact area, size) is a primary FP variability source; in silico models; E-4031 IC50 8 nM. *Front Physiol* 14:1123190.

**After:**

> - [Hwang et al. 2023](papers/hwang-2023-spheroids.md) — In silico 3D models of hiPSC-CM spheroids on an MEA compared with in vitro MEA data: FP shapes vary strongly with stimulation and electrode location, so three-dimensionality contributes to FP variability; Fridericia FPDc; E-4031 and nifedipine IC50 values from matched FPD in line with the literature. *Front Physiol* 14:1123190.

### 25. `wiki/index.md`: Ismaili

**Why:** 'FPDc limitations' was removed: the paper does not discuss FPD or rate correction (the finding that led to correction 1 of the 2026-10-24 verification).

**Before:**

> - [Ismaili et al. 2023](papers/ismaili-2023-hamburg.md) — Hamburg perspective review: hiPSC-CM If/ICa,T expression, AP heterogeneity, FPDc limitations, automated patch clamp. *Front Physiol* 14:1132165.

**After:**

> - [Ismaili et al. 2023](papers/ismaili-2023-hamburg.md) — Hamburg perspective review: hiPSC-CM If/ICa,T expression, the mixed-population (ventricular/atrial/nodal) debate, atrial models, automated patch clamp; the paper does not discuss MEA, FPD or rate correction. *Front Physiol* 14:1132165.

### 26. `wiki/index.md`: Mäki 2023

**Why:** The index said 'Zenodo v2'; the page, main.md and the reference list use v3 (version list of the record).

**Before:**

> - [Mäki 2023](papers/maki-2023-opinion.md) — Opinion: first positive FP peak is neighbor-cell artifact; FPD end = baseline return not repolarization peak; morphology-aware handling for pacemaker/inverted signals; DatAnalyzer. Zenodo v2.

**After:**

> - [Mäki 2023](papers/maki-2023-opinion.md) — Opinion: first positive FP peak is neighbor-cell artifact; FPD end = baseline return not repolarization peak; morphology-aware handling for pacemaker/inverted signals; DatAnalyzer. Zenodo v3 (published 23 June 2026; first version 2023).

### 27. `wiki/index.md`: Matsuda

**Why:** '13.5 µm pitch' was wrong (the paper gives 11 µm electrodes with 0.25 µm spacing); the missing FPD/FPDc is the finding behind correction 11 of the verification.

**Before:**

> - [Matsuda et al. 2025](papers/matsuda-2025-uhd.md) — Sony UHD-CMOS-MEA (236,880 electrodes, 13.5 µm pitch): field potential imaging (FPI), excitation origin count, propagation area, CV maps. *Toxicol Sci* 208(2):384–400.

**After:**

> - [Matsuda et al. 2025](papers/matsuda-2025-uhd.md) — Sony UHD-CMOS-MEA (236,880 electrodes over 5.9 × 5.5 mm; 11 µm electrodes): field potential imaging, excitation origins, propagation area, conduction velocity; 11 compounds; doxorubicin effects at 0.03 µM within 24 h; no FPD or FPDc in its own recordings. *Toxicol Sci* 208(2):384–400.

### 28. `wiki/index.md`: Park 2025

**Why:** '8 CiPA drugs' and '10× sensitivity' were stronger than the paper (it says arrhythmogenic drugs; the ratio is 3.3- to 10-fold with no test).

**Before:**

> - [Park et al. 2025](papers/park-2025-cardiotoxicity.md) — Healthy vs. LQTS (KCNH2 c.453delC) hiPSC-CMs with 8 CiPA drugs; FPD20/FPDc20 metric; 10× LQTS sensitivity to E-4031. *Korean J Physiol Pharmacol* 29(2):257–269.

**After:**

> - [Park et al. 2025](papers/park-2025-cardiotoxicity.md) — Healthy vs. LQTS (KCNH2 c.453delC) hiPSC-CMs with 8 arrhythmogenic drugs (concentrations from Millard et al.); FPD20/FPDc20 (lowest tested concentration with >20 % change); E-4031 FPD20 0.003 µM in the LQTS line vs 0.01–0.03 µM in healthy lines (3.3- to 10-fold, no statistics); FPDc from vendor software, formula not named. *Korean J Physiol Pharmacol* 29(2):257–269.

### 29. `wiki/index.md`: Scheurer

**Why:** 'stages maturity' and 'linking it to MEA-observable quantities' went beyond the paper (two conditions; the cited paper does not study maturation).

**Before:**

> - [Scheurer et al. 2025](papers/scheurer-2025-optical-ai.md) — Video-based SVM/SHAP classifier stages iPSC-CM maturity from beating features (99.5% accuracy); not MEA, but cites an FPD–contraction-duration correlation linking it to MEA-observable quantities. TU Dresden, *Comput Struct Biotechnol J* 27:3719–3728.

**After:**

> - [Scheurer et al. 2025](papers/scheurer-2025-optical-ai.md) — Video-based SVM/SHAP classifier separating immature (day 21) from lipid-medium-matured (day 42) iPSC-CM cultures from beating features (99.5 % test accuracy; binary, with a heterogeneous less-mature B27 group); not MEA; cites Hayakawa et al. for the FPD–contraction link. TU Dresden, *Comput Struct Biotechnol J* 27:3719–3728.

### 30. `wiki/index.md`: Hayakawa: removed from its old place

**Why:** The entry was out of alphabetical order (it stood after Scheurer).

**Before:**

> - [Hayakawa et al. 2014](papers/hayakawa-2014-motion-fp.md) — Simultaneous video motion analysis and MEA field potentials in iCell monolayers; contraction–relaxation duration and FPD linearly related per drug (E-4031, verapamil, isoproterenol), non-arrhythmic conditions. *J Mol Cell Cardiol* 77:178–191. Pre-2022 background.
>

**After:**

> (removed)

### 31. `wiki/index.md`: Hayakawa: re-inserted in alphabetical order, text extended

**Why:** Placed between Guerrelli and Hwang; the entry now also mentions the FPD end-point observation that main.md uses.

**Before:**

> - [Guerrelli et al. 2024](papers/guerrelli-2024-hipscm.md) — Temporal and spatial confounders in hiPSC-CM MEA; 22.6% beating rate drift in 20 min; outer rows 8.8 bpm faster; FPD increases 257 ms over 14 days; KCNJ2 up 27.5× over 30 days. *Am J Physiol* 327:H12–H27.

**After:**

> - [Guerrelli et al. 2024](papers/guerrelli-2024-hipscm.md) — Temporal and spatial confounders in hiPSC-CM MEA; 22.6% beating rate drift in 20 min; outer rows 8.8 bpm faster; FPD increases 257 ms over 14 days; KCNJ2 up 27.5× over 30 days. *Am J Physiol* 327:H12–H27.
> - [Hayakawa et al. 2014](papers/hayakawa-2014-motion-fp.md) — Simultaneous video motion analysis and MEA field potentials in iCell monolayers; contraction–relaxation duration and FPD linearly related per drug (E-4031, verapamil, isoproterenol), non-arrhythmic conditions; notes that the two FPD end points then in use appear to match different phases of the relaxation motion. *J Mol Cell Cardiol* 77:178–191. Pre-2022 background.

### 32. `wiki/index.md`: Last updated line

**Why:** The index had not been dated since the first ingests.

**Before:**

> *Last updated: 2026-07-02*

**After:**

> *Last updated: 2026-10-24*

### 33. `wiki/index.md`: Concepts section: two new entries

**Why:** Adds the concept pages created in the same lint pass; the remaining candidates stay listed.

**Before:**

> *(other candidates: FPDcF, CiPA, hERG trafficking, 3D vs 2D cultures)*

**After:**

> - [Multimodal measurement of hiPSC-CMs](multimodal-measurement.md) — Where MEA is combined with impedance, intracellular-like electroporation signals, AFM, video, Ca²⁺ imaging or traction force (Altrocchi, Lee, Kabanov, Hayakawa, Välimäki, Vuorenpää); the sensor-fusion hypotheses themselves are only in main.md.
> - [CiPA in the reviewed papers](cipa.md) — How Blinova 2018, Park 2025/2026, Pramudito 2026, Clements 2025 and Matsuda 2025 relate to the Comprehensive in vitro Proarrhythmia Assay.
>
> *(other candidates: hERG trafficking, 3D vs 2D cultures)*

### 34. `wiki/index.md`: Methods section: two new entries

**Why:** Adds the method pages created in the same lint pass.

**Before:**

> *(none yet — candidates: FPD measurement conventions, Fridericia correction, LEAP recording, tolerance intervals)*

**After:**

> - [FPD end conventions](fpd-end-conventions.md) — The FPD start and end definitions documented on the paper pages (Mäki, Dunham, Lee, Weiser-Bitoun, Ernault, Hayakawa), side by side; basis of Table 2 in main.md.
> - [Fridericia and other rate corrections](fridericia-rate-correction.md) — Which reviewed papers correct FPD for rate, how, and which do not; equilibration drift (Guerrelli).
>
> *(other candidates: LEAP recording, tolerance intervals)*

## Group 6. new concept and method pages

### 35. `wiki/fpd-end-conventions.md`: New page: FPD end conventions

**Why:** Recurring across six paper pages and the basis of Table 2 (AGENTS: create a page when a method recurs). Built only from facts already on the verified paper pages; it states what is not listed.

**New file.** See the file itself; its contents are not repeated here.

### 36. `wiki/fridericia-rate-correction.md`: New page: Fridericia and rate correction

**Why:** Recurs in ten paper pages and is the subject of Gap 1 in main.md. Built only from facts already on the verified paper pages; pages that say nothing about rate correction are not claimed to.

**New file.** See the file itself; its contents are not repeated here.

### 37. `wiki/cipa.md`: New page: CiPA

**Why:** CiPA is mentioned on six paper pages and in main.md (Introduction, FPDc). Built only from facts on the verified pages.

**New file.** See the file itself; its contents are not repeated here.

### 38. `wiki/multimodal-measurement.md`: New page: multimodal measurement

**Why:** Six paper pages and the Outlook section of main.md rest on this theme. The page separates documented combinations from the hypotheses.

**New file.** See the file itself; its contents are not repeated here.

## Group 7. main.md: softened generalisations (synthesis items 1, 3, 9, 10, 14, 15)

### 39. `main.md`: Abstract, sentence 2 (item 1)

**Why:** 'emerged as a primary source of inter-study variability' stated an effect that no reviewed study measures; the sentence now says 'a possible source'.

**Before:**

> the methods used to analyse FP signals have emerged as a primary source of inter-study variability.

**After:**

> the methods used to analyse FP signals have become a focus of attention as a possible source of inter-study variability.

### 40. `main.md`: Motivation, first paragraph (items 1 and 15)

**Why:** Two unsourced statements are replaced. (a) 'have increasingly been used ... since 2022' (a trend, item 15) now names the uses found in the studies examined, each with its source. (b) 'have emerged as a major source of variability and a limiting factor' (item 1) is reworded to 'plausible source ... possible limit', followed by what the evidence does and does not show, including the counterpoint from Vuorenpää et al. (2023, section 6.1.1). Your '<!-- needs citation(s) -->' comment is untouched and still follows the paragraph.

**Before:**

> Since 2022, multielectrode array (MEA) recordings from human induced pluripotent stem cell–derived cardiomyocytes (hiPSC-CMs) have increasingly been used not only for basic measurements such as beating rate and field potential duration (FPD), but also for mechanistic electrophysiological phenotyping, proarrhythmia risk assessment, and longitudinal drug testing. As a consequence, **signal analysis methods—particularly the definition of fiducial points in field potential (FP) waveforms—have emerged as a major source of variability and a limiting factor for inter-study comparability**.

**After:**

> In the studies examined, multielectrode array (MEA) recordings from human induced pluripotent stem cell–derived cardiomyocytes (hiPSC-CMs) are used not only for basic measurements such as beating rate and field potential duration (FPD), but also for mechanistic electrophysiological phenotyping (Maurissen et al., 2024; Park et al., 2025; Park et al., 2026), proarrhythmia risk assessment (Blinova et al., 2018; Pramudito et al., 2026) and longitudinal drug testing (Altrocchi et al., 2023; Guerrelli et al., 2024). This makes the analysis of the recorded signals important, and **signal analysis methods—particularly the definition of fiducial points in field potential (FP) waveforms—are a plausible source of variability and a possible limit to inter-study comparability**. The studies reviewed below show that conventions differ and that FPD does not always track the action potential, but none of them measures how much variability analysis methods cause, and a review of cardiac microphysiological systems describes the parametrization of action potentials and field potentials as well established and as enabling clear comparison of results between studies (Vuorenpää et al., 2023).

### 41. `main.md`: Abstract, gap 2 (item 3)

**Why:** 'the lack of formalised criteria' read as a statement about the field; it is an absence claim that holds for the studies examined only.

**Before:**

> the lack of formalised waveform morphology classification criteria;

**After:**

> the absence, in the studies examined, of shared and validated waveform morphology classification criteria;

### 42. `main.md`: Conclusion, gap 2 (item 3)

**Why:** 'is still largely informal' (no source says so) is replaced by what the sources show. The existing acceptance criteria are now named with their citations, and 'would reduce' becomes 'might reduce ... a proposal and not a tested effect'.

**Before:**

> Second, **waveform morphology classification is still largely informal**: studies describe exclusion rules and morphology-specific handling in qualitative terms rather than through validated shared criteria. Standardised morphology assessment analogous to existing beat acceptance thresholds (amplitude, rate, beat regularity) would reduce between-study variability at the data collection stage.

**After:**

> Second, **shared, validated waveform morphology classification criteria were not identified**: in the studies examined, morphology handling is described case by case (analysis of inverted signals, exclusion of electrodes, interpretation restricted to biphasic T waves; Mäki, 2023; Ernault et al., 2024; Weiser-Bitoun et al., 2026) rather than through common criteria, whereas quantitative acceptance criteria exist for well acceptance (amplitude, rate, beat period; Blinova et al., 2018; Clements et al., 2025). Standardised morphology assessment analogous to these acceptance thresholds might reduce between-study variability at the data collection stage, which is a proposal and not a tested effect.

### 43. `main.md`: Morphology section, first paragraph (item 9)

**Why:** 'frequently observed' had no source. The sentence now says the morphologies are described (Mäki, 2023) and cites the patch-clamp evidence for nodal-like cells (Park et al., 2026).

**Before:**

> Pacemaker-like signals lacking a pronounced high peak, waveforms dominated by a single peak, and mixed or atypical morphologies are frequently observed in hiPSC-CM cultures.

**After:**

> Pacemaker-like signals lacking a pronounced high peak, waveforms dominated by a single peak, and mixed or atypical morphologies are described in hiPSC-CM cultures (Mäki, 2023), and hiPSC-CM preparations contain nodal-like cells (Park et al., 2026).

### 44. `main.md`: Morphology section, trend sentence (item 9)

**Why:** 'growing recognition', 'increasingly report' and 'a significant methodological maturation compared with earlier studies' rested on two studies and no comparison with earlier work. The text now says 'two of them' and that the comparison was not assessed.

**Before:**

> While not all post-2022 studies adopt identical rules, there is growing recognition of waveform heterogeneity: post-2022 studies increasingly report morphology-dependent analysis branches or document that T-wave morphology varies between preparations, reflecting an awareness that a single canonical FP shape cannot be assumed (Ernault et al., 2024; Weiser-Bitoun et al., 2026). This represents a significant methodological maturation compared with earlier studies that implicitly assumed a single canonical FP shape.

**After:**

> The studies examined do not adopt identical rules, but two of them show an awareness of waveform heterogeneity: they report morphology-dependent analysis branches or document that T-wave morphology varies between preparations, which indicates that a single canonical FP shape cannot be assumed (Ernault et al., 2024; Weiser-Bitoun et al., 2026). Whether this differs from earlier studies was not assessed here.

### 45. `main.md`: Model complexity, first sentence (item 10)

**Why:** 'the increasing adoption ... has further stressed' was an uncited trend with a causal claim. It is now a statement of possibility that the two cited studies and Mäki (2023) support.

**Before:**

> Since 2022, the increasing adoption of **three-dimensional (3D) cardiomyocyte models**, including spheroids and engineered cardiac tissues, has further stressed FP analysis heuristics originally developed for two-dimensional monolayers.

**After:**

> **Three-dimensional (3D) cardiomyocyte models**, including spheroids and engineered cardiac tissues, are a setting in which FP analysis heuristics originally developed for two-dimensional monolayers may not transfer directly.

### 46. `main.md`: Model complexity, 'Consequently' sentence (item 10)

**Why:** 'more recent studies explicitly report ... and increasingly acknowledge' generalised from Hwang and Maurissen. It now says what those two do and that the wider trend was not assessed.

**Before:**

> Consequently, more recent cardiomyocyte MEA studies explicitly report model format (2D vs. 3D) and increasingly acknowledge the need for model-aware quality control and interpretation.

**After:**

> The two studies discussed here state the model format explicitly; whether model-aware quality control and interpretation are becoming general practice was not assessed.

### 47. `main.md`: High-throughput section, first sentence (item 14)

**Why:** 'post-2022 studies increasingly emphasize' was a trend nobody measured; it is now 'several of the studies examined address'.

**Before:**

> Finally, post-2022 cardiomyocyte MEA studies increasingly emphasize **high-throughput and longitudinal applications**, particularly in cardiotoxicity and proarrhythmia screening.

**After:**

> Finally, several of the post-2022 studies examined address **high-throughput and longitudinal applications**, particularly in cardiotoxicity and proarrhythmia screening.

### 48. `main.md`: High-throughput section, 'As a result' sentence (item 14)

**Why:** 'reliance on a single metric ... has progressively given way' claimed a historical shift. Matsuda et al. report no FPD at all, so 'FPD gave way' was also inexact; the sentence now says single conventional metrics are complemented by multi-parameter sets in the two cited studies.

**Before:**

> As a result, reliance on a single metric such as FPD has progressively given way to multi-parameter feature sets encompassing beat rate, beat-to-beat variability, conduction properties, and event-based descriptors (Altrocchi et al., 2023; Matsuda et al., 2025). This shift further amplifies the importance of clearly defined analysis methods,

**After:**

> In the studies examined, single conventional metrics are complemented by multi-parameter feature sets encompassing beat rate, beat-to-beat variability, conduction properties, and event-based descriptors (Altrocchi et al., 2023; Matsuda et al., 2025). This further increases the importance of clearly defined analysis methods,

### 49. `main.md`: Conclusion, 'Looking forward' sentence (item 15)

**Why:** 'rapidly becoming an integral layer' was an uncited trend, and 'AI-driven interpretation of spatially rich UHD-MEA data' had no source (Matsuda et al. use PCA and MANOVA, not machine learning). The sentence now names the three machine-learning uses found in the reviewed studies and states the rest as a possibility.

**Before:**

> Looking forward, machine learning is rapidly becoming an integral layer in cardiomyocyte MEA workflows — from ensemble classifiers for TdP risk prediction to AI-driven interpretation of spatially rich UHD-MEA data.

**After:**

> Looking forward, machine learning is used in several of the studies examined — from ensemble classifiers for TdP risk prediction (Pramudito et al., 2026) and genotype-specific risk models (Park et al., 2026) to automated feature ranking in an open platform (Lee et al., 2024) — and it may become a more integral layer of cardiomyocyte MEA workflows.

## Group 8. docs/claims-by-source.md: claims and synthesis items brought in line with the softened text

### 50. `docs/claims-by-source.md`: Claims paragraph of Altrocchi et al. (2023)

**Why:** New citations in the softened main.md sections (Motivation, Morphology, Conclusion) must appear in the source's claim list so that the coverage check shows no gaps.

**Before:**

> Claims: (1) [FPDc] the study reports rate-corrected FPD with the Fridericia formula (listed among the studies that use it). (2) [High-throughput] it used 48-well MEA plates to evaluate acute (<2 h) and delayed (≥24 h) electrophysiological and cytotoxic effects of reference compounds, including tyrosine-kinase inhibitors, an anthracycline (doxorubicin) and ion-channel trafficking inhibitors, over 4 days, combining field potential recordings with impedance readouts. (3) [High-throughput] chronic and longitudinal MEA assays "have been validated for both acute and delayed cardiotoxicity" (this study is the example). (4) [High-throughput] it is one of the two examples (with Matsuda et al., 2025) of multi-parameter feature sets encompassing beat rate, beat-to-beat variability, conduction properties and event-based descriptors. (5) [Intro] cited, with Blinova et al. (2018) and Park et al. (2025), for MEA recordings of hiPSC-CMs being widely used in cardiac safety pharmacology, drug discovery and disease modelling. (6) [Outlook] impedance is read alongside FP, as an example of a second measurement added to the MEA recording.

**After:**

> Claims: (1) [FPDc] the study reports rate-corrected FPD with the Fridericia formula (listed among the studies that use it). (2) [High-throughput] it used 48-well MEA plates to evaluate acute (<2 h) and delayed (≥24 h) electrophysiological and cytotoxic effects of reference compounds, including tyrosine-kinase inhibitors, an anthracycline (doxorubicin) and ion-channel trafficking inhibitors, over 4 days, combining field potential recordings with impedance readouts. (3) [High-throughput] chronic and longitudinal MEA assays "have been validated for both acute and delayed cardiotoxicity" (this study is the example). (4) [High-throughput] it is one of the two examples (with Matsuda et al., 2025) of multi-parameter feature sets encompassing beat rate, beat-to-beat variability, conduction properties and event-based descriptors. (5) [Intro] cited, with Blinova et al. (2018) and Park et al. (2025), for MEA recordings of hiPSC-CMs being widely used in cardiac safety pharmacology, drug discovery and disease modelling. (6) [Outlook] impedance is read alongside FP, as an example of a second measurement added to the MEA recording. (7) [Motivation] example of longitudinal drug testing.

### 51. `docs/claims-by-source.md`: Claims paragraph of Blinova et al. (2018)

**Why:** New citations in the softened main.md sections (Motivation, Morphology, Conclusion) must appear in the source's claim list so that the coverage check shows no gaps.

**Before:**

> Claims: (1) [Intro] cited, with Altrocchi et al. (2023) and Park et al. (2025), for MEA recordings of hiPSC-CMs being widely used in cardiac safety pharmacology, drug discovery and disease modelling, and, with Park et al. (2025), for FPD and related metrics being integral to the CiPA initiative. (2) [FPDc] it was a "blinded multisite CiPA study" that applied Fridericia correction to all 28 reference drugs across ten sites. (3) [FPDc] it states that the Fridericia formula was not thoroughly validated for hiPSC-CMs, and this is described as a recognised methodological gap. (4) [FPDc] spontaneous rates of hiPSC-CMs are "accepted at 20–90 BPM" in this study (inclusion criterion for baseline beating rate). (5) [Limitations] it is cited only as pre-2022 background for conventions and datasets that later studies build on, not as one of the post-2022 developments reviewed. Pointers: Fridericia statement in the Data Analysis section of the Experimental Procedures; the 20–90 bpm criterion in the same section; ten sites and 28 drugs in the Summary.

**After:**

> Claims: (1) [Intro] cited, with Altrocchi et al. (2023) and Park et al. (2025), for MEA recordings of hiPSC-CMs being widely used in cardiac safety pharmacology, drug discovery and disease modelling, and, with Park et al. (2025), for FPD and related metrics being integral to the CiPA initiative. (2) [FPDc] it was a "blinded multisite CiPA study" that applied Fridericia correction to all 28 reference drugs across ten sites. (3) [FPDc] it states that the Fridericia formula was not thoroughly validated for hiPSC-CMs, and this is described as a recognised methodological gap. (4) [FPDc] spontaneous rates of hiPSC-CMs are "accepted at 20–90 BPM" in this study (inclusion criterion for baseline beating rate). (5) [Limitations] it is cited only as pre-2022 background for conventions and datasets that later studies build on, not as one of the post-2022 developments reviewed. Pointers: Fridericia statement in the Data Analysis section of the Experimental Procedures; the 20–90 bpm criterion in the same section; ten sites and 28 drugs in the Summary. (6) [Motivation] example of proarrhythmia risk assessment. (7) [Conclusion] quantitative acceptance criteria exist for well acceptance (amplitude, rate, beat period).

### 52. `docs/claims-by-source.md`: Claims paragraph of Clements et al. (2025)

**Why:** New citations in the softened main.md sections (Motivation, Morphology, Conclusion) must appear in the source's claim list so that the coverage check shows no gaps.

**Before:**

> Claims: (1) [FPDc] a recent proposed acceptance standard for hiPSC-ventricular-CM MEA assays builds the Fridericia correction into quality control by requiring an FPDc of 200–700 ms. (2) [FPDc] spontaneous rates are accepted at 20–80 BPM in that proposal. (3) [Maturation] it is an industry-led proposal (Axion BioSystems' "AIMS \#CM01", presented as a poster at ISSCR 2025) defining minimum well-acceptance criteria for spontaneous-beating hiPSC-ventricular-CM MEA assays: spike amplitude ≥ 0.5 mV and synchronized beating on at least half of the electrodes, a spontaneous beat period of 750–3000 ms, and FPDc of 200–700 ms. (4) it targets assay quality control, not maturation staging. (5) it has been presented as a conference poster and vendor document rather than a peer-reviewed methods paper. Pointers: the "AIMS \#CM01: Proposed standards" box; "Presented at ISSCR 2025, Hong Kong, June 11, 2025". The standard document on the vendor's website (last revised 2 December 2024) was read only through a web-fetch summary.

**After:**

> Claims: (1) [FPDc] a recent proposed acceptance standard for hiPSC-ventricular-CM MEA assays builds the Fridericia correction into quality control by requiring an FPDc of 200–700 ms. (2) [FPDc] spontaneous rates are accepted at 20–80 BPM in that proposal. (3) [Maturation] it is an industry-led proposal (Axion BioSystems' "AIMS \#CM01", presented as a poster at ISSCR 2025) defining minimum well-acceptance criteria for spontaneous-beating hiPSC-ventricular-CM MEA assays: spike amplitude ≥ 0.5 mV and synchronized beating on at least half of the electrodes, a spontaneous beat period of 750–3000 ms, and FPDc of 200–700 ms. (4) it targets assay quality control, not maturation staging. (5) it has been presented as a conference poster and vendor document rather than a peer-reviewed methods paper. Pointers: the "AIMS \#CM01: Proposed standards" box; "Presented at ISSCR 2025, Hong Kong, June 11, 2025". The standard document on the vendor's website (last revised 2 December 2024) was read only through a web-fetch summary. (4) [Conclusion] quantitative acceptance criteria exist for well acceptance (amplitude, synchrony, beat period, FPDc).

### 53. `docs/claims-by-source.md`: Claims paragraph of Ernault et al. (2024)

**Why:** New citations in the softened main.md sections (Motivation, Morphology, Conclusion) must appear in the source's claim list so that the coverage check shows no gaps.

**Before:**

> Claims: (1) [Timeline, Table 2, Figure 2] T-wave peak equals APD90 for biphasic T waves, in NRVM. (2) [Fiducial] using simultaneous MEA and sharp-microelectrode recordings from neonatal rat ventricular myocyte (NRVM) monolayers, the peak time of the T wave in FPs correlates strongly with APD90, but only when the T wave displays a biphasic pattern. (3) the authors report that morphology in only a minority of recorded monolayers. (4) [Fiducial, our inference] the T-wave peak, when biphasic, is better anchored to APD90 than a baseline-return convention, which extends into the repolarization tail; the two definitions measure different quantities. (5) [Morphology] together with Weiser-Bitoun et al., it is cited for post-2022 studies increasingly reporting morphology-dependent analysis branches or document that T-wave morphology varies between preparations. (6) [Limitations] example of evidence in rat cells. (7) [Outlook] the T-wave peak tracks APD90 only for biphasic T waves; the LEAP depends on current from neighbouring cells, so removing the device contribution alone would not suffice (the second half is our inference).

**After:**

> Claims: (1) [Timeline, Table 2, Figure 2] T-wave peak equals APD90 for biphasic T waves, in NRVM. (2) [Fiducial] using simultaneous MEA and sharp-microelectrode recordings from neonatal rat ventricular myocyte (NRVM) monolayers, the peak time of the T wave in FPs correlates strongly with APD90, but only when the T wave displays a biphasic pattern. (3) the authors report that morphology in only a minority of recorded monolayers. (4) [Fiducial, our inference] the T-wave peak, when biphasic, is better anchored to APD90 than a baseline-return convention, which extends into the repolarization tail; the two definitions measure different quantities. (5) [Morphology] together with Weiser-Bitoun et al., it is cited for post-2022 studies increasingly reporting morphology-dependent analysis branches or document that T-wave morphology varies between preparations. (6) [Limitations] example of evidence in rat cells. (7) [Outlook] the T-wave peak tracks APD90 only for biphasic T waves; the LEAP depends on current from neighbouring cells, so removing the device contribution alone would not suffice (the second half is our inference). (8) [Conclusion] interpretation restricted to biphasic T waves is an example of case-by-case morphology handling.

### 54. `docs/claims-by-source.md`: Claims paragraph of Guerrelli et al. (2024)

**Why:** New citations in the softened main.md sections (Motivation, Morphology, Conclusion) must appear in the source's claim list so that the coverage check shows no gaps.

**Before:**

> Claims: (1) [Timeline] temporal and spatial confounders quantified. (2) [FPDc] one study reported that the beating rate increases by more than 22 % and FPD decreases by about 8 % during a 20-minute recording equilibration period. (3) [High-throughput] the same numbers more precisely: beating rate +22.6 % and FPD −7.7 % over a 20-minute equilibration window. (4) [High-throughput] from 2 to 14 days in culture the beating rate decreases while FPD lengthens substantially. (5) [Maturation] FPD lengthens by about 257 ms and beating rate declines over days 2–14 in culture. (6) [Maturation] KCNJ2 (I_K1-encoding) gene expression rises 27.5-fold over 30 days. (7) [Maturation, our interpretation] this drift is consistent with ongoing maturation and rate correction alone does not address it. (8) [High-throughput] the findings highlight the need to standardise recording time points and culture age.

**After:**

> Claims: (1) [Timeline] temporal and spatial confounders quantified. (2) [FPDc] one study reported that the beating rate increases by more than 22 % and FPD decreases by about 8 % during a 20-minute recording equilibration period. (3) [High-throughput] the same numbers more precisely: beating rate +22.6 % and FPD −7.7 % over a 20-minute equilibration window. (4) [High-throughput] from 2 to 14 days in culture the beating rate decreases while FPD lengthens substantially. (5) [Maturation] FPD lengthens by about 257 ms and beating rate declines over days 2–14 in culture. (6) [Maturation] KCNJ2 (I_K1-encoding) gene expression rises 27.5-fold over 30 days. (7) [Maturation, our interpretation] this drift is consistent with ongoing maturation and rate correction alone does not address it. (8) [High-throughput] the findings highlight the need to standardise recording time points and culture age. (9) [Motivation] example of longitudinal drug testing (culture-time effects).

### 55. `docs/claims-by-source.md`: Claims paragraph of Lee et al. (2024)

**Why:** New citations in the softened main.md sections (Motivation, Morphology, Conclusion) must appear in the source's claim list so that the coverage check shows no gaps.

**Before:**

> Claims: (1) [Timeline] CardioMEA platform, scalable open analysis. (2) [Open pipelines, Table 1] it was built for high-density MEA data, processes files in parallel into an SQL database, has a web-based dashboard, extracts features from extracellular and intracellular-like (electroporation-derived) signals, and has an automated machine-learning module ranking features that separate diseased from control lines; Python. (3) [Open pipelines] open tools such as MultiElec and CardioMDA already existed before 2022 (Table 3 of the paper lists them). (4) [Fiducial, Table 1, Table 2] FPD is measured from the R spike to the T-wave peak. (5) [Fiducial] in iCell cardiomyocyte HD-MEA recordings, R-to-T-peak FPD correlated only minimally with APD50 and APD90 measured from intracellular-like signals on the same electrodes, which the authors attribute to small, noisy T waves. (6) [FPDc, Table 1] the published feature set contains FPD but no rate-corrected FPD. Pointers: Table 1 (features), Figure 4 (correlations), Table 3 (platform comparison). (7) [Outlook] intracellular-like signals are obtained through the same electrodes by electroporation; R-to-T-peak FPD correlated only minimally with APD50 and APD90 from those signals; electroporation gives paired FP and AP-like signals from the same electrodes (the use as training and validation data is our proposal).

**After:**

> Claims: (1) [Timeline] CardioMEA platform, scalable open analysis. (2) [Open pipelines, Table 1] it was built for high-density MEA data, processes files in parallel into an SQL database, has a web-based dashboard, extracts features from extracellular and intracellular-like (electroporation-derived) signals, and has an automated machine-learning module ranking features that separate diseased from control lines; Python. (3) [Open pipelines] open tools such as MultiElec and CardioMDA already existed before 2022 (Table 3 of the paper lists them). (4) [Fiducial, Table 1, Table 2] FPD is measured from the R spike to the T-wave peak. (5) [Fiducial] in iCell cardiomyocyte HD-MEA recordings, R-to-T-peak FPD correlated only minimally with APD50 and APD90 measured from intracellular-like signals on the same electrodes, which the authors attribute to small, noisy T waves. (6) [FPDc, Table 1] the published feature set contains FPD but no rate-corrected FPD. Pointers: Table 1 (features), Figure 4 (correlations), Table 3 (platform comparison). (7) [Outlook] intracellular-like signals are obtained through the same electrodes by electroporation; R-to-T-peak FPD correlated only minimally with APD50 and APD90 from those signals; electroporation gives paired FP and AP-like signals from the same electrodes (the use as training and validation data is our proposal). (8) [Conclusion] automated feature ranking in an open platform is one of the machine-learning uses in the studies examined.

### 56. `docs/claims-by-source.md`: Claims paragraph of Mäki (2023, version v3)

**Why:** New citations in the softened main.md sections (Motivation, Morphology, Conclusion) must appear in the source's claim list so that the coverage check shows no gaps.

**Before:**

> Claims: (1) [Abstract, Motivation, Scope, Timeline] it is used as the evaluative framework; the Figure 1 timeline lists "DatAnalyzer / Mäki opinion paper — morphology-aware FPD" under 2023. (2) [Motivation] it challenged the physiological validity of commonly used FP annotation conventions, arguing that the widely adopted peak-to-peak FPD definition is often mismatched to the underlying electrophysiology. (3) it argues that the first positive FP peak in a propagating hiPSC-CM monolayer may reflect depolarization of neighbouring cells rather than the locally recorded cardiomyocyte. (4) it argues that FPD end should be measured to the return of the signal to baseline rather than the repolarization peak. (5) [Fiducial] it describes an algorithm: beat-aligned segmentation, averaging across beats to reduce noise, threshold-based identification of depolarization onset relative to FP amplitude, FPD end as return of the signal toward baseline. (6) [Morphology] morphology-aware handling of pacemaker-like signals and waveform inversion for "only high peak" cases, internally validated in that work but not independently replicated. (7) [Model complexity] its caution that analysis frameworks optimised for 2D cultures may not be directly transferable to 3D systems (its Limitations section says the analysis "might not be as easily … extrapolated to the 3D model"). (8) [Table 1, Table 2, Figure 2] DatAnalyzer (Python): FPD from depolarization onset to baseline return; the merged peak-to-peak row of Table 2 also characterises that convention as common and criticised in this paper; Figure 2 and the Morphology paragraph also cite it for the baseline-return end. (9) [Declarations, References] the first version was posted on Zenodo in 2023; the text assessed is v3, published 23 June 2026 (the version list of the record zenodo.org/records/20807245 reads "Version v3, 10.5281/zenodo.20807245, Jun 23, 2026"; the "Updated 2025-08-07" date on the record page is a separate metadata field and not the publication date). The reference entry keeps the year 2023 of the original version and states "(Version v3, published 23 June 2026)"; the Declarations version note says the same. (10) [Limitations] it is the author's own, non-peer-reviewed opinion paper; its inversion approach is not independently replicated; its FPD-end convention is one of several. (11) [Declarations] competing-interest statement: the author wrote this paper and the DatAnalyzer tool. (12) [Outlook] the author's view that machine learning applied directly to raw MEA signals is unlikely to work, the two-step approach (extract parameters from detected peaks, then machine learning), and the idea of estimating the AP from the FP by modelling the recording system, ideally with electroporation through the MEA electrodes.

**After:**

> Claims: (1) [Abstract, Motivation, Scope, Timeline] it is used as the evaluative framework; the Figure 1 timeline lists "DatAnalyzer / Mäki opinion paper — morphology-aware FPD" under 2023. (2) [Motivation] it challenged the physiological validity of commonly used FP annotation conventions, arguing that the widely adopted peak-to-peak FPD definition is often mismatched to the underlying electrophysiology. (3) it argues that the first positive FP peak in a propagating hiPSC-CM monolayer may reflect depolarization of neighbouring cells rather than the locally recorded cardiomyocyte. (4) it argues that FPD end should be measured to the return of the signal to baseline rather than the repolarization peak. (5) [Fiducial] it describes an algorithm: beat-aligned segmentation, averaging across beats to reduce noise, threshold-based identification of depolarization onset relative to FP amplitude, FPD end as return of the signal toward baseline. (6) [Morphology] morphology-aware handling of pacemaker-like signals and waveform inversion for "only high peak" cases, internally validated in that work but not independently replicated. (7) [Model complexity] its caution that analysis frameworks optimised for 2D cultures may not be directly transferable to 3D systems (its Limitations section says the analysis "might not be as easily … extrapolated to the 3D model"). (8) [Table 1, Table 2, Figure 2] DatAnalyzer (Python): FPD from depolarization onset to baseline return; the merged peak-to-peak row of Table 2 also characterises that convention as common and criticised in this paper; Figure 2 and the Morphology paragraph also cite it for the baseline-return end. (9) [Declarations, References] the first version was posted on Zenodo in 2023; the text assessed is v3, published 23 June 2026 (the version list of the record zenodo.org/records/20807245 reads "Version v3, 10.5281/zenodo.20807245, Jun 23, 2026"; the "Updated 2025-08-07" date on the record page is a separate metadata field and not the publication date). The reference entry keeps the year 2023 of the original version and states "(Version v3, published 23 June 2026)"; the Declarations version note says the same. (10) [Limitations] it is the author's own, non-peer-reviewed opinion paper; its inversion approach is not independently replicated; its FPD-end convention is one of several. (11) [Declarations] competing-interest statement: the author wrote this paper and the DatAnalyzer tool. (12) [Outlook] the author's view that machine learning applied directly to raw MEA signals is unlikely to work, the two-step approach (extract parameters from detected peaks, then machine learning), and the idea of estimating the AP from the FP by modelling the recording system, ideally with electroporation through the MEA electrodes. (13) [Conclusion] analysis of inverted signals (waveform inversion) is an example of case-by-case morphology handling.

### 57. `docs/claims-by-source.md`: Claims paragraph of Maurissen et al. (2024)

**Why:** New citations in the softened main.md sections (Motivation, Morphology, Conclusion) must appear in the source's claim list so that the coverage check shows no gaps.

**Before:**

> Claims: (1) [Timeline] KCNH2 mutation phenotyping in 3D tissues. (2) [FPDc] the study uses Fridericia-corrected FPD (FPDcF). (3) [Model complexity] it combined gene-edited KCNH2 variants (N588D, N588K) with hiPSC-derived cardiac tissue sheets and MEA analysis to recapitulate long QT and short QT phenotypes, with differential repolarization and susceptibility to pharmacologically induced arrhythmias, in 3D isogenic tissues.

**After:**

> Claims: (1) [Timeline] KCNH2 mutation phenotyping in 3D tissues. (2) [FPDc] the study uses Fridericia-corrected FPD (FPDcF). (3) [Model complexity] it combined gene-edited KCNH2 variants (N588D, N588K) with hiPSC-derived cardiac tissue sheets and MEA analysis to recapitulate long QT and short QT phenotypes, with differential repolarization and susceptibility to pharmacologically induced arrhythmias, in 3D isogenic tissues. (4) [Motivation] example of mechanistic electrophysiological phenotyping.

### 58. `docs/claims-by-source.md`: Claims paragraph of Park et al. (2025)

**Why:** New citations in the softened main.md sections (Motivation, Morphology, Conclusion) must appear in the source's claim list so that the coverage check shows no gaps.

**Before:**

> Claims: (1) [Timeline] healthy vs LQTS hiPSC-CM CiPA drug comparison (2025). (2) [Intro] cited, with Blinova et al. and Altrocchi et al., for MEA use in cardiac safety pharmacology, drug discovery and disease modelling, and, with Blinova et al., for FPD metrics being integral to CiPA. (3) [FPDc] it reports corrected FPD (FPDc) from the vendor software but does not name the formula. (4) [Open pipelines] the vendor's Cardiac Analysis Tool was used for the analysis. (5) [High-throughput] it compared eight arrhythmia-inducing drugs (for example E4031, moxifloxacin, quinidine) across healthy and long QT syndrome–derived hiPSC-CM lines via MEA, demonstrating dose-dependent FPD and arrhythmogenic risk and disease-specific sensitivity to hERG blockade. (6) [High-throughput] it shares group, platform and apparently an LQT line with Park et al. (2026), so the two are one body of evidence.

**After:**

> Claims: (1) [Timeline] healthy vs LQTS hiPSC-CM CiPA drug comparison (2025). (2) [Intro] cited, with Blinova et al. and Altrocchi et al., for MEA use in cardiac safety pharmacology, drug discovery and disease modelling, and, with Blinova et al., for FPD metrics being integral to CiPA. (3) [FPDc] it reports corrected FPD (FPDc) from the vendor software but does not name the formula. (4) [Open pipelines] the vendor's Cardiac Analysis Tool was used for the analysis. (5) [High-throughput] it compared eight arrhythmia-inducing drugs (for example E4031, moxifloxacin, quinidine) across healthy and long QT syndrome–derived hiPSC-CM lines via MEA, demonstrating dose-dependent FPD and arrhythmogenic risk and disease-specific sensitivity to hERG blockade. (6) [High-throughput] it shares group, platform and apparently an LQT line with Park et al. (2026), so the two are one body of evidence. (7) [Motivation] example of mechanistic electrophysiological phenotyping.

### 59. `docs/claims-by-source.md`: Claims paragraph of Park et al. (2026)

**Why:** New citations in the softened main.md sections (Motivation, Morphology, Conclusion) must appear in the source's claim list so that the coverage check shows no gaps.

**Before:**

> Claims: (1) [FPDc] the study uses Fridericia-corrected FPDc and other MEA parameters. (2) [FPDc] it trained neural-network, random-forest and gradient-boosting classifiers on these features from long QT and Brugada syndrome lines, took the rate correction as given, and did not test how the choice of correction affects performance. (3) [FPDc] it evaluated on a small test set of 15 drugs by repeated resampling. (4) [Open pipelines] the vendor's Cardiac Analysis Tool was used. (5) [High-throughput] the same group applied a similar MEA workflow to patient-derived LQTS and BrS lines and 28 compounds, reporting disease-specific drug sensitivities. (6) [High-throughput] the two Brugada lines consisted largely of atrial-like cells (100 % and 87.5 % atrial-like in Figure 3), so their comparison with ventricular-like normal lines is confounded by cell identity. (7) [High-throughput] overlap with Park et al. (2025): same group and platform, apparently the same long QT line (KCNH2 c.453delC). (8) [Maturation] patch-clamp data show ventricular-, atrial- and nodal-like cells in the normal lines (about 70 %, 20 % and 9 %). (9) The reference year is 2026 (volume 82; online July 2025). (9) [Outlook] the machine-learning classifiers were trained on small datasets.

**After:**

> Claims: (1) [FPDc] the study uses Fridericia-corrected FPDc and other MEA parameters. (2) [FPDc] it trained neural-network, random-forest and gradient-boosting classifiers on these features from long QT and Brugada syndrome lines, took the rate correction as given, and did not test how the choice of correction affects performance. (3) [FPDc] it evaluated on a small test set of 15 drugs by repeated resampling. (4) [Open pipelines] the vendor's Cardiac Analysis Tool was used. (5) [High-throughput] the same group applied a similar MEA workflow to patient-derived LQTS and BrS lines and 28 compounds, reporting disease-specific drug sensitivities. (6) [High-throughput] the two Brugada lines consisted largely of atrial-like cells (100 % and 87.5 % atrial-like in Figure 3), so their comparison with ventricular-like normal lines is confounded by cell identity. (7) [High-throughput] overlap with Park et al. (2025): same group and platform, apparently the same long QT line (KCNH2 c.453delC). (8) [Maturation] patch-clamp data show ventricular-, atrial- and nodal-like cells in the normal lines (about 70 %, 20 % and 9 %). (9) The reference year is 2026 (volume 82; online July 2025). (9) [Outlook] the machine-learning classifiers were trained on small datasets. (10) [Motivation] example of mechanistic electrophysiological phenotyping. (11) [Morphology] hiPSC-CM preparations contain nodal-like cells (patch-clamp data). (12) [Conclusion] genotype-specific risk models are one of the machine-learning uses in the studies examined.

### 60. `docs/claims-by-source.md`: Claims paragraph of Pramudito et al. (2026)

**Why:** New citations in the softened main.md sections (Motivation, Morphology, Conclusion) must appear in the source's claim list so that the coverage check shows no gaps.

**Before:**

> Claims: (1) [Timeline, Conclusion] stacking ensemble ML for TdP risk prediction; the Conclusion mentions "ensemble classifiers for TdP risk prediction" without naming the paper. (2) [FPDc] ΔFPDc has become a primary input feature for machine-learning proarrhythmic risk classifiers. (3) [FPDc] a stacking ensemble of random forest, gradient boosting and neural network classifiers outperformed each of its single constituent classifiers in predicting TdP risk on 16 held-out CiPA reference compounds. (4) [FPDc] it used ΔFPDc values already corrected in the multisite CiPA dataset, took the correction as given, and did not test the effect of the correction. (5) [FPDc] it evaluated on a small test set (16 drugs) by repeated resampling. Pointers: Tables 3 and 4 for the comparison; Datasets and Methods sections for the pre-corrected ΔFPDc. (6) [Outlook] the machine-learning classifiers were trained on small datasets (test set of 16 drugs).

**After:**

> Claims: (1) [Timeline, Conclusion] stacking ensemble ML for TdP risk prediction; the Conclusion mentions "ensemble classifiers for TdP risk prediction" without naming the paper. (2) [FPDc] ΔFPDc has become a primary input feature for machine-learning proarrhythmic risk classifiers. (3) [FPDc] a stacking ensemble of random forest, gradient boosting and neural network classifiers outperformed each of its single constituent classifiers in predicting TdP risk on 16 held-out CiPA reference compounds. (4) [FPDc] it used ΔFPDc values already corrected in the multisite CiPA dataset, took the correction as given, and did not test the effect of the correction. (5) [FPDc] it evaluated on a small test set (16 drugs) by repeated resampling. Pointers: Tables 3 and 4 for the comparison; Datasets and Methods sections for the pre-corrected ΔFPDc. (6) [Outlook] the machine-learning classifiers were trained on small datasets (test set of 16 drugs). (7) [Motivation] example of proarrhythmia risk assessment.

### 61. `docs/claims-by-source.md`: Claims paragraph of Weiser-Bitoun et al. (2026)

**Why:** New citations in the softened main.md sections (Motivation, Morphology, Conclusion) must appear in the source's claim list so that the coverage check shows no gaps.

**Before:**

> Claims: (1) [Timeline] PhysioMEA, cardiac organoid BRV and 2D heatmaps (2026). (2) [Open pipelines] a platform for cardiac organoids whose software, source code and documentation are freely available (written in MATLAB and also distributed as a standalone executable), providing one-dimensional biomarkers (FPD, spike amplitude, peak-to-peak duration, inter-beat interval) across all recording electrodes, two-dimensional spatiotemporal heatmaps quantifying electrode-to-electrode variability in signal propagation, and beat rate variability (BRV) analysis with 45 standardised measures adapted from heart rate variability frameworks. (3) [Fiducial, Table 1, Table 2, Morphology] FPD is defined as the interval from the R peak to the T-wave peak, not the return to baseline. (4) [Morphology] with Ernault et al., cited for post-2022 studies increasingly reporting morphology-dependent analysis branches or document that T-wave morphology varies between preparations.

**After:**

> Claims: (1) [Timeline] PhysioMEA, cardiac organoid BRV and 2D heatmaps (2026). (2) [Open pipelines] a platform for cardiac organoids whose software, source code and documentation are freely available (written in MATLAB and also distributed as a standalone executable), providing one-dimensional biomarkers (FPD, spike amplitude, peak-to-peak duration, inter-beat interval) across all recording electrodes, two-dimensional spatiotemporal heatmaps quantifying electrode-to-electrode variability in signal propagation, and beat rate variability (BRV) analysis with 45 standardised measures adapted from heart rate variability frameworks. (3) [Fiducial, Table 1, Table 2, Morphology] FPD is defined as the interval from the R peak to the T-wave peak, not the return to baseline. (4) [Morphology] with Ernault et al., cited for post-2022 studies increasingly reporting morphology-dependent analysis branches or document that T-wave morphology varies between preparations. (5) [Conclusion] analysis of inverted signals and exclusion of electrodes are examples of case-by-case morphology handling.

### 62. `docs/claims-by-source.md`: Claims paragraph of Vuorenpää et al. (2023)

**Why:** New citations in the softened main.md sections (Motivation, Morphology, Conclusion) must appear in the source's claim list so that the coverage check shows no gaps.

**Before:**

> Claims: (1) [Outlook] a review of cardiac microphysiological systems sees potential in combining different measurement modalities, which heart-on-chip systems can monitor concurrently. (2) [Outlook] it notes that continuous, multimodal measurements give a holistic data set for parameterising and validating computational models and that, to its authors' knowledge, integrative simulations of all building blocks of a microphysiological system had not been published. (3) [Declarations] two of its authors are co-authors of Välimäki et al. (2021).

**After:**

> Claims: (1) [Outlook] a review of cardiac microphysiological systems sees potential in combining different measurement modalities, which heart-on-chip systems can monitor concurrently. (2) [Outlook] it notes that continuous, multimodal measurements give a holistic data set for parameterising and validating computational models and that, to its authors' knowledge, integrative simulations of all building blocks of a microphysiological system had not been published. (3) [Declarations] two of its authors are co-authors of Välimäki et al. (2021). (4) [Motivation] the review describes the parametrization of action potentials and field potentials as well established and as enabling clear comparison of results between studies (section 6.1.1; a counterpoint to the 'source of variability' statement).

### 63. `docs/claims-by-source.md`: Synthesis item 1

**Why:** The quoted wording and the support rating follow the revised main.md text.

**Before:**

> 1. [Abstract, Motivation] "the methods used to analyse FP signals have emerged as a primary source of inter-study variability" and, in bold, "signal analysis methods—particularly the definition of fiducial points in field potential (FP) waveforms—have emerged as a major source of variability and a limiting factor for inter-study comparability" (you marked this with "needs citation(s)"). Based on: Mäki (2023) as the argument; Lee et al. (2024), whose FPD correlated minimally with APD because of small T waves; Ernault et al. (2024); the spread of conventions in Table 2. No reviewed study measures how much analysis methods contribute to inter-study variability, and Blinova et al. (2018) found site variability smaller than cell-line and concentration effects (without testing analysis methods). Counter-evidence: Vuorenpää et al. (2023, section 6.1.1) state that "the parametrization of APs and field potentials has been well established, enabling clear comparison of results between studies" (citing Kussauer et al., 2019), without discussing fiducial conventions. Support: none for "major/primary source" as stated; consider softening or citing.

**After:**

> 1. [Abstract, Motivation] "the methods used to analyse FP signals have become a focus of attention as a possible source of inter-study variability" and, in bold, "signal analysis methods—particularly the definition of fiducial points in field potential (FP) waveforms—are a plausible source of variability and a possible limit to inter-study comparability", followed by "none of them measures how much variability analysis methods cause" and the counterpoint that a review of cardiac microphysiological systems describes the parametrization of action potentials and field potentials as well established (Vuorenpää et al., 2023). Revised 2026-10-24; your "needs citation(s)" comment is still in `main.md`. Based on: Mäki (2023) as the argument; Lee et al. (2024), Ernault et al. (2024) and Hayakawa et al. (2014) for FPD not tracking APD or the end points appearing to match different phases; Table 2 for the spread of conventions; Vuorenpää et al. (2023, section 6.1.1) and Blinova et al. (2018) (site variability smaller than cell-line and concentration effects, without testing analysis methods) as counter-evidence. Support: the revised wording claims only plausibility and says that no reviewed study measures the effect; supported as written (inference).

### 64. `docs/claims-by-source.md`: Synthesis item 3

**Why:** Quotes and rating follow the revised Abstract and Conclusion; the earlier note 'No source says that morphology handling is informal' is no longer needed because the claim was dropped.

**Before:**

> 3. [Abstract, Conclusion] Gap 2: "waveform morphology classification is still largely informal: studies describe exclusion rules and morphology-specific handling in qualitative terms rather than through validated shared criteria. Standardised morphology assessment analogous to existing beat acceptance thresholds (amplitude, rate, beat regularity) would reduce between-study variability at the data collection stage." Based on: Mäki (2023) (three morphologies, own method), Ernault et al. (2024) (biphasic T waves a minority), Weiser-Bitoun et al. (2026) (inverted T peaks), Lee et al. (2024) (small T waves). Quantitative acceptance criteria do exist (Blinova et al., 2018; Clements et al., 2025: amplitude, synchrony, beat period, FPDc) but they concern well acceptance, not waveform classification, and the Conclusion does not cite them. No source says that morphology handling is "informal". Support: thin; the statement is an inference from a small set of papers.

**After:**

> 3. [Abstract, Conclusion] Gap 2 (revised 2026-10-24): "the absence, in the studies examined, of shared and validated waveform morphology classification criteria" and "shared, validated waveform morphology classification criteria were not identified: in the studies examined, morphology handling is described case by case (analysis of inverted signals, exclusion of electrodes, interpretation restricted to biphasic T waves ...) rather than through common criteria, whereas quantitative acceptance criteria exist for well acceptance ... Standardised morphology assessment analogous to these acceptance thresholds might reduce between-study variability at the data collection stage, which is a proposal and not a tested effect." Based on: Mäki (2023) (three morphologies, own method), Ernault et al. (2024) (biphasic T waves a minority), Weiser-Bitoun et al. (2026) (inverted signals, electrode exclusion), Lee et al. (2024) (small T waves), and for the acceptance criteria Blinova et al. (2018) and Clements et al. (2025). Support: thin; the first part is an absence claim limited to the studies examined, the last sentence is an untested proposal and is labelled as such.

### 65. `docs/claims-by-source.md`: Synthesis item 9

**Why:** The unsupported comparison with earlier studies and the word 'frequently' were removed, so the item is now supported as worded.

**Before:**

> 9. [Morphology] "post-2022 studies increasingly report morphology-dependent analysis branches or document that T-wave morphology varies between preparations ... (Ernault et al., 2024; Weiser-Bitoun et al., 2026). This represents a significant methodological maturation compared with earlier studies that implicitly assumed a single canonical FP shape." and "Pacemaker-like signals ... are frequently observed in hiPSC-CM cultures." Based on two studies; the comparison with "earlier studies" and the frequency statement are uncited (Ismaili et al., 2023 supports the existence of nodal-like cells only). Support: thin for the trend, none for "earlier studies" and "frequently".

**After:**

> 9. [Morphology] (revised 2026-10-24) "The studies examined do not adopt identical rules, but two of them show an awareness of waveform heterogeneity: they report morphology-dependent analysis branches or document that T-wave morphology varies between preparations ... (Ernault et al., 2024; Weiser-Bitoun et al., 2026). Whether this differs from earlier studies was not assessed here." and "Pacemaker-like signals ... are described in hiPSC-CM cultures (Mäki, 2023), and hiPSC-CM preparations contain nodal-like cells (Park et al., 2026)." Based on the two studies named (checked against their texts), Mäki (2023) and the patch-clamp data of Park et al. (2026). Support: supported as written; the comparison with earlier studies is explicitly left open.

### 66. `docs/claims-by-source.md`: Synthesis item 10

**Why:** The trend and causal wording were removed; the sentences now state a possibility and what was not assessed.

**Before:**

> 10. [Model complexity] "Since 2022, the increasing adoption of three-dimensional (3D) cardiomyocyte models ... has further stressed FP analysis heuristics originally developed for two-dimensional monolayers" and "Consequently, more recent cardiomyocyte MEA studies explicitly report model format (2D vs. 3D) and increasingly acknowledge the need for model-aware quality control and interpretation." Based on Hwang et al. (2023) and Maurissen et al. (2024) only; the adoption trend and the reporting trend are uncited. Support: thin.

**After:**

> 10. [Model complexity] (revised 2026-10-24) "Three-dimensional (3D) cardiomyocyte models ... are a setting in which FP analysis heuristics originally developed for two-dimensional monolayers may not transfer directly." and "The two studies discussed here state the model format explicitly; whether model-aware quality control and interpretation are becoming general practice was not assessed." Based on Hwang et al. (2023), Maurissen et al. (2024) and the caution in Mäki (2023). Support: the possibility is supported by those three sources (thin); the trend is explicitly not claimed.

### 67. `docs/claims-by-source.md`: Synthesis item 14

**Why:** The unmeasured trend wording was replaced by statements about the studies examined.

**Before:**

> 14. [High-throughput] "post-2022 cardiomyocyte MEA studies increasingly emphasize high-throughput and longitudinal applications" and "As a result, reliance on a single metric such as FPD has progressively given way to multi-parameter feature sets". Based on Altrocchi et al. (2023), Matsuda et al. (2025) and Park et al. (2025, 2026); the trends are not measured. Support: thin.

**After:**

> 14. [High-throughput] (revised 2026-10-24) "several of the post-2022 studies examined address high-throughput and longitudinal applications" and "In the studies examined, single conventional metrics are complemented by multi-parameter feature sets encompassing beat rate, beat-to-beat variability, conduction properties, and event-based descriptors (Altrocchi et al., 2023; Matsuda et al., 2025)." Based on Altrocchi et al. (2023), Matsuda et al. (2025) and Park et al. (2025, 2026); the trends are no longer claimed. Support: supported as worded for the studies named (thin: two studies for the feature sets).

### 68. `docs/claims-by-source.md`: Synthesis item 15

**Why:** The uncited trend statements were replaced by cited examples; the sentence on UHD-MEA data was removed because Matsuda et al. use PCA and MANOVA.

**Before:**

> 15. [Motivation] "Since 2022, MEA recordings from hiPSC-CMs have increasingly been used not only for basic measurements ... but also for mechanistic electrophysiological phenotyping, proarrhythmia risk assessment, and longitudinal drug testing." and [Conclusion] "Looking forward, machine learning is rapidly becoming an integral layer in cardiomyocyte MEA workflows." Trend statements with no citation; the examples in the review (Pramudito, Park 2026, Lee, Scheurer) show that such uses exist, not that they are rapidly growing. Support: none for the trend wording.

**After:**

> 15. [Motivation, Conclusion] (revised 2026-10-24) "In the studies examined, MEA recordings from hiPSC-CMs are used not only for basic measurements ... but also for mechanistic electrophysiological phenotyping (Maurissen et al., 2024; Park et al., 2025; Park et al., 2026), proarrhythmia risk assessment (Blinova et al., 2018; Pramudito et al., 2026) and longitudinal drug testing (Altrocchi et al., 2023; Guerrelli et al., 2024)" and "machine learning is used in several of the studies examined — ... (Pramudito et al., 2026), ... (Park et al., 2026), ... (Lee et al., 2024) — and it may become a more integral layer of cardiomyocyte MEA workflows." Based on the studies named. Support: supported as worded; the earlier trend wording ('increasingly', 'rapidly becoming') and the uncited 'AI-driven interpretation of UHD-MEA data' were removed.

### 69. `docs/claims-by-source.md`: Pointer at the end of the file

**Why:** Points readers to the summary of the lint pass.

**Before:**

> (end of file)

**After:**

> See also `docs/lint-fixes-2026-10-24.md` for the changes made in the lint pass of 2026-10-24 (wiki pages, index, new concept and method pages, and the softened sentences of `main.md` behind synthesis items 1, 3, 9, 10, 14 and 15).

## Group 9. Licence, README, export notes, ToDo

### 70. `LICENSE`: New file: CC BY 4.0 legal text

**Why:** You chose a free licence, the same CC BY 4.0 that the Declarations give the paper. The file is the unmodified official plain-text legal code downloaded from creativecommons.org (18,657 bytes); I did not type or alter any of it.

**New file.** See the file itself; its contents are not repeated here.

### 71. `README.md`: README: new Licence section

**Why:** Adds the licence statement that was missing. The `raw/` exception is stated because the PDFs have their own licences (for example CC BY-NC-ND for Hayakawa et al., 2014). No link to the Zenodo deposit is added yet; you said to add that after publication.

**Before:**

> ## Tips

**After:**

> ## Licence
>
> Unless noted otherwise, the content written for this repository (`main.md`, `wiki/`, `docs/`, `scripts/` and `notes.md`) is released under the [Creative Commons Attribution 4.0 International licence (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/); the full text is in [LICENSE](LICENSE). This is the same licence that the Declarations of the paper give to the text. The source documents in `raw/` are not covered: they keep the licences and copyrights of their publishers and authors, and the non-open-access ones are kept out of the repository (see `.gitignore`).
>
> ## Tips

### 72. `docs/pdf-export-notes.md`: pdf-export-notes: repository section rewritten

**Why:** The earlier text said that a link to a moving branch would not match the deposited PDF and proposed a Declarations sentence about a tag. You decided that the link stays and main.md is not touched, so the section now says that the address is stable, the tag is optional and needs no text change, and the licence step is done. It also explains the point you did not understand.

**Before:**

> ## Repository snapshot (added 2026-10-24)
>
> The Declarations point to https://github.com/AnaHill/MEA_review_llm_wiki for the source notes and log. A link to a moving branch will not match the deposited PDF after later edits, so freeze the state:
>
> - [ ] Finish all edits to `main.md`, run `python -I scripts/check.py` (0 errors) and commit.
> - [ ] Optional: add one sentence to Declarations (Data and code availability) such as "The state of the repository at the time of deposit is tagged v1.0-preprint." Commit it first, because the tag must sit on the commit that already contains the sentence.
> - [ ] Create an annotated tag on that commit (for example `git tag -a v1.0-preprint -m "state at Zenodo deposit"` and `git push origin v1.0-preprint`) and, if wanted, a GitHub release from it. Do not enable the automatic GitHub-to-Zenodo archiving unless a second DOI is wanted; the PDF is deposited manually and linked to the opinion paper's record.
> - [ ] Check that the repository is public and that the non-open-access PDFs (`raw/pramudito-2026-ensemble.pdf`, `raw/clements-2025-aims-poster.pdf`) are not in the pushed history (`git log --all -- raw/pramudito-2026-ensemble.pdf`); open-access PDFs keep their own licences (for example CC BY-NC-ND for Hayakawa et al., 2014).
> - [ ] Add a LICENSE file or a README licence section (none exists on 2026-10-24); the paper itself is CC BY 4.0 (Declarations).
>
>

**After:**

> ## Repository link and snapshot (revised 2026-10-24)
>
> The Declarations point to https://github.com/AnaHill/MEA_review_llm_wiki for the source notes and log. That address does not change and `main.md` (including the Declarations) is not edited for this. What does change is the content behind the address: a reader who follows it later sees the repository as it is then, not as it was at deposit. This is acceptable and needs no action; the steps below are optional and only for your own reference.
>
> - [ ] Optional: after the last commit, create an annotated tag on it (for example `git tag -a v1.0-preprint -m "state at Zenodo deposit"` and `git push origin v1.0-preprint`). It does not change the link and needs no change in `main.md`.
> - [ ] Do not enable the automatic GitHub-to-Zenodo archiving of releases: it would mint a second DOI for the repository. The PDF is deposited manually and linked to the opinion paper's record.
> - [ ] After the Zenodo deposit is published, add its link to the start of `README.md` (the ToDo item "Kun julkaistu Zenodossa").
> - [x] Licence: `LICENSE` (CC BY 4.0) and a README section were added on 2026-10-24.
> - [ ] Check that the non-open-access PDFs (`raw/pramudito-2026-ensemble.pdf`, `raw/clements-2025-aims-poster.pdf`) are not in the pushed history: `git log --all -- raw/pramudito-2026-ensemble.pdf raw/clements-2025-aims-poster.pdf` printed nothing on 2026-10-24.
>

### 73. `ToDo.md`: ToDo: synthesis row

**Why:** The row now says which items were softened and which remain.

**Before:**

> - [ ] Synteesikohdat: docs/claims-by-source.md:n osio "Claims that rest on the author's own synthesis or are not cited" (17 numeroitua kohtaa). Kohdissa 1, 3, 9, 10, 14 ja 15 on yleistyksiä ilman lähdettä: lisää lähde, pehmennä tai poista. Niitä ovat mm. neljä aukkoa, päätelmä avoimista alustoista ja MEA-natiivin maturaatioindeksin kokoaminen olemassa olevista osista. Kohdat 16 ja 17 ovat outlookin hypoteeseja (tekstissä merkitty hypoteeseiksi). Kohdan 1 vasta-argumentti: Vuorenpää ym. 2023 (osio 6.1.1) sanoo, että AP:iden ja FP:iden parametrisointi on vakiintunutta ja mahdollistaa tulosten vertailun, joten pehmennä "major source of variability" (Abstract, Motivation) tai perustele se paremmin

**After:**

> - [ ] Synteesikohdat: docs/claims-by-source.md:n osio "Claims that rest on the author's own synthesis or are not cited" (17 numeroitua kohtaa). Kohdat 1, 3, 9, 10, 14 ja 15 pehmennettiin 24.10. (ks. docs/lint-fixes-2026-10-24.md, ryhmä 7): lue uudet sanamuodot ja päätä, kelpaavatko. Jäljellä olevat kohdat (2, 4, 5–8, 11–13) ovat ennallaan; 16 ja 17 ovat outlookin hypoteeseja. Motivation-lauseen "needs citation(s)" -kommentti on yhä paikallaan (lause sai nyt lähteitä)

### 74. `ToDo.md`: ToDo: lint row

**Why:** Lint item closed with a pointer to the summary.

**Before:**

> - [ ] Lint 24.10. tehty (ks. wiki/log.md, merkintä lint): korjausehdotukset odottavat päätöstäsi: indeksin vanhentuneet rivit (Ismaili, Matsuda, Park 2025, Hwang, Scheurer, Ernault, Mäki v2/v3, Hayakawa-järjestys, Last updated), wiki/hipsc-cm-maturation.md (Fetterman ja Correia -yleistykset), wiki/critical-assessment-maki-claims.md (Ernault "majority", "field converging", PhysioMEA ja kääntäminen, Fig. 6), Weiser-Bitoun-sivulta puuttuva käänteis-/inversiokäsittely, Limitations (v) ja Välimäki

**After:**

> - [x] Lint 24.10.: korjaukset 1–4, 6 ja 7 tehty (indeksi, maturaatiosivu, critical assessment, Weiser-Bitoun-sivu, neljä uutta sivua, main.md:n pehmennykset). Kohta 5 ei vaadi muutosta (täystekstit luettiin aina kun mahdollista; Välimäki ei ollut mahdollinen). Lue koonti docs/lint-fixes-2026-10-24.md ennen committia

### 75. `ToDo.md`: ToDo: GitHub row

**Why:** Closed according to your decision.

**Before:**

> - [ ] GitHub-repo julkaisuhetken tilaan: tee viimeisen commitin jälkeen tagi (esim. `v1.0-preprint`) ja GitHub-release, ja harkitse virkettä Declarationsin Data and code availability -kohtaan ("The state of the repository at the time of deposit is tagged v1.0-preprint."). Tagi pitää tehdä sen commitin päälle, jossa virke jo on. Ks. docs/pdf-export-notes.md, osio "Repository snapshot"

**After:**

> - [x] GitHub-linkki: pysyy ennallaan eikä main.md:tä muuteta; tagi on valinnainen (ks. docs/pdf-export-notes.md, osio "Repository link and snapshot")

### 76. `ToDo.md`: ToDo: licence row

**Why:** Closed; the Zenodo link remains a post-publication task.

**Before:**

> - [ ] Repon lisenssi: repossa ei ole LICENSE-tiedostoa eikä README mainitse lisenssiä; Declarations lupaa vain tekstille CC BY 4.0. Päätä koodin (scripts/) ja wiki-sisällön lisenssi ja kirjaa se README:hen; avoimet raw-PDF:t ovat omien lisenssiensä alaisia (esim. CC BY-NC-ND), ei-avoimet pysyvät .gitignoressa

**After:**

> - [x] Repon lisenssi: CC BY 4.0 (LICENSE + README:n Licence-osio) lisätty 24.10.; raw/-PDF:t eivät kuulu siihen. README:hen lisätään linkki Zenodoon julkaisun jälkeen

## Group 10. Small fixes after reading the simulated peer review (docs/peer_review_main.md)

These changes followed the simulated peer review in `docs/peer_review_main.md` (deleted later the same day; in the git history, last version in commit d3430e6); the proposed sentence for review point 4 is deliberately not applied (see the end of that file).

### Figure 1: label on the 2023 entry (review point 1)

**File:** `main.md`. **Why:** The timeline put the author's own, non-peer-reviewed tool and opinion paper beside peer-reviewed software without saying so; this was disclosed only in Limitations (iv) and the Declarations, which a reader of the figure does not see.

**Before:**

> DatAnalyzer / Mäki opinion paper — morphology-aware FPD

**After:**

> DatAnalyzer / Mäki opinion paper (own work, not peer reviewed) — morphology-aware FPD

### Table 1: DatAnalyzer row (review points 1 and 3)

**File:** `main.md`. **Why:** Same disclosure as in Figure 1, and the inversion feature is marked as not independently validated, as the text already says.

**Before:**

> | DatAnalyzer (Mäki, 2023) | 2023 | Python | Baseline return | Morphology-aware classification (3 waveform types); inversion for only-high-peak signals |

**After:**

> | DatAnalyzer (Mäki, 2023; author's own tool, not peer reviewed) | 2023 | Python | Baseline return | Morphology-aware classification (3 waveform types); inversion for only-high-peak signals (not independently validated) |

### Fiducial section: noise sensitivity of the baseline-return end point (review point 2)

**File:** `main.md`. **Why:** The text said nothing about how sensitive a threshold-based return to baseline is to noise and drift. The added sentence states that this was not examined in the reviewed studies, using only what the sources say (beat averaging in Mäki 2023; Hayakawa et al. on the difficulty of an accurate end point).

**Before:**

> These findings underscore the importance of waveform morphology assessment prior to any fiducial-point-based analysis.

**After:**

> These findings underscore the importance of waveform morphology assessment prior to any fiducial-point-based analysis. The robustness of the baseline-return convention has not been examined in the studies reviewed here: Mäki (2023) averages beats to reduce noise, but how the end point behaves at low signal-to-noise ratios or with baseline drift is not evaluated, and an accurate end point was already described as difficult to establish in simultaneous video and MEA recordings (Hayakawa et al., 2014).

### Figure 2 caption: inversion caveat (review point 3)

**File:** `main.md`. **Why:** The figure presented the inversion branch as one of several equal branches; the text says it is internally validated but not independently replicated. The caption now says so.

**Before:**

> Waveform classification determines the analysis branch applied before FPD measurement; rate correction is applied after.*

**After:**

> Waveform classification determines the analysis branch applied before FPD measurement; rate correction is applied after. The signal-inversion branch is the author's own proposal (Mäki, 2023) and has not been independently validated.*

### Abstract, gap 4: scope (review point 5)

**File:** `main.md`. **Why:** The Conclusion already scopes the proposed reference value to the electrophysiological axis (because maturation axes are independent, Fetterman et al., 2024), but the Abstract did not, which invited the reading that the paper contradicts itself.

**Before:**

> and the absence of validated MEA-derived reference values for staging hiPSC-CM maturation status.

**After:**

> and the absence of validated MEA-derived reference values for staging the electrophysiological axis of hiPSC-CM maturation status.

### Table 2: Ernault row, FPD start (review point 6)

**File:** `main.md`. **Why:** The dash read as a missing value; the paper does not define an FPD start, it tests T-wave landmarks against the action potential.

**Before:**

> | T-wave peak (biphasic-validated, NRVM) | — | T-wave peak |

**After:**

> | T-wave peak (biphasic-validated, NRVM) | not defined (T-wave landmarks are tested against APD) | T-wave peak |

### Section heading: model complexity (review point 6)

**File:** `main.md`. **Why:** The section discusses 3D systems and, at the end, in silico models of the MEA including the 2D model of Botti et al.; the old heading mentioned only 3D. The coverage tag 'Model complexity' still matches.

**Before:**

> ## Model complexity: limitations of 2D-centric heuristics in 3D cardiomyocyte systems

**After:**

> ## Model complexity: 3D cardiomyocyte systems and in silico models of the MEA

### Rate correction section: pacing as an alternative (review point 6)

**File:** `main.md`. **Why:** The review criticised the Fridericia correction but did not mention pacing as the other way to handle rate. The sentence is marked as the author's reasoning, and its sourced parts come from the Clements, Matsuda and Guerrelli pages.

**Before:**

> Open analysis platforms do not necessarily close it: the published CardioMEA feature set contains FPD but no rate-corrected FPD (Lee et al., 2024). Despite this limitation,

**After:**

> Open analysis platforms do not necessarily close it: the published CardioMEA feature set contains FPD but no rate-corrected FPD (Lee et al., 2024). Pacing at a fixed rate would in principle avoid the need for a correction (the author's reasoning), but several of the studies examined recorded spontaneous beating (Clements et al., 2025; Matsuda et al., 2025, who name the absence of pacing as a limitation of their recordings), and Guerrelli et al. (2024) also recorded paced beating. Despite this limitation,

### Claims checklist of Matsuda et al. (2025)

**File:** `docs/claims-by-source.md`. **Why:** The softened main.md now cites this source in the Fiducial or FPDc section; the claim is added so that the coverage check shows no gap.

**Before:**

> - [ ] (4) it detected doxorubicin-induced cardiotoxicity at 0.03 µM within 24 h, a concentration 10-fold lower than reported in earlier studies.

**After:**

> - [ ] (4) it detected doxorubicin-induced cardiotoxicity at 0.03 µM within 24 h, a concentration 10-fold lower than reported in earlier studies.
> - [ ] (5) [FPDc] its recordings were of spontaneous beating without pacing, which the authors name as a limitation (a stimulation upgrade was under way).

### Claims checklist of Guerrelli et al. (2024)

**File:** `docs/claims-by-source.md`. **Why:** The softened main.md now cites this source in the Fiducial or FPDc section; the claim is added so that the coverage check shows no gap.

**Before:**

> - [ ] (9) [Motivation] example of longitudinal drug testing (culture-time effects).

**After:**

> - [ ] (9) [Motivation] example of longitudinal drug testing (culture-time effects).
> - [ ] (10) [FPDc] it also recorded paced beating (paced recordings on days 3-14), besides spontaneous recordings.

### Claims checklist of Clements et al. (2025)

**File:** `docs/claims-by-source.md`. **Why:** The softened main.md now cites this source in the Fiducial or FPDc section; the claim is added so that the coverage check shows no gap.

**Before:**

> - [ ] (4b) [Conclusion] quantitative acceptance criteria exist for well acceptance (amplitude, synchrony, beat period, FPDc).

**After:**

> - [ ] (4b) [Conclusion] quantitative acceptance criteria exist for well acceptance (amplitude, synchrony, beat period, FPDc).
> - [ ] (6) [FPDc] the proposed acceptance criteria are for spontaneous-beating hiPSC-ventricular-CM assays.

### Claims checklist of Hayakawa et al. (2014)

**File:** `docs/claims-by-source.md`. **Why:** The softened main.md now cites this source in the Fiducial or FPDc section; the claim is added so that the coverage check shows no gap.

**Before:**

> - [ ] (4) [Fiducial] simultaneous video and MEA recordings in iCell monolayers: the two FPD end points in use at the time, the peak of the positive deflection and the return of the positive deflection to baseline, appeared to correspond to different phases of the relaxation motion (upstroke and peak, respectively), and an accurate end point was difficult to establish.

**After:**

> - [ ] (4) [Fiducial] simultaneous video and MEA recordings in iCell monolayers: the two FPD end points in use at the time, the peak of the positive deflection and the return of the positive deflection to baseline, appeared to correspond to different phases of the relaxation motion (upstroke and peak, respectively), and an accurate end point was difficult to establish.
> - [ ] (5) [Fiducial] an accurate FP end point was difficult to establish in the simultaneous recordings (cited in the sentence on the robustness of the baseline-return end point).

## Group 11. Follow-up: hash escapes, the ill-posed-inverse-problem sentence, caution note

Follow-up to the simulated peer review and to the guide `docs/peer_review_missing_references_main.md` (also deleted later the same day; in the git history, last version in commit d3430e6).

### Hash identifiers escaped; caution note added

**File:** `docs/peer_review_missing_references_main.md`. **Why:** Three unescaped hash identifiers (the AIMS identifier) (lines 54, 57, 82) would be read as Obsidian tags; they are now written \#CM01 as the repository rule requires. The caution note records that the guide was not verified: five of its seven references are already in main.md (and were checked), the two others have incomplete details and must not be added before they are read, and some LaTeX is damaged. I did not change any other text in the file.

**Before:**

> the AIMS identifier with an unescaped hash, in three places

**After:**

> the same identifier with an escaped hash in three places, plus the caution note at the top

### Outlook, device-separation paragraph: ill-posed inverse problem (review point 4)

**File:** `main.md`. **Why:** Approved by the researcher on 2026-10-24. The sentence states the mathematical difficulty that the simulated reviewer raised and labels it as the author's reasoning, not a sourced finding, so the outlook does not overstate what could be achieved.

**Before:**

> Whether the AP can be recovered from the FP at all is an open question: the FP also depends on current from neighbouring cells (Ernault et al., 2024), so removing the device contribution alone would not be sufficient.

**After:**

> Whether the AP can be recovered from the FP at all is an open question: the FP also depends on current from neighbouring cells (Ernault et al., 2024), so removing the device contribution alone would not be sufficient. The recovery may also be an ill-posed inverse problem, because a field potential is a weighted sum of the transmembrane currents of many surrounding cells; this is the author's reasoning from extracellular recording theory and not a finding of the studies reviewed.

### Synthesis item 17 updated

**File:** `docs/claims-by-source.md`. **Why:** Keeps the claims list in line with the new sentence in main.md; it is marked as reasoning without a source.

**Before:**

> A proposal of the author; no reviewed study attempted it, and Ernault et al. suggest the FP also depends on neighbouring cells.

**After:**

> A proposal of the author; no reviewed study attempted it, and Ernault et al. suggest the FP also depends on neighbouring cells. The text adds, as the author's reasoning from extracellular recording theory with no source, that the recovery may be an ill-posed inverse problem because the FP is a weighted sum of the currents of many surrounding cells (added 2026-10-24).

### Peer review assessment: heading of the proposal

**File:** `docs/peer_review_main.md`. **Why:** The proposal was approved and applied, so the heading no longer says 'not yet added'.

**Before:**

> ## Ehdotus kohdan 4 virkkeeksi (ei vielä lisätty)

**After:**

> ## Kohdan 4 virke (lisätty 24.10.)

### Peer review assessment: status of point 4

**File:** `docs/peer_review_main.md`. **Why:** Same reason.

**Before:**

> Ehdotettu lisävirke odottaa hyväksyntääsi, ks. alla.

**After:**

> Lisävirke lisättiin 24.10. hyväksyntäsi jälkeen, ks. alla.

### ToDo: review point 4 closed

**File:** `ToDo.md`. **Why:** The sentence was added.

**Before:**

> - [ ] Päätä kohdan 4 virke (outlook, laitteen erottaminen signaalista): ehdotettu virke on docs/peer_review_main.md:n lopussa; lisätäänkö se vai ei? Muut peer review -korjaukset (1, 2, 3, 5, 6) on tehty 24.10., ks. docs/lint-fixes-2026-10-24.md, ryhmä 10

**After:**

> - [x] Kohdan 4 virke (käänteisongelma huonosti asetettu) lisätty outlookiin 24.10.; muut peer review -korjaukset (1, 2, 3, 5, 6) tehty samana päivänä, ks. docs/lint-fixes-2026-10-24.md, ryhmät 10 ja 11

## Appendix: the author's assessment of the simulated peer review (kept when the review files were deleted)

The simulated review (`docs/peer_review_main.md`) was written by an AI model that was not told that the text is a preprint. The author's assessment, summarised from the deleted file:

**Applied (group 10 above):** label the author's own tool and opinion paper as not peer reviewed (Figure 1, Table 1); state that the robustness of the baseline-return end point to noise and drift was not examined; caveat the signal-inversion branch (Table 1, Figure 2 caption); scope gap 4 in the Abstract to the electrophysiological axis; cosmetic fixes (Table 2 cell for Ernault, section heading, a sentence on pacing). **Applied after approval (group 11):** a sentence that recovering the action potential from a field potential may be an ill-posed inverse problem, marked as the author's reasoning.

**Rejected or not applicable, with the reasons:**
- *Re-anchor the review to CiPA and reject the manuscript.* CiPA does not define field-potential analysis conventions, so it is not an alternative evaluative framework. The paper is an unreviewed preprint, and the Mäki (2023) anchor is documented in the Scope section, Limitations (iv) and the Declarations.
- *PRISMA and reproducibility of the search.* The review is openly narrative and non-systematic, and Limitations says so.
- *HTML comments, affiliation and target-journal requirements.* The comments are removed before export (ToDo); the rest does not apply to a preprint.
- *"Core premise not demonstrated".* The text already says "plausible source" and that no reviewed study measures the effect; the softening is deliberate, not a contradiction.
- *"Self-contradiction with Fetterman et al. (2024)".* A misreading: the Conclusion scopes the proposed reference value to the electrophysiological axis, which is why the Abstract was clarified.
- *"Conflation of electroporation with computational processing".* Incorrect: in the text electroporation is a separate source of paired data.
- *Biophysical argument against inversion.* Judged exaggerated (the polarity at an electrode depends on the electrode-source geometry, and PhysioMEA analyses inverted signals for inverted T waves and low R peaks), but the branch was caveated because it is not independently validated. This is a field-expertise judgement of the author.

The companion guide of "missing references" (`docs/peer_review_missing_references_main.md`) was judged useless: five of its seven references were already in `main.md` and checked, the two others (activation-recovery intervals; Millard et al., rate correction) are unverified, and its line numbers and LaTeX were unreliable. Its one useful idea, the activation-recovery interval as an alternative to peak-to-peak FPD, is a to-do item in `ToDo.md`.

## Group 12. Välimäki et al. (2021) replaced by Ryynänen et al. (2018) (2026-10-25)

Replacement of the conference record of Välimäki et al. (2021) with the open-access paper Ryynänen et al. (2018), read in full on 2026-10-25. Main reason: Välimäki et al. could be cited only from a portal record (no abstract, DOI or file), whereas Ryynänen et al. is a peer-reviewed, open-access paper in which the researcher is not an author.

### New wiki page for Ryynänen et al. (2018)

**File:** `wiki/papers/ryynanen-2018-single-cell-mea.md`. **Why:** Written from the full text read on 2026-10-25. The page separates what the authors state from our observations (small sample, unsynchronised recordings, Bazett's formula).

**New file.** See the file itself.

### Outlook, sensor-fusion paragraph

**File:** `main.md`. **Why:** The conference contribution (only a portal record was available) is replaced by a peer-reviewed, open-access paper that was read in full and in which the researcher is not an author.

**Before:**

> , and combined MEA and video-based motion analysis of hiPSC-CMs in hypoxia has been presented in a conference contribution by the author's former research group (Välimäki et al., 2021).

**After:**

> , and an MEA with transparent electrodes has been used to record the field potential and the video-based motion of the same single hPS-CM at the same time, although the two recordings were not automatically synchronised (Ryynänen et al., 2018).

### Limitations (vi)

**File:** `main.md`. **Why:** Same replacement in the list of pre-2022 background works.

**Before:**

> such as Blinova et al. (2018), Hayakawa et al. (2014) and Välimäki et al. (2021), are cited only

**After:**

> such as Blinova et al. (2018), Hayakawa et al. (2014) and Ryynänen et al. (2018), are cited only

### Declarations, competing interests

**File:** `main.md`. **Why:** The author is no longer a co-author of any cited work other than Mäki (2023), so the sentence about co-authoring Välimäki et al. (2021) is removed. The remaining relationship is stated as the researcher described it (the former research group); this wording should be confirmed by the researcher.

**Before:**

> The author is also a co-author of the conference contribution Välimäki et al. (2021), cited in the outlook; two of its co-authors are also authors of the review Vuorenpää et al. (2023), likewise cited in the outlook.

**After:**

> Several authors of the review Vuorenpää et al. (2023) and of Ryynänen et al. (2018), both cited in the outlook, belong to the research group in which the author previously worked; the author is not an author of either.

### References: Välimäki entry removed

**File:** `main.md`. **Why:** The work is no longer cited.

**Before:**

> Välimäki, H., Mäki, A.-J., Kattipparambil Rajan, D., Pekkanen-Mattila, M., Kreutzer, J., Ryynänen, T., Verho, J., Aalto-Setälä, K., & Kallio, P. (2021, July 1–2). *Combined electrophysiological and video-based motion analysis for human induced pluripotent stem cell-derived cardiomyocytes in hypoxia* [Conference contribution]. EUROOoCs conference of European Organ-on-Chip Society, virtual conference. https://researchportal.tuni.fi/fi/publications/combined-electrophysiological-and-video-based-motion-analysis-for/
>
>

**After:**

> (removed)

### References: Ryynänen entry added

**File:** `main.md`. **Why:** APA entry from the title page of the paper (seven authors in order, journal, article number 117001, DOI). The issue number is not given in the paper and is therefore not stated.

**Before:**

> Scheurer, F., Hammer, A.,

**After:**

> Ryynänen, T., Pekkanen-Mattila, M., Shah, D., Kreutzer, J., Kallio, P., Lekkala, J., & Aalto-Setälä, K. (2018). Microelectrode array for noninvasive analysis of cardiomyocytes at the single-cell level. *Japanese Journal of Applied Physics*, *57*, 117001. https://doi.org/10.7567/JJAP.57.117001
>
> Scheurer, F., Hammer, A.,

### Rate correction section

**File:** `main.md`. **Why:** Adding Ryynänen et al. (2018) means that a study in the reference list used a different formula; the sentence 'the Fridericia formula is the correction used in the studies examined here' would otherwise be inexact.

**Before:**

> Park et al. (2025) also report corrected FPD but do not name the formula.

**After:**

> Park et al. (2025) also report corrected FPD but do not name the formula. Ryynänen et al. (2018), a pre-2022 study cited only in the outlook, corrected FPD with Bazett's formula.

### references.md: Välimäki entry removed

**File:** `wiki/references.md`. **Why:** The work is no longer cited.

**Before:**

> Välimäki, H., Mäki, A.-J., Kattipparambil Rajan, D., Pekkanen-Mattila, M., Kreutzer, J., Ryynänen, T., Verho, J., Aalto-Setälä, K., & Kallio, P. (2021, July 1–2). *Combined electrophysiological and video-based motion analysis for human induced pluripotent stem cell-derived cardiomyocytes in hypoxia* [Conference contribution]. EUROOoCs conference of European Organ-on-Chip Society, virtual conference. https://researchportal.tuni.fi/fi/publications/combined-electrophysiological-and-video-based-motion-analysis-for/
>
>

**After:**

> (removed)

### references.md: Ryynänen entry added

**File:** `wiki/references.md`. **Why:** Same entry as in main.md (the checker requires them to match).

**Before:**

> Scheurer, F., Hammer, A.,

**After:**

> Ryynänen, T., Pekkanen-Mattila, M., Shah, D., Kreutzer, J., Kallio, P., Lekkala, J., & Aalto-Setälä, K. (2018). Microelectrode array for noninvasive analysis of cardiomyocytes at the single-cell level. *Japanese Journal of Applied Physics*, *57*, 117001. https://doi.org/10.7567/JJAP.57.117001
>
> Scheurer, F., Hammer, A.,

### index: Välimäki line removed

**File:** `wiki/index.md`. **Why:** The page was deleted.

**Before:**

> - [Välimäki et al. 2021](papers/valimaki-2021-hypoxia-video-mea.md) — Conference contribution (EUROOoCs 2021): combined MEA and video-based motion analysis of hiPSC-CMs in hypoxia (MEA use confirmed by the researcher); portal record only, content not read. Researcher is a co-author.
>

**After:**

> (removed)

### index: Ryynänen line added (before Scheurer)

**File:** `wiki/index.md`. **Why:** Alphabetical position between Pramudito and Scheurer.

**Before:**

> - [Scheurer et al. 2025](papers/scheurer-2025-optical-ai.md) — Video-based SVM/SHAP classifier separating immature (day 21) from lipid-medium-matured (day 42) iPSC-CM cultures from beating features (99.5 % test accuracy; binary, with a heterogeneous less-mature B27 group); not MEA; cites Hayakawa et al. for the FPD–contraction link. TU Dresden, *Comput Struct Biotechnol J* 27:3719–3728.

**After:**

> - [Ryynänen et al. 2018](papers/ryynanen-2018-single-cell-mea.md) — Single-cell MEA with 80 µm electrodes (opaque and transparent ITO): field potential, beating rate, FPD (Bazett cFPD) and E-4031 effect from single hPS-CMs, with simultaneous video-based motion analysis (not automatically synchronised). *Jpn J Appl Phys* 57:117001. Pre-2022 background; open access.
> - [Scheurer et al. 2025](papers/scheurer-2025-optical-ai.md) — Video-based SVM/SHAP classifier separating immature (day 21) from lipid-medium-matured (day 42) iPSC-CM cultures from beating features (99.5 % test accuracy; binary, with a heterogeneous less-mature B27 group); not MEA; cites Hayakawa et al. for the FPD–contraction link. TU Dresden, *Comput Struct Biotechnol J* 27:3719–3728.

### index: Vuorenpää line

**File:** `wiki/index.md`. **Why:** The sentence about Välimäki 2021 no longer applies.

**Before:**

> - [Vuorenpää et al. 2023](papers/vuorenpaa-2023-mps-building-blocks.md) — Review of cardiac microphysiological system building blocks (cells, matrix, stimulation, functional measurements, computational modelling); multimodal concurrent measurements give data for parameterising and validating models. *Front Physiol* 14:1213959. Two authors co-authored Välimäki 2021.

**After:**

> - [Vuorenpää et al. 2023](papers/vuorenpaa-2023-mps-building-blocks.md) — Review of cardiac microphysiological system building blocks (cells, matrix, stimulation, functional measurements, computational modelling); multimodal concurrent measurements give data for parameterising and validating models. *Front Physiol* 14:1213959.

### index: multimodal concept line

**File:** `wiki/index.md`. **Why:** Välimäki replaced by Ryynänen.

**Before:**

> Hayakawa, Välimäki, Vuorenpää)

**After:**

> Hayakawa, Ryynänen, Vuorenpää)

### Multimodal page: row replaced

**File:** `wiki/multimodal-measurement.md`. **Why:** Välimäki (portal record only) replaced by Ryynänen et al. (2018), read in full.

**Before:**

> | [[wiki/papers/valimaki-2021-hypoxia-video-mea.md]] | MEA and video-based motion analysis of hiPSC-CMs in hypoxia (conference contribution; portal record only) |

**After:**

> | [[wiki/papers/ryynanen-2018-single-cell-mea.md]] | MEA field potential and video-based motion analysis of the same single hPS-CM through transparent electrodes (recorded at the same time but not automatically synchronised; FPD, beating rate and beat-to-beat interval comparable between MEA and video where compared) |

### Hayakawa page: see also

**File:** `wiki/papers/hayakawa-2014-motion-fp.md`. **Why:** Link follows the replacement.

**Before:**

> - [[wiki/papers/valimaki-2021-hypoxia-video-mea.md]]

**After:**

> - [[wiki/papers/ryynanen-2018-single-cell-mea.md]]

### Vuorenpää page: note on overlap

**File:** `wiki/papers/vuorenpaa-2023-mps-building-blocks.md`. **Why:** Reworded because Välimäki et al. (2021) is no longer cited.

**Before:**

> Two of the authors (Välimäki, Pekkanen-Mattila) are also co-authors of [[wiki/papers/valimaki-2021-hypoxia-video-mea.md]]; disclosed in the Declarations of main.md.

**After:**

> Pekkanen-Mattila is also an author of [[wiki/papers/ryynanen-2018-single-cell-mea.md]]; the Declarations of main.md mention that several authors of both belong to the research group in which the researcher previously worked.

### Vuorenpää page: see also

**File:** `wiki/papers/vuorenpaa-2023-mps-building-blocks.md`. **Why:** Link follows the replacement.

**Before:**

> - [[wiki/papers/valimaki-2021-hypoxia-video-mea.md]]

**After:**

> - [[wiki/papers/ryynanen-2018-single-cell-mea.md]]

### Fridericia page: statement

**File:** `wiki/fridericia-rate-correction.md`. **Why:** Ryynänen et al. (2018) used Bazett's formula, so 'the only one used' is no longer true.

**Before:**

> Among the papers that name a formula, Fridericia is the only one used;

**After:**

> Among the papers that name a formula, Fridericia is used by all except Ryynänen et al. (2018, a pre-2022 single-cell MEA study, Bazett's formula);

### Fridericia page: new row

**File:** `wiki/fridericia-rate-correction.md`. **Why:** Records the Bazett use.

**Before:**

> | [[wiki/papers/lee-2024-cardiomea.md]] | the published CardioMEA feature set contains FPD but no rate-corrected FPD |

**After:**

> | [[wiki/papers/lee-2024-cardiomea.md]] | the published CardioMEA feature set contains FPD but no rate-corrected FPD |
> | [[wiki/papers/ryynanen-2018-single-cell-mea.md]] | cFPD calculated with Bazett's formula (pre-2022; single-cell MEA, FPD measured with an in-house Origin module) |

### Page deleted

**File:** `wiki/papers/valimaki-2021-hypoxia-video-mea.md`. **Why:** The conference contribution is no longer cited; the page (portal record only) is replaced by the Ryynänen page. It remains in the git history.

**Before:**

> (page with portal record only, content not read)

**After:**

> (deleted)

### Claims list: Välimäki section removed

**File:** `docs/claims-by-source.md`. **Why:** The work is no longer cited.

**Before:**

> ## Välimäki et al. (2021)
>
> Local file: none (conference contribution; only the Tampere University research portal record was seen); page `wiki/papers/valimaki-2021-hypoxia-video-mea.md`. Status: from the portal record only (title, authors, year, event); the abstract and the contribution itself were not read. The researcher is a co-author (self-citation, disclosed in the Declarations).
>
> Claims (tick `[x]` when you have checked the claim against the source):
>
> - [ ] (1) [Outlook] combined electrophysiological and video-based motion analysis of hiPSC-CMs in hypoxia has been presented in a conference contribution by the author's former research group (the title supports this; that the electrophysiology was MEA recording was confirmed by the researcher, a co-author, on 2026-10-24, not by the portal record).
> - [ ] (2) [Declarations] the author is a co-author.
> - [ ] (3) [Limitations] pre-2022 conference contribution cited as background for earlier multimodal work.
>
> Check 2026-10-24: title, nine authors in order, year 2021 and event (EUROOoCs, virtual, 1–2 July 2021) match the portal record; no DOI, abstract, publisher or pages are shown. Verify the content yourself before relying on it.
>
>

**After:**

> (removed)

### Claims list: Ryynänen section added

**File:** `docs/claims-by-source.md`. **Why:** Keeps the coverage check at zero gaps; the claims follow the new main.md wording.

**Before:**

> ## Scheurer et al. (2025)

**After:**

> ## Ryynänen et al. (2018)
>
> Local file: `raw/ryynanen-2018-single-cell-mea.pdf`; page `wiki/papers/ryynanen-2018-single-cell-mea.md`. Status: checked against the full text 2026-10-25 (text extraction; figures not viewed; supplementary videos not available). The researcher is not an author.
>
> Claims (tick `[x]` when you have checked the claim against the source):
>
> - [ ] (1) [Outlook] an MEA with transparent electrodes has been used to record the field potential and the video-based motion of the same single hPS-CM at the same time, although the two recordings were not automatically synchronised.
> - [ ] (2) [Limitations] pre-2022 work cited as background for earlier multimodal work.
> - [ ] (3) [FPDc] it corrected FPD with Bazett's formula.
> - [ ] (4) [Declarations] several of its authors (with those of Vuorenpää et al., 2023) belong to the research group in which the researcher previously worked; the researcher is not an author (to be confirmed by the researcher).
>
> Check 2026-10-25: (1) pp. 2–3 (aim: transparent electrodes enable simultaneous imaging and video analysis of the same cardiomyocytes), p. 5 ("Video and MEA recordings were taken manually at the same time; therefore, the recordings were not automatically synchronized in this study"), p. 7 ("beating frequencies and beat-to-beat intervals were similar when recorded with the two methods"; the electromechanical correlation is left to future studies). (3) p. 4 ("Bazett's formula was used to calculate the beat-rate-corrected FPD ...

### Claims list: Vuorenpää status line

**File:** `docs/claims-by-source.md`. **Why:** Reworded because Välimäki et al. (2021) is no longer cited.

**Before:**

> Two of the authors (Välimäki, Pekkanen-Mattila) are co-authors of Välimäki et al. (2021); disclosed in the Declarations.

**After:**

> Two of the authors (Välimäki, Pekkanen-Mattila) belong to the research group in which the researcher previously worked (Pekkanen-Mattila also co-authored Ryynänen et al., 2018); disclosed in the Declarations.

### Claims list: Vuorenpää claim 3

**File:** `docs/claims-by-source.md`. **Why:** Same reason.

**Before:**

> - [ ] (3) [Declarations] two of its authors are co-authors of Välimäki et al. (2021).

**After:**

> - [ ] (3) [Declarations] several of its authors (with those of Ryynänen et al., 2018) belong to the research group in which the researcher previously worked; the researcher is not an author (to be confirmed by the researcher).

### Synthesis item 16

**File:** `docs/claims-by-source.md`. **Why:** The basis of the sensor-fusion statement now cites Ryynänen et al. (2018) instead of the conference record.

**Before:**

> Välimäki et al. (2021; record only),

**After:**

> Ryynänen et al. (2018),

### ToDo: Välimäki row replaced

**File:** `ToDo.md`. **Why:** Records the replacement and the one wording that needs the researcher's confirmation.

**Before:**

> - [x] Välimäki ym. (2021): vahvistettu 24.10., että kyseessä on MEA + video; DOI:ta tai PDF:ää ei ole, joten viite pysyy portaalin tietueen varassa (kohdat a–c suljettu)

**After:**

> - [x] Välimäki ym. (2021) -viite korvattu 25.10. Ryynänen ym. (2018) -artikkelilla (JJAP 57, 117001; avoin, täysi teksti luettu, raw/ryynanen-2018-single-cell-mea.pdf): yhden solun MEA läpinäkyvillä elektrodeilla ja samanaikainen videoanalyysi. Tarkista: Declarationsin virke "... belong to the research group in which the author previously worked; the author is not an author of either" kuvaa ryhmäsuhteen oikein

### ToDo: own-check row for new sources

**File:** `ToDo.md`. **Why:** Välimäki is no longer cited; Ryynänen was read in full.

**Before:**

>   - Uudet lähteet: Hayakawa 2014 ja Vuorenpää 2023 on luettu kokonaan (kuvia ei katsottu Vuorenpäältä), mutta main.md:n tiivistykset kannattaa lukea itse; Välimäki 2021 perustuu vain portaalin tietueeseen ja sinun vahvistukseesi (MEA + video), eikä sisältöä ole luettu

**After:**

>   - Uudet lähteet: Hayakawa 2014 ja Vuorenpää 2023 on luettu kokonaan (kuvia ei katsottu Vuorenpäältä), mutta main.md:n tiivistykset kannattaa lukea itse; Ryynänen 2018 (korvasi Välimäki 2021:n 25.10.) on luettu kokonaan, kuvia ei katsottu

### ToDo: check.py row

**File:** `ToDo.md`. **Why:** Välimäki's two warnings (no DOI, no raw file) are gone with the replacement.

**Before:**

> - [ ] Aja `python -I scripts/check.py`: 0 virhettä (odotetut varoitukset nyt kolme: Clements 2025 -posterilla ei ole DOI:ta; Välimäki 2021 -viitteellä ei ole DOI:ta eikä raw-tiedostoa)

**After:**

> - [ ] Aja `python -I scripts/check.py`: 0 virhettä (odotettu varoitus nyt yksi: Clements 2025 -posterilla ei ole DOI:ta)

## Group 13. Declarations wording: CoEBoC collaboration (2026-10-25)

The researcher confirmed the Declarations sentence and gave the [CoEBoC](https://research.tuni.fi/coeboc/) collaboration (Centre of Excellence in Body-on-Chip Research, Tampere University) as the relationship; the sentence and the dependent texts were reworded accordingly.

### Declarations, competing interests

**File:** `main.md`. **Why:** Confirmed by the researcher on 2026-10-25: the relationship is the shared Centre of Excellence collaboration ([CoEBoC](https://research.tuni.fi/coeboc/), Tampere University). The Vuorenpää et al. title page lists the CoEBoC affiliation for all its authors; the Ryynänen paper predates it, so the sentence names the collaboration as the researcher described it.

**Before:**

> belong to the research group in which the author previously worked; the author is not an author of either.

**After:**

> are colleagues of the author from the Centre of Excellence in Body-on-Chip Research (CoEBoC) research collaboration at Tampere University; the author is not an author of either.

### Claims list: Ryynänen claim 4

**File:** `docs/claims-by-source.md`. **Why:** Wording follows the confirmed Declarations sentence.

**Before:**

> - [ ] (4) [Declarations] several of its authors (with those of Vuorenpää et al., 2023) belong to the research group in which the researcher previously worked; the researcher is not an author (to be confirmed by the researcher).

**After:**

> - [ ] (4) [Declarations] several of its authors (with those of Vuorenpää et al., 2023) are colleagues of the researcher from the Centre of Excellence in Body-on-Chip Research (CoEBoC) collaboration at Tampere University; the researcher is not an author (confirmed by the researcher, 2026-10-25).

### Claims list: Vuorenpää claim 3

**File:** `docs/claims-by-source.md`. **Why:** Same reason.

**Before:**

> - [ ] (3) [Declarations] several of its authors (with those of Ryynänen et al., 2018) belong to the research group in which the researcher previously worked; the researcher is not an author (to be confirmed by the researcher).

**After:**

> - [ ] (3) [Declarations] several of its authors (with those of Ryynänen et al., 2018) are colleagues of the researcher from the Centre of Excellence in Body-on-Chip Research (CoEBoC) collaboration at Tampere University (the CoEBoC affiliation is on the paper's title page); the researcher is not an author (confirmed by the researcher, 2026-10-25).

### Claims list: Vuorenpää status line

**File:** `docs/claims-by-source.md`. **Why:** Same reason.

**Before:**

> belong to the research group in which the researcher previously worked (Pekkanen-Mattila also co-authored Ryynänen et al., 2018); disclosed in the Declarations.

**After:**

> are colleagues of the researcher from the CoEBoC collaboration at Tampere University (Pekkanen-Mattila also co-authored Ryynänen et al., 2018); disclosed in the Declarations.

### Vuorenpää page: note on overlap

**File:** `wiki/papers/vuorenpaa-2023-mps-building-blocks.md`. **Why:** Same reason.

**Before:**

> mention that several authors of both belong to the research group in which the researcher previously worked.

**After:**

> mention that several authors of both are colleagues of the researcher from the Centre of Excellence in Body-on-Chip Research ([CoEBoC](https://research.tuni.fi/coeboc/)) collaboration at Tampere University.

### ToDo: confirmation recorded

**File:** `ToDo.md`. **Why:** The wording check is done.

**Before:**

> - [x] Välimäki ym. (2021) -viite korvattu 25.10. Ryynänen ym. (2018) -artikkelilla (JJAP 57, 117001; avoin, täysi teksti luettu, raw/ryynanen-2018-single-cell-mea.pdf): yhden solun MEA läpinäkyvillä elektrodeilla ja samanaikainen videoanalyysi. Tarkista: Declarationsin virke "... belong to the research group in which the author previously worked; the author is not an author of either" kuvaa ryhmäsuhteen oikein

**After:**

> - [x] Välimäki ym. (2021) -viite korvattu 25.10. Ryynänen ym. (2018) -artikkelilla (JJAP 57, 117001; avoin, täysi teksti luettu, raw/ryynanen-2018-single-cell-mea.pdf): yhden solun MEA läpinäkyvillä elektrodeilla ja samanaikainen videoanalyysi. Declarationsin virke vahvistettu 25.10.: yhteys on CoEBoC-tutkimuskollaboraatio (Tampere)
