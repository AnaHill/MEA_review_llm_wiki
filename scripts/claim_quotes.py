"""Attach the sentences of main.md that cite a source under that source's claims in docs/claims-by-source.md.

For every numbered claim line such as `- [ ] (2) [High-throughput] ...` the sentences of main.md that cite the same
source in the section named in brackets are listed below the claim as `    - > sentence` sub-bullets.

The stored lines carry no main.md line number, deliberately. They used to, and the number changed in every quote of
the file whenever a paragraph was split or a heading added: over twelve commits, 1152 of 1261 changed lines were
line numbers alone, which buried the quotes that had really changed. Without them a quote line changes only when
its sentence does, so `git diff docs/claims-by-source.md` shows exactly which claims moved. The numbers are still
printed by a dry run, which is where they are useful — while you are working, not in the history.
Only those generated sub-bullets are rewritten; checkbox state, claim text and everything else in the file are kept.

Usage (run from the repository root):
    python -I scripts/claim_quotes.py                       dry run: prints the result with main.md line numbers,
                                                            writes nothing — use it to locate a sentence
    python -I scripts/claim_quotes.py --only Altrocchi      dry run for the sources whose section title starts so
    python -I scripts/claim_quotes.py --write               update the file for all sources and refresh the ✅ marks
    python -I scripts/claim_quotes.py --write --only Hwang  update the quotes of the sources named; ✅ marks are
                                                            still refreshed for every section (use it to mark a
                                                            source as done once all its boxes are ticked)
    python -I scripts/claim_quotes.py --write --skip Altrocchi
                                                            update the file for all sources except those named
Options may be repeated. A sentence is assigned to a claim by the section tag, so two claims with the same tag show
the same sentences unless the claim narrows them itself: a claim line may end with `{q: <regex>}`, and then the
sentences of that section matching that regex are listed under it instead. Use it where one section holds several
claims about the same source, for example `{q: two ΔFPDc-derived}`; without it the generated quotes are a pointer to
the text, not a judgement of which claim they support. The regex replaces the citation test, so it also reaches a
sentence that continues a citation without naming the source ("Both evaluated their models on small test sets ..."),
which is otherwise not found at all. A regex that matches nothing is reported, and so is a sentence citing the source
that no claim lists once any claim of that section is narrowed.
With --write, a `## ` section whose top-level checkboxes are all ticked gets a "✅ " in front of its title, and loses
it again when a box is unticked.
A `## ` section missing from the SOURCES table is given a pattern derived from the surname in its title, and the run
says so under Notes, so that a newly ingested source works without editing this file. Where the surname is shared by
two sections the script will not guess: it collects nothing for them and asks for an explicit entry with the year.
A heading of main.md missing from SECTION_TAG is reported the same way: its sentences are tagged with the heading's
own text, so every claim tagged otherwise finds nothing, and renaming a section or promoting a bold label to a `##`
heading empties that section's claims at once. Both failures produce no quotes rather than an error, so read the
Notes after every run, and run without --write first after a structural edit to main.md.
"""
import argparse
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

MAIN = "main.md"
CLAIMS = "docs/claims-by-source.md"

# Every heading of main.md belongs here. An unmapped heading becomes a tag of its own and quietly
# takes the sentences under it away from the tag the claims use, so the table is kept complete and
# main_sentences() reports anything missing from it.
SECTION_TAG = [
    ("Abstract", "Abstract"), ("Highlights", "Highlights"), ("Abbreviations", "Abbreviations"),
    ("Acknowledgements", "Acknowledgements"), ("About the author", "About the author"),
    ("Introduction", "Intro"), ("Motivation", "Motivation"),
    ("Scope and Literature Search", "Scope"), ("Literature review", "Timeline"),
    ("Open analysis pipelines", "Open pipelines"), ("Explicit and physiologically", "Fiducial"),
    ("Rate correction", "FPDc"), ("Maturation status", "Maturation"),
    ("Morphology-aware", "Morphology"), ("Three-dimensional cardiomyocyte", "3D"),
    ("High-throughput", "High-throughput"), ("Limitations of this review", "Limitations"),
    ("Conclusion", "Conclusion"), ("Discussion", "Outlook"), ("Personal note", "Personal"),
    # The two subsections of the Discussion keep its tag; without these, every [Outlook] claim
    # silently loses its sentences, because an unmapped heading becomes a section tag of its own.
    ("Multimodal recordings", "Outlook"), ("Separating the recording system", "Outlook"),
    ("Declarations", "Declarations"),
]
# Tables sit under these headings; the claims file tags their rows separately.
TABLE_TAG = {"Open pipelines": "Table 1", "Fiducial": "Table 2"}

REGISTER = "Register of the author's own inferences"  # the one `## ` section that is not a source

# claims-file section title prefix -> regex that recognises a citation of that source in main.md.
# A section missing from here does not fail: its pattern is derived from the surname in its title
# (see resolve_sources), and a note says so. Add an entry when the surname alone is not enough.
SOURCES = {
    "Altrocchi": r"\bAltrocchi\b", "Blinova": r"\bBlinova\b", "Botti": r"\bBotti\b",
    "Clements": r"\bClements\b", "Correia": r"\bCorreia\b", "Dunham": r"\bDunham\b",
    "Ernault": r"\bErnault\b", "Fetterman": r"\bFetterman\b", "Guerrelli": r"\bGuerrelli\b",
    "Hayakawa": r"\bHayakawa\b", "Hu": r"\bHu et al\b", "Hwang": r"\bHwang\b", "Ismaili": r"\bIsmaili\b",
    "Kabanov": r"\bKabanov\b", "Kim": r"\bKim et al\b", "Lee et al. (2024)": r"\bLee et al\.?,? \(?2024|CardioMEA platform.*\(Lee et al\.\)",
    "Lee et al. (2026)": r"\bLee et al\.?,? \(?2026|Transparent MEA.*\(Lee et al\.\)", "Karami": r"\bKarami\b", "Li et al. (2024)": r"\bLi et al\.?,? \(?2024", "Li et al. (2025)": r"\bLi et al\.?,? \(?2025|\(Li et al\.\)",
    "Lin": r"\bLin et al\b", "Mäki": r"(?<!Antti-Juhana )\bMäki\b",
    "Matsuda": r"\bMatsuda\b", "Maurissen": r"\bMaurissen\b",
    "Park et al. (2025)": r"Park et al\.?,? \(?2025|\(Park et al\.\)",
    "Park et al. (2026)": r"Park et al\.?,? \(?2026",
    "Pramudito": r"\bPramudito\b", "Ryynänen": r"\bRyynänen\b", "Scheurer": r"\bScheurer\b",
    "Vuorenpää": r"\bVuorenpää\b", "Weiser-Bitoun": r"\bWeiser-Bitoun\b",
}

ABBREVIATIONS = {"al", "e.g", "i.e", "vs", "fig", "figs", "approx", "cf", "ca", "no", "dr", "eg", "ie"}

CLAIM = re.compile(r"^- \[[ x]\] \((\d+[a-z]?)\) \[([^\]]+)\]")
NARROW = re.compile(r"\{q:\s*(.+?)\}\s*$")
GENERATED = re.compile(r"^ {4}- > ")
CHECKBOX = re.compile(r"^- \[([ x])\] ")
DONE = "✅ "


def split_sentences(text):
    """Split a paragraph into sentences; keeps 'et al.' and initials together."""
    out, start = [], 0
    for m in re.finditer(r"[.!?][)*\"”]*\s+(?=[A-Z*\[“\"(])", text):
        end = m.start() + len(m.group(0).rstrip())
        token = re.search(r"(\S+)$", text[:m.start() + 1]).group(1).rstrip(".!?").lstrip("(*")
        if token.lower() in ABBREVIATIONS or re.fullmatch(r"[A-Z]", token):
            continue
        out.append(text[start:end])
        start = m.end()
    out.append(text[start:])
    return [s.strip() for s in out if s.strip()]


def main_sentences():
    """Return ([(tag, line number, sentence)], notes) for the body of main.md, up to the reference list.

    The notes name any heading missing from SECTION_TAG. Such a heading is not an error in itself —
    its sentences simply get the heading's own text as their tag — but it is how a renamed or newly
    added section takes every sentence away from the tag its claims carry, which shows up only as
    claims that find nothing.
    """
    lines = open(MAIN, encoding="utf-8").read().split("\n")
    result, current, fence, notes = [], None, False, []
    first = 0
    if lines and lines[0].strip() == "---":  # YAML front matter: not part of the text
        first = next((i for i, line in enumerate(lines[1:], 1) if line.strip() == "---"), 0) + 1
    for number, raw in enumerate(lines[first:], first + 1):
        if raw.startswith("# References"):
            break
        line = re.sub(r"<!--.*?-->", "", raw).rstrip()
        if raw.strip().startswith("```"):
            fence = not fence
            continue
        heading = re.match(r"^(#{1,3}) (.+)", line)
        if heading and not fence:
            title = heading.group(2)
            current = next((tag for key, tag in SECTION_TAG if title.startswith(key)), None)
            if current is None:
                notes.append(f'main.md:{number}: the heading "{title}" is not in SECTION_TAG, so its sentences '
                             f'are tagged "{title}" and no claim tagged otherwise can reach them — add it to '
                             f'scripts/claim_quotes.py if claims should see this section under another tag')
                current = title
            continue
        if current is None or not line.strip():
            continue
        if line.lstrip().startswith("|"):
            result.append((TABLE_TAG.get(current, current), number, re.sub(r"\s{2,}", " ", line.strip())))
        elif fence:
            # Mermaid labels use a literal "\n" for line breaks; "\nDunham" would hide the name from \b
            result.append((current, number, line.strip().replace("\\n", " ")))
        else:
            for sentence in split_sentences(line.strip()):
                result.append((current, number, sentence))
    return result, notes


def surname_of(title):
    """The first word of a section title: "Weiser-Bitoun et al. (2026)" -> "Weiser-Bitoun"."""
    return re.split(r"[ (]", title.removeprefix(DONE).strip())[0]


def resolve_sources(claim_lines):
    """SOURCES, plus a pattern derived from the title for any source section not listed there.

    Without this a newly ingested source matches nothing: its claims collect no sentences and simply
    look empty, with no error anywhere — the failure is silent, which is how an ingest can look done
    while every quote under it is missing. Deriving `\\bSurname\\b` keeps a fresh ingest working, and
    the note tells the next reader to add an explicit entry where the surname is not enough: a year
    to separate two first authors of the same name, or an alternation for a citation that omits the
    surname (a Figure 1 timeline label, say).
    """
    titles = [line[3:].removeprefix(DONE).strip() for line in claim_lines if line.startswith("## ")]
    patterns, notes, by_surname = dict(SOURCES), [], {}
    for title in titles:
        if title != REGISTER:
            by_surname.setdefault(surname_of(title), []).append(title)
    for title in titles:
        if title == REGISTER or any(title.startswith(name) for name in SOURCES):
            continue
        surname = surname_of(title)
        if len(by_surname[surname]) > 1:
            notes.append(f"{title}: not in SOURCES, and '{surname}' heads {len(by_surname[surname])} sections — "
                         f"add a pattern that includes the year to scripts/claim_quotes.py; no quotes were "
                         f"collected for this source")
            continue
        patterns[title] = rf"\b{re.escape(surname)}\b"
        notes.append(f"{title}: not in SOURCES; using the derived pattern {patterns[title]}. Add an entry to "
                     f"scripts/claim_quotes.py if this source is ever cited without the surname, or if a later "
                     f"source shares it")
    return patterns, notes


def source_of(title, patterns):
    title = title.removeprefix(DONE)
    for name in patterns:
        if title.startswith(name):
            return name
    return None


def quote_lines(sentences, source, tag, patterns, narrow=None):
    """The sentences of section `tag` that cite `source`, or, when `narrow` is given, those matching that regex.

    A `{q: ...}` regex replaces the citation test rather than adding to it, so a claim can also pick up a sentence
    that continues a citation without naming the source ("Both evaluated their models on small test sets ...").

    Returns [(line, number)]: the line is what the claims file stores and carries no line number, so a quote
    changes in git only when its sentence changes; the number travels alongside for the dry run to print.
    """
    pattern = re.compile(narrow if narrow else patterns[source])
    seen, lines = set(), []
    for sentence_tag, number, sentence in sentences:
        if sentence_tag != tag or not pattern.search(sentence) or (number, sentence) in seen:
            continue
        seen.add((number, sentence))
        lines.append((f"    - > {sentence}", number))
    return lines


def update(claim_lines, sentences, selected, patterns, notes):
    out, source, claimed, shown = [], None, {}, []
    notes = list(notes)
    narrowed, listed = set(), {}  # (source, tag) pairs that use {q: ...}, and the quote lines they produced
    i = 0
    while i < len(claim_lines):
        line = claim_lines[i]
        if line.startswith("## "):
            source = source_of(line[3:], patterns)
            if source and selected(source):
                shown.append(line)
        m = CLAIM.match(line)
        if m and source and selected(source):
            out.append(line)
            shown.append(line)
            i += 1
            while i < len(claim_lines) and GENERATED.match(claim_lines[i]):
                i += 1
            narrowing = NARROW.search(line)
            narrow = narrowing.group(1) if narrowing else None
            if narrow:
                try:
                    re.compile(narrow)
                except re.error as error:
                    notes.append(f"{source} claim ({m.group(1)}): {{q: {narrow}}} is not a valid regex ({error})")
                    narrow = None
            for tag in [t.strip() for t in m.group(2).split(",")]:
                claimed.setdefault(source, set()).add(tag)
                found = quote_lines(sentences, source, tag, patterns, narrow)
                if not found:
                    reason = f" matching {{q: {narrow}}}" if narrow else ""
                    notes.append(f"{source} claim ({m.group(1)}) [{tag}]: no sentence found in main.md{reason}")
                if narrow:
                    narrowed.add((source, tag))
                listed.setdefault((source, tag), set()).update(line for line, _ in found)
                out.extend(line for line, _ in found)
                shown.extend(f"{line} — main.md:{number}" for line, number in found)
            continue
        out.append(line)
        i += 1
    for source, tags in claimed.items():
        cited = {t for t, _, s in sentences if re.search(patterns[source], s)}
        for tag in sorted(cited - tags):
            notes.append(f"{source}: cited in main.md section [{tag}] but no claim carries that tag")
    # Where {q: ...} is used, every sentence of that section should still end up under some claim.
    for source, tag in sorted(narrowed):
        for line, number in quote_lines(sentences, source, tag, patterns):
            if line not in listed[(source, tag)]:
                notes.append(f"{source} [{tag}]: no claim lists main.md:{number} {line.strip()[:90]}…")
    return out, notes, shown


def mark_done(lines):
    """Put DONE in front of every `## ` title whose top-level checkboxes are all ticked; remove it otherwise."""
    out, changed = list(lines), []
    starts = [i for i, line in enumerate(lines) if line.startswith("## ")] + [len(lines)]
    for start, end in zip(starts, starts[1:]):
        boxes = [CHECKBOX.match(line).group(1) for line in lines[start + 1:end] if CHECKBOX.match(line)]
        title = lines[start][3:].removeprefix(DONE)
        heading = "## " + (DONE if boxes and all(b == "x" for b in boxes) else "") + title
        if heading != lines[start]:
            out[start] = heading
            changed.append(heading)
    return out, changed


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--write", action="store_true", help="update docs/claims-by-source.md (default: dry run)")
    parser.add_argument("--only", action="append", default=[], help="only sources whose name starts with this")
    parser.add_argument("--skip", action="append", default=[], help="leave sources whose name starts with this")
    parser.add_argument("--check", action="store_true",
                        help="print only whether the file is out of date and the Notes (used by the main.md hook)")
    args = parser.parse_args()

    def selected(source):
        if args.only and not any(source.startswith(o) for o in args.only):
            return False
        return not any(source.startswith(s) for s in args.skip)

    original = open(CLAIMS, encoding="utf-8").read().split("\n")
    patterns, source_notes = resolve_sources(original)
    sentences, heading_notes = main_sentences()
    updated, notes, shown = update(original, sentences, selected, patterns, heading_notes + source_notes)
    updated, changed = mark_done(updated)
    if args.check:
        # Short form for the PostToolUse hook: both failure modes of this script produce nothing
        # rather than an error, so the Notes are what the agent must see after an edit of main.md.
        stale = sum(1 for a, b in zip(original, updated) if a != b) + abs(len(original) - len(updated))
        if stale:
            print(f"docs/claims-by-source.md is out of date with main.md ({stale} line(s) would change); "
                  "run python -I scripts/claim_quotes.py --write")
        else:
            print("docs/claims-by-source.md is up to date with main.md")
        if notes:
            print("Notes:")
            for note in notes:
                print("-", note)
        return
    if args.write:
        open(CLAIMS, "w", encoding="utf-8", newline="\n").write("\n".join(updated))
        print(f"wrote {CLAIMS}")
        for heading in changed:
            print("heading updated:", heading)
    else:
        print("dry run: nothing written\n")
        print("\n".join(shown))
        for heading in changed:
            print("heading would change to:", heading)
    if notes:
        print("\nNotes:")
        for note in notes:
            print("-", note)


main()
