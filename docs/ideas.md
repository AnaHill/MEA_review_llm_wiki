# Ideas for later development

Ideas that were considered and deliberately not carried out yet, kept here because `ToDo.md` is deleted at publication. Each says what it is, why it might help and why it waits. Nothing here is planned work; decide again when the paper is published or when the template is developed further ([llm-wiki-academic-template](https://github.com/AnaHill/llm-wiki-academic-template)). Ideas that were considered and rejected for good belong in `wiki/log.md` with their reasons instead.

## Skills from Matt Pocock's collection

Source: https://github.com/mattpocock/skills (MIT). One skill of this repository already comes from that collection: `/grill-paper` is adapted from his `grilling` skill. Noted 2026-11-23, not carried out because the paper is close to publication and none of these would change it.

- **`handoff`**: condenses a long conversation into a document from which a new conversation can continue. Useful in long sessions, such as the ones this project had. Waits because Claude Code's own summarising of a long conversation already covers most of the need.
- **`retro`**: after a session, suggests improvements to the agent's environment (rules, hooks, permissions). The hook and the permission rules of 2026-11-11 came out of exactly that kind of reflection, done by hand; `docs/lessons.md` records what each change answered.
- **`research`**: investigates a question from primary sources and saves a markdown report with references. Close to the Query operation and to the documented literature search (`docs/maturation-mea-search.md`), with a stricter process of its own. Worth a look before the next literature search, especially for its rules on citing sources, given this project's history of invented citations.

## Ingest and Lint as skills of their own

Done 2026-11-25 (after outside feedback that AGENTS.md was too long for a file sent with every request): Ingest, Draft and Lint are skills in `.claude/skills/`, and AGENTS.md keeps only what applies to every task. The Ingest checklist below and the first, fourth and fifth points of the guide went into the new files; what remains is open.

- **An Ingest checklist drawn from the log:** look at the figures, read the supplements, take the author order from page 1 of the PDF, apply the reference-year rule, record the source's own inconsistencies, add a `SOURCES` pattern in `claim_quotes.py` when two sources share a surname.
- **Guide:** Matt Pocock's `writing-for-agents` (https://github.com/mattpocock/skills/blob/main/skills/productivity/writing-for-agents/SKILL.md, MIT), for the two skills and for tidying the template's `AGENTS.md`, not during the final stretch of the paper. What to do with it:
  - remove repetition, so that each rule lives in one place ("raw/ is immutable" is now in three places, the `notes.md` rule in two)
  - fix the heading "Four operations" (there are now seven)
  - keep "Never" and "Do not" for hard limits, and turn the rest into positive instructions
  - give every step a checkable definition of done (the Finishing check is a good model; Ingest has none)
  - leave short pointers where parts were moved out, trigger first ("When ingesting, read …")

## A decision record at the end of `/grill-paper`

Idea from Matt Pocock's `grill-with-docs` and `domain-modeling` skills: at the end of a grilling session, write the decision, its reasons and the rejected options as short entries, for example in `docs/decisions.md`, so that decisions need not be dug out of the log. Optional; today the skill offers a `grill` entry in `wiki/log.md`, and the rule "Decisions go in the log" in `AGENTS.md` covers the same need, less conveniently.
