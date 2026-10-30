# docs/: project and process documentation

This folder holds documents about how the review was made and how it is to be finished. None of it is research content. The research content is in `main.md` (the paper) and in `wiki/` (notes on the sources). `AGENTS.md` defines `docs/` as "project/process documentation, not part of the wiki".

## What each file does

| File | What it is | Used when | Can be deleted when |
|---|---|---|---|
| `claims-by-source.md` | A tick-box checklist of every claim that `main.md` attributes to each source (26 sources), with a section tag, the status of the earlier check and what was found, plus the statements that rest on the author's own synthesis (items 1-21), which is the single register of the author's own inferences in `main.md`. | During the researcher's own check of every claim against the sources; it should be regenerated when the text of `main.md` is final. | After the paper is published; it supports the Declarations statement that the sources were checked. |
| `lint-fixes-2026-10-24.md` | An audit trail of the wiki health check of 2026-10-24: every change with the reason and the exact text before and after (about 100 pages of quotes). | When the researcher reviews whether those changes were good. | After that review. `git diff` and the `lint` entries of `wiki/log.md` hold the same information. |
| `maturation-mea-search.md` | The record of the documented literature search of 2026-10-30 on MEA-derived maturation reference values: queries, databases, candidates, selection reasons and the resulting changes to `main.md`. | When checking the search sentence in Scope and in the maturation section of `main.md`. | Never while `main.md` cites it (the Declarations point to it). |
| `pdf-export-notes.md` | A checklist for turning `main.md` into the Zenodo PDF: what usually breaks (Mermaid diagrams, the LaTeX formula, wide tables, Unicode, front matter, escaped hash), what to decide at deposit, and the repository link, tag and licence notes. | At the end, when the PDF is made. | After the deposit is published. |
| `search-strategy.md` | The literature search strategy kept from the original research-assistant prompt (February 2026): time filter, databases and search terms. | As background for the Scope section. It describes the intended strategy, not the search that was actually done; `main.md` says that databases, dates and counts were not recorded, so this file must not be cited as evidence that these databases were searched. | Never needed for the paper; keep as method background. |

Two further files, a simulated AI peer review of `main.md` (`peer_review_main.md`) and an unverified AI list of "missing references" (`peer_review_missing_references_main.md`), were kept here for a day and deleted on 2026-10-24 because their useful results are in `wiki/log.md` and `lint-fixes-2026-10-24.md`. They remain in the git history (last version in commit d3430e6; for example `git show d3430e6:docs/peer_review_main.md`).

## Why these are in `docs/` and not in `wiki/`

- **`wiki/` holds knowledge about the sources.** Its pages describe papers and concepts from the literature, are maintained by the LLM, must be listed in `wiki/index.md`, and are checked by `scripts/check.py` (every paper page needs a reference entry and a raw file, every citation in `main.md` must exist in the reference list).
- **`docs/` holds knowledge about the work.** These files describe how the review was done or how it is to be finished (a checklist, an audit trail, export notes, a method description, reviews of the draft). They are not about a source or a literature concept, so they have no place in the index and no matching reference entry.
- **Rule of thumb.** If a document describes a source or a concept in the literature, it belongs in `wiki/`. If it describes the process, a decision or a checklist, it belongs in `docs/`. The researcher's own thoughts go in `notes.md`, which the agent does not edit.
- `scripts/check.py` still scans the Markdown files in `docs/` for unescaped hash identifiers, so the "no stray tags" rule applies here too.
