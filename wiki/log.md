# Wiki Log

Append-only chronological record of all wiki operations. Each entry starts with a consistent prefix for grep-parseability. Entries from June to October 2026 are in [log-2026-06-to-10.md](log-2026-06-to-10.md).

Format:
```
## [YYYY-MM-DD] ingest | Author Year — Paper Title
## [YYYY-MM-DD] query | Question summary
## [YYYY-MM-DD] draft | Section updated
## [YYYY-MM-DD] lint | pass
## [YYYY-MM-DD] grill | Decision topic
```

---

## [2026-11-01] draft | High-throughput section heading and opening

At the researcher's choice, the heading "High-throughput and longitudinal assays drive broader feature sets" became "High-throughput and long-term assays": "drive" was a causal claim no source supports, and "longitudinal" fitted only Guerrelli et al. (2024) ("long-term" covers the chronic assay of Altrocchi et al., 2023, and the culture-time recordings of Guerrelli). The researcher shortened the opening sentence; "of the studies examined" was restored to keep the review's scoping ("Several of the studies examined addressed high-throughput and chronic applications"). The cross-reference in the rate-correction paragraph, the section list and synthesis item 14 in docs/claims-by-source.md and the researcher's bookmark in ToDo.md were updated; the claim tag [High-throughput/longitudinal] was kept. scripts/claim_quotes.py needs no change (the heading still starts with "High-throughput").

## [2026-11-01] draft | High-throughput section split into four paragraphs

At the researcher's request, the single long paragraph was split into four (Altrocchi chronic assay and vehicle drift; Park et al. 2025 and 2026; feature sets and Guerrelli's drift; UHD-CMOS-MEA and CardioScripts) with shorter sentences. Content unchanged except: the stray ",." and "Therefore" after the Table 2 citation fixed; Guerrelli's "findings that highlight the necessity of standardizing recording time points and culture age" replaced by the authors' own recommendation (standardised protocols, reporting culture time and equilibration time); "FPD lengthens substantially" replaced by a pointer to the maturation section, where the numbers are given. docs/claims-by-source.md Guerrelli (8) annotated.

## [2026-11-01] draft | High-throughput section tightened to its topic; Park limits moved, Kabanov removed

At the researcher's decision after a per-paragraph review: the Park et al. (2025, 2026) paragraph was shortened to two sentences at the end of the Altrocchi paragraph ("Disease-line screening is another application ... Both reported disease-specific drug sensitivities"); the two limits (one body of evidence; atrial-like Brugada lines) moved to the machine-learning paragraph of the FPDc section, where Park et al. (2026) is discussed, and "the former" there was replaced by "Pramudito et al. (2026)" to stay unambiguous. The CardioScripts sentences (Kabanov et al., 2026) were removed from the section, since the tool is multimodal rather than high-throughput or long-term; Kabanov remains in the Timeline, Table 1 and the Outlook. The section now has three paragraphs. docs/claims-by-source.md: Park 2025 (5)(6), Park 2026 (5)(6)(7) and Kabanov (2) annotated.

## [2026-11-01] draft | Outlook: sensor-fusion paragraph split

At the researcher's request, the sensor-fusion paragraph was split before "In these studies the modalities are mostly analysed separately or side by side": the first paragraph lists the existing multimodal studies, the second states the hypothesis and how it would be done. No wording changed.

## [2026-11-01] draft | Outlook: Li 2025 added to the sensor-fusion example; paragraph split again

The example "adding MEA-derived parameters to a video-based classifier of maturation status" now continues "for which MEA data from the same maturation conditions already exist (Li et al., 2025)" (Scheurer et al., 2025, base their B27 and MM groups on Li et al., 2025; same conditions, not the same cultures). The hypothesis paragraph was split before "The proposal is not to feed raw MEA signals to a model", so the sensor-fusion part now has three paragraphs: existing studies, hypothesis, method and cautions. docs/claims-by-source.md: Li (6) added, synthesis item 16 annotated; Li wiki page relevance note updated.

## [2026-11-01] draft | Outlook: the two hypotheses linked (separated cellular signal as ML input)

On the researcher's idea: the raw MEA signal as it is suits machine learning poorly, but a cellular signal separated from the recording system could be a useful input itself, beyond extracted parameters. The sensor-fusion method paragraph now ends with two sentences making this distinction and noting that whole extracellular waveforms have already been used as machine-learning input in tissue-embedded recordings (Lin et al., 2023); the device-separation paragraph's last sentence now adds that the separated cellular signal could serve as that input. docs/claims-by-source.md: synthesis item 23 (the link is the author's hypothesis) and Lin (6) added; Lin wiki page relevance note updated.

## [2026-11-01] draft | Outlook: device-separation paragraph split into five

At the researcher's request, the paragraph "Separating the recording system from the cellular signal" was split like the sensor-fusion part: (1) the problem and the forward model (Ernault, Lee, Botti); (2) the inverse hypothesis and training data (Mäki, Lee); (3) the recording side changing over time (Altrocchi impedance hypothesis); (4) the open questions (neighbouring cells, ill-posed inverse problem); (5) the digital twin, Vuorenpää and the payoff. Two referents fixed because the split separated them from their antecedents: "The same review notes" became "The review of cardiac microphysiological systems cited above notes", and "If this worked" became "If the separation worked".

## [2026-11-01] draft | Outlook: inverse-hypothesis sentence split into four

At the researcher's request, the long sentence starting "The hypothesis is the inverse direction" was split into four short sentences without changing its content or citation (Mäki, 2023; see the references therein).

## [2026-11-01] draft | Limitations as a list

At the researcher's request, the Limitations paragraph became a lead-in and a bulleted list that keeps the roman numerals (i)–(vii), so cross-references such as "Limitations (vi)" in wiki pages and the claims file stay valid; long sentences were split. Two updates: (i) now mentions the one documented search on maturation reference values (see Scope); (ii) adds tissue-embedded electrodes (Lin et al., 2023) to the kinds of non-standard evidence.

## [2026-11-01] draft | Conclusion: the four gaps as a numbered list

At the researcher's request, the long gap paragraph of the Conclusion became a lead-in ("Four methodological gaps stand out as priorities:") and a numbered list, each item opening with its bold gap statement, with shorter sentences. Wording changes besides splitting: gap 1 "would substantially improve the reliability of FPDc" became "would make FPDc a more reliable pharmacological endpoint" (no source measures the size of the effect); gap 4 "would materially improve inter-study comparability" became "would improve comparability between studies", and the unclear analogy "comparable to how FPDc reports how rate-corrected a measurement is" was dropped; the Correia point is now a plain sentence ("for one drug target, in vitro results correlated with in vivo results only in matured cells"). Citations unchanged.

## [2026-11-01] draft | Conclusion: first paragraph tightened

At the researcher's request, "transparent, physiologically reasoned, and model-conscious practices" became "transparent and physiologically reasoned practices", and "model-specific interpretation" was dropped from the list of developments, since the narrowed 3D section no longer supports them.

## [2026-11-01] draft | docs/claims-by-source.md rewritten from the current main.md

The researcher finished reading main.md. docs/claims-by-source.md was rewritten from scratch: every claim per source restated in the current wording of main.md, with section tags that match the current headings (3D, High-throughput; Figure 2 claims under Morphology, Figure 1 under Timeline; reference-year notes moved to the source headers), obsolete claims dropped (Botti's former 3D passage, Kabanov's CardioScripts passage, the removed CardioMEA FPDc sentence), the Park limits under FPDc, and the old "Check 2026-10-24" notes condensed to page pointers. Ticks kept where the claim is unchanged in substance (Altrocchi 1–5 and 7–9 in the new numbering, Clements 4, Mäki 8, 11, 13, 14; Mäki's former "[z]" read as a tick). The synthesis section became "Register of the author's own inferences" (27 items), adding items the old list lacked: trend framing in the Introduction and Motivation (1), the Abstract/Conclusion closing sentences (7), "growing emphasis" and "trends increasingly seen" in the Fiducial section (9), the morphology-assessment conclusion (12), the rate-correction reasoning (14) and the High-throughput requirements sentence (22). The "Corrections made in the 2026-10-24 verification" list was removed (it is in this log and in docs/lint-fixes-2026-10-24.md). scripts/claim_quotes.py: tags 3D and High-throughput, the Mäki pattern now matches the bare name (Figure 1 entry), and Mermaid "\n" line breaks are turned into spaces so that names after them are found; `--write` run: 173 claims, every one with at least one main.md sentence, no notes. docs/README.md and ToDo.md updated.

## [2026-11-01] draft | Small fixes found while rewriting the claims file

Motivation: missing comma before "chronic drug testing". 3D section: "Fridericia-corrected FPDc" (a doubled correction) back to "Fridericia-corrected FPD". Rate-correction paragraph: the repeated sentence "As mentioned, it has been noted that the Fridericia formula had not been thoroughly validated for hiPSC-CMs (Blinova et al., 2018)" removed (the point is made in the first paragraph). Table 1: "no rate-corrected FPD" removed from the CardioMEA row (its sentence in the text had been removed on 2026-10-29 and the column adds nothing to the review). docs/claims-by-source.md Blinova (4) and Lee (4) adjusted; quotes regenerated.

## [2026-11-01] ingest | Hu 2026 — Unsupervised machine learning-assisted multimodal characterization of cardiomyocytes on a TFT-MEA

The researcher supplied the PDF and supplement (saved as raw/u-2026-...; renamed to raw/hu-2026-tft-mea-multimodal.pdf and -supplementary.pdf to match the page stem). Not open access: all rights reserved by the publisher, so both files were added to .gitignore. Read in full (text extraction), supplement read, Figures 2–7 viewed. Key points: primary fetal mouse cardiomyocytes, not hiPSC-CMs; transparent TFT-MEA (22,500 ITO electrodes) of which 10 adjacent electrodes were recorded; video at 30 fps, much shorter than the electrical recording, aligned by the drug-addition timestamp; spike features (R50/R90 times to and from peak, peak width, peak-to-peak interval) defined on the depolarization spike, no FPD; k-means labels per modality (Fig. 4), supervised models as an internal-consistency check (LR accuracy 0.97), SHAP lists electrical features only (Fig. 6); isoprenaline as the main test, nifedipine in the supplement as less stable; number of cultures not reported; called a proof of concept by the authors. Pages: new wiki/papers/hu-2026-tft-mea-multimodal.md; wiki/multimodal-measurement.md (row and observation); wiki/references.md; wiki/index.md. main.md not yet changed: proposed changes to the outlook are with the researcher.

## [2026-11-01] draft | Outlook and Limitations: Hu 2026 added

At the researcher's approval. Sensor-fusion part, first paragraph: after Ryynänen et al. (2018), two sentences on Hu et al. (2026) (a proof of concept on a transparent TFT-MEA with field potentials and video of the same culture of fetal mouse cardiomyocytes, analysed with interpretable machine learning before and after isoprenaline; ten electrodes, depolarization-based features without FPD, modalities clustered separately, so the degree of combination is unclear). Second paragraph: "In these studies the modalities are mostly analysed separately or side by side" became "In most of these studies the modalities are analysed separately or side by side, and the one joint analysis is a small proof of concept outside hiPSC-CMs". Limitations (ii): "fetal mouse cells (Hu et al., 2026)" added. Not added to the Timeline (outside the hiPSC-CM scope). References: entry copied verbatim from wiki/references.md. docs/claims-by-source.md: Hu section (3 claims) and register item 24 updated; scripts/claim_quotes.py: pattern for Hu; quotes regenerated, no notes.

## [2026-11-01] ingest | Karami 2026 — Microelectrode arrays: from electrophysiology to integrated cancer treatment induced cardiotoxicity assessment

The researcher supplied the PDF as raw/out.pdf; after a relevance check (verdict: useful for the MEA-physics parts only) it was renamed raw/karami-2026-mea-cardiotoxicity.pdf. Open access, CC BY 4.0, not git-ignored. Read in full. Used parts: FP versus APD and the factors shaping the FP (p. 9); superposition of transmembrane currents of all cells (p. 14); the cell–electrode equivalent circuit and the signal shape depending on seal tightness (pp. 13–14, Figure 5B, Equations 4–7; Figure 5B is adapted from a Springer source with permission and is not reusable under CC BY); impedance sensitivity to cell–electrode distance and viability (pp. 16–18); electroporation and Braeken et al. (2012) (p. 11, Table 4). Several citation slips noted (p. 11, Tables 2 and 5), so it is to be used only for textbook-level statements. Candidate found, not read: Lee et al. (2026), Int. J. Stem Cells 19, 146–156 (transparent ITO MEA with hiPSC-CMs). Pages: new wiki/papers/karami-2026-mea-cardiotoxicity.md; wiki/references.md; wiki/index.md. main.md not changed; proposals with the researcher.

## [2026-11-01] ingest | Lee 2026 — Integrated electrophysiological and optical analysis of human iPSC-derived cardiomyocytes using transparent ITO microelectrode chip

Candidate found through Karami et al. (2026); the researcher supplied the PDF and supplement (raw/ijsc-19-2-146.pdf and _supplementary.pdf; renamed raw/lee-2026-ito-mea.pdf and -supplementary.pdf). Open access, CC BY-NC 4.0, not git-ignored. Read in full; Figure 4 viewed. hiPSC-CMs (one in-house line) on a transparent ITO MEA with morphology and baseline Ca²⁺ imaging of the same wells, reported side by side; E-4031 and nifedipine acute, doxorubicin over 2 days. Points for main.md: on doxorubicin day 1 the beat period rose to about 8 s and Fridericia FPDc fell while FPD rose (Fig. 4C, D); the authors state that MEA chip composition and recording hardware may alter absolute signal values. Pages: new wiki/papers/lee-2026-ito-mea.md; wiki/multimodal-measurement.md; wiki/fridericia-rate-correction.md; wiki/references.md; wiki/index.md. main.md not changed.

## [2026-11-01] draft | Karami 2026 and Lee 2026 added to the rate-correction and outlook parts

At the researcher's approval. Rate correction: after the cube-root sentence, "In one hiPSC-CM study, doxorubicin slowed the beat period to about 8 s, and Fridericia-corrected FPD then fell while uncorrected FPD rose (Lee et al., 2026)". Sensor fusion, first paragraph: a sentence on Lee et al. (2026) (transparent ITO MEA, FP, morphology and Ca²⁺ imaging of the same wells, reported side by side). Device separation: the opening statement now names electrode geometry, cell–electrode coupling, cell density and gap-junctional coupling (Karami et al., 2026); a new sentence on the cell–electrode equivalent circuit and the signal following the membrane potential or its first or second derivative, "the kind of device model that the inverse approach would have to estimate" (Karami et al., 2026); the ill-posed sentence cites Karami et al. (2026); the impedance paragraph adds that impedance is sensitive to cell–electrode distance down to about 1 nm; the comparability sentence adds that chip composition and recording hardware can alter absolute signal values (Lee et al., 2026). References: both entries copied verbatim from wiki/references.md. docs/claims-by-source.md: sections for Karami (4 claims) and Lee 2026 (3 claims), register items 14, 24, 26, 27 annotated. scripts/claim_quotes.py: separate patterns for Lee et al. (2024) and (2026) and for Karami; quotes regenerated, no notes.

## [2026-11-01] draft | Declarations generalised; Li 2025 and Lee 2026 added to the timeline

Declarations, competing interests: "both cited in the outlook" became "both cited in this review" (Vuorenpää et al., 2023, is also cited in the Motivation and Ryynänen et al., 2018, in the rate-correction section). Figure 1: "MEA parameters differ between maturation conditions (Li et al.)" under 2025 and "Transparent ITO MEA with FP and optical readouts of hiPSC-CMs (Lee et al.)" under 2026. Hu et al. (2026) and Karami et al. (2026) were not added (fetal mouse cells; a review). docs/claims-by-source.md: Timeline claims (0) for Li and Lee 2026, Vuorenpää (4) annotated; scripts/claim_quotes.py: the two "(Lee et al.)" timeline rows are told apart by their text, and "(Li et al.)" is recognised. ToDo.md: source-check item updated with Hu, Karami and Lee 2026 and the open R-peak check pinned to Lee et al. (2024).

## [2026-11-01] draft | Highlights added; Declarations AI sentence on the claims checklist

At the researcher's request, a "Highlights" section of five uncited bullets (at most about 85 characters each) after the Abstract: open tools with differing FPD definitions; no hiPSC-CM-specific rate correction and Fridericia misleading at extreme rates; no validated MEA-derived maturation reference values; case-by-case morphology handling; ML on MEA data possibly learning analysis differences. LLM-wiki lessons were kept out of the highlights (not findings of the review). Declarations, use of AI assistance: added "Every claim that the text attributes to a source is listed in a checklist for verification against that source, and statements that are the author's own inferences are listed separately; both lists are in the project repository" (worded so as not to claim that the verification is complete). docs/claims-by-source.md: Highlights added to the section list and register item 0. Abbreviations list deferred to a later step.

## [2026-11-01] draft | First highlight reworded

The researcher noted that "Open MEA analysis tools have appeared" suggests open tools are new since 2022, which the text itself contradicts (MultiElec, CardioMDA before 2022). The bullet now reads "Open MEA tools define FPD differently; their FPD values are not directly comparable". docs/claims-by-source.md register item 0 updated.

## [2026-11-01] draft | Sixth highlight on raw signals and device separation

At the researcher's choice (option b), the fifth highlight stays tied to the four gaps, and a sixth was added: "Raw MEA signals mix cell, tissue and device; separating them is proposed as a hypothesis". Raw-signal problems come from cultures and recording hardware, not from analysis definitions, so they were kept apart from "Without these". docs/claims-by-source.md register item 0 updated.

## [2026-11-01] draft | First highlight: "Open" removed by the researcher

The researcher removed "Open" from the first highlight, which now reads "MEA tools define FPD differently; their FPD values are not directly comparable", because vendor tools also define FPD in their own ways. docs/claims-by-source.md register item 0 rewritten for the six highlights; it notes that the reviewed sources document the open tools' FPD definitions, while the vendor tool's definition is not described in the studies that used it.

## [2026-11-01] lint | check.py taken from the template; fixes ported to the template

scripts/check.py replaced by the template's version (ignores hidden files in raw/, warns if main.md has no "# References" heading, skips HTML comments in the reference list); output unchanged here (0 errors, 1 warning). Ported to ../llm-wiki-academic-template (local, not committed; the researcher pushes): the Mermaid "\n" fix in scripts/claim_quotes.py, the register section renamed "Register of the author's own inferences" with the rewrite-from-scratch practice in AGENTS.md, and a general note on same-surname first authors.

## [2026-11-01] draft | Abbreviations list, first-use definitions and italics

At the researcher's request (ToDo A3): main.md gained an "# Abbreviations" section after the Highlights (33 entries). Every listed abbreviation is now spelled out at its first use in the running text: AI (Scope), 3D and 2D (Scope; the later redefinitions in the 3D section were removed), APD90 and APD50 (Fiducial), RR (defined with the Fridericia formula), FPDc (Clements sentence), IGF-1, BCKDK and IC50 (Correia), CMOS (Matsuda), ITO (Lee 2026), AIMS (Clements; "Axion iPSC Model Standards"). Abbreviations used once were written out instead: hPS-CM (Ryynänen), VT (Maurissen), ISSCR; Scheurer's "iPSC-CM cultures" became "hiPSC-CM cultures". Italics: *KCNJ2* as a gene name; I<sub>K1</sub> and I<sub>f</sub> as subscripts. New scripts/check_abbreviations.py (unlisted abbreviations, missing first-use definitions, unused entries; names in an IGNORE list); 0 warnings. Conventions recorded in AGENTS.md; README and ToDo updated; quotes in docs/claims-by-source.md regenerated.

## [2026-11-02] query | Blinova 2018 supplementary files

The researcher added the publisher's supplementary files (mmc1–mmc5.pdf) to raw/ for a verify-before-ingest check. mmc5 is identical to raw/blinova-2018-multisite.pdf, and mmc1 duplicates its pages 13–23 (Tables S1–S8, Figures S1–S3). mmc2–mmc4 are Supplemental Data S1–S3, per-drug figure pages for the low-, intermediate- and high-risk drugs; only their text was read and the figures were not analysed. None of them changes a claim in main.md or docs/claims-by-source.md. Only wiki/papers/blinova-2018-multisite.md was updated: a corrected note and a new "Supplementary material" section summarising Tables S1, S3, S6, S7 and S8 and Data S1–S3. The supplementary files were not renamed or added to the repo.

## [2026-11-02] draft | Reworded register items 9, 16, 19 and 20 (Abstract, Fiducial, FPDc, Maturation, Morphology, Conclusion)

During the researcher's review of the register of the author's own inferences, four items were judged too strong. (9) Trend wording without counts was removed. The Abstract item became "explicitly stated, and in one study physiologically validated, fiducial definitions" and the heading became "Explicit and physiologically motivated fiducial definitions". The Fiducial section now opens with what the studies examined show (the open platforms state their definitions; Ernault tested one against intracellular recordings). "reflects trends increasingly seen" (which contradicted the T-peak conventions of CardioMEA and PhysioMEA) and "has received renewed attention" were removed. (16) The pacing sentence now attributes the rationale to Guerrelli (measurements repeated under 1.5 Hz pacing because the metrics are rate dependent) and drops "it is not the norm in the studies examined". (19) "the components … exist separately" became "some ingredients … have been reported separately", and the missing ingredient was added: an independent maturity measure on the same MEA cultures. The same change was made in Conclusion gap 4, where "no classifier or reference values exist" became "have been reported". (20) The Morphology opening no longer calls the variation a recent "development", which contradicted "Such variation is not new"; it now reads "FP waveform morphology varies between preparations and over culture time, and some of the studies examined handle this variation explicitly". Updated docs/claims-by-source.md (register items 9, 16, 19, 20; Guerrelli (4); Hayakawa (4)), the section tag in scripts/claim_quotes.py and ToDo A2.

## [2026-11-02] draft | Abstract findings sentence split and clarified; Highlights checked

At the researcher's request, the Abstract's five-item list of findings (semicolons with a nested parenthetical) became two plain sentences: "open analysis software is used alongside vendor software, and the open tools state how they place the waveform landmarks (fiducial points) that define the measured intervals; one study tested such a definition against intracellular recordings. Some studies handle differing FP waveform shapes explicitly, analysis approaches have been applied to three-dimensional cardiac models, and assays have expanded to high-throughput and chronic use, …". "emergence of" (trend wording) was dropped. "structured handling of FP waveform morphology heterogeneity" was replaced because it contradicted gap (ii) and the Conclusion's "case by case". Register items 9 and 20 updated. The Highlights were checked against today's rewordings; all six still match the text and were not changed.

## [2026-11-02] draft | Highlight 2 softened to an absence finding

At the researcher's request, Highlight 2 "No hiPSC-CM–specific rate correction exists; …" became "No validated hiPSC-CM rate correction found; Fridericia can mislead at extreme rates" (84 characters). It is now worded like Highlight 3 ("were found"), not as an absolute claim. Register item 0 (2) updated.

## [2026-11-02] draft | Morphology-handling wording made concrete (Abstract, Morphology)

The researcher found "handle differing FP waveform shapes explicitly" unclear. The Abstract now reads "Some tools adapt the analysis to the waveform shape, for example by inverting signals whose peaks point the other way". The Morphology opening now reads "… and some of the studies examined adapt their analysis to it, for example by detecting peaks on the inverted signal". The example comes from PhysioMEA (Weiser-Bitoun et al., 2026) and Mäki (2023). Ernault et al. (2024) is not counted as a handling rule, since it shows why the shape must be checked. Register item 20 updated.

## [2026-11-02] draft | Abstract: last findings sentence split into three

The researcher found the run-on after "point the other way" unclear. The sentence was split into three: "Some tools adapt the analysis to the waveform shape, for example by inverting signals whose peaks point the other way. MEA analysis has also been applied to three-dimensional cardiac models. Assays have expanded to high-throughput and chronic use, with ultra-high-density electrode arrays and machine learning classifiers among the tools used." The content is unchanged; no register item quoted the changed part.

## [2026-11-02] draft | Abstract: bridge to the gaps, "validated" in gap (i)

The Abstract's move from findings to gaps now reads "Despite these developments, **four methodological gaps remain** and are identified as priorities". Gap (i) became "the absence of a validated hiPSC-CM–specific rate correction formula", in line with Highlight 2 ("No validated … found"). Conclusion gap 1 already says the Fridericia formula "lacks formal validation" and was not changed.

## [2026-11-02] lint | claim_quotes.py marks finished sections with ✅

The researcher started marking finished sections of docs/claims-by-source.md with "✅" (the register and Altrocchi). scripts/claim_quotes.py now strips the mark before matching a section title to a source; without this, the Altrocchi quotes would no longer have been updated. With --write it also adds "✅ " to every `## ` section whose top-level checkboxes are all ticked, and removes the mark when a box is unticked. Tested on a temporary copy (untick → mark removed, retick → mark restored). AGENTS.md scripts row updated.

## [2026-11-03] lint | Lint findings 1–4 and 6 fixed (title, trend wording, gap 1, raw annotations)

From the lint of 2026-11-03, at the researcher's decision:
(1) Title. "Charting the Field: Cardiomyocyte MEA Analysis Evolution Since 2022" became "Four Gaps Limiting the Comparability of Multielectrode Array Analyses of hiPSC-Derived Cardiomyocytes: A Review Since 2022" in the main.md front matter and README.md. The description line was rewritten without "evolution".
(2) Open pipelines. "represents an early example of this transition" became "is the earliest of the open pipelines published since 2022 that are examined here".
(3) Conclusion opening. The trend sentence ("methodological development … toward transparent and physiologically reasoned practices", "points toward progress in inter-study comparability") was replaced by what the studies show and by "These are preconditions for comparing results between studies, but whether they have improved comparability cannot be judged from this small evidence base".
(4) Gap 1 worded as a finding of this review. Abstract: "the absence, in the studies examined, of a validated …". Conclusion heading: "No validated FPD rate correction for hiPSC-CMs was found".
(6) AGENTS.md now allows the researcher's highlights and annotations in raw PDFs; the source text is never changed or added to.
The researcher removed the leftover "<!-- jatka -->" comment (finding 5). Register items 3 and 8 updated.

## [2026-11-03] draft | Title shortened, description expanded

At the researcher's request, the title became "Four Gaps Limiting Comparability in MEA Analysis of hiPSC-Cardiomyocytes" (main.md front matter and README.md). The front-matter description now carries what the title leaves out: that this is a narrative review since 2022, the spelled-out terms, and the four gaps.

## [2026-11-03] draft | Abstract: scope qualifier stated once for the four gaps

The repeated "in the studies examined" in gaps (i) and (ii) was removed. The qualifier now appears once, in "**four methodological gaps remain** in the studies examined", and covers all four gaps. Register item 3 updated.

## [2026-11-03] draft | Highlight 5: "ML" spelled out

Highlight 5 became "Without these, machine learning may learn analysis differences rather than biology" (83 characters). "machine learning" replaces the abbreviation, since highlights are read on their own, and "on MEA data" was dropped to stay within 85 characters. ML remains in the Abbreviations list because it is still used in the text. Register item 0 (5) updated.

## [2026-11-03] lint | Lint findings 8, 9, 12, 13 and 16 handled

(8) wiki/papers/ernault-2024-interpretation.md now gives the current name of the fiducial section. (9) Karami et al. (2026) added to wiki/multimodal-measurement.md as a review row (TFT-MEAs recording optical, voltage and impedance signals; impedance sensitivity to cell–electrode distance, morphology and viability). (12) The finding was wrong: all 11 supplementary files are already linked from their paper pages. scripts/check.py only counted the **File:** link, so it now counts every existing [[raw/...]] link on a page (0 info lines left). (13, 16) The documented searches for gap (i), and for gap (ii) at lower priority, were added to ToDo A4 for a later decision. (10) The index date is left for the final wiki tidy (ToDo A4). (11) needs no action, (15) was done earlier, and (14) is still under discussion.

## [2026-11-03] query | New concept page: signal separation (lint finding 14)

At the researcher's decision, wiki/signal-separation.md was created from the paper pages and the device-separation part of the outlook (Highlight 6). It has a table of what Karami, Ernault, Lee 2024, Botti, Altrocchi, Lee 2026, Lin, Vuorenpää and Mäki say about the cell, tissue and device shares of the FP, and which main.md sentence each supports. The author's hypotheses (register items 25–27) are listed separately. Observations: four outlook sentences rest on Karami et al. (2026) alone, a review with citation slips; the Ernault page records neighbouring-cell current for the simulated LEAP, not for the ordinary FP, so main.md's "the FP also depends on current from neighbouring cells (Ernault et al., 2024)" should be checked (Ernault claim 5); Lee et al. (2024) attribute the weak FPD–APD correlation to noise and small T waves. Linked from wiki/index.md (date updated), the multimodal page, and the Karami and Botti pages. main.md not changed.

## [2026-11-03] draft | Outlook: Ernault citation corrected; electroporation caution added

The researcher checked Ernault et al. (2024). Its neighbouring-cell current concerns the LEAP ("a LEAP is not a recording of the local action potential but is generated by intracellular current provided by neighboring cardiomyocytes"), not the ordinary FP. In the outlook, "the FP also depends on current from neighbouring cells (Ernault et al., 2024)" was removed. The insufficiency of removing the device contribution is now argued from Karami's superposition point, merged with the ill-posed sentence. Ernault is now used for a new caution: "The paired signals proposed above as training data share part of this limitation: a local extracellular action potential obtained by electroporation is not a recording of the local AP but is generated by current from neighbouring cardiomyocytes". Updated Ernault (5), Karami (3) and register item 26 in docs/claims-by-source.md, and the observation on wiki/signal-separation.md.

## [2026-11-04] draft | Timeline: Botti label clarified

At the researcher's request, the Figure 1 label "In silico MEA–tissue biophysical model (Botti et al.)" became "In silico model of hiPSC-CM tissue coupled to MEA electrodes (Botti et al.)", matching the paper's Discussion (a bidomain tissue model with a coupled electrode model). Botti claim (1) updated.

## [2026-11-04] draft | Introduction and Motivation: trend framing replaced, Botti cited

The researcher pointed to a sentence in Botti et al. (2026): "To enhance the utility of hiPSC-CMs in drug development, reliable MEA recordings are essential." The unsourced trend sentence "As the use of MEA-based assays has grown, so has the need for consistent, physiologically meaningful analysis of FP waveforms" (register item 1) became "Reliable MEA recordings are considered essential for using hiPSC-CMs in drug development (Botti et al., 2026), and that reliability depends not only on the recording but also on consistent, physiologically meaningful analysis of FP waveforms". "how methods and analysis practices … have evolved since 2022" became "This review examines methods and analysis practices in cardiomyocyte MEA studies published since 2022". The heading "Motivation: why analysis methods became central after 2022" became "Motivation: why analysis methods matter". README.md was aligned. Register item 1 was reworded and unticked for review, and Botti claim (5) added.

## [2026-11-04] draft | FPDc: Clements pacing sentence clarified

At the researcher's request, the Clements part of the pacing sentence now reads "…defined for spontaneously beating cells: more mature cells can beat with periods longer than its 3000 ms upper limit, which makes recordings impractically long, so pacing would probably be needed, a paced assay being left to a possible future standard (Clements et al., 2025)". This makes explicit that 3000 ms is the upper limit of the 750–3000 ms window and that the standard's reason for pacing is practical, not rate correction. Clements claim (4) updated.

## [2026-11-04] draft | Detail trimmed in maturation, open pipelines, FPDc, 3D and high-throughput sections

Removed detail not needed for the argument: Correia medium composition, patch-clamp values and BCKDK/IC50 details (paragraph now one sentence; timeline label without ACC2); Altrocchi plate format and compound classes; Park 2025 example drugs; classifier types for Pramudito 2026 and Park 2026; CardioMEA SQL/dashboard and PhysioMEA MATLAB/executable (both remain in Table 1); Li 2025 numerical values; Scheurer SVM/Shapley parenthesis; Maurissen example FPDc values. Abbreviations ACC2, BCKDK, IC50 and IGF-1 removed from the list. Matching claims in docs/claims-by-source.md reworded; Correia claims (5) and (6) dropped, (7) renumbered to (5).

## [2026-11-05] draft | DatAnalyzer dated 2022 and language corrected to MATLAB

GitHub repository AnaHill/DatAnalyzer: created 2022-04-27, language MATLAB, no licence at the time (the author is adding MIT). Timeline: DatAnalyzer moved to 2022, separate 2023 entry for the opinion paper. Table 1: year 2022, language Python corrected to MATLAB, caption explains the year column. Open pipelines: DatAnalyzer released the same year as Cardio PyMEA, which stays the earliest (its repository dates from 2020). Mäki 2023 page and claims (2), (4) updated.

## [2026-11-05] query | DatAnalyzer licence confirmed

GitHub API: AnaHill/DatAnalyzer now has an MIT licence (LICENSE). Mäki 2023 page updated; "open-source" in Table 1 caption now holds for DatAnalyzer too.

## [2026-11-05] draft | Timeline: own work shown once

The separate 2023 entry for the Mäki opinion paper was merged into the 2022 DatAnalyzer entry, which now names the paper as the description of the method.

## [2026-11-05] draft | Morphology: FP polarity as an unstated assumption

From the researcher's flipped screenshots of Dunham et al. (2022) Figs 4–6. Added one neutral paragraph at the end of the morphology section (Dunham beat and LAT definitions presuppose polarity, not stated; Karami: FP may follow Vm or its first or second derivative). New concept page wiki/fp-polarity.md keeps the inverted, pacemaker-like reading, arguments for and against and possible tests; linked from index, Dunham, Mäki and Karami pages. Claims Dunham (7), Karami (5) and register item 28 added.

## [2026-11-05] query | FP polarity page: Dunham figures added

Figures 4 (left plot), 5A–B and 6C–D extracted from raw/dunham-2022-cardiopyemea.pdf, cropped and shown as published next to a vertically flipped copy in wiki/assets/fp-polarity/; embedded on wiki/fp-polarity.md with CC BY attribution and a note of the changes. The researcher's Word file is no longer needed.

## [2026-11-05] draft | Figure 2: biphasic condition on the T-wave-peak branch

From the Ernault et al. (2024) claim check: the Figure 2 node "APD90 surrogate" now reads "APD90 surrogate if biphasic T wave", because the paper found the T-wave peak to coincide with APD90 only for biphasic T waves, a minority of the monolayers (p. H803). Claim Ernault (4) and its quote updated.

## [2026-11-05] draft | Maturation: Fetterman paragraph shortened, timeline wording

From the Fetterman et al. (2024) claim check. Timeline label now says "largely independent", as the source does. In the maturation section the method sentence (single additions and subtractions, nine formulations by RNA sequencing) and the fatty-acid example were merged into one general sentence: functional, metabolic and transcriptional maturation responded largely independently when medium components were added or removed one at a time. Claims in docs/claims-by-source.md: Fetterman (2) reworded, former (3) dropped, (4) and (5) renumbered to (3) and (4); register item 18 now points to Fetterman (2).

## [2026-11-05] draft | Limitations: "non-MEA modalities" reworded

Fetterman et al. (2024) call their impedance recordings MEA-based but recorded no field potentials; Scheurer et al. (2025) used video-based analysis (checked by the researcher). Limitations item (ii) now says "modalities other than field potentials". Fetterman (4) and Scheurer (7) in docs/claims-by-source.md updated.

## [2026-11-06] ingest | Guerrelli 2024 — supplementary material

raw/guerrelli-2024-hipscm-supplementary.pdf (figshare 10.6084/m9.figshare.24222883) read from the text layer; Supplementary line and a "Supplementary material" section added to the Guerrelli page (Figs S1–S6, Tables S1–S8: intrawell FPD homogeneity, daily and paced values, LEAP APD, Cor.4U, reporting datasheet S8 without fiducial or rate-correction fields). main.md not changed; proposals to the researcher.

## [2026-11-06] draft | Guerrelli supplement used in maturation, high-throughput and morphology sections

Maturation: Clements amplitude criterion (≥ 0.5 mV) depends on recording day (Guerrelli Suppl. Tables S2, S5: day 2 below 0.5 mV in both lines, 3.6 and 8.1 mV on day 14; Clements leaves culture protocols to vendors). High-throughput: Guerrelli's reporting datasheet (Table S8) has no field for FPD definition or rate correction. Morphology: Guerrelli chose electrodes by T-wave shape. Claims Guerrelli (9)–(11), Clements (8) and register item 29 added.

## [2026-11-06] draft | Maturation: amplitude sentence simplified

"day 2 after thawing" replaced with Guerrelli's own term "post-defrost"; exact amplitude values dropped (below 0.5 mV on day 2, several millivolts by day 14).

## [2026-11-06] draft | FPDc: Guerrelli equilibration sentence made precise

The 15–20 min recommendation is now attributed to the authors with its basis (changes for 7–12 min in iCell², longer than the manufacturer's 10 min) and the absence of the effect in Cor.4U. Guerrelli claim (3) reworded, pointers added.

## [2026-11-06] draft | FPDc: Guerrelli pacing sentence covers drug tests

The pacing sentence now names both uses of external pacing in Guerrelli et al. (2024): across days in culture (1.5 Hz) and in drug tests (rate chosen per drug). Claim (4) reworded, pointers added.

## [2026-11-06] draft | Maturation: Guerrelli drift paragraph without exact values

Dropped 257 ms, 27.5-fold, 30 days, the I<sub>K1</sub> parenthesis, 1.5 Hz and 275.5 → 336.0 ms; the text now says FPD lengthened markedly when spontaneous and significantly when paced. Values remain in the claims and on the Guerrelli page. Claim (5) reworded.

## [2026-11-06] draft | High-throughput: Guerrelli equilibration percentages dropped

The researcher removed the 22.6 % and 7.7 % values from the high-throughput section; Guerrelli claim (7) updated to match. All Guerrelli claims checked by the researcher.

## [2026-11-06] draft | Abbreviations cut from 25 to 17 entries; detail trimmed

Spelled out or dropped so they leave the list: 1D, AFM, AIMS, BRV, CMOS, FPDcF, ITO, LAT, LQTS, ML, NR, UHD (timeline, Table 1, formula, Figure 2, Matsuda and Lee 2026 sentences). Trimmed detail: Cardio PyMEA and PhysioMEA feature lists (kept in Table 1), CardioMEA parallel processing/dashboard in Table 1, Maurissen mutation codes, Matsuda 0.03 µM / 10-fold. Equivalent-circuit detail (Karami) kept at the researcher's request. Matching claims reworded.

## [2026-11-06] ingest | Hayakawa 2014 — supplementary methods

The researcher added the publisher supplement mmc1.docx; renamed to raw/hayakawa-2014-motion-fp-supplementary.docx. It holds only expanded methods (MEA seeding inside a silicone ring, 3–6 days on the probe, one cell lot; block-matching motion vector algorithm; stage-top incubator for simultaneous FP and motion; traction force microscopy), no further results. Wiki page updated (Supplementary line, culture details under Methodology, new "Supplementary material" section); claims-by-source status line updated. No change to main.md, wiki/references.md or wiki/index.md.

## [2026-11-07] query | Hayakawa 2014 claim check: isoproterenol slope

The paper gives the isoproterenol FPD/CRD slope as 0.737 in the Results text (p. 6) and 0.738 in the Fig. 8B caption. The wiki page and the Pointers line in docs/claims-by-source.md gave only 0.738; both now give both values. main.md does not cite the number.

## [2026-11-08] draft | Outlook: Hu et al. (2026) on sensor fusion

Prompted by the researcher after the Hu claim check. One sentence added after the sensor-fusion hypothesis in the Discussion and future outlook: the authors of the proof of concept see combining a transparent MEA with machine learning as moving beyond single-modality analyses towards sensor fusion (Hu et al., 2026, Conclusion, p. 9). Worded as their view, since their own analysis clustered the modalities separately. "likewise" in the following Vuorenpää sentence changed to "also". New claim Hu (4) in docs/claims-by-source.md; register item 24 updated.

## [2026-11-09] query | grinding skill added

New skill .claude/skills/grinding (MIT licence, written for this repository): `/grinding <source>` checks every claim listed for that source in docs/claims-by-source.md against the full source and reports a verdict per claim, read-only until fixes are asked for. Formalises the claim-check reports used for Ernault, Fetterman, Guerrelli and Hayakawa. AGENTS.md (directory table, new "Grinding" section), README.md (usage, layout, licence) and ToDo.md (A2 tips) updated.

## [2026-11-09] draft | 3D and Conclusion: Hwang 2023 wording; supplement ingested

From the /grinding check of Hwang et al. (2023). The supplement raw/hwang-2023-spheroids-supplementary.pdf (Figures S1 and S2: experimental FP, simulated FP and simulated AP for E-4031 and nifedipine concentration series) was added by the researcher and viewed; summarised on the wiki page. main.md: the 3D section now follows the authors (three-dimensionality "contributes", as they "take to imply") and names the adult human ventricular cell model of the simulation; the Conclusion gap 3 no longer says "the 3D geometry alone changed FP shape" but that FP shape varied with stimulation and electrode locations in a 3D geometry with a single cell type. Wiki page: Supplementary line, cell model in Methodology, new finding on FP repolarization peaks at high concentrations, Limitations corrected (the paper does have a limitations paragraph, p. 8). docs/claims-by-source.md: Hwang (3), (4), status and Pointers updated ((2) is on p. 3, not p. 5).

## [2026-11-09] draft | 3D section: Hwang sentence refined

After the researcher compared the new wording with the paper: "hiPSC-CM" restored in "simulations of hiPSC-CM spheroids" (the paper's name for its geometric model), "adult" dropped (the paper says only "human ventricular cell model"), and the authors' other sources of heterogeneity (cell types, differentiation) added. Hwang (3), its Pointers and the wiki page updated to match.

## [2026-11-09] draft | Ismaili 2023: author order and timeline entry

Grinding Ismaili. The reference had the authors in the wrong order; corrected from p. 1 of the PDF in both wiki/references.md and the main.md reference list (Ismaili, Schulz, Horváth, Koivumäki, Mika, Hansen, Eschenhagen, Christ). Wiki page: Authors line reordered and "Donatus Mika" corrected to "Delphine Mika". main.md timeline (2023): "Hamburg perspective on hiPSC-CM limitations" replaced by "hiPSC-CMs as electrophysiological models — opportunities and challenges", following the paper's title (the paper covers opportunities as well, and "Hamburg" means little to a reader). docs/claims-by-source.md: Ismaili (1), status and Pointers updated.

## [2026-11-09] ingest | Kabanov 2026 — supplementary material

The researcher added the supplement of Kabanov et al. (2026) (mmc1.docx), renamed to raw/kabanov-2026-cardioscripts-supplementary.docx. Six figures of example traces (S1–S2 AFM on EBs with 1 mM aminophylline, isoprenaline, metoprolol; S3–S5 HL-1 MEA with detected peaks and the filtering; S6 cantilever position on the EB); no data bearing on the claims in main.md. Summarised on the wiki page.

## [2026-11-09] draft | Kabanov 2026: grinding and Outlook wording

Grinding Kabanov: claims (1)–(3) hold. main.md Outlook: "contraction force from simultaneous atomic force microscopy" reworded to "a mechanical contraction signal from simultaneous atomic force microscopy, used to measure the delay between field potential and contraction", because the synchronous recordings were analysed for timing (force came from AFM alone, Fig. 7). Wiki page: aminophylline concentrations and cell types corrected (arrhythmia 10 µM in EBs, QT prolongation 128 µM in HL-1), the Fig. 5 scheme of the QT interval (Q to the T-wave end) and T-offset (to the T peak) added, the inconsistent QT error (Table 1 19.4 ms on artificial data, text 0.06719 s, Fig. 9 caption 0.2) recorded, page numbers of the limitations corrected. docs/claims-by-source.md: Kabanov (4), status and Pointers updated (T-peak detection is on p. 5, not p. 3; Fig. 10 on p. 9).

## [2026-11-09] draft | Table 1 and fiducial list: CardioScripts QT end point

After the researcher read the zoomed Fig. 6D of Kabanov et al. (2026) (Q marker just before the R peak, T marker on the T-wave peak) and the script detects no T-wave end (p. 5; Table 1 labels Q, R, S, T), the Table 1 cell "Not reported (T peaks detected)" became "T peak (QT measured from the Q point to the T peak; no FPD)", and the fiducial-list parenthesis now says that CardioScripts reports "a QT interval from the Q point to the T peak rather than an FPD". The Fig. 5 schematic, which draws the QT brace to the T-wave end, is noted on the wiki page as not matching the detected points. Kabanov (2), (3) and Pointers updated.

## [2026-11-09] draft | Outlook: Karami 2026 sentences made more general

Grinding Karami. At the researcher's request the Karami sentences in "Separating the recording system from the cellular signal" now say less detail and more generally: the opening sentence says that an FP reflects not only the AP and the recording electronics but also the surrounding tissue and its coupling to the electrodes (adhesion, electrode geometry, cell density, gap junctions); the equivalent-circuit sentence adds that the membrane-potential case needs very tight contact and low junctional membrane resistance (the source's text and Table 4 disagree here); the impedance sentence says "far smaller than a cell" instead of "about 1 nm"; and the ill-posed sentence now cites Karami only for the contribution of surrounding cells and their adhesion, with the device-removal and ill-posed parts left as the author's inference (register item 26 updated). Wiki page: text–Table 4 disagreement recorded as substantive. docs/claims-by-source.md: Karami (1)–(4), status and Pointers updated.

## [2026-11-09] ingest | Lee 2024 — supplementary material

The researcher added the supplement of Lee et al. (2024) ("lee2024_table 1.docx"), renamed to raw/lee-2024-cardiomea-supplementary.docx. Figures S1–S11 (processing time, simultaneous patch-clamp and HD-MEA intracellular-like recordings reprinted from Lee et al., 2022, dose series for six drugs on SQT5 cultures and two on iCell cardiomyocytes, dashboard tab), Supplementary Method 1 (electroporation protocol) and Method 2 with Table S1 (AUTO-SKLEARN candidate models). No claim in main.md changes; summarised on the wiki page with the caption slips ("four baseline measurements (file_1 to file_3)").

## [2026-11-09] draft | Fiducial: Lee 2024 attribution softened

Grinding Lee 2024: all eight claims hold. main.md: "which the authors attribute to small, noisy T waves" became "which the authors suggest may reflect small, noisy T waves" (the paper: "This could be attributed to"). Claim (5) resolved from Fig. 2A (FPD from the positive R peak to the T-wave peak). Wiki page: outdated note on the unreadable PDF replaced, Fig. 2A and Fig. 4 values added. docs/claims-by-source.md: Lee 2024 (5), (6), status and Pointers updated.

## [2026-11-10] draft | FPDc and Outlook: Lee 2026 sentences

Grinding Lee 2026 (claims (1) and (2)). Rate-correction section: "doxorubicin slowed the beat period to about 8 s, and Fridericia-corrected FPD then fell while uncorrected FPD rose" generalised to "In a two-day doxorubicin exposure of hiPSC-CMs, beating slowed so much on the first day that Fridericia-corrected FPD fell while uncorrected FPD rose". Outlook: "at baseline" added to the Ca²⁺ imaging of the transparent-MEA study (Fluo-4 imaging was done only at baseline, separately from FP recording). docs/claims-by-source.md: Lee 2026 (1), (2), status and Pointers updated.

## [2026-11-11] query | Harness guardrails after the single-loop agent article

Added project .claude/settings.json: permission deny rules Edit(raw/**) and Edit(notes.md) (they cover Write too), and a PostToolUse hook on Edit|Write that runs scripts/hooks/main_md_checks.py, which runs check_abbreviations.py and check.py when main.md was edited and returns the output to the model. Pipe-tested and seen firing on a main.md edit. AGENTS.md: Finishing check and Schema evolution updated; moving Ingest and Lint into skills noted as planned. ToDo C2 updated.

## [2026-11-11] query | README: agent design section

README "How it works" gained a subsection "Agent design: a single loop with progressive disclosure", linking Anthropic's article on folding subagents into the main loop and mapping its system prompt / thin tools / guardrails summary onto AGENTS.md, the scripts, the skills, .claude/settings.json and the claims checklist.

## [2026-11-12] draft | Acknowledgements and About the author added

New sections before Declarations: thanks to former colleagues (no names, at the researcher's request) and a short author description based on the researcher's academic portfolio page (D.Sc. (Tech.) 2018, doctoral and postdoctoral work 2011–2022, visiting scholar until 2024, DatAnalyzer) and current work described generally as data and AI expert. The researcher added "PhD" to the author line in the front matter.

## [2026-11-12] draft | About the author: links to dissertation and DatAnalyzer

After the researcher's own edits: dissertation title linked to its URN (from the researcher's academic portfolio page), DatAnalyzer linked to its GitHub repository, and the last sentence made grammatical ("combining agent-assisted workflows with attention to data quality is part of daily work").

## [2026-11-12] draft | Maturation and Outlook: Li 2025 sentences

Grinding Li 2025. Maturation section: the CV and spike-amplitude sentence generalised to "increased as maturation stimuli were added to the culture (a lipid- and calcium-enriched medium, nanopatterning and electrostimulation)", naming the medium's higher calcium, which the authors link strongly to electrophysiological maturation; "the authors do not propose these values as maturity markers" became "the authors read these changes as signs of electrophysiological maturation but do not propose reference values" (Discussion, p. 10). The classifier-ingredients sentence drops "the same" ("MEA parameters that differ between maturation conditions"). Outlook: "MEA data from the same maturation conditions" became "from the same culture media" (the schedules of Li and Scheurer differ). Wiki page Limitations and docs/claims-by-source.md Li (1), (3), (6), status and Pointers updated.

## [2026-11-12] draft | Maturation: Li 2025 clause removed

The researcher removed "but do not propose reference values" from the Li 2025 sentence in the maturation section as not essential; the paragraph's last sentence already states that no reference value for standard MEA recordings has been reported. docs/claims-by-source.md Li (3) updated to match.

## [2026-11-12] draft | Outlook: Scheurer 2025 cited for the video-based classifier

At the researcher's suggestion the sensor-fusion sentence now cites Scheurer et al. (2025) directly for "a video-based classifier of maturation status" (their SVM separates day-21 from day-42 maturation-medium cultures on beating features, p. 9), before the Li et al. (2025) citation for the MEA data. docs/claims-by-source.md Scheurer (6) updated.

## [2026-11-12] draft | Maturation: Scheurer 2025 sentence generalised

Grinding Scheurer: all seven claims hold. At the researcher's request the maturation-section sentence was made more general: "Scheurer et al. (2025) showed that an interpretable machine-learning classifier can separate immature from more mature hiPSC-CM cultures using only non-invasive, video-based beating features" (the days, the 99.5 % accuracy and the 46-video test set dropped; the separate sentence on video-based features merged into it). docs/claims-by-source.md Scheurer (3) and Pointers updated (journal page numbers).

## [2026-11-12] query | Scheurer 2025 wiki page updated after grinding

Wiki page: the B27-to-MM split on day 21 and two videos per well added to Methodology; a new "Our observations" subsection notes that the classes differ in both age and medium, and that the per-video train–test split may let both videos of a well fall on different sides (not stated in the paper); Relevance updated to the generalised main.md sentence.

## [2026-11-13] draft | Conclusion: machine-learning outlook paragraph

The researcher rewrote the paragraph; language corrected ("It is clear that ... will" changed to an attributed opinion, "the previous section" to the Discussion and future outlook section, the sentence fragment starting with "And" joined, typo "reseach"). Register item 23 updated.

## [2026-11-13] draft | About the author: two hiPSC-CM MEA studies linked

DatAnalyzer sentence now names its use in two co-authored hiPSC-CM studies, linked by DOI: Häkli et al. (2021), Scientific Reports 11, 4153 (cardiac ischemia), and Häkli et al. (2022), Stem Cells International 2022, 9438281 (acute hypoxia and reoxygenation). Details from the researcher's publications.bib; linked, not cited, so they stay out of the reference list.

## [2026-11-13] draft | Personal note added after the Conclusion

First-person section on the FPD end point: T-wave peak linked to APD90 for biphasic T waves (Ernault), two open tools end at the T-wave peak (Lee 2024, Weiser-Bitoun), Cardio PyMEA locates the T-wave end (Dunham), no study compared the wave end with the AP, a positive T wave ended before the AP (Ernault); a difficult measurement is not a reason to skip it. claim_quotes.py maps the section to the tag [Personal]; claims Ernault (8), Lee 2024 (9), Weiser-Bitoun (8), Dunham (8), Mäki (16) and register item 30 added. ToDo A3b personal note done as a first version.

## [2026-11-13] draft | Personal note: early afterdepolarizations as the reason for the full FPD end

The researcher's added sentence reworded and sourced to Mäki (2023): early afterdepolarizations may go unnoticed when the FPD ends at the repolarization peak. Mäki claim (16) extended.

## [2026-11-13] draft | Personal note: EAD sentence replaced; afterdepolarization note on the critical assessment page

The EAD sentence in the personal note was replaced by a neutral one about measuring the last part of repolarization, without a citation. Critical assessment, Claim 2: removed the unqualified "tail matters for EAD risk" and added a note that the opinion paper's EAD argument is broader than the physiology supports (phase-2 EADs early in the AP, only phase-3 EADs near the end of repolarization, DADs after it). Mäki claim (16) back to its original scope; register item 30 updated.

## [2026-11-14] draft | Maturation: Lin 2023 validation sentence

Grinding Lin: six of seven claims hold. Claim (4) overlooked that sarcomere alignment was imaged in the same tissue/electronics hybrids after recording (p. 5, Fig. 2E–G); main.md now says "and the trajectory was not validated against an independent maturity measure" instead of "no external maturity measure was taken on the same cultures". Same correction on wiki/papers/lin-2023-nanoelectronics.md (Limitations, Relevance 2c) and wiki/hipsc-cm-maturation.md. docs/claims-by-source.md Lin (4), status and Pointers updated (sarcomere imaging; p. 5 for the one-surface MEA argument).

## [2026-11-14] lint | wiki graph: tags, hub pages and links

At the researcher's request the wiki's links and tags were reworked for the Obsidian graph. (1) Tags: the 53 tags (34 used once, several duplicates such as review/review-perspective, 3d/3d-model, cardiotoxicity/cardiac-safety) were replaced by a fixed vocabulary of 13 theme tags following the main.md sections plus page-type tags (type/concept, type/method, type/analysis, type/review); every wiki page now has 1–4 tags from it, and critical-assessment-maki-claims.md got front matter. The vocabulary is recorded in AGENTS.md (Conventions). (2) Three new concept pages compiled from existing paper pages and main.md, no new content: open-analysis-platforms.md, 3d-models.md, machine-learning-mea.md; added to wiki/index.md (3D removed from the candidate list; Last updated 2026-11-14). (3) Paper-to-paper links with a short reason added for pairs that main.md compares but the wiki did not link (Lin–Mäki, Lee 2024–Mäki, Correia–Scheurer, Hayakawa–Lee 2024, Ernault–Hayakawa, Altrocchi–Park 2026, Blinova–Park 2025, Blinova–Maurissen, Ernault–Karami, Guerrelli–Clements). (4) Every paper page's See also now links the concept pages that cite it. (5) .obsidian/graph.json (git-ignored, local only): colour groups by theme tag and one for concept/method/analysis pages.

## [2026-11-14] lint | write-back from main.md to the wiki

The wiki had no way back from main.md: connections and themes made while drafting did not reach the wiki pages. AGENTS.md: Draft gets step 5 "Write back to the wiki" (links with reasons, concept pages for recurring themes, new tags only via the Tag vocabulary) and the log step names the wiki pages changed; Lint gets a check that the wiki carries main.md's connections; the scripts row mentions the new checks. scripts/check.py: (1) INFO for sources cited in one sentence of main.md (Limitations of this review skipped) whose wiki pages are neither linked directly nor both linked from one concept page; (2) WARN for wiki pages without tags or with tags outside the Tag vocabulary, read from AGENTS.md. On the current wiki both report nothing (all 18 same-sentence pairs are connected through concept pages after today's rework). README: the "rule plus mechanical check" principle added to the agent-design list. ToDo.md C2: these items marked for the template.

## [2026-11-14] ingest | Matsuda 2025 — supplementary material

The researcher added the supplement of Matsuda et al. (2025) (toxsci-25-0276-File009.docx), to be renamed raw/matsuda-2025-uhd-supplementary.docx (the rename was blocked by the deny rule on raw/ in .claude/settings.json; the researcher renames it). Contents: Supplementary Figure 1 (0.1 µM doxorubicin over 72 h, conventional MEA versus CMOS-MEA: CV falls on CMOS from 24 h, spike amplitude falls on the conventional MEA at 48–72 h) and legends of Movies 1–4. Recorded on the wiki page: absolute CV and amplitude differ between the two platforms (our observation); the Movie 4 legend gives 30 nM E-4031 for the EAD-like waveforms where the Fig. 4C caption gives 100 nM; the supplement names Eisai Co., Ltd. as the second affiliation. The E-4031 propagation-area concentration on the page was marked ambiguous. No claim in main.md changes.

## [2026-11-14] draft | High-throughput: Matsuda 2025 doxorubicin sentence

Grinding Matsuda: all five claims hold. At the researcher's request the doxorubicin sentence was generalised by attributing it to the authors ("The authors report that the platform detected doxorubicin-induced cardiotoxicity at lower concentrations than earlier studies"), since the earlier studies used other readouts and partly animal cells. Wiki page: the nature of those earlier studies added, page-number convention noted. docs/claims-by-source.md: Matsuda (5), status and Pointers (journal page numbers) updated.

## [2026-11-14] ingest | Li 2024 — Human iPSC-derived closed-loop cardiac tissue for drug assessment

The researcher added raw/Li_2025_PIIS258900422400213X.pdf (to be renamed raw/li-2024-closed-loop.pdf by the researcher; the rename was blocked by the deny rule on raw/). The paper is from 2024 (iScience 27:108992, published 23 January 2024), not 2025. New page wiki/papers/li-2024-closed-loop.md; reference added to wiki/references.md and main.md; index entry; hipsc-cm-maturation.md (new bullet) and fridericia-rate-correction.md (new row) updated. Chosen over the EMA review by Mondéjar-Parreño et al. (2026), which was assessed and not ingested (general NAM review; it misdescribes Matsuda 2025 and this paper as using controlled pacing).

## [2026-11-14] draft | Maturation and FPDc: Li 2024 added

Two short sentences, kept minimal at the researcher's request: maturation section ("Rapid pacing by a self-sustained traveling wave likewise raised MEA conduction velocity and changed the responses to several drugs") and rate-correction section (pacing before the recording as a maturation step, stopped before drug tests, tissues then at about 1 Hz). Wiki write-back: li-2024-closed-loop.md links li-2025-maturation, guerrelli and matsuda with reasons and the two concept pages. docs/claims-by-source.md: new section Li et al. (2024) with two claims.

## [2026-11-14] ingest | Li 2024 — supplementary material and raw renames

The raw/ rule in .claude/settings.json was changed from deny to ask at the researcher's request (edits to raw/ now need approval, so renames at ingest are possible; notes.md stays denied). The researcher's files were renamed to raw/li-2024-closed-loop.pdf and raw/li-2024-closed-loop-supplementary.pdf. Supplement (Figures S1–S8) summarised on the wiki page; Figure S4 shows QT of about 0.15 s with the traveling wave running against about 0.6 s in controls, a rate effect, whereas the main text reports about 300 ms in both groups after the wave was stopped. No main.md change. AGENTS.md and README.md updated to describe the ask rule.

## [2026-11-15] ingest | Maurissen 2024 — supplementary material

Supplement (Figures S1–S8, Tables S1–S11) read and summarised on the wiki page. It adds the per-probe and per-sheet values behind the group means: the spread within a genotype is wide and tracks the differentiation run and cardiomyocyte purity; every 3D sheet used was mixed 1:1 with mesenchymal cells; the 3D long-QT group pools LQT46 and LQT26 while the 2D value is LQT26 alone, and the E-4031 dose–response in 3D is LQT46; most arrhythmias first appeared at 1000 nM, above the 100 nM cut-off of the arrhythmogenic score; clone-to-clone differences within one genotype are as large as some genotype differences (Supplementary Fig. 7a); and individual sheets span roughly 5–60 % cardiomyocytes. Our calculation: the ± values of the main text match neither the standard deviation nor the standard error of the per-probe values for most groups, while the means match exactly.

## [2026-11-15] draft | 3D section: two word-level corrections after the Maurissen supplement

"for both mutant lines" became "for both mutant genotypes", because the 3D long-QT group pools LQT46 and LQT26 while the 2D value is LQT26 alone. "the cardiomyocyte purity of the sheets was 25–41%" became "averaged 25–41%", because that is the range of the three group means and individual sheets span roughly 5–60 %. docs/claims-by-source.md: Maurissen (5), (6), status and Pointers updated; the Pointers now also record that the paper defines its FPD end point explicitly (p. 9), which Table 2 of main.md does not list.

## [2026-11-15] draft | 3D section simplified and Maurissen added to Table 2

At the researcher's request the Maurissen passage in the three-dimensional models section was shortened from three sentences to two: the KCNH2 gene name, the genotype enumeration and the cardiomyocyte purity percentage were dropped. The purity number was replaced by what it reflects, namely that the sheets mix cardiomyocytes with mesenchymal cells, which the authors consider necessary for the arrhythmic waveforms alongside the three-dimensional structure (p. 3 and p. 7). Table 2 now lists Maurissen et al. (2024) under the R-to-T-peak convention, since the paper states its end point explicitly (p. 9); wiki/fpd-end-conventions.md gained the matching row and the paper page links it. docs/claims-by-source.md: Maurissen (5) and (6) reworded, new claim (7) for Table 2, Pointers updated.

## [2026-11-15] draft | Motivation: "mechanistic" dropped from the use-case list

Checking Maurissen claim (2) showed that "mechanistic electrophysiological phenotyping" is the review's own label and that none of the three sources behind it supports "mechanistic": Maurissen measures no ion currents and infers IKr from FPD and the mutation (p. 4), Park 2026 uses the word only of a procedure-based system and of in silico models by others, and Park 2025 uses neither "mechanistic" nor "phenotyping". The label is now "genotype-specific electrophysiological phenotyping", which fits all three (gene-edited KCNH2 lines; LQTS and BrS patient lines; an LQTS line against healthy lines). docs/claims-by-source.md: Maurissen (2), Park 2025 (3), Park 2026 (1) and register item 23 updated. The Maurissen Pointers now name the two Results subsections that hold the 2D and 3D means and record that the paper never compares them.

## [2026-11-15] draft | FPDc: the Brugada-line caveat reworded after grinding both Park studies

Grinding Park et al. (2025) and Park et al. (2026) together. All claims hold except one wording: main.md said the two Brugada lines of Park et al. (2026) make the comparison with normal lines "confounded by cell identity", but the authors test exactly that explanation with marker expression (MYL2, MYL7, Fig. S3) and conclude the cells were not directed toward atrial differentiation, attributing the atrial-like action potentials to the disease. The sentence now says "which the authors attribute to the disease itself rather than to atrial differentiation". New register item 31 records the remaining own inference in that sentence, that the two Park studies are one body of evidence rather than independent replication. docs/claims-by-source.md: Park 2026 (6) and Park 2025 (7) reworded, both Pointers rewritten (the vendor tool of Park 2026 is named only in the Supplementary Methods; the subtype proportions are in Fig. S2; Park 2025 never mentions Fridericia and notes that some healthy lines responded like the patient line).

## [2026-11-15] draft | FPDc: the unnamed correction of Park et al. (2025)

The rate-correction sentence said Fridericia is "the correction used in the studies examined here that report rate-corrected FPD" and then that Park et al. (2025) also report corrected FPD without naming the formula, which read as a contradiction since that study does report rate-corrected FPD. "Used" became "named", and at the researcher's request the clause now adds that they use the same vendor software as studies that name Fridericia, without saying which formula they used. New register item 32 records the inference and the sources behind it (Li et al., 2025 names Fridericia for the same Axion Cardiac Analysis Tool; Altrocchi et al., 2023 and Park et al., 2026 use the same platform; the vendor's own poster ties its FPDc criterion to Fridericia). wiki/fridericia-rate-correction.md and the Park 2025 page record the reasoning; docs/claims-by-source.md: Park 2025 (5) and Pointers updated.

## [2026-11-15] query | Axion application note read for the vendor FPD definition

The researcher pointed to Axion BioSystems' application note "CiPA on the Maestro" (web page and its flyer PDF, September 2017). Read 2026-11-15: the flyer never defines FPD in words and names no rate-correction formula, but its schematic marks FPD from the depolarization spike to the peak of the repolarization wave, and ΔFPD as the shift between the repolarization peaks of control and dosed traces, i.e. the R-to-T-peak convention. Recorded in wiki/fpd-end-conventions.md as a separate section with its caveats (vendor marketing, 2017, a drawing rather than a specification, and it names the CiPA Analysis Tool while the reviewed studies name the Cardiac Analysis Tool), and linked from the Park 2025 page. Not ingested as a paper page and not cited in main.md: that is the researcher's decision, and a corporate-author reference entry would not be recognised by the parser in scripts/check.py.

## [2026-11-15] draft | Park 2026: shared lines, subtype thresholds and the small-dataset caution

Grinding Park et al. (2026) on its own, with the supplementary methods read in full. Three changes. (1) The overlap with Park et al. (2025) is larger than stated: besides the long QT line DPHCi01, the normal line CMC-011 appears in both, so "apparently a long QT line" became "two cell lines" in main.md, in both claim entries and in register item 31. (2) A new sentence in the maturation section, "Such classifications rest on action potential thresholds, so a disease phenotype that shortens the action potential can shift cells into the atrial-like class", with new claim (13) for the sourced half and register item 33 for the consequence. (3) The researcher questioned whether the paper admits a small dataset. It does not: its statement that "AI analytics still heavily rely on the quantity and quality of data" is a general remark and a call for external validation. The claim entry now says the description is the review's own, and new register item 34 records that Scheurer and Pramudito call their datasets small themselves while Park et al. (2026) do not.

## [2026-11-19] draft | Pramudito 2026: what the FPDc section needs from it

Grinding Pramudito et al. (2026); all six claims held against the full text, so the only change is one of emphasis. The sentence in the rate-correction section reported that the stacking ensemble outperformed each of its constituent classifiers on 16 held-out CiPA compounds. That is a result about machine-learning architecture, not about rate correction, and the number of test drugs is already given two sentences later. It now reads that the ensemble "predicted torsades de pointes (TdP) risk from two ΔFPDc-derived predictors alone", which is the fact that matters here: the classifier rests entirely on the rate-corrected value whose correction the study never examines (Methods, p. 2: "relies on only two MEA-derived biomarkers"). Claim (3) was reworded to match and the Pointers line now names the supporting passage for each claim, including the authors' own "The dataset is small" (p. 9). No wiki page needed a change: pramudito-2026-ensemble.md already records both predictors and the authors' limitations.

## [2026-11-19] draft | per-claim quotes in the claims file

`scripts/claim_quotes.py` assigned the sentences of `main.md` to claims by section tag alone, so every claim sharing a tag showed the same sentences: 152 of the generated quote lines were repeats, and a reader could not see which sentence a claim was about. A claim line may now end with `{q: <regex>}`, and then only the sentences matching it are listed. The regex replaces the citation test instead of narrowing it, which also solves the older limitation that a sentence continuing a citation without naming the source was listed nowhere at all: claim (5) of Pramudito et al. (2026) now shows "Both evaluated their models on small test sets of 15–16 drugs by repeated resampling", and three claims of Lin et al. (2023) show "Their recordings came from stretchable electrodes embedded in 3D microtissues ...", neither of which had ever appeared. Markers were written for 97 claims across 25 sources, leaving 16 repeats where two claims genuinely describe one sentence. The script reports a regex matching nothing, and, once any claim of a section is narrowed, a sentence of that section that no claim lists. The convention is in AGENTS.md under "Claims file"; the generated lines stay machine-written and are not edited by hand.

## [2026-11-19] draft | Ryynänen 2018 and Vuorenpää 2023 ground; the Motivation sentence split

Grinding Ryynänen et al. (2018) and Vuorenpää et al. (2023) against their full texts. All eight claims held. Ryynänen: Bazett's formula (p. 4), the unsynchronised video and MEA recordings of the same single cell on transparent ITO electrodes (p. 5, Fig. 4g–h). Vuorenpää: the parametrization sentence (p. 15, section 6.1.1, which the review attributes to Kussauer et al., 2019), the modality-combining potential (p. 15, section 6.1) and the holistic data set with no integrative multiphysics models published (pp. 20–21); the text contains no machine learning, AI or digital twin discussion, as the Pointers line states.

The only change is to the last sentence of the Motivation section, which ran to three clauses joined by "but" and "and". It is now three sentences: what the reviewed studies show, that none of them measures the variability, and the review's contrasting description of parametrization as well established. The claim quotes were regenerated, so claim (1) of Vuorenpää now carries only its own sentence. Two findings reported but not yet fixed: the Pointers line of Vuorenpää claim (2) gives p. 12–13 for a passage that is on p. 15, and the paper pages of both sources have small stale spots (ryynanen-2018-single-cell-mea.md says Table I compares video data for cells 1–3 where the table has cells 1–4; vuorenpaa-2023-mps-building-blocks.md names only the two Outlook citations under "Relevance to our paper", not the Motivation one).

## [2026-11-19] draft | the Motivation gap narrowed; Ryynänen and Vuorenpää pages corrected

The second sentence of the Motivation gap claimed that none of the studies reviewed "measures how much variability analysis methods cause". Read literally that is a universal negative about measuring variability at all, and the review itself cites work that does: Hwang et al. (2023) measure the contribution of spheroid three-dimensionality to field potential variability, and Guerrelli et al. (2024) quantify equilibration and days-in-culture effects. Lee et al. (2024) and Ernault et al. (2024) come closer still, testing one FPD definition against the action potential. What none of them does is apply two analysis conventions to the same recordings and report the difference, and the sentence now says that. It is checkable, it survives those four studies, and it matches the abstract's "one study tested such a definition against intracellular recordings". Synthesis item 2 records the narrowing.

Corrections from the grinding of the two sources: the Pointers line of Vuorenpää claim (2) gave p. 12–13 for a passage on p. 15; ryynanen-2018-single-cell-mea.md said Table I compares MEA and video data for cells 1–3 where the table has cells 1–4 at baseline, and the page carried only one tag, so `rate-correction` was added for the FPDc citation; vuorenpaa-2023-mps-building-blocks.md listed only the two Outlook citations under "Relevance to our paper" and now names all four, the Motivation one first. The same page records two things found in the full text: the well-established-parametrization sentence is attributed onwards to Kussauer et al. (2019), and section 7 of the same review speaks of "highly variable in vitro results from different laboratories".

## [2026-11-19] draft | the Vuorenpää counterpoint moved from Motivation to Limitations

The Motivation section ended on a review of cardiac microphysiological systems calling the parametrization of action potentials and field potentials well established. The sentence arrived without a stated role: the paragraph had been about MEA analysis methods throughout, "by contrast" pointed at the wrong neighbour (the contrast is with the plausible-source sentence two sentences earlier, not with the one before it), and the statement is thin for the position it held — one clause of a review that is not about MEA analysis methods, attributed onwards to Kussauer et al. (2019), from a text that elsewhere speaks of "highly variable in vitro results from different laboratories".

Dropping it entirely would have left the gap claim resting on the author's own opinion paper, which is the exact exposure the Declarations already disclose. It is now the last sentence of Limitations (iv), where the standing of the evaluative framework is already admitted: "The premise that FP analysis methods are a source of inter-study variability is not universally shared either". The Motivation paragraph now ends on the gap. Vuorenpää claim (1) moved from the Motivation tag to Limitations, synthesis item 2 records the counterpoint as its own line, and the paper page names Limitations (iv) as the citation site. Item numbering in Limitations is unchanged, so no claim referring to (vi) was affected.

## [2026-11-19] draft | grinding Weiser-Bitoun 2026: PhysioMEA's map types and the R-peak polarity

Grinding Weiser-Bitoun et al. (2026) against the full text, Results included for the first time. Six of eight claims held unchanged; two changes were applied.

The open-pipelines sentence credited PhysioMEA with "two-dimensional spatiotemporal heatmaps of signal propagation". The paper has three distinct map types: 2D potential heatmaps (Fig. 3A), a propagation period heatmap for one beat (Fig. 3B) and 2D biomarker heatmaps over many beats (Fig. 4). The spatiotemporal dimension belongs to the biomarker maps, and propagation maps are not the paper's novelty — MultiElec and Cardio PyMEA already produce them (p. 11), while "for the first time, a comprehensive 2D analysis of biomarkers" is the claim the authors make for themselves. The sentence now reads "per-electrode biomarkers, two-dimensional spatiotemporal biomarker heatmaps, propagation maps and beat rate variability analysis".

In Table 2 the R-to-T-peak row described its start point only as Hayakawa's initial negative peak. PhysioMEA defines the R peak as the positive sharp spike, detected by a positive-amplitude threshold with a 50 µV default (pp. 1 and 3), so two sources in one row of the table define the start with opposite polarity. The Start cell now names both. This is an instance of the inconsistency the section is about, not a defect of the table, and it makes the row carry its own argument. The paper pages of both sources link each other with that reason, and the convention table in `wiki/fpd-end-conventions.md` records the polarity.

Claim (4) was extended and claim (2) reworded, both with the date; the Pointers line gained the polarity passages and the list of the three map types; the Status line records that the Results are now read. Two findings reported and left unfixed: main.md calls the PhysioMEA organoids a 3D preparation, where the source never describes the construct as three-dimensional (its only "three-dimensional" is a data matrix) and the organoids are seeded directly onto the plate inside a 1.5 mm² ring; and the Pointers line places the MATLAB runtime on pp. 2–3 where it is on pp. 4–5. Also noted for later: the Discussion (p. 11) states that standardizing peak detection and biomarker calculations matters for comparability between studies, which is the first sourced statement of this review's own premise.

## [2026-11-19] draft | the PhysioMEA organoids are no longer called a 3D preparation

The 3D section opened its analysis-tool sentence with "Analysis tools are beginning to target 3D preparations, such as PhysioMEA for cardiac organoids". The three-dimensionality rested on the word "organoid" and on nothing in the source. Weiser-Bitoun et al. (2026) use "three-dimensional" once, of the X/Y/beat-number matrix behind their heatmaps (p. 3); their own dimensional language is 1D versus 2D in the electrode plane, and the analysed object is "the 2D cardiac sample" (p. 11). The organoids are made by seeding dissociated cardiomyocytes directly onto a Matrigel-coated MEA plate through a guide ring with a 1.5 mm² hole (p. 3), and the Limitations note that the ring "constrained the organoid's dimensions" (p. 12). That is closer to a confined dense monolayer than to a spheroid, and since this was the only analysis-tool example in the section, an assessor reading the Methods would have found the example empty.

The sentence now reads "Analysis tools are beginning to target organoids and other multicellular constructs, such as PhysioMEA for cardiac organoids (Weiser-Bitoun et al., 2026), although those organoids were seeded directly onto the MEA plate and all of its analysis is planar", and the systematic-comparison point follows as its own sentence. The condition strengthens that second half rather than weakening it: it says why no 2D-versus-3D comparison exists. Claim (6) was reworded with the reasoning, the Pointers line gained the ring and the constrained dimensions, and the same caution is on the paper page and in `wiki/3d-models.md`, so the wiki no longer presents the construct as 3D either. The Pointers line also had the MATLAB runtime on pp. 2–3; it is on pp. 4–5.

## [2026-11-20] query | PhysioMEA software links and the 2025-versus-2026 year

Three addresses for PhysioMEA were fetched and recorded on the paper page: the GitHub repository (MATLAB sources, a bundled `mhrv` folder behind the BRV measures, GPL-3.0, no tagged release and no installer), the lab's documentation page (a four-part user manual: raw data, peak detection and biomarkers, 2D heatmaps and videos, batch BRV) and the lab's novelty page (two self-declared novelties, 2D biomarker analysis and batch BRV of cardiac constructs, with no competing tool named — weaker than §4.5 of the paper, which compares six tools). The paper itself names only the lab site root, not the repository. `wiki/open-analysis-platforms.md` gained the repository and licence for PhysioMEA, and a note that the same check has not been done for the other open tools, so the table does not yet say whether their code is reachable, licensed or versioned.

The year was questioned because the authors' GitHub README and Elsevier's Cite widget both say 2025. It stays 2026: the article header reads "Journal of Molecular and Cellular Cardiology 210 (2026) 137–149", so the issue year is 2026, while 17 November 2025 is the online-first date that the copyright line and the DOI also carry. The same split was decided the same way for Botti et al. (2026) and Park et al. (2026), and APA takes the issue year once volume and pages exist. Nothing in `main.md`, `wiki/references.md` or the file names changes. The evidence for both readings is now on the paper page and in the claims status line, so the question does not need to be reopened.

## [2026-11-20] query | the Support vocabulary of the register, written down as it is used

The reading guide of the register promised three values for **Support** — `none`, `thin` and `inference` — but the items use five: `sourced` and `opinion` had grown in without being defined, and three items gave their support in prose with no keyword at all. The guide now lists all five, each with what it claims and how it fails, and states what the earlier one-line definition left implicit: `thin` and `inference` are not points on one scale. `thin` is sourced but narrow and needs a better study; `inference` is derived rather than sourced and needs a better argument, so it can fail although every source behind it is right. The guide also records the two shapes that no single value fits: composite support, where each part is named separately, and absence claims, whose support is the search behind them rather than a value. Item 0, the highlights, is named as the one item that inherits its support from the items it summarises.

Three Support lines were normalised to match: item 7's "supported for the list" became `sourced` for the list, and the word opinion was marked as the value it already was in items 3, 6 and 7. Every Support line now carries a backticked value except item 0. Counting occurrences across the 34 items: `inference` 19, `thin` 7, `none` 5, `sourced` 4, `opinion` 4. **Origin** was also added to the guide, since items use it for whose idea a statement was and when, and the guide did not mention it.

## [2026-11-20] lint | the register's Support vocabulary documented where it is needed and checked by script

The Support vocabulary was defined only in the reading guide of the register, about 650 lines into `docs/claims-by-source.md`. That is the right place to read it, but the wrong place to learn that it exists: an agent starting a session reads `AGENTS.md`, which until now did not mention the register at all. The Draft operation said to write connections back to the wiki and nothing about registering an unsourced statement, and the "Cite everything in the draft" guideline covered only missing citations, not statements that are deliberately not sourced. The evidence that this got lost is in the file itself: `sourced` and `opinion` grew in without ever being defined, and three items gave their support in prose with no value.

The repository's own design principle answers this, and the README states it: "a rule in AGENTS.md alone gets forgotten, and a script alone cannot judge". So both were added. `AGENTS.md` gained a "Register of the author's own inferences" paragraph after the Claims file one, naming the six values and pointing to the reading guide as the authority, with the instruction not to invent a seventh but to add it to the guide and then to `SUPPORT_VALUES` in `check.py`; the "Cite everything in the draft" guideline now separates a missing citation from a deliberate inference; and the `check.py` row of the scripts table mentions the new check. `scripts/check.py` warns about a Support line that carries a value outside the vocabulary or no value at all, which was tested by planting a `plausible` value and seeing the warning (line, value and all) and then restoring the file.

Two smaller changes followed from making the rule mechanical. Item 0 had been an exception written in prose, so it now carries `inherited`, a sixth value defined in the guide for an item that summarises others; every Support line now carries a value, which is what makes the check simple. The guide also states that the vocabulary is fixed there and that a value may take a qualifier or be composed per part. `docs/README.md` and the public `README.md` describe the register and the vocabulary where each one's reader will meet it, and the stale "29 sources" and "items 1–27" in the docs table were corrected.

## [2026-11-20] draft | the morphology-awareness sentence: the numeral dropped and the consequence weakened

Grinding Weiser-Bitoun claim (5) alone, to see what the sentence rests on. The Weiser-Bitoun half holds: two morphology-dependent branches in §2.5, low-amplitude R peaks found on the inverted signal and inverted T waves on the inverse segment (p. 3). Two other parts of the sentence did not survive the check.

"Two of them show an awareness" invited a count that the section does not support. The Conclusion names three sources for case-by-case morphology handling (Mäki, Ernault, Weiser-Bitoun), the next sentence of the Morphology section credits the opinion paper with the same awareness of large differences in FP signal forms, and register item 20 assigns the handling branches to Weiser-Bitoun and Mäki while stating that Ernault "is the reason to check the shape, not a handling rule". The pair in the sentence is Ernault and Weiser-Bitoun because its "or" spans two kinds of evidence, which is defensible, but the numeral made a checkable claim out of it. It now reads "some of them anticipate waveform heterogeneity".

"Which indicates that a single canonical FP shape cannot be assumed" ran against the cited source. Weiser-Bitoun describe a canonical waveform on p. 1, "a positive sharp spike (R-peak) followed by a negative sharp spike (S-peak) … then … a smooth, hill-like segment (T-wave)", and treat the branches as exceptions to it, so the paper does assume the shape and corrects afterwards. The evidence supports the weaker and true consequence, now a sentence of its own: "The canonical FP shape therefore does not always hold."

The counter-evidence had been recorded nowhere, so it is now in three places: claim (5) states that the anticipation is read off the algorithm rather than stated by the authors, the Pointers line carries the p. 1 passage against (5) and notes that the electrode exclusion is a data-consistency rule, and the paper page says the same under Morphology handling. Ernault claim (4) was reworded with the sentence, and register item 20 records both changes with their reasons.

## [2026-11-20] lint | every claim in main.md is now checked against its source

ToDo A2 is complete. `docs/claims-by-source.md` has no unticked box left: 199 claims across 30 sources and 35 register items, in 31 sections that all carry the ✅ mark. The checking ran from 2026-10-18 to today, first as a page-by-page pass at ingest and in the lint of 2026-10-24, then from early November as `/grinding` sessions that read a source in full and reported a verdict per claim before anything was changed.

What the pass was worth is visible in what it changed rather than in the ticks. Wordings were narrowed where the source said less than the draft: the Motivation gap became "none of them applies two analysis conventions to the same recordings and reports how much the results differ" instead of a universal negative about measuring variability; the morphology sentence lost its numeral and its consequence became "the canonical FP shape therefore does not always hold"; the PhysioMEA organoids stopped being called a 3D preparation; the FPDc sentence on Pramudito et al. (2026) now says what the rate-correction section needs from that study. Facts were corrected where the record was wrong: page numbers in several Pointers lines, the R-peak polarity difference inside one row of Table 2, Table I of Ryynänen et al. (2018) on a paper page. Counter-evidence that existed only in my reading is now written down, most of it against claims that still stand.

Three things are worth carrying forward. The register has grown to 35 items, which is the honest measure of how much of this review is the author's own reasoning rather than a report of sources; its Support values now say which kind each item is. Nothing in `main.md` is cited to a source that was not read in full, except where a status line says otherwise. And the Discussion of Weiser-Bitoun et al. (2026), p. 11, states that standardizing peak detection and biomarker calculations matters for comparability between studies — the first sourced statement of this review's own premise, which register item 2 still carries as `inference`; deciding whether to cite it is the one piece of unfinished business this pass turned up.

## [2026-11-20] query | why only one gap has a documented search behind it

Recording a decision that until now existed only as a ticked box in `ToDo.md`, which is a working file that will not survive publication. Of the four gaps, only gap (iv), MEA-derived maturation reference values, rests on a documented search (`docs/maturation-mea-search.md`, 30 October 2026). For gap (i), a validated hiPSC-CM-specific rate correction, a search of the same kind was considered and not run; for gap (ii), shared morphology criteria, it was given lower priority for the same reason and is still open.

What makes the asymmetry defensible is the scope limiter in the claims themselves. The Abstract and the Conclusion state that the gaps remain "in the studies examined", not in the literature at large, and an absence claim of that shape is tested by reading the studies examined, which the claim-by-claim pass has now done for all of them. A documented search would be needed only to make the stronger claim that no such formula or criteria exist anywhere, which the paper does not make. Gap (iv) is the exception because its sentence does claim more: `main.md` says that no study proposing or validating such reference values "was found in a search of PubMed/MEDLINE (30 October 2026, no date limit)", and that wording needs a search behind it.

The consequence is already disclosed rather than hidden: Limitations (i) says the selection is non-systematic with one documented search, register item 3 notes that no documented search lies behind gap (i) unlike gap (iv), and register item 6 marks gap (iv)'s support as only as strong as that search. If the claims for gaps (i) or (ii) are ever widened beyond "the studies examined", the search becomes necessary before the wording changes, not after.

## [2026-11-20] lint | final index tidy: the date and the Vuorenpää role

Closing lint finding 10 of 3 November, which left the index date for the final wiki tidy. `wiki/index.md` read "Last updated: 2026-11-14" although nearly every page changed after that, during the grinding of Lin, Matsuda, Maurissen, Park, Pramudito, Ryynänen, Vuorenpää and Weiser-Bitoun; it now reads 2026-11-20 and should be stamped again at export. The rest of the index needed nothing: all 30 paper pages and all 11 concept pages are listed, `check.py` finds no broken link or missing entry, and the summaries that could have gone stale had not. In particular the Weiser-Bitoun and 3D entries say "cardiac organoid" and "organoid analysis", never 3D, so they were already consistent with yesterday's correction.

One entry gained a role. Index summaries say what a page is, which is enough while a source is used for what it reports, but Vuorenpää et al. (2023) is now cited for something its summary did not reveal: its statement that AP and FP parametrization is well established is the counterpoint to this review's own premise, and it sits in Limitations (iv) rather than among the findings. A reader of the index would have taken it for an ordinary MPS review. The entry now names that role. The same could be done for other pages whose use in `main.md` is not evident from what they report; it was not done wholesale, because for most sources the summary and the use are the same thing.

## [2026-11-20] lint | figure workflow: the diagrams stay in main.md, the export gets images

Preparing the two Mermaid figures for the Zenodo export. The obvious move, replacing the ```mermaid blocks in `main.md` with image references, turned out to be blocked: `claim_quotes.py` reads those blocks as sentences of the draft, and 22 generated quote lines in `docs/claims-by-source.md` come from inside them, including all 18 Timeline claims and the Figure 2 claims such as "J -->|T-wave peak| K[APD90 surrogate if biphasic T wave Ernault et al., 2024]". Replacing the blocks would have left every one of those claims with no sentence to point at, days after the claim-by-claim pass was completed.

So the blocks stay in `main.md` as the source of truth, and the export works from a generated copy. A new script, `scripts/figures.py`, does three things: `--write` copies each block to `figures/<slug>.mmd` for uploading to Mermaid Live and records its SHA-256 in `figures/figures.json`; `--export` writes `main-export.md`, a git-ignored build copy in which each block is replaced by an image reference to the rendered `figures/<slug>.svg`, with alt text taken from the figure caption; and a plain run reports the state of each figure. `check.py` now warns while a rendered image is missing and warns again when a diagram changes after its image was recorded, which was tested by planting a wrong hash. Both the missing-image warnings are showing now, as they should until the rendering is done.

This answers the two failures of the test export directly: the HTML will no longer load Mermaid from an unpinned `unpkg.com` URL and draw the diagrams in the reader's browser, so an offline reader sees them, and the PDF cannot split a diagram the way Figure 2 was split over pages 9–11 with an empty grey box. The route is written up in `docs/pdf-export-notes.md` under "Figure workflow", the Mermaid item there is marked solved, `AGENTS.md` gained a "Figures stay as Mermaid in `main.md`" convention with the reason, and the README shows both figures and describes the arrangement. One caution carried into the notes: Figure 2 uses a literal `\n` inside node labels, which recent Mermaid versions may print instead of breaking the line, and it must not be changed to `<br/>` in `main.md` without checking `claim_quotes.py`, which strips `\n` when it reads the block.

## [2026-11-20] lint | README: the wiki maintenance that the pattern descriptions leave implicit

The README described the division of labour between author and agents in two sentences, which was enough to be accurate and not enough to be noticed. The part that gets skipped when people adopt the LLM-wiki pattern is the reviewing: Karpathy's gist promises a compounding artifact where "the synthesis already reflects everything you've read", and the sentence that makes that true is further down, almost in passing — "I browse the results in real time — following links, checking the graph view, reading the updated pages". A new section quotes both and says plainly that an unsupervised wiki does not stay empty, which would at least be visible, but fills with plausible, well-formatted, confidently cross-referenced material that nobody has checked. It compounds either way; the reviewing decides which way.

The section argues from this repository's record rather than from principle, because the record is unusually specific: the four hallucinated-citation incidents, "Galli et al. 2024" among them, a paper that does not exist and that reached both the draft text and the reference list; the claim-by-claim pass of 199 claims across 30 sources and three wordings that did not survive it, including the 3D claim that rested on the word "organoid" and the "two of them" that did not survive counting; and the 35 registered inferences that separate what the paper asserts on its own account from what it reports. It closes on the division that makes the work sustainable: mechanical checks for what a script can decide, human reading for what it cannot, with `check.py` able to see a missing reference entry or a stale figure and unable to see a page that misrepresents the study it summarises.

`llm-wiki.md` was left untouched, since it is another author's text under its own terms. A pointer was added to the blog item in `ToDo.md`, where this is the main message rather than a side note.

## [2026-11-20] draft | Declarations: the source check stated as done, and a brief for AI reviewers

Two changes before the export. The Declarations said that every claim attributed to a source "is listed in a checklist for verification against that source", which was the wording from before the check was run: it promised a list, not a result. The claim-by-claim pass finished yesterday, so the sentence now says that every such claim was checked against its source by the author, one source at a time, and that where a claim did not hold as written the sentence was narrowed or corrected. The consequence matters more than the activity: a check that changed nothing would be worth little. No counts were put into the sentence, because a number in prose goes stale silently and the repository already reports the live ones.

`docs/ai-review-brief.md` is new: the instructions to hand an external AI reviewer along with `main.md`, which is self-contained and the only input it needs. The brief lists what the review already discloses about itself, so that a reviewer does not spend its findings restating the non-systematic selection, the single author or the author's own framework; it asks for the five kinds of comment that would actually change the text, starting with claims that overreach their evidence; it rules out the suggestions that do not apply to a Zenodo preprint; and it requires a DOI and a statement of how each suggested reference was verified, because invented citations have reached this draft before. The reply is to come back inside one markdown code block so it can be pasted into the repository unchanged.

## [2026-11-20] query | Open ScholarPeer dropped; the external review is one second-model read

Recording a decision, because `ToDo.md` is deleted at publication and a decision kept only there leaves no trace. Open ScholarPeer, the AI peer reviewer considered in ToDo B0, will not be tried. The external look at the paper before export is instead a single read by a second model, given `docs/ai-review-brief.md` and `main.md` and nothing else.

What the two would have bought differs. A second-model read costs nothing to set up and returns text-level criticism: wording that outruns its evidence, gaps in the argument, internal inconsistencies. Those change sentences. Open ScholarPeer's distinctive value is a literature search that looks for missing comparisons, and a missing source is the expensive kind of finding here: accepting one means an ingest, a set of new claims, a grinding pass and a re-check of the claims file, days after that work was completed for all 30 sources. The scope of this review is also already declared as non-systematic, so a fuller search does not repair a weakness the text hides; it would widen a review that says what it is.

The decision is reversible in one direction only, and the cheap moment is now: if the coverage starts to look doubtful it must be reopened before B1, since anything it adds would travel back through the claim check and then through the export. After the export it would cost the export twice.

## [2026-11-20] lint | the export build: three manual checklist items turned into a script

The export side of ToDo B1 listed four things to do by hand to `main.md` itself: a visible title block, clickable URLs, removing HTML comments, and the figures. Doing them in `main.md` would have damaged the draft, since the front matter is metadata the wiki workflow uses, the Mermaid blocks are read by `claim_quotes.py`, and HTML comments are working notes. They are now done to a generated copy instead.

`scripts/export.py --write` builds `main-export.md`: the Mermaid diagrams become image references to the rendered SVGs with alt text from the figure caption, a visible title block is written from the front matter (title, author, date, with `--date` to stamp another one), bare URLs become Markdown links, and HTML comments are stripped. The front matter is kept as well, since a converter that reads it gets the document title and one that does not drops it silently, as the test export did. On the current draft that is 2 diagrams, 31 URLs and 0 comments; `main.md` turned out to have no HTML comments left, so that ToDo item was already satisfied without anyone noticing. Existing Markdown links are masked before the URL pass, so the CoEBoC link and the thesis link were not double-wrapped, which a first version would have done.

`--export` moved out of `figures.py`, which now does one job, the diagrams and their hashes, and `export.py` reads the manifest it writes. `docs/print.css` carries the print rules: `break-inside: avoid` for figures and tables, a caption kept with its figure, repeated table headers, a hanging indent for the reference list, tables at 8.5 pt because Table 1 and Table 2 overflow at body size, and a forced light background in case the converter leaves a theme class on `<body>`. It states plainly what CSS cannot do: the running header and footer belong to the browser, and the only way to remove them is the print dialog. `docs/pdf-export-notes.md` gained a six-step build checklist and a verification list ordered by what has failed before, starting with opening the HTML offline to see whether the figures appear.

One finding from the work itself: `check.py` rejected the checklist text, because the sentence about the escaped hash contained an unescaped one. The rule caught its own documentation.

## [2026-11-20] draft | AI review 1 (ChatGPT): APD90 wording, Figure 2, FPDc range, gaps 2 and 3

The first external AI review (`docs/feedback1-from-AI-reviewer.md`, given `main.md` and `docs/ai-review-brief.md`) was gone through finding by finding, and its short Finnish summary added nothing beyond the two major findings. Changes to `main.md`:

- **T-wave peak and APD90 (finding 1).** "This anchors the T-wave peak, when the waveform is biphasic, to APD90" became "This is conditional evidence of a relationship between the two measurements, not validation of the T-wave peak as a general APD90 surrogate". The reviewer named the sentence and Figure 2; the same step from correlation to identity was also in the Timeline ("T-wave peak = APD90"), Table 2 ("coincided with") and the Outlook ("tracks"), all now "correlates with". Ernault et al. (2024) report a correlation; the wiki page also notes that FPD to the T-wave peak is longer than APD in ventricular iPSC-CMs, so the identity reading was not available.
- **Figure 2 (findings 1 and 4).** K is now "Correlates with APD90 in NRVM if biphasic T wave", L "Intended to capture full repolarization, not compared with the AP", so both branches carry the same level of caution and L matches Table 2, which already said so. NRVM sits mid-label because `check_abbreviations.py` read `\nNRVM` as the word "nNRVM".
- **FPDc (finding 3).** RR is now "in seconds". The sentence that read the accepted rate ranges (20–90 and 20–80 bpm) as a reason the formula "may under- or over-correct at the extremes" now says only that this has not been tested in the studies examined; the doxorubicin example of Lee et al. (2026) stays as the concrete case.
- **Gap 2 (finding 6)**, in the Conclusion and the Abstract: criteria for classifying waveform morphology "and for choosing the fiducial definitions valid within each class".
- **Gap 3 (finding 5).** The heading named ultra-high-density platforms, but all three pieces of evidence were 3D. The gap now names the two settings and their different problems, and the high-density side gets Lee et al. (2024) (minimal FPD–APD correlation on the same electrodes) and Matsuda et al. (2025) (spatial endpoints). The Abstract already said "three-dimensional and spatially resolved" and was left alone.

**Not done: the two 3D platforms (finding 2).** Choi et al. (2026, *Advanced Materials*, 10.1002/adma.202506793, shell MEA encapsulating organoids) and Kim et al. (2026, *Advanced Science*, 10.1002/advs.202514365, conformable MEA for hiPSC-derived organoids including Duchenne) exist: title, authors, journal and volume match in Crossref, checked 2026-11-20; Wiley blocked direct fetching. They are not ingested, so nothing was written into `main.md`. By their abstracts they advance 3D recording and use calcium imaging for corroboration, not the validation of fiducial definitions, so they would bear on the Lin et al. (2023) one-surface point and would sharpen gap 3 (acquisition is moving ahead of analytical validation) rather than close it. The reviewer's reason for including them (a "literature-search cutoff of 30 October 2026") misreads the Scope: that date belongs to the maturation search only.

`docs/claims-by-source.md`: Ernault (1), (2) with its `{q:}` regex, (4), (5); Mäki (7) with its regex; Lee 2024 (8) narrowed and (10) added; Matsuda (6) added; register items 4, 5, 11 and 14 updated with the new wording and the old in brackets, item 5 also with a note on the two un-ingested platforms. `figures.py --write` run; both SVGs still need rendering in Mermaid Live. No wiki pages changed: the edits reword existing claims and connect no new sources.

## [2026-11-20] ingest | Kim et al. 2026 — Conformable Microelectrode Arrays Integrated with a Scoop-Shaped Slide-Well for Dynamic Electrophysiological Profiling of Patient-Derived Cardiac Organoids

Suggested by AI review 1 as one of two missing 3D developments. The DOI, title, authors, journal and volume were checked against Crossref before the PDF arrived; `raw/kim-2026.pdf` and the supplement were renamed to the page stem (`kim-2026-organoid-mea`). Open access, CC BY, so no `.gitignore` entry is needed. Read in full (16 pp.), with the supplement unpacked and read, and Figures 1 and 4 inspected as images.

**What it is.** A roughly 4 µm thick six-electrode MEA is bonded by capillary adhesion into the concave floor of a PDMS "scoop" well; a millimetre-scale cardiac organoid rolls down the incline and settles on the electrodes under gravity. Organoids come from urine-derived hiPSCs of two healthy donors and two Duchenne patients. E-4031 prolonged FPD in normal organoids and triggered arrhythmia in DMD organoids already at 10 nM.

**Why it was taken.** Not because it closes a gap, but because it is a 2026 hiPSC-CM study that advances the recording geometry while stating no analysis convention at all. Neither the Experimental Section (notch filter, downsampling, wavelet denoising — that is the whole EFP analysis description) nor the supplement gives a fiducial rule, a peak-detection method or a single FPD value; "prolonged FPD" is read off representative traces, and the figures carry no fiducial markers. The authors also report repolarization metrics "only where waveform morphology supports interval quantification" (p. 12) and note that fragmented DMD waveforms break standard peak detection. That is gap 2 stated by other authors, and gap 3 shown rather than argued.

**Two readings in the AI review that the source does not support.** The abstract's "validated by calcium imaging" is not a per-electrode comparison of calcium with the field potential: Fluo-4 imaging compares whole normal and DMD organoids (Fig. S21c). And the device does not overturn the one-surface point of Lin et al. (2023): the electrodes lie in the floor of the well, so the organoid is contacted on its lower curved surface, not encapsulated. Both are on the paper page under Limitations.

**An unexpected find.** Figure S25 measures impedance at 300 Hz across 16 channels before and after the organoid makes contact, and uses the drop as a coupling check. The Discussion of `main.md` asks whether an impedance channel could indicate FP changes that come from altered cell–electrode coupling rather than from the cells; Altrocchi et al. (2023) used impedance for cytotoxicity. Kim et al. use it for coupling, in the contact direction, without relating it to the waveforms — one step closer to the hypothesis, and now cited there.

`main.md`: three sentences added (3D section, Conclusion gap 2, Discussion impedance paragraph) and the reference entry. The 3D section also gained an unsourced closing clause, that recording geometry for 3D models has advanced further than the analysis conventions applied to it; it is register item 27, `inference` over five studies. Wiki: new page `wiki/papers/kim-2026-organoid-mea.md`; `wiki/3d-models.md` (row and the open point), `wiki/fpd-end-conventions.md` (a row whose start and end are both "not stated" — the point of including it), `wiki/multimodal-measurement.md`, `wiki/index.md` (paper entry and two concept lines), `wiki/references.md`. `docs/claims-by-source.md`: four claims, checked at ingest, and register item 5 updated to record that Kim is in and Choi stays out. Choi et al. (2026) was not obtained in full text; an abstract is not a basis for a claim, so it is not cited.

One script change: `scripts/claim_quotes.py` had no pattern for Kim, so its claims silently collected no sentences until `"Kim": r"\bKim et al\b"` was added to `SOURCES`. Worth remembering at the next ingest — a new source needs a line there or its claims look empty.

## [2026-11-20] lint | claim_quotes.py no longer fails silently on a new source

Found during the Kim ingest the same day: the source had no pattern in the `SOURCES` table of `scripts/claim_quotes.py`, so `source_of` returned None, every claim in its section was skipped, and the quote lines were simply absent. Nothing was reported — the section looked like a source whose claims happen to have no sentences, which is also a legitimate state. That is the worst shape for an error in this repo: it reads as done.

Fixed in the script rather than in AGENTS.md, following the rule that a mechanical requirement belongs in the harness. `resolve_sources` now builds the pattern table from the file itself: a `## ` section not in `SOURCES` (the register section excepted) gets `\bSurname\b` derived from its title, and a note says which pattern was derived and when to replace it with an explicit entry. Where a surname heads two sections — the Lee, Li and Park pairs — the script refuses to guess a year, collects nothing and says so, which is the one case that still needs a hand-written pattern. Both branches were tested by removing the Kim entry and by appending a second Kim section.

The explicit `"Kim"` entry was kept: derivation is a safety net, not the preferred state. AGENTS.md ("Claims file") now says a new source needs no script edit, when an explicit entry is still required, and that the Notes of a `--write` run are the place where a source that collected nothing shows up.

## [2026-11-20] lint | a highlight left asserting what the body no longer claims

Checking whether `main.md` was ready for the figure and export step turned up one real inconsistency, caused by the morning's own edit. Highlight (2) read "No validated hiPSC-CM rate correction found; Fridericia can mislead at extreme rates", while the FPDc section had been reworded a few hours earlier, after AI review 1, to say that whether the formula under- or over-corrects at particular rates has not been tested in the studies examined. The highlight therefore asserted what the body had just withdrawn.

It now reads "in one study the correction reversed the direction of an FPD change", which is the doxorubicin case of Lee et al. (2026) and already a checked claim. Register item 0 (2) records the old wording and why it went.

Worth noting as a pattern rather than a one-off: the Highlights and the Abstract restate the gaps in their own words, and neither `check.py` nor `claim_quotes.py` can see that a summary has drifted from the section it summarises — the register is the only place the link is written down. After rewording a claim in the body, read register item 0 and the Abstract before calling the change done.

## [2026-11-20] draft | Highlights: the one gap that had no highlight

Reading the four gaps against the six highlights showed that gap 3 was the only one not summarised: rate correction, maturation and morphology each had a line, the transfer of 2D-calibrated analysis to 3D and spatially resolved recordings had none. Added as "2D-calibrated analysis is carried over to 3D tissues and to high-density arrays, validated in neither", which follows the two-setting split the gap was given earlier the same day. Register item 0 now lists seven highlights; the machine-learning and signal-separation lines are renumbered (5)→(6) and (6)→(7), with the old numbers noted so the history stays readable.

Figure 1 was checked at the same time and left alone. Nine post-2022 sources are not on it (Altrocchi, Clements, Hu, Karami, Kim, Li 2024, Lin, Park 2026, Vuorenpää), so it is a selection of 19 entries, not a chronology of the corpus. The caption does not say so, which is the open question left for the researcher.

## [2026-11-20] draft | Figure 1 caption states what the timeline is a selection of

Decision by the researcher: fix the caption, not the figure. The old caption, "Timeline of key methodological developments in cardiomyocyte MEA analysis, 2022–2026", promised more than the figure delivers — nine post-2022 sources carry no entry (Altrocchi, Clements, Hu, Karami, Kim, Li 2024, Lin, Park 2026, Vuorenpää) against 19 entries on it. The caption now says the entries are a selection chosen to show the range, names the three kinds of source that are left out (reviews, the non-peer-reviewed acceptance standard, studies whose contribution is to the recording rather than the analysis), and states that the figure is a chronology neither of the field nor of the reference list.

This settles two asymmetries found while checking: Pramudito et al. (2026) is on the figure and Park et al. (2026) is not, though both are 2026 machine-learning risk classifiers; Lee et al. (2026) is on it and Hu et al. (2026) is not, though both pair transparent electrodes with optical recording. Under the old caption those looked like omissions; under the new one the figure never claims to be complete. Adding Park et al. (2026) was considered and declined — the 2026 row already carries five entries and has to stay legible in the PDF.

Register item 36 records the caption. The diagram itself is unchanged, so `figures.py` reports no drift and the `.mmd` files are still in step; the caption sits outside the fenced block and reaches the export as the image's alt text.

Also fixed here: the item added this morning for "recording geometry has advanced further than the analysis conventions" had been numbered 27, which was already the impedance item. It is now item 35, with the collision noted. The register has 37 items and no duplicate numbers.

## [2026-11-20] draft | gap 3 hedged like the other gaps, and the review's second round answered

The second round of AI review 1 asked for two things: a one-sentence mention of Choi et al. (2026) written from its abstract, and softer wording for gap 3.

**Choi stays out.** Its bibliographic details are verified in Crossref, so this is not a question of whether the paper exists; it is a question of what may be claimed from an abstract. The review's one hard guarantee is that every claim has been checked against its source, and limitation (v) says full texts were consulted wherever available. The sentence the reviewer proposed also repeated the construction that reading Kim's full text had just caught: Kim's abstract says the waveforms were "validated by calcium imaging", while the full text compares whole organoids, not electrode by electrode. The reviewer itself grants that Choi resolves nothing central. Register item 5 records that the paper is known, verified and consciously left out.

**Gap 3 was reworded, but not as asked.** The real defect was narrower and was ours, introduced by the first-round rewrite: gap 3 had become the only one of the four stated as a fact about the literature instead of as a finding of this review. Gaps 1 and 2 say "was found" and "were not identified"; gap 4 states an absolute, but it is the gap with a documented search behind it. Gap 3's Support is `thin` — absence limited to the studies examined — so the heading promised more than the register allows. It now reads "Dedicated validation of 2D-calibrated analysis frameworks was not found for either 3D tissues or spatially resolved recordings, two settings that pose different problems." The reviewer's own wording was not used: it drops "calibrated on 2D monolayers", which carries the point, and adds "systematically", which is vaguer than the hedge needed.

A written response to both rounds now sits at the end of `docs/feedback1-from-AI-reviewer.md` under "Meidän vastine tähän": what was changed, what was not, and why. It also records the two defects the review process surfaced that no finding mentioned — the highlight that outlived its claim, and Figure 1 promising more than it delivered.

## [2026-11-20] draft | AI review 2: three changes made, four findings declined

A second AI review (`docs/feedback2-from-AI-reviewer.md`, a different model) argues that the four-gap framing is overdrawn relative to a thin, non-systematic sample, and that the main fix is to stop presenting the sample's silences as field-wide gaps. Each of its eight findings was checked against the text.

**Made:**

- **Gap 1 (finding 1).** The heading was already hedged ("was found"), but the sentence under it was not: Fridericia "lacks formal validation for the beating rate range and rate–FPD relationship of hiPSC-CM cultures". The reviewer missed the defence — the CiPA authors say the same (Blinova et al., 2018) — but the real defect is adjacent and was ours: that statement is from 2018, and the sentence carried it to the present tense as a fact about the field, which register item 3 already says would need a documented search first. It now attributes and dates the statement and limits the absence since then to the studies examined. Blinova claim (4) gained the Conclusion tag.
- **Motivation (finding 5).** "None of them applies two analysis conventions to the same recordings" became "None of the studies reviewed below ...". The antecedent was the previous sentence, so the scope was already bounded, but a sentence-initial "None of them" reads loosely.
- **Discussion (finding 7).** A bridging sentence now says that neither hypothesis solves the four gaps and what they address instead. Register item 37, `opinion`; it lowers the claim rather than raising it.

**Declined, because the text already does what is asked:**

- **Finding 2 (gap 2 conflates classification with fiducial rules; baseline return as benchmark).** That Ernault, Weiser-Bitoun and Kim are not trying to solve morphology classification *is* the finding, not a conflation — and the claims file already records that Weiser-Bitoun's "awareness" is read off its algorithm rather than stated by its authors. On the benchmark charge, the fiducial section says the two definitions "may therefore measure different quantities rather than one being universally more correct", Table 2 and Figure 2 were hedged earlier the same day, and Limitations (iv) calls the author's convention one of several.
- **Finding 3 (gap 3 bundles geometry, contact and spatial mapping).** The split the reviewer asks for is in the gap's own paragraph: 3D geometry changing electrode contact and signal contributions, high-density arrays raising how local fiducial points and propagation metrics relate to the cells. The reviewer appears to have read the bold heading only.
- **Finding 4 (gap 4 self-undermined, outside MEA scope).** Its suggested reframing — a reporting and confounding issue, maturity rarely measured alongside MEA in the same wells — is the text's own wording ("what is missing is an independent maturity measure taken on the same MEA cultures"), as is the limit to the electrophysiological axis.
- **Finding 8 (tension with Vuorenpää).** Limitations (iv) keeps that tension visible, which is what the finding asks for.

**Not taken: the reframings of gaps 1–4.** Recasting them as "practices vary" would be weaker than the material allows and, for gap 1, weaker than what the CiPA authors themselves wrote. Finding 6 (Botti "not fitted", small test sets) was left for the language pass.

Two reviews now point the same way, which is a reason to watch for over-hedging rather than to keep hedging: the gaps are already scoped to the studies examined in the Abstract, in three of four headings, and in Limitations (i). The fourth is the one with a documented search behind it.

## [2026-11-21] draft | the four gaps in the Abstract become a real list

The researcher had split the Abstract into three paragraphs and put the four gaps on separate lines. The paragraph split is an improvement and was kept. The gap enumeration was not doing what it looked like: the four lines ended in a single trailing space, which Markdown reads as a soft break, so Pandoc would have rejoined them into one running paragraph and the exported PDF would have looked exactly as before. It also left one paragraph spread over five lines, against the no-soft-wrap rule in the researcher's own instructions, which allows a line break only where it is real structure.

They are now a bulleted list, which is real structure and survives to the PDF. The roman numerals are plain, not italic and not bold: the Limitations list already uses plain `- (i)` through `- (vii)`, so the Abstract was the only place with italic numerals, and bold is reserved here for the gap headings in the Conclusion and for the phrase "four methodological gaps remain". No wording changed; register item 3 records the change of form.

Nothing broke in the scripts, and nothing would have warned if it had: no source claim carries the `[Abstract]` tag, and register items are quoted by hand rather than generated, so `claim_quotes.py` never reads these lines. Checked before editing rather than after.

## [2026-11-21] draft | the Highlights now say what was found, the Abstract what is missing

The researcher asked whether the Abstract's new gap list repeats the other sections. The Abstract-to-Conclusion overlap is what an abstract is for and was left alone, except that gap (ii) is worth varying later: both now carry the same long clause word for word, from the widening on 2026-11-20. The Highlights were the real duplication, and it was ours: four of the seven lines restated the four gaps, so the gaps were stated three times before the body, and the set became an exact parallel of the Abstract list the day before, when the gap that had no highlight was given one.

Rather than deleting a highlight or accepting the repetition as the journal convention it is, the division of labour changed: the Highlights now carry findings and the Abstract carries the gaps. The four restatements were replaced by four findings already checked against their sources — the one FPD end point tested against intracellular recordings and the condition it holds under (Ernault), rate correction reversing the direction of an FPD change (Lee et al., 2026, doxorubicin), FPD drifting over days in culture even under fixed-rate pacing (Guerrelli), and recording geometry for 3D models having moved ahead of the analysis (register item 35). The machine-learning line lost "Without these", which no longer had an antecedent once the preceding lines stopped being the gaps.

One line was dropped rather than replaced: "Raw MEA signals mix cell, tissue and device; separating them is proposed as a hypothesis". It was the only highlight that led with a hypothesis of the author's, which does not fit a list of findings; the hypothesis stays in the Discussion. Register item 0 records every old wording, including this one, and notes that re-adding it would be a judgement call rather than a correction.

A consequence worth keeping in view: yesterday's "one gap has no highlight" problem no longer exists, because the highlights are no longer a mapping of the gaps. That earlier fix was right for the structure as it then was and is what made the duplication visible.

## [2026-11-21] draft | Highlights shortened to seven, and the gap (ii) duplication broken

Two small things after the rewrite earlier today.

**Gap (ii) now reads differently in the two places it appears.** The widening of 2026-11-20 had left the Abstract and the Conclusion carrying the same long clause word for word, so the pair read as copied rather than summarised. The Abstract now says "the absence of shared criteria for sorting waveforms by shape, and for deciding which fiducial points remain meaningful in each shape"; the Conclusion keeps the technical wording. Same claim, plainer words.

**The Highlights were measured rather than eyeballed.** With the separation hypothesis restored at the researcher's request the list stood at eight lines, 686 characters, four of them over the 85-character convention — a paragraph's worth of text, which stops being a list one can scan. It is now seven lines and 570 characters, the longest 92. Two lines were merged: the drift under pacing and the rarely measured maturity, which belong together because the drift is what makes the missing measurement matter. The others were tightened without losing anything.

One shortening was declined. "Intracellular recordings" could have become "an action potential", saving five characters, but it is exactly what separates Ernault's sharp-microelectrode comparison from the intracellular-*like* electroporation signals of Lee et al. (2024), and it is what makes "the one" true. "In rat cells" was dropped from that line instead; the species is still in the Fiducial section and in Table 2.

Register item 0 carries every old wording and the reasoning for each merge, so the seven lines can be traced back to the eight they came from.

## [2026-11-21] draft | the APD90 highlight made plain, and the 3D highlight dropped

Two changes the researcher asked for after reading the shortened list.

**The second highlight was unclear, and the diagnosis was grammatical.** "The one FPD end point tested against intracellular recordings held only for biphasic T waves" makes the reader unpack a reduced relative clause — the one end point *that was* tested — before the sentence resolves, and then "held" never says what held. It now names the landmark and the measure outright: "In rat cells, the T-wave peak correlates with APD90 only when the T wave is biphasic". Shorter by 23 characters, and the rat caveat fits again.

What the plainer line gives up is the claim that this is the *only* end point ever tested against intracellular recordings. That fact stays in the Abstract; the conditionality, which is what AI review 1 required, is what a highlight should carry. APD90 is used unspelled, consistent with FPD and MEA in the same list, and the Abbreviations section follows immediately — checked against `check_abbreviations.py`, which passes.

**The 3D highlight was dropped,** at the researcher's judgement that 3D sits at the edge of this review rather than at its centre. It was also the one highlight resting on an inference across five studies rather than on a finding from one. Gap 3 is unaffected: it is stated in the Abstract and the Conclusion, and register item 35 keeps the inference.

The list is now six lines and 483 characters, the longest 88 — from eight lines and 686 characters this morning, with no claim lost that is not stated elsewhere. Register item 0 holds every wording the list has had today.

## [2026-11-21] draft | the maturation absence returns to the Highlights, as the one with a search behind it

The researcher noticed that the morning's rewrite had lost "No validated MEA-derived reference values for hiPSC-CM maturation were found", first by replacing it with a statement about practice and then by merging that away. The instinct was right, and for a better reason than the line reading well.

Gap 4 is the only one of the four with a documented search behind it: PubMed/MEDLINE on 30 October 2026, no date limit, with citation chasing and bioRxiv searches, recorded in `docs/maturation-mea-search.md`. The other three are of the form "not found among the studies examined", which is a limit of the sample. That difference makes gap 4 a result of this review rather than a scoping statement, which is why it belongs in a list of findings even though the division of labour otherwise leaves the gaps to the Abstract. The highlight says "A documented search found no ..." so that the distinction is visible in the line itself rather than only in the register.

The drift finding stands alone again, as it did before the merge. The practice statement that replaced the absence claim — maturity is rarely measured in the same wells — stays in the Maturation section and the Conclusion, where it belongs.

Seven lines, 525 characters, longest 88. Register item 0 now records three states for this line in one day: restated gap, replaced by a practice statement, merged away, restored with the search named.

## [2026-11-21] draft | the maturation highlight names PubMed

The line settled after three wordings were weighed against each other. "A documented search found no MEA-derived reference values for hiPSC-CM maturation" became "A PubMed search ...": naming the database is concrete and checkable, where "documented" only asserts that documentation exists somewhere. The search is PubMed/MEDLINE with citation chasing and bioRxiv web searches, so the line names its core rather than all of it; the Scope and the Maturation section carry the full description.

Two shorter forms were declined, both proposed by the researcher and both defensible. "No MEA-derived reference values for hiPSC-CM maturation were found" takes the same shape as the three gap restatements removed from the list that morning, so it hides the one thing that earns this line its place. "hiPSC-CM maturation is missing MEA-derived reference values" is the Conclusion's gap 4 heading almost word for word — it would have put the same sentence at both ends of the paper, which is the duplication we removed between the Abstract and the Conclusion for gap (ii) the day before. A grammatical slip was fixed on the way: the source sentence reads "No **study** ... **was** found", and shortening it to "reference values ... was found" left the verb agreeing with nothing.

Highlights now: seven lines, 521 characters, longest 88. Register item 0 holds every wording of the day with the reason each was kept or dropped.

## [2026-11-21] draft | a paragraph between the Literature review heading and Figure 1

The section opened straight onto the figure caption, so the reader met a diagram before being told what the section does. Three sentences now stand between them: the developments are grouped by the analysis problem they bear on rather than by year, with the seven problems named in the order the subsections take them; several studies bear on more than one and are discussed in more than one subsection; and Figure 1 keeps the chronological view alongside that grouping.

The last point also gives the figure a job. Until now the timeline sat in a section organised by theme without anything saying why both views are there.

Nothing is claimed about the literature, only about this review, so no citation is involved; register item 38 records it as `sourced` by the draft itself, like item 36 for the figure caption. The diagram is untouched, so `figures.py` reports no drift.

## [2026-11-21] draft | the Scope section split into three paragraphs

The section was one paragraph carrying four separate things: what kind of review this is and how candidates were found, the one documented search, what was not recorded about the rest of the selection, the subject-matter limit on 3D and in silico work, and the author's own opinion paper as the evaluative anchor. It now reads as three: how the selection was made, what that method does not cover, and the evaluative framework with its competing interest. The break points are the end of the documented-search sentence and the end of the 2D-to-3D scope sentence.

One error fixed in passing: "research assistants working from the terms like" lost its article mismatch and reads "from terms like".

No wording else changed and no claim moved section, so the quotes under the Scope claims are the same sentences at new line numbers; `claim_quotes.py --write` refreshed them and reported nothing.

## [2026-11-21] draft | the documented search names its file, and the archival gap is written down

The Scope said only that the record of the maturation search "is in the project repository (see Declarations)", which left the reader three steps from it: find the Declarations, follow the GitHub link, then find one file among hundreds. The sentence now names it: "its record is in the project repository, as docs/maturation-mea-search.md (see Declarations)". Written as plain text, because `main.md` uses no inline code formatting anywhere else.

The chain was checked end to end rather than assumed: the file exists and is tracked (142 lines, written 30 October 2026), the Declarations give the repository URL under Data and code availability, the repository answers unauthenticated, and the raw file is reachable there. The promise is not empty.

What the check did surface is that the link is to a mutable repository while the preprint is permanent — and this is the claim the review leans on hardest, now also in the Highlights. That is a publication-time decision, not a text change, so it went into `ToDo.md` under B2: archive a repository snapshot to Zenodo through a GitHub release at the same time as the preprint, and use its DOI in the "is supplemented by" related identifier.

## [2026-11-21] draft | the 3D section split into three paragraphs

One paragraph carried three different jobs: whether 2D-calibrated endpoints transfer at all (Mäki's caution, the Hwang simulations, the Maurissen 2D-versus-3D comparison), what is being done about the recording and the tools (Lin on one-surface contact, PhysioMEA targeting organoids but analysing in the plane, Kim's conformable array), and what is still open. It is now three paragraphs on those lines, with the closing sentence standing alone so the gap is not buried at the end of a long block.

No sentence was moved. A reordering is available and was not taken: Kim sits after PhysioMEA, so the middle paragraph alternates recording, tools, recording. Putting Kim next to Lin would group the recording-side points, at the cost of separating the two 2026 organoid studies, which the text currently contrasts — an analysis tool that states its convention and a device paper that states none. That contrast is worth more than the tidier grouping, so the order stands.

Quotes refreshed; the Scope and 3D claims keep the same sentences at new line numbers.

## [2026-11-21] draft | the recording chain named, and the Discussion given real subheadings

**The electronics are now named rather than gestured at.** The outlook said an FP reflects "the cellular action potential (AP) and the recording electronics", which left the reader to guess how much of the instrument that covers; the amplifier appeared only later, inside the equivalent-circuit sentence. It now reads "the recording electronics, from the electrode and the conductive tracks leading to it through to the amplifier". Both ends are sourced: Karami et al. (2026) build the electrode impedance from a Randles circuit plus spreading and metal resistance — the tracks — and the amplifier impedance, and Lee et al. (2026) are already cited at the end of the section for chip composition and recording hardware altering absolute signal values. Karami claim (1) records the addition.

**The two parts of the Discussion are now `##` subsections** instead of bold run-in labels, matching how the Literature review is structured. The researcher asked for visual separation and was unsure whether subheadings were right; they are, because the Discussion was the only `#` section carrying two long themes with nothing in the table of contents to show it.

That change broke something that would not have announced itself. `claim_quotes.py` assigns each sentence to the section heading above it, and an unmapped heading becomes a tag of its own — so both new headings silently took every sentence out of `[Outlook]`, and all 33 Outlook claims lost their quotes at once. The dry run showed it before anything was written; `SECTION_TAG` now maps both subsection titles to `Outlook`, with a comment saying why. A second instance of the same lesson as the Kim ingest: this script fails by producing nothing rather than by erroring, so a structural edit to `main.md` deserves a dry run before a `--write`.

## [2026-11-21] lint | the section table completed, and an unmapped heading now says so

Asked whether this morning's lesson was written down anywhere, the honest answer was half. AGENTS.md had the `SOURCES` half from yesterday — a new source needs no script edit, and the Notes are where a source that collected nothing shows up — but nothing about `SECTION_TAG`, which is what the Discussion subheadings broke.

Worth correcting one thing said earlier today: that failure was not silent. The run reported 33 claims finding no sentence. What it did not do was name the cause, so the reader sees 33 symptoms and has to infer the one change behind them.

So the fix is in the script rather than only in the text. `SECTION_TAG` now holds every heading of `main.md` — Highlights, Abbreviations, Acknowledgements and About the author were missing and worked only because an unmapped heading falls back to its own title, which happened to match the tag the claims used. With the table complete, any unmapped heading is an anomaly, and `main_sentences` reports it with its line number and what it does to the claims, ahead of the claims that went empty because of it. The YAML front matter is skipped too: `# output: html_document` inside it had been parsed as a heading all along.

Tested both ways: the current draft produces no notes, and renaming one subheading produces the heading note first, followed by the Outlook claims it emptied.

AGENTS.md now carries both failure modes in one place, with the rule that follows from them: this script fails by producing nothing rather than by erroring, so read the Notes after every run, and after a structural edit to `main.md` run it once without `--write` before writing.

## [2026-11-21] draft | the title stops claiming what the text only calls plausible

Two days of scoping the claims had left the title as the strongest statement in the paper, which is backwards: "Four Gaps Limiting Comparability in MEA Analysis of hiPSC-Cardiomyocytes" asserts both that the gaps exist in the field and that they limit comparability, while register item 2 says fiducial definitions are "a plausible source of variability and a possible limit to inter-study comparability", `inference`, only plausibility claimed — and Limitations (iv) admits the premise is not universally shared, citing Vuorenpää et al. (2023) against it. The same defect as the highlight that outlived its claim, in the one sentence most readers see alone.

It now reads **"Four Methodological Gaps in Field Potential Analysis of hiPSC-Cardiomyocytes: A Narrative Review of Multielectrode Array Studies Since 2022"**. "Methodological" replaces the unproven effect, the subtitle states the scope the old title left to the description, and the words readers search for — field potential, multielectrode array — are in it. The "four gaps" spine stays, because the Abstract and the Conclusion are built on it.

The description carried the same claim and was reworded with it: "In the studies examined, four methodological gaps remain", with gap 2 and gap 3 brought into line with the wordings the Conclusion settled on this week. `README.md` carries the title too and was updated; `main-export.md` is generated and git-ignored, so it will pick the title up at the next `export.py --write`. The old title survives in `docs/private/llm-wiki-post/`, which is the researcher's own draft and not edited from here.

## [2026-11-21] draft | the byline carries the degree, and About the author carries the ORCID

The author field now reads "Antti-Juhana Mäki, D.Sc. (Tech.), Independent researcher", and About the author ends with the ORCID as a bare URL. The degree is written as D.Sc. (Tech.), not PhD: the section itself says a D.Sc. (Tech.) from Tampere University of Technology, and PhD would have been the wrong name for it.

The reasoning for having both is that they do different work. The byline tells a reader of a single-author, non-peer-reviewed preprint that the author is trained in the field, where "Independent researcher" alone can read as no background at all. The ORCID is the machine-readable half: it ties this preprint to the rest of the author's record and is what the Zenodo deposit will ask for.

Two small things checked rather than assumed: `check_abbreviations.py` flagged ORCID, which is the name of a registry and not an abbreviation to spell out, so it went into `IGNORE` beside PubMed and MEDLINE; and `export.py` was run to confirm the bare URL becomes a link in `main-export.md` without swallowing the sentence period.

## [2026-11-21] lint | the claims file stops storing main.md line numbers

The researcher noticed that every quote line in `docs/claims-by-source.md` ends with `— main.md:NNN`, so any structural edit renumbers all of them and the diff hides the one change that matters. Measured before deciding: the staged diff at that moment was 246 changed lines, of which 246 differed only in the number and **none** in content; across the twelve commits that touched the file, 1152 of 1261 changed lines were line numbers alone, 91 %. Structural edits produced 123–256 noise lines with 0–4 real ones, while content edits diffed cleanly.

That is not only noise, it is why a defect got past review this week: the highlight that kept claiming what the body had withdrawn was found by reading, not from the diff it should have stood out in.

The quotes now carry no line number. `quote_lines()` returns `(line, number)` pairs — the line is stored, the number travels alongside so the dry run can print it beside each quote. The jump-to-line workflow survives where it is useful, while the git history stops carrying data that is stale the moment a paragraph is added. Same principle as `main-export.md` being generated and ignored.

Four options were weighed. Dropping the pointer entirely and keeping it in the tool's output were the same change to the file, so they merged. A stable locator (`— Fiducial §3`) still churns within a section and repeats the tag the claim line already carries. A git-level fix was rejected on inspection: `.gitattributes` with a `textconv` driver needs local `git config` that does not travel with a clone, which is wrong for a template repo, and `git diff -I` would hide genuinely changed quotes too, since those lines match the same pattern.

Verified rather than assumed: no script parses the pointer, so nothing broke mechanically; and after the change, inserting a paragraph before the Conclusion — which shifts every line number below it — leaves the claims file byte-identical. The one-off cost was a single 246-line commit.

One real dependency did turn up and was fixed: `.claude/skills/grinding/SKILL.md` told the reviewer that the `- >` lines come with line numbers and to check those numbers against `main.md`. It now says to check the quoted text, and points at the dry run for line numbers. AGENTS.md records the format, the reason and the dry-run affordance.

## [2026-11-21] lint | the line-number removal verified against five cases

The change above was committed on the strength of one test. The researcher asked the right follow-up — what happens when a change to `main.md` moves the linked line for most claims, not just a few — so it was tested properly afterwards. Five cases, with the working tree checksummed before and restored after.

| | What was done | Result |
|---|---|---|
| A | Five paragraphs inserted after the Abstract, shifting the line of **all 246 quotes** | the claims file came out byte-identical |
| B | One quoted sentence reworded (the Kim impedance sentence) | exactly two lines changed — the two claims that quote it |
| C | Every printed line number checked against the line it names, after the shift | 245 of 246 matched; the one miss was the test's own fault |
| D | A sentence no claim quotes deleted | no notes, as it should be |
| E | A sentence Kim claim (4) quotes deleted | reported: "no sentence found in main.md matching {q: measured it at a single frequency}" |

Case E is the one that answers the underlying worry. Dropping the stored numbers did not weaken the check that a quote still exists: a sentence that disappears or drifts out of its `{q:}` pattern is still named in the Notes. It is now easier to see, because it is no longer printed beside 246 renumbered lines.

Case C's single miss is worth recording so nobody reads it as a one-in-246 defect: the line is a Mermaid label containing a literal `\n`, which `main_sentences` replaces with a space before matching, while the comparison in the test looked for the replaced text in the raw line. The number was right; the test was wrong.

Why it works at all: the line number was never used to find anything. Quotes are re-derived on every run from the section tag and the citation pattern, so the number was only ever an output that happened to be stored. Removing it took away nothing the matching relies on.

## [2026-11-22] lint | wiki audit: a missing theme, two dead ends, two phantom nodes

The researcher asked for a critical pass over `wiki/`: graph quality, links between pages, and whether the tags are the right ones. Measured rather than eyeballed, across all 45 pages.

**What held up.** No orphans; every one of the 31 paper pages links at least one concept page and 3–10 other papers; all 17 vocabulary tags in use and none outside it. Near-duplicate tags were checked by co-occurrence rather than by eye: the highest Jaccard overlap is 0.50 (`cardiac-safety`+`rate-correction`, `fiducial-definition`+`open-platform`), which is two different things that travel together, not one thing named twice — a duplicate would sit at 0.8–1.0.

**The real gap: one section of main.md had neither a tag nor a concept page.** "High-throughput and long-term assays" was the only one of ten. Six pages carry the theme, twice the threshold AGENTS.md sets for a new tag. Added `high-throughput` to the Tag vocabulary and to Altrocchi, Guerrelli, Matsuda, Clements, Lee et al. (2026) and Fetterman, and wrote `wiki/high-throughput-assays.md`. The new page makes the point the scattered pages could not: three of those sources show an endpoint moving with no treatment — vehicle drift over four days, equilibration and culture-time drift, and a rate correction reversing the sign of a drug effect — and in all three the Fridericia correction fails to absorb it, which is why this material supports gap 1 rather than standing beside it.

`check.py` accepted the new tag without being touched: it reads the vocabulary out of the AGENTS.md line itself, so the rule lives in one place. Worth remembering before anyone adds a second list.

**Two pages carried a single tag**, against the two-to-four convention: Fetterman and Li et al. (2025), both only `maturation`. Fetterman is a high-throughput screen, so the new tag fits it. Li et al. (2025) got `rate-correction`, which its page earns — Fridericia-corrected FPDc drug responses, including the E-4031 prolongation absent in B27 cultures.

**One tag had to give way.** Altrocchi was already at four, and the theme genuinely applies, so `signal-separation` was dropped from it: the paper's own contribution is recording impedance alongside the field potential, while separation is this review's hypothesis about what such a channel could do. The `signal-separation` concept page still links Altrocchi, so no graph edge was lost — only the tag-level grouping. Say so if the trade reads wrong.

**Two concept pages were dead ends in the concept backbone** — `hipsc-cm-maturation` (13 inbound) and `critical-assessment-maki-claims` linked only to paper pages, making stars rather than a network. Both now carry a "See also (concept pages)" block. The maturation one was the more wrong of the two: culture-time drift, rate correction and the video classifier are the same argument seen from three pages.

**Two phantom nodes removed.** `log.md` referenced `[[wiki/citation-issues.md]]` and `[[wikilinks]]`, a deleted file and a word in prose, which Foam and Obsidian draw as placeholder nodes. The history is unchanged; only the brackets went, so the entries still say what happened. `references.md` also had no inbound link and is now reachable from `index.md`.

After the pass: no unresolved links, no orphans, no dead ends among concept pages, no page with fewer than two tags.

## [2026-11-22] lint | README: claim counts rounded

The README gave exact counts (199 claims across 30 sources, thirty-five registered inferences), which had already gone stale: the Kim ingest and the register items added on 2026-11-20 and 2026-11-21 brought them to 205 claims, 31 sources and 39 items. The README now says "over 200 claims across more than 30 sources" and "nearly forty statements", and points to `docs/claims-by-source.md` for the exact counts, one checkbox per claim. A rounded figure stays true through the next few ingests, where an exact one goes stale silently.

## [2026-11-22] lint | three new checks, and the hook now covers the claims file

Guards for the failures that the log of the past weeks recorded as found by eye. `scripts/check.py` now warns when the first author on a paper page differs from the key the page and its reference entry are filed under (the Ismaili author order was wrong until 2026-11-09), and when a claim or register number is used twice within one section of `docs/claims-by-source.md` (two register items 27 on 2026-11-20); it also reports highlights longer than 85 characters, as INFO because a preprint has no hard limit (two of the seven are 87 and 88 characters now). `scripts/claim_quotes.py` gained `--check`, which prints only whether the claims file is out of date with `main.md` and the Notes, and the PostToolUse hook runs it after every edit of `main.md`: both failure modes of that script produce nothing rather than an error, so the Notes now reach the agent at the moment of the edit instead of at the next `--write`. Each check was tested by planting the error (a swapped first author, a duplicated register number, a renamed Outlook subheading) and restoring the files afterwards. `AGENTS.md` and `README.md` describe the additions.

## [2026-11-22] draft | Motivation: Weiser-Bitoun 2026 cited for the standardisation call

The premise of the review, that analysis methods and fiducial definitions in particular are a plausible source of inter-study variability (register item 2, `inference`), rested on the author's own opinion paper and on indirect findings, which AI review 2 named as a weakness. The log of 2026-11-20 had recorded the one outside statement of it: Weiser-Bitoun et al. (2026), Discussion 4.2, p. 11, conclude that standardising peak detection and biomarker calculation matters for comparability between studies of cardiac organoids. At the researcher's decision the Motivation now cites it right after the plausible-source sentence: "The developers of one open platform make a similar call for cardiac organoids: noting that amplitude and slope values vary widely between studies, they recommend standardising peak detection and biomarker calculation to improve comparability (Weiser-Bitoun et al., 2026)."

The wording carries the limits of the passage: it is about organoids, its evidence is amplitude and slope rather than FPD (their FPD values matched earlier reports), the causes it names include equipment and culture time, and it is a recommendation rather than a measurement. So register item 2 stays `inference`, with a note. New claim Weiser-Bitoun (9), left unticked for the author; the section has lost its ✅ until then. Wiki write-back: the Relevance section of `wiki/papers/weiser-bitoun-2026-physiomea.md`. The new PostToolUse check reported the missing claim immediately after the edit ("cited in main.md section [Motivation] but no claim carries that tag").

## [2026-11-22] lint | register quotes checked against main.md

Phase 3 of the plan made after reading the whole log: the defect of a summary outliving its claim (the highlight of 2026-11-20 that kept asserting what the body had withdrawn, and the title that was the strongest claim in the paper) had been found by reading only. The plan was to generate `{q:}` quote lines for the register items as for the source claims. That would have duplicated the register's hand-written **Text:** quotes, which are curated and carry history, and added a large diff. Instead `claim_quotes.py` now checks those quotes: every double-quoted wording on a **Text:** line or a highlight line of item 0 must still occur in `main.md` (ignoring case, emphasis and line breaks; split at an ellipsis; quotes inside parentheses or followed by "became" are history and skipped). A missing one is a Note, so it also reaches the PostToolUse hook through `--check`.

The first run checked 92 quoted fragments and found three that had drifted: item 6 still quoted "exist separately" where `main.md` has said "have been reported separately" since 2026-11-02; item 22 quoted a clause that had become its own sentence; and item 23 still quoted "may become a more integral layer", although the researcher had strengthened it on 2026-11-13 to "are likely to become an integral layer" and recorded that in an Update line without changing the Text line. All three now quote the current wording, with the old one in parentheses. Tested by changing a highlight in a copy of `main.md`: the Note named register item 0 and the quoted line. `AGENTS.md` (Register paragraph) describes the check.

## [2026-11-22] lint | log split, a NUL byte repaired, two conventions written down

Phase 4 of the plan made after reading the whole log. (1) The 125 entries from 2026-06-17 to the end of October moved unchanged and in their original order to `wiki/log-2026-06-to-10.md`; `log.md` keeps November onwards, links the archive from its header, and its format block now lists `grill` too. `check.py` treats the archive as a non-page and checks its headers as well; `AGENTS.md`, `README.md` and `wiki/index.md` name it. November alone is still about 160 kB, more than one read of an agent takes, so a further split may be needed. (2) The Park et al. (2026) supplementary entry of 2026-10-18 had contained a NUL byte since it was written ("ML input: [NUL]hange of FPD"), which made grep treat the whole log as binary and silently return nothing; it now reads "percent change", as the paper page does. (3) `AGENTS.md` now states the reference-year rule (issue year once volume and pages exist, decided three times: Botti, Park 2026, Weiser-Bitoun) and that decisions go in the log, since `ToDo.md` is deleted at publication. (4) The grinding skill tells the agent to re-read the title, the Highlights and the Abstract after a change of wording.
