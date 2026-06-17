# Modeling mutation-specific arrhythmogenic phenotypes in isogenic human iPSC-derived cardiac tissues

**Authors:** Thomas L. Maurissen\*, Masahide Kawatou\*, Víctor López-Dávila\*, Kenji Minatoya, Jun K. Yamashita, Knut Woltjen (\*equal contribution)  
**Year:** 2024  
**Venue:** Scientific Reports 14:2586  
**File:** [[raw/maurissen-2024-mutation.pdf]]  
**DOI:** 10.1038/s41598-024-52871-1

## Contribution
Generates compound heterozygous KCNH2 mutant hiPSC lines (LQTS2 N588D; SQTS N588K) using CRISPR-Cas9 + ssODN in an isogenic background (409B2), and demonstrates that 3D cardiac tissue sheets (CTSs) incorporating non-cardiomyocyte support cells are required to reveal TdP-like arrhythmic waveforms. Establishes compound heterozygous editing as a solution to the problem of unintended homozygous CRISPR outcomes.

## Methodology
- **Cell line:** 409B2 hiPSCs (RIKEN BRC #HPS0076)
- **Genome editing:** CRISPR-Cas9 + single-stranded oligodeoxynucleotide (ssODN) for precise heterozygous SNP introduction
- **Mutations:** KCNH2 N588D (LQT26; LQTS2 phenotype) and KCNH2 N588K (SQT22; SQTS phenotype)
- **MEA platform:** Alpha MED Scientific MED system (MED-P515A); 64 channels, 8×8 grid; 50 µm square electrodes, 150 µm intervals
- **Preparations:**
  - 2D monolayers: standard cardiomyocyte-only cultures
  - 3D cardiac tissue sheets (CTSs): hiPSC-CMs + mesenchymal cells (MCs) layered on decellularized matrix
- **FPD measurement:** FPDcF (Fridericia-corrected: FPD / RR^0.33)
- **Arrhythmia:** E-4031 challenge at multiple concentrations; arrhythmogenic scoring

## Findings
- **FPDcF:** parent 231±24 ms; SQT22 82±18 ms; LQT26 323±21 ms — consistent with expected phenotypes
- **TdP-like waveforms** only emerged in 3D CTSs containing mesenchymal cells (MCs); 2D monolayers did not exhibit characteristic TdP morphology
- **LQT26** arrhythmogenic score was significantly higher than both parent and SQT22
- **SQT22** required substantially higher E-4031 concentrations to trigger arrhythmic events, consistent with partial hERG gain-of-function protective effect
- **Compound heterozygous editing** reliably recapitulates heterozygous disease states; standard CRISPR often produces unintended homozygous edits, which overrepresent the phenotype

## Limitations
- Alpha MED 64-channel system limits spatial propagation mapping compared to newer high-density platforms
- CTSs require more complex preparation than monolayers; not yet standardized for routine drug screening
- Compound heterozygous strategy is technically demanding; may not be accessible to all labs

## Relevance to our paper
Cited in main.md for: (1) the FPDcF metric applied to mutation-specific phenotypes, (2) the necessity of 3D tissue formats for TdP-relevant endpoints, and (3) the isogenic design as best practice for mechanistic studies. Also relevant to LQTS disease modeling use case for MEA.

## See also
- [[wiki/papers/park-2025-cardiotoxicity.md]]
- [[wiki/papers/hwang-2023-spheroids.md]]
- [[wiki/papers/altrocchi-2023-chronic.md]]
