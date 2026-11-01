---
tags: [review, mea-physics, cell-electrode-coupling, impedance, electroporation, cardiotoxicity]
---

# Microelectrode arrays: from electrophysiology to integrated cancer treatment induced cardiotoxicity assessment

**Authors:** Neda Karami, Sebastian Knafl, Heinz D. Wanzenboeck, Sonia Prado-López  
**Year:** 2026  
**Venue:** Frontiers in Electronics 7:1886715 (review; received 20 May 2026, published 18 September 2026)  
**File:** [[raw/karami-2026-mea-cardiotoxicity.pdf]] (open access, CC BY 4.0; the copy came through ProQuest)  
**DOI:** 10.3389/felec.2026.1886715

Note: ingested 2026-11-01 from the full text (30 pages, read as PDF; figures viewed). Affiliation: Institute of Solid-State Electronics, TU Wien. Figure 5B is adapted from Shaik et al. (Springer) "with permission from the rights holder", so it is not covered by the CC BY licence of the article and cannot be reused in main.md.

## Contribution
A narrative review of in vitro assays for cancer-treatment-induced cardiotoxicity, centred on microelectrode arrays: CiPA and its recommended assays, cardiac electrophysiology, the physics of field potential and impedance recording, passive, CMOS and TFT MEA architectures, intracellular-like recording by electroporation, and MEA studies of chemotherapeutics. Most of it (cancer biology, CiPA history, impedance spectroscopy theory) is outside the scope of main.md; the parts used here are the MEA-physics sections.

## Methodology
Narrative review; no search method stated. Tables: CiPA assays (Table 2), passive/CMOS/TFT MEAs (Table 3), extracellular versus electroporation versus patch clamp (Table 4), MEA cardiotoxicity studies (Table 5).

## Findings
Statements relevant to main.md (page numbers of the article):
- **FP is not the AP (p. 9):** "FPD and APD are not equivalent measurements"; the FP "is influenced by a variety of factors that do not reflect the intracellularly measured APD. These factors could be electrode geometry, cell-electrode coupling, cell density and degree of gap junctional coupling and conduction properties".
- **Superposition (p. 14):** under volume conduction the recorded voltage is proportional to the transmembrane current, so the FP is proportional to the second derivative of the AP; "the potential changes of all transmembrane ion currents of all cells will contribute to the potential at the distant electrode. Consequently, the recorded signal will be a superposition of these individual signals", which the authors note matters especially for 3D organoids.
- **Cell–electrode interface model (pp. 13–14, Figure 5B, Equations 4–7):** the point-contact model (Fromherz et al., 1991; simplified by Shaik et al., 2022) relates the measured voltage to the membrane potential through the seal resistance, the junctional membrane impedance, the electrode impedance (Randles circuit plus spreading and metal resistance) and the amplifier impedance. With a tight seal the recorded signal follows the membrane potential, with loose contact its first time derivative, and with little or no attachment its second derivative. Table 4 states that passive extracellular MEA signals are proportional to the first (high seal, "typical for MEAs") or second (loose seal) derivative; the text and table differ slightly in wording.
- **Impedance (pp. 16–18):** impedance is sensitive to cell–electrode distance (Giaever and Keese, 1991, distance changes of about 1 nm), to cell morphology, and to viability (dying cells typically show a decreased impedance magnitude, for example after membrane disruption in necrosis).
- **Electroporation (p. 11, Table 4):** local electroporation gives attenuated intracellular-like APs on planar MEAs; in Braeken et al. (2012) the dofetilide effect was visible in open-cell recordings but not in the extracellular FP; Table 4 lists APD50, APD90 and depolarization time as extractable features (citing Lee et al., 2024).
- **TFT-MEAs (pp. 10–11, Table 3):** cites Hu et al. (2025, Sensors and Actuators B) and Hu et al. (2026) for transparent TFT-MEAs recording optical, voltage and impedance signals.
- **Outlook (p. 24):** high-throughput multiparametric recordings will need a move from manual feature extraction to AI and machine-learning analysis.

## Limitations
Our observations (not from the paper): a narrative review outside the hiPSC-CM analysis focus; several citation slips, for example cell types on p. 11 cited to unrelated papers (heart organoids to Hamill et al., 1981, a patch-clamp paper), "Can be used with heart organoids" listed as a disadvantage in Table 2, Iachetta et al. (2023) labelled "Xu et al. (2022)" in Table 5, and Ghosheh et al. (2023) cited as "Qin et al. 2024". Use it only for textbook-level statements (interface model, superposition, impedance sensitivity) and keep the primary sources in mind (Fromherz et al., 1991; Spira and Hai, 2013; Giaever and Keese, 1991).

## Relevance to our paper
Cited in main.md from 2026-11-01 in the device-separation part of the outlook (opening statement, equivalent-circuit sentence, ill-posed sentence, impedance sentence).

Supports the "Separating the recording system from the cellular signal" part of the Discussion and future outlook: (1) a source for the opening statement that the FP is shaped by tissue and hardware; (2) a source for the superposition argument behind the ill-posed inverse problem (register item 26); (3) the cell–electrode equivalent-circuit model as the concrete device model that system identification would have to estimate; (4) mechanistic support for the impedance-as-coupling hypothesis (register item 27). Candidate source found through it, not read: Lee, Park, Kim and Chung (2026), "Integrated electrophysiological and optical analysis of human iPSC-derived cardiomyocytes using transparent ITO microelectrode chip", Int. J. Stem Cells 19, 146–156 (possible hiPSC-CM counterpart to Hu et al., 2026, for the sensor-fusion paragraph).

## See also
- [[wiki/papers/lee-2024-cardiomea.md]]
- [[wiki/papers/hu-2026-tft-mea-multimodal.md]]
- [[wiki/papers/altrocchi-2023-chronic.md]]
- [[wiki/papers/botti-2026-insilico.md]]
- [[wiki/multimodal-measurement.md]]
