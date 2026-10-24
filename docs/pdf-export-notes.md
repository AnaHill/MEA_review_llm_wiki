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

## Repository snapshot (added 2026-10-24)

The Declarations point to https://github.com/AnaHill/MEA_review_llm_wiki for the source notes and log. A link to a moving branch will not match the deposited PDF after later edits, so freeze the state:

- [ ] Finish all edits to `main.md`, run `python -I scripts/check.py` (0 errors) and commit.
- [ ] Optional: add one sentence to Declarations (Data and code availability) such as "The state of the repository at the time of deposit is tagged v1.0-preprint." Commit it first, because the tag must sit on the commit that already contains the sentence.
- [ ] Create an annotated tag on that commit (for example `git tag -a v1.0-preprint -m "state at Zenodo deposit"` and `git push origin v1.0-preprint`) and, if wanted, a GitHub release from it. Do not enable the automatic GitHub-to-Zenodo archiving unless a second DOI is wanted; the PDF is deposited manually and linked to the opinion paper's record.
- [ ] Check that the repository is public and that the non-open-access PDFs (`raw/pramudito-2026-ensemble.pdf`, `raw/clements-2025-aims-poster.pdf`) are not in the pushed history (`git log --all -- raw/pramudito-2026-ensemble.pdf`); open-access PDFs keep their own licences (for example CC BY-NC-ND for Hayakawa et al., 2014).
- [ ] Add a LICENSE file or a README licence section (none exists on 2026-10-24); the paper itself is CC BY 4.0 (Declarations).

