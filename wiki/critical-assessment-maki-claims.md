# Critical assessment: key methodological claims in Mäki (2023)

**Date:** 2026-06-22  
**Question:** Do the four central methodological claims in [[wiki/papers/maki-2023-opinion.md]] hold up against the post-2022 literature in this wiki?

Claims assessed:
1. The first positive FP peak reflects depolarization of *neighboring* cells, not the locally recorded cell — it should not be used as the FPD start.
2. FPD end should be defined as the return to baseline, not the repolarization peak.
3. Pacemaker-like cells (no high peak) require different fiducial logic and are frequently misclassified or excluded without justification in published studies.
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

**Verdict: The most challenged claim in the available literature; requires reframing.**

Ernault et al. (2024) used simultaneous FP and sharp-microelectrode AP recordings and found that the **T-wave peak time correlates with APD90** — but only when the T-wave is biphasic. APD90 is the established clinical target (the quantity the QT interval is meant to capture). If T-wave peak = APD90, then the conventional peak-based FPD definition is actually *better anchored to the validated electrophysiological endpoint* than the baseline-return definition.

The baseline-return definition measures something closer to APD95–100 (the very tail of repolarization). That is physiologically real — the repolarization tail matters for early afterdepolarization (EAD) risk — but it is **not** what the field has validated as the APD surrogate, and it will systematically inflate FPD relative to the clinical QT benchmark.

Weiser-Bitoun et al. (2026, PhysioMEA) adopting R-to-T-peak operationally is a second data point: the field is converging on T-peak as standard, consistent with Ernault's APD90 finding.

**There is a defensible version of the argument**, but it needs to be reframed around what is actually being measured:

| Target | Better fiducial | Evidence |
|---|---|---|
| APD90 correspondence | T-wave peak (biphasic T-wave only) | Ernault et al. 2024 |
| Full repolarization completion | Baseline return | Mäki 2023 (physiological reasoning) |

These are genuinely different quantities. The claim as written implies baseline return is simply more correct; the literature says it measures something *different*, not something better in all contexts.

**Recommended fix:** Instead of *"baseline return is more correct"*, use *"baseline return captures complete repolarization, distinct from the APD90-anchored T-peak convention; the choice depends on the quantity of interest."*

**One point where the literature strengthens the morphology argument:** For non-biphasic T-waves, Ernault et al. (2024) show that T-wave peak does *not* reliably indicate APD90 either. In those cases, neither definition is validated as an APD90 surrogate — which supports the broader argument that waveform morphology must be assessed before any fiducial-point-based analysis is interpreted.

---

## Claim 3 — Pacemaker-like cells are frequently misclassified or excluded without justification

**Verdict: Two separable sub-claims with very different evidence bases.**

**Part A — "Different fiducial logic is required":** Unambiguously correct. You cannot apply peak-based depolarization detection to a waveform that has no pronounced initial peak. This is a logical necessity.

**Part B — "Frequently misclassified or excluded without justification":** Plausible inference from publication practice, but asserted rather than evidenced. The *existence* of pacemaker-like cells in hiPSC-CM cultures is well-supported — Ismaili et al. (2023) explicitly notes If and ICa,T expression and the coexistence of nodal-like subtypes in typical preparations. But "frequently excluded without justification" is an empirical claim about what published studies *do*, which would require a systematic survey of methods sections to verify. None of the available papers provide that evidence.

What the available literature does provide is silence: Guerrelli et al. (2024), Dunham et al. (2022), Weiser-Bitoun et al. (2026), and other tool/methods papers all describe analysis frameworks without mentioning pacemaker-like morphology handling. This is *consistent with* the claim — if the waveform type is simply filtered out by vendor beat-detection thresholds without being reported — but consistent-with is not the same as direct evidence.

**Recommended fix:** The word *frequently* is doing unverified work. Instead of *"frequently misclassified or excluded without justification"*, use: *"Pacemaker-like morphologies arise in hiPSC-CM preparations due to the coexistence of nodal-like subtypes (Ismaili et al. 2023), yet most published analysis pipelines do not describe how these waveforms are handled, creating an undisclosed source of inter-study variability."* That formulation is fully evidenced.

---

## Claim 4 — "Only high peak" morphology is addressable by signal inversion before pacemaker-cell analysis

**Verdict: Credible internal observation that needs clearer mechanism framing and external validation. The core treatment step is stronger than it first appears.**

**On the physical mechanism:** The paper attributes this morphology to the distance between the dominant cell and the measurement electrode — at sufficient distance, the fast Na⁺-driven depolarization spike attenuates more rapidly than the slower repolarization current, so the electrode registers predominantly the repolarization phase as a dominant positive peak. This is physically coherent and consistent with standard extracellular recording theory.

*(Note: the paper text contains a typographic error — "distance between the dominant cell and the cell" — that obscures this explanation. The correct reading is "distance between the dominant cell and the measurement electrode.")*

**On the inversion treatment:** Closer inspection of the figures confirms that the inverted "only high peak" signal (Fig. 8 flipped) is structurally similar to a genuine pacemaker-cell signal (Fig. 5): it shows the slow pre-depolarization drift followed by a trough that characterizes pacemaker waveforms. The assumption that inversion produces a pacemaker-like waveform is therefore not speculative — it is internally validated in the paper's own data. This substantially strengthens the claim compared to what can be inferred from text alone.

**What remains open:**

1. *Diagnosis disambiguation.* The paper describes one mechanism (electrode-cell distance), but in practice, other conditions can produce a dominant positive peak with no visible trough (e.g., very weak cell-electrode coupling). The reader has no guidance for distinguishing distance-attenuation cases — where inversion is appropriate — from cases where the electrode should simply be excluded as non-informative.

2. *External corroboration is absent.* No other paper in the available literature (including Ernault 2024, Dunham 2022, Weiser-Bitoun 2026) describes this waveform type or validates the inversion approach. The structural similarity between inverted Fig. 8 and Fig. 5 is an internal observation, not an independently reproduced result.

3. *Comparability of resulting FPD values.* It is not established whether FPD values derived from inverted only-high-peak signals are numerically comparable to FPD values from standard or pacemaker waveforms in the same recording.

**Recommended fix:** Retain the claim but add explicitly: (a) a statement that the physical basis is electrode-cell distance-dependent attenuation; (b) a practical criterion for when the morphology warrants inversion vs. electrode exclusion; (c) a note that the structural similarity after inversion is an empirical observation from the paper's own recordings that has not yet been independently replicated.

---

## Summary

| Claim | Verdict | Key challenge | Priority |
|---|---|---|---|
| 1. First positive peak = neighbor artifact | Holds; preparation-specific | Needs "propagating monolayer" qualifier; not valid for synchronous/3D preparations | Low — minor wording fix |
| 2. FPD end = baseline return | Challenged by literature | Ernault 2024: T-peak = APD90 for biphasic T-waves; baseline return measures a different (not invalid) quantity | High — reframe as two distinct targets |
| 3. Pacemaker cells frequently excluded | Part A correct; Part B asserted | "Frequently" unquantified; "misclassified" undemonstrated | Medium — reword without the frequency claim |
| 4. Only-high-peak → inversion | Credible internal observation | Mechanism framing needs typographic fix; needs diagnosis criterion and external replication | Medium — strengthen with explicit criteria |

---

## References consulted

- [[wiki/papers/ernault-2024-interpretation.md]] — T-wave peak correlates with APD90 for biphasic T-waves (direct empirical challenge to Claim 2)
- [[wiki/papers/hwang-2023-spheroids.md]] — 3D geometry alters FP morphology and propagation (limits scope of Claim 1)
- [[wiki/papers/ismaili-2023-hamburg.md]] — If/ICa,T expression and nodal-like subtypes (supports existence of pacemaker-like cells, Claim 3)
- [[wiki/papers/guerrelli-2024-hipscm.md]] — Analysis pipeline without pacemaker morphology handling (consistent with Claim 3B by silence)
- [[wiki/papers/dunham-2022-cardiopyemea.md]] — Cardio PyMEA pipeline without pacemaker morphology handling (consistent with Claim 3B by silence)
- [[wiki/papers/weiser-bitoun-2026-physiomea.md]] — PhysioMEA adopts R-to-T-peak (field convergence against Claim 2; silent on Claims 3 and 4)
