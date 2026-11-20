# Finnish summary
Lyhyesti: käsikirjoitus on rehellinen ja huolellisesti rajattu katsaus, joka nostaa esiin aitoja käytännön kysymyksiä kenttäpotentiaalien (FP) analyysistä, fidusiaaripisteistä ja kypsyysasteen vaikutuksesta hiPSC-kardiomyosyyttien MEA-mittauksissa.

Suurin heikkous on se, että katsaus rakentaa melko raskaan *"neljä aukkoa"* -rakenteen melko pienen, ei-systemaattisesti valitun aineiston varaan ja esittää yksittäisten tai rajallisten esimerkkien pohjalta välillä liian jyrkkiä yleistyksiä. Myös omat pohdinnat ja arviointikehikko (`Mäki, 2023` ja *DatAnalyzer*) näkyvät vahvasti, vaikka niiden rajoitukset onkin pyritty merkitsemään näkyviin.

Jos muotoilet "neljä aukkoa" hieman maltillisemmin ja tarkemmin aineiston rajoihin sitoen—sekä erotat selvemmin varsinaiset analyysimenetelmien puutteet ja solujen/laitteiston biologiset tai tekniset ominaisuudet—kokonaisuus kantaa huomattavasti vakuuttavammin.
# Full feeback
## Verdict

The review is transparent about its scope and limitations and raises real, practical questions about how MEA waveform conventions and maturation confounds affect comparability, but its central four-gap framing is overdrawn relative to the thin, non-systematic evidence base it surveys. The single most important thing to fix is to stop treating the absence of consensus or validation *within this small convenience sample* as proof of field-wide gaps (especially for rate correction and maturation staging), and to separate genuine analytical bottlenecks from broader biological or hardware issues.

## Findings

### 1. "No validated FPD rate correction" gap overstates what the reviewed set tested — major
**Where:** Abstract; Highlights; Section "Rate correction of field potential duration (FPDc)"; Conclusion, Gap 1 ("No validated FPD rate correction for hiPSC-CMs was found. The Fridericia formula, borrowed from clinical electrocardiography, lacks formal validation for the beating rate range and rate–FPD relationship of hiPSC-CM cultures.").
**Problem:** The text establishes that Fridericia correction is widely used in the reviewed papers and in CiPA, and cites one doxorubicin study where slowing rate caused FPDc to fall while raw FPD rose, plus two ML papers that did not test alternative rate corrections. Showing that a small, non-systematically chosen set of papers did not perform or compare rate-correction validation does not establish that no rate-correction evaluation or pacing/rate-adjustment approach exists in hiPSC-CM MEA work, nor does a single-drug slowing case prove that Fridericia fails generally.
**Suggestion:** Reframe Gap 1 around *inconsistent and unexamined rate-handling practices in the reviewed studies*—specifically that Fridericia is often applied by default without checking rate-dependence across wide beat-rate windows or testing sensitivity to correction choice—rather than declaring a blanket absence of validation across the field.

### 2. Gap 2 conflates waveform morphology classification with fiducial-point rules and overreaches on baseline-return — major
**Where:** Abstract; Section "Morphology-aware analysis and handling of heterogeneous FP waveforms"; Conclusion, Gap 2 ("Shared, validated criteria for classifying waveform morphology, and for choosing the fiducial definitions valid within each class, were not identified.").
**Problem:** Several of the cited papers are not actually trying to solve waveform morphology classification for FPD: Ernault et al. (2024) examines T-wave shape vs. APD90 in NRVMs, Weiser-Bitoun et al. (2026) focuses on beat rate/rhythm and 2D heatmaps, and Kim et al. (2026) reports a scoop-shaped organoid MEA without defining FPD. Moreover, the review repeatedly treats the author's own `DatAnalyzer` baseline-return convention (Mäki, 2023) as a benchmark against which T-wave peak or trapezoid endpoints are found wanting, even while noting that baseline-return was not compared against the AP and lacks noise/drift robustness testing.
**Suggestion:** Narrow Gap 2 to what the reviewed studies actually show—that open tools and studies use differing, often unstated waveform and fiducial assumptions without side-by-side comparison—and avoid implying that baseline-return is a validated standard that other tools fail to match.

### 3. Gap 3 bundles 3D geometry, device contact, and high-density spatial mapping into one "validation" gap — moderate
**Where:** Abstract; Highlights; Section "Three-dimensional cardiomyocyte models"; Conclusion, Gap 3 ("Dedicated validation of 2D-calibrated analysis frameworks was not found for either 3D tissues or spatially resolved recordings, two settings that pose different problems.").
**Problem:** Even the review's own text admits these are "two settings that pose different problems," and several cited problems are physical/hardware or biological rather than failures of "2D-calibrated analysis frameworks": Maurissen et al. (2024) actually found similar FPDc between 2D and 3D sheets, Hwang et al. (2023) is a simulation of electrode/stimulation position, Lin et al. (2023) is about single-sided contact/detachment in 3D microtissues, and Matsuda et al. (2025) introduces new spatial endpoints rather than misapplying a 2D FPD formula.
**Suggestion:** Split or sharpen the point so it distinguishes (a) *measurement/coupling and geometry limits* in 3D and high-density recordings from (b) *untested transfer of specific 2D metrics* (such as local FPD or conduction metrics) across 3D constructs and dense arrays.

### 4. Gap 4 ("no MEA-derived reference values for maturation") is partly self-undermined and partly outside MEA scope — moderate
**Where:** Section "Maturation status as an unresolved confound for MEA-derived metrics"; Conclusion, Gap 4 ("hiPSC-CM maturation status lacks MEA-derived reference values... Because functional, metabolic and transcriptional maturation are induced largely independently (Fetterman et al., 2024), such a benchmark could only cover the electrophysiological axis.").
**Problem:** First, the review argues that maturation is multidimensional and largely independent across functional, metabolic, and transcriptional axes, which makes a single "maturation status" reference value conceptually fragile even on MEA. Second, showing that culture duration, media, pacing, or spike amplitude/conduction velocity change across conditions (Guerrelli et al., 2024; Li et al., 2024; Li et al., 2025) does not show that MEA analysis methods themselves are flawed—only that biological maturity varies and is rarely anchored to an independent maturity assay in the same wells.
**Suggestion:** Frame this as a *reporting and confounding issue* (maturation state is rarely measured independently alongside MEA readouts, complicating cross-study comparisons) rather than a missing "MEA reference value" for overall maturation.

### 5. "None of them applies two analysis conventions to the same recordings" is an overgeneralisation from a non-systematic subset — moderate
**Where:** Introduction ("Motivation: why analysis methods matter"): "The studies reviewed below show that conventions differ and that FPD does not always track the action potential. None of them applies two analysis conventions to the same recordings and reports how much the results differ."
**Problem:** Because the selection of papers is non-systematic, AI-assisted, and explicitly small, saying *"None of them"* can overread as a statement about the literature rather than strictly about the handful of papers included here.
**Suggestion:** Qualify the sentence explicitly to the reviewed papers—e.g., *"Among the studies reviewed here, none applies two FPD analysis conventions to the same recordings to quantify how much the resulting values or conclusions diverge."*

### 6. Over-strong phrasing on "unvalidated" and "small datasets" in ML/modeling claims — minor
**Where:** Section "Rate correction of field potential duration (FPDc)" ("Both evaluated their models on small test sets of 15–16 drugs by repeated resampling."); Discussion ("The forward model of Botti et al. (2026) is the closest existing component among the studies examined, but it was not fitted to new measurements.").
**Problem:** Saying a forward model "was not fitted to new measurements" can sound like a criticism when forward/bidomain models are typically parameterized from biophysical/electrophysiological models and compared against experimental observations rather than "fitted" to a single new dataset; similarly, noting 15–16 drugs in ML evaluation is useful context, provided it is not framed as inherently invalidating without stating why that size limits generalizability (e.g., chemical/mechanistic diversity and resampling leakage risk).
**Suggestion:** State plainly what Botti et al. (2026) did and did not do (forward simulation of tissue–electrode coupling rather than inverse parameter fitting to experimental recordings), and briefly state the specific limitation of small compound sets (limited drug diversity and potential optimism under resampling).

### 7. Argument arc: "Four Gaps" title vs. "Two Hypotheses" outlook does not fully close the loop — minor
**Where:** Title; Abstract; Section "Discussion and future outlook"; Section "Conclusion".
**Problem:** The review is titled around *four gaps limiting comparability*, and the Conclusion revisits those four gaps, yet the Discussion pivots to two broad personal hypotheses (multimodal sensor fusion and inverse "digital twin" separation of device/tissue/AP) that go well beyond fixing FPD rate correction, morphology rules, 3D/HD-MEA validation, or maturation reporting. That shift is clearly flagged as speculative, which helps, but the transition feels slightly abrupt relative to the four-gap structure.
**Suggestion:** Add one brief bridging sentence at the start of "Discussion and future outlook" explaining how sensor fusion and signal decomposition relate to—or leapfrog past—the four comparability gaps rather than solving them directly.

### 8. Minor internal tension between treating FPD conventions as a core comparability blocker vs. noting alternative views — minor
**Where:** Section "Motivation: why analysis methods matter"; Section "Limitations of this review", point (iv); Section "Conclusion".
**Problem:** Point (iv) of Limitations commendably cites Vuorenpää et al. (2023) to note that parametrization of APs and FPs is often treated as well established and enabling comparison across studies, whereas the Title, Highlights, and Conclusion present differing fiducial conventions as a central barrier to comparability.
**Suggestion:** Keep the tension visible, and make sure the Conclusion reflects the modest weight of evidence for how much fiducial differences actually alter biological or pharmacological conclusions across studies.

## Suggested references (if any)

| Work (authors, year, title, venue) | DOI | How verified | Which sentence it affects | Why it matters |
|---|---|---|---|---|
| *None suggested* | — | — | — | No additional external paper is needed to fix the core scoping and overreach issues identified above, and I will not supply unverified citations. |

## What I checked and could not fault

- **Transparency on AI assistance, authorship, and competing interests:** The Scope, Limitations, About the author, and Declarations sections are unusually candid about single-author drafting, non-systematic selection, LLM assistance, and the author's prior work (`Mäki, 2023` and `DatAnalyzer`).
- **Distinction between empirical findings and speculative hypotheses:** The review consistently labels the author's proposals in "Discussion and future outlook" and "Personal note" as hypotheses or personal views rather than results of the reviewed papers.
- **Careful handling of non-hiPSC-CM and non-MEA evidence:** Where papers use NRVMs (Ernault et al., 2024), fetal mouse cells (Hu et al., 2026), simulations (Hwang et al., 2023; Botti et al., 2026), or embedded electrodes (Lin et al., 2023), the text generally flags those model/modality boundaries when introducing them.
- **Mermaid diagrams as visual aids:** Figure 1 and Figure 2 are clear structural overviews that match the prose they accompany (with the caveat in Finding 2 regarding `DatAnalyzer` / waveform classification scope).

# Our response

Written 2026-11-20, after every finding was checked against the text.

**Three changes made.**

- **Finding 1, gap 1.** The heading was already hedged ("was found"); the sentence under it was not. It now attributes and dates the claim: the CiPA authors noted in 2018 that Fridericia had not been thoroughly validated for hiPSC-CMs (Blinova et al., 2018), and nothing validating it since then was found among the studies examined. The review's register already required this — it records that no documented search lies behind gap 1, unlike gap 4 — so the old present-tense wording was out of step with its own rules.
- **Finding 5.** "None of them applies two analysis conventions ..." is now "None of the studies reviewed below ...".
- **Finding 7.** The Discussion opens with a sentence saying that neither hypothesis solves the four gaps, and what they address instead.

**Four findings declined, because the text already does what they ask.**

- **2.** That Ernault, Weiser-Bitoun and Kim are not trying to solve morphology classification *is* the finding, not a conflation. On baseline return: the fiducial section says the two definitions "may therefore measure different quantities rather than one being universally more correct", Table 2 and Figure 2 state the convention as intended rather than demonstrated, and Limitations (iv) calls it one of several in use.
- **3.** The split between coupling and geometry limits on one side and untested transfer of 2D metrics on the other is already written out in gap 3's own paragraph; only the bold heading is short.
- **4.** The suggested reframing — maturity rarely measured independently in the same wells — is the text's own wording, as is the limit to the electrophysiological axis.
- **8.** Limitations (iv) keeps the tension with Vuorenpää et al. (2023) visible, which is what the finding asks for.

Finding 6 is left for the language pass.

**The reframings of gaps 1–4 were not taken.** Recasting them as "practices vary" would claim less than the material supports and, for gap 1, less than the CiPA authors wrote themselves. The headline criticism — that the sample's silences are presented as field-wide gaps — is answered by wording already in place: the Abstract scopes all four gaps to "the studies examined", three of the four headings are stated as findings of this review, and the fourth is the one with a documented search behind it.

Two reviews now push the same way. That is a reason to watch for over-hedging, not to keep hedging.
