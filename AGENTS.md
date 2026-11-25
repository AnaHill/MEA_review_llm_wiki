# AGENTS.md

Guidance for the coding agent (Claude Code, Codex or similar) in this repository: an LLM-maintained academic wiki behind one review paper. The researcher curates sources and makes the decisions; you keep the wiki and draft the paper. The pattern is in [llm-wiki.md](llm-wiki.md); what the repository does and why is in [README.md](README.md).

## Layout

- `raw/` — source documents (PDFs, supplements).
- `wiki/` — yours: `papers/` (one page per source), concept pages, `index.md` (catalog; read it first), `log.md` (append-only log; older entries in `log-archive/`), `references.md` (APA list of every ingested source).
- `main.md` — the paper: one file, IMRaD sections as `#` headings.
- `notes.md` — the researcher's own thinking.
- `docs/` — project/process documentation, not part of the wiki; `docs/claims-by-source.md` lists the claims of `main.md` per source. Edit `docs/private/` only when asked.
- `scripts/` — check and build scripts; each describes itself in its docstring.

## Procedures

The steps of each operation are in `.claude/skills/<name>/SKILL.md`. Claude Code loads them by itself; with another agent, read the file before starting the task.

| When | Skill |
|------|-------|
| the researcher adds sources to `raw/` and asks to process or check them | `ingest` |
| writing or revising `main.md` or `docs/claims-by-source.md` | `draft` |
| the researcher asks for a health check | `lint` |
| `/grill-paper`: interview before a decision (only when called) | `grill-paper` |
| `/grinding <source>`: claim-by-claim check of `main.md` against a source; `/grinding wiki <source>`: the same for the wiki, right after ingest (only when called) | `grinding` |

To answer a question, read `wiki/index.md` and `notes.md`, drill into the relevant pages and answer with citations; offer to file a substantial comparison or synthesis as a new wiki page.

## Rules that always apply

- **Never invent citations, authors or facts.** If an author list, DOI, venue or finding cannot be verified from the source itself (or a reliable secondary confirmation), say so and mark it unverified. This repository has had fabricated author lists (for what became Dunham et al. 2022 and Hwang et al. 2023), an unverifiable Blinova 2025 entry and a wholly invented "Galli et al. 2024" in the draft: an uncorroborated bibliographic detail is a stop-and-flag case.
- **`raw/` is immutable.** Never edit a source; the only change allowed is renaming a file at ingest. Highlights and annotations the researcher adds to PDFs are expected, not an error.
- **`notes.md` is the researcher's.** Never edit it, and never turn its content into wiki pages as if it were sourced fact. When you use it, say so ("your note of 2026-10-15"). If the researcher wants a thought kept, write it in the chat, dated and ready to paste; they add it themselves.
- **No stray tags.** The wiki is read in Obsidian, where `#word` in prose becomes a tag. In every markdown file write an identifier that starts with a hash with a backslash escape (`\#CM01`, `\#HPS0076`), keeping it as the source writes it; not with quotes, a bare hash or a dropped hash.
- **Tag vocabulary.** Tags in the `tags:` front matter come from this list. Theme tags: `open-platform`, `fiducial-definition`, `rate-correction`, `waveform-morphology`, `maturation`, `3d-model`, `spatial-analysis`, `multimodal`, `machine-learning`, `signal-separation`, `cardiac-safety`, `disease-model`, `in-silico`, `high-throughput`. Page-type tags: `type/concept`, `type/method`, `type/analysis` (pages outside `wiki/papers/`), `type/review` (review or perspective papers). Two to four tags per page; add a tag here only when it fits at least three pages.
- **References.** `wiki/references.md` lists every ingested source in APA, one entry per line, sorted by first-author surname. The year is the issue year once volume and pages exist, not the online-first year, even when the publisher's citation tool or the authors' own page gives the earlier one (decided for Botti et al., 2026, Park et al., 2026 and Weiser-Bitoun et al., 2026); the paper page records both dates. The `# References` list of `main.md` holds exactly the entries cited there, each a verbatim copy of its line in `wiki/references.md`: never edit one copy without the other.
- **Decisions go in the log.** Each `wiki/log.md` entry starts `## [YYYY-MM-DD] <type> | <subject>`, with type `ingest`, `query`, `draft`, `lint` or `grill`. A decision and its reasons (what to cite or leave out, which option was declined) get an entry even when nothing else changes. When a task adds a rule, a check or a limit because something went wrong, also add a lesson to `docs/lessons.md` (evidence as `log <date> <type>`). To search the history, grep `wiki/log.md wiki/log-archive/`.
- **Finish with the checks.** Before ending a task that changed `wiki/` or `main.md`, run `python -I scripts/check.py` and fix every ERROR, or say why not. After editing `main.md` also run `check_abbreviations.py` and `claim_quotes.py --check`; Claude Code's hook does this after its own Edit and Write, but not after a change made by a shell command or by another agent.
- **Commit messages** (the researcher's preference; change or delete this line freely): propose one line, lowercase, in the present tense, completing "In this commit, I …", alone in a code block, with no body or trailer. The researcher commits.
- **Surgical and minimal.** State assumptions; ask when a source's relevance or a request is ambiguous. Change only what the request or the new source warrants. Note a concept inline where it first appears, and give it a page of its own when it recurs or becomes central.

## Schema evolution

This file is the schema of the wiki; update it with the researcher as conventions evolve. Keep here only what applies to every task, and put a procedure in a skill. When a rule is absolute and mechanical, also enforce it in `.claude/settings.json` (permission rule or hook).
