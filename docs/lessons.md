# Lessons from writing this review with an LLM wiki

What went wrong or worked during the project, and what changed because of it, gathered by theme from `wiki/log.md` and its archives. The log is the evidence and stays chronological; this file is the index of what it taught. It is written for a later project and for the template ([llm-wiki-academic-template](https://github.com/AnaHill/llm-wiki-academic-template)): read it before starting, not after.

Each lesson has three lines:

- **Evidence:** the log entries it rests on, as `log <date> <type>`, which match a `## [<date>] <type> |` header in `wiki/log.md` or its archives in `wiki/log-archive/`. `scripts/check.py` reports a reference that matches no header, so every lesson can be traced to what actually happened. A lesson that the log does not record names its other source instead.
- **Changed:** what was added to the harness because of it (a rule in `AGENTS.md`, a script, a setting, a skill), with the date.
- **Status:** `rule + check` (a rule and a mechanical check that notices when it is broken), `rule only` (written down, but depends on someone remembering it), or `open` (learned, but nothing in the repository enforces or even states it yet). The `open` and `rule only` items are the ones to carry into the next project deliberately.

Add a lesson when a task adds a rule, a check or a limit because something went wrong (see "Decisions go in the log" in `AGENTS.md`).

## 1. Sources and ingest

### Look at the figures, not only the extracted text
The first visual pass over two papers found what text extraction had hidden: the key analysis of one study used rat cells, not human ones, and the other's carbachol result had been read the wrong way round.
- **Evidence:** log 2026-07-02 query
- **Changed:** `scripts/render_pdf_pages.py` renders pages for viewing; Ingest step 1 in `AGENTS.md` (2026-10-18)
- **Status:** rule only (nothing checks that a figure behind a claim was viewed)

### Read the supplements
Supplementary files changed claims more than once: the ± values of one paper matched, for most groups, neither the standard deviation nor the standard error of its per-sample data; another's supplement showed that a QT difference was a rate effect; a third showed that an amplitude acceptance criterion depends on the recording day.
- **Evidence:** log 2026-11-15 ingest; log 2026-11-14 ingest; log 2026-11-06 ingest
- **Changed:** supplementary files get the page stem (`<stem>-supplementary.<ext>`) and a link from the paper page; `check.py` counts every `[[raw/...]]` link as referenced (2026-11-03)
- **Status:** rule only

### Take every bibliographic detail from the source itself
The first draft had fabricated author lists for two papers, two wrong first authors, and one paper that does not exist; much later, one reference still had its authors in the wrong order and one author's first name wrong.
- **Evidence:** log 2026-06-17 query; log 2026-10-15 lint; log 2026-11-09 draft
- **Changed:** "Never invent citations, authors, or facts" in `AGENTS.md` (2026-07-02); `check.py` warns when a paper page's first author differs from its reference key (2026-11-22)
- **Status:** rule + check (the check sees a page and its reference disagreeing, not both being wrong)

### Summarise from the full text, never from metadata
Two paper pages written from metadata (one PDF too large to read, one blocked) carried substantive claims into the draft; the full texts showed one platform described wrongly and the other model described as 3D when it is 2D.
- **Evidence:** log 2026-10-18 lint; log 2026-10-18 ingest
- **Changed:** both pages rewritten from the full text; status lines in `docs/claims-by-source.md` say how each source was read
- **Status:** rule only

### Record a source's own inconsistencies instead of picking one value
Sources disagree with themselves: a concentration given as 30 nM in one place and 100 nM in another, an error value given three ways, a slope as 0.737 in the text and 0.738 in a caption, a text that contradicts its own table, an AUC in the text that differs from the table.
- **Evidence:** log 2026-10-18 ingest; log 2026-11-07 query; log 2026-11-09 draft; log 2026-11-14 ingest
- **Changed:** the grinding skill looks for "the source disagreeing with itself" and reports both values (2026-11-09)
- **Status:** rule only

### Decide the year of a reference once
Whether a paper is cited by its online-first year or its issue year was decided three separate times before it was written down.
- **Evidence:** log 2026-10-18 ingest; log 2026-11-20 query
- **Changed:** reference-year rule in `AGENTS.md`, Citation format (2026-11-22)
- **Status:** rule only

## 2. Claims and their wording

### Check claims against the source, not against the wiki page
The wiki looks tidy and confident, and its errors are invisible from inside it: the first systematic pass found statements beyond their source on every one of the twelve wiki pages it checked.
- **Evidence:** log 2026-10-24 lint
- **Changed:** `docs/claims-by-source.md` lists every claim under its source with a checkbox (2026-10-18, as checkboxes 2026-10-24); the `/grinding` skill reads one source in full per claim (2026-11-09)
- **Status:** rule + check (the check is a person ticking a box against the PDF; the script only keeps the quoted sentences current)

### When you correct a claim, rewrite the whole sentence
A correction appended to the end of a sentence left its beginning saying the opposite; the automatic checks could not see it, and reading found it.
- **Evidence:** log 2026-10-27 draft
- **Changed:** Draft step 3 in `AGENTS.md` (2026-11-22; until then the rule was only in the log, although the blog draft already said the agent had it)
- **Status:** rule only

### Narrow a universal statement to what was actually checked
"None of the studies measures how much variability analysis methods cause" was contradicted by studies the review itself cites; it became "none applies two conventions to the same recordings". A tool "built for 3D preparations" rested on the word "organoid" alone. "Two of them" did not survive counting.
- **Evidence:** log 2026-11-19 draft; log 2026-11-20 draft
- **Changed:** the sentences, with the reasoning in the claims file
- **Status:** open (only reading catches it)

### Word an absence claim to the size of its search
Of four gaps, only one has a documented search behind it; the other three are scoped to "the studies examined", and the one with the search says so by naming the database.
- **Evidence:** log 2026-10-30 draft; log 2026-11-20 query; log 2026-11-21 draft
- **Changed:** `docs/maturation-mea-search.md` as the search record; the reasoning written into the log so that it survives the deletion of `ToDo.md`
- **Status:** rule only

### A method sentence must describe something that happened
The draft described a "targeted search of PubMed/MEDLINE, bioRxiv and Scopus" that had no record; it had been the agent's web search. The documented search that replaced it also found two sources the first had missed.
- **Evidence:** log 2026-10-18 lint; log 2026-10-30 ingest
- **Changed:** the search was redone and documented; search prompts ask for queries, databases and dates
- **Status:** rule only

### Keep the author's own inferences in a register, with a fixed vocabulary
Unsourced statements are kept out of the text's labels and in one register, each with a Support value. Two values crept in without a definition before the vocabulary was written down.
- **Evidence:** log 2026-10-30 draft; log 2026-11-20 query; log 2026-11-20 lint
- **Changed:** the register in `docs/claims-by-source.md`; its paragraph in `AGENTS.md` and the Support check in `check.py` (2026-11-20)
- **Status:** rule + check

## 3. Summaries

### A summary outlives the claim it summarises
A highlight kept asserting what the body had withdrawn the same day, and the title remained the strongest claim in the paper after weeks of narrowing the text. Corrections travel down to the claims list, not up to the title, highlights and abstract.
- **Evidence:** log 2026-11-20 lint; log 2026-11-21 draft
- **Changed:** `claim_quotes.py` reports a wording quoted in the register that `main.md` no longer contains, and the hook shows it (2026-11-22); the grinding skill re-reads the title, highlights and abstract after a change (2026-11-22)
- **Status:** rule + check (only for wordings the register quotes)

### Give each summary its own job
The four gaps were stated three times before the body (Highlights, Abstract, Conclusion), word for word in places. The highlights now carry findings and the abstract the gaps.
- **Evidence:** log 2026-11-21 draft
- **Changed:** the highlights rewritten; register item 0 keeps every wording they have had
- **Status:** open

## 4. Tools and silent failures

### A tool that fails by producing nothing reads as done
A new source had no pattern in `claim_quotes.py`, so its claims collected no sentences and looked legitimately empty; two new subheadings later emptied 33 claims the same way.
- **Evidence:** log 2026-11-20 lint; log 2026-11-21 draft; log 2026-11-21 lint
- **Changed:** missing source patterns are derived and reported; an unmapped heading is named in the Notes; the hook runs `claim_quotes.py --check` after every edit of `main.md` (2026-11-22)
- **Status:** rule + check

### One invisible byte can hide a whole file
A NUL byte written into the log in October made `grep` treat the log as binary and return nothing for a month; nothing complained.
- **Evidence:** log 2026-11-22 lint
- **Changed:** the byte removed; `scripts/rotate_log.py` refuses to run on a log that contains one (2026-11-22)
- **Status:** rule + check (only when the log is rotated)

### Keep generated noise out of files you review as diffs
Stored line numbers made 91 % of the changed lines in the claims file over twelve commits; a real defect passed review in such a diff.
- **Evidence:** log 2026-11-21 lint
- **Changed:** quotes stored without line numbers; the dry run prints them on demand (2026-11-21)
- **Status:** rule + check (the script writes the format)

### Keep one source of truth and generate everything else from it
Replacing the diagrams in `main.md` with images would have left 22 quoted claims with nothing to point at; the export works from a generated copy instead.
- **Evidence:** log 2026-11-20 lint
- **Changed:** `figures.py` and `export.py`; `check.py` warns when a rendered figure is older than its diagram (2026-11-20)
- **Status:** rule + check

### A log too long to read stops being context
At about 290 kB the log took several reads; an agent starting a session could not take it in.
- **Evidence:** log 2026-11-22 lint
- **Changed:** `scripts/rotate_log.py` moves the oldest entries to archives of at most 40 kB; `check.py` warns when `log.md` passes 40 kB (2026-11-22)
- **Status:** rule + check

## 5. The harness: rules, permissions, memory

### A rule in the prompt holds while it is remembered; a rule in the settings holds every time
Hard limits (never edit `notes.md`, ask before touching `raw/`) and the checks after every edit of `main.md` moved from `AGENTS.md` into `.claude/settings.json`.
- **Evidence:** log 2026-11-11 query
- **Changed:** permission rules and a PostToolUse hook (2026-11-11)
- **Status:** rule + check

### A limit that is too strict gets in the way
Denying every write to `raw/` also blocked the file renames that ingest requires, so the rule became "ask".
- **Evidence:** log 2026-11-14 ingest
- **Changed:** `Edit(raw/**)` moved from deny to ask (2026-11-14)
- **Status:** rule + check

### Pair each rule with a mechanical check
A rule alone gets forgotten and a script alone cannot judge. The write-back from `main.md` to the wiki, the tag vocabulary and the Support vocabulary each got both.
- **Evidence:** log 2026-11-14 lint; log 2026-11-20 lint
- **Changed:** `check.py` checks unlinked same-sentence sources, tags and Support values; the principle is in the README
- **Status:** rule + check

### A memory works only if its index line carries the rule
A new session loads only the one-line index of the memory files; a rule stated in the file but not in its line kept being missed.
- **Evidence:** not in the log; the blog draft, section "What else worked" (`docs/private/`)
- **Changed:** the index line now states the rule
- **Status:** rule only

### Decisions go in the log, not in a working file
Two decisions (not running a second search, dropping an external review tool) existed only as ticked boxes in `ToDo.md`, which is deleted at publication.
- **Evidence:** log 2026-11-20 query
- **Changed:** "Decisions go in the log" in `AGENTS.md` (2026-11-22)
- **Status:** rule only

## 6. Review and models

### An abstract is not a source, and neither is an AI's reading of one
An AI reviewer proposed two papers. The one read in full did not support what its abstract says ("validated by calcium imaging" was a comparison of whole organoids); the one available only as an abstract stayed out.
- **Evidence:** log 2026-11-20 ingest; log 2026-11-20 draft
- **Changed:** the decision and its reason in register item 5
- **Status:** rule only (limitation (v) of the paper: full texts wherever available)

### Brief an external reviewer, and verify what it suggests
An earlier AI list of "missing references" turned out to hold five references already in the paper and two that could not be found as given. The brief given to the later reviewers lists what the paper already admits and requires a DOI for every suggestion.
- **Evidence:** log 2026-10-24 draft; log 2026-11-20 draft
- **Changed:** `docs/ai-review-brief.md` (2026-11-20)
- **Status:** rule only

### When two reviews push the same way, watch for over-hedging
Both external reviews pushed towards weaker gap statements. Some changes were right; others would have made the text weaker than its evidence, and were declined with reasons.
- **Evidence:** log 2026-11-20 draft
- **Changed:** nothing beyond the recorded decisions
- **Status:** open

## 7. Process

### Check the sources early: the earlier an error is born, the more places it is copied to
A misread source passes into the paper page, concept pages, the index, several sections of the draft and finally the abstract. Most of the checking in this project happened late and at full size.
- **Evidence:** log 2026-10-24 lint; log 2026-11-20 lint
- **Changed:** nothing enforces the timing
- **Status:** open

### Grill a decision before acting on it
The first `/grill-paper` session settled a section's scope in three rounds, with twelve decisions written down, before any text changed.
- **Evidence:** log 2026-10-31 grill
- **Changed:** the `/grill-paper` skill
- **Status:** rule only (the skill runs only when called)
