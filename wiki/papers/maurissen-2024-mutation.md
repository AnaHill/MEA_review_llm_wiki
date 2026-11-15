---
tags: [3d-model, disease-model, rate-correction]
---

# Modeling mutation-specific arrhythmogenic phenotypes in isogenic human iPSC-derived cardiac tissues

**Authors:** Thomas L. Maurissen\*, Masahide Kawatou\*, Víctor López-Dávila\*, Kenji Minatoya, Jun K. Yamashita, Knut Woltjen (\*equal contribution)  
**Year:** 2024  
**Venue:** Scientific Reports 14:2586  
**File:** [[raw/maurissen-2024-mutation.pdf]]  
**Supplementary:** [[raw/maurissen-2024-mutation-supplementary.pdf]] (Figures S1–S8, Tables S1–S11)  
**DOI:** 10.1038/s41598-024-52871-1

## Contribution
Generates compound heterozygous KCNH2 mutant hiPSC lines (LQTS2 N588D; SQTS N588K) using CRISPR-Cas9 + ssODN in an isogenic background (409B2), and uses 3D cardiac tissue sheets (CTSs) of hiPSC-CMs plus mesenchymal cells (MCs), the format the authors' earlier work (Kawatou et al., 2017) found necessary for TdP-like waveforms, to show E-4031-induced TdP-like/VT-like waveforms and genotype-dependent arrhythmogenicity. A mix of ssODN templates (missense plus silent PAM-blocking) is used to obtain compound heterozygous clones and reduce indels on the second allele.

Note: page checked against the source text on 2026-10-24; statements not supported by the paper were removed or reworded. Supplement ingested 2026-11-15 (Supplementary Figures 7 and 8 and Tables 3–6, 10 and 11 read; Figures 7 and 8 and Tables 3 and 4 viewed as rendered pages).

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

### Supplementary material
Read 2026-11-15. The per-sample tables and the clone-level figures add context that the main text does not give:

- **Per-probe values, 2D (Supplementary Table 3).** Each row is one MEA probe, with its differentiation run, cardiomyocyte purity and recording day. The group means match the main text exactly (parent 231.3, SQT22 82.3, LQT26 322.6 ms), but the spread within a genotype is wide: parent FPDcF 165–282 ms (n = 7), SQT22 57–114 ms (n = 12), LQT26 222–556 ms (n = 9). The spread tracks the differentiation run: parent probes from run 1 (cardiomyocyte purity 68.3 %) gave 233–282 ms, those from run 3 (97.9 %) gave 165–222 ms.
- **The ± values could not be reproduced.** From the same per-probe values, the standard deviation is 49 ms (parent 2D), 18 ms (SQT22 2D) and 102 ms (LQT26 2D), and the standard error 19, 5 and 34 ms; the main text gives ± 24, ± 18 and ± 21 ms. Only SQT22 matches (its standard deviation). The Methods say values are mean ± SEM. Our calculation; the means themselves match.
- **Per-sheet values, 3D (Supplementary Table 4).** All sheets used for the MEA recordings were mixed at **1:1 cardiomyocytes to mesenchymal cells** (the Methods allow 3:1 or 1:1). The 2D recordings come from differentiation runs 1–3 and the 3D recordings from runs 3–4, so only one run is shared. Recording day from plating was 4–8 days in 2D and 3–20 days in 3D.
- **The 3D "LQT" group is not one clone.** Its five sheets are LQT46 (three, run 3) and LQT26 (two, run 4). The Figure 4c caption says "LQT26 and LQT46 (n = 5)", but the Results text attributes the 3D value to "the LQT26 mutant". The 2D value (323 ms) is LQT26 only.
- **The E-4031 dose–response in 3D is LQT46, not LQT26** (Supplementary Tables 5–6 and Supplementary Fig. 8c: parent n = 3, SQT22 n = 5, LQT46 n = 3). The relative FPDcF change at 30 nM is about +30 % in the parent, +15 % in SQT22 and +5 % in LQT46.
- **Arrhythmias mostly needed 1000 nM (Supplementary Table 11).** Counts of sheets whose arrhythmia first appeared at each concentration: parent 1/1/1/3/1/5 and SQT 1/0/0/0/0/7 and LQT 0/0/0/1/3/1 at 0.3, 3, 10, 30, 100 and 1000 nM. The arrhythmogenic score counts only events up to 100 nM as "drug test induced", so the 1000 nM events (five parent, seven SQT, one LQT) score as "not induced".
- **Clone-to-clone spread within a genotype (Supplementary Fig. 7a).** Eleven clones are shown. The three control clones carrying only the silent blocking mutation differ among themselves (CTL1 median about 220 ms, CTL41 and CTL60 about 155 ms), and so do clones of one genotype: SQT96 about 165 ms against SQT22 about 85 ms, LQT79 about 190 ms against LQT26 about 305 ms. The main text reports SQT22 and LQT26, the two clones with the most extreme values. Panel b pools the clones (parent n = 7, CTL n = 11, SQT n = 42, LQT n = 21); its caption labels the pooled short-QT group "SQT22".
- **Sheet purity varies more than the main text suggests (Supplementary Fig. 8b).** The individual sheets span roughly 5–60 % cardiomyocytes; 25–41 % is the range of the three group means, and the difference between genotypes is not significant.
- **Vehicle control (Supplementary Table 10).** In 2D, FPDcF was 249–259 ms across 0.1–0.5 % DMSO (n = 5), so the vehicle itself did not shift the endpoint.

## Limitations
Stated by the authors (pp. 3–7):
- Arrhythmia in vitro may depend on external stimuli, and SQT22 did not show significantly more arrhythmias.
- How MCs influence arrhythmia needs further study, and the non-cardiomyocyte cells need better characterisation.
- Pre-TdP stages are not addressed.

Our observations (not from the paper), from the supplement: the 3D LQT group pools LQT46 and LQT26 while the 2D value is LQT26 alone; the E-4031 dose–response in 3D is LQT46; 2D and 3D recordings come mostly from different differentiation runs; clone-to-clone differences within one genotype are as large as some genotype differences (Supplementary Fig. 7a); and the ± values of the main text do not match the dispersion of the per-probe data.
- CTS cTnT purity was only 25–41%, and the 3D phenotyping used one clone per genotype (n = 5–13).

## Relevance to our paper
Since 2026-10-31 (grill decision) main.md presents this study in the 3D section with two findings: FPDcF close in 2D and 3D for all three genotypes (so this endpoint transferred in that setting), and TdP/VT-like waveforms reported in 3D sheets only, with the purity caveat. The earlier sentence that the findings "reinforce the caution raised by Mäki (2023)" was removed because the 2D/3D values contradict it. Also cited in the Conclusion's third gap.

Cited in main.md for (1) the Fridericia-corrected FPD, (2) as an example of MEA analysis in 3D isogenic mutation-specific tissue models (LQTS and SQTS phenotypes), and (3) since 2026-11-15 in Table 2 as a study that states its FPD end point (first peak to second peak, i.e. R-to-T-peak); see [[wiki/fpd-end-conventions.md]]. The 3D passage was simplified the same day: the genotype enumeration and the cardiomyocyte purity percentage were dropped, the latter replaced by the mesenchymal cells it reflects. The review's formula notation RR^0.33 is the review's own; the paper writes the cube root of the inter-spike interval.

## See also
- [[wiki/papers/park-2025-cardiotoxicity.md]]
- [[wiki/papers/hwang-2023-spheroids.md]]
- [[wiki/papers/altrocchi-2023-chronic.md]]
- [[wiki/papers/botti-2026-insilico.md]]
- [[wiki/papers/ismaili-2023-hamburg.md]]
- [[wiki/papers/blinova-2018-multisite.md]] — both report Fridericia-corrected FPD
- [[wiki/fridericia-rate-correction.md]]
- [[wiki/3d-models.md]]
- [[wiki/fpd-end-conventions.md]]
