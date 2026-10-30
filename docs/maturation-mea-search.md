# Targeted search: MEA-derived reference values for hiPSC-CM maturation

Search run on 30 October 2026 by Claude Code at the researcher's request; selection decided with the researcher the same day. This file records how the search was done, what was found, and why two sources were chosen for ingest. It is process documentation, not part of the wiki.

## 1. Question and starting point

**Question.** Has any published work (peer-reviewed or preprint, any year) proposed or validated reference values or a classifier for hiPSC-CM maturation status based on MEA (extracellular field potential) measurements, for example FPD, spike amplitude, upstroke/depolarization slope, conduction velocity, beat rate, or a combination of these as markers of maturity? Pre-2022 work counts if it answers the question; in the paper it would be marked as background (as Blinova et al., 2018 and Hayakawa et al., 2014 are).

**Claims in `main.md` that the search tests.**

- Section "Maturation status as an unresolved confound for MEA-derived metrics": "No peer-reviewed 2022–present study proposing or validating such MEA-only maturation reference values was identified in a targeted search of PubMed/MEDLINE, bioRxiv and Scopus (2 July 2026)".
- Same section, last sentence, and the fourth gap in the Conclusion: the components of an MEA-native maturity classifier (interpretable machine learning, the FPD–contraction link, the translational stake) "already exist in the literature, but have not yet been assembled" / "have not yet been combined into an MEA-native equivalent".

**Sources already in the wiki and therefore not proposed again:** Fetterman et al. (2024), Correia et al. (2024), Guerrelli et al. (2024), Scheurer et al. (2025), Hayakawa et al. (2014), Clements et al. (2025), Ismaili et al. (2023), Blinova et al. (2018) and the rest of `wiki/index.md`.

**Note on the earlier search.** `wiki/hipsc-cm-maturation.md` describes the 2 July 2026 check as "scoped via PubMed/bioRxiv/Scopus web search", i.e. web searches, not documented database queries. Its queries and record counts were not recorded. The search below is the first one with recorded queries.

## 2. Search strategy

### 2.1 PubMed/MEDLINE

Queried through the NCBI E-utilities API (esearch), all years, title/abstract fields. Record summaries and abstracts were retrieved with esummary/efetch, and the DOIs listed in section 4 come from those PubMed records.

Building blocks:

- **CM** = ("induced pluripotent stem cell-derived cardiomyocyte\*" OR "iPSC-CM\*" OR "hiPSC-CM\*" OR "iPS-CM\*" OR "hiPS-CM\*" OR "stem cell-derived cardiomyocyte\*" OR "hPSC-CM\*")[tiab]
- **CMB** (broad) = cardiomyocyte\*[tiab] AND (stem OR pluripotent OR iPS\* OR hiPS\* OR hPSC\* OR hESC\*)[tiab]; in S1–S4 also OR organoid\*[tiab]
- **MEA** = ("multielectrode array\*" OR "multi-electrode array\*" OR "microelectrode array\*" OR "MEA" OR "field potential\*")[tiab]
- **MAT** = (maturation OR maturity OR mature OR immature OR immaturity)[tiab]

The broad block CMB was added after the first round because abbreviation truncation (hiPSC-CM\*) is unreliable in PubMed.

| ID | Query | Records |
|---|---|---|
| Q1 | CM AND MEA AND MAT | 37 |
| Q2 | CM AND MEA AND ("maturation index" OR "maturity index" OR "maturity marker\*" OR "maturation marker\*" OR "maturation score" OR "maturity score" OR classif\* OR "reference value\*" OR benchmark\*) | 13 |
| Q3 | CM AND "conduction velocity" AND MAT | 21 |
| Q4 | CM AND ("electrophysiological maturation" OR "electrophysiological maturity" OR "functional maturation") AND MEA | 7 |
| Q5 | CM AND MEA AND ("culture time" OR "culture duration" OR "time in culture" OR "long-term culture" OR "days in culture" OR "culture age" OR longitudinal) | 4 |
| Q6 | CM AND MEA AND (fetal OR foetal OR adult) AND MAT | 14 |
| B1 | CMB AND MEA AND MAT | 52 |
| B2 | CMB AND MEA AND MAT AND (marker\* OR index OR score OR classif\* OR predict\* OR staging OR benchmark\* OR reference OR criteria OR indicator\*) | 18 |
| S1 | CMB AND (pseudotime OR trajectory) AND (electrophysiolog\* OR electrical) AND (maturation OR development\*) | 6 |
| S2 | CMB AND (CMOS OR "high-density" OR HD-MEA OR nanoelectronic\* OR "mesh electronics") AND (maturation OR development\*) | 25 |
| S3 | CMB AND (field potential / MEA terms) AND ("machine learning" OR "deep learning" OR classifier) AND (matur\* OR immatur\*) | 0 |
| S4 | CMB AND (field potential / MEA terms) AND ("adult-like" OR "fetal-like" OR "adult human" OR "human ventricular") AND matur\* | 8 |

Q1–Q6 gave 69 unique records; B1–B2 added 15 (84 in total). S1–S4 were screened separately (39 records, mostly overlapping or off-topic). S3 returning zero records is itself informative: no PubMed-indexed paper combines MEA/field-potential terms, machine learning and maturation in its title or abstract.

### 2.2 Citation chasing

Forward citations ("cited in", PubMed/PMC) of the candidates that looked closest to the question:

| Seed paper | Citing records screened |
|---|---|
| Zhu et al. (2017), PMID 28266620 | 25 |
| Kumar et al. (2019), PMID 31515494 | 29 |
| Lee et al. (2024), PMID 38946019 | 6 |
| Miyoshi et al. (2026), PMID 41712753 | 1 |

Backward chasing: the reference list of Scheurer et al. (2025) (already ingested, text dump in `figure_analysis/scheurer-2025-optical-ai/text.txt`) was checked for the source of its maturity labels; see section 5.2.

The citing records of Zhu et al. (2017) led to Lin et al. (2023).

### 2.3 Web search and bioRxiv

A general web search engine was used (Google Scholar itself could not be queried from the tool):

- hiPSC-CM maturation "multielectrode array" field potential maturity marker
- "maturation index" OR "maturity score" iPSC cardiomyocytes field potential MEA electrophysiological
- high-density microelectrode array tracking electrophysiological maturation human iPSC cardiomyocytes conduction velocity weeks
- bioRxiv iPSC cardiomyocyte maturation classifier field potential multielectrode array machine learning
- "electrophysiological maturation" "MEA" stem cell cardiomyocytes days differentiation field potential amplitude increase
- site:biorxiv.org iPSC cardiomyocytes field potential maturation multielectrode array

Two further web queries (conduction velocity / spike slope combined with maturation) were blocked by the tool's safety filter and returned nothing. bioRxiv preprint metadata were checked through the bioRxiv API (`api.biorxiv.org/details`); bioRxiv's own search page was not used.

### 2.4 Not searched

Scopus, Web of Science, Google Scholar (directly) and IEEE Xplore. Any statement in `main.md` about the search should therefore name only PubMed/MEDLINE, citation chasing and web searches including bioRxiv, unless a Scopus search is run separately.

## 3. Screening

All titles from the PubMed queries and citation lists were screened. About 25 abstracts were read. Inclusion as a candidate required that the paper record MEA or extracellular field potentials in stem cell-derived cardiomyocytes and relate at least one FP parameter to maturation (over time in culture or between maturation conditions). For the closest candidates the PMC full text was read through a tool that summarises the page; the numbers below come from those summaries and must be checked against the PDF at ingest. For Lin et al. (2023) only the first 100,000 characters of the PMC page (about two thirds) were read.

Exclusion reasons that recurred: MEA used only for drug response with no maturation comparison; maturation measured only with patch clamp, optical mapping or Ca²⁺ imaging; non-human or neonatal rat cells; reviews without primary data.

## 4. Candidates

"Full text" = PMC full text read through the summarising tool; "abstract" = PubMed abstract only. DOIs are taken from the PubMed records.

| # | Source | MEA/FP parameters linked to maturity | Comparison / validation | Answers the question? |
|---|---|---|---|---|
| 1 | Zhu, H., Scharnhorst, K. S., Stieg, A. Z., Gimzewski, J. K., Minami, I., Nakatsuji, N., Nakano, H., & Nakano, A. (2017). Two dimensional electrophysiological characterization of human pluripotent stem cell-derived cardiomyocyte system. *Scientific Reports*, 7, 43210. DOI 10.1038/srep43210. Full text. | FP amplitude (4–5-fold rise), FP dV/dtmax (15.3 → 122.9 µV/ms, days 18–26) and conduction velocity (about 35 → 120 mm/s) increase; FPDc roughly stable. The authors call the electrophysiological parameters more sensitive maturity indicators than the gene markers. | qPCR markers; conduction velocity compared with literature values for neonatal (about 0.3 m/s) and adult (about 1 m/s) cardiomyocytes. No patch clamp. Text and figure legends disagree (day of peak amplitude, FPD range). | Partly: proposes indicators, no reference values. Pre-2022 background. |
| 2 | Lin, Z., Garbern, J. C., Liu, R., Li, Q., Mancheño Juncosa, E., Elwell, H. L. T., Sokol, M., Aoyama, J., Deumer, U. S., Hsiao, E., Sheng, H., Lee, R. T., & Liu, J. (2023). Tissue-embedded stretchable nanoelectronics reveal endothelial cell-mediated electrical maturation of human 3D cardiac microtissues. *Science Advances*, 9(10), eade8513. DOI 10.1126/sciadv.ade8513. Full text (partial). | Machine-learning pseudotime trajectory (PHATE + Slingshot) computed from whole extracellular FP waveforms recorded on days 15–37; along the trajectory amplitude and dV/dt rise and spike duration falls. | scRNA-seq in separate samples and a different time window (no paired analysis); no patch clamp, no adult tissue comparison. 3D hiPSC-CM/hiPSC-EC microtissues with embedded mesh electrodes, not an MEA plate. | Partly: closest existing analogue of an FP-based maturity classifier, but gives a trajectory, not reference values. |
| 3 | Kumar, N., Dougherty, J. A., Manring, H. R., Elmadbouh, I., Mergaye, M., Czirok, A., Greta Isai, D., Belevych, A. E., Yu, L., Janssen, P. M. L., Fadda, P., Gyorke, S., Ackermann, M. A., Angelos, M. G., & Khan, M. (2019). Assessment of temporal functional changes and miRNA profiling of human iPSC-derived cardiomyocytes. *Scientific Reports*, 9, 13188. DOI 10.1038/s41598-019-49653-5. Full text. | Axion Maestro Edge, weeks 1/2/4: FPD 241 → 445 → 580 ms; conduction velocity 0.20 → 0.39 m/s; beat rate 57 → 42 bpm. | Conduction velocity set against a textbook adult value (0.5 m/s); qPCR and TEM against adult heart done separately, not linked to MEA values; n = 4 wells. | No (time course, no reference values). |
| 4 | Li, W., Luo, X., Strano, A., Arun, S., Gamm, O., Poetsch, M. S., Hasse, M., Steiner, R. P., Fischer, K., Pöche, J., Ulbricht, Y., Lesche, M., Trimaglio, G., El-Armouche, A., Dahl, A., Mirtschink, P., Guan, K., & Schubert, M. (2025). Comprehensive promotion of iPSC-CM maturation by integrating metabolic medium with nanopatterning and electrostimulation. *Nature Communications*, 16, 2785. DOI 10.1038/s41467-025-58044-6. Full text. | Conduction velocity rises stepwise: B27 12.5, MM 22.3, MM+NP 25.6, MM+NP+ES 27.8 cm/s; spike amplitude and slope change in the same order (values in Supplementary Table 3); E-4031 FPDc response small in B27, concentration-dependent in MM groups. | Qualitative agreement with patch-clamp trends (Vmax, AP amplitude) in separate cells; transcriptome "intermediate between that of human foetal and adult CMs"; FP values not compared with adult data. | No reference values, but MEA parameters separate maturation conditions; source of the maturity labels of Scheurer et al. (2025). |
| 5 | Miyoshi, H., Morimura, K., Hara, R., Hori, R., Watanabe, E., Mochizuki, N., Kamei, A., Yamazaki, R., & Kazusa, K. (2026). Short-term electrical stimulation promotes partial functional and morphological maturation of human-induced pluripotent stem cell-derived cardiomyocytes enabling cardiotoxicity risk mitigation at early-stage drug discovery for cardiac contractility modulation. *Toxicological Sciences*, 209(3), kfag018. DOI 10.1093/toxsci/kfag018. Full text. | 48 h electrical stimulation on MEA raises conduction velocity to 0.4–0.5 m/s (compared with 0.3–0.4 m/s cited for human myocardium); FPDc about 317–343 ms after stimulation. | Two facilities (same trends, different baselines); maturity judged by a positive force–frequency relationship. CSAHi consortium; one author from Axion BioSystems. | No (no MEA criteria proposed). |
| 6 | Lee, S. G., Rhee, J., Seok, J., Kim, J., Kim, M. W., Song, G. E., Park, S., Jeong, K. S., Lee, S., Lee, Y. H., Jeong, Y., Kim, C. Y., & Chung, H. M. (2024). Promotion of maturation of human pluripotent stem cell-derived cardiomyocytes via treatment with the peroxisome proliferator-activated receptor alpha agonist Fenofibrate. *Stem Cells Translational Medicine*, 13(8), 750–762. DOI 10.1093/stcltm/szae029. Full text. | Spike amplitude higher with fenofibrate (1.68 vs 0.36 mV); FPD and beat period unchanged. | No patch clamp; amplitude compared by analogy with AP amplitude; inconsistent units reported (mV vs µV), unchecked. | No (weak). |
| 7 | Shinozawa, T., Imahashi, K., Sawada, H., Furukawa, H., & Takami, K. (2012). Determination of appropriate stage of human-induced pluripotent stem cell-derived cardiomyocytes for drug screening and pharmacological evaluation in vitro. *Journal of Biomolecular Screening*, 17(9), 1192–1203. DOI 10.1177/1087057112449864. Abstract. | MEA responses to ion channel blockers comparable at days 30, 60 and 90, although structure and contraction matured. | Electron microscopy, motion vectors, gene expression. | No; a counter-example in which MEA drug responses did not separate stages. |
| 8 | Otsuji, T. G., Minami, I., Kurose, Y., Yamauchi, K., Tada, M., & Nakatsuji, N. (2010). Progressive maturation in contracting cardiomyocytes derived from human embryonic stem cells: Qualitative effects on electrophysiological responses to drugs. *Stem Cell Research*, 4(3), 201–213. DOI 10.1016/j.scr.2010.01.002. Abstract. | MEA QT tests: resistance to K⁺ channel block rises with maturation. | qRT-PCR, patch clamp. | No (hESC, background). |
| 9 | Fleischer, S., Jahnke, H. G., Fritsche, E., Girard, M., & Robitzki, A. A. (2019). Comprehensive human stem cell differentiation in a 2D and 3D mode to cardiomyocytes for long-term cultivation and multiparametric monitoring on a multimodal microelectrode array setup. *Biosensors and Bioelectronics*, 126, 624–631. DOI 10.1016/j.bios.2018.10.061. Abstract. | States a lack of label-free methods for assessing maturation status; combined impedance and FP over more than 100 days. | Not clear from the abstract. | Probably no. |

Adjacent records noted but not assessed further: Kussauer, David & Lemcke (2019), *Cells* 8:1331, DOI 10.3390/cells8111331 (MEA review; maturation content not checked); Li, Q. et al. (2019), *Nano Letters*, DOI 10.1021/acs.nanolett.9b02512, and Lin, Z. et al. (2025), *Nature Protocols*, DOI 10.1038/s41596-025-01147-7 (the cyborg-organoid method behind Lin et al., 2023); Rebs, S. et al. (2025), bioRxiv 10.1101/2025.10.29.684362 (preprint; maturation judged by patch clamp against adult values, MEA not used for reference values); bioRxiv 10.1101/2020.09.28.317461 (deep-learning translation of iPSC-CM to adult action potentials; AP-based, not FP; authors unverified).

## 5. Assessment and selection

The researcher asked for as few new sources as possible: at most two, or three if one adds clear value to the paper. Each candidate was judged by one test: does leaving it out make a statement in `main.md` wrong, weaker, or open to an obvious reviewer objection?

### 5.1 Lin et al. (2023): selected

The Conclusion says the pieces of an MEA-native maturity classifier "have not yet been combined". Lin et al. (2023) applied machine learning to extracellular field-potential waveforms to trace electrical maturation, which is close to that combination. Without it the sentence is open to a reviewer who knows the paper. Cited with its limits (3D microtissue, embedded mesh electrodes rather than an MEA plate, a trajectory rather than reference values, transcriptomics from separate samples), it changes the claim from "nobody has done this" to "it has been shown with tissue-embedded electrodes, but not on standard MEA plates and not as reference values". That is more accurate and still leaves the gap.

### 5.2 Li et al. (2025): selected

The Scheurer et al. (2025) text dump shows that its maturity labels rest on Li et al. (2025): cells in maturation medium (MM) "were considered to represent a more mature state compared to those in B27 medium, based on previous reports … [11]", and the lower maturation of B27 cultures is attributed to the same reference [11], which is Li et al. (2025). The two papers share authors (Schubert, Steiner, Gamm, Guan). Li et al. (2025) recorded MEA field potentials in the same B27 and MM conditions and found that conduction velocity, spike amplitude and spike slope separate them.

This makes the argument of `main.md` concrete. The labelled culture conditions that Scheurer's video classifier separates already have MEA field-potential data showing differences between them, from the same group. What has not been done is to train a classifier on those FP features. The paper is also within the review's primary period (2022 onward), whereas the only in-scope MEA evidence so far that FP parameters change with maturation is the culture-time drift of Guerrelli et al. (2024).

### 5.3 Zhu et al. (2017): not selected

Zhu et al. (2017) is the earliest explicit proposal found of FP amplitude, dV/dtmax and conduction velocity as maturity indicators. It does not propose reference values, so the current `main.md` claim (no study proposing or validating MEA reference values) remains true without it. Li et al. (2025) shows the same parameters tracking maturation, more recently and with patch-clamp agreement. Zhu et al. (2017) is also pre-2022 background, its text and figure legends disagree on two points, and whether its main data come from hESC- or hiPSC-derived cells was not checked. If a reviewer raises it, it can be added later as background.

### 5.4 Others: not selected

Kumar et al. (2019) and Miyoshi et al. (2026) show FPD or conduction velocity changing with culture time or stimulation, which Guerrelli et al. (2024) and Li et al. (2025) already cover. Lee et al. (2024) is weak (one parameter, unit inconsistencies). Shinozawa et al. (2012) is an interesting counter-example but abstract-only and pre-2022. Otsuji et al. (2010) is hESC and pre-2022. Fleischer et al. (2019) was not read beyond the abstract.

## 6. Conclusions

1. **Answer to the question.** No published work was found that proposes or validates MEA-derived reference values, thresholds or a classifier for hiPSC-CM maturation status. The gap stated in `main.md` holds. What exists is (a) proposals and observations that individual FP parameters (amplitude, dV/dtmax or spike slope, conduction velocity, FPD) change with maturation (Zhu et al., 2017; Kumar et al., 2019; Guerrelli et al., 2024; Li et al., 2025; Miyoshi et al., 2026), and (b) one machine-learning trajectory of electrical maturation from extracellular waveforms recorded with tissue-embedded electrodes (Lin et al., 2023).
2. **Sources to ingest:** Lin et al. (2023) and Li et al. (2025). The researcher will supply the PDFs; for Li et al. (2025) the Supplementary Table 3 values are needed as well.
3. **Changes to propose in `main.md` after ingest** (not made yet; each needs the researcher's approval):
   - The search sentence in the maturation section (and its counterpart in Scope and Literature Search) should name only what was searched and when: PubMed/MEDLINE on 30 October 2026, citation chasing, and web searches including bioRxiv; Scopus only if a Scopus search is run. The restriction "2022–present" can be dropped, since this search had no date limit.
   - The last sentence of the maturation section and the end of the fourth Conclusion gap should acknowledge Lin et al. (2023) and state the gap more precisely: FP-based tracking of maturation has been shown with tissue-embedded electrodes, but no classifier or reference values exist for standard MEA recordings.
   - Li et al. (2025) can support the statement that MEA parameters differ between maturation conditions, and the link to the labels of Scheurer et al. (2025).
4. **Wiki pages to update at ingest:** `wiki/hipsc-cm-maturation.md` (the "What partial evidence already exists" section and the description of the search), `wiki/papers/scheurer-2025-optical-ai.md` (link to Li et al., 2025 as the source of its labels), `wiki/index.md`, `wiki/references.md`, `wiki/log.md`.

## 7. Status

- **Li et al. (2025): ingested 2026-10-30** as `wiki/papers/li-2025-maturation.md` (raw files `raw/li-2025-maturation.pdf`, `-supplementary.pdf`, `-supplementary-description.txt`). The numbers in section 4 were checked against the PDF and Supplementary Tables 2–3 and agree. Supplementary Table 3 gives spike amplitude 3.2 (B27), 10.4 (MM), 10.7 (MM+NP) and 13.6 mV (MM+NP+ES) and spike slope −3.6, −21.2, −23.6 and −29.1 V/s. The link to Scheurer et al. (2025) in section 5.2 was confirmed: Scheurer cites Li et al. (2025) as reference [11] on pp. 5–6, and the two papers' B27 and MM media match (Scheurer also lists biotin; MM starts on day 15–16 in Li and day 21 in Scheurer). Two points found at ingest: the MEA recordings were made after replating on day 42 and 7 days of recovery, with all groups in MM for one hour before recording, and baseline FPDc is not reported per group.
- **Lin et al. (2023): ingested 2026-10-30** as `wiki/papers/lin-2023-nanoelectronics.md` (raw files `raw/lin-2023-nanoelectronics.pdf` and `-supplementary.pdf`; open access, CC BY-NC 4.0). The full text (including the part not read during the search) and the supplement confirm section 4. Points found at ingest that sharpen the gap statement: (a) the "spike duration" is the time between the maximum and minimum dV/dt of the depolarization spike, so all four features describe depolarization and there is no FPD or repolarization feature; (b) one iPSC line, both conditions in StemPro-34 + VEGF; (c) the pseudotime is unsupervised (PHATE + Slingshot on pooled waveforms, default parameters), with no classifier, held-out test or external maturity label on the same samples; (d) the t-tests use channels or 16-channel "groups" (four per well) as observations; (e) the authors argue that classic MEAs keep contact with 3D microtissues only at one surface and lose it as the tissue contracts (table S1).
- **main.md: changed 2026-10-30** with the researcher's approval, as proposed in section 6: the search sentence in Scope and in the maturation section now names PubMed/MEDLINE (30 October 2026, no date limit), citation chasing and web searches including bioRxiv; Li et al. (2025) is cited for MEA parameters that differ between maturation conditions and as the source of the Scheurer et al. (2025) groups; the maturation synthesis and the Conclusion's fourth gap cite Lin et al. (2023) as the closest step and state the remaining gap for standard MEA recordings. The Declarations now mention this search record.
