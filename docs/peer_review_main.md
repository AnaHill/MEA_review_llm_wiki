# Academic Peer Review Report

> **Simulated AI review / simuloitu tekoälyarvio.** This report is a simulated review produced by an AI model, not a review by a journal or by real reviewers. The reviewer was not told that the manuscript is a preprint that will not go through peer review, and the line numbers do not match the current `main.md`. The author's assessment of the report is at the end of this file (heading "Kirjoittajan arvio tästä raportista").
>
> Tämä raportti on tekoälyn tuottama simuloitu arvio, ei lehden eikä oikeiden arvioijien tekemä. Arvioijalle ei kerrottu, että teksti on preprint, joka ei kulje vertaisarvioinnin kautta, eivätkä rivinumerot vastaa nykyistä `main.md`:tä. Kirjoittajan arvio raportista on tiedoston lopussa.

**Manuscript Title:** Charting the Field: Cardiomyocyte MEA Analysis Evolution Since 2022  
**Author:** Antti-Juhana Mäki (Independent researcher)  
**Target File Reviewed:** main.md  
**Reviewer Role:** Academic Peer Reviewer  
**Overall Recommendation:** Rejection in Current Form / Major Revision Required



## 1. Executive Summary & Review Overview

This narrative review surveys developments in microelectrode array (MEA) field potential (FP) analysis methodology for human induced pluripotent stem cell-derived cardiomyocytes (hiPSC-CMs) from 2022 to mid-2026. The manuscript addresses a highly relevant topic in cardiac safety pharmacology, safety screening, and disease modeling, focusing on open analysis platforms, fiducial point definitions, rate correction, maturation confounders, 3D/high-density models, and machine learning integration.



While the topic is timely and important, the manuscript suffers from critical methodological flaws, severe self-citation bias, circular evaluative logic, biophysically questionable signal processing recommendations, unverified core assumptions, and significant manuscript hygiene issues (including unremoved internal editorial/prompt comments). 

Most notably, the author uses their own un-peer-reviewed Zenodo opinion paper (Mäki, 2023) as the central evaluative framework and anchor to judge published, peer-reviewed literature. Furthermore, several signal-processing recommendations (such as arbitrary waveform inversion) lack biophysical validation and risk distorting electrophysiological data.



## 2. Major Methodological & Scientific Flaws

### 2.1. Circular Evaluative Framework & Self-Citation Bias
* Lines 14, 27, 29, 39, 65, 79, 134, 147
* Issue: The author evaluates post-2022 literature using their own un-peer-reviewed report (Mäki, 2023, published on Zenodo) as the reference gold standard.
* Critique: A scientific review paper must evaluate literature against established, consensus-driven international guidelines (e.g., CiPA protocols, HESI/SPS standards) or verified biophysical principles, not an author's own unvalidated opinion paper. Elevating one's own non-peer-reviewed Zenodo preprint to an evaluative anchor introduces severe confirmation bias and circular reasoning.



### 2.2. Non-Systematic Search Protocol & Selection Bias
* Lines 28-29, 134
* Issue: The review explicitly acknowledges that search statistics, databases queried, numbers of screened records, and inclusion/exclusion criteria were not recorded. Search candidate identification relied on unquantified AI assistant prompting and citation tracing.
* Critique: Without a reproducible search strategy or systematic protocol (e.g., PRISMA guidelines), the manuscript cannot claim to represent the evolution of the field. It risks cherry-picking studies that align with the author's prior opinions while omitting counter-evidence.

### 2.3. Unverified Core Premise & Logical Contradiction
* Lines 26, 89
* Issue: The central thesis of the review is that FP signal analysis methods are a major source of inter-study variability. However, on Line 26, the author explicitly admits that none of them measures how much variability analysis methods cause, and cites Vuorenpää et al. (2023) stating that FP parametrization is well-established and enables clear comparisons.
* Critique: The paper builds its entire rationale on a hypothesis that it acknowledges has never been quantified in the literature. A review should not assert a problem as an established fact while simultaneously admitting the absence of empirical evidence measuring its impact.



### 2.4. Biophysically Flawed Signal Processing Recommendations
* Lines 65, 92, 101, 129
* Issue 1 (Waveform Inversion - Lines 65, 92, 101): The manuscript recommends waveform inversion (multiplying the signal by -1) for only high peak field potentials prior to analysis.
  * Critique: In extracellular electrophysiology, field potential polarity reflects the local direction of current propagation (sinks vs. sources relative to the electrode). Arbitrarily flipping the sign of a signal alters current polarity and introduces artifacts into depolarization vs. repolarization phase identification. Recommending this in a general analysis flowchart (Figure 2) without rigorous biophysical simulation or experimental validation is scientifically unsafe.
* Issue 2 (Inverse Problem / Digital Twin - Line 129): The author hypothesizes that system identification can separate the recording system from the cellular signal to mathematically reconstruct intracellular action potentials (APs) from extracellular FPs.
  * Critique: Reconstructing APs from single un-passivated extracellular FP electrodes is an ill-posed mathematical inverse problem due to spatial averaging across thousands of heterogeneous cells, variable seal resistance, and capacitive loading. The author conflates physical electroporation (which opens membrane pores to record intracellular-like signals) with pure computational signal processing.



### 2.5. Omission of Signal-to-Noise Ratio (SNR) Sensitivity for Baseline Return
* Lines 71, 74, 79
* Issue: The manuscript advocates for the baseline return definition of FPD over the R-to-T-peak definition.
* Critique: While baseline return theoretically captures full repolarization (APD95-100), the distal T-wave return to baseline in hiPSC-CMs is notoriously flat, low-amplitude, and susceptible to baseline drift, noise, and pacing artifacts. The author fails to address the extreme sensitivity of threshold-based baseline return detectors to low signal-to-noise ratios (SNR), which is a primary reason commercial and open platforms favor peak-based fiducials.

### 2.6. Self-Contradiction Regarding Cell Maturation Staging
* Lines 88, 89, 140
* Issue: On Line 88, the author cites Fetterman et al. (2024), demonstrating that electrophysiological, metabolic, and transcriptional maturation occur independently. Yet on Lines 89 and 140, the author calls for an MEA-native maturation reference value to stage overall hiPSC-CM maturation status.
* Critique: If maturation axes are compartmentalized and independent (as proven by Fetterman et al.), an electrophysiological MEA metric cannot serve as a general proxy for overall cell maturity. The proposal directly contradicts the evidence cited immediately before it.



## 3. Comprehensive Line-by-Line Table of Findings

| Line Number(s) | Section / Component | Finding / Issue Type | Detailed Reviewer Critique & Recommended Action |
| :--- | :--- | :--- | :--- |
| Line 4 | Metadata | Editorial | Lists author as Antti-Juhana Mäki, Independent researcher. Ensure institutional affiliations comply with target journal standards. |
| Line 9 | Header | Manuscript Status | States Preprint, not peer reviewed. Prepared with AI assistance. Must be cleaned for formal submission. |
| Lines 12, 15, 18, 21 | Abstract | Manuscript Hygiene | Contains raw HTML comments from LLM editing. Remove immediately. |
| Line 14 | Abstract | Circular Reasoning | Uses author's own Zenodo report (Mäki, 2023) as the evaluative framework for the review. Re-anchor review against objective industry standards (e.g., CiPA). |
| Line 17 | Abstract | Gap Definition | Identifies 4 methodological gaps, but these are narrowly tailored to author's specific Zenodo opinion paper rather than a systematic field survey. |
| Line 26 | Introduction | Editorial / Logical | Contains leftover editorial comment. Furthermore, admits that no study has measured how much variability analysis methods actually cause. |
| Line 27 | Introduction | Citation Bias | Devotes an entire paragraph to summarizing Mäki (2023) arguments against peak-to-peak FPD without balancing with counter-arguments regarding SNR stability. |
| Line 29 | Scope & Search | Methodological Flaw | Admits no PRISMA protocol was used, no search statistics were recorded, and search criteria were unrecorded. Reframe as a narrative commentary or conduct a structured literature search. |
| Line 39 | Figure 1 (Timeline) | Self-Promotional Bias | Includes DatAnalyzer / Mäki opinion paper in a timeline of major field developments alongside peer-reviewed packages (Cardio PyMEA, CardioMEA). Remove self-citation from timeline unless independently peer-reviewed and widely adopted. |
| Line 58 | Literature Review | Fact Check | Correctly notes that open tools (MultiElec, CardioMDA) existed prior to 2022. Accurate statement. |
| Line 60 | Open Pipelines | Verification | Concedes that open tools have not been shown to displace vendor software and adoption data are lacking. Accurate limitation. |
| Lines 61-68 (Table 1) | Open Platforms | Bias & Technical Issue | Features author's DatAnalyzer alongside validated open platforms. Lists inversion for only-high-peak signals, which is biophysically unvalidated. |
| Line 72 | Literature Review | Manuscript Hygiene | Unremoved internal editing instruction. Remove immediately. |
| Line 74 | Fiducial Definitions | Technical Gap | Discusses Ernault et al. (2024) (NRVM) and Lee et al. (2024) (hiPSC-CM). Fails to critically analyze the SNR failure modes of baseline return in noisy real-world recordings. |
| Line 81 (Table 2) | Table 2 | Missing Data | Entry for Ernault et al., 2024 lists FPD start as blank. Provide explicit definition or state Not Defined. |
| Line 84 | Rate Correction | Analysis Gap | Criticizes Fridericia correction in hiPSC-CMs, but fails to propose or evaluate alternative models (e.g., dynamic pacing, Hodges, Bazett). |
| Line 85 | Machine Learning | Methodological Insight | Correctly notes that ML classifiers (Pramudito et al., 2026; Park et al., 2026) take rate-corrected FPDc as input without testing sensitivity to the rate-correction formula. Good observation. |
| Line 88 | Maturation | Citation / Logic | Cites Fetterman et al. (2024) showing independent maturation compartments. |
| Line 89 | Maturation | Logical Contradiction | Proposes an MEA-native maturity classifier, contradicting Fetterman et al. (2024) who proved electrophysiology cannot index overall maturation. |
| Line 92 | Waveform Morphology | Biophysical Issue | Promotes signal inversion for only high peak signals, acknowledging it is internally validated but unreplicated. Signal inversion alters current polarity and should not be recommended without proof. |
| Line 101 (Figure 2) | Flowchart | Biophysical Error | Flowchart box specifies Signal inversion then pacemaker analysis. Inverting Ve(t) flips physical sinks into sources, corrupting electrophysiological interpretation. |
| Line 119 | 3D Systems | Structural Misalignment | Discusses Botti et al. (2026) under the 3D subsection, but explicitly admits it is a 2D monolayer model. Move to 2D section. |
| Line 122 | Longitudinal Assays | Critical Analysis | Correctly identifies that Brugada syndrome lines in Park et al. (2026) were predominantly atrial-like cells, confounding comparison with normal ventricular lines. Strong review point. |
| Line 127 | Discussion / Outlook | Disclaimer | Explicitly states that outlook views are speculative hypotheses from Mäki (2023) and not findings of reviewed studies. Good transparency. |
| Line 129 | Digital Twins / Inverse | Biophysical Misconception | Claims system identification can extract APs from FPs by removing electrode/tissue effects. Ignores spatial ill-posedness and confuses signal processing with physical electroporation. |
| Line 134 | Limitations | Transparency | Discloses 7 major limitations. While honest, it highlights that the manuscript lacks the methodological rigor required for a peer-reviewed review paper. |
| Line 140 | Conclusion | Re-iteration | Summarizes the 4 gaps. Must be revised if the gaps are re-framed without self-citation bias. |
| Line 147 | Declarations | Conflict of Interest | Author acknowledges authoring Mäki (2023), DatAnalyzer, and co-authoring Välimäki et al. (2021). Transparency is appreciated, but bias remains in text. |
| Line 149 | Declarations | AI Disclosure | Discloses extensive use of LLMs (Claude Code, Cursor) for searching, screening, drafting, and editing. |
| Line 152 | Data Availability | Code Repository | Provides GitHub URL. Verified present. |
| Lines 156-180 | References | Bibliography | Check publication years for post-2024 preprints/articles to ensure all DOIs and citation details are accurate. |



## 4. Section-by-Section Detailed Commentary

### 4.1 Metadata, Abstract, and Introduction (Lines 1-27)
* Editorial Artifacts: The presence of prompt engineering markers on Lines 12 & 18, and Line 26 indicates insufficient manuscript proofreading.
* Framing: The abstract relies heavily on Mäki (2023) to set the evaluative framework. The author must reframe the review to evaluate post-2022 developments against objective experimental benchmarks rather than a self-authored Zenodo report.

### 4.2 Literature Search Methodology (Lines 28-29 & Line 134)
* The manuscript candidly acknowledges that search statistics were not retained and AI tools were used without a systematic screening protocol.
* Requirement: In modern biomedical literature, even narrative reviews are expected to report transparent search parameters (e.g., exact search strings, date ranges, number of returned vs. included papers). The authors should convert this into a semi-structured search or clearly label it as a Perspective/Commentary rather than a systematic review.

### 4.3 Open Platforms and Timeline (Lines 34-69)
* Figure 1 (Timeline): Placing DatAnalyzer / Mäki opinion paper (2023) on equal footing with major published software tools (Cardio PyMEA, CardioMEA, PhysioMEA) gives an unwarranted impression of field adoption.
* Table 1: DatAnalyzer is an un-peer-reviewed tool. It should either be placed in a separate footnote or explicitly noted as a personal unvalidated tool, rather than aggregated seamlessly into Table 1 alongside established packages.

### 4.4 Fiducial Definitions and Biophysical Realities (Lines 70-82 & Lines 90-115)
* Signal Inversion (Line 92 & Line 101): In extracellular MEA recordings, a negative deflection (spike) represents local inward depolarizing sodium/calcium currents (current sink), whereas a positive peak represents an outward current or propagation from neighboring cells (current source). Inverting the waveform turns inward currents into fictitious outward currents. This invalidates the physical basis of extracellular field potential theory (e.g., Bidomain / Cable Theory).
* Baseline Return vs. Peak Detection: The author strongly criticizes the peak-to-peak definition. However, baseline return algorithms fail when SNR is low or when T-waves decay slowly into background noise. The review must include a balanced discussion on computational robustness vs. theoretical physiological accuracy.

### 4.5 Rate Correction and Maturation Confounders (Lines 83-89)
* Rate Correction: The critique of the Fridericia formula is valid and well-supported by Blinova et al. (2018). However, the review misses an opportunity to discuss alternative dynamic pacing methodologies (e.g., field stimulation pacing on MEA) which physically eliminate rate variability.
* Maturation Staging: The author rightly cites Correia et al. (2024) regarding the impact of maturation on pharmacology. However, claiming that MEA metrics alone can form a maturation index conflicts directly with Fetterman et al. (2024), who demonstrated that transcriptional, metabolic, and electrophysiological maturation occur via independent signaling pathways.

### 4.6 Discussion, Future Outlook, and Digital Twins (Lines 126-130)
* Digital Twin & AP Extraction (Line 129): Reconstructing action potentials from field potentials via system identification is presented as a prospective solution. However, extracellular field potentials represent the spatial sum of weighted transmembrane currents from surrounding cells. Because Ve is a spatial integral, recovering a single-cell Vm(t) without invasive electroporation or high-density patch clamp is mathematically ill-posed. The author must temper these claims and distinguish between computational deconvolution and physical membrane electroporation (Lee et al., 2024).

---

## 5. Summary of Actionable Recommendations for Authors

1. Eliminate Self-Citation Bias: Remove Mäki (2023) as the evaluative framework. Re-evaluate the reviewed software and methods against objective consensus criteria (e.g., CiPA validation guidelines).
2. Correct Biophysical Misstatements: Remove or heavily caveat the recommendation for signal inversion in Figure 2 and Table 1. Clarify the mathematical limitations of extracting action potentials from extracellular field potentials in the Discussion section.
3. Clean Up Manuscript Hygiene: Delete all unremoved HTML tags and editorial notes.
4. Resolve Self-Contradictions: Align the discussion on MEA maturation staging with the findings of Fetterman et al. (2024).
5. Fix Table Formatting: Fill in missing values in Table 2 (e.g., FPD start for Ernault et al., 2024) and re-categorize Botti et al. (2026) out of the 3D subsection.
6. Reframe Literature Search: Clearly define the paper as a narrative perspective/commentary and provide exact details on search terms, databases, and selection logic.

---

**Final Verdict:** *Major Revision / Rejection in present form. The paper addresses an important methodological topic but requires substantial restructuring, removal of self-citation bias, biophysical correction, and rigorous editorial cleaning before it can be considered for publication.*



---

# Kirjoittajan arvio tästä raportista (24.10.2026)

Tulkitsen raportin niin, että kolme viidestä pääväitteestä on joko väärinluettu tai jo käsitelty tekstissä, ja jäljelle jää muutama aito ja halpa korjaus. Väitteet on tarkistettu silloisen `main.md`:n sisältöä vasten. Raportin rivinumerot eivät täsmää tiedostoon, joten niihin ei kannata luottaa. Arvioija ei tiennyt, että teksti on preprint eikä vertaisarvioitavaksi tarkoitettu artikkeli.

## Aidot ja hyödylliset havainnot

1. **Oma työkalu ja opinion paper samalla viivalla muiden kanssa.** Figure 1 -aikajanalla ja Table 1:ssä DatAnalyzer ja Mäki 2023 olivat vertaisarvioitujen työkalujen rinnalla ilman merkintää siitä, että ne ovat omia ja vertaisarvioimattomia. Se kerrottiin vain Declarationsissa ja Limitations (iv):ssä. Korjattu 24.10.: aikajanan merkintä ja Table 1:n rivi sanovat nyt, että kyseessä on oma, vertaisarvioimaton työ.
2. **Baseline return -määritelmän kohinaherkkyyttä ei käsitelty.** Teknisesti perusteltu huomio. Korjattu 24.10.: Fiducial-osioon lisättiin lause siitä, ettei käsiteltyjen tutkimusten joukossa ole arvioitu määritelmän kestävyyttä kohinalle ja ajelehtimiselle (Mäki 2023 keskiarvoistaa lyöntejä, Hayakawa 2014 kuvasi tarkan loppupisteen määrittämisen vaikeaksi).
3. **Inversio esitettiin Figure 2:ssa ja Table 1:ssä ilman varausta.** Korjattu 24.10.: kuvateksti ja taulukkorivi sanovat, että kyse on kirjoittajan omasta ehdotuksesta, jota ei ole riippumattomasti validoitu. Arvioijan biofysikaalinen perustelu on mielestäni liioiteltu: elektrodin mittaama polariteetti riippuu elektrodin ja lähteen välisestä geometriasta, ja PhysioMEA analysoi käännettyä signaalia käänteisten T-aaltojen ja matalien R-huippujen kohdalla. Tämä on kuitenkin kenttäsi asiantuntemusta ja sinä tunnet sen paremmin.
4. **AP:n palauttaminen FP:stä on todennäköisesti huonosti asetettu käänteisongelma.** Teksti sanoo jo, että kysymys on avoin ja ettei laitteen osuuden poisto yksin riitä (Ernault). Arvioijan väite, että elektroporaatio ja laskennallinen käsittely sekoitettaisiin, on väärä: tekstissä elektroporaatio on erillinen lähde pariaineistolle. Lisävirke lisättiin 24.10. hyväksyntäsi jälkeen, ks. alla.
5. **Abstractin kohta 4 oli epäselvä.** Arvioijan "ristiriita Fettermanin kanssa" on virhetulkinta, koska Conclusion rajaa vertailuarvon sähköfysiologiseen akseliin. Korjattu 24.10.: Abstract sanoo nyt "electrophysiological axis".
6. **Kosmeettiset.** Korjattu 24.10.: Table 2:n tyhjä FPD start -solu Ernaultin rivillä on nyt "not defined (T-wave landmarks are tested against APD)"; osion otsikko on "Model complexity: 3D cardiomyocyte systems and in silico models of the MEA", koska osio käsittelee myös Bottin 2D-mallia; nopeuskorjauskappaleeseen lisättiin virke pacingista vaihtoehtona (Clements, Matsuda, Guerrelli).

## Kohdan 4 virke (lisätty 24.10.)

Sijoitus: Discussion and future outlook, device-separation-kappale, heti lauseen "Whether the AP can be recovered from the FP at all is an open question: ..." jälkeen.

> The recovery may also be an ill-posed inverse problem, because a field potential is a weighted sum of the transmembrane currents of many surrounding cells; this is the author's reasoning from extracellular recording theory and not a finding of the studies reviewed.

## Ei pidä tai ei koske tavoitettasi

- **"Re-anchor to CiPA" ja hylkäys.** CiPA ei määrittele FP-analyysin fiduciaaleja, joten se ei ole vaihtoehtoinen arviointikehys. Paperi on julkaisematon preprint, ja Mäki 2023 -ankkuri on dokumentoitu Scope-, Limitations (iv)- ja Declarations-osioissa.
- **PRISMA ja haun toistettavuus.** Katsaus on avoimesti narratiivinen ja ei-systemaattinen, ja Limitations sanoo sen.
- **HTML-kommentit, affiliaatio ja kohdelehden vaatimukset.** Kommentit poistetaan ennen vientiä (ToDo), ja loput ovat irrelevantteja preprintille.
- **"Keskeinen premissi ei ole osoitettu".** Teksti sanoo jo "plausible source" ja että kukaan ei ole mitannut vaikutusta; se on tarkoituksellinen pehmennys eikä ristiriita.
