#!/usr/bin/env python3
"""Deterministic consistency check for the wiki. Stdlib only; read-only, fixes nothing.

Run from anywhere: python -I scripts/check.py
Exit code 1 if any ERROR is found (warnings and info do not fail the run).

It cannot verify that author lists or findings are true (that needs the source itself),
but it catches structural ways a citation can appear without a source behind it. It also
reports where main.md has made a connection the wiki lacks (sources cited in one sentence
whose pages do not link each other) and wiki tags outside the vocabulary in AGENTS.md.
"""
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI, RAW, PAPERS = ROOT / "wiki", ROOT / "raw", ROOT / "wiki" / "papers"
LOG_TYPES = {"init", "ingest", "query", "draft", "lint", "grill"}
NON_PAGES = {"index.md", "log.md", "references.md"}

findings = {"ERROR": [], "WARN": [], "INFO": []}


def report(level, where, msg):
    findings[level].append(f"{where}: {msg}")


def read(path):
    return path.read_text(encoding="utf-8")


def norm(surname):
    """'Mäki' / 'Weiser-Bitoun' / 'Van Ammel' -> 'maki' / 'weiserbitoun' / 'vanammel'."""
    s = unicodedata.normalize("NFKD", surname).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z]", "", s.lower())


def rel(path):
    return path.relative_to(ROOT).as_posix()


# --- references.md: key (surname, year) -> DOI --------------------------------------
refs = {}
for line in read(WIKI / "references.md").splitlines():
    m = re.match(r"^([^\s,]+(?: [^\s,]+)?),[^(]*\((\d{4})(?:,[^)]*)?\)", line)
    if not m or line.startswith(("#", ">", "Default", "Auto-")):
        continue
    key = (norm(m.group(1)), m.group(2))
    doi = re.search(r"https://doi\.org/(\S+)", line)
    if key in refs:
        report("ERROR", "wiki/references.md", f"duplicate entry for {key[0]} {key[1]}")
    if not doi:
        report("WARN", "wiki/references.md", f"no DOI link: {line[:60]}…")
    refs[key] = doi.group(1).rstrip(".") if doi else None

# --- paper pages ---------------------------------------------------------------------
page_keys, raw_used = {}, set()
for page in sorted(PAPERS.glob("*.md")):
    text, where = read(page), rel(page)
    m = re.match(r"([a-z\-]+?)-(\d{4})-", page.name)
    if not m:
        report("WARN", where, "filename is not <firstauthor>-<year>-<keyword>.md")
        continue
    key = (norm(m.group(1)), m.group(2))
    page_keys[key] = page
    if key not in refs:
        report("ERROR", where, "no matching entry in wiki/references.md")
    f = re.search(r"\*\*File:\*\*\s*\[\[(raw/[^\]]+)\]\]", text)
    if not f:
        report("WARN", where, "no **File:** [[raw/...]] line (source PDF not recorded)")
    elif not (ROOT / f.group(1)).exists():
        report("ERROR", where, f"**File:** points to missing {f.group(1)}")
    else:
        raw_used.add(f.group(1))
        raw_stem = Path(f.group(1)).stem
        if not raw_stem.startswith(page.stem):
            report("WARN", where, f"raw file stem '{raw_stem}' differs from page stem '{page.stem}' (rename per AGENTS.md)")
    # supplementary files linked anywhere on the page (e.g. a **Supplementary:** line) count as referenced
    raw_used.update(r for r in re.findall(r"\[\[(raw/[^\]|#]+)", text) if (ROOT / r).exists())
    d = re.search(r"\*\*DOI:\*\*\s*(\S+)", text)
    if d and refs.get(key) and d.group(1).rstrip(".") != refs[key]:
        report("ERROR", where, f"DOI {d.group(1)} differs from references.md ({refs[key]})")
for key in refs:
    if key not in page_keys:
        report("ERROR", "wiki/references.md", f"{key[0]} {key[1]} has no page in wiki/papers/")

for f in sorted(RAW.iterdir()):
    if f.is_file() and not f.name.startswith(".") and f"raw/{f.name}" not in raw_used:
        report("INFO", f"raw/{f.name}", "not referenced by any paper page (supplementary or not ingested)")

# --- index.md and orphans ------------------------------------------------------------
index_text = read(WIKI / "index.md")
indexed = set()
for target in re.findall(r"\]\(([^)#]+\.md)\)", index_text):
    path = (WIKI / target).resolve()
    indexed.add(path)
    if not path.exists():
        report("ERROR", "wiki/index.md", f"broken link {target}")
pages = [p for p in WIKI.rglob("*.md") if p.name not in NON_PAGES or p.parent != WIKI]
for p in pages:
    if p.resolve() not in indexed:
        report("ERROR", rel(p), "not listed in wiki/index.md")

# --- broken relative links inside wiki pages -----------------------------------------
for p in WIKI.rglob("*.md"):
    for target in re.findall(r"\]\(([^)#\s]+)\)", read(p)):
        if target.startswith(("http", "mailto:")):
            continue
        if not (p.parent / target).exists():
            report("ERROR", rel(p), f"broken link {target}")

# --- main.md citations must exist in references.md -----------------------------------
main = read(ROOT / "main.md")
cited = set()
for group in re.findall(r"\(([^()]*\d{4}[a-z]?[^()]*)\)", main):
    for part in group.split(";"):
        m = re.match(r"\s*([A-ZÄÖÅ][\w\-äöåÄÖÅ]+)(?:,?\s+(?:et al\.|and\s+[A-ZÄÖÅ][\w\-]+|&\s+[A-ZÄÖÅ][\w\-]+))?,?\s+((?:19|20)\d{2})[a-z]?\s*$", part)
        if m:
            cited.add((norm(m.group(1)), m.group(2)))
for m in re.finditer(r"([A-ZÄÖÅ][\w\-äöåÄÖÅ]+)(?:\s+et al\.|\s+and\s+[A-ZÄÖÅ][\w\-]+)?\s+\(((?:19|20)\d{2})[a-z]?\)", main):
    cited.add((norm(m.group(1)), m.group(2)))
for key in sorted(cited - set(refs)):
    report("ERROR", "main.md", f"cites {key[0]} {key[1]}, which is not in wiki/references.md")
for key in sorted(set(refs) - cited):
    report("INFO", "wiki/references.md", f"{key[0]} {key[1]} is not cited in main.md")
# the reference list at the end of main.md must hold exactly the cited entries, verbatim from wiki/references.md
ref_lines = [l for l in read(WIKI / "references.md").split("\n---\n", 1)[-1].splitlines() if l.strip()]
parts = re.split(r"^# References[ \t]*$", main, maxsplit=1, flags=re.M)
if len(parts) < 2:
    report("WARN", "main.md", "no '# References' heading; the reference list cannot be compared with wiki/references.md")
main_lines = [l for l in parts[-1].splitlines() if l.strip() and not l.lstrip().startswith("<!--")] if len(parts) == 2 else []
main_keys = set()
for l in main_lines:
    if l not in ref_lines:
        report("ERROR", "main.md", f"reference differs from wiki/references.md: {l[:70]}…")
    m = re.match(r"^([^\s,]+(?: [^\s,]+)?),[^(]*\((\d{4})(?:,[^)]*)?\)", l)
    if m:
        main_keys.add((norm(m.group(1)), m.group(2)))
for key in sorted(cited - main_keys):
    report("ERROR", "main.md", f"{key[0]} {key[1]} is cited in the text but missing from the # References list")
for key in sorted(main_keys - cited):
    report("WARN", "main.md", f"{key[0]} {key[1]} is in the # References list but not cited in the text")
if "[CITATION NEEDED]" in main:
    report("INFO", "main.md", f"{main.count('[CITATION NEEDED]')} open [CITATION NEEDED] flag(s)")

# --- write-back from main.md to the wiki ---------------------------------------------
# main.md compares sources and gathers themes; the wiki should carry the same connections.
# (1) Sources cited in one sentence of main.md should have linked wiki pages (INFO).
#     The "Limitations of this review" section is skipped: it lists sources as examples.
def cite_keys(text):
    keys = set()
    for group in re.findall(r"\(([^()]*\d{4}[a-z]?[^()]*)\)", text):
        for part in group.split(";"):
            m = re.match(r"\s*([A-ZÄÖÅ][\w\-äöåÄÖÅ]+)(?:,?\s+(?:et al\.|and\s+[A-ZÄÖÅ][\w\-]+|&\s+[A-ZÄÖÅ][\w\-]+))?,?\s+((?:19|20)\d{2})[a-z]?\s*$", part)
            if m:
                keys.add((norm(m.group(1)), m.group(2)))
    for m in re.finditer(r"([A-ZÄÖÅ][\w\-äöåÄÖÅ]+)(?:\s+et al\.|\s+and\s+[A-ZÄÖÅ][\w\-]+)?\s+\(((?:19|20)\d{2})[a-z]?\)", text):
        keys.add((norm(m.group(1)), m.group(2)))
    return {k for k in keys if k in page_keys}


body = re.split(r"^# References[ \t]*$", main, maxsplit=1, flags=re.M)[0]
body = re.sub(r"^# Limitations of this review.*?(?=^# )", "", body, flags=re.M | re.S)
# A pair counts as connected if one paper page links the other, or if a concept page
# (outside wiki/papers/) links both: list-like sentences ("used in A, B and C") belong on a hub page.
stem_key = {p.stem: k for k, p in page_keys.items()}
def paper_links(path):
    return {stem_key[t] for t in re.findall(r"\[\[wiki/papers/([^\]|#]+?)(?:\.md)?\]\]", read(path)) if t in stem_key}
linked = set()
for key, page in page_keys.items():
    linked.update(frozenset((key, k2)) for k2 in paper_links(page) if k2 != key)
for p in WIKI.glob("*.md"):
    if p.name not in NON_PAGES:
        hub = sorted(paper_links(p))
        linked.update(frozenset((a, b)) for i, a in enumerate(hub) for b in hub[i + 1:])
unlinked = {}
for line in body.splitlines():
    for sentence in re.split(r"(?<=[.!?])\s+(?=[A-Z*])", line):
        keys = sorted(cite_keys(sentence))
        for i, a in enumerate(keys):
            for b in keys[i + 1:]:
                if frozenset((a, b)) not in linked:
                    unlinked[(a, b)] = unlinked.get((a, b), 0) + 1
for (a, b), n in sorted(unlinked.items()):
    report("INFO", "main.md", f"{page_keys[a].stem} and {page_keys[b].stem} are cited in the same sentence "
           f"({n}x) but their wiki pages do not link each other (write back, AGENTS.md Draft)")

# (2) Tags come from the vocabulary in AGENTS.md ("Tag vocabulary"), so the graph groups by theme (WARN).
agents = ROOT / "AGENTS.md"
vocab_line = next((l for l in read(agents).splitlines() if l.startswith("**Tag vocabulary.**")), "") if agents.exists() else ""
vocab = {t for t in re.findall(r"`([a-z0-9/\-]+)`", vocab_line) if not t.endswith("/")}
if vocab:
    for p in sorted(WIKI.rglob("*.md")):
        if p.parent == WIKI and p.name in NON_PAGES:
            continue
        fm = re.match(r"---\r?\ntags:\s*\[([^\]]*)\]", read(p))
        tags = [t.strip() for t in fm.group(1).split(",") if t.strip()] if fm else []
        if not tags:
            report("WARN", rel(p), "no tags in the front matter (see Tag vocabulary in AGENTS.md)")
        for t in tags:
            if t not in vocab:
                report("WARN", rel(p), f"tag '{t}' is not in the Tag vocabulary of AGENTS.md")

# --- log.md header format ------------------------------------------------------------
for i, line in enumerate(read(WIKI / "log.md").splitlines(), 1):
    if line.startswith("## [") and "YYYY" not in line:
        m = re.match(r"## \[\d{4}-\d{2}-\d{2}\] (\w+) \| .+", line)
        if not m or m.group(1) not in LOG_TYPES:
            report("WARN", f"wiki/log.md:{i}", f"non-standard log header: {line[:60]}")

# --- accidental Obsidian tags ----------------------------------------------------------
# A '#word' in prose is read as a tag in Obsidian. Tags belong in the front matter only.
# Always escape the hash with a backslash (\#word); quotes do not count as an escape.
TAG = re.compile(r"(?<![\w\\&/#`])#(?=[A-Za-z_])[\w/-]*[A-Za-z_][\w/-]*")
for p in [ROOT / "main.md", *sorted(WIKI.rglob("*.md")), *sorted((ROOT / "docs").glob("*.md"))]:
    in_front, in_fence = False, False
    for n, line in enumerate(read(p).splitlines(), 1):
        s = line.strip()
        if n == 1 and s == "---":
            in_front = True
            continue
        if in_front:
            in_front = s != "---"
            continue
        if s.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence or s.startswith("#"):
            continue
        for m in TAG.finditer(re.sub(r"`[^`]*`|https?://\S+", "", line)):
            report("WARN", f"{rel(p)}:{n}", f"'{m.group(0)}' would be read as an Obsidian tag; escape the hash with a backslash")

# --- output --------------------------------------------------------------------------
sys.stdout.reconfigure(encoding="utf-8")
for level in ("ERROR", "WARN", "INFO"):
    for item in findings[level]:
        print(f"{level:5} {item}")
print(f"\n{len(findings['ERROR'])} error(s), {len(findings['WARN'])} warning(s), {len(findings['INFO'])} info "
      f"— {len(page_keys)} paper pages, {len(refs)} references, {len(cited)} distinct citations in main.md")
sys.exit(1 if findings["ERROR"] else 0)
