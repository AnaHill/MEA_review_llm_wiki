# Notes for turning main.md into a PDF (Zenodo deposit)

Things in `main.md` that commonly break or look wrong when Markdown is converted to PDF, and things to settle at deposit. Written 2026-10-18 for use when the PDF export is made; revisit if `main.md` changes.

## Elements in main.md that need handling

- **Mermaid diagrams (2).** Figure 1 (timeline) and Figure 2 (flowchart) are fenced ```mermaid blocks. Pandoc and most Markdown-to-PDF tools print them as code. Render them to SVG or PNG first (for example with mermaid-cli) and replace the blocks with images, keeping the captions that sit above them as italic lines.
- **Mermaid labels with line breaks.** Figure 2 uses literal `\n` inside node labels. This is correct for Mermaid, but check the rendered image for overlong boxes.
- **Inline LaTeX (1).** The Fridericia formula `$FPDcF = FPD/RR^{0.33}$` needs math support in the converter. If the tool has none, the dollar signs appear as plain text.
- **Tables (2).** Table 1 has long cell text in the last column and Table 2 has five columns; both can overflow the page width or split badly. Use landscape pages or a smaller table font, or allow column wrapping, and check that the header row repeats on page breaks.
- **Unicode characters.** The text contains Δ, ², ⁺, ≥, – and — and the letters á ä ó ö ř (Mäki, Přibyl, Später and so on). A LaTeX-based PDF engine with a font lacking these glyphs drops or garbles them; use a Unicode engine (XeLaTeX or LuaLaTeX) with a font that includes Greek and superscripts, or a browser-based (HTML to PDF) route.
- **Front matter and horizontal rules.** The YAML block at the top (title, description, author) must be consumed as metadata and not printed. The five `---` section separators are horizontal rules; in Pandoc a `---` line can be misread as a YAML block if it is followed directly by text, which is not the case now but is easy to break by editing.
- **Reference list style.** Entries are plain APA paragraphs with italic journal titles and volume numbers. Hanging indents and clickable DOI links are not produced automatically; add them in the template or CSS if wanted.
- **Italic caption lines.** Figure and table captions are single italic lines above the object. Keep them attached to their figure or table so they do not end up on a different page.
- **Bold text and emphasis markers.** The draft uses bold for key terms and `*...*` for search terms and journal names; check that none of the asterisks printed literally.

## Content that must be resolved before the export

- Remove or resolve every `[CITATION NEEDED]` flag (four at last count; list them with `grep -n "CITATION NEEDED" main.md`).
- Confirm the Declarations text (status, competing interests, AI assistance, data and code availability) and add funding information, which is currently missing.
- Add what the Markdown lacks: affiliation, date and version, and keywords if the deposit form wants them.
- The sentence at the top ("Preprint, not peer reviewed. Prepared with AI assistance; see Declarations.") should survive into the PDF.
- Check that the PDF is not larger than expected and that links in the reference list work.

## Zenodo deposit points to decide

- Resource type (preprint or publication, report) and license (the opinion paper (Mäki, 2023) is CC BY 4.0; keep the same unless there is a reason).
- Whether to link the deposit to the opinion paper's Zenodo record as a related work.
- Which version of the opinion paper to cite: the review currently cites v3 (Zenodo record 20807245, published 23 June 2026) with the year 2023, explained in the version note in Declarations.
- Whether the repository link in the Declarations should stay (https://github.com/AnaHill/MEA_review_llm_wiki), since the source notes and log are public there.
