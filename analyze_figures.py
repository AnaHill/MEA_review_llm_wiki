'''
Analyze figures and tables in a PDF file.
Usage:
python analyze_figures.py raw\some-paper.pdf
-> raw\some-paper.pdf — the positional pdf_path argument (required): the PDF file to analyze.
-> run with no flags and get the default behavior (output to .\figure_analysis, capped at 50 entries). 


python analyze_figures.py raw\some-paper.pdf -o custom_output --max-entries 0
-o custom_output (or --output-dir custom_output)
— overrides where the summary .txt file gets written. 
If omitted, it defaults to a figure_analysis folder next to the script.

--max-entries 0 — overrides the cap on how many figure/table matches get written to the output file. 
Default is 50; passing 0 means "no limit," so every match found in the PDF gets written.

Specific command python analyze_figures.py raw\some-paper.pdf -o custom_output --max-entries 0 
1) analyzes raw\some-paper.pdf, 
2) writes the results into .\custom_output\ instead of the default folder, 
3) and includes all matches instead of just the first 50.

Run python analyze_figures.py -h any time to see this help text from argparse itself.
'''

import argparse
import os
from pypdf import PdfReader

DEFAULT_OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "figure_analysis")
FIGURE_PATTERNS = ['figure', 'fig.', 'fig ', 'table']


def analyze_figures(pdf_path, output_dir, max_entries):
    reader = PdfReader(pdf_path)
    print(f"Total pages: {len(reader.pages)}\n")

    figure_summary = []

    for page_num, page in enumerate(reader.pages, 1):
        text = page.extract_text()
        lines = text.split('\n') if text else []

        for i, line in enumerate(lines):
            if any(pattern in line.lower() for pattern in FIGURE_PATTERNS):
                context = '\n'.join(lines[max(0, i - 1):min(len(lines), i + 3)])
                figure_summary.append({
                    'page': page_num,
                    'content': context.strip()
                })

    os.makedirs(output_dir, exist_ok=True)
    pdf_name = os.path.basename(pdf_path)
    output_path = os.path.join(output_dir, f"{os.path.splitext(pdf_name)[0]}_figures_summary.txt")

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(f"FIGURE ANALYSIS - {pdf_name}\n")
        f.write("=" * 70 + "\n\n")

        entries = figure_summary if max_entries is None else figure_summary[:max_entries]
        for fig in entries:
            f.write(f"\nPage {fig['page']}:\n")
            f.write(fig['content'] + "\n")
            f.write("-" * 70 + "\n")

    print(f"Found {len(figure_summary)} figure-related entries")
    print(f"Summary written to {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Extract figure/table caption context from a PDF.")
    parser.add_argument("pdf_path", help="Path to the input PDF file")
    parser.add_argument("-o", "--output-dir", default=DEFAULT_OUTPUT_DIR,
                         help=f"Output directory (default: {DEFAULT_OUTPUT_DIR})")
    parser.add_argument("--max-entries", type=int, default=50,
                         help="Maximum number of entries to write (default: 50, use 0 for unlimited)")
    args = parser.parse_args()

    max_entries = None if args.max_entries == 0 else args.max_entries
    analyze_figures(args.pdf_path, args.output_dir, max_entries)


if __name__ == "__main__":
    main()
