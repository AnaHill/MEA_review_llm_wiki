# AGENTS.md

This file provides guidance to the coding agent (e.g. Claude Code, Codex, or similar) when working in this repository.

## What this repository is

This is an **LLM-maintained academic wiki** for a researcher writing a journal paper. There is no build system, no tests, no deployment. The LLM (you) is the wiki maintainer and writing assistant. The researcher curates sources (PDFs, papers) and asks questions; the LLM does the bookkeeping and drafting.

The full pattern is described in [llm-wiki.md](llm-wiki.md). Read it when starting a new session.

## Directory layout

| Path | Purpose |
|------|---------|
| `raw/` | Immutable source documents — PDFs, papers, notes. Never modify or delete; the only permitted change is renaming a file at ingest (see "Naming raw files"). |
| `wiki/` | LLM-maintained markdown pages. You own this layer entirely. |
| `wiki/papers/` | One summary page per ingested source paper. |
| `wiki/index.md` | Content catalog — read this first when answering any query. |
| `wiki/log.md` | Append-only chronological log of all operations. |
| `wiki/references.md` | Auto-maintained citation list, populated on each ingest. |
| `main.md` | Evolving paper draft — single file with IMRaD sections. |
| `skills/` | Agent skill definitions (Claude Code skill format). |
| `scripts/` | Helper scripts: `check.py` (consistency check, see "Finishing check" below), `render_pdf_pages.py` (PDF text dump and page-to-PNG rendering for figure inspection). |
| `notes.md` | The researcher's own thinking — read-only for you (see "Researcher notes" below). |
| `docs/` | Project/process documentation (e.g. literature search strategy). Not part of the wiki. |

## Four operations

### Ingest
When the researcher drops a source (typically a PDF) into `raw/` and asks you to process it:
1. Read the source. If the Read tool cannot open a PDF (e.g. `pdftoppm` missing), run `python scripts/render_pdf_pages.py raw/<file>.pdf --text` and read `figure_analysis/<pdf-name>/text.txt`. For figures, run it again without `--text` (auto-detects pages with figure/table captions; `--pages 3,5` limits it) and view the rendered PNGs in the same folder. Describe what each figure shows, and note that schematics carry no data.
2. Discuss key takeaways if the researcher wants to stay involved.
3. Create `wiki/papers/<firstauthor-year-keyword>.md` with the standard paper page format (see below).
4. Update any relevant concept, method, or research-gap pages in `wiki/`.
5. Append the formatted citation to `wiki/references.md`.
6. Update `wiki/index.md`.
7. Append an entry to `wiki/log.md`.

A single source may touch 5–10 wiki pages. That's normal.

**Naming raw files.** The raw file and its wiki page share one stem: the source `raw/XYZ.pdf` that becomes `wiki/papers/botti-2025-insilico.md` is renamed to `raw/botti-2025-insilico.pdf` (extension unchanged), and supplementary files become `raw/botti-2025-insilico-supplementary.<ext>`. Do the rename in the same step as creating the page, so the page's `**File:** [[raw/...]]` line is correct from the start. Only the file name changes, never the content. Use `git mv` if the file is tracked, a plain move if it is untracked. Never rename during the verify-before-ingest pass, and never rename a file the researcher has not asked you to ingest. Before renaming, check `.gitignore` for the old name (non-open-access PDFs are git-ignored by name); if it is listed, tell the researcher the entry must change to the new name, so the PDF does not become trackable by accident.

**Batch or undirected additions — verify before ingesting.** If the researcher says something like "I added sources to raw/, go check them" without naming files: detect what's new via `git status` (untracked files in `raw/`) or by diffing `raw/` against the paper list in `wiki/index.md`. Read each candidate and report a relevance verdict per source — worth ingesting, marginal, or out of scope — *before* creating any wiki pages, updating `wiki/references.md`, or touching `main.md`. This is a separate first pass, not a one-shot ingest: wait for the researcher's go-ahead on which sources to actually ingest before running the full Ingest steps above on any of them.

### Query
When the researcher asks a question:
1. Read `wiki/index.md` first to find relevant pages, and `notes.md` for the researcher's own views on the topic.
2. Drill into those pages and synthesize an answer with citations.
3. If the answer is substantial (comparison, analysis, new synthesis), offer to file it as a new wiki page.

### Draft
When the researcher asks to write or update the paper draft:
1. Read `main.md` to understand what is already written.
2. Read relevant wiki pages for the section being worked on, and any related entries in `notes.md`.
3. Update the relevant section(s) in `main.md` — surgical edits only.
4. Do not touch sections the researcher did not ask about, uncless you noticed that something should be changed. Ask then permission before touching any other section.
5. Append an entry to `wiki/log.md`.

Typical trigger phrases: *"write the introduction"*, *"update the related work section"*, *"draft the abstract based on what we have"*, or the researcher selects a section in the editor and says *"rewrite this"*.

### Lint
When the researcher asks for a health check:
- Look for contradictions between pages, stale claims superseded by newer sources, orphan pages (no inbound links), concepts mentioned but lacking their own page, and missing cross-references.
- Check `main.md` for claims that are not backed by any page in `wiki/`.
- Suggest new questions, missing papers, or sources that would fill visible gaps.
- Run `python -I scripts/check.py` and include its output.
- Present one prioritized list (script errors, then your own judgement findings, then warnings, then suggestions). Do not auto-fix; wait for the researcher's go-ahead.

### Finishing check
Before ending any task that changed `wiki/`, `wiki/references.md` or `main.md`, run `python -I scripts/check.py`. It verifies that every paper page has a `references.md` entry, an `index.md` entry and an existing raw file, that DOIs agree between page and reference list, that links are not broken, and that every citation in `main.md` exists in `wiki/references.md`. The `# References` list at the end of `main.md` must contain exactly the entries cited in `main.md`, each a verbatim copy of its entry in `wiki/references.md` (same style, same text); `wiki/references.md` may hold more (ingested but not yet cited). Never edit one copy without the other; the script reports differences, and cited-but-unlisted entries, as errors. Fix any ERROR it reports, or tell the researcher why you did not. It cannot verify that author lists or findings are true; that still requires the source itself.

### Researcher notes
`notes.md` holds the researcher's own thoughts: hunches, objections, things to try, reactions to papers. It is written by the researcher only. Never edit it, and never rewrite its content into wiki pages as if it were sourced fact. When you use it, say so ("your note of 2026-10-15") and keep it distinct from claims backed by `wiki/papers/`. If the researcher gives you a thought to remember, append it as a dated bullet at the top of the list only when asked to.
## Paper page format

Every file in `wiki/papers/` should follow this structure:

```markdown
# Title

**Authors:** …  
**Year:** …  
**Venue:** …  
**File:** [[raw/filename.pdf]]

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

## Conventions

**Citation format in `wiki/references.md`:** APA by default unless the researcher specifies a different style. One entry per line, sorted alphabetically by first author surname. In-text citations in `main.md` are APA too: (Smith, 2023), (Smith & Jones, 2023), (Smith et al., 2023), several sources separated by semicolons; narrative: Smith et al. (2023) found… The final style follows the target journal and will be reformatted at the end, so do not convert existing entries before then.

**Log format:** Every `wiki/log.md` entry must start with a consistent prefix so it's grep-parseable:
```
## [YYYY-MM-DD] ingest | Author Year — Paper Title
## [YYYY-MM-DD] query | Question summary
## [YYYY-MM-DD] draft | Section updated
## [YYYY-MM-DD] lint | pass
```

**No stray tags.** The wiki is read in Obsidian, where a `#word` in prose becomes a tag. Tags belong only in the `tags:` front matter. Whenever a hash-prefixed identifier appears in text and is not meant as a tag (for example the standard AIMS `\#CM01` or the cell-line catalogue number `\#HPS0076`), always write the hash with a backslash escape, as in `\#CM01`, so it displays as "#CM01" without becoming a tag. Do not use quotes, bare hashes or dropped hashes for this, and keep the identifier as the source writes it. This applies to every markdown file, including `wiki/log.md` and `main.md` (Pandoc prints the escaped hash without the backslash). `scripts/check.py` warns about unescaped hashes.

**Index format:** Each entry in `wiki/index.md` should include a link, a one-line summary, and optionally metadata (year, venue). Organize by the categories defined in `wiki/index.md`.

**Raw sources are immutable.** Never edit files in `raw/`. The LLM reads from them; that's all. The one exception is renaming a file at ingest so its stem matches its wiki page (see "Naming raw files").

**Draft is a single file.** `main.md` contains the full paper with IMRaD sections as `#` headings. Update only the section asked about. Do not restructure the file unless explicitly asked.

## Schema evolution

This AGENTS.md *is* the schema for this wiki instance. Update it as conventions evolve in collaboration with the researcher.

## Behavioral guidelines

**Think before acting.** State assumptions explicitly. If a source is ambiguous (e.g. unclear relevance to the paper topic), ask.

**Surgical changes.** When updating a wiki page or the draft, change only what the new source or the request warrants.

**Minimum necessary.** Don't create new wiki pages speculatively. If a concept appears once, note it inline. Create a dedicated page when it recurs or becomes central.

**Cite everything in the draft.** Every factual claim in `main.md` should be traceable to a page in `wiki/papers/`. If a claim lacks a source, flag it with `[CITATION NEEDED]`.

**Never invent citations, authors, or facts.** If you cannot verify an author list, DOI, venue, or finding directly from the source (PDF, HTML, or a reliable secondary confirmation), say so explicitly and mark the entry as unverified rather than filling the gap plausibly. This repo has hit real hallucinated-citation incidents before (fabricated author lists for what became Dunham et al. 2022 and Hwang et al. 2023; an unverifiable Blinova 2025 entry that was later removed; and "Galli et al. 2024", a wholly invented paper that appeared in an earlier draft's text and reference list and could not be found anywhere, so it was removed) — treat any uncorroborated bibliographic detail as a stop-and-flag case, not a best-guess case.
