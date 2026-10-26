# Notes for turning main.md into a PDF (Zenodo deposit)

Things in `main.md` that commonly break or look wrong when Markdown is converted to PDF, and things to settle at deposit. Written 2026-10-18 for use when the PDF export is made; revisit if `main.md` changes.

## Revised export plan (2026-10-26): HTML first, PDF made from the HTML

Background: a test export with the VS Code "Markdown PDF" extension produced `main.html` and `main.pdf`. The HTML was a faithful conversion (all 9 `h1` and 8 `h2` headings, both tables, the KaTeX formula, Unicode characters and the escaped hash `\#CM01` came out correctly, and no comment was visible to a reader), but the PDF was not usable, and the HTML had problems that must be fixed before anything is deposited. Plan: make the HTML the master, then print the PDF from it.

Problems found in the test export:

- **Title and author missing.** The YAML front matter was dropped, so the page starts with the preprint line and "Abstract". The paper's title, author, affiliation and keywords are not shown anywhere, and the browser tab title is "main.md". Fix: add a visible title block (title, author, affiliation, date) and set `<title>`.
- **Diagrams are drawn at view time.** The HTML loads Mermaid from `https://unpkg.com/mermaid/dist/mermaid.min.js` (no version pinned) and draws the two diagrams in the reader's browser. Offline, with JavaScript blocked or after a Mermaid release that changes the layout, the figures break or show raw code. Not acceptable in an archived deposit. Fix: render both diagrams once to SVG (mermaid-live or mermaid-cli) and embed them as images with alt text; then the HTML needs no script at all.
- **Links are not clickable.** `main.md` has 26 URLs but the HTML has one `<a href>`; the DOIs in the reference list are plain text. Fix: write the DOIs and URLs as links or use an extension or converter that auto-links.
- **Comments remain in the HTML source.** Six comments (two style-marker pairs, `needs citation(s)`, `Continue manual check here`). Invisible to readers, visible in "view source" and to indexers. Fix: remove them from `main.md` before the export (the ToDo list has the grep).
- **VS Code page template.** The file is 1.5 MB because the VS Code stylesheet, KaTeX styles and fonts are embedded, and it has dark-theme logic keyed to the VS Code body class. Fix: use a small own print stylesheet or accept the size; check it in both a light and a dark browser theme.
- **PDF page breaks.** In `main.pdf` Figure 1's caption is on page 2 and its diagram on page 3, and Figure 2 is split over pages 9–11 (page 9 is an empty grey box). Every page also carries the header "main.md" and the date. Fix: print the PDF from the finished HTML with the browser (Chrome or Edge, "Save as PDF", background graphics on, headers and footers off) and add `figure, table { break-inside: avoid; }` to the stylesheet so the caption and the figure stay together; with the diagrams as SVG images this works reliably.

Deposit plan: PDF as the main file (Zenodo previews PDFs and search engines index them best; check Zenodo's current handling of HTML files before relying on it), the self-contained HTML as an additional file. Do the export last, after `main.md` is final.

Checks on the finished files: open the HTML with the network disabled and confirm both figures show; confirm title, author and keywords are visible; click a DOI link; page through the PDF for figures, tables and the formula; search the PDF text for `<!--`, `\#` and stray asterisks.

The checklist below was written for a generic Markdown-to-PDF route; items about Mermaid, LaTeX, tables and Unicode still apply but are now checked in the HTML first.

## Elements in main.md that need handling

- **Mermaid diagrams (2).** Figure 1 (timeline) and Figure 2 (flowchart) are fenced ```mermaid blocks. Pandoc and most Markdown-to-PDF tools print them as code. Render them to SVG or PNG first (for example with mermaid-cli) and replace the blocks with images, keeping the captions that sit above them as italic lines.
- **Mermaid labels with line breaks.** Figure 2 uses literal `\n` inside node labels. This is correct for Mermaid, but check the rendered image for overlong boxes.
- **Inline LaTeX (1).** The Fridericia formula `$FPDcF = FPD/RR^{0.33}$` needs math support in the converter. If the tool has none, the dollar signs appear as plain text.
- **Tables (2).** Table 1 has long cell text in the last column and Table 2 has five columns; both can overflow the page width or split badly. Use landscape pages or a smaller table font, or allow column wrapping, and check that the header row repeats on page breaks.
- **Unicode characters.** The text contains Δ, ², ⁺, ≥, – and — and the letters á ä ó ö ř (Mäki, Přibyl, Später and so on). A LaTeX-based PDF engine with a font lacking these glyphs drops or garbles them; use a Unicode engine (XeLaTeX or LuaLaTeX) with a font that includes Greek and superscripts, or a browser-based (HTML to PDF) route.
- **Front matter and horizontal rules.** The YAML block at the top (title, description, author) must be consumed as metadata and not printed. The five `---` section separators are horizontal rules; in Pandoc a `---` line can be misread as a YAML block if it is followed directly by text, which is not the case now but is easy to break by editing.
- **Reference list style.** Entries are plain APA paragraphs with italic journal titles and volume numbers. Hanging indents and clickable DOI links are not produced automatically; add them in the template or CSS if wanted.
- **Italic caption lines.** Figure and table captions are single italic lines above the object. Keep them attached to their figure or table so they do not end up on a different page.
- **Escaped hash.** `main.md` writes the standard's name as `AIMS \#CM01` so that Obsidian does not read it as a tag. All identifiers that start with a hash are escaped this way throughout the repository (see "No stray tags" in AGENTS.md). The converter should print the escaped form without the backslash, as `AIMS #CM01`; check this in the PDF.
- **Bold text and emphasis markers.** The draft uses bold for key terms and `*...*` for search terms and journal names; check that none of the asterisks printed literally.

## Content that must be resolved before the export

- [ ] No `[CITATION NEEDED]` flag remains as of 2026-10-18; re-check with `grep -n "CITATION NEEDED" main.md` after any further edits.
- [ ] Confirm the Declarations text (status, competing interests, AI assistance, funding, licence, data and code availability). Funding (none) and licence (CC BY 4.0) were added on 2026-10-18.
- [ ] Affiliation is set to "Independent researcher" and keywords are stored in the YAML front matter of `main.md` (`author` and `keywords`); the PDF template must print them from there. 
- [ ] Keywords for the Zenodo form: multielectrode array, hiPSC-cardiomyocytes, field potential duration, rate correction, cardiac safety pharmacology, review.
- [ ] Still missing in the Markdown: date and version (Zenodo adds the deposit date; the version can be "Version 1").
- [ ] The sentence at the top ("Preprint, not peer reviewed. Prepared with AI assistance; see Declarations.") should survive into the PDF.
- [ ] Check that the PDF is not larger than expected and that links in the reference list work.

## Zenodo deposit points to decide

- [ ] Resource type (preprint or publication, report). The licence is decided: CC BY 4.0, the same as the opinion paper (Mäki, 2023); select the same one on the deposit form.
- [x] Whether to link the deposit to the opinion paper's Zenodo record as a related work.
- [x] Which version of the opinion paper to cite: the review currently cites v3 (Zenodo record 20807245, published 23 June 2026) with the year 2023, explained in the version note in Declarations.
- [x] Whether the repository link in the Declarations should stay (https://github.com/AnaHill/MEA_review_llm_wiki), since the source notes and log are public there.

## Repository link and snapshot (revised 2026-10-24)

The Declarations point to https://github.com/AnaHill/MEA_review_llm_wiki for the source notes and log. That address does not change and `main.md` (including the Declarations) is not edited for this. What does change is the content behind the address: a reader who follows it later sees the repository as it is then, not as it was at deposit. This is acceptable and needs no action; the steps below are optional and only for your own reference.

- [ ] Optional: after the last commit, create an annotated tag on it (for example `git tag -a v1.0-preprint -m "state at Zenodo deposit"` and `git push origin v1.0-preprint`). It does not change the link and needs no change in `main.md`.
- [ ] Do not enable the automatic GitHub-to-Zenodo archiving of releases: it would mint a second DOI for the repository. The PDF is deposited manually and linked to the opinion paper's record.
- [ ] After the Zenodo deposit is published, add its link to the start of `README.md` (the ToDo item "Kun julkaistu Zenodossa").
- [x] Licence: `LICENSE` (CC BY 4.0 for the written content), `scripts/LICENSE` (MIT for the code) and a README section were added on 2026-10-24.
- [ ] Check that the non-open-access PDFs (`raw/pramudito-2026-ensemble.pdf`, `raw/clements-2025-aims-poster.pdf`) are not in the pushed history: `git log --all -- raw/pramudito-2026-ensemble.pdf raw/clements-2025-aims-poster.pdf` printed nothing on 2026-10-24.
