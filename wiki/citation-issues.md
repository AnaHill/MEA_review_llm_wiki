# Citation issues in main.md

Errors and uncertainties identified during the ingest of all 14 references. Four confirmed errors, one likely hallucination, and one unverifiable future paper.

---

## Confirmed author errors

### 1. "Meyer et al. 2022" → Dunham et al. 2022

| Field | main.md says | Actual PDF |
|---|---|---|
| First author | Meyer, T. | Dunham, Christopher S. |
| All authors | Meyer, T., Bridge, J.H.B., Schröder, J.R.B. | Dunham, Mackenzie, H. Nakano, Kim, A. Nakano, Stieg, Gimzewski |
| Title | "…An open-source Python application…" | "…A user-friendly, open-source Python application…" |
| Venue | *(not stated)* | PLOS ONE 17(5):e0266647, 2022 |
| DOI | *(not given)* | 10.1371/journal.pone.0266647 |
| Affiliation | *(implied German from fake names)* | UCLA, Los Angeles |

**Assessment:** Complete author hallucination. Three fictional names (Meyer, Bridge, Schröder) replace the real seven-author UCLA team. The paper title was recalled correctly except "An" vs. "A user-friendly, an". This is a pattern-of-plausibility hallucination — the fake names sound like German academics, which an LLM might generate for an electrophysiology paper.

**Fix:** Replace "Meyer et al. 2022" with "Dunham et al. 2022" throughout main.md. Update reference list entry.

---

### 2. "Tsai et al. 2023" → Hwang et al. 2023

| Field | main.md says | Actual PDF |
|---|---|---|
| First author | Tsai, Y.-H. | Hwang, Minki |
| All authors | Tsai, Y.-H., Cho, S.K., Boheler, K.R. | Hwang, Lee, Lim, Shim, H.-A. Lee |
| Venue | *(not stated)* | Frontiers in Physiology 14:1123190 |
| DOI | *(not given)* | 10.3389/fphys.2023.1123190 |
| Affiliation | *(implied Taiwanese from fake names)* | Korea (INHA University / Hallym University) |

**Assessment:** Complete author hallucination. "Boheler" is a real cardiac cell biologist (City University of Hong Kong), but he is not an author of this paper. The title in main.md matches the actual paper closely, suggesting the LLM found the right paper but fabricated authors.

**Fix:** Replace "Tsai et al. 2023" with "Hwang et al. 2023" throughout main.md. Update reference list entry.

---

### 3. "Schulz et al. 2023" → First author is Ismaili

| Field | main.md says | Actual PDF |
|---|---|---|
| First author | Schulz, C. | Ismaili, Djemail |
| Last listed author | Ismaili, D. | Schulz, Carl (2nd) |
| Full list | Schulz, Eschenhagen, Christ, Hansen, Mika, Koivumäki, Horváth, Ismaili | Ismaili, Schulz, Eschenhagen, Christ, Hansen, Mika, Koivumäki, Horváth |

**Assessment:** Author order is reversed in main.md — Schulz is listed first and Ismaili last, when the actual first author is Ismaili. All eight authors are correctly named; only the order is wrong. Minor but affects citation and credit.

**Fix:** Rename in-text citation to "Ismaili et al. 2023". Reorder author list in reference entry: Ismaili, D., Schulz, C., Eschenhagen, T., etc.

---

### 4. "Steemans et al. 2023" → First author is Altrocchi

| Field | main.md says | Actual PDF |
|---|---|---|
| First author (by citing name) | Steemans | Altrocchi, C. |
| Position of Steemans | *(cited as first)* | 3rd author |

**Assessment:** main.md uses "Steemans" as the cite-name, but the actual first author is Altrocchi; Steemans is third. All authors appear to be correctly listed in the reference, just the wrong one was chosen as the cite-name.

**Fix:** Rename in-text citation to "Altrocchi et al. 2023". Update reference entry first-author position accordingly.

---

## Removed citation

### 5. "Blinova et al. 2025" — removed from main.md

main.md previously cited: Blinova, K., Vicente, J., Strauss, D.G. 2025. *Journal of Pharmacological and Toxicological Methods* 122:1–10.

**Assessment:** K. Blinova is a real FDA researcher. However, no DOI was ever provided, and the citation could not be verified during ingestion. It was used four times in main.md to support claims about CiPA, high-throughput screening, and multi-parameter feature sets.

**Resolution (2026-06-22):** Removed from main.md entirely. Replacements made:
- CiPA reference → Park et al. 2025 (confirmed, uses CiPA drugs)
- Fridericia formula prevalence → Park et al. 2025
- Multi-parameter feature sets → Altrocchi et al. 2023; Matsuda et al. 2025
- First introductory sentence → citation removed (Ismaili et al. 2023 retained)

The wiki stub page, index entry, and references.md entry have all been deleted. The record of the hallucination is kept here in citation-issues.md only.

---

## Unverifiable future paper

### 6. "Pramudito et al. 2026" — confirmed real

main.md cites: Pramudito, A., Fuadah, N., Kim, Y.S., Lim, K.M. 2026. *Annals of Biomedical Engineering* 54:1334–1344.

**Assessment:** Confirmed real. DOI: 10.1007/s10439-026-03978-1; PubMed: 41586860. DOI has been added to main.md and wiki/references.md.

---

## Summary table

| Cite name in main.md | Error type | Actual first author | Severity |
|---|---|---|---|
| Meyer et al. 2022 | Completely fabricated authors | Dunham et al. 2022 | Critical |
| Tsai et al. 2023 | Completely fabricated authors | Hwang et al. 2023 | Critical |
| Schulz et al. 2023 | Wrong author order | Ismaili et al. 2023 | Moderate |
| Steemans et al. 2023 | Wrong first author cited | Altrocchi et al. 2023 | Moderate |
| Blinova et al. 2025 | Unverified — removed | Removed from main.md | Resolved |
| Pramudito et al. 2026 | ~~Unverified~~ Confirmed real; DOI added | — | Resolved |
