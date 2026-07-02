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

Rendered and visually inspected Figs. 1–4 of the Ernault PDF. Found the core FP-shape/APD/CV correlation analysis (Figs. 1–4) uses NRVM (rat) monolayers, not hiPSC-CMs — only the separate LEAP experiments (Figs. 5–6) use human iPSC-CMs; the existing wiki page's Methodology section obscured this. Also found biphasic T-waves (required for the Tpeak/Tup↔APD correlation to hold) occurred in only a **minority** of recorded monolayers per the paper's text — a materially stronger caveat than the page's prior "requires morphology assessment" phrasing. Added: Tup↔APD50 correlation (previously only Tpeak↔APD90 was noted); cell-type-dependent direction of the LEAP/APD offset (atrial vs. ventricular); the CV-correlation's breakdown after premature stimulation and its restriction to the lower CV range in silico. Flagged (not yet applied) a caveat for main.md's citation of this paper — species and biphasic-minority nuance — pending researcher review. Deleted now-redundant text-only caption dumps `figure_analysis/figures_summary.txt` (superseded weiser-bitoun output, pre filename-fix) and `figure_analysis/ernault-2024-interpretation_figures_summary.txt` (superseded by this visual pass); `figure_analysis/` is gitignored scratch space regenerable via `render_pdf_pages.py`.

## [2026-06-28] lint | Graph improvement B+A — YAML frontmatter tags and cross-paper wikilinks added to all 15 wiki/papers/*.md files

Added YAML frontmatter `tags:` blocks to all 15 paper pages (tag vocabulary: open-platform, fiducial-definition, waveform-morphology, rate-correction, temporal-confounder, maturation, 3d-model, in-silico, high-throughput, spatial-analysis, cardiac-safety, disease-model, lqts, machine-learning, electromechanical, conduction-velocity, review-perspective, brv, 2d-culture). Expanded cross-paper `[[wikilinks]]` in all See also sections so the Obsidian/Foam graph forms thematic clusters rather than a pure star topology. Side fixes: stale `[[wiki/citation-issues.md]]` links removed from dunham, hwang, pramudito; stale citation-error blockquotes removed from altrocchi, dunham, hwang, ismaili; kabanov "Not currently in main.md" note updated.

## [2026-06-25] lint | Citation issues resolved; wiki documentation cleaned up

All citation errors originally identified in main.md have been corrected in the draft: (1) Meyer et al. 2022 → Dunham et al. 2022 (authors completely fabricated); (2) Tsai et al. 2023 → Hwang et al. 2023 (authors completely fabricated); (3) Schulz et al. 2023 → Ismaili et al. 2023 (wrong author order); (4) Steemans et al. 2023 → Altrocchi et al. 2023 (wrong first author cited); (5) Blinova 2025 — unverified citation removed from main.md entirely (replaced with Park 2025, Altrocchi 2023, Matsuda 2025); (6) Pramudito 2026 — confirmed real (DOI: 10.1007/s10439-026-03978-1). wiki/citation-issues.md deleted; error annotations removed from wiki/references.md; wiki/index.md updated.

