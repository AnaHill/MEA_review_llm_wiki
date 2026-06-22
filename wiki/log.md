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
