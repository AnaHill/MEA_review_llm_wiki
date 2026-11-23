# docs/images/: images of the repository README

The images here are screenshots, not generated files, so nothing checks that they are current. This page records how they were made, so that they can be retaken when the wiki has changed enough that the picture no longer matches its caption, and keeps one idea that was considered and not carried out.

## Obsidian graph view (`fpd-end-conventions-graph-view.png`, 2026-11-23)

### Settings

Graph view uses the same syntax as Obsidian search (https://obsidian.md/help/plugins/search).

- **Filter:** `path:wiki -file:index -file:log`. `index.md` and the log link to almost every page and would turn the graph into one star around them; `-file:log` drops `log.md` and the archives in `wiki/log-archive/`.
- **Groups, in this order** (a node takes the colour of the first group it matches, so the order does the work):
  1. `path:wiki/papers`, blue `#5B8DD6`: the many paper pages, in a calm colour that leaves the structure visible.
  2. `path:wiki`, orange `#E8833A`: everything else in `wiki/`, that is the concept and method pages in its root, the hubs that should stand out.
  3. Optional, placed above the papers group: `tag:#type/review`, teal `#2BA38A`, to set the review and perspective papers apart.
- **Root pages only, without relying on the order:** `path:wiki -path:wiki/papers -path:wiki/assets` (`papers/`, `assets/` and `log-archive/` are the subfolders of `wiki/`), or the regular expression `path:/^wiki\/[^\/]+$/`, which also holds if more subfolders are added.
- **Tags:** with the Tags toggle on, the tags of the front matter appear as their own nodes (green in the image); `type/method` shows as `method`.
- **Highlight:** hover over or click the chosen node; its links turn purple and the rest of the graph dims.
- **Text fade threshold:** raise it until only the names around the highlighted node are readable; otherwise the labels cover each other.
- **Background:** the dark theme reads well on GitHub in both its light and dark mode.

Blue and orange stay distinguishable for the common forms of colour blindness.

### Choosing the node to highlight

The picture should show what the wiki adds to a reference manager: a page that compares sources, not one that summarises a single source. Count the links of the candidate pages first; a star with ten to twenty rays reads well, more turns into a blur. The counts on 2026-11-23 (links between wiki pages, inbound and outbound):

| Page | In | Out | Verdict |
|---|---|---|---|
| `fridericia-rate-correction` | 20 | 17 | the largest hub, but rate correction is not the main message of the paper |
| `maki-2023-opinion` | 18 | 14 | not chosen: centring the author's own paper moves the picture from the method to the author |
| `fpd-end-conventions` | 15 | 16 | **chosen**: the method page behind Table 2, on one of the four gaps; it sets side by side how each source defines the start and end of the FPD |
| `multimodal-measurement` | 16 | 13 | possible |
| `hipsc-cm-maturation` | 13 | 13 | the previous image; a side theme, with its paper nodes at the edges |

To count again, a few lines of Python over `wiki/` are enough: collect the targets of `[[...]]` and `](...md)` links of each page outside the log, index and reference list, and tally them in both directions.

### The caption

The caption in the README states numbers read off the image (fourteen paper pages, six concept pages and two tags around `fpd-end-conventions`). When the image is retaken, count them again from the new picture, and change the date in the caption.

## Before/after pair for the blog post (tag rework)

The blog post shows the wiki before and after the tag rework of 2026-11-14 (log 2026-11-14 lint), which replaced 53 tags, 34 of them used once, with a fixed vocabulary that follows the sections of the paper. The "before" screenshot exists (in the private post folder, not in this repository): filter `path:wiki -index.md`, Tags on, no colour groups, no node highlighted, the Filters panel open on the right. For the pair to show the tags and nothing else, take the "after" screenshot under the same conditions:

- **Filter:** `path:wiki -file:index -file:log` (the log has moved since, so `-index.md` alone would now let it in), Tags on.
- **No highlight:** keep the pointer off the nodes, so that no star of purple links appears.
- **Groups:** the blue and orange groups above may stay; the tag nodes must remain visible in their own colour.
- **Framing:** about the same zoom and crop as the "before" image; the Filters panel may stay open, as it explains the missing index.
- **Check:** the tag nodes in the picture should all come from the Tag vocabulary of `AGENTS.md`; the caption names three of them.

## Markmap of the paper outline: considered, not done (2026-11-21 to 2026-11-23)

A mind map of `main.md` made with the Markmap extension for VS Code was considered as a README or blog image. It was not made; the findings are kept here in case the idea returns.

- **The problem, measured on 2026-11-21.** A markmap of `main.md` works only with `foldLevel: 1`. At level 2, markmap 0.3 makes a node of every list item (not of paragraphs), which puts forty list nodes in the picture: Conclusion 4 (the longest 1304 characters, mean 960), Limitations 7 (628 / 320), Abstract 4 (141 / 128), Abbreviations 15, Highlights 7. With `wrapWidth: 300`, a node of a thousand characters becomes a column ten lines tall, and that is what breaks the picture. The length of the title is not the cause.
- **The solution that was planned: a separate `docs/paper-outline.md`** holding only the heading tree and a short title. The markmap then shows the structure (the seven subsections of the Literature review, the two of the Discussion) without the list noise, and no presentation matter enters the source file of the paper. The plan had three steps:
  - `scripts/outline.py` reads the `#` and `##` headings of `main.md` (skipping the front matter and `# References`, with the same logic as `main_sentences` in `claim_quotes.py`) and writes `docs/paper-outline.md`: front matter with a short `title` and `markmap: foldLevel/theme/wrapWidth`, then the headings as they are, no lists.
  - Keep it current the way the figures are kept: store a hash of the heading tree and let `check.py` warn when the headings of `main.md` have changed but the outline has not been regenerated (`figures.py` and `figures/figures.json` are the model).
  - Render the image only when the headings of the paper are final (the title changed on 2026-11-21, and the Discussion gained two subsections).
- **Rejected alternative: `foldLevel: 2` with `<!-- markmap: fold -->` directives.** The installed markmap-vscode 0.3.1 recognises the `fold` and `foldAll` directives (checked in the extension code), but the directive would be needed in five sections, and a line `# Highlights <!-- markmap: fold -->` would break `check_abbreviations.py`: its `section()` requires the heading line to end with the heading, so Highlights would no longer be excluded from the abbreviation check, and APD90, FPD and MEA would start to warn. A one-line change to the script would fix that, but the price is presentation matter in the source of the paper.
- **Decision (2026-11-23):** not carried out for now; the README uses the graph view image instead. If the idea returns, start from the planned solution above.
