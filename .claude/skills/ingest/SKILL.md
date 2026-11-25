---
name: ingest
description: Turn a source document in raw/ into wiki pages - a paper page, concept-page updates, the reference entry, the index line and a log entry - and rename the raw file to match. Also the verify-first pass when the researcher says new files were added without naming them. Use when asked to ingest, process or add a paper or PDF, or to check what is new in raw/.
license: MIT
---

# Ingest

The rules of AGENTS.md apply throughout, above all: never invent bibliographic details, and never change the text of a file in `raw/`.

## New files without names: verify first

If the researcher says something like "I added sources to raw/, go check them" without naming files, find the new ones (`git status` for untracked files in `raw/`, or `raw/` against the paper list in `wiki/index.md`). Read each and report a verdict per source — worth ingesting, marginal, or out of scope — and stop. Create no pages, rename nothing and touch neither `wiki/references.md` nor `main.md` until the researcher names the sources to ingest.

## Steps for one source

1. **Read the source in full**, supplements included. If the Read tool cannot open a PDF (e.g. `pdftoppm` missing), run `python -I scripts/render_pdf_pages.py raw/<file>.pdf --text` and read `figure_analysis/<pdf-name>/text.txt`. For figures, run it again without `--text` (it finds pages with figure or table captions; `--pages 3,5` limits it) and view the PNGs. Describe what each figure shows; say when a schematic carries no data.
2. **Take the bibliographic details from the source itself:** the author order from page 1 of the PDF, the venue, the DOI, and both the online-first and the issue dates. Note any place where the source disagrees with itself (text versus figure caption, abstract versus results).
3. **Discuss the key takeaways** if the researcher wants to stay involved.
4. **Create the paper page** `wiki/papers/<firstauthor-year-keyword>.md` in the format below, and in the same step **rename the raw file** to the same stem (below).
5. **Update concept, method and research-gap pages** the source bears on. Link the concept pages that cite the paper from its "See also", and give a short reason after a link to another paper ("— T-wave peak versus APD90"). Two to four tags from the Tag vocabulary.
6. **Append the reference** to `wiki/references.md` (format below).
7. **Add the index line** to `wiki/index.md`, under its category: link, one-line summary, optionally year and venue.
8. **Append the log entry** `## [YYYY-MM-DD] ingest | Author Year — Paper Title`, naming the pages touched.
9. **Run `python -I scripts/check.py`** and fix its ERRORs. If the source will be cited in `main.md` and shares a surname with another source, or is cited somewhere without its surname, add an entry to `SOURCES` in `scripts/claim_quotes.py`.

A single source often touches 5–10 wiki pages. **Done when:** the page, the renamed raw file, the reference, the index line and the log entry exist, and `check.py` reports no ERROR for the source.

## Naming the raw file

The raw file and its page share one stem: `raw/XYZ.pdf` that becomes `wiki/papers/botti-2025-insilico.md` is renamed to `raw/botti-2025-insilico.pdf`, and supplements to `raw/botti-2025-insilico-supplementary.<ext>`. Only the name changes. Use `git mv` for a tracked file, a plain move otherwise. Rename only files the researcher has asked you to ingest, never during the verify-first pass. Check `.gitignore` for the old name first (non-open-access PDFs are git-ignored by name); if it is listed, tell the researcher the entry must change to the new name, so the PDF does not become trackable by accident.

## Reference format

As in the References rule of AGENTS.md (APA, issue year, both dates on the paper page). Do not convert existing entries to another style; the target journal's style is applied at the end.

## Paper page format

```markdown
---
tags: [theme-tag, theme-tag]
---

# Title

**Authors:** …  
**Year:** …  
**Venue:** …  
**File:** [[raw/filename.pdf]]  
**Supplementary:** [[raw/filename-supplementary.ext]]  (when there is one)  
**DOI:** …

## Contribution
One paragraph: what does this paper claim to contribute?

## Methodology
Key methods, datasets, experimental setup.

## Findings
Main results and conclusions.

## Limitations
What the authors acknowledge as limitations or what you observe.

## Relevance to our paper
How this source relates to, supports, challenges, or fits into the paper being written.

## See also
Links to related wiki pages.
```
