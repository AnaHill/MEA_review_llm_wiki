Feedback from AI (chatGPT free version), 2026-11-20
## Finnish short version
Pidin käsikirjoitusta kokonaisuutena onnistuneena, asiantuntevana ja johdonmukaisena narratiivisena katsauksena. Sen vahvuus on, että se ei ainoastaan luettele MEA-menetelmiä, vaan pyrkii jäsentämään, miksi mittaustulosten fysiologinen tulkinta, fidusiaaliset pisteet, syketaajuuden korjaus ja solujen kypsyys ovat edelleen ongelmallisia. Neljän tutkimusaukon kokonaisuus on pääosin perusteltu, ja tekstin rajaukset sekä kirjoittajan oma näkökulma on tuotu avoimesti esiin.

Suurimmat korjaustarpeet liittyvät muutamaan kohtaan, joissa tulkinta menee näyttöä pidemmälle. Erityisesti T-aallon huipun rinnastaminen APD90:een on liian vahva väite, ja lähtötasoon palaamista ei pitäisi esittää automaattisesti täydellisen repolarisaation mittana. Lisäksi 3D-MEA-menetelmistä on tullut uutta merkittävää tutkimusta vuosina 2025–2026, mikä kannattaa huomioida ja samalla täsmentää, mitä 3D-mittausten validoinnissa oikeastaan vielä puuttuu.

En siis pitäisi käsikirjoituksen perusajatusta tai rakennetta uudistamista vaativana. Kyse on pikemminkin muutamien väitteiden täsmentämisestä ja ajantasaisuuden parantamisesta. Näillä korjauksilla tekstistä voisi tulla vakuuttava ja hyödyllinen katsaus, jossa sen keskeinen argumentti säilyy ennallaan.


**## Verdict**

The review is substantially sound, unusually careful about distinguishing evidence from the author's hypotheses, and its central argument carries. The four gaps are mostly defensible, although the third combines two technically different problems, and the second needs a clearer distinction between waveform morphology classification and fiducial-point selection.

The most important corrections are to avoid treating the conditional association between T-wave peak and APD90 as validation of an APD90 surrogate, and to incorporate two directly relevant 2025–2026 developments in three-dimensional MEA technology. There are also two places where the wording implies more physiological certainty than the evidence warrants. I would make these changes before posting, but I would not restructure the review.

**## Findings**

**### 1. The T-wave peak is not established as an APD90 surrogate — major**

**Where:** Section "Explicit and physiologically motivated fiducial definitions", sentence:

"This anchors the T-wave peak, when the waveform is biphasic, to APD90."

Also Figure 2, node K:

"APD90 surrogate if biphasic T wave."

**Problem:** Ernault et al. (2024) report a strong correlation between T-wave peak timing and APD90 in NRVM monolayers with biphasic T waves. Correlation does not establish equivalence, interchangeability or the validity of using T-wave peak as an APD90 surrogate. Furthermore, the result is conditional on a morphology found in only a minority of monolayers and comes from rat rather than human cells.

The review correctly reports these qualifications in the surrounding text, but the phrase "anchors ... to APD90" and especially the figure's "APD90 surrogate" make the result sound stronger than it is.

**Suggestion:** Replace the sentence with:

"Ernault et al. (2024) found a strong correlation between T-wave peak timing and APD90 in NRVM monolayers, but only when the T wave was biphasic, a morphology present in a minority of recorded monolayers. This provides conditional evidence for a relationship between the two measurements, not validation of the T-wave peak as a general APD90 surrogate."

In Figure 2, replace "APD90 surrogate if biphasic T wave" with:

"Correlates with APD90 in biphasic T waves (NRVM; Ernault et al., 2024)."

This is particularly important because the physiological interpretation of the FPD end point is one of the review's central arguments.

**### 2. Two important developments in 3D MEA recording are missing — major**

**Where:** Section "Three-dimensional cardiomyocyte models", particularly:

"No study examined here compared fiducial definitions between 2D and 3D recordings systematically."

And Conclusion, gap 3:

"The transfer of 2D-calibrated analysis frameworks to 3D models and ultra-high-density platforms proceeds empirically."

**Problem:** Two directly relevant publications appeared before the review's stated literature-search cutoff of 30 October 2026.

The first presents a shell-shaped MEA that encapsulates cardiac organoids and enables three-dimensional electrophysiological mapping. It produces 3D isochrone and conduction-velocity maps and uses calcium imaging to corroborate electrophysiological findings. This is a significant development beyond planar organoid recordings.

The second presents a conformable MEA integrated into a scoop-shaped slide-well for patient-derived hiPSC-CM cardiac organoids. It resolves region-specific extracellular field potentials, validates these against calcium imaging, and demonstrates disease-associated waveform morphology and drug responses.

Neither paper establishes universally validated FPD fiducial definitions. However, both materially change the discussion of how far 3D and spatially resolved MEA analysis has progressed.

**Suggestion:** Add both to the 3D section and distinguish acquisition validation from analytical validation. In particular, the new studies show that spatially resolved 3D recording and independent corroboration are already possible. The remaining problem is not simply a lack of 3D analysis frameworks, but the lack of validation and standardisation of the physiological interpretation and quantitative analysis of their outputs.

Suggested replacement for the concluding sentence of the 3D section:

"Recent conformable and shell-shaped MEA platforms have advanced three-dimensional electrophysiological mapping and provided independent corroboration through calcium imaging (Choi et al., 2026; Kim et al., 2026). However, this does not yet establish the transferability of conventional FPD fiducial definitions or the comparability of quantitative conduction and repolarization metrics across different 2D and 3D recording geometries."

The two references are detailed below.

**### 3. Fridericia correction at extreme rates: the physiological concern is reasonable, but the evidence is not demonstrated — moderate**

**Where:** Section "Rate correction of field potential duration (FPDc)":

"Furthermore, a fixed cube-root correction cannot be assumed to hold across the wide range of spontaneous rates of hiPSC-CMs, which are accepted at 20–90 bpm in the multisite CiPA study (Blinova et al., 2018) and 20–80 bpm in a proposed acceptance standard (Clements et al., 2025), so the formula may under- or over-correct at the extremes of this range."

**Problem:** The cited rate ranges establish that the assays accommodate widely differing spontaneous rates. They do not establish that Fridericia systematically undercorrects or overcorrects at the extremes.

The distinction matters because the review's central claim is the absence of a validated correction formula, not that Fridericia has already been demonstrated to fail at particular rates.

There is also a small technical ambiguity in the equation:

"FPDc = FPD/RR^0.33"

The units of RR should be specified. The conventional Fridericia calculation uses RR in seconds. Without this qualification, the equation is dimensionally ambiguous when FPD is expressed in milliseconds.

**Suggestion:** Replace the sentence with:

"Because hiPSC-CM assays accommodate a wide range of spontaneous beating rates, it remains uncertain whether a fixed cube-root correction adequately describes the rate–FPD relationship across the full range. Whether Fridericia systematically under- or over-corrects at particular rates requires direct experimental evaluation."

Specify RR in seconds in the equation.

I would retain the doxorubicin example from Lee et al. (2026). It is a much stronger illustration of why rate correction matters in practice: corrected and uncorrected FPD changed in opposite directions.

**### 4. Baseline return is presented as full repolarization without sufficient physiological qualification — moderate**

**Where:** Figure 2, node L:

"Full repolarization — Mäki, 2023."

Section "Explicit and physiologically motivated fiducial definitions", sentence:

"definition of FPD end as the return of the signal toward baseline rather than the repolarization peak."

And Table 2:

"Intended to capture the full repolarization wave (Mäki, 2023)."

**Problem:** The review itself establishes that extracellular field potentials are not direct recordings of membrane potential and that their morphology depends on cell–electrode coupling, tissue geometry and the activity of surrounding cells.

Consequently, the return of an extracellular signal to baseline is not necessarily equivalent to complete repolarization of the underlying cardiomyocytes.

This is particularly important because the review proposes baseline return as a physiologically preferable alternative to T-wave peak, while acknowledging that the convention has not been compared with intracellular action potentials.

The author's proposal is reasonable, but the diagram makes it look like an established physiological interpretation.

**Suggestion:** Change the figure node to:

"Baseline return — intended to capture the complete extracellular repolarization wave (Mäki, 2023)."

Change the Table 2 description to:

"Proposed to capture the full extracellular repolarization wave; correspondence with AP repolarization has not been established."

This preserves the author's argument without presenting the proposed relationship as demonstrated.

**### 5. The third methodological gap combines two different validation problems — moderate**

**Where:** Conclusion, gap 3:

"The transfer of 2D-calibrated analysis frameworks to 3D models and ultra-high-density platforms proceeds empirically."

**Problem:** Three-dimensional tissue geometry and ultra-high-density spatial recording are related but not equivalent methodological problems.

In 3D tissues, relevant complications include:
- Electrode–tissue contact and coupling.
- Depth-dependent signal contributions.
- Spatially heterogeneous activation and propagation.
- Differences between surface recordings and tissue-embedded recordings.

In ultra-high-density planar arrays, the principal additional issues include:
- Spatial sampling resolution.
- Local activation-time estimation.
- Propagation mapping and conduction-velocity calculation.
- Interpretation of spatially varying waveform morphology.

A method validated for 3D organoids is not necessarily validated for ultra-high-density planar recording, and vice versa.

The review already presents these topics separately in its body. Grouping them into one gap obscures what actually needs validation.

**Suggestion:** Keep four overarching gaps, but describe the third as two related validation needs:

"Dedicated validation of analysis methods in non-planar three-dimensional tissues and spatially resolved MEA recordings remains limited. These settings present different challenges: three-dimensional tissue geometry changes electrode contact and signal contributions, whereas high-density spatial recordings require validation of local activation and propagation metrics."

This also makes the gap more actionable.

**### 6. Morphology classification and fiducial definition are not quite the same methodological problem — minor**

**Where:** Conclusion, gap 2:

"Shared, validated waveform morphology classification criteria were not identified."

**Problem:** The review brings together three related but distinct operations:

1. Classifying waveform morphology.
2. Deciding which fiducial points are meaningful for a given morphology.
3. Deciding whether a particular electrode should be excluded.

These operations are related, but a shared classification scheme does not automatically establish a valid FPD measurement for each class.

For example, even if two laboratories agree that a waveform is biphasic, they still need to agree on which peak or endpoint to measure and how that measurement relates to the action potential.

The review's Figure 2 actually makes this distinction quite well: morphology classification precedes FPD measurement, followed by selection of the FPD end convention.

**Suggestion:** Retain the gap, but explicitly state that it concerns both classification and the mapping of waveform classes to valid analysis procedures.

A possible formulation:

"Shared, validated criteria for waveform morphology classification and for selecting appropriate fiducial definitions within each morphological class have not been established."

This would make the gap more precise and better align the conclusion with Figure 2.

---

**## Suggested references (if any)**

| Work (authors, year, title, venue) | DOI | How verified | Which sentence it affects | Why it matters |
|---|---|---|---|---|
| Choi, S. J., Liu, Z., Yang, F., Wang, H., George, D., Gracias, D. H., & Kim, D.-H. (2026). 3D Spatiotemporal Electrophysiology of Cardiac Organoids Using Shell Microelectrode Arrays. *Advanced Materials*, 38(2), e06793. | 10.1002/adma.202506793 | Retrieved and checked against the indexed PubMed record and Wiley publisher record. | Section "Three-dimensional cardiomyocyte models": "No study examined here compared fiducial definitions between 2D and 3D recordings systematically." | Demonstrates 3D organoid-encapsulating MEAs, spatial mapping and calcium-based corroboration. Does not resolve the validation of FPD fiducial definitions. |
| Kim, Y. S., Jeong, J., Heo, G., Kwon, Y. W., Lee, J., Jeong, Y. J., Park, G. T., Jeong, S., Hwang, K. W., Choi, M., Shin, J., Hong, S. W., & Kim, J. H. (2026). Conformable Microelectrode Arrays Integrated with a Scoop-Shaped Slide-Well for Dynamic Electrophysiological Profiling of Patient-Derived Cardiac Organoids. *Advanced Science*, 13(31), e14365. | 10.1002/advs.202514365 | Retrieved and checked against the indexed PubMed record and Wiley publisher record. | Section "Three-dimensional cardiomyocyte models", particularly the discussion of spatially heterogeneous recordings and the limitations of conventional MEAs. | Demonstrates region-specific EFP waveforms in patient-derived hiPSC-CM organoids, corroborated by calcium imaging. Particularly relevant because it is explicitly based on human iPSC-derived cardiac organoids. |

Both references are genuine publications, not reconstructed citations. Their publication dates are within the review's stated coverage period.

I would not add a long list of further papers merely to increase the reference count. These two are sufficient to make a material difference to the discussion of the third gap.

---

**## What I checked and could not fault**

- **Overall argument:** The Introduction establishes why analysis conventions matter, and the Conclusion returns to the same problem through four identifiable methodological gaps. The argument does not lose its direction.
- **Rate correction:** The review correctly distinguishes the widespread use of Fridericia correction from its formal validation for hiPSC-CMs. The discussion of pacing is also appropriately nuanced: pacing removes spontaneous rate variation during measurement but does not resolve every experimental comparability issue.
- **Maturation:** The distinction between electrophysiological maturation and overall cellular maturation is important and correctly handled. Fetterman et al. (2024) provide a particularly useful reason not to treat maturation as a single scalar quantity. The review also correctly distinguishes assay acceptance criteria from maturation reference values.
- **The four gaps:** They are genuinely different questions. Rate correction concerns mathematical normalisation; morphology concerns signal interpretation; 3D/spatial analysis concerns the transferability of measurement and analysis methods; maturation concerns biological comparability. They interact but should not be collapsed into one problem.
- **The maturation gap:** The argument that an MEA-derived reference should be validated against an independent maturity measure on the same cultures is sound. The review also appropriately recognises that such a reference could describe electrophysiological maturation without describing overall cellular maturity.
- **The morphology section:** The distinction between waveform polarity, waveform shape and fiducial-point placement is valuable. The discussion of signal inversion is appropriately cautious about independent validation.
- **The 3D section:** The distinction between the effects of geometry on recorded signals and the limitations of electrode–tissue contact is useful. The review does not incorrectly claim that 3D FPD cannot be measured; Maurissen et al. (2024) provide an important counterexample.
- **High-throughput and chronic assays:** This section contributes something beyond a catalogue of hardware developments. The discussion of equilibration, culture-time drift and vehicle-control variation reinforces the central argument that analysis cannot be interpreted independently of experimental conditions.
- **Machine learning:** The concern that models may learn differences in analytical conventions rather than biological differences follows logically from the preceding sections. The author also correctly avoids presenting the small classifier studies as evidence of generalisable predictive performance.
- **Discussion and future outlook:** The two speculative directions, sensor fusion and separation of recording-system contributions from cellular signals, are recognisably extensions of the earlier methodological argument. They are not presented as established findings.
- **Figure 1:** The timeline is consistent with the broad development described in the review. It does not need to be interpreted as a comprehensive chronology.
- **Figure 2:** The proposed sequence of beat detection, averaging, morphology classification, fiducial selection and rate correction is internally coherent. The figure appropriately identifies the signal-inversion branch as the author's own proposal.
- **Limitations and declarations:** The author identifies the relevant conflicts of interest, distinguishes the opinion paper from peer-reviewed evidence, and makes the speculative status of the Discussion explicit. These disclosures are proportionate to the project.
- **Personal note:** Although it revisits the FPD endpoint argument, it adds a useful account of the author's reasoning and does not introduce an inconsistency with the scientific sections.

**Overall recommendation:** Make findings 1–5 the priority, incorporate the two missing 3D publications, and retain the rest of the manuscript substantially as it is. The review has a defensible central thesis and does not need a larger or more elaborate structure to become a useful preprint.