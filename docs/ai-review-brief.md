# Brief for an AI reviewer of `main.md`

Give this file to the reviewing model together with `main.md`, and nothing else. `main.md` is self-contained: it holds the full text, both figures and the reference list.

---

## What you are reviewing

A narrative review by a single author on the analysis of multielectrode array (MEA) recordings from human induced pluripotent stem cell–derived cardiomyocytes (hiPSC-CMs), covering methodological developments from 2022 onwards. It will be posted as a preprint on Zenodo. It is not submitted to a journal, it reports no new experiments, and it was written as an unfunded personal project.

The two figures are fenced ```mermaid code blocks. Read them as diagrams, not as code to be corrected.

## What the review already says about itself

Do not spend the review restating these. They are stated in the text, and a finding that repeats one of them tells the author nothing.

- The selection of studies is **not systematic**: assembled with AI assistance and by citation tracing, with one documented literature search (on maturation reference values). It is not reproducible as a search and may over-represent some groups and journals.
- It was written by **one author**, with no independent screening, data extraction or risk-of-bias assessment.
- The evaluative framework is the **author's own earlier opinion paper** (Mäki, 2023), which is not peer reviewed; the author declares this interest.
- Some statements rest on **one or two studies**, and some on rat cells, fetal mouse cells, simulations, tissue-embedded electrodes or non-field-potential modalities.
- Figures and supplementary files were not inspected for every source.
- The Discussion and future outlook is explicitly **speculative** and labelled as the author's hypotheses.
- A few pre-2022 works are cited only as background.

Every claim attributed to a source has already been checked against that source, one source at a time, so "verify the citations" is not the useful task here.

## What would be most useful

In rough order of value:

1. **Claims that overreach their evidence.** Places where the wording is stronger than what the cited work can carry, where a condition of the source is dropped, or where a generalisation rests on a single study without saying so.
2. **Missing literature that would change a conclusion.** Not a reading list: a work that contradicts a claim, supersedes a cited source, or fills one of the four gaps the review says are open. For each, say which sentence it affects and how.
3. **Whether the four gaps hold up.** The review concludes that four methodological gaps remain: no validated hiPSC-CM-specific rate correction for field potential duration; no shared, validated waveform morphology criteria; no dedicated validation of analysis frameworks for 3D and spatially resolved recordings; and no MEA-derived reference values for maturation status. Are they genuinely distinct, genuinely open, and genuinely supported by the material presented?
4. **Whether the argument carries.** Does the Introduction set up what the Conclusion delivers? Is any section doing no work? Is anything important asserted but never returned to?
5. **Internal inconsistencies.** A statement in one section that another section contradicts, including between the text, the tables and the figures.

## What is not useful here

- Recommending that it be made a systematic review, or asking for PRISMA. The scope is declared.
- Journal formatting, reference style, word counts, section-heading conventions.
- Asking for new experiments or data; this is a literature review.
- Line edits for style, unless the wording changes the meaning of a claim.

## Rules for any reference you suggest

This project has been burned by invented citations more than once, so a suggested reference that cannot be verified is worse than none.

- Give the **DOI** for every work you propose, with the author list, year, title and venue.
- State **how you know it exists**: an indexed record you retrieved, or your training data. Say which.
- If you are not certain a work exists as you describe it, either leave it out or mark it clearly as unverified. Do not reconstruct a plausible citation.
- Prefer naming a specific finding in the work and the sentence of `main.md` it bears on, rather than a general topic.

## How to return your review

Return your **entire response inside one markdown code block**, fenced with four backticks, so that it can be pasted into a file unchanged. Use this structure:

````markdown
## Verdict

Two or three sentences: is the review sound as it stands, and what is the single most important thing to fix?

## Findings

### 1. <short title> — <major | moderate | minor>
**Where:** the section, and the sentence quoted well enough to find it.
**Problem:** what is wrong, in one or two sentences.
**Suggestion:** a concrete replacement wording, or the specific thing to check.

### 2. ...

## Suggested references (if any)

| Work (authors, year, title, venue) | DOI | How verified | Which sentence it affects | Why it matters |
|---|---|---|---|---|

## What I checked and could not fault

A short list, so the author knows what the review covered rather than only what it objected to.
````

Rank the findings most important first. A short review of real problems is more useful than a long one padded with observations.
