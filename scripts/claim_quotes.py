"""Attach the sentences of main.md that cite a source under that source's claims in docs/claims-by-source.md.

For every numbered claim line such as `- [ ] (2) [High-throughput] ...` the sentences of main.md that cite the same
source in the section named in brackets are listed below the claim as `    - > sentence — main.md:line` sub-bullets.
Only those generated sub-bullets are rewritten; checkbox state, claim text and everything else in the file are kept.

Usage (run from the repository root):
    python -I scripts/claim_quotes.py                       dry run for all sources: prints the result, writes nothing
    python -I scripts/claim_quotes.py --only Altrocchi      dry run for the sources whose section title starts so
    python -I scripts/claim_quotes.py --write --skip Altrocchi
                                                            update the file for all sources except those named
Options may be repeated. A sentence is assigned to a claim only by the section tag, so two claims with the same tag
show the same sentences; the generated quotes are a pointer to the text, not a judgement of which claim they support.
A sentence that continues a citation without naming the source ("The same study ...") is not found.
"""
import argparse
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

MAIN = "main.md"
CLAIMS = "docs/claims-by-source.md"

SECTION_TAG = [
    ("Abstract", "Abstract"), ("Introduction", "Intro"), ("Motivation", "Motivation"),
    ("Scope and Literature Search", "Scope"), ("Literature review", "Timeline"),
    ("Open analysis pipelines", "Open pipelines"), ("Increasing emphasis", "Fiducial"),
    ("Rate correction", "FPDc"), ("Maturation status", "Maturation"),
    ("Morphology-aware", "Morphology"), ("Model complexity", "Model complexity"),
    ("High-throughput", "High-throughput/longitudinal"), ("Limitations of this review", "Limitations"),
    ("Conclusion", "Conclusion"), ("Discussion", "Outlook"), ("Declarations", "Declarations"),
]
# Tables sit under these headings; the claims file tags their rows separately.
TABLE_TAG = {"Open pipelines": "Table 1", "Fiducial": "Table 2"}

# claims-file section title prefix -> regex that recognises a citation of that source in main.md
SOURCES = {
    "Altrocchi": r"\bAltrocchi\b", "Blinova": r"\bBlinova\b", "Botti": r"\bBotti\b",
    "Clements": r"\bClements\b", "Correia": r"\bCorreia\b", "Dunham": r"\bDunham\b",
    "Ernault": r"\bErnault\b", "Fetterman": r"\bFetterman\b", "Guerrelli": r"\bGuerrelli\b",
    "Hayakawa": r"\bHayakawa\b", "Hwang": r"\bHwang\b", "Ismaili": r"\bIsmaili\b",
    "Kabanov": r"\bKabanov\b", "Lee": r"\bLee et al\b", "Mäki": r"\bMäki,? \(?20",
    "Matsuda": r"\bMatsuda\b", "Maurissen": r"\bMaurissen\b",
    "Park et al. (2025)": r"Park et al\.?,? \(?2025|\(Park et al\.\)",
    "Park et al. (2026)": r"Park et al\.?,? \(?2026",
    "Pramudito": r"\bPramudito\b", "Ryynänen": r"\bRyynänen\b", "Scheurer": r"\bScheurer\b",
    "Vuorenpää": r"\bVuorenpää\b", "Weiser-Bitoun": r"\bWeiser-Bitoun\b",
}

ABBREVIATIONS = {"al", "e.g", "i.e", "vs", "fig", "figs", "approx", "cf", "ca", "no", "dr", "eg", "ie"}

CLAIM = re.compile(r"^- \[[ x]\] \((\d+[a-z]?)\) \[([^\]]+)\]")
GENERATED = re.compile(r"^ {4}- > ")


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
    """Return [(tag, line number, sentence)] for the body of main.md (everything before the reference list)."""
    lines = open(MAIN, encoding="utf-8").read().split("\n")
    result, current, fence = [], None, False
    for number, raw in enumerate(lines, 1):
        if raw.startswith("# References"):
            break
        line = re.sub(r"<!--.*?-->", "", raw).rstrip()
        if raw.strip().startswith("```"):
            fence = not fence
            continue
        heading = re.match(r"^(#{1,3}) (.+)", line)
        if heading and not fence:
            title = heading.group(2)
            current = next((tag for key, tag in SECTION_TAG if title.startswith(key)), title)
            continue
        if current is None or not line.strip():
            continue
        if line.lstrip().startswith("|"):
            result.append((TABLE_TAG.get(current, current), number, re.sub(r"\s{2,}", " ", line.strip())))
        elif fence:
            result.append((current, number, line.strip()))
        else:
            for sentence in split_sentences(line.strip()):
                result.append((current, number, sentence))
    return result


def source_of(title):
    for name in SOURCES:
        if title.startswith(name):
            return name
    return None


def quote_lines(sentences, source, tag):
    pattern = re.compile(SOURCES[source])
    seen, lines = set(), []
    for sentence_tag, number, sentence in sentences:
        if sentence_tag == tag and pattern.search(sentence) and (number, sentence) not in seen:
            seen.add((number, sentence))
            lines.append(f"    - > {sentence} — main.md:{number}")
    return lines


def update(claim_lines, sentences, selected):
    out, source, claimed, notes, shown = [], None, {}, [], []
    i = 0
    while i < len(claim_lines):
        line = claim_lines[i]
        if line.startswith("## "):
            source = source_of(line[3:])
            if source and selected(source):
                shown.append(line)
        m = CLAIM.match(line)
        if m and source and selected(source):
            out.append(line)
            shown.append(line)
            i += 1
            while i < len(claim_lines) and GENERATED.match(claim_lines[i]):
                i += 1
            for tag in [t.strip() for t in m.group(2).split(",")]:
                claimed.setdefault(source, set()).add(tag)
                found = quote_lines(sentences, source, tag)
                if not found:
                    notes.append(f"{source} claim ({m.group(1)}) [{tag}]: no sentence found in main.md")
                out.extend(found)
                shown.extend(found)
            continue
        out.append(line)
        i += 1
    for source, tags in claimed.items():
        cited = {t for t, _, s in sentences if re.search(SOURCES[source], s)}
        for tag in sorted(cited - tags):
            notes.append(f"{source}: cited in main.md section [{tag}] but no claim carries that tag")
    return out, notes, shown


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--write", action="store_true", help="update docs/claims-by-source.md (default: dry run)")
    parser.add_argument("--only", action="append", default=[], help="only sources whose name starts with this")
    parser.add_argument("--skip", action="append", default=[], help="leave sources whose name starts with this")
    args = parser.parse_args()

    def selected(source):
        if args.only and not any(source.startswith(o) for o in args.only):
            return False
        return not any(source.startswith(s) for s in args.skip)

    original = open(CLAIMS, encoding="utf-8").read().split("\n")
    updated, notes, shown = update(original, main_sentences(), selected)
    if args.write:
        open(CLAIMS, "w", encoding="utf-8", newline="\n").write("\n".join(updated))
        print(f"wrote {CLAIMS}")
    else:
        print("dry run: nothing written\n")
        print("\n".join(shown))
    if notes:
        print("\nNotes:")
        for note in notes:
            print("-", note)


main()
