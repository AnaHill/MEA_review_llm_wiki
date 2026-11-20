#!/usr/bin/env python3
"""Keep the Mermaid diagrams of main.md and their rendered images in step. Stdlib only.

The fenced ```mermaid blocks in `main.md` are the source of truth and stay there: `claim_quotes.py`
reads them as sentences of the draft, so 18 Timeline claims and the Figure 2 claims in
`docs/claims-by-source.md` are quoted from inside those blocks. Removing them would leave those
claims with no sentence to point at. What this script does instead is make the blocks usable
outside `main.md`:

  * `--write` copies each block to `figures/<slug>.mmd`, for uploading to Mermaid Live, and records
    its SHA-256 in `figures/figures.json`. `check.py` compares that hash with the current block and
    warns when a rendered image is older than the diagram it was made from.
`scripts/export.py` reads that manifest when it builds `main-export.md`, the copy of the paper in
which the diagrams are replaced by the rendered images.

Usage (run from the repository root):
    python -I scripts/figures.py             dry run: report the figures found and their state
    python -I scripts/figures.py --write     write figures/*.mmd and figures/figures.json

The .mmd files are generated, like the `- >` lines of the claims file: edit the block in `main.md`
and run `--write` again, never the other way round.
"""
import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
MAIN = ROOT / "main.md"
FIGURES = ROOT / "figures"
MANIFEST = FIGURES / "figures.json"
IMAGE_SUFFIX = ".svg"

# Figure number -> file stem. A figure without an entry falls back to "figN" and is reported,
# so a new diagram is named deliberately rather than by an accident of its caption wording.
NAMES = {1: "fig1-timeline", 2: "fig2-morphology-pipeline"}

CAPTION = re.compile(r"^\*Figure (\d+)\.\s*(.+?)\*$")


def find_blocks(lines):
    """Return [(figure number, slug, caption, body, first line, last line)] for the mermaid fences.

    The caption is the nearest `*Figure N. ...*` line above the fence. check.py repeats this
    scan in a few lines of its own; keep the two in step if the fence or caption format changes.
    """
    out, i = [], 0
    while i < len(lines):
        if lines[i].strip().startswith("```mermaid"):
            start = i
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                i += 1
            body = "\n".join(lines[start + 1:i])
            number, caption = None, ""
            for back in range(start - 1, max(start - 6, -1), -1):
                m = CAPTION.match(lines[back].strip())
                if m:
                    number, caption = int(m.group(1)), m.group(2).strip()
                    break
            slug = NAMES.get(number, f"fig{number}" if number else f"figure-{len(out) + 1}")
            out.append((number, slug, caption, body, start, i))
        i += 1
    return out


def digest(body):
    return hashlib.sha256(body.replace("\r\n", "\n").encode("utf-8")).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--write", action="store_true", help="write figures/*.mmd and figures/figures.json")
    args = parser.parse_args()

    lines = MAIN.read_text(encoding="utf-8").split("\n")
    blocks = find_blocks(lines)
    if not blocks:
        print("no ```mermaid block found in main.md")
        return

    manifest = {}
    if MANIFEST.exists():
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))

    for number, slug, caption, body, start, _ in blocks:
        sha = digest(body)
        known = manifest.get(slug, {})
        image = FIGURES / (slug + IMAGE_SUFFIX)
        state = "image missing" if not image.exists() else (
            "image may be stale (the block changed)" if known.get("sha256") not in (None, sha) else "up to date")
        print(f"Figure {number} [{slug}] line {start + 1}: {len(body.splitlines())} lines, {state}")
        if number is None:
            print("    no '*Figure N. ...*' caption found above the block; it was named by position")
        elif number not in NAMES:
            print(f"    no name for figure {number} in NAMES; add one to scripts/figures.py")

    if args.write:
        FIGURES.mkdir(exist_ok=True)
        for number, slug, caption, body, _, _ in blocks:
            (FIGURES / (slug + ".mmd")).write_text(body + "\n", encoding="utf-8", newline="\n")
            manifest[slug] = {"figure": number, "caption": caption, "sha256": digest(body),
                              "image": slug + IMAGE_SUFFIX}
        MANIFEST.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
                            encoding="utf-8", newline="\n")
        print(f"\nwrote {len(blocks)} .mmd file(s) and {MANIFEST.relative_to(ROOT).as_posix()}")


main()
