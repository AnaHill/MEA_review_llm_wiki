# Cardiomyocyte MEA Studies: Methods and Analysis Evolution since 2022

A narrative review paper by Antti-Juhana Mäki, maintained with an LLM-assisted academic wiki workflow using VS Code + [Foam](https://foambubble.github.io/foam/).

---

## Paper

The paper draft is in **[main.md](main.md)**.

## How it works

| Layer | Path | Who owns it |
|-------|------|-------------|
| Source papers | `raw/` | PDFs. Immutable. |
| Wiki pages | `wiki/` | LLM — paper summaries, concepts, gaps |
| Paper draft | `main.md` | LLM writes, author directs |

**Four operations (ask Claude Code):**
- **Ingest** — drop a PDF into `raw/`, LLM reads it, creates a summary page, updates the wiki, appends citation
- **Query** — ask anything; LLM reads the wiki and synthesizes an answer with citations
- **Draft** — ask to write or rewrite any section of `main.md`
- **Lint** — health check: stale claims, orphans, unsupported draft assertions

See [CLAUDE.md](CLAUDE.md) for the full schema and [llm-wiki.md](llm-wiki.md) for the pattern.

---

## Repository layout

```
raw/               source PDFs (immutable)
wiki/
  papers/          one page per ingested paper (firstauthor-year-keyword.md)
  index.md         content catalog — LLM reads this first on every query
  log.md           append-only operation log
  references.md    auto-maintained citation list (APA)
  citation-issues.md  known errors in the draft's reference list
main.md            paper draft — IMRaD sections, single file
skills/            Claude Code skill definitions
CLAUDE.md          wiki schema and LLM instructions
llm-wiki.md        the wiki pattern explained
```

---

## Tips

- **Select a section** in `main.md` and say *"rewrite this"* — Claude edits only that section.
- **`[CITATION NEEDED]`** markers mean no supporting source was found — add the paper and re-ingest.
- **Graph view** in Foam shows how paper pages link across the wiki — useful for spotting coverage gaps.
- **`wiki/references.md`** is copy-paste ready for submission; tell Claude your citation style if not APA.

---

*Based on [Andrej Karpathy's LLM wiki idea](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) — see [AnaHill/LLM-wiki-academic-template](https://github.com/AnaHill/LLM-wiki-academic-template) for a reusable blank template.*
