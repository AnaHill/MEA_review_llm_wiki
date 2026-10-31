---
tags: [3d-model, disease-model, lqts]
---

# Modeling mutation-specific arrhythmogenic phenotypes in isogenic human iPSC-derived cardiac tissues

**Authors:** Thomas L. Maurissen\*, Masahide Kawatou\*, Víctor López-Dávila\*, Kenji Minatoya, Jun K. Yamashita, Knut Woltjen (\*equal contribution)  
**Year:** 2024  
**Venue:** Scientific Reports 14:2586  
**File:** [[raw/maurissen-2024-mutation.pdf]]  
**DOI:** 10.1038/s41598-024-52871-1

## Contribution
Generates compound heterozygous KCNH2 mutant hiPSC lines (LQTS2 N588D; SQTS N588K) using CRISPR-Cas9 + ssODN in an isogenic background (409B2), and uses 3D cardiac tissue sheets (CTSs) of hiPSC-CMs plus mesenchymal cells (MCs), the format the authors' earlier work (Kawatou et al., 2017) found necessary for TdP-like waveforms, to show E-4031-induced TdP-like/VT-like waveforms and genotype-dependent arrhythmogenicity. A mix of ssODN templates (missense plus silent PAM-blocking) is used to obtain compound heterozygous clones and reduce indels on the second allele.

Note: page checked against the source text on 2026-10-24; statements not supported by the paper were removed or reworded.

## Methodology
- **Cell line:** 409B2 hiPSCs (RIKEN BRC \#HPS0076)
- **Genome editing:** CRISPR-Cas9 + single-stranded oligodeoxynucleotide (ssODN) for precise heterozygous SNP introduction
- **Mutations:** KCNH2 N588D (LQT26; LQTS phenotype) and KCNH2 N588K (SQT22; SQTS phenotype)
- **MEA platform:** Alpha MED Scientific MED system (MED-P515A); 64 channels, 8×8 grid; 50 µm square electrodes, 150 µm intervals
- **Preparations:**
  - 2D hiPSC-CM monolayers on MEA probes (cTnT purity at least 65%; samples below were excluded)
  - 3D cardiac tissue sheets (CTSs): hiPSC-CMs and MCs mixed (3:1 or 1:1) on gelatin-coated temperature-sensitive UpCell dishes and detached as sheets about 5 cell layers (100 µm) thick
- **FPD measurement:** FPDcF = FPD divided by the cube root of the inter-spike interval (s); one arbitrary electrode of the 64 analysed per probe
- **Arrhythmia:** E-4031 challenge at multiple concentrations; arrhythmogenic scoring

## Findings
- **FPDcF (2D monolayers):** parent 231±24 ms; SQT22 82±18 ms; LQT26 323±21 ms (n = 7, 12, 9) — consistent with expected phenotypes. 3D CTSs: 225±13 / 87±16 / 320±16 ms (n = 7, 5, 5).
- **TdP-like and VT-like waveforms** were induced by E-4031 in 3D CTSs; the authors attribute the need for MCs and 3D structure to their earlier work (this study did not test 2D with E-4031 or CTSs without MCs)
- **Arrhythmia score:** LQT26 significantly higher, and SQT22 significantly lower, than the isogenic control (Dunnett's test against the parent only)
- **SQT22:** the authors suggest the increased IKr current in N588K requires higher IKr-blocker concentrations to prolong FPD enough for arrhythmias (hypothesis, not tested); SQT22 had no significantly higher arrhythmia likelihood
- **Editing:** standard Cas9/ssODN editing commonly yields homozygous clones or clones with an indel on the second allele; the silent-blocker design reduced indels, and homozygous clones appeared only as a byproduct. The heterozygous isogenic lines reproduced the expected FPD shifts.

## Limitations
Stated by the authors (pp. 3–7):
- Arrhythmia in vitro may depend on external stimuli, and SQT22 did not show significantly more arrhythmias.
- How MCs influence arrhythmia needs further study, and the non-cardiomyocyte cells need better characterisation.
- Pre-TdP stages are not addressed.
- CTS cTnT purity was only 25–41%, and the 3D phenotyping used one clone per genotype (n = 5–13).

## Relevance to our paper
Since 2026-10-31 (grill decision) main.md presents this study in the 3D section with two findings: FPDcF close in 2D and 3D for all three genotypes (so this endpoint transferred in that setting), and TdP/VT-like waveforms reported in 3D sheets only, with the purity caveat. The earlier sentence that the findings "reinforce the caution raised by Mäki (2023)" was removed because the 2D/3D values contradict it. Also cited in the Conclusion's third gap.

Cited in main.md for (1) the Fridericia-corrected FPD and (2) as an example of MEA analysis in 3D isogenic mutation-specific tissue models (LQTS and SQTS phenotypes). The review's formula notation RR^0.33 is the review's own; the paper writes the cube root of the inter-spike interval.

## See also
- [[wiki/papers/park-2025-cardiotoxicity.md]]
- [[wiki/papers/hwang-2023-spheroids.md]]
- [[wiki/papers/altrocchi-2023-chronic.md]]
- [[wiki/papers/botti-2026-insilico.md]]
- [[wiki/papers/ismaili-2023-hamburg.md]]
