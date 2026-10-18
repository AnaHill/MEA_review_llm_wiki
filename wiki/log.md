# Wiki Log

Append-only chronological record of all wiki operations. Each entry starts with a consistent prefix for grep-parseability.

Format:
```
## [YYYY-MM-DD] ingest | Author Year — Paper Title
## [YYYY-MM-DD] query | Question summary
## [YYYY-MM-DD] draft | Section updated
## [YYYY-MM-DD] lint | pass
```

---

## [2026-06-17] init | Academic wiki template initialized

Bootstrapped wiki structure. No sources ingested yet.

---

## [2026-07-02] query | Post-ingest verification of Correia et al. 2024 — Table S2 read-through + Figure 7F visual check

The initial Correia/Scheurer ingest used text-only extraction throughout; on review, this left two gaps specific to Correia et al. 2024. (1) Table S2 (supplementary) was cited in the wiki page's Methodology from a passing text mention but never actually read — it is a full text-extractable table cross-comparing 8 published maturation-medium formulations (including Fetterman et al. 2024's) component by component. Read in full: confirms Correia's own medium omits creatine, taurine, and dedicated sodium selenite (all present in Fetterman's formulation), consistent with Correia's own citation of Fetterman's "dispensability" finding; ACC2i (5 µM) is the unique differentiator of Correia's medium. (2) Figure 7F — the in vitro-to-in vivo correlation plot backing the paper's central translatability claim, now load-bearing in main.md's Conclusion — was rendered to PNG (render_pdf_pages.py, page 22) and visually inspected, per this wiki's established practice of checking figures behind consequential claims (precedent: the Weiser-Bitoun BRV/CCh correction and the Ernault species-conflation correction, both caught only by visual inspection). Outcome here was confirmatory rather than corrective: Pearson r = 0.85, R² = 0.72, p < 0.0001 across ~4 orders of magnitude for 21 compounds — a genuinely strong correlation, and standard-medium cells' "no usable correlation" is because they largely failed to respond at all (Figure 7D–E), not a weaker fit. Updated wiki/papers/correia-2024-acc2.md (Findings, Table S2 comparison) and main.md (exact correlation statistics in the maturation section). Other figures in both papers (Ca²⁺/AP traces, TEM/immunofluorescence images, SHAP beeswarm/waterfall plots) were judged lower-priority for visual verification since both papers already report the underlying statistics directly in prose; Scheurer's Supplementary Figure 2 (per-cell-line breakdown) was also left unchecked on the same reasoning — the donor-line-variability caveat it would support is already stated narratively in the main text and captured in the wiki page's Limitations.

---

## [2026-07-02] draft | main.md — Correia and Scheurer added to maturation section, conclusion, timeline, references

Extended the "Maturation status as an unresolved confound" section with a new paragraph covering Correia et al. 2024 (matured cells only produced a usable in vitro-to-in vivo PK/PD correlation — translatability gated by maturation status) and Scheurer et al. (2025) (99.5%-accuracy video-based SVM/SHAP maturity classifier, cites an FPD-contraction-duration correlation). Conclusion's fourth gap paragraph extended to note the translational stake (Correia) and that the components for an MEA-native classifier already exist separately in the literature but haven't been combined (Scheurer). Timeline (Figure 1) given 2024 and 2025 entries for Correia and Scheurer respectively. Both added to main.md References, alphabetically placed.

## [2026-07-02] ingest | Correia et al. 2024 — ACC2-inhibitor maturation medium

PDF: raw/correia-et-al-2024.pdf (+ raw/correia-et-al-supplementary.pdf). *Cells* 13:1339. Approved for ingest per the triage below. Maturation medium (galactose/FA base + T3/IGF1/Dex + ACC2 inhibitor CP-640186) improves metabolic (Seahorse), electrophysiological (patch-clamp AP/I_Na/I_Ca,L/I_K1 — no MEA), structural (TEM, Cx43, sarcomere), and molecular (RNA-seq) maturation; explicitly cites and builds on Fetterman et al. 2024. Distinctive contribution: validated in vitro-to-in vivo PK/PD correlation (21 BCKDK inhibitors) achieved only in matured cells — concrete evidence for the maturation gap's clinical-translation argument. Created wiki/papers/correia-2024-acc2.md. Updated wiki/hipsc-cm-maturation.md (translation evidence), wiki/index.md, wiki/references.md, and cross-linked wiki/papers/fetterman-2024-maturation.md.

## [2026-07-02] ingest | Scheurer et al. 2025 — video-based interpretable-AI maturity classifier

PDF: raw/scheurer-et-al-2025.pdf (+ raw/scheurer-et-al-2025_supplementary.docx, extracted via zipfile/regex since python-docx unavailable). *Comput Struct Biotechnol J* 27:3719–3728. Approved for ingest per the triage below. SVM+SHAP classifier stages iPSC-CM maturity from video-based beating features alone (99.5% accuracy; displacement, relaxation-rise time, beating duration, Max C, R time as top features); correctly resolves an intermediate (B27-medium) condition as partially mature. Not MEA-based, but cites a prior FPD–contraction-duration correlation (Hayakawa et al.) linking its approach to an MEA-observable quantity — the strongest existing precedent for what an MEA-native maturity classifier would look like. Created wiki/papers/scheurer-2025-optical-ai.md. Updated wiki/hipsc-cm-maturation.md (sharpened the gap statement from "no evidence exists" to "the ingredients exist but haven't been assembled"), wiki/index.md, wiki/references.md, and cross-linked wiki/papers/fetterman-2024-maturation.md.

## [2026-07-02] query | Batch triage of 4 new raw/ sources — 2 ingested, 2 skipped

Researcher added four new PDFs to raw/ (plus two supplementary files) without naming them; detected via `git status`. Read title/abstract/keywords and grepped full text for MEA/electrode/electrophysiology-method keywords for each before deciding whether to ingest, per the new "Batch or undirected additions" CLAUDE.md rule. None of the four use MEA/field-potential recording — all "MEA" text hits were false positives (substring match inside words like "measure"). Verdicts:

- **Correia et al. 2024** — "Enhancing Maturation and Translatability of Human Pluripotent Stem Cell-Derived Cardiomyocytes through a Novel Medium Containing Acetyl-CoA Carboxylase 2 Inhibitor." *Cells*, 13, 1339. DOI: 10.3390/cells13161339. File: raw/correia-et-al-2024.pdf (+ raw/correia-et-al-supplementary.pdf). **Ingest** — maturation-medium study (patch-clamp/Ca²⁺-transient based, not MEA) with in vitro–to–in vivo translatability data; strengthens the maturation gap section's clinical-translation argument alongside Fetterman et al. 2024.
- **Scheurer et al. 2025** — "Non-invasive maturity assessment of iPSC-CMs based on optical maturity characteristics using interpretable AI." *Computational and Structural Biotechnology Journal*, 27, 3719–3728. DOI: 10.1016/j.csbj.2025.08.024. File: raw/scheurer-et-al-2025.pdf (+ raw/scheurer-et-al-2025_supplementary.docx). **Ingest** — video-based SVM/SHAP maturity classifier (99.5% accuracy, d21 vs. d42+MM); non-MEA but directly sharpens the maturation gap statement (an adjacent-modality maturity classifier already exists; the gap is specifically MEA-derived reference values).
- **Feng et al. 2025** — "A Platform Integrating Biophysical and Biochemical Stimuli to Enhance Differentiation and Maturation of Cardiomyocyte Subtypes Derived from Human Induced Pluripotent Stem Cells." *Journal of Cardiovascular Development and Disease*, 12, 56. DOI: 10.3390/jcdd12020056. File: raw/feng-et-al-2025.pdf (present in raw/, not ingested). **Skip** — bioreactor with stimulation electrodes (not recording) and cantilever-based mechanical/video beat analysis for ventricular-subtype separation; different axis entirely, no clear tie to FP analysis or the maturation-reference-value gap. Revisit only if the review's scope expands to differentiation/subtype-separation platforms.
- **Shead et al. 2024** — "Human Induced Pluripotent Stem Cell-Derived Cardiomyocytes for Preclinical Cardiotoxicity Screening in Cardio-Oncology." *JACC: CardioOncology*, 6(5), 678–683. DOI: 10.1016/j.jaccao.2024.07.012. File: raw/shead-et-al-2024.pdf (present in raw/, not ingested). **Skip** — short primer/perspective (not primary research) comparing 2D monolayer/3D spheroid/ECT for cardio-oncology cardiotoxicity screening; contains only one passing, non-methodological mention of "multi-electrode assays." The 2D/3D comparison ground is already covered by primary sources already in the wiki (Hwang 2023, Altrocchi 2023, Maurissen 2024, Park 2025). Revisit if the review ever adds an explicit clinical-application motivating example (e.g. cardio-oncology).

## [2026-07-02] draft | CLAUDE.md — batch-ingest verification step added

Added a "Batch or undirected additions" note to the Ingest workflow: when the researcher adds sources to raw/ without naming files, detect new files via git status or by diffing raw/ against wiki/index.md, then report a relevance verdict per source and wait for go-ahead before creating any wiki pages or touching main.md — a separate verify pass ahead of the existing Ingest steps, not a one-shot ingest.

## [2026-07-02] draft | CLAUDE.md — anti-hallucination rule added

Reviewed external LLM-wiki projects (nashsu/llm_wiki, MetamusicX/llm-research-wiki, bitsofchris critique) for adoptable conventions per the researcher's request. Added an explicit "never invent citations, authors, or facts" rule to CLAUDE.md's Behavioral guidelines, citing this repo's own prior hallucinated-citation incidents (Dunham/Hwang author fabrications, unverifiable Blinova 2025 entry) as the concrete basis. Other proposed additions (epistemic markers, a raw-thinking scratchpad, a numeric page-promotion threshold) were declined by the researcher or judged low-value at this repo's current scale and not implemented.

---

## [2026-06-17] ingest | Altrocchi 2023 — Evaluation of chronic drug-induced electrophysiological and cytotoxic effects using hiPSC-CMs

PDF: raw/steemans-2023-chronic.pdf. First author in main.md listed as Steemans (third author); corrected to Altrocchi. Created wiki/papers/altrocchi-2023-chronic.md.

## [2026-06-17] ingest | Blinova 2025 — High-throughput evaluation of cardiac electrophysiology and proarrhythmic risk

No PDF available; no DOI in main.md. Citation possibly hallucinated. Created stub wiki/papers/blinova-2025-highthroughput.md with warning.

## [2026-06-17] ingest | Botti 2025 — In silico modelling of multi-electrode arrays for hiPSC-CM drug testing

PDF unavailable (Wiley 403 blocked). DOI: 10.1113/JP287276. Created stub wiki/papers/botti-2025-insilico.md.

## [2026-06-17] ingest | Dunham 2022 — Cardio PyMEA: open-source Python MEA analysis tool

PDF: raw/dunham-2022-cardiopyemea.pdf. Authors in main.md completely wrong (listed as Meyer, Bridge, Schröder — all fictitious). Actual authors: Dunham et al., UCLA. Created wiki/papers/dunham-2022-cardiopyemea.md.

## [2026-06-17] ingest | Ernault 2024 — Interpretation of field and LEAP potentials from cardiomyocyte monolayers

PDF: raw/ernault-2024-interpretation.pdf. Created wiki/papers/ernault-2024-interpretation.md.

## [2026-06-17] ingest | Guerrelli 2024 — hiPSC-CM electrophysiology: temporal changes and study parameters

PDF: raw/guerrelli-2024-hipscm.pdf. Created wiki/papers/guerrelli-2024-hipscm.md.

## [2026-06-17] ingest | Hwang 2023 — 3D spheroid geometry contributes to FP variability

PDF: raw/hwang-2023-spheroids.pdf. Authors in main.md completely wrong (listed as Tsai, Cho, Boheler — not authors of this paper). Actual first author: Minki Hwang, Korea. Created wiki/papers/hwang-2023-spheroids.md.

## [2026-06-17] ingest | Ismaili 2023 — Hamburg perspective on hiPSC-CM electrophysiology

PDF: raw/schulz-2023-hamburg.pdf. First author in main.md listed as Schulz (second author); corrected to Ismaili. Created wiki/papers/ismaili-2023-hamburg.md.

## [2026-06-17] ingest | Lee 2024 — CardioMEA comprehensive MEA analysis platform

PDF: raw/lee-2024-cardiomea.pdf (62 MB — exceeds read limit; content not extracted). Created partial stub wiki/papers/lee-2024-cardiomea.md.

## [2026-06-17] ingest | Mäki 2023 — Opinion: correct way to analyze FP signals

Zenodo HTML downloaded (not PDF). Self-citation by review author. DOI: 10.5281/zenodo.16760143. Created stub wiki/papers/maki-2023-opinion.md.

## [2026-06-22] ingest | Mäki 2023 — Opinion: correct way to analyze FP signals (re-ingest from HTML)

Source: raw/MEAopinion_Ver2.html. Full content extracted from HTML despite embedded base64 images making direct reading impossible (used grep). Stub upgraded to full wiki page with methodology table, morphology case handling (non-pacemaker, pacemaker, only-high-peak), and DatAnalyzer reference.

## [2026-06-17] ingest | Matsuda 2025 — UHD-CMOS-MEA with field potential imaging endpoints

PDF: raw/matsuda-2025-uhd.pdf. Created wiki/papers/matsuda-2025-uhd.md.

## [2026-06-17] ingest | Maurissen 2024 — Isogenic KCNH2 mutations in hiPSC-derived cardiac tissues

PDF: raw/maurissen-2024-mutation.pdf. Created wiki/papers/maurissen-2024-mutation.md.

## [2026-06-17] ingest | Park 2025 — hiPSC-CMs for cardiotoxicity: healthy vs. LQTS with CiPA drugs

PDF: raw/park-2025-cardiotoxicity.pdf. Created wiki/papers/park-2025-cardiotoxicity.md.

## [2026-06-17] ingest | Pramudito 2026 — Stacking ensemble ML for cardiac safety assessment

No PDF available. 2026 paper unverifiable at time of ingestion; no DOI in main.md. Created stub wiki/papers/pramudito-2026-ensemble.md.

## [2026-06-17] query | Citation errors in main.md — identified 4 confirmed errors and 2 unverifiable references

Created wiki/citation-issues.md documenting: Meyer→Dunham (authors hallucinated), Tsai→Hwang (authors hallucinated), Schulz→Ismaili (first-author order error), Steemans→Altrocchi (first-author order error), Blinova 2025 (unverified, possibly hallucinated), Pramudito 2026 (future date, unverifiable).

## [2026-06-22] ingest | Kabanov 2026 — A comprehensive system of algorithms for characterization of cardiomyocyte mechanical and electrical function

PDF: raw/kabanov-2026-cardioscripts.pdf (renamed from 1-s2.0-S1746809426006798-main.pdf). Biomedical Signal Processing and Control 120:110125. Open-source Python CardioScripts/Myopyth for combined AFM+MEA electromechanical analysis. Created wiki/papers/kabanov-2026-cardioscripts.md. Added to main.md "High-throughput and longitudinal assays" section (electromechanical feature expansion).

## [2026-06-22] ingest | Weiser-Bitoun 2026 — PhysioMEA: Signal processing platform for rate and rhythm analysis of multi-electrode array cardiac electrophysiological recordings

PDF: raw/weiser-bitoun-2026-physiomea.pdf (renamed from 1-s2.0-S0022282825002111-main.pdf). Journal of Molecular and Cellular Cardiology 210:137–149. Open-source MATLAB platform for cardiac organoid MEA; 1D/2D biomarker heatmaps; BRV analysis with 45 measures; FPD defined as R-to-T-peak (differs from Mäki 2023 baseline-return convention). Created wiki/papers/weiser-bitoun-2026-physiomea.md. Added to main.md "Transition from vendor-defined metrics" section (new platform) and "Morphology-aware analysis" section (FPD definitional inconsistency example).

## [2026-06-22] draft | main.md academic quality pass — 6 fixes

Blinova 2025 (unverified citation) removed from all 4 locations; replaced with Park 2025, Altrocchi 2023, Matsuda 2025. Motivation section reworded: self-citation phrasing fixed; Mäki 2023 claims qualified ("argues that", "propagating monolayer"). Fiducial section: added clarification that T-peak = APD90 and baseline-return measures a different quantity. Morphology section: "clear trend" claim supported with Ernault 2024 and Weiser-Bitoun 2026; waveform inversion noted as internally validated but not independently replicated. Updated wiki/citation-issues.md.


## [2026-06-22] ingest | Lee 2024 — CardioMEA (second download attempt)

PDF: raw/lee-2024-cardiomea-b.pdf (renamed from fphys-15-1472126.pdf). Same paper as raw/lee-2024-cardiomea.pdf (Front Physiol 15:1472126); second copy also exceeds 20 MB read limit. Wiki stub wiki/papers/lee-2024-cardiomea.md unchanged.

## [2026-06-22] query | Critical assessment of Mäki 2023 boldest claims against current literature

Created wiki/critical-assessment-maki-claims.md. Claim 1 (first positive peak = neighbor artifact) holds with qualifier. Claim 2 (FPD end = baseline return) challenged by Ernault 2024 (T-wave peak = APD90 for biphasic T-waves).

## [2026-06-23] draft | raw/maki-2023-opinion.html corrected per corrigendum

Four changes applied to the HTML source: (1) typographic error fixed — "distance between the dominant cell and the cell" → "...and the measurement electrode" (only-high-peak section); (2) "propagating hiPSC-CM monolayer" qualifier added to the main opinion statement and the numbered FP peak list; (3) note added that baseline-return captures APD₉₅–100, a distinct quantity from the T-wave peak (APD₉₀); (4) note added in Limitations that the inverted only-high-peak signal is structurally similar to Fig.5 pacemaker waveform (internal validation), but has not been independently replicated and lacks a formal inversion-vs-exclusion criterion. Updated wiki/papers/maki-2023-opinion.md (pacemaker exclusion finding reworded) and wiki/critical-assessment-maki-claims.md (Claim 4 typographic error marked resolved).

Additionally, wiki/critical-assessment-maki-claims.md Claim 3 corrected: "frequently misclassified or excluded without justification" was an LLM over-interpretation not present in the HTML source. Mäki 2023 only claims pacemaker signals require different fiducial logic.

## [2026-07-02] query | Visual figure analysis of weiser-bitoun-2026-physiomea.pdf — wiki page corrected and expanded

Rendered all 11 figure/table pages of the PhysioMEA PDF to PNG (new `render_pdf_pages.py`, PyMuPDF-based; complements the caption-text-only `analyze_figures.py`) and visually inspected each (Figs. 1–8, GUI screenshots). Corrected an error in wiki/papers/weiser-bitoun-2026-physiomea.md: the Findings section incorrectly stated carbachol (CCh) increases BRV's HF component — the paper's text and Fig. 6F both show no significant frequency-domain or Poincaré (SD1/SD2) difference between basal and CCh states; only time-domain IBI (mean, not SD) differs significantly. Added previously-missing methodological details visible only in full page context: the Brugada Syndrome validation (Fig. 8) uses externally-sourced, previously-published 2D hiPSC-CM monolayer data on a different MEA electrode geometry (200/30 µm) than the organoid platform (100/10 µm), not organoid data; total N=15 organoids from 8 differentiation batches split into non-overlapping basal (n=10) and CCh (n=5) cohorts; 2D heatmaps use moving-average interpolation for missing electrode values; conduction-velocity mapping requires a seeding guide ring constraining organoid position/size (stated limitation, §4.6). No corresponding claims existed in main.md, so no draft changes were needed.

## [2026-07-02] query | Visual figure analysis of ernault-2024-interpretation.pdf — wiki page expanded, main.md caveat flagged

Rendered and visually inspected Figs. 1–4 of the Ernault PDF. Found the core FP-shape/APD/CV correlation analysis (Figs. 1–4) uses NRVM (rat) monolayers, not hiPSC-CMs — only the separate LEAP experiments (Figs. 5–6) use human iPSC-CMs; the existing wiki page's Methodology section obscured this. Also found biphasic T-waves (required for the Tpeak/Tup↔APD correlation to hold) occurred in only a **minority** of recorded monolayers per the paper's text — a materially stronger caveat than the page's prior "requires morphology assessment" phrasing. Added: Tup↔APD50 correlation (previously only Tpeak↔APD90 was noted); cell-type-dependent direction of the LEAP/APD offset (atrial vs. ventricular); the CV-correlation's breakdown after premature stimulation and its restriction to the lower CV range in silico. Deleted now-redundant text-only caption dumps `figure_analysis/figures_summary.txt` (superseded weiser-bitoun output, pre filename-fix) and `figure_analysis/ernault-2024-interpretation_figures_summary.txt` (superseded by this visual pass); `figure_analysis/` is gitignored scratch space regenerable via `render_pdf_pages.py`.

## [2026-07-02] query | critical-assessment-maki-claims.md — Claim 2 reassessed after Ernault figure analysis

Revisited Claim 2 (FPD end = baseline return) in light of the Ernault 2024 figure analysis. Two facts weaken the "challenge to Mäki 2023" verdict: (1) Ernault's T-peak↔APD90 correlation was established in NRVM (rat), not hiPSC-CM, monolayers — Mäki's claim is hiPSC-CM-specific, making this cross-species rather than direct evidence; (2) biphasic T-waves (required for the correlation) were the *minority* morphology, not an edge case — meaning for most real recordings neither T-peak nor baseline-return is an empirically validated APD90 surrogate. Updated the claim narrative, evidence table, summary table row, and references-consulted line to reflect this; overall verdict softened from "most challenged claim, requires reframing" to "partially challenged, requires reframing — weaker than first stated." No change to Claims 1, 3, or 4 (unaffected by this evidence).

## [2026-07-02] draft | Table 2 and timeline — Ernault 2024 species/prevalence caveat propagated

Extended the earlier prose fix to two other main.md spots making the same overstatement: Table 2 row label "T-wave peak (empirically validated)" → "T-wave peak (biphasic-validated, NRVM)" with the target-quantity cell now noting NRVM (not hiPSC-CM) and biphasic as a minority morphology; timeline entry "T-wave peak validates as APD90 surrogate (Ernault et al.)" → "T-wave peak = APD90 for biphasic T-waves, in NRVM (Ernault et al.)". Left the morphology-pipeline flowchart's "APD90 surrogate — Ernault et al. 2024" node unchanged — it's a high-level schematic already qualified by the surrounding prose and table, not a standalone claim.

## [2026-07-02] draft | Literature review section — Ernault 2024 citation corrected

Applied the species/prevalence caveat flagged above to main.md's "Increasing emphasis on explicit and physiologically motivated fiducial definitions" section: "cardiomyocyte monolayers" → "neonatal rat ventricular myocyte (NRVM) monolayers", and added "a morphology the authors report in only a minority of recorded monolayers" after the biphasic-pattern clause. Single-sentence surgical edit; no other main.md content changed.

## [2026-06-28] lint | Graph improvement B+A — YAML frontmatter tags and cross-paper wikilinks added to all 15 wiki/papers/*.md files

Added YAML frontmatter `tags:` blocks to all 15 paper pages (tag vocabulary: open-platform, fiducial-definition, waveform-morphology, rate-correction, temporal-confounder, maturation, 3d-model, in-silico, high-throughput, spatial-analysis, cardiac-safety, disease-model, lqts, machine-learning, electromechanical, conduction-velocity, review-perspective, brv, 2d-culture). Expanded cross-paper `[[wikilinks]]` in all See also sections so the Obsidian/Foam graph forms thematic clusters rather than a pure star topology. Side fixes: stale `[[wiki/citation-issues.md]]` links removed from dunham, hwang, pramudito; stale citation-error blockquotes removed from altrocchi, dunham, hwang, ismaili; kabanov "Not currently in main.md" note updated.

## [2026-07-02] ingest | Fetterman 2024 — Independent compartmentalization of functional, metabolic, and transcriptional maturation of hiPSC-derived cardiomyocytes

PDF: raw/fetterman-2024.pdf (27 pages, text-extracted via PyMuPDF since pdftoppm unavailable). Cell Reports 43:114160. Sourced in response to a colleague's suggestion (relayed by the researcher) that MEA-derived reference values for hiPSC-CM maturation status would improve inter-study comparability and clinical translation — a gap not previously covered in this wiki beyond a passing mention in Ismaili et al. 2023. Web search (2026-07-02) found no 2022+ peer-reviewed paper validating MEA-only maturation reference values/index; this paper was the closest relevant find. Uses CardioExcyte96 (Nanion) impedance recordings, not MEA field-potential voltage, alongside Ca2+ imaging, patch-clamp AP/Nav, Seahorse OCR, and RNA-seq. Key finding: functional/metabolic/transcriptional maturation are induced independently by different medium components — no single index would capture "maturation" as a whole. Created wiki/papers/fetterman-2024-maturation.md and wiki/hipsc-cm-maturation.md (new concept/gap page). Updated wiki/index.md (Papers, Concepts, Research Gaps) and wiki/references.md.

## [2026-07-02] draft | main.md — maturation gap added as 4th priority (Abstract, new subsection, Conclusion, References)

Added new literature-review subsection "Maturation status as an unresolved confound for MEA-derived metrics" between "Rate correction of FPD" and "Morphology-aware analysis" (main.md), citing Ismaili 2023, Guerrelli 2024, and the newly ingested Fetterman 2024, plus the unpublished Axion Biosystems AIMS #CM01 / ISSCR 2025 standardization effort (flagged as non-peer-reviewed). Abstract and Conclusion updated from "three" to "four" methodological gaps, with the fourth being the absence of MEA-derived maturation reference values. Timeline (Figure 1) given a 2024 entry for Fetterman et al. Fetterman 2024 added to main.md References. Cross-linked wiki/papers/ismaili-2023-hamburg.md and wiki/papers/guerrelli-2024-hipscm.md to the new fetterman-2024-maturation.md and hipsc-cm-maturation.md pages.

## [2026-07-02] draft | main.md — frontmatter retitled; Introduction foreshadowing added for maturation gap

Frontmatter title/description updated per researcher's request (options proposed, "Charting the Field" chosen): title now "Charting the Field: Cardiomyocyte MEA Analysis Methods and Analysis Evolution Since 2022"; description folds in the original title's descriptive content. Introduction's closing scope sentence (main.md) updated to list "hiPSC-CM maturation status as an underexamined confound" alongside the other themes it already foreshadows (open pipelines, fiducial definitions, morphology-aware handling, 2D/3D/high-throughput), matching the new maturation subsection and 4th conclusion gap added earlier.

## [2026-07-02] draft | main.md title trimmed; README.md synced

Researcher edited main.md's frontmatter title directly: "Charting the Field: Cardiomyocyte MEA Analysis Methods and Analysis Evolution Since 2022" → "Charting the Field: Cardiomyocyte MEA Analysis Evolution Since 2022" (dropped redundant "Methods and"). Synced README.md's H1 heading to match (was still the pre-rename original title). Frontmatter `description` line unchanged. No other file references the paper title verbatim.

## [2026-07-02] lint | README.md and CLAUDE.md wording made agent-agnostic

Researcher removed the stale `citation-issues.md` line from README.md's repository-layout table (file was deleted in the 2026-06-25 lint pass) and asked to genericize remaining "Claude Code" wording. Replaced in README.md: "ask Claude Code" → "ask agent" (Four operations), "Claude Code skill definitions" → "Agent skill definitions" (layout table), "Claude edits only that section" → "agent edits only that section" (Tips). Softened two mentions in CLAUDE.md: line 3 now reads "the coding agent (e.g. Claude Code, Codex, or similar)"; `skills/` row now "Agent skill definitions (Claude Code skill format)". llm-wiki.md and skills/karpathy-guidelines/SKILL.md already used agent-agnostic language (Claude Code appears there only as one example among several) — no changes needed. The CLAUDE.md filename itself is unchanged, since that name is the actual convention this specific agent reads.

## [2026-06-25] lint | Citation issues resolved; wiki documentation cleaned up

All citation errors originally identified in main.md have been corrected in the draft: (1) Meyer et al. 2022 → Dunham et al. 2022 (authors completely fabricated); (2) Tsai et al. 2023 → Hwang et al. 2023 (authors completely fabricated); (3) Schulz et al. 2023 → Ismaili et al. 2023 (wrong author order); (4) Steemans et al. 2023 → Altrocchi et al. 2023 (wrong first author cited); (5) Blinova 2025 — unverified citation removed from main.md entirely (replaced with Park 2025, Altrocchi 2023, Matsuda 2025); (6) Pramudito 2026 — confirmed real (DOI: 10.1007/s10439-026-03978-1). wiki/citation-issues.md deleted; error annotations removed from wiki/references.md; wiki/index.md updated.


## [2026-10-15] lint | Schema moved from CLAUDE.md to AGENTS.md

The schema now lives in AGENTS.md (agent-agnostic); CLAUDE.md contains only an `@AGENTS.md` import so Claude Code still reads it. README.md and docs/search-strategy.md now point to AGENTS.md. Also: citation style kept as APA (final style follows the target journal, reformat at the end); "Galli et al. 2024" added to the hallucination examples; old prompt_history.md and research_assistant_system_prompt.md removed, search strategy kept in docs/search-strategy.md. Older log entries still say CLAUDE.md, left as historical record.

## [2026-10-15] lint | check.py findings fixed: Mäki 2023 version, Pramudito 2026 authors and content

First run of scripts/check.py. (1) Mäki 2023: references.md and main.md said v2 / 10.5281/zenodo.16760143, paper page said v3 / 10.5281/zenodo.20807245; researcher confirmed v3 is current (raw HTML is v3). references.md, main.md and docs/search-strategy.md updated to v3. (2) Pramudito 2026: Europe PMC (PMID 41586860) showed author initials were wrong in references.md and main.md ("A.", "N." → "M.A.", "Y.N."); corrected. The stub page contained guessed methodology ("likely uses…"); replaced with abstract-level content only (RF/XGBoost/shallow NN stacking, two FP-derived features, 16 unseen CiPA compounds, authors report AUC 1.000 for XGBoost meta-classifier). Full text not read (not open access). Observation: main.md reference list is in Harvard style while wiki/references.md is APA; final style to be decided with target journal.

## [2026-10-18] ingest | Pramudito 2026 — Stacking Ensemble Machine Learning for Cardiac Safety Assessment Using hiPSC-CM MEA Data (full text)

Full PDF added as raw/s10439-026-03978-1.pdf and read (text via PyMuPDF; figures via render_pdf_pages.py, pages 3 and 5 viewed). Replaced the abstract-level stub in wiki/papers/pramudito-2026-ensemble.md with a full page. Verified from the PDF: author names (Muhammad Adnan Pramudito, Yunendah Nur Fuadah, Yoo Seok Kim, Ki Moo Lim), dates, DOI, pages. Key content: two ΔFPDc predictors from the public Blinova 2018 dataset (no raw signal reanalysis), 12 train / 16 test drugs, RF/XGBoost/ANN + RF/XGB/SVM meta-classifier, XGBoost-meta AUC 1.000. Flagged on the page: pseudo-replicate resampling, possible in-sample meta-features (not stated either way), three internal inconsistencies (RF train AUC text vs Table 2, XGB AUC1 0.833 vs 0.883, Serrano 2023 vs 2024), non-like-for-like comparison with Blinova 2018. Leads noted but not ingested: Blinova 2018, Serrano 2023, Park Y.G. 2025 (J Adv Res). wiki/index.md entry updated; AGENTS.md Ingest step 1 now documents the PDF/figure workaround. main.md unchanged; suggested caution: do not quote the perfect AUC as robust evidence.

## [2026-10-18] lint | Scripts consolidated into scripts/; raw/.gitkeep removed; Pramudito file link fixed

render_pdf_pages.py and analyze_figures.py moved from the repo root to scripts/ (default output still the repo-root figure_analysis/, which is git-ignored). raw/.gitkeep deleted since raw/ now holds tracked files. The researcher renamed the Pramudito PDF to raw/pramudito-2026-ensemble.pdf and git-ignored it (not open access); scripts/check.py caught the then-broken **File:** link in wiki/papers/pramudito-2026-ensemble.md, now fixed. Note: wiki/papers/pramudito-2026-ensemble.md and raw/pramudito-2026-ensemble.pdf stay local-only for the PDF; the wiki page text is public.

## [2026-10-18] lint | analyze_figures.py removed; --text flag added to render_pdf_pages.py

analyze_figures.py only listed lines containing "figure"/"table" (47 noisy hits on Pramudito 2026, which has 3 figures and 5 tables), duplicated what full-text extraction and render_pdf_pages.py already provide, and needed an extra dependency (pypdf); removed (still in git history). scripts/render_pdf_pages.py gained `--text`, which writes the full PDF text to figure_analysis/<pdf-name>/text.txt and skips rendering unless --pages is also given. AGENTS.md Ingest step 1 and the scripts/ table row, and the .gitignore comment, updated to match.

## [2026-10-18] lint | Raw-file naming rule added to AGENTS.md; check.py warns on stem mismatch

At ingest the raw file is now renamed to share the stem of its wiki page (raw/XYZ.pdf -> raw/botti-2025-insilico.pdf; supplementary: <stem>-supplementary.<ext>), the only permitted change to raw/ (content stays immutable). scripts/check.py warns when a paper page's **File:** stem differs from the page stem. First run flags five legacy files: altrocchi (raw/steemans-2023-chronic.pdf), ismaili (raw/schulz-2023-hamburg.pdf, both named after earlier wrong first authors), correia, fetterman, scheurer. Not renamed yet; awaiting researcher go-ahead.

## [2026-10-18] lint | Five legacy raw files renamed to match their wiki pages

Renamed with git mv (content unchanged), and the **File:** lines on the five paper pages updated: steemans-2023-chronic.pdf -> altrocchi-2023-chronic.pdf; schulz-2023-hamburg.pdf -> ismaili-2023-hamburg.pdf; correia-et-al-2024.pdf -> correia-2024-acc2.pdf and correia-et-al-supplementary.pdf -> correia-2024-acc2-supplementary.pdf; fetterman-2024.pdf -> fetterman-2024-maturation.pdf; scheurer-et-al-2025.pdf -> scheurer-2025-optical-ai.pdf and scheurer-et-al-2025_supplementary.docx -> scheurer-2025-optical-ai-supplementary.docx. Older log entries still use the old file names; they are historical and left unchanged. No .gitignore entries referenced these files.

## [2026-10-18] query | Relevance triage of three new raw PDFs (no ingest yet)

Researcher added raw/blinova-2018.pdf, raw/park-2026.pdf and raw/serrano-2022.pdf. Read text and key methods (text via scripts/render_pdf_pages.py --text); no wiki pages, references or main.md touched. Verdicts: Blinova et al. 2018 (Cell Rep 24:3582-3592, open access CC BY-NC-ND) worth ingesting as 2018 context: source dataset of Pramudito 2026, states Fridericia correction "not thoroughly validated for hiPSC-CMs", multisite variability and QC criteria. Park et al. 2026 (J Adv Res 82:381-396, online July 2025, open access CC BY-NC-ND) moderately relevant: MEA FPDc (Fridericia) + ML on LQTS/BrS iPSC-CMs, same group and evaluation design as Pramudito; check overlap with the already ingested Park 2025 (KJPP) first. Serrano et al. (Cell Stem Cell 30:86-95, published 5 Jan 2023, not 2022) marginal/out of scope: optical voltage-dye action potentials with a CNN, not MEA/field potentials; relevant only as a Pramudito comparator; license not stated in the PDF. Awaiting researcher decision on which to ingest.

## [2026-10-18] query | Overlap check: Park 2025 (KJPP) vs Park 2026 (J Adv Res)

Compared texts of raw/park-2025-cardiotoxicity.pdf and raw/park-2026.pdf; supplementary methods/datasets of Park 2026 not available. Not a duplicate publication but a clear partial overlap from the same group (N.K. Park, Y.-G. Park, S.-J. Park, S.-H. Moon, S.W. Choi on both): same Axion Maestro Pro/Cytoview MEA setup and Fridericia FPDc; very probably the same KCNH2 c.453delC LQT2 line (KJPP: DPHC01i-AR / table entry DPHCi-01; J Adv Res: DPHCi01, citing the c.453delC papers); shared normal line CMC-011; four shared drugs (nifedipine, mexiletine, quinidine, ranolazine). Scope differs: KJPP = 4 lines, 8 drugs, FPD20/FPDc20, patch clamp, no ML; J Adv Res = 9 patient lines (LQTS and BrS) plus 4 normal, 28 CiPA compounds stated, ANN/RF/XGBoost (AUC 0.94). Neither paper cites the other (J Adv Res cites a different KJPP 2024;28(4) paper). Open points: whether recordings were reused is not stated; mexiletine in the c.453delC line: KJPP reports FPD20 = 1 uM while J Adv Res says mexiletine caused <20% change except in DPHCi08 (KCNQ1); J Adv Res says 28 compounds but its sections count 12+14 and 11+15 = 26. Advice: do not cite the two as independent confirmation of the disease-line result.

## [2026-10-18] query | Park 2026 supplementary read (mmc116 docx = supplementary methods/tables, mmc117 pdf = Data set S1 heatmaps)

Read raw/1-s2.0-S2090123225005491-mmc116.docx (text via zipfile/regex) and mmc117.pdf (28 pages, one per drug; page 4 mexiletine viewed). Findings: (1) the "28 drugs" are 12 ion-channel blockers + 14 non-cardiovascular drugs + amiodarone + remdesivir (unclassified risk, tested separately, Fig. 8); the earlier 26 vs 28 count worry is explained. (2) MEA protocol: Axion Maestro Pro, two independent 5-min recordings around a 30-min exposure, one concentration per well, >=3 replicates, Axion Cardiac Analysis Tool, concentrations from Blinova 2018, Fridericia FPDc. (3) ML input:  hange of FPD, FPDc, beat period and amplitude, averaged over the four concentrations ("data augmentation"); binary label high vs low/no risk. (4) Table S4: headline AUC 0.94 (95% CI 0.81-1.0) is ANN trained and tested on LQTS lines; normal/normal AUC 0.84-0.86 (CI 0.63-1.0); cross-condition (normal-trained) 0.74-0.78; LR values up to ~750000 from the epsilon term; 10,000 resampled test sets as in Pramudito 2026. (5) Mexiletine (Data set S1 p.4): DPHCi01 FPDc about +15% at 1 uM, about -13% at 10 uM, quiescent at 100 uM; DPHCi08 quiescent at 10 and 100 uM; the main-text "exception" in DPHCi08 therefore reflects quiescence coded as 100% FPDc change. No clear contradiction with Park 2025 (FPD20 at 1 uM is borderline); reuse of recordings still not stated. Underlying csv/video files not downloaded.

## [2026-10-18] ingest | Blinova 2018 — International Multisite Study of hiPSC-CMs for Drug Proarrhythmic Potential Assessment

Researcher-approved after the triage entry above. raw/blinova-2018.pdf renamed to raw/blinova-2018-multisite.pdf (naming rule; content unchanged; file is open access CC BY-NC-ND, no .gitignore entry needed). Created wiki/papers/blinova-2018-multisite.md, added the APA entry to wiki/references.md (22 authors, so first 19 + ellipsis + last), index entry added. Cross-links added to Pramudito 2026 and Guerrelli 2024; Pramudito page updated with the now-known Fridericia convention, the MEA/optical pooling, and the fact that Blinova's 0.872-0.862 are fit/CV AUCs on all 28 drugs. Text read via extraction; main-article figures not inspected. Cited in neither main.md nor yet used there; suggested home: FPDc rate-correction section (Fridericia not thoroughly validated for hiPSC-CMs), only on researcher request.

## [2026-10-18] ingest | Park 2026 — A machine learning platform for genotype-specific cardiotoxicity risk prediction using patient-derived iPSC-CMs

Researcher-approved. raw/park-2026.pdf renamed to raw/park-2026-genotype-ml.pdf, plus raw/park-2026-genotype-ml-supplementary-methods.docx (was ...-mmc116.docx) and raw/park-2026-genotype-ml-supplementary-dataset-s1.pdf (was ...-mmc117.pdf). Open access CC BY-NC-ND. Created wiki/papers/park-2026-genotype-ml.md, APA entry added (year 2026 = volume year; online 22 Jul 2025, Pramudito 2026 cites 2025; check against target style), index entry added; overlap note and See also added to Park 2025. Flagged on the page: overlap with Park 2025, quiescence coded as 100 percent FPDc change, averaging over concentrations, headline AUC 0.94 on 15 test drugs, unclear handling of intermediate-risk drugs (clarithromycin/clozapine called low risk), disopyramide called low risk in the Discussion but scored 0.991 in Fig. 7. Supplementary videos/csv not downloaded. Not cited in main.md.

## [2026-10-18] lint | check.py: main.md reference list must hold exactly the cited entries

References in wiki/references.md can now exceed those in main.md (ingested but uncited papers, here Blinova 2018 and Park 2026). scripts/check.py now requires every entry in main.md's # References list to be a verbatim copy of its wiki/references.md entry, every cited work to be listed, and warns about listed-but-uncited entries; AGENTS.md Finishing check text updated to match. Serrano et al. (raw/serrano-2022.pdf) not ingested: optical action potentials with a CNN, outside the MEA/field-potential scope; license not stated in the PDF.

## [2026-10-18] query | Figure inspection of Blinova 2018 and Park 2026 main articles

Rendered and viewed Blinova Figs 1, 2, 5, 6, 7 and all eight Park 2026 figures. Updated both wiki pages with figure notes. New findings on Park 2026: the two retained BrS lines are atrial-like (DPHCi15 100 percent, DPHKi09 87.5 percent atrial-like, no ventricular-like cells), confounding BrS-vs-normal comparisons; the binary labels (Fig. 7E: 16 high, 10 low) treat nine CiPA-intermediate drugs as high but clarithromycin and clozapine as low, so my earlier guess that intermediate drugs were folded into low/no risk was wrong and is corrected on the page; amiodarone/remdesivir 'validation' has no ground truth; FPDc heatmap colour scale 0-100 percent hides shortening; FPD20-type risk levels give verapamil and nitrendipine 3.3 in normal lines, above several high-risk drugs. Blinova: ddFPDc is an absolute change in ms, Park uses percent change, so the 'dFPDc' of the two ML papers differ in unit. Fig. 1A of Park confirms the identical c.453delC variant for DPHCi01.

## [2026-10-18] draft | Rate correction (FPDc) and high-throughput sections: Blinova 2018 and Park 2026 added

Researcher-approved. In main.md: (1) FPDc section, first paragraph: Blinova et al. 2018 added as the origin of the Fridericia convention (applied across ten sites, 'not thoroughly validated for hiPSC-CMs'). (2) FPDc section, ML sentence: Park et al. 2026 added with the observation that both ML studies took the rate correction as given and evaluated on 15-16 test drugs by resampling. (3) High-throughput section: Park et al. 2026 added after Park et al. 2025, with the overlap (same group, platform, apparently same LQTS line) and the atrial-like BrS-line confound. The # References list of main.md received the Blinova and Park 2026 entries verbatim from wiki/references.md. Not changed, but flagged to the researcher: the existing sentence crediting Pramudito et al. 2026 with 'improved sensitivity for TdP prediction over single-threshold approaches' is not what that paper reports (it compared stacking against single ML classifiers and reports AUC, likelihood ratios, accuracy).

## [2026-10-18] draft | Rate correction (FPDc) section: Pramudito claim corrected

Researcher-approved. The sentence crediting Pramudito et al. 2026 with 'improved sensitivity for TdP prediction over single-threshold approaches' replaced by what the paper reports: a stacking ensemble of random forest, gradient boosting and neural network classifiers outperformed each single constituent classifier on 16 held-out CiPA reference compounds (the paper compares against single ML classifiers, reports AUC, likelihood ratios and accuracy, and not sensitivity against threshold methods). The following sentence on resampled small test sets was kept.

## [2026-10-18] lint | Critical review of main.md for Zenodo publication readiness

Read all of main.md against the wiki. Not ready to post as a scientific text yet. Blockers found: (1) Lee 2024 (CardioMEA) and Botti 2025 are cited with substantive claims and in Table 1, but both wiki pages are stubs written from metadata (Lee PDF 62 MB unread, Botti PDF blocked), so those claims are unverified; (2) the Scope paragraph states searches of PubMed, bioRxiv and Scopus, but nothing in the repo documents them and the log shows citation chasing and a colleague suggestion; (3) Mäki (2023) is cited as 2023, but Zenodo v3 (record 20807245) shows publication date 23 June 2026, so the year, the timeline entry and the 'prior framework' framing need resolving; the author reviews own non-peer-reviewed opinion paper and own tool without a competing-interest statement; (4) Table 1 says Cardio PyMEA FPD end is NR while the text says Dunham and Lee explicitly state their FPD definition; (5) uncited claims: Axion AIMS #CM01 at ISSCR 2025, Fridericia exponent/heart-rate ranges, 'most widely used correction' (cites one single-lab study), 'peak-to-peak widely used vendor default', FPD-contraction link (only via Scheurer); (6) no limitations section, no AI-assistance disclosure, no preprint label, no affiliation/date/version, Mermaid figures will not render on Zenodo. Results discussed with the researcher; no edits made.

## [2026-10-18] ingest | Lee 2024 and Botti 2026 — stub pages replaced by full-text pages

Both pages had been written from metadata only (the Lee PDF is 62 MB and unreadable by the tools, the Botti PDF was blocked) while main.md made substantive claims about both. Full texts were obtained from Europe PMC (Lee PMC11557525, Botti PMC13628577, both CC BY) and both pages rewritten. Botti: wiki page renamed botti-2025-insilico -> botti-2026-insilico because the issue year is 2026 (J Physiol 604(19):8141-8166, online 11 May 2025), consistent with the issue-year rule used for Weiser-Bitoun and Kabanov; reference completed with volume, issue and pages; links in Hwang, Matsuda, Maurissen and the index updated; raw/botti-2026-insilico.xml saved, the researcher added the version-of-record PDF and the peer review history (renamed to botti-2026-insilico.pdf and botti-2026-insilico-peer-review-history.pdf). Findings that changed main.md: CardioMEA is an HD-MEA platform (Python; extracellular and intracellular-like signals; FPD = R spike to T-wave peak; no FPDc; FPD correlated minimally with APD in iCell recordings); Botti is a 2D bidomain MEA model with a fixed 30 percent atrial-like fraction in drug simulations, validated only qualitatively against published data, so the earlier wording (3D context, drug prediction across AL/VL mixtures) was inaccurate. Cardio PyMEA does report an FPD convention (R wave to a T-wave endpoint by a trapezoid-area algorithm; PDF text checked), so Table 1 'NR' was wrong; the Dunham page now records the method.

## [2026-10-18] draft | Review-driven edits to main.md (preprint readiness)

Researcher-approved. Changes: preprint status line; abstract and conclusion softened to 'in the studies examined'; Scope rewritten to the actual provenance (AI-assisted, reference tracing, colleague suggestions, one documented targeted search on 2 July 2026) without claiming searches that were not recorded; Table 1 and Table 2 corrected (Lee, Dunham, Kabanov; added T-wave endpoint convention); FPDc section: 'most widely used' replaced by the studies examined that use Fridericia, Blinova 2018 cited as origin, CardioMEA has no FPDc, '[CITATION NEEDED]' for the 30-90 BPM statement; maturation section wording and a flagged citation for the ISSCR AIMS #CM01 item; Botti sentence corrected; CiPA citation in the introduction now includes Blinova 2018; new sections 'Limitations of this review' and 'Declarations' (status, competing interests incl. own opinion paper and DatAnalyzer, version note for Mäki 2023, AI assistance, data and code availability); spelling 'modeling' -> 'modelling'. Four [CITATION NEEDED] flags remain open.

## [2026-10-18] lint | Botti page now points to the PDF; PDF-export notes added

wiki/papers/botti-2026-insilico.md no longer links the Europe PMC XML (raw/botti-2026-insilico.xml, a working copy now redundant since the version-of-record PDF was added; the researcher may delete it). docs/pdf-export-notes.md lists the elements of main.md that can break in a Markdown-to-PDF conversion (Mermaid diagrams, inline LaTeX, tables, Unicode, front matter, reference style, captions) and the items to settle at the Zenodo deposit. The XML is mentioned here for history only.

## [2026-10-18] draft | Declarations: funding and licence added

Researcher-approved. Declarations in main.md now state that the work is independent and unfunded and is released under CC BY 4.0. docs/pdf-export-notes.md updated accordingly. raw/botti-2026-insilico.xml was deleted by the researcher; no page links it.

## [2026-10-18] draft | Front matter: author affiliation and keywords

Researcher-approved. main.md front matter now reads author 'Antti-Juhana Mäki, Independent researcher' and carries the keyword list (multielectrode array, hiPSC-cardiomyocytes, field potential duration, rate correction, cardiac safety pharmacology, review) so the PDF export and the Zenodo form use the same terms; docs/pdf-export-notes.md updated.

## [2026-10-18] ingest | Clements 2025 — Standards for hiPSC-derived cardiomyocyte electrophysiology using the MEA assay (AIMS #CM01 poster)

Added to resolve the [CITATION NEEDED] flag on the Axion AIMS #CM01 statement. Sources: the poster PDF from the vendor (saved as raw/clements-2025-aims-poster.pdf, git-ignored, not redistributed; read in full as extracted text) and the vendor's web document 'AIMS #CM01' (last revised 2 December 2024, read only through a web-fetch summary, no local copy because the site blocked direct download). Verified from the poster: ISSCR 2025 Hong Kong, 11 June 2025, poster W1284; four well criteria (spike >= 0.5 mV on >= 50 percent of electrodes, synchronized beating on >= 50 percent, beat period 750-3000 ms, FPDc 200-700 ms with Fridericia); status 'proposed standard'. References, wiki page, index updated; scripts/check.py now accepts reference years written as '(2025, June 11)'.

## [2026-10-18] draft | The four [CITATION NEEDED] flags resolved

Researcher-approved review of the flags. (1) The sentence on 'traditional peak-to-peak definitions that prioritize robustness' was deleted because it attributed motives without a source; the next sentence already lists the explicit conventions of Cardio PyMEA, CardioMEA, PhysioMEA and DatAnalyzer. (2) Table 2, peak-to-peak row: studies cell now says 'Described as a common convention and criticised in Mäki, 2023' (the only source for that characterisation). (3) The statement on Fridericia exponent derivation for 60-100 BPM and hiPSC-CM rates of 30-90 BPM was replaced by a sourced version: spontaneous rates accepted at 20-90 BPM in Blinova 2018 and 20-80 BPM in the AIMS proposal (Clements 2025); the unsourced 60-100 BPM claim was dropped. (4) AIMS #CM01 now cited with the criteria; a sentence added to the FPDc section that the proposal builds the Fridericia correction into quality control (FPDc 200-700 ms). main.md contains no [CITATION NEEDED] flag any more.

## [2026-10-18] lint | Claims-by-source checklist created; Botti moved to 2026 in the timeline

docs/claims-by-source.md lists, for each of the 21 sources, every claim main.md attributes to it (one paragraph per source, with section tags, local file, wiki page and verification status) so the researcher can check the paper against the sources. Checked in the 2026-10-18 session: Blinova, Botti, Clements, Lee, Park 2026, Pramudito (full text) and the FPD definitions of Dunham, Kabanov and Weiser-Bitoun; all other sources are marked as written from the wiki pages and not re-checked since. Also checked: Mäki's Limitations section does say that the analysis might not extrapolate easily to 3D, so the Model complexity sentence is supported. Figure 1 timeline: Botti et al. moved from 2025 to 2026 to match the reference year.
