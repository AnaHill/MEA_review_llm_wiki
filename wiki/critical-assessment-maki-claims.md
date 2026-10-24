# Critical assessment: key methodological claims in Mäki (2023)

**Date:** 2026-06-22 (updated 2026-10-24 after the source verification; the sentences changed then are listed in docs/lint-fixes-2026-10-24.md)  
**Question:** Do the four central methodological claims in [[wiki/papers/maki-2023-opinion.md]] hold up against the post-2022 literature in this wiki?

Claims assessed:
1. The first positive FP peak reflects depolarization of *neighboring* cells, not the locally recorded cell — it should not be used as the FPD start.
2. FPD end should be defined as the return to baseline, not the repolarization peak.
3. Pacemaker-like cells (no high peak) require different fiducial logic and should be analyzed differently (using Figure 5 method) rather than with the standard depolarization-peak approach.
4. The "only high peak" morphology is addressable by signal inversion before applying pacemaker-cell analysis.

---

## Claim 1 — First positive peak = neighboring-cell artifact

**Verdict: Defensible, with one important qualification.**

This is grounded in classical extracellular recording theory: in a propagating monolayer, the electrode sees the depolarization wavefront arriving from upstream cells before the local cell fires, producing the initial positive deflection. None of the available papers directly contradict this.

However, the claim is **preparation-dependent in a way the opinion paper does not make explicit.** It holds for propagating 2D monolayer recordings where a clear wavefront moves across the electrode array, but does not necessarily hold for:

- Synchronously beating preparations with no organized spatial propagation (small clusters, isolated areas, early-stage cultures), where the first positive peak may instead reflect the local cell's own initial displacement current
- 3D spheroid or tissue-sheet geometries where propagation patterns differ fundamentally from 2D monolayers (Hwang et al. 2023)

The opinion paper itself acknowledges in its Limitations section that applicability to 3D systems is not formally addressed.

**Recommended fix:** Add the qualifier *"propagating"* explicitly. Instead of *"the first positive FP peak reflects depolarization of neighboring cells"*, use *"the first positive peak in a **propagating** hiPSC-CM monolayer reflects depolarization of neighboring cells."* Making the scope explicit prevents misapplication to preparation types where the interpretation may not hold.

---

## Claim 2 — FPD end = baseline return, not the repolarization peak

**Verdict: The most challenged claim in the available literature; requires reframing — but the challenge is weaker than first stated once two caveats are made explicit.**

Ernault et al. (2024) used simultaneous FP and sharp-microelectrode AP recordings and found that the **T-wave peak time correlates with APD90** — but only when the T-wave is biphasic. APD90 is the established clinical target (the quantity the QT interval is meant to capture). If T-wave peak = APD90, then the conventional peak-based FPD definition is actually *better anchored to the validated electrophysiological endpoint* than the baseline-return definition.

**Two caveats that materially weaken this as a challenge to a hiPSC-CM-specific claim:**
1. **Species gap.** This correlation was established in **neonatal rat ventricular myocyte (NRVM)** monolayers, not hiPSC-CMs — Ernault's separate hiPSC-CM experiments (LEAP, Fig. 5A–C; Fig. 6 is a simulation) test a different question (local vs. spatially-averaged APD) and do not themselves validate T-peak↔APD90 in hiPSC-CMs. Mäki (2023) makes a claim specifically about hiPSC-CM FPD conventions, so this is indirect, cross-species evidence, not a direct empirical rebuttal.
2. **Prevalence.** Biphasic T-waves — the precondition for the correlation to hold at all — occurred in only a **minority** of the monolayers Ernault et al. recorded; the other monolayers often showed only a positive T wave that ended before the end of the action potential, which gave an unreliable assessment of local repolarization. So even setting the species gap aside, "T-peak is better anchored to APD90" holds only where a biphasic T wave is present, which was a minority of the recordings; elsewhere neither T-peak nor baseline-return was shown to be a validated APD90 surrogate.

The baseline-return definition measures something closer to APD95–100 (the very tail of repolarization). That is physiologically real — the repolarization tail matters for early afterdepolarization (EAD) risk — but it is **not** what the field has validated as the APD surrogate, and it will systematically inflate FPD relative to the clinical QT benchmark.

Weiser-Bitoun et al. (2026, PhysioMEA) and Lee et al. (2024, CardioMEA) both use R-to-T-peak operationally, whereas Dunham et al. (2022) use a T-wave endpoint from a fitted trapezoid and Mäki (2023) the baseline return (Table 2 in main.md), so the conventions remain diverse. Two platforms adopting the T peak does not by itself validate it as an APD90 surrogate: Lee et al. found R-to-T-peak FPD to correlate only minimally with APD50 and APD90 in iCell recordings.

**There is a defensible version of the argument**, but it needs to be reframed around what is actually being measured:

| Target | Better fiducial | Evidence |
|---|---|---|
| APD90 correspondence | T-wave peak (biphasic T-wave only — a minority morphology, and shown in NRVM not hiPSC-CM) | Ernault et al. 2024 |
| Full repolarization completion | Baseline return | Mäki 2023 (physiological reasoning) |

These are genuinely different quantities. The claim as written implies baseline return is simply more correct; the literature says it measures something *different*, not something better in all contexts. Independent support comes from a mechanical measurement: in simultaneous video and MEA recordings of iCell monolayers, Hayakawa et al. (2014) noted that the two FPD end points in use at the time (the peak of the positive deflection and the return of the positive deflection to baseline) appeared to match different phases of the relaxation motion (its upstroke and its peak) and that an accurate end point was difficult to establish.

**Recommended fix:** Instead of *"baseline return is more correct"*, use *"baseline return captures complete repolarization, distinct from the APD90-anchored T-peak convention; the choice depends on the quantity of interest."*

**One point where the literature strengthens the morphology argument:** Because biphasic T waves were found in only a minority of the monolayers in Ernault et al. (2024), the T-wave peak does *not* reliably indicate APD90 in many recordings either. In those cases, neither definition is validated as an APD90 surrogate — which supports the broader argument that waveform morphology must be assessed before any fiducial-point-based analysis is interpreted, and implies that a universally applicable, validated FPD-end convention for hiPSC-CMs largely remains an open problem rather than one resolved in T-peak's favor.

---

## Claim 3 — Pacemaker-like cells require different fiducial logic

**Verdict: Correct. The claim as actually stated in Mäki (2023) is unambiguous and logically necessary.**

The HTML paper states: *"FP-signals from pacemaker cells are different from signals generated by other cell types... they do not have the first high peak at all. Therefore, in this signal case, tdep and FPD should be analyzed as shown in Figure5."* The claim is simply that the standard depolarization-peak approach does not apply to pacemaker-like waveforms and a different method must be used.

This is unambiguously correct. You cannot apply peak-based depolarization detection to a waveform that has no pronounced initial peak. This is a logical necessity, not an empirical assertion.

The *existence* of pacemaker-like cells in hiPSC-CM cultures is supported in part: Ismaili et al. (2023) note If (HCN4) expression but call it debated whether ventricular-, atrial- and nodal-like cells form distinct subpopulations within one preparation, and patch-clamp data in Park et al. (2026) show about 9 % nodal-like cells in the normal lines. The methodological point — that these waveforms require different fiducial logic — follows directly.

**Note on what Mäki (2023) does NOT claim:** The language "frequently misclassified or excluded without justification" does not appear in the HTML source. That was an over-interpretation introduced in this wiki's initial summary. The paper makes a methodological prescription; it does not make an empirical claim about field-wide publication practice.

**Broader observation from the available literature:** Guerrelli et al. (2024) and Dunham et al. (2022) describe analysis frameworks without mentioning pacemaker-like morphology handling; Weiser-Bitoun et al. (2026) handle inverted T waves and low-amplitude R peaks via the inverted signal and exclude electrodes with inconsistent biomarker counts (p. 3) but do not describe pacemaker-like signals as such. This is consistent with the waveform type being excluded or filtered silently, though it is not directly documented.

---

## Claim 4 — "Only high peak" morphology is addressable by signal inversion before pacemaker-cell analysis

**Verdict: Credible internal observation that needs clearer mechanism framing and external validation. The core treatment step is stronger than it first appears.**

**On the physical mechanism:** The paper attributes this morphology to the distance between the dominant cell and the measurement electrode — at sufficient distance, the fast Na⁺-driven depolarization spike attenuates more rapidly than the slower repolarization current, so the electrode registers predominantly the repolarization phase as a dominant positive peak. This is physically coherent and consistent with standard extracellular recording theory.

*(Note: the paper text previously contained a typographic error — "distance between the dominant cell and the cell" — that obscured this explanation. This has been corrected in the HTML source to "distance between the dominant cell and the measurement electrode.")*

**On the inversion treatment:** Closer inspection of the figures confirms that the inverted "only high peak" signal (Fig. 8 flipped) is structurally similar to a genuine pacemaker-cell signal (Fig. 5): it shows the slow pre-depolarization drift followed by a trough that characterizes pacemaker waveforms. The assumption that inversion produces a pacemaker-like waveform is therefore not speculative — it is internally validated in the paper's own data. This substantially strengthens the claim compared to what can be inferred from text alone.

**What remains open:**

1. *Diagnosis disambiguation.* The paper describes one mechanism (electrode-cell distance), but in practice, other conditions can produce a dominant positive peak with no visible trough (e.g., very weak cell-electrode coupling). The reader has no guidance for distinguishing distance-attenuation cases — where inversion is appropriate — from cases where the electrode should simply be excluded as non-informative.

2. *External corroboration is largely absent.* No other paper in the wiki describes the "only high peak" waveform type or validates its inversion (Ernault 2024 and Dunham 2022 do not mention it). Weiser-Bitoun et al. (2026) do analyse an inverted signal for inverted T waves and low-amplitude R peaks (p. 3), a related but different case that shows the idea of analysing inverted signals outside the opinion paper without validating the "only high peak" case. The structural similarity between inverted Fig. 8 and Fig. 5 is an internal observation, not an independently reproduced result.

3. *Comparability of resulting FPD values.* It is not established whether FPD values derived from inverted only-high-peak signals are numerically comparable to FPD values from standard or pacemaker waveforms in the same recording.

**Recommended fix:** Retain the claim but add explicitly: (a) a statement that the physical basis is electrode-cell distance-dependent attenuation; (b) a practical criterion for when the morphology warrants inversion vs. electrode exclusion; (c) a note that the structural similarity after inversion is an empirical observation from the paper's own recordings that has not yet been independently replicated.

---

## Summary

| Claim | Verdict | Key challenge | Priority |
|---|---|---|---|
| 1. First positive peak = neighbor artifact | Holds; preparation-specific | Needs "propagating monolayer" qualifier; not valid for synchronous/3D preparations | Low — minor wording fix |
| 2. FPD end = baseline return | Partially challenged; weaker than first stated | Ernault 2024: T-peak = APD90 for biphasic T-waves, but shown in NRVM (not hiPSC-CM) and biphasic is a minority morphology; baseline return measures a different (not invalid) quantity | High — reframe as two distinct, both-incomplete targets |
| 3. Pacemaker cells need different analysis | Correct; logically necessary | "Frequently excluded" language was not in the paper — removed from wiki | Resolved — claim accurately restated |
| 4. Only-high-peak → inversion | Credible internal observation | Typographic error corrected; diagnosis criterion and external replication still needed (PhysioMEA uses a related inverted-signal branch for other cases) | Medium — criterion to be specified in future work |

---

## References consulted

- [[wiki/papers/ernault-2024-interpretation.md]] — T-wave peak correlates with APD90 for biphasic T-waves, but in NRVM (not hiPSC-CM) monolayers and only for a minority T-wave morphology (indirect, qualified challenge to Claim 2)
- [[wiki/papers/hwang-2023-spheroids.md]] — 3D geometry alters FP morphology and propagation (limits scope of Claim 1)
- [[wiki/papers/ismaili-2023-hamburg.md]] — If/ICa,T expression; the mixed-population question is debated (Claim 3)
- [[wiki/papers/guerrelli-2024-hipscm.md]] — Analysis pipeline without pacemaker morphology handling (consistent with Claim 3B by silence)
- [[wiki/papers/dunham-2022-cardiopyemea.md]] — Cardio PyMEA pipeline without pacemaker morphology handling (consistent with Claim 3B by silence)
- [[wiki/papers/weiser-bitoun-2026-physiomea.md]] — PhysioMEA uses R-to-T-peak (one convention among several, Claim 2) and an inverted-signal branch for inverted T waves and low R peaks (related to Claim 4); silent on pacemaker-like signals (Claim 3)
- [[wiki/papers/hayakawa-2014-motion-fp.md]] — two FPD end points appear to match different phases of the relaxation motion (supports the 'different quantities' reading of Claim 2)
- [[wiki/papers/park-2026-genotype-ml.md]] — patch-clamp proportions of ventricular-, atrial- and nodal-like cells in the normal lines (Claim 3)
