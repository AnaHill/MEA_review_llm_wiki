# Four Gaps Limiting Comparability in MEA Analysis of hiPSC-Cardiomyocytes

A narrative review paper by Antti-Juhana Mäki, maintained with an LLM-assisted academic wiki workflow using VS Code + [Foam](https://foambubble.github.io/foam/) or [Obsidian](https://obsidian.md/).

---

## Paper

The paper is in **[main.md](main.md)**.

## About this repository and AI assistance

This repository explores using AI agents as helpers in writing a review paper on MEA analysis of hiPSC-CMs since 2022. A second goal is to log the process (`wiki/log.md`) so that the workflow itself can be evaluated: how AI-assisted paper writing can be done efficiently, and where it goes wrong (for example, hallucinated citations caught during the work).

The author selects the sources, directs the agents and is responsible for the final text. The agents summarise sources, maintain the wiki and draft text. `scripts/check.py` checks that citations, the reference list and the wiki pages are consistent, but it cannot verify that a claim is true; that requires reading the source, and every claim in the paper is checked against its source before publication (see `docs/claims-by-source.md`). Not every intermediate commit has been reviewed in detail.

## How it works

| Layer | Path | Who owns it |
|-------|------|-------------|
| Source papers | `raw/` | PDFs. Immutable. |
| Wiki pages | `wiki/` | LLM — paper summaries, concepts, gaps |
| Paper draft | `main.md` | LLM writes, author directs and edits |
| Own thinking | `notes.md` | Author only; the agent reads it, never edits it |

**Four operations (ask agent):**
- **Ingest** — drop a PDF into `raw/`, LLM reads it, creates a summary page, updates the wiki, appends citation
- **Query** — ask anything; LLM reads the wiki and synthesizes an answer with citations
- **Draft** — ask to write or rewrite any section of `main.md`
- **Lint** — health check: stale claims, orphans, unsupported draft assertions; runs `scripts/check.py`

Before a non-trivial choice (what a section should claim, which sources to ingest or cite, which lint findings to fix), type `/grill-paper`: the agent interviews you in rounds, looks up the facts in the wiki itself and leaves the decisions to you.

To check the claims cited to one source, type `/grinding <source>` (for example `/grinding Hayakawa`): the agent reads the source in full and reports a verdict per claim in `docs/claims-by-source.md`, with the sentence from `main.md`, the supporting passage and its page, without changing anything.

See [AGENTS.md](AGENTS.md) for the full schema and [llm-wiki.md](llm-wiki.md) for the pattern.

### Agent design: a single loop with progressive disclosure

The repository follows the single-agent-loop design described in Anthropic's article [Building agents: when to fold subagents into your main agent loop](https://claude.com/resources/articles/building-agents-when-to-fold-subagents-into-your-main-agent-loop): one agent in one context window, instead of an orchestrator handing work to specialist subagents. The article's summary, "one clear system prompt, 4-5 thin data tools, and firm output guardrails would cover most of the use case", maps onto this repository as follows:

- **One clear system prompt:** [AGENTS.md](AGENTS.md), with a single owner (the author).
- **Thin data tools:** four scripts in `scripts/` (`check.py`, `claim_quotes.py`, `check_abbreviations.py`, `render_pdf_pages.py`), each doing one mechanical job and returning plain text the agent can read.
- **Progressive disclosure:** procedures that are needed only sometimes live in skills that load on demand (`/grill-paper`, `/grinding`); moving Ingest and Lint into skills is planned.
- **Guardrails in the harness, not only in the prompt:** [.claude/settings.json](.claude/settings.json) denies file edits to `raw/` and `notes.md`, and a hook runs the abbreviation and consistency checks after every edit of `main.md`.
- **Rule plus mechanical check:** a rule in AGENTS.md alone gets forgotten, and a script alone cannot judge what makes a good tag or link. So each important convention has both: for example, the Draft operation tells the agent to write connections made in `main.md` back to the wiki, and `check.py` lists sources that `main.md` cites in one sentence but the wiki does not connect, and tags outside the agreed vocabulary.
- **Checking the output:** [docs/claims-by-source.md](docs/claims-by-source.md) lists every claim in `main.md` per source and is ticked off against the sources by hand, which serves as the evaluation set.

---

## Repository layout

```
raw/               source documents (immutable; files are only renamed at ingest)
wiki/
  papers/          one page per ingested paper (firstauthor-year-keyword.md)
  index.md         content catalog — LLM reads this first on every query
  log.md           append-only operation log
  references.md    auto-maintained citation list (APA)
main.md            paper draft — IMRaD sections, single file
notes.md           the author's own notes (the agent does not edit it)
docs/              process documents (see docs/README.md): claims-by-source checklist, lint audit trail, PDF export notes, search strategy, maturation search record
scripts/           check.py (consistency check), render_pdf_pages.py (PDF text and page images), claim_quotes.py (main.md sentences under each source's claims; dry run by default, `--write` updates the file and puts ✅ on sources whose claims are all ticked), check_abbreviations.py (abbreviation list)
skills/            Agent skill definitions (reference)
.claude/skills/    skills Claude Code loads: grill-paper (/grill-paper), grinding (/grinding)
AGENTS.md          wiki schema and LLM instructions (CLAUDE.md just imports it)
llm-wiki.md        the wiki pattern explained
```

---

## Licence

Unless noted otherwise, the written content of this repository (`main.md`, `wiki/`, `docs/` and `notes.md`) is released under the [Creative Commons Attribution 4.0 International licence (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/); the full text is in [LICENSE](LICENSE). This is the same licence that the Declarations of the paper give to the text. The code in `scripts/` is released under the MIT licence ([scripts/LICENSE](scripts/LICENSE)). `skills/` and `llm-wiki.md` come from other authors and keep their own terms (the skill states MIT in its front matter); `.claude/skills/grill-paper` is adapted from Matt Pocock's `grilling` skill and keeps its MIT licence; `.claude/skills/grinding` is written for this repository and released under the MIT licence, like the scripts. The source documents in `raw/` are not covered: they keep the licences and copyrights of their publishers and authors, and the non-open-access ones are kept out of the repository (see `.gitignore`).

## Tips

- **Select a section** in `main.md` and say *"rewrite this"* — agent edits only that section.
- **`[CITATION NEEDED]`** markers mean no supporting source was found — add the paper and re-ingest.
- **Graph view** in Foam or Obsidian shows how paper pages link across the wiki — useful for spotting coverage gaps.
- **`wiki/references.md`** is copy-paste ready for submission; tell agent your citation style if not APA.
- **`python -I scripts/check.py`** is run after every change to the wiki or `main.md`; it reports broken links, missing references and unescaped hashes (a `#word` in prose becomes a tag in Obsidian, so write it as `\#word`).
- **`docs/claims-by-source.md`** lists every claim in `main.md` per source, for checking the paper against the sources.

---

*Based on [Andrej Karpathy's LLM wiki idea](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) — see [AnaHill/llm-wiki-academic-template](https://github.com/AnaHill/llm-wiki-academic-template) for a reusable blank template.*
