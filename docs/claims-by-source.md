# Claims in main.md, by source

A checklist for verifying the paper against its sources. Each source has a list of every claim that `main.md` attributes to it, with the section in brackets; tick `[x]` when you have checked a claim against the source. The last section is the register of the author's own inferences, which `main.md` does not mark in the text. Verify each claim in the local file named under the source (all files are in `raw/`; page and figure pointers are given where known). The wiki pages were checked against the source texts on 2026-10-24 and later; figures were viewed only where stated, so numbers, figure readings and nuances of wording still need your own check.

This version was written from scratch on 2026-11-01 from the current `main.md`; ticks set before that date were kept where the claim is unchanged in substance. The history of earlier wordings and corrections is in `wiki/log.md` and git. Run `python -I scripts/claim_quotes.py --write` to list the current `main.md` sentence under each claim (the generated `- >` lines are rewritten on every run; a dry run without `--write` changes nothing).

Sections cited in brackets: Abstract, Highlights, Intro, Motivation, Scope, Timeline (Figure 1), Open pipelines, Table 1, Fiducial, Table 2, FPDc (rate correction), Maturation, Morphology (incl. Figure 2), 3D (section "Three-dimensional cardiomyocyte models"), High-throughput (section "High-throughput and long-term assays"), Outlook (Discussion and future outlook), Limitations, Conclusion, Declarations.

## ✅ Altrocchi et al. (2023)

Local file: `raw/altrocchi-2023-chronic.pdf` (+ supplementary .docx); page `wiki/papers/altrocchi-2023-chronic.md`. Status: checked against the full text 2026-10-24; supplement text read 2026-10-31.

- [x] (1) [Intro] cited, with Blinova et al. (2018) and Park et al. (2025), for MEA recordings of hiPSC-CMs being widely used in cardiac safety pharmacology, drug discovery and disease modelling.
    - > Multielectrode arrays (MEAs) recording extracellular field potentials (FPs) from human induced pluripotent stem cell–derived cardiomyocytes (hiPSC-CMs) are widely used in cardiac safety pharmacology, drug discovery, and disease modelling (Blinova et al., 2018; Altrocchi et al., 2023; Park et al., 2025). — main.md:43
- [x] (2) [Motivation] example of chronic drug testing.
    - > In the studies examined, multielectrode array (MEA) recordings from human induced pluripotent stem cell–derived cardiomyocytes (hiPSC-CMs) are used not only for basic measurements such as beating rate and field potential duration (FPD), but also for mechanistic electrophysiological phenotyping (Maurissen et al., 2024; Park et al., 2025; Park et al., 2026), proarrhythmia risk assessment (Blinova et al., 2018; Pramudito et al., 2026), chronic drug testing (Altrocchi et al., 2023) and recordings repeated over days in culture (Guerrelli et al., 2024). — main.md:46
- [x] (3) [FPDc] the study reports rate-corrected FPD with the Fridericia formula.
    - > By analogy with the clinical QT interval, the Fridericia formula ($FPDc = FPD/RR^{0.33}$, where RR is the interval between beats) is the correction used in the studies examined here that report rate-corrected FPD (Altrocchi et al., 2023; Hwang et al., 2023; Maurissen et al., 2024; Park et al., 2026); Park et al. (2025) also report corrected FPD but do not name the formula. — main.md:121
- [x] (4) [High-throughput] a chronic MEA assay with repeated recordings over four days has been validated for both acute and delayed cardiotoxicity.
    - > A chronic MEA assay with repeated recordings over four days has been validated for both acute and delayed cardiotoxicity (Altrocchi et al., 2023). — main.md:181
    - > Vehicle-treated wells also drifted over the four days: by 96 h, mean beating rate had fallen by 5.8% and mean FPDc had risen by 7.9% despite Fridericia correction (Altrocchi et al., 2023, Table 2). — main.md:181
    - > In the studies examined, single conventional metrics are complemented by multi-parameter feature sets: beat rate, beat-to-beat variability, conduction properties and event-based descriptors (Altrocchi et al., 2023; Matsuda et al., 2025). — main.md:183
- [x] (5) [High-throughput] reference compounds; acute (<2 h) and delayed (≥24 h) electrophysiological and cytotoxic effects; field potentials combined with impedance; a platform the authors describe as medium-throughput.
    - > A chronic MEA assay with repeated recordings over four days has been validated for both acute and delayed cardiotoxicity (Altrocchi et al., 2023). — main.md:181
    - > Vehicle-treated wells also drifted over the four days: by 96 h, mean beating rate had fallen by 5.8% and mean FPDc had risen by 7.9% despite Fridericia correction (Altrocchi et al., 2023, Table 2). — main.md:181
    - > In the studies examined, single conventional metrics are complemented by multi-parameter feature sets: beat rate, beat-to-beat variability, conduction properties and event-based descriptors (Altrocchi et al., 2023; Matsuda et al., 2025). — main.md:183
- [x] (6) [High-throughput] vehicle-treated wells drifted over the four days: by 96 h, mean beating rate −5.8 % and mean FPDc +7.9 % despite Fridericia correction; the authors therefore judged compound effects against tolerance intervals computed from vehicle wells at each time point.
    - > A chronic MEA assay with repeated recordings over four days has been validated for both acute and delayed cardiotoxicity (Altrocchi et al., 2023). — main.md:181
    - > Vehicle-treated wells also drifted over the four days: by 96 h, mean beating rate had fallen by 5.8% and mean FPDc had risen by 7.9% despite Fridericia correction (Altrocchi et al., 2023, Table 2). — main.md:181
    - > In the studies examined, single conventional metrics are complemented by multi-parameter feature sets: beat rate, beat-to-beat variability, conduction properties and event-based descriptors (Altrocchi et al., 2023; Matsuda et al., 2025). — main.md:183
- [x] (7) [High-throughput] one of the two examples (with Matsuda et al., 2025) of multi-parameter feature sets (beat rate, beat-to-beat variability, conduction properties, event-based descriptors).
    - > A chronic MEA assay with repeated recordings over four days has been validated for both acute and delayed cardiotoxicity (Altrocchi et al., 2023). — main.md:181
    - > Vehicle-treated wells also drifted over the four days: by 96 h, mean beating rate had fallen by 5.8% and mean FPDc had risen by 7.9% despite Fridericia correction (Altrocchi et al., 2023, Table 2). — main.md:181
    - > In the studies examined, single conventional metrics are complemented by multi-parameter feature sets: beat rate, beat-to-beat variability, conduction properties and event-based descriptors (Altrocchi et al., 2023; Matsuda et al., 2025). — main.md:183
- [x] (8) [Outlook] impedance read alongside FP, as an example of a second measurement added to the MEA recording.
    - > Several of the studies examined already add a second measurement to the MEA recording: impedance read alongside FP (Altrocchi et al., 2023), intracellular-like signals obtained through the same electrodes by electroporation (Lee et al., 2024), and contraction force from simultaneous atomic force microscopy (Kabanov et al., 2026), whose synchronous validation was done on embryoid bodies only. — main.md:193
    - > In the chronic assay of Altrocchi et al. (2023), a background impedance signal was recorded alongside the FP; the authors describe a drop in impedance when the cells attach less well to the bottom of the well, owing to cell death or changes in the monolayer morphology, and used it as a readout of cytotoxicity to help separate electrophysiological effects from cell death. — main.md:203
- [x] (9) [Outlook] a background impedance signal was recorded alongside the FP; it drops when the cells attach less well to the bottom of the well, owing to cell death or changes in the monolayer morphology; it was used as a readout of cytotoxicity to help separate electrophysiological effects from cell death. (The hypothesis that follows in `main.md` is the author's; see register item 27.)
    - > Several of the studies examined already add a second measurement to the MEA recording: impedance read alongside FP (Altrocchi et al., 2023), intracellular-like signals obtained through the same electrodes by electroporation (Lee et al., 2024), and contraction force from simultaneous atomic force microscopy (Kabanov et al., 2026), whose synchronous validation was done on embryoid bodies only. — main.md:193
    - > In the chronic assay of Altrocchi et al. (2023), a background impedance signal was recorded alongside the FP; the authors describe a drop in impedance when the cells attach less well to the bottom of the well, owing to cell death or changes in the monolayer morphology, and used it as a readout of cytotoxicity to help separate electrophysiological effects from cell death. — main.md:203

Pointers: (3) p. 5 ("Fredericia correction formula, FPDc"). (4) abstract p. 1 ("recordings were conducted for 4 days"), Methods 2.3 (baseline and 2, 24, 48, 72, 96 h), "developed and validated a functional assay" (p. 3). (5) abstract p. 1, Methods p. 3 (Axion Cytoview M768-tMEA-48B); doxorubicin is the only anthracycline; "a medium-throughput, human-based platform" (Discussion). (6) Table 2 (DMSO 0.1 %, N = 81; BR mean −5.8, FPDc mean 7.9 at 96 h; median 6.9, tolerance interval 0.4 to 20.8). Δ% is each well's change from its own baseline before compound or vehicle addition (Methods 2.3; 2.5 "the percent change from the baseline (Δ%)"); FP data are not DMSO-normalised. The paper names no cause for the drift. (7) the study reports beating rate, FP amplitude, FPD/FPDc, impedance and arrhythmic events; Supplementary Tables S7–S9 count events per well (beating below threshold, EAD, flat T-wave-like); beat-to-beat variability and conduction come from Matsuda. (9) Methods, data analysis on Imp (p. 5): "a reduction in the attachment of hiPSC-CMs to the bottom of the well due to cell death or changes in the monolayer morphology, causes a drop in the impedance signal".

## ✅ Blinova et al. (2018)

Local file: `raw/blinova-2018-multisite.pdf`; page `wiki/papers/blinova-2018-multisite.md`. Status: checked (Methods, Results, Discussion; Figures 1, 2, 5–7 viewed) 2026-10-18.

- [x] (1) [Intro] cited, with Altrocchi et al. (2023) and Park et al. (2025), for the cardiac-safety-pharmacology part: hiPSC-CM use for cardiac safety evaluation "continues to increase" (Introduction, p. 2), and the study itself used MEA at nine of ten sites (p. 3; Methods; site 2 was the only optical site). Drug discovery and disease modelling rest on the other two sources. With Park et al. (2025), also cited for FPD and related metrics being integral to CiPA.
    - > Multielectrode arrays (MEAs) recording extracellular field potentials (FPs) from human induced pluripotent stem cell–derived cardiomyocytes (hiPSC-CMs) are widely used in cardiac safety pharmacology, drug discovery, and disease modelling (Blinova et al., 2018; Altrocchi et al., 2023; Park et al., 2025). — main.md:43
    - > The field potential duration (FPD) and related metrics serve as surrogates for repolarization and are integral to initiatives such as the Comprehensive in Vitro Proarrhythmia Assay (CiPA) (Blinova et al., 2018; Park et al., 2025). — main.md:43
- [x] (2) [Motivation] example of proarrhythmia risk assessment.
    - > In the studies examined, multielectrode array (MEA) recordings from human induced pluripotent stem cell–derived cardiomyocytes (hiPSC-CMs) are used not only for basic measurements such as beating rate and field potential duration (FPD), but also for mechanistic electrophysiological phenotyping (Maurissen et al., 2024; Park et al., 2025; Park et al., 2026), proarrhythmia risk assessment (Blinova et al., 2018; Pramudito et al., 2026), chronic drug testing (Altrocchi et al., 2023) and recordings repeated over days in culture (Guerrelli et al., 2024). — main.md:46
- [x] (3) [FPDc] Fridericia correction was already in use before 2022: the blinded multisite CiPA study (ten sites, 28 reference drugs) applied it to all its FPD data.
    - > Fridericia correction was already in use before 2022: the blinded multisite CiPA study (ten sites, 28 reference drugs) applied it to all its FPD data, although its authors noted that the formula had not been thoroughly validated for hiPSC-CMs (Blinova et al., 2018). — main.md:121
    - > Furthermore, a fixed cube-root correction cannot be assumed to hold across the wide range of spontaneous rates of hiPSC-CMs, which are accepted at 20–90 bpm in the multisite CiPA study (Blinova et al., 2018) and 20–80 bpm in a proposed acceptance standard (Clements et al., 2025), so the formula may under- or over-correct at the extremes of this range. — main.md:123
- [x] (4) [FPDc] its authors noted that the Fridericia formula had not been thoroughly validated for hiPSC-CMs.
    - > Fridericia correction was already in use before 2022: the blinded multisite CiPA study (ten sites, 28 reference drugs) applied it to all its FPD data, although its authors noted that the formula had not been thoroughly validated for hiPSC-CMs (Blinova et al., 2018). — main.md:121
    - > Furthermore, a fixed cube-root correction cannot be assumed to hold across the wide range of spontaneous rates of hiPSC-CMs, which are accepted at 20–90 bpm in the multisite CiPA study (Blinova et al., 2018) and 20–80 bpm in a proposed acceptance standard (Clements et al., 2025), so the formula may under- or over-correct at the extremes of this range. — main.md:123
- [x] (5) [FPDc] spontaneous rates of hiPSC-CMs were accepted at 20–90 bpm (baseline inclusion criterion).
    - > Fridericia correction was already in use before 2022: the blinded multisite CiPA study (ten sites, 28 reference drugs) applied it to all its FPD data, although its authors noted that the formula had not been thoroughly validated for hiPSC-CMs (Blinova et al., 2018). — main.md:121
    - > Furthermore, a fixed cube-root correction cannot be assumed to hold across the wide range of spontaneous rates of hiPSC-CMs, which are accepted at 20–90 bpm in the multisite CiPA study (Blinova et al., 2018) and 20–80 bpm in a proposed acceptance standard (Clements et al., 2025), so the formula may under- or over-correct at the extremes of this range. — main.md:123
- [x] (6) [Limitations] cited only as pre-2022 background, not as one of the post-2022 developments.
    - > - (vi) A few works from before 2022, such as Blinova et al. (2018), Hayakawa et al. (2014) and Ryynänen et al. (2018), are cited only as background for conventions, datasets and earlier multimodal work. — main.md:220
- [x] (7) [Conclusion] quantitative criteria exist for well acceptance (amplitude, rate, beat period).
    - > In contrast, quantitative criteria exist for well acceptance, such as amplitude, rate and beat period (Blinova et al., 2018; Clements et al., 2025). — main.md:232

Pointers: Fridericia statement and the 20–90 bpm criterion in the Data Analysis section of the Experimental Procedures; ten sites and 28 drugs in the Summary.

## ✅ Botti et al. (2026)

Local file: `raw/botti-2026-insilico.pdf` (+ peer review history); page `wiki/papers/botti-2026-insilico.md`. Status: checked against the Europe PMC full text 2026-10-18; compare with the PDF. Reference year 2026 (issue 604(19), October 2026; online 11 May 2025).

- [x] (1) [Timeline] "In silico model of hiPSC-CM tissue coupled to MEA electrodes", listed under 2026 (reworded 2026-11-04 from "In silico MEA–tissue biophysical model"; Discussion: the framework "incorporates a model of electrodes that couples with the bidomain framework").
    - > 2026 : In silico model of hiPSC-CM tissue coupled to MEA electrodes (Botti et al.) — main.md:77
- [x] (2) [Outlook] forward modelling already includes the electrode: a bidomain model with a resistor–capacitor electrode model simulates FPs from phenotype-specific cell models.
    - > Forward modelling already includes the electrode: a bidomain model with a resistor–capacitor electrode model simulates FPs from phenotype-specific cell models (Botti et al., 2026). — main.md:199
    - > The forward model of Botti et al. (2026) is the closest existing component among the studies examined, but it was not fitted to new measurements. — main.md:207
- [x] (3) [Outlook] it is the closest existing component of a digital twin of the recording among the studies examined, but it was not fitted to new measurements.
    - > Forward modelling already includes the electrode: a bidomain model with a resistor–capacitor electrode model simulates FPs from phenotype-specific cell models (Botti et al., 2026). — main.md:199
    - > The forward model of Botti et al. (2026) is the closest existing component among the studies examined, but it was not fitted to new measurements. — main.md:207
- [x] (4) [Limitations] example of simulation-based evidence.
    - > Most methodological statements rest on one or two studies, and some rest on rat cells (Ernault et al., 2024), fetal mouse cells (Hu et al., 2026), simulations (Hwang et al., 2023; Botti et al., 2026), tissue-embedded electrodes (Lin et al., 2023) or modalities other than field potentials (Fetterman et al., 2024; Scheurer et al., 2025). — main.md:216
- [x] (5) [Intro] reliable MEA recordings are essential for using hiPSC-CMs in drug development (added 2026-11-04). Quote supplied by the researcher: "To enhance the utility of hiPSC-CMs in drug development, reliable MEA recordings are essential." Locate its page in the PDF.
    - > Reliable MEA recordings are considered essential for using hiPSC-CMs in drug development (Botti et al., 2026), and that reliability depends not only on the recording but also on consistent, physiologically meaningful analysis of FP waveforms. — main.md:43

## ✅ Clements et al. (2025)

Local file: `raw/clements-2025-aims-poster.pdf` (git-ignored); page `wiki/papers/clements-2025-aims-poster.md`. Status: poster text read in full 2026-10-18 (layout not viewed); the standard's web page https://www.axionbiosystems.com/axion-ipsc-model-standards-aims/aims-cm01 read through a web-fetch tool 2026-10-31.

- [x] (1) [FPDc] a recent proposed acceptance standard for hiPSC-ventricular-CM MEA assays builds the Fridericia correction into quality control by requiring an FPDc of 200–700 ms.
    - > A recent proposed acceptance standard for hiPSC-ventricular-CM MEA assays likewise builds the Fridericia correction into quality control, by requiring a rate-corrected FPD (FPDc) of 200–700 ms (Clements et al., 2025). — main.md:121
    - > Furthermore, a fixed cube-root correction cannot be assumed to hold across the wide range of spontaneous rates of hiPSC-CMs, which are accepted at 20–90 bpm in the multisite CiPA study (Blinova et al., 2018) and 20–80 bpm in a proposed acceptance standard (Clements et al., 2025), so the formula may under- or over-correct at the extremes of this range. — main.md:123
    - > Matsuda et al. (2025), however, recorded spontaneous beating only and name the absence of pacing as a limitation, and the proposed acceptance standard is defined for spontaneously beating cells: more mature cells can beat with periods longer than its 3000 ms upper limit, which makes recordings impractically long, so pacing would probably be needed, a paced assay being left to a possible future standard (Clements et al., 2025). — main.md:123
- [x] (2) [FPDc] spontaneous rates are accepted at 20–80 bpm in that proposal.
    - > A recent proposed acceptance standard for hiPSC-ventricular-CM MEA assays likewise builds the Fridericia correction into quality control, by requiring a rate-corrected FPD (FPDc) of 200–700 ms (Clements et al., 2025). — main.md:121
    - > Furthermore, a fixed cube-root correction cannot be assumed to hold across the wide range of spontaneous rates of hiPSC-CMs, which are accepted at 20–90 bpm in the multisite CiPA study (Blinova et al., 2018) and 20–80 bpm in a proposed acceptance standard (Clements et al., 2025), so the formula may under- or over-correct at the extremes of this range. — main.md:123
    - > Matsuda et al. (2025), however, recorded spontaneous beating only and name the absence of pacing as a limitation, and the proposed acceptance standard is defined for spontaneously beating cells: more mature cells can beat with periods longer than its 3000 ms upper limit, which makes recordings impractically long, so pacing would probably be needed, a paced assay being left to a possible future standard (Clements et al., 2025). — main.md:123
- [x] (3) [FPDc] the standard is defined for spontaneously beating cells.
    - > A recent proposed acceptance standard for hiPSC-ventricular-CM MEA assays likewise builds the Fridericia correction into quality control, by requiring a rate-corrected FPD (FPDc) of 200–700 ms (Clements et al., 2025). — main.md:121
    - > Furthermore, a fixed cube-root correction cannot be assumed to hold across the wide range of spontaneous rates of hiPSC-CMs, which are accepted at 20–90 bpm in the multisite CiPA study (Blinova et al., 2018) and 20–80 bpm in a proposed acceptance standard (Clements et al., 2025), so the formula may under- or over-correct at the extremes of this range. — main.md:123
    - > Matsuda et al. (2025), however, recorded spontaneous beating only and name the absence of pacing as a limitation, and the proposed acceptance standard is defined for spontaneously beating cells: more mature cells can beat with periods longer than its 3000 ms upper limit, which makes recordings impractically long, so pacing would probably be needed, a paced assay being left to a possible future standard (Clements et al., 2025). — main.md:123
- [x] (4) [FPDc] more mature cells can beat with periods longer than the 3000 ms upper limit of its 750–3000 ms window; such cells are impractical because of the long recordings needed, so pacing would probably be required, and a paced assay is left to a possible future standard (reworded 2026-11-04: the upper limit and the practical reason made explicit).
    - > A recent proposed acceptance standard for hiPSC-ventricular-CM MEA assays likewise builds the Fridericia correction into quality control, by requiring a rate-corrected FPD (FPDc) of 200–700 ms (Clements et al., 2025). — main.md:121
    - > Furthermore, a fixed cube-root correction cannot be assumed to hold across the wide range of spontaneous rates of hiPSC-CMs, which are accepted at 20–90 bpm in the multisite CiPA study (Blinova et al., 2018) and 20–80 bpm in a proposed acceptance standard (Clements et al., 2025), so the formula may under- or over-correct at the extremes of this range. — main.md:123
    - > Matsuda et al. (2025), however, recorded spontaneous beating only and name the absence of pacing as a limitation, and the proposed acceptance standard is defined for spontaneously beating cells: more mature cells can beat with periods longer than its 3000 ms upper limit, which makes recordings impractically long, so pacing would probably be needed, a paced assay being left to a possible future standard (Clements et al., 2025). — main.md:123
- [x] (5) [Maturation] an industry-led proposal, Axion BioSystems' AIMS \#CM01, presented as a poster at ISSCR 2025, defining minimum acceptance criteria for MEA wells of spontaneously beating hiPSC-ventricular cardiomyocytes (spike amplitude, synchronised beating, beat period and FPDc).
    - > An industry-led proposal also exists, the Axion iPSC Model Standards \#CM01 of Axion BioSystems (Clements et al., 2025), presented as a poster at the 2025 meeting of the International Society for Stem Cell Research. — main.md:134
    - > Whether a culture meets the amplitude criterion also depends on when it is recorded: in Guerrelli et al. (2024), the mean spike amplitude of spontaneously beating cells of two commercial lines was below 0.5 mV two days post-defrost and had risen to several millivolts by day 14, whereas the proposal leaves culture protocols to the cell vendors (Clements et al., 2025). — main.md:134
- [x] (6) [Maturation] the criteria target assay quality control, not maturation staging, and the proposal has not been published as a peer-reviewed methods paper.
    - > An industry-led proposal also exists, the Axion iPSC Model Standards \#CM01 of Axion BioSystems (Clements et al., 2025), presented as a poster at the 2025 meeting of the International Society for Stem Cell Research. — main.md:134
    - > Whether a culture meets the amplitude criterion also depends on when it is recorded: in Guerrelli et al. (2024), the mean spike amplitude of spontaneously beating cells of two commercial lines was below 0.5 mV two days post-defrost and had risen to several millivolts by day 14, whereas the proposal leaves culture protocols to the cell vendors (Clements et al., 2025). — main.md:134
- [x] (7) [Conclusion] quantitative criteria exist for well acceptance (amplitude, rate, beat period).
    - > In contrast, quantitative criteria exist for well acceptance, such as amplitude, rate and beat period (Blinova et al., 2018; Clements et al., 2025). — main.md:232

- [x] (8) [Maturation] the proposal leaves culture protocols to the cell vendors ("Participating vendor protocols must specify key details"); it states no recording day (added 2026-11-06).
    - > An industry-led proposal also exists, the Axion iPSC Model Standards \#CM01 of Axion BioSystems (Clements et al., 2025), presented as a poster at the 2025 meeting of the International Society for Stem Cell Research. — main.md:134
    - > Whether a culture meets the amplitude criterion also depends on when it is recorded: in Guerrelli et al. (2024), the mean spike amplitude of spontaneously beating cells of two commercial lines was below 0.5 mV two days post-defrost and had risen to several millivolts by day 14, whereas the proposal leaves culture protocols to the cell vendors (Clements et al., 2025). — main.md:134
Pointers: poster, box "AIMS \#CM01: Proposed standards" (spike amplitude ≥ 0.5 mV on ≥ 50 % of electrodes, synchronised beating, "Spontaneous beat period of 750-3000 ms (i.e. 20-80 beats per minute, BPM)", FPDc 200–700 ms with Fridericia); "Presented at ISSCR 2025, Hong Kong, June 11, 2025". (4) web page, criterion 3, "Additional Information": maturation "can result in spontaneous beat periods greater than 3000 ms"; such cells are impractical because of long recordings; external pacing "will probably be required to make these cells more practical to work with"; "A paced hiPSC-CM assay could be the subject of a future AIMS but is beyond the scope of this AIMS" (quoted by the tool as verbatim; check on the page). (8) box "Important considerations": "Reproducibility and quality is dependent on culture protocols. Participating vendor protocols must specify key details (see AIMS website)."

## ✅ Correia et al. (2024)

Local files: `raw/correia-2024-acc2.pdf` (+ supplementary, not read); page `wiki/papers/correia-2024-acc2.md`. Status: checked against the full text and Figure 7F 2026-10-24.

- [x] (1) [Timeline] "Maturation medium improves in vitro-to-in vivo translatability" (2024) (reworded 2026-11-04: detail not needed for the argument removed).
    - > : Maturation medium improves in vitro-to-in vivo translatability (Correia et al.) — main.md:72
- [x] (2) [Maturation] hiPSC-CMs retain a fetal-like phenotype (cited with Scheurer et al., 2025).
    - > Maturation adds a further complication for comparisons between studies, distinct from but interacting with rate correction. hiPSC-CMs are electrophysiologically immature compared with adult cardiomyocytes and retain a fetal-like phenotype (Correia et al., 2024; Scheurer et al., 2025). — main.md:128
    - > Correia et al. (2024) developed a maturation medium that improved electrophysiological, metabolic and structural maturation, and for one drug target, in vitro results correlated with in vivo results only in matured cells. — main.md:136
    - > Taken together, some ingredients of an MEA-based maturity classifier have been reported separately: an interpretable machine-learning method validated on video features (Scheurer et al., 2025), MEA parameters that differ between the same maturation conditions (Li et al., 2025, whose B27 and maturation-medium groups Scheurer et al. follow), a reported link between FPD and contraction (Hayakawa et al., 2014), and evidence that maturation status matters for translation (Correia et al., 2024). — main.md:140
- [x] (3) [Maturation] a maturation medium that improved electrophysiological, metabolic and structural maturation (reworded 2026-11-04: detail not needed for the argument removed).
    - > Maturation adds a further complication for comparisons between studies, distinct from but interacting with rate correction. hiPSC-CMs are electrophysiologically immature compared with adult cardiomyocytes and retain a fetal-like phenotype (Correia et al., 2024; Scheurer et al., 2025). — main.md:128
    - > Correia et al. (2024) developed a maturation medium that improved electrophysiological, metabolic and structural maturation, and for one drug target, in vitro results correlated with in vivo results only in matured cells. — main.md:136
    - > Taken together, some ingredients of an MEA-based maturity classifier have been reported separately: an interpretable machine-learning method validated on video features (Scheurer et al., 2025), MEA parameters that differ between the same maturation conditions (Li et al., 2025, whose B27 and maturation-medium groups Scheurer et al. follow), a reported link between FPD and contraction (Hayakawa et al., 2014), and evidence that maturation status matters for translation (Correia et al., 2024). — main.md:140
- [x] (4) [Maturation] for one drug target, in vitro results correlated with in vivo results only in matured cells (reworded 2026-11-04: detail not needed for the argument removed); the earlier claims on patch-clamp details, BCKDK IC50 values (r = 0.85) and the absent response in standard medium were dropped with the text.
    - > Maturation adds a further complication for comparisons between studies, distinct from but interacting with rate correction. hiPSC-CMs are electrophysiologically immature compared with adult cardiomyocytes and retain a fetal-like phenotype (Correia et al., 2024; Scheurer et al., 2025). — main.md:128
    - > Correia et al. (2024) developed a maturation medium that improved electrophysiological, metabolic and structural maturation, and for one drug target, in vitro results correlated with in vivo results only in matured cells. — main.md:136
    - > Taken together, some ingredients of an MEA-based maturity classifier have been reported separately: an interpretable machine-learning method validated on video features (Scheurer et al., 2025), MEA parameters that differ between the same maturation conditions (Li et al., 2025, whose B27 and maturation-medium groups Scheurer et al. follow), a reported link between FPD and contraction (Hayakawa et al., 2014), and evidence that maturation status matters for translation (Correia et al., 2024). — main.md:140
- [x] (5) [Maturation, Conclusion] evidence that maturation status matters for translation; for one drug target, in vitro results correlated with in vivo results only in matured cells.
    - > Maturation adds a further complication for comparisons between studies, distinct from but interacting with rate correction. hiPSC-CMs are electrophysiologically immature compared with adult cardiomyocytes and retain a fetal-like phenotype (Correia et al., 2024; Scheurer et al., 2025). — main.md:128
    - > Correia et al. (2024) developed a maturation medium that improved electrophysiological, metabolic and structural maturation, and for one drug target, in vitro results correlated with in vivo results only in matured cells. — main.md:136
    - > Taken together, some ingredients of an MEA-based maturity classifier have been reported separately: an interpretable machine-learning method validated on video features (Scheurer et al., 2025), MEA parameters that differ between the same maturation conditions (Li et al., 2025, whose B27 and maturation-medium groups Scheurer et al. follow), a reported link between FPD and contraction (Hayakawa et al., 2014), and evidence that maturation status matters for translation (Correia et al., 2024). — main.md:140
    - > Even a partial reference would improve comparability between studies and support the translation of MEA findings to adult myocardium; for one drug target, in vitro results correlated with in vivo results only in matured cells (Correia et al., 2024). — main.md:234

Pointers: (3) p. 3 (medium composition), p. 14 (MDP −79.2 vs −74.3 mV; dV/dt max 68.6 vs 23.4 V/s), p. 16 (IK1 −27.3 vs −4.1 pA/pF). (4) Figure 7F, p. 22 (r 0.85, R² 0.72, p < 0.0001, 21 BCKDK inhibitors), p. 23 ("not possible to obtain using standard medium"; BCAT inhibitors responded in both media).

## ✅ Dunham et al. (2022)

Local file: `raw/dunham-2022-cardiopyemea.pdf`; page `wiki/papers/dunham-2022-cardiopyemea.md`. Status: checked against the abstract and the FPD section 2026-10-24.

- [x] (1) [Timeline] Cardio PyMEA, an open-source Python pipeline, 2022.
    - > 2022 : Cardio PyMEA — open-source Python pipeline (Dunham et al.) — main.md:63
- [x] (2) [Open pipelines] open analysis tools existed before 2022 (cited with Lee et al., 2024; the names MultiElec and CardioMDA come from Lee).
    - > Such tools are not new, as MultiElec and CardioMDA, for example, existed before 2022 (Dunham et al., 2022; Lee et al., 2024), but several new ones have appeared since 2022, some of them built for new kinds of data such as high-density arrays (Lee et al., 2024) and cardiac organoids (Weiser-Bitoun et al., 2026). — main.md:85
    - > This open-source Python-based application enables explicit analysis of cardiomyocyte MEA recordings, including beat detection, pacemaker origin estimation and conduction velocity (Dunham et al., 2022). — main.md:87
- [x] (3) [Open pipelines] Cardio PyMEA, introduced in 2022, is an open-source Python application for beat detection, pacemaker origin estimation and conduction velocity, among other features (reworded 2026-11-06: detail and abbreviations not needed for the argument removed); an early example of open pipelines.
    - > Such tools are not new, as MultiElec and CardioMDA, for example, existed before 2022 (Dunham et al., 2022; Lee et al., 2024), but several new ones have appeared since 2022, some of them built for new kinds of data such as high-density arrays (Lee et al., 2024) and cardiac organoids (Weiser-Bitoun et al., 2026). — main.md:85
    - > This open-source Python-based application enables explicit analysis of cardiomyocyte MEA recordings, including beat detection, pacemaker origin estimation and conduction velocity (Dunham et al., 2022). — main.md:87
- [x] (4) [Table 1] Python; FPD end at a T-wave endpoint located with a trapezoid-area algorithm; beat detection, local activation time, conduction velocity, pacemaker origin estimation (reworded 2026-11-06: detail and abbreviations not needed for the argument removed).
    - > | Cardio PyMEA (Dunham et al., 2022) | 2022 | Python | T-wave endpoint (trapezoid-area algorithm) | Beat detection, local activation time, conduction velocity, pacemaker origin estimation | — main.md:95
- [x] (5) [Fiducial, Table 2] FPD runs from the R peak to a T-wave endpoint located with a trapezoid-area algorithm, not validated against the AP in the paper.
    - > - **Cardio PyMEA**: from the R peak to a T-wave endpoint located with a trapezoid-area algorithm (Dunham et al., 2022) — main.md:106
    - > | T-wave endpoint (trapezoid area) | R peak | T-wave end located with a trapezoid-area algorithm | Not validated against the AP in the source | Dunham et al., 2022 | — main.md:118
- [x] (6) [Morphology] Figure 2 shows the trapezoid-area T-wave endpoint as a third FPD end convention ("End of the T wave").
    - > J -->|T-wave endpoint trapezoid area| P[End of the T wave Dunham et al., 2022] — main.md:164
    - > Cardio PyMEA detects beats at the most prominent peak of the field potential and places local activation at the steepest negative deflection after it (Dunham et al., 2022), so its analysis presupposes the polarity of its recordings, which the paper does not state. — main.md:173

- [x] (7) [Morphology] beats are detected at the most prominent peak of the field potential and local activation is placed at the steepest negative deflection after it; the paper does not state the polarity convention of the recording system (added 2026-11-05; that the analysis therefore presupposes the polarity is our inference, register item 28; see wiki/fp-polarity.md).
    - > J -->|T-wave endpoint trapezoid area| P[End of the T wave Dunham et al., 2022] — main.md:164
    - > Cardio PyMEA detects beats at the most prominent peak of the field potential and places local activation at the steepest negative deflection after it (Dunham et al., 2022), so its analysis presupposes the polarity of its recordings, which the paper does not state. — main.md:173

Pointers: (2) p. 2 ("open-access tools offering enhanced functionality beyond ... proprietary software"). (3) abstract p. 1 (free, modifiable, open source under GPL; Python 3, PyQt5 GUI). (5) section "Field potential duration calculation", p. 10 (R wave to the T-wave endpoint; trapezoid with a mobile point, maximum area gives the endpoint; method of Vázquez-Seisdedos et al.). (7) Methods, beat detection ("identified in MEAs as the most prominent peak of the field potential", SciPy findpeaks); LAT calculation ("maximal negative intrinsicoid deflection"), Figure 5B; no polarity convention found in the text.

## ✅ Ernault et al. (2024)

Local file: `raw/ernault-2024-interpretation.pdf`; page `wiki/papers/ernault-2024-interpretation.md`. Status: checked against the abstract and Results 2026-10-24.

- [x] (1) [Timeline] "T-wave peak = APD90 for biphasic T-waves, in NRVM".
    - > : T-wave peak = APD90 for biphasic T-waves, in NRVM (Ernault et al.) — main.md:68
- [x] (2) [Fiducial, Table 2] with simultaneous MEA and sharp-microelectrode recordings from neonatal rat ventricular myocyte (NRVM) monolayers, the peak time of the T wave correlates strongly with APD90, but only when the T wave is biphasic, a morphology reported in only a minority of monolayers.
    - > Ernault et al. (2024) demonstrated using simultaneous MEA and sharp-microelectrode recordings from neonatal rat ventricular myocyte (NRVM) monolayers that the peak time of the T wave in FPs correlates strongly with the action potential duration at 90% repolarization (APD90), but only when the T wave displays a biphasic pattern — a morphology the authors report in only a minority of recorded monolayers. — main.md:110
    - > The baseline-return convention was not compared with the action potential in that study, and in monolayers with only a positive T wave the T wave ended before the end of the action potential (Ernault et al., 2024); the two definitions may therefore measure different quantities rather than one being universally more correct. — main.md:110
    - > | R-to-T-peak | R peak (Hayakawa et al., 2014: initial negative peak) | T-wave peak | T-wave peak coincided with APD90 only for biphasic T waves (a minority morphology; NRVM, not hiPSC-CM; Ernault et al., 2024); in hiPSC-CMs, R-to-T-peak FPD correlated only minimally with APD50 and APD90 (Lee et al., 2024); the peak of the positive deflection appeared to match the upstroke of relaxation (Hayakawa et al., 2014) | Hayakawa et al., 2014; Lee et al., 2024; Weiser-Bitoun et al., 2026; described as a common convention and criticised in Mäki, 2023 | — main.md:116
- [x] (3) [Fiducial] the baseline-return convention was not compared with the action potential in that study, and in monolayers with only a positive T wave the T wave ended before the end of the action potential.
    - > Ernault et al. (2024) demonstrated using simultaneous MEA and sharp-microelectrode recordings from neonatal rat ventricular myocyte (NRVM) monolayers that the peak time of the T wave in FPs correlates strongly with the action potential duration at 90% repolarization (APD90), but only when the T wave displays a biphasic pattern — a morphology the authors report in only a minority of recorded monolayers. — main.md:110
    - > The baseline-return convention was not compared with the action potential in that study, and in monolayers with only a positive T wave the T wave ended before the end of the action potential (Ernault et al., 2024); the two definitions may therefore measure different quantities rather than one being universally more correct. — main.md:110
- [x] (4) [Morphology] with Weiser-Bitoun et al. (2026), one of two studies showing awareness of waveform heterogeneity (T-wave morphology varies between preparations; a single canonical FP shape cannot be assumed); Figure 2 labels the T-wave-peak branch "APD90 surrogate if biphasic T wave" (condition added 2026-11-05; the label previously omitted it).
    - > J -->|T-wave peak| K[APD90 surrogate if biphasic T wave Ernault et al., 2024] — main.md:162
    - > The studies examined do not adopt identical rules, but two of them show an awareness of waveform heterogeneity: they report morphology-dependent analysis branches or document that T-wave morphology varies between preparations, which indicates that a single canonical FP shape cannot be assumed (Ernault et al., 2024; Weiser-Bitoun et al., 2026). — main.md:171
- [x] (5) [Outlook] the T-wave peak tracks APD90 only when the T wave is biphasic; and a LEAP obtained by electroporation is not a recording of the local action potential but is generated by current from neighbouring cardiomyocytes, a limitation of paired electroporation signals as training data (reworded 2026-11-03; was cited for "the FP also depends on current from neighbouring cells", which the paper says of the LEAP, not of the FP; that general point is now cited to Karami (3)). Quotes supplied by the researcher: "a LEAP is not a recording of the local action potential but is generated by intracellular current provided by neighboring cardiomyocytes"; "the current causing the LEAP signal was indeed coming from neighboring myocytes".
    - > The T-wave peak tracks APD90 only when the T wave is biphasic (Ernault et al., 2024), and R-to-T-peak FPD correlated only minimally with APD50 and APD90 from intracellular-like signals on the same electrodes (Lee et al., 2024). — main.md:199
    - > The paired signals proposed above as training data share part of this limitation: a local extracellular action potential obtained by electroporation is not a recording of the local AP but is generated by current from neighbouring cardiomyocytes (Ernault et al., 2024). — main.md:205
- [x] (6) [Limitations] example of evidence in rat cells.
    - > Most methodological statements rest on one or two studies, and some rest on rat cells (Ernault et al., 2024), fetal mouse cells (Hu et al., 2026), simulations (Hwang et al., 2023; Botti et al., 2026), tissue-embedded electrodes (Lin et al., 2023) or modalities other than field potentials (Fetterman et al., 2024; Scheurer et al., 2025). — main.md:216
- [x] (7) [Conclusion] interpretation restricted to biphasic T waves is an example of case-by-case morphology handling.
    - > In the studies examined, morphology handling is described case by case: analysis of inverted signals, exclusion of electrodes, or interpretation restricted to biphasic T waves (Mäki, 2023; Ernault et al., 2024; Weiser-Bitoun et al., 2026). — main.md:232

Pointers: (2) abstract p. 1 and p. 4 ("only in the monolayers exhibiting field potentials with a biphasic T wave ... only the case in the minority of the monolayers"). (3) Results on Fig. 3A: "Often the field potentials showed only a positive T wave that ended before the end of the action potential"; the paper does not test the baseline-return convention. (5) the dependence on neighbouring cells is the paper's point on the LEAP; the "not sufficient" step is ours.

## ✅ Fetterman et al. (2024)

Local file: `raw/fetterman-2024-maturation.pdf`; page `wiki/papers/fetterman-2024-maturation.md`. Status: checked against the full text 2026-10-24.

- [x] (1) [Timeline] "Functional/metabolic/transcriptional maturation shown largely independent" ("largely" added 2026-11-05).
    - > : Functional/metabolic/transcriptional maturation shown largely independent (Fetterman et al.) — main.md:71
- [x] (2) [Maturation] when the components of a maturation medium were added or removed one at a time, functional (electrophysiology and excitation–contraction coupling), metabolic and transcriptional maturation responded largely independently (shortened 2026-11-05: the method sentence and the fatty-acid example were merged into this one claim; former (3) dropped, (4) and (5) renumbered).
    - > A recent high-throughput study outside the MEA literature limits what such a reference value could measure: when the components of a maturation medium were added or removed one at a time, functional (electrophysiology and excitation–contraction coupling), metabolic and transcriptional maturation responded largely independently (Fetterman et al., 2024). — main.md:132
- [x] (3) [Conclusion] because maturation is induced largely independently, a benchmark could only cover the electrophysiological axis.
    - > Because functional, metabolic and transcriptional maturation are induced largely independently (Fetterman et al., 2024), such a benchmark could only cover the electrophysiological axis. — main.md:234
- [x] (4) [Limitations] example of a modality other than field potentials (was "non-MEA modalities" until 2026-11-05; the paper calls its impedance recordings MEA-based, but no FPs were recorded: Ca²⁺ imaging, impedance, patch clamp).
    - > Most methodological statements rest on one or two studies, and some rest on rat cells (Ernault et al., 2024), fetal mouse cells (Hu et al., 2026), simulations (Hwang et al., 2023; Botti et al., 2026), tissue-embedded electrodes (Lin et al., 2023) or modalities other than field potentials (Fetterman et al., 2024; Scheurer et al., 2025). — main.md:216

Pointers: (1)(2) summary p. 2 ("induction of these attributes is largely independent"); highlights p. 1 ("Functional and metabolic maturation are largely independent"). (2) single-addition experiments in MMb and single-subtraction experiments in MMc (p. 5, Figure 2); p. 7 ("Fatty acids contribute to metabolism but not viability, Ca²⁺ dynamics, impedance, or Nav current"); nine formulations in the RNA-seq comparison (Figure 6, p. 10).

## ✅ Guerrelli et al. (2024)

Local file: `raw/guerrelli-2024-hipscm.pdf`; page `wiki/papers/guerrelli-2024-hipscm.md`. Status: checked against the abstract, p. 10 and the paced results 2026-10-24 and 2026-10-30.

- [x] (1) [Timeline] "Temporal and spatial confounders quantified".
    - > : Temporal and spatial confounders quantified (Guerrelli et al.) — main.md:69
- [x] (2) [Motivation] example of recordings repeated over days in culture.
    - > In the studies examined, multielectrode array (MEA) recordings from human induced pluripotent stem cell–derived cardiomyocytes (hiPSC-CMs) are used not only for basic measurements such as beating rate and field potential duration (FPD), but also for mechanistic electrophysiological phenotyping (Maurissen et al., 2024; Park et al., 2025; Park et al., 2026), proarrhythmia risk assessment (Blinova et al., 2018; Pramudito et al., 2026), chronic drug testing (Altrocchi et al., 2023) and recordings repeated over days in culture (Guerrelli et al., 2024). — main.md:46
- [x] (3) [FPDc] in iCell², beating rate and FPD kept changing for 7–12 min after the plate was placed in the MEA system (rate 2–12 min, FPD 2–7 min), longer than the manufacturer's 10 min; the authors recommend 15–20 min before baseline recordings; Cor.4U showed no such change (reworded 2026-11-06: manufacturer's 10 min and the line dependence added).
    - > In one commercial line, beating rate and FPD kept changing for 7–12 min after the plate was placed in the MEA system, longer than the 10 min equilibration recommended by the manufacturer, and the authors recommend 15–20 min before baseline recordings; a second line showed no such change (Guerrelli et al., 2024; see also the section on high-throughput and long-term assays). — main.md:123
    - > Pacing at a fixed rate removes the rate dependence, and Guerrelli et al. (2024) recorded under external pacing for this reason, both across days in culture (1.5 Hz) and in drug tests, where the rate was chosen for each drug because the drugs themselves changed the spontaneous rate. — main.md:123
- [x] (4) [FPDc] the authors recorded under external pacing because the metrics are rate dependent: across days in culture at 1.5 Hz (alongside spontaneous recordings), and in drug tests at a rate chosen per drug (1.5 Hz for E-4031, 3 Hz for nifedipine and isoproterenol) because the drugs changed the spontaneous rate (reworded 2026-11-06: drug tests added).
    - > In one commercial line, beating rate and FPD kept changing for 7–12 min after the plate was placed in the MEA system, longer than the 10 min equilibration recommended by the manufacturer, and the authors recommend 15–20 min before baseline recordings; a second line showed no such change (Guerrelli et al., 2024; see also the section on high-throughput and long-term assays). — main.md:123
    - > Pacing at a fixed rate removes the rate dependence, and Guerrelli et al. (2024) recorded under external pacing for this reason, both across days in culture (1.5 Hz) and in drug tests, where the rate was chosen for each drug because the drugs themselves changed the spontaneous rate. — main.md:123
- [x] (5) [Maturation] over two weeks in culture the FPD of spontaneously beating cells lengthened markedly and the beating rate declined, together with a rise in KCNJ2 expression; the authors link these changes to continued maturation (reworded 2026-11-06, numbers dropped from the text: FPD about +257 ms over days 2–14, +54.8 % days 3–14; KCNJ2 27.5-fold over 30 days).
    - > Guerrelli et al. (2024) show this kind of drift in an MEA setting: over two weeks in culture, the FPD of spontaneously beating cells lengthened markedly and the beating rate declined, together with a rise in *KCNJ2* expression, changes the authors link to continued maturation. — main.md:130
    - > Whether a culture meets the amplitude criterion also depends on when it is recorded: in Guerrelli et al. (2024), the mean spike amplitude of spontaneously beating cells of two commercial lines was below 0.5 mV two days post-defrost and had risen to several millivolts by day 14, whereas the proposal leaves culture protocols to the cell vendors (Clements et al., 2025). — main.md:134
- [x] (6) [Maturation] FPD lengthened significantly also when the cells were paced at a fixed rate (1.5 Hz; 275.5 ms on day 3 to 336.0 ms on day 14, +21.9 %, P < 0.0001; numbers dropped from the text 2026-11-06). (The conclusion drawn from it is in register item 17.)
    - > Guerrelli et al. (2024) show this kind of drift in an MEA setting: over two weeks in culture, the FPD of spontaneously beating cells lengthened markedly and the beating rate declined, together with a rise in *KCNJ2* expression, changes the authors link to continued maturation. — main.md:130
    - > Whether a culture meets the amplitude criterion also depends on when it is recorded: in Guerrelli et al. (2024), the mean spike amplitude of spontaneously beating cells of two commercial lines was below 0.5 mV two days post-defrost and had risen to several millivolts by day 14, whereas the proposal leaves culture protocols to the cell vendors (Clements et al., 2025). — main.md:134
- [x] (7) [High-throughput] over a 20-minute equilibration window, beating rate increased and FPD decreased; over 2–14 days in culture the beating rate fell while FPD lengthened (percentages dropped from the text by the researcher 2026-11-06: +22.6 % and −7.7 %, abstract p. 1).
    - > Guerrelli et al. (2024) quantified these effects directly. — main.md:183
    - > The authors recommend standardised protocols and reporting of key conditions such as culture time and equilibration time, but the analysis parameters in their example reporting datasheet are limited to the number of electrodes analysed and the averaging time, with no field for the FPD definition or rate correction (Guerrelli et al., 2024). — main.md:183
- [x] (8) [High-throughput] the authors recommend standardised protocols and reporting of key conditions such as culture time and equilibration time.
    - > Guerrelli et al. (2024) quantified these effects directly. — main.md:183
    - > The authors recommend standardised protocols and reporting of key conditions such as culture time and equilibration time, but the analysis parameters in their example reporting datasheet are limited to the number of electrodes analysed and the averaging time, with no field for the FPD definition or rate correction (Guerrelli et al., 2024). — main.md:183

- [x] (9) [High-throughput] the analysis parameters of their example reporting datasheet are limited to the number of electrodes analysed and the averaging time; no field for the FPD definition or rate correction (added 2026-11-06; the missing fields are our observation).
    - > Guerrelli et al. (2024) quantified these effects directly. — main.md:183
    - > The authors recommend standardised protocols and reporting of key conditions such as culture time and equilibration time, but the analysis parameters in their example reporting datasheet are limited to the number of electrodes analysed and the averaging time, with no field for the FPD definition or rate correction (Guerrelli et al., 2024). — main.md:183
- [x] (10) [Morphology] an electrode with an upright T wave, or the positive portion of a biphasic T wave, was chosen for FPD analysis (added 2026-11-06).
    - > The shape of the T wave can also decide which signal is analysed: Guerrelli et al. (2024) chose for FPD analysis an electrode whose T wave was upright or had a positive portion of a biphasic T wave. — main.md:173
- [x] (11) [Maturation] mean spike amplitude of spontaneously beating cells was below 0.5 mV two days post-defrost and several millivolts by day 14 (iCell² 0.30 → 3.6 mV, Cor.4U 0.23 → 8.1 mV; added 2026-11-06, values dropped from the text 2026-11-06; comparison with the Clements threshold is ours, register item 29).
    - > Guerrelli et al. (2024) show this kind of drift in an MEA setting: over two weeks in culture, the FPD of spontaneously beating cells lengthened markedly and the beating rate declined, together with a rise in *KCNJ2* expression, changes the authors link to continued maturation. — main.md:130
    - > Whether a culture meets the amplitude criterion also depends on when it is recorded: in Guerrelli et al. (2024), the mean spike amplitude of spontaneously beating cells of two commercial lines was below 0.5 mV two days post-defrost and had risen to several millivolts by day 14, whereas the proposal leaves culture protocols to the cell vendors (Clements et al., 2025). — main.md:134
Pointers: abstract p. 1 (22.6 % and 7.7 % in 20 min; −12.7 beats/min and +257 ms from day 2 to 14; "may be linked to the continued maturation"; "MEA-based studies should establish a standardized protocol and report key experimental conditions (e.g., cell line, culture time, equilibration time, electrical stimulation settings, and raw data values)"). KCNJ2 27.5-fold at p. 10 (iCell², 2–30 days; 5.0-fold in Cor.4U). (6) Results on paced recordings ("metrics are rate dependent, we measured each variable again in response to external pacing (1.5 Hz)"; 275.5 ± 13.8 to 336.0 ± 14 ms, +21.9 % against +54.8 % spontaneous; Fig. 5A). (3) the 15–20 min recommendation is on the wiki page (Practical recommendations); the page in the paper was not looked up. (9) Supplemental Table S8 ("Example reporting datasheet"; Analysis Parameters: number of electrodes analyzed, length of time signals were averaged over); main text cites it ("see Supplemental Table S8"). (10) Methods, p. 3 ("signals were selected for FPD analysis that had an upright t-wave or the positive portion of a biphasic t-wave"; one electrode per well, averaged 30 s; Supplemental Fig. S1, CV 1.85–3.79 %). (11) Supplemental Tables S2 (iCell², day 2 0.301 ± 0.238, day 14 3.611 ± 0.774 mV) and S5 (Cor.4U, day 2 0.228 ± 0.153, day 14 8.093 ± 3.092 mV); values are well means from one selected electrode, not the percentage of electrodes used by Clements. (3) p. 4, Results ("The manufacturer's instructions (51) recommend equilibrating hiPSC-CMs in an MEA system for 10 min ..., although some studies have reported using a longer equilibration time (15–20 min)"; rate slower than at 20 min only between 2 and 12 min, FPD longer only between 2 and 7 min; "it is recommended that hiPSC-CM acclimate to the MEA system for 15–20 min"); Cor.4U: Supplemental Fig. S5 and Table S7 (no significant change). (4) Results, culture time ("Since the hiPSC-CM spontaneous beating rate slowed significantly ... and cardiac electrophysiology metrics are rate dependent, we measured each variable again in response to external pacing (1.5 Hz)"); Methods, drug exposure ("Since these pharmacological agents can alter the spontaneous beating rate, electrical signals were recorded in response to external pacing (1.5 Hz for E-4031, 3 Hz for nifedipine and isoproterenol)") and the drug figure legend (E-4031 slowed, nifedipine and isoproterenol increased the intrinsic rate).

## ✅ Hayakawa et al. (2014)

Local file: `raw/hayakawa-2014-motion-fp.pdf`; page `wiki/papers/hayakawa-2014-motion-fp.md`. Status: checked against the full text 2026-10-24 (text extraction; figures not viewed; supplementary materials not available then). Supplementary methods (`raw/hayakawa-2014-motion-fp-supplementary.docx`) read 2026-11-06: methods only, no effect on the claims below.

- [x] (1) [Fiducial] with simultaneous video and MEA recordings in iCell monolayers, the two FPD end points in use at the time (peak of the positive deflection; return of the positive deflection to baseline) appeared to correspond to different phases of the relaxation motion (its upstroke and its peak), and an accurate end point was difficult to establish.
    - > Earlier work with simultaneous video and MEA recordings in iCell monolayers likewise noted that the two FPD end points in use at the time, the peak of the positive deflection and the return of the positive deflection to baseline, appeared to correspond to different phases of the relaxation motion (its upstroke and its peak, respectively), and that an accurate end point was difficult to establish (Hayakawa et al., 2014). — main.md:110
- [x] (2) [Table 2] listed in the R-to-T-peak row with the start at the initial negative peak; the relation column repeats (1).
    - > | R-to-T-peak | R peak (Hayakawa et al., 2014: initial negative peak) | T-wave peak | T-wave peak coincided with APD90 only for biphasic T waves (a minority morphology; NRVM, not hiPSC-CM; Ernault et al., 2024); in hiPSC-CMs, R-to-T-peak FPD correlated only minimally with APD50 and APD90 (Lee et al., 2024); the peak of the positive deflection appeared to match the upstroke of relaxation (Hayakawa et al., 2014) | Hayakawa et al., 2014; Lee et al., 2024; Weiser-Bitoun et al., 2026; described as a common convention and criticised in Mäki, 2023 | — main.md:116
    - > | Baseline return | Depolarization onset (10% threshold) | Signal return to within 10% of baseline | Intended to capture the full repolarization wave (Mäki, 2023); not compared with the AP; return to baseline appeared to match the peak of relaxation (Hayakawa et al., 2014) | Mäki, 2023 | — main.md:117
- [x] (3) [Maturation] field potential duration and contraction duration were linearly related across drug concentrations under non-arrhythmic conditions, with a different slope for each drug (the evidence Scheurer et al., 2025, cite).
    - > Scheurer et al. also cite earlier evidence linking field potential duration to contraction duration; in that work, the two were linearly related across drug concentrations under non-arrhythmic conditions, with a different slope for each drug (Hayakawa et al., 2014). — main.md:138
    - > Taken together, some ingredients of an MEA-based maturity classifier have been reported separately: an interpretable machine-learning method validated on video features (Scheurer et al., 2025), MEA parameters that differ between the same maturation conditions (Li et al., 2025, whose B27 and maturation-medium groups Scheurer et al. follow), a reported link between FPD and contraction (Hayakawa et al., 2014), and evidence that maturation status matters for translation (Correia et al., 2024). — main.md:140
- [x] (4) [Maturation, Conclusion] a reported link between FPD and contraction duration, as one ingredient of an MEA-based maturity classifier.
    - > Scheurer et al. also cite earlier evidence linking field potential duration to contraction duration; in that work, the two were linearly related across drug concentrations under non-arrhythmic conditions, with a different slope for each drug (Hayakawa et al., 2014). — main.md:138
    - > Taken together, some ingredients of an MEA-based maturity classifier have been reported separately: an interpretable machine-learning method validated on video features (Scheurer et al., 2025), MEA parameters that differ between the same maturation conditions (Li et al., 2025, whose B27 and maturation-medium groups Scheurer et al. follow), a reported link between FPD and contraction (Hayakawa et al., 2014), and evidence that maturation status matters for translation (Correia et al., 2024). — main.md:140
    - > Some ingredients for such a reference have been reported separately: an interpretable machine-learning approach validated on non-invasive beating features (Scheurer et al., 2025), MEA parameters that differ between maturation conditions (Li et al., 2025) and a reported link between field potential duration and contraction duration (Hayakawa et al., 2014); what is missing is an independent maturity measure taken on the same MEA cultures. — main.md:234
- [x] (5) [Outlook] image-based motion and MEA field potentials were recorded simultaneously in hiPSC-CM monolayers, with linear relationships between contraction–relaxation duration and FPD across drug concentrations and drug-specific slopes.
    - > Earlier work recorded image-based motion and MEA field potentials simultaneously in hiPSC-CM monolayers and found linear relationships between contraction–relaxation duration and FPD across drug concentrations, with drug-specific slopes (Hayakawa et al., 2014). — main.md:193
- [x] (6) [Limitations] pre-2022 work cited as background.
    - > - (vi) A few works from before 2022, such as Blinova et al. (2018), Hayakawa et al. (2014) and Ryynänen et al. (2018), are cited only as background for conventions, datasets and earlier multimodal work. — main.md:220

Pointers: (1) p. 3 ("The end of the FPD was previously defined as either the peak of the positive deflection ... or the point where the positive deflection returns to the baseline ... The former end-point appears to be correlated with the upstroke of relaxation motion, while the latter ... with the peak of relaxation motion. However, determination of an accurate end-point of FP proved difficult to establish"). (2) TTX section, p. 5: FPD "between the initial negative peak and the peak of positive deflection" (confirmed by the researcher 2026-10-29). (3)(5) abstract p. 1; p. 5–6 (E-4031 R = 0.915, slope 1.362; verapamil R = 0.970, 0.633; isoproterenol R = 0.943, 0.737 in the Results text p. 6 and 0.738 in the Fig. 8B caption); p. 11 ("the CRD can be a surrogate of the FPD in non-arrhythmic conditions").

## ✅ Hu et al. (2026)

Local file: `raw/hu-2026-tft-mea-multimodal.pdf` (+ supplementary; both git-ignored, not open access); page `wiki/papers/hu-2026-tft-mea-multimodal.md`. Status: full text and supplement read, Figures 2–7 viewed, at ingest 2026-11-01. Fetal mouse cardiomyocytes, outside the hiPSC-CM scope; cited in the outlook only.

- [x] (1) [Outlook] a proof of concept on a transparent thin-film-transistor MEA recorded field potentials and video of the same culture of fetal mouse cardiomyocytes and analysed both with interpretable machine learning, separating the recording before and after isoprenaline.
    - > A recent proof of concept on a transparent thin-film-transistor MEA recorded field potentials and video of the same culture of fetal mouse cardiomyocytes and analysed both with interpretable machine learning, separating the recording before and after isoprenaline (Hu et al., 2026). — main.md:193
    - > The authors of the proof of concept above see the same direction: combining a transparent MEA with machine learning, in their view, moves beyond single-modality analyses towards sensor fusion (Hu et al., 2026). — main.md:195
- [x] (2) [Outlook] it used ten electrodes and depolarization-based features without FPD, and the two modalities were clustered separately, so how far they were combined in one model is unclear.
    - > A recent proof of concept on a transparent thin-film-transistor MEA recorded field potentials and video of the same culture of fetal mouse cardiomyocytes and analysed both with interpretable machine learning, separating the recording before and after isoprenaline (Hu et al., 2026). — main.md:193
    - > The authors of the proof of concept above see the same direction: combining a transparent MEA with machine learning, in their view, moves beyond single-modality analyses towards sensor fusion (Hu et al., 2026). — main.md:195
- [x] (3) [Limitations] example of evidence in fetal mouse cells.
    - > Most methodological statements rest on one or two studies, and some rest on rat cells (Ernault et al., 2024), fetal mouse cells (Hu et al., 2026), simulations (Hwang et al., 2023; Botti et al., 2026), tissue-embedded electrodes (Lin et al., 2023) or modalities other than field potentials (Fetterman et al., 2024; Scheurer et al., 2025). — main.md:216
- [x] (4) [Outlook] the authors see the combination of a transparent MEA and machine learning as moving beyond single-modality analyses towards sensor fusion (added 2026-11-08; a stated outlook of the authors, not something their own analysis achieved, see (2)).
    - > A recent proof of concept on a transparent thin-film-transistor MEA recorded field potentials and video of the same culture of fetal mouse cardiomyocytes and analysed both with interpretable machine learning, separating the recording before and after isoprenaline (Hu et al., 2026). — main.md:193
    - > The authors of the proof of concept above see the same direction: combining a transparent MEA with machine learning, in their view, moves beyond single-modality analyses towards sensor fusion (Hu et al., 2026). — main.md:195

Pointers: (1) section 2.1.2 (primary prenatal mouse cardiomyocytes, "rather than iPSC-derived cells"), 2.3 (optical flow; alignment by the drug-addition timestamp), 2.6 (k-means, supervised check, SHAP; "a sensor fusion technique"), Fig. 4 (isoprenaline). (2) section 2.2.3 and 3.1 (10 adjacent electrodes), Fig. 3 (features on the depolarization spike: R50/R90 times to and from peak, peak width, peak-to-peak interval), Fig. 4 (k-means per modality), Fig. 6 (SHAP lists electrical features only). "How far they were combined ... is unclear" is our reading of Figs 4 and 6. (4) section 5, Conclusion, p. 9 ("Such an approach moves beyond conventional single-modality or purely statistical analyses by enabling sensor fusion, robust feature attribution, and reproducibility").

## Hwang et al. (2023)

Local file: `raw/hwang-2023-spheroids.pdf`; page `wiki/papers/hwang-2023-spheroids.md`. Status: checked against the full text 2026-10-24.

- [ ] (1) [Timeline] "3D spheroid geometry as FP variability source".
    - > : 3D spheroid geometry as FP variability source (Hwang et al.) — main.md:66
- [ ] (2) [FPDc] the study uses Fridericia-corrected FPD.
    - > By analogy with the clinical QT interval, the Fridericia formula ($FPDc = FPD/RR^{0.33}$, where RR is the interval between beats) is the correction used in the studies examined here that report rate-corrected FPD (Altrocchi et al., 2023; Hwang et al., 2023; Maurissen et al., 2024; Park et al., 2026); Park et al. (2025) also report corrected FPD but do not name the formula. — main.md:121
- [ ] (3) [3D] in simulations of hiPSC-CM spheroids on MEAs, compared with in vitro recordings, FP shapes varied strongly with the stimulation and electrode locations even with a single cell type, so the 3D geometry itself adds FP variability; the evidence comes from a simulation with one cell source and two drugs.
    - > In simulations of hiPSC-CM spheroids on MEAs, compared with in vitro recordings, field potential shapes varied strongly with the stimulation and electrode locations even with a single cell type, so the 3D geometry itself adds FP variability (Hwang et al., 2023); this evidence comes from a simulation with one cell source and two drugs. — main.md:176
- [ ] (4) [Conclusion] in simulations the 3D geometry alone changed FP shape.
    - > In one study, Fridericia-corrected FPD was similar in 2D monolayers and 3D tissue sheets (Maurissen et al., 2024), but in simulations the 3D geometry alone changed FP shape (Hwang et al., 2023), and conventional MEAs contact 3D tissue only on one surface (Lin et al., 2023). — main.md:233
- [ ] (5) [Limitations] example of simulation-based evidence.
    - > Most methodological statements rest on one or two studies, and some rest on rat cells (Ernault et al., 2024), fetal mouse cells (Hu et al., 2026), simulations (Hwang et al., 2023; Botti et al., 2026), tissue-embedded electrodes (Lin et al., 2023) or modalities other than field potentials (Fetterman et al., 2024; Scheurer et al., 2025). — main.md:216

Pointers: (3) abstract p. 1 and Discussion p. 7; one cell source and two drugs from the wiki page (Our observations). (2) p. 5 ("FPD corrected with Fridericia's formula").

## Ismaili et al. (2023)

Local file: `raw/ismaili-2023-hamburg.pdf`; page `wiki/papers/ismaili-2023-hamburg.md`. Status: checked against the full text 2026-10-24.

- [ ] (1) [Timeline] "Hamburg perspective on hiPSC-CM limitations".
    - > 2023 : Hamburg perspective on hiPSC-CM limitations (Ismaili et al.) — main.md:65
- [ ] (2) [Motivation] broader methodological and biological challenges of hiPSC-CMs as electrophysiological models, including ion channel expression, resting membrane potential and the identity of cell subtypes, discussed from a critical perspective.
    - > Broader methodological and biological challenges of hiPSC-CMs as electrophysiological models—including ion channel expression, resting membrane potential, and the identity of cell subtypes—have been discussed from a critical perspective (Ismaili et al., 2023). — main.md:48
- [ ] (3) [Maturation] hiPSC-CMs express ion channels that are absent from adult working myocardium, notably the funny current (If) and occasionally the T-type Ca²⁺ current, although the latter is not necessarily a sign of immaturity.
    - > They express ion channels that are absent from adult working myocardium, notably the funny current (I<sub>f</sub>) and occasionally the T-type Ca²⁺ current, although the latter is not necessarily a sign of immaturity (Ismaili et al., 2023). — main.md:128
    - > Whether ventricular-, atrial- and nodal-like cells form distinct subpopulations within one preparation is debated (Ismaili et al., 2023), but patch-clamp data show such subtypes in the lines of Park et al. (2026). — main.md:128
- [ ] (4) [Maturation] whether ventricular-, atrial- and nodal-like cells form distinct subpopulations within one preparation is debated.
    - > They express ion channels that are absent from adult working myocardium, notably the funny current (I<sub>f</sub>) and occasionally the T-type Ca²⁺ current, although the latter is not necessarily a sign of immaturity (Ismaili et al., 2023). — main.md:128
    - > Whether ventricular-, atrial- and nodal-like cells form distinct subpopulations within one preparation is debated (Ismaili et al., 2023), but patch-clamp data show such subtypes in the lines of Park et al. (2026). — main.md:128

Pointers: (3) p. 3 ("clearly express ion channels that are absent in the adult human working myocardium"; HCN4; ICa,T "cannot necessarily be taken as an indication of immaturity"). (4) p. 4 (a study of 320 cells with a single Gaussian APD90 distribution "arguing against ... a truly mixed cell population"). The paper does not mention MEA, FPD or rate correction.

## Kabanov et al. (2026)

Local file: `raw/kabanov-2026-cardioscripts.pdf`; page `wiki/papers/kabanov-2026-cardioscripts.md`. Status: checked against the abstract, Methods and the lidocaine experiment 2026-10-24.

- [ ] (1) [Timeline] "CardioScripts — combined atomic force microscopy and MEA electromechanical analysis" (reworded 2026-11-06: detail and abbreviations not needed for the argument removed).
    - > : CardioScripts — combined atomic force microscopy and MEA electromechanical analysis (Kabanov et al.) — main.md:79
- [ ] (2) [Table 1] CardioScripts / Myopyth, Python; FPD end not reported (T peaks detected); combined atomic force microscopy and MEA, electromechanical coupling and decoupling analysis.
    - > | CardioScripts / Myopyth (Kabanov et al., 2026) | 2026 | Python | Not reported (T peaks detected) | Combined atomic force microscopy and MEA; electromechanical coupling and decoupling analysis | — main.md:99
- [ ] (3) [Fiducial] CardioScripts reports QT and T-peak rather than FPD.
    - > The open platforms in Table 1 that measure FPD state their convention explicitly, and the conventions differ (CardioScripts reports QT and T-peak rather than FPD; Kabanov et al., 2026): — main.md:104
- [ ] (4) [Outlook] contraction force from simultaneous atomic force microscopy is added to the MEA recording; the synchronous validation was done on embryoid bodies only.
    - > Several of the studies examined already add a second measurement to the MEA recording: impedance read alongside FP (Altrocchi et al., 2023), intracellular-like signals obtained through the same electrodes by electroporation (Lee et al., 2024), and contraction force from simultaneous atomic force microscopy (Kabanov et al., 2026), whose synchronous validation was done on embryoid bodies only. — main.md:193

Pointers: p. 2 ("fully open source and freely available"); cells HL-1 and embryoid bodies from hESC line CCTL14; T peaks detected, FPD not defined (p. 3); lidocaine and the FP–contraction delay in embryoid bodies (p. 7–8, Figure 10).

## Karami et al. (2026)

Local file: `raw/karami-2026-mea-cardiotoxicity.pdf` (open access, CC BY); page `wiki/papers/karami-2026-mea-cardiotoxicity.md`. Status: read in full at ingest 2026-11-01. A narrative review with several citation slips; used only for textbook-level statements.

- [ ] (1) [Outlook] the FP is shaped by tissue and hardware, including electrode geometry, cell–electrode coupling, cell density and gap-junctional coupling.
    - > An FP is the cellular signal as shaped by the surrounding tissue and by the recording hardware, including electrode geometry, cell–electrode coupling, cell density and gap-junctional coupling (Karami et al., 2026), and several of the studies examined show that FP features do not map directly onto the action potential (AP). — main.md:199
    - > The cell–electrode interface can be described by an equivalent circuit in which the recorded voltage depends on the membrane potential through the seal resistance and the impedances of the junctional membrane, the electrode and the amplifier; depending on how tightly the cells adhere, the signal follows the membrane potential or its first or second time derivative (Karami et al., 2026). — main.md:199
    - > Impedance is sensitive to the distance between cells and electrode, down to changes of about 1 nm (Karami et al., 2026), so it could in principle register changes in coupling. — main.md:203
    - > Removing the device contribution alone would not be sufficient, because a field potential is a weighted sum of the transmembrane currents of many surrounding cells, which may also make the recovery an ill-posed inverse problem (Karami et al., 2026). — main.md:205
- [ ] (2) [Outlook] the cell–electrode interface can be described by an equivalent circuit in which the recorded voltage depends on the membrane potential through the seal resistance and the impedances of the junctional membrane, the electrode and the amplifier; depending on how tightly the cells adhere, the signal follows the membrane potential or its first or second time derivative.
    - > An FP is the cellular signal as shaped by the surrounding tissue and by the recording hardware, including electrode geometry, cell–electrode coupling, cell density and gap-junctional coupling (Karami et al., 2026), and several of the studies examined show that FP features do not map directly onto the action potential (AP). — main.md:199
    - > The cell–electrode interface can be described by an equivalent circuit in which the recorded voltage depends on the membrane potential through the seal resistance and the impedances of the junctional membrane, the electrode and the amplifier; depending on how tightly the cells adhere, the signal follows the membrane potential or its first or second time derivative (Karami et al., 2026). — main.md:199
    - > Impedance is sensitive to the distance between cells and electrode, down to changes of about 1 nm (Karami et al., 2026), so it could in principle register changes in coupling. — main.md:203
    - > Removing the device contribution alone would not be sufficient, because a field potential is a weighted sum of the transmembrane currents of many surrounding cells, which may also make the recovery an ill-posed inverse problem (Karami et al., 2026). — main.md:205
- [ ] (3) [Outlook] a field potential is a superposition of the transmembrane currents of many surrounding cells; cited since 2026-11-03 also for removing the device contribution alone not being sufficient (moved from Ernault (5)).
    - > An FP is the cellular signal as shaped by the surrounding tissue and by the recording hardware, including electrode geometry, cell–electrode coupling, cell density and gap-junctional coupling (Karami et al., 2026), and several of the studies examined show that FP features do not map directly onto the action potential (AP). — main.md:199
    - > The cell–electrode interface can be described by an equivalent circuit in which the recorded voltage depends on the membrane potential through the seal resistance and the impedances of the junctional membrane, the electrode and the amplifier; depending on how tightly the cells adhere, the signal follows the membrane potential or its first or second time derivative (Karami et al., 2026). — main.md:199
    - > Impedance is sensitive to the distance between cells and electrode, down to changes of about 1 nm (Karami et al., 2026), so it could in principle register changes in coupling. — main.md:203
    - > Removing the device contribution alone would not be sufficient, because a field potential is a weighted sum of the transmembrane currents of many surrounding cells, which may also make the recovery an ill-posed inverse problem (Karami et al., 2026). — main.md:205
- [ ] (4) [Outlook] impedance is sensitive to the distance between cells and electrode, down to changes of about 1 nm.
    - > An FP is the cellular signal as shaped by the surrounding tissue and by the recording hardware, including electrode geometry, cell–electrode coupling, cell density and gap-junctional coupling (Karami et al., 2026), and several of the studies examined show that FP features do not map directly onto the action potential (AP). — main.md:199
    - > The cell–electrode interface can be described by an equivalent circuit in which the recorded voltage depends on the membrane potential through the seal resistance and the impedances of the junctional membrane, the electrode and the amplifier; depending on how tightly the cells adhere, the signal follows the membrane potential or its first or second time derivative (Karami et al., 2026). — main.md:199
    - > Impedance is sensitive to the distance between cells and electrode, down to changes of about 1 nm (Karami et al., 2026), so it could in principle register changes in coupling. — main.md:203
    - > Removing the device contribution alone would not be sufficient, because a field potential is a weighted sum of the transmembrane currents of many surrounding cells, which may also make the recovery an ill-posed inverse problem (Karami et al., 2026). — main.md:205

- [ ] (5) [Morphology] depending on cell–electrode coupling, the FP may follow the membrane potential or its first or second time derivative (same source passage as (2); added 2026-11-05).
    - > Which sign the repolarization wave should have cannot simply be assumed either, because depending on cell–electrode coupling the FP may follow the membrane potential or its first or second time derivative (Karami et al., 2026). — main.md:173

Pointers: (1) p. 9 ("FPD and APD are not equivalent measurements ... electrode geometry, cell-electrode coupling, cell density and degree of gap junctional coupling and conduction properties"). (2) pp. 13–14, Figure 5B, Equations 4–7 (point-contact model, Fromherz et al., 1991; Shaik et al., 2022); Table 4 words the derivative cases slightly differently. (3) p. 14 ("the recorded signal will be a superposition of these individual signals"; the text says "superposition", main.md "weighted sum", the weighting being the decay with distance described in the same passage). (4) p. 18 (Giaever and Keese, 1991). (5) pp. 13–14, Table 4 (derivative cases).

## Lee et al. (2024)

Local file: `raw/lee-2024-cardiomea.pdf`; page `wiki/papers/lee-2024-cardiomea.md`. Status: checked against the Europe PMC full text 2026-10-18 (Table 1, Table 3, Results); Table 3 rechecked in the PDF 2026-10-29.

- [ ] (1) [Timeline] "CardioMEA platform — scalable open analysis".
    - > 2024 : CardioMEA platform — scalable open analysis (Lee et al.) — main.md:67
- [ ] (2) [Open pipelines] open tools such as MultiElec and CardioMDA existed before 2022.
    - > Such tools are not new, as MultiElec and CardioMDA, for example, existed before 2022 (Dunham et al., 2022; Lee et al., 2024), but several new ones have appeared since 2022, some of them built for new kinds of data such as high-density arrays (Lee et al., 2024) and cardiac organoids (Weiser-Bitoun et al., 2026). — main.md:85
    - > More recently, the CardioMEA platform (Lee et al., 2024) was built specifically for high-density MEA data: it extracts features from both extracellular and intracellular-like (electroporation-derived) signals, and includes an automated machine-learning module for ranking the features that separate diseased from control lines. — main.md:87
- [ ] (3) [Open pipelines] one of the new open tools built for a new kind of data (high-density arrays).
    - > Such tools are not new, as MultiElec and CardioMDA, for example, existed before 2022 (Dunham et al., 2022; Lee et al., 2024), but several new ones have appeared since 2022, some of them built for new kinds of data such as high-density arrays (Lee et al., 2024) and cardiac organoids (Weiser-Bitoun et al., 2026). — main.md:85
    - > More recently, the CardioMEA platform (Lee et al., 2024) was built specifically for high-density MEA data: it extracts features from both extracellular and intracellular-like (electroporation-derived) signals, and includes an automated machine-learning module for ranking the features that separate diseased from control lines. — main.md:87
- [ ] (4) [Open pipelines, Table 1] CardioMEA, Python, built for high-density MEA data: features from extracellular and intracellular-like (electroporation-derived) signals, and an automated machine-learning module ranking the features that separate diseased from control lines.
    - > Such tools are not new, as MultiElec and CardioMDA, for example, existed before 2022 (Dunham et al., 2022; Lee et al., 2024), but several new ones have appeared since 2022, some of them built for new kinds of data such as high-density arrays (Lee et al., 2024) and cardiac organoids (Weiser-Bitoun et al., 2026). — main.md:85
    - > More recently, the CardioMEA platform (Lee et al., 2024) was built specifically for high-density MEA data: it extracts features from both extracellular and intracellular-like (electroporation-derived) signals, and includes an automated machine-learning module for ranking the features that separate diseased from control lines. — main.md:87
    - > | CardioMEA (Lee et al., 2024) | 2024 | Python | R-to-T-wave peak | High-density MEA; extracellular and intracellular-like signals; automated machine-learning feature ranking | — main.md:97
- [ ] (5) [Fiducial, Table 1, Table 2] FPD runs from the R peak to the T-wave peak. To check: the paper says "R spike"; confirm that it means the peak.
    - > - **CardioMEA** (Lee et al., 2024) and **PhysioMEA** (Weiser-Bitoun et al., 2026): from the R peak to the T-wave peak — main.md:107
    - > Direct evidence from hiPSC-CMs points in the same cautious direction: in high-density recordings from iCell cardiomyocytes, R-to-T-peak FPD correlated only minimally with the action potential duration at 50% repolarization (APD50) and APD90 measured from intracellular-like signals on the same electrodes, which the authors attribute to small, noisy T waves (Lee et al., 2024). — main.md:110
    - > | CardioMEA (Lee et al., 2024) | 2024 | Python | R-to-T-wave peak | High-density MEA; extracellular and intracellular-like signals; automated machine-learning feature ranking | — main.md:97
    - > | R-to-T-peak | R peak (Hayakawa et al., 2014: initial negative peak) | T-wave peak | T-wave peak coincided with APD90 only for biphasic T waves (a minority morphology; NRVM, not hiPSC-CM; Ernault et al., 2024); in hiPSC-CMs, R-to-T-peak FPD correlated only minimally with APD50 and APD90 (Lee et al., 2024); the peak of the positive deflection appeared to match the upstroke of relaxation (Hayakawa et al., 2014) | Hayakawa et al., 2014; Lee et al., 2024; Weiser-Bitoun et al., 2026; described as a common convention and criticised in Mäki, 2023 | — main.md:116
- [ ] (6) [Fiducial, Table 2, Outlook] in iCell cardiomyocyte high-density recordings, R-to-T-peak FPD correlated only minimally with APD50 and APD90 measured from intracellular-like signals on the same electrodes, which the authors attribute to small, noisy T waves.
    - > - **CardioMEA** (Lee et al., 2024) and **PhysioMEA** (Weiser-Bitoun et al., 2026): from the R peak to the T-wave peak — main.md:107
    - > Direct evidence from hiPSC-CMs points in the same cautious direction: in high-density recordings from iCell cardiomyocytes, R-to-T-peak FPD correlated only minimally with the action potential duration at 50% repolarization (APD50) and APD90 measured from intracellular-like signals on the same electrodes, which the authors attribute to small, noisy T waves (Lee et al., 2024). — main.md:110
    - > | R-to-T-peak | R peak (Hayakawa et al., 2014: initial negative peak) | T-wave peak | T-wave peak coincided with APD90 only for biphasic T waves (a minority morphology; NRVM, not hiPSC-CM; Ernault et al., 2024); in hiPSC-CMs, R-to-T-peak FPD correlated only minimally with APD50 and APD90 (Lee et al., 2024); the peak of the positive deflection appeared to match the upstroke of relaxation (Hayakawa et al., 2014) | Hayakawa et al., 2014; Lee et al., 2024; Weiser-Bitoun et al., 2026; described as a common convention and criticised in Mäki, 2023 | — main.md:116
    - > Several of the studies examined already add a second measurement to the MEA recording: impedance read alongside FP (Altrocchi et al., 2023), intracellular-like signals obtained through the same electrodes by electroporation (Lee et al., 2024), and contraction force from simultaneous atomic force microscopy (Kabanov et al., 2026), whose synchronous validation was done on embryoid bodies only. — main.md:193
    - > The T-wave peak tracks APD90 only when the T wave is biphasic (Ernault et al., 2024), and R-to-T-peak FPD correlated only minimally with APD50 and APD90 from intracellular-like signals on the same electrodes (Lee et al., 2024). — main.md:199
    - > Electroporation through the recording electrodes (Lee et al., 2024) yields paired FP and AP-like signals from the same electrodes and is therefore a candidate source of training and validation data, and AI-assisted sensor fusion of further simultaneous modalities could add ground truth. — main.md:201
- [ ] (7) [Outlook] electroporation through the recording electrodes yields paired FP and AP-like signals from the same electrodes (their use as training and validation data is the author's proposal).
    - > Several of the studies examined already add a second measurement to the MEA recording: impedance read alongside FP (Altrocchi et al., 2023), intracellular-like signals obtained through the same electrodes by electroporation (Lee et al., 2024), and contraction force from simultaneous atomic force microscopy (Kabanov et al., 2026), whose synchronous validation was done on embryoid bodies only. — main.md:193
    - > The T-wave peak tracks APD90 only when the T wave is biphasic (Ernault et al., 2024), and R-to-T-peak FPD correlated only minimally with APD50 and APD90 from intracellular-like signals on the same electrodes (Lee et al., 2024). — main.md:199
    - > Electroporation through the recording electrodes (Lee et al., 2024) yields paired FP and AP-like signals from the same electrodes and is therefore a candidate source of training and validation data, and AI-assisted sensor fusion of further simultaneous modalities could add ground truth. — main.md:201
- [ ] (8) [Conclusion] automated feature ranking in an open platform is one of the machine-learning uses in the studies examined.
    - > Looking forward, machine learning is used in several of the studies examined — from ensemble classifiers for TdP risk prediction (Pramudito et al., 2026) and genotype-specific risk models (Park et al., 2026) to automated feature ranking in an open platform (Lee et al., 2024) — and it may become a more integral layer of cardiomyocyte MEA workflows. — main.md:236

Pointers: (2) Table 3 (MultiElec, CardioMDA; it compares language, GUI, pipeline execution, condition comparison, wave propagation and intracellular-like analysis, not FPD definitions). (4) Table 1 (features) and Table 3 (platform comparison). (6) Figure 4 (Spearman correlations) and the text after it.

## Lee et al. (2026)

Local file: `raw/lee-2026-ito-mea.pdf` (+ supplementary; open access, CC BY-NC); page `wiki/papers/lee-2026-ito-mea.md`. Status: read in full at ingest 2026-11-01; Figure 4 viewed. First author S.-G. Lee, not the J. Lee of CardioMEA.

- [ ] (0) [Timeline] "Transparent MEA with FP and optical readouts of hiPSC-CMs", 2026 (added 2026-11-01; ITO dropped 2026-11-06).
    - > : Transparent MEA with FP and optical readouts of hiPSC-CMs (Lee et al.) — main.md:81
- [ ] (1) [FPDc] in one hiPSC-CM study, doxorubicin slowed the beat period to about 8 s, and Fridericia-corrected FPD then fell while uncorrected FPD rose.
    - > In one hiPSC-CM study, doxorubicin slowed the beat period to about 8 s, and Fridericia-corrected FPD then fell while uncorrected FPD rose (Lee et al., 2026). — main.md:123
- [ ] (2) [Outlook] a transparent MEA (indium tin oxide electrodes; material dropped from the text 2026-11-06) was used to record field potentials, morphology and Ca²⁺ imaging of hiPSC-CMs in the same wells, with the readouts reported side by side.
    - > A transparent MEA has also been used to record field potentials, morphology and Ca²⁺ imaging of hiPSC-CMs in the same wells, with the readouts reported side by side (Lee et al., 2026). — main.md:193
    - > If the separation worked, it would also make FP-derived results from different hardware more comparable, since chip composition and recording hardware can alter absolute signal values (Lee et al., 2026), and the separated cellular signal could serve as the machine-learning input discussed above, rather than only the parameters extracted from the raw recording. — main.md:207
- [ ] (3) [Outlook] chip composition and recording hardware can alter absolute signal values.
    - > A transparent MEA has also been used to record field potentials, morphology and Ca²⁺ imaging of hiPSC-CMs in the same wells, with the readouts reported side by side (Lee et al., 2026). — main.md:193
    - > If the separation worked, it would also make FP-derived results from different hardware more comparable, since chip composition and recording hardware can alter absolute signal values (Lee et al., 2026), and the separated cellular signal could serve as the machine-learning input discussed above, rather than only the parameters extracted from the raw recording. — main.md:207

Pointers: (1) Results on doxorubicin and Fig. 4B–D (beat period 8.213 s on day 1 against 1.961 s in controls; FPD 0.382, 0.448, 0.495 s; FPDc fell on day 1 "due to the sharp BP prolongation"). (2) Methods (CFPS-ITO-16W2E plates; Fluo-4 imaging at baseline only) and Figs 2–4. (3) Discussion, first paragraph ("differences in MEA chip composition and recording hardware may alter absolute signal values").

## Li et al. (2025)

Local file: `raw/li-2025-maturation.pdf` (+ supplementary); page `wiki/papers/li-2025-maturation.md`. Status: full text and Supplementary Tables 2–3 read at ingest 2026-10-30.

- [ ] (0) [Timeline] "MEA parameters differ between maturation conditions", 2025 (added 2026-11-01).
    - > : MEA parameters differ between maturation conditions (Li et al.) — main.md:76
- [ ] (1) [Maturation] conduction velocity and spike amplitude rose from a standard B27 medium to a fatty-acid-enriched maturation medium, and further with nanopatterning and electrostimulation (reworded 2026-11-04: detail not needed for the argument removed).
    - > In Li et al. (2025), conduction velocity and spike amplitude rose from a standard B27 medium to a fatty-acid-enriched maturation medium, and further with nanopatterning and electrostimulation. — main.md:134
    - > Taken together, some ingredients of an MEA-based maturity classifier have been reported separately: an interpretable machine-learning method validated on video features (Scheurer et al., 2025), MEA parameters that differ between the same maturation conditions (Li et al., 2025, whose B27 and maturation-medium groups Scheurer et al. follow), a reported link between FPD and contraction (Hayakawa et al., 2014), and evidence that maturation status matters for translation (Correia et al., 2024). — main.md:140
- [ ] (2) [Maturation] patch-clamp markers measured in other cells of the same groups changed in the same direction.
    - > In Li et al. (2025), conduction velocity and spike amplitude rose from a standard B27 medium to a fatty-acid-enriched maturation medium, and further with nanopatterning and electrostimulation. — main.md:134
    - > Taken together, some ingredients of an MEA-based maturity classifier have been reported separately: an interpretable machine-learning method validated on video features (Scheurer et al., 2025), MEA parameters that differ between the same maturation conditions (Li et al., 2025, whose B27 and maturation-medium groups Scheurer et al. follow), a reported link between FPD and contraction (Hayakawa et al., 2014), and evidence that maturation status matters for translation (Correia et al., 2024). — main.md:140
- [ ] (3) [Maturation] the authors do not propose these values as maturity markers.
    - > In Li et al. (2025), conduction velocity and spike amplitude rose from a standard B27 medium to a fatty-acid-enriched maturation medium, and further with nanopatterning and electrostimulation. — main.md:134
    - > Taken together, some ingredients of an MEA-based maturity classifier have been reported separately: an interpretable machine-learning method validated on video features (Scheurer et al., 2025), MEA parameters that differ between the same maturation conditions (Li et al., 2025, whose B27 and maturation-medium groups Scheurer et al. follow), a reported link between FPD and contraction (Hayakawa et al., 2014), and evidence that maturation status matters for translation (Correia et al., 2024). — main.md:140
- [ ] (4) [Maturation] the B27 and maturation-medium groups of Scheurer et al. (2025) follow this paper.
    - > In Li et al. (2025), conduction velocity and spike amplitude rose from a standard B27 medium to a fatty-acid-enriched maturation medium, and further with nanopatterning and electrostimulation. — main.md:134
    - > Taken together, some ingredients of an MEA-based maturity classifier have been reported separately: an interpretable machine-learning method validated on video features (Scheurer et al., 2025), MEA parameters that differ between the same maturation conditions (Li et al., 2025, whose B27 and maturation-medium groups Scheurer et al. follow), a reported link between FPD and contraction (Hayakawa et al., 2014), and evidence that maturation status matters for translation (Correia et al., 2024). — main.md:140
- [ ] (5) [Conclusion] cited for MEA parameters that differ between maturation conditions.
    - > Some ingredients for such a reference have been reported separately: an interpretable machine-learning approach validated on non-invasive beating features (Scheurer et al., 2025), MEA parameters that differ between maturation conditions (Li et al., 2025) and a reported link between field potential duration and contraction duration (Hayakawa et al., 2014); what is missing is an independent maturity measure taken on the same MEA cultures. — main.md:234
- [ ] (6) [Outlook] MEA data from the same maturation conditions that a video-based maturity classifier separates already exist.
    - > The hypothesis here is that interpreting them jointly (sensor fusion), with AI support, could give a more complete picture of a preparation than any single signal, for example by adding MEA-derived parameters to a video-based classifier of maturation status, for which MEA data from the same maturation conditions already exist (Li et al., 2025). — main.md:195

Pointers: (1) Supplementary Table 3 (mean ± SD, n = 24 cultures per group). (2) Supplementary Table 2 (INa, IK1, RMP, Vmax); patch clamp on single cells, MEA on replated monolayers. (4) Scheurer et al. (2025), reference [11], pp. 5–6; same group, matching media. (6) "the same conditions" means the culture conditions, not the same cultures; MEA recordings were made after replating on day 42 and 7 days of recovery, all groups in MM for one hour before recording.

## Lin et al. (2023)

Local file: `raw/lin-2023-nanoelectronics.pdf` (+ supplementary); page `wiki/papers/lin-2023-nanoelectronics.md`. Status: full text and supplement read at ingest 2026-10-30.

- [ ] (1) [Maturation, Conclusion] extracellular waveforms were ordered along an electrical-maturation trajectory by unsupervised machine learning (pseudotime).
    - > The closest step towards combining them is Lin et al. (2023), who ordered extracellular waveforms along an electrical-maturation trajectory by unsupervised machine learning (pseudotime). — main.md:140
    - > In one study, Fridericia-corrected FPD was similar in 2D monolayers and 3D tissue sheets (Maurissen et al., 2024), but in simulations the 3D geometry alone changed FP shape (Hwang et al., 2023), and conventional MEAs contact 3D tissue only on one surface (Lin et al., 2023). — main.md:233
    - > Unsupervised tracking of electrical maturation from extracellular waveforms has been shown with tissue-embedded electrodes in 3D microtissues (Lin et al., 2023), but no classifier or reference values have been reported for standard MEA recordings. — main.md:234
- [ ] (2) [Maturation, Conclusion] the recordings came from stretchable electrodes embedded in 3D microtissues, not from MEA plates.
    - > The closest step towards combining them is Lin et al. (2023), who ordered extracellular waveforms along an electrical-maturation trajectory by unsupervised machine learning (pseudotime). — main.md:140
    - > In one study, Fridericia-corrected FPD was similar in 2D monolayers and 3D tissue sheets (Maurissen et al., 2024), but in simulations the 3D geometry alone changed FP shape (Hwang et al., 2023), and conventional MEAs contact 3D tissue only on one surface (Lin et al., 2023). — main.md:233
    - > Unsupervised tracking of electrical maturation from extracellular waveforms has been shown with tissue-embedded electrodes in 3D microtissues (Lin et al., 2023), but no classifier or reference values have been reported for standard MEA recordings. — main.md:234
- [ ] (3) [Maturation] the features describe only the depolarization spike, not FPD.
    - > The closest step towards combining them is Lin et al. (2023), who ordered extracellular waveforms along an electrical-maturation trajectory by unsupervised machine learning (pseudotime). — main.md:140
- [ ] (4) [Maturation] no external maturity measure was taken on the same cultures.
    - > The closest step towards combining them is Lin et al. (2023), who ordered extracellular waveforms along an electrical-maturation trajectory by unsupervised machine learning (pseudotime). — main.md:140
- [ ] (5) [3D, Conclusion] the authors argue that conventional MEAs contact a 3D microtissue only at one surface and lose contact as the tissue contracts.
    - > The recording itself may also be limited: the authors of a study with tissue-embedded electrodes argue that conventional MEAs contact a 3D microtissue only at one surface and lose contact as the tissue contracts (Lin et al., 2023). — main.md:176
    - > In one study, Fridericia-corrected FPD was similar in 2D monolayers and 3D tissue sheets (Maurissen et al., 2024), but in simulations the 3D geometry alone changed FP shape (Hwang et al., 2023), and conventional MEAs contact 3D tissue only on one surface (Lin et al., 2023). — main.md:233
    - > Unsupervised tracking of electrical maturation from extracellular waveforms has been shown with tissue-embedded electrodes in 3D microtissues (Lin et al., 2023), but no classifier or reference values have been reported for standard MEA recordings. — main.md:234
- [ ] (6) [Outlook] whole extracellular waveforms have already been used as machine-learning input, in tissue-embedded recordings.
    - > If the cellular signal could be separated from it, as outlined next, that signal could be a useful input in its own right, beyond the parameters extracted from it; whole extracellular waveforms have already been used as machine-learning input, in tissue-embedded recordings (Lin et al., 2023). — main.md:197
- [ ] (7) [Limitations] example of evidence from tissue-embedded electrodes.
    - > Most methodological statements rest on one or two studies, and some rest on rat cells (Ernault et al., 2024), fetal mouse cells (Hu et al., 2026), simulations (Hwang et al., 2023; Botti et al., 2026), tissue-embedded electrodes (Lin et al., 2023) or modalities other than field potentials (Fetterman et al., 2024; Scheurer et al., 2025). — main.md:216

Pointers: (1)(6) Methods p. 14 (PHATE + Slingshot on all channel-averaged waveforms, default parameters), Fig. 4. (3) "spike duration" = time between maximum and minimum dV/dt (p. 14). (4) scRNA-seq on separate cocultures. (5) p. 2 and table S1.

## Mäki (2023, version v3)

Local file: `raw/maki-2023-opinion.html`; page `wiki/papers/maki-2023-opinion.md`; also `wiki/critical-assessment-maki-claims.md`. Status: claims on the conventions, thresholds and the Limitations sentence checked against the HTML 2026-10-24; the waveform-variation passage 2026-10-31. This is the author's own opinion paper.

- [ ] (1) [Scope] it serves as the evaluative anchor: reviewed studies are assessed against the methodological standards and physiological reasoning it articulates (the Abstract describes the same comparison without citing it by name).
    - > An opinion paper on FP signal analysis (Mäki, 2023), written by the present author, serves as an evaluative anchor: reviewed studies are assessed against the methodological standards and physiological reasoning it articulates. — main.md:52
- [ ] (2) [Timeline] "DatAnalyzer — MATLAB tool with morphology-aware FPD (own work; method in Mäki 2023, not peer reviewed)", 2022; the opinion paper has no timeline entry of its own (reworded 2026-11-05: release year 2022 and language MATLAB from the GitHub repository AnaHill/DatAnalyzer, created 2022-04-27, language MATLAB; not stated in the paper).
    - > : DatAnalyzer — MATLAB tool with morphology-aware FPD (own work; method in Mäki 2023, not peer reviewed) — main.md:64
- [ ] (3) [Motivation] it challenged the physiological validity of commonly used FP annotation conventions: the widely adopted peak-to-peak FPD definition is often mismatched to the underlying electrophysiology; the first positive peak in a propagating monolayer may reflect neighbouring cells; FPD end should be measured to the return of the signal to baseline.
    - > An opinion paper by the present author (Mäki, 2023) explicitly challenged the physiological validity of commonly used FP annotation conventions, arguing that the widely adopted peak-to-peak definition of FPD is often mismatched to the underlying electrophysiology of cardiomyocytes. — main.md:48
- [ ] (4) [Open pipelines, Table 1] DatAnalyzer, the author's own tool, released in 2022, MATLAB (reworded 2026-11-05: release year 2022 and language MATLAB from the GitHub repository AnaHill/DatAnalyzer, created 2022-04-27, language MATLAB; not stated in the paper); FPD end at baseline return; morphology-aware classification of three waveform types; inversion for only-high-peak signals (not independently validated).
    - > Cardio PyMEA, introduced in 2022, is the earliest of the open pipelines published since 2022 that are examined here, and DatAnalyzer, the author's own tool described in Mäki (2023), was released the same year. — main.md:87
    - > Year is the year of the describing publication; for DatAnalyzer it is the year of the first public release, the method being described in Mäki (2023).* — main.md:91
    - > | DatAnalyzer (Mäki, 2023; author's own tool, not peer reviewed) | 2022 | MATLAB | Baseline return | Morphology-aware classification (3 waveform types); inversion for only-high-peak signals (not independently validated) | — main.md:96
- [ ] (5) [Fiducial] it describes an algorithm: beat-aligned segmentation, averaging across beats, threshold-based identification of depolarization onset relative to FP amplitude, FPD end at the return of the signal toward baseline; it averages beats, but how the end point behaves at low signal-to-noise ratios or with baseline drift is not evaluated.
    - > The opinion paper by Mäki (2023) describes a concrete, algorithmic approach: beat-aligned segmentation followed by averaging across multiple beats to reduce noise, threshold-based identification of depolarization onset relative to FP amplitude, and definition of FPD end as the return of the signal toward baseline rather than the repolarization peak. — main.md:102
    - > - **DatAnalyzer**: from depolarization onset to baseline return (Mäki, 2023) — main.md:108
    - > The robustness of the baseline-return convention has not been examined in the studies reviewed here: Mäki (2023) averages beats to reduce noise, but how the end point behaves at low signal-to-noise ratios or with baseline drift is not evaluated. — main.md:110
- [ ] (6) [Fiducial, Table 2] DatAnalyzer FPD from depolarization onset (10 % threshold) to return within 10 % of baseline, intended to capture the full repolarization wave; the R-to-T-peak convention is described as common and criticised in this paper.
    - > The opinion paper by Mäki (2023) describes a concrete, algorithmic approach: beat-aligned segmentation followed by averaging across multiple beats to reduce noise, threshold-based identification of depolarization onset relative to FP amplitude, and definition of FPD end as the return of the signal toward baseline rather than the repolarization peak. — main.md:102
    - > - **DatAnalyzer**: from depolarization onset to baseline return (Mäki, 2023) — main.md:108
    - > The robustness of the baseline-return convention has not been examined in the studies reviewed here: Mäki (2023) averages beats to reduce noise, but how the end point behaves at low signal-to-noise ratios or with baseline drift is not evaluated. — main.md:110
    - > | R-to-T-peak | R peak (Hayakawa et al., 2014: initial negative peak) | T-wave peak | T-wave peak coincided with APD90 only for biphasic T waves (a minority morphology; NRVM, not hiPSC-CM; Ernault et al., 2024); in hiPSC-CMs, R-to-T-peak FPD correlated only minimally with APD50 and APD90 (Lee et al., 2024); the peak of the positive deflection appeared to match the upstroke of relaxation (Hayakawa et al., 2014) | Hayakawa et al., 2014; Lee et al., 2024; Weiser-Bitoun et al., 2026; described as a common convention and criticised in Mäki, 2023 | — main.md:116
    - > | Baseline return | Depolarization onset (10% threshold) | Signal return to within 10% of baseline | Intended to capture the full repolarization wave (Mäki, 2023); not compared with the AP; return to baseline appeared to match the peak of relaxation (Hayakawa et al., 2014) | Mäki, 2023 | — main.md:117
- [ ] (7) [Morphology] pacemaker-like signals lacking a high peak, single-peak and mixed or atypical morphologies are described; morphology-aware handling with waveform inversion for "only high peak" cases, internally validated but not independently replicated; Figure 2 shows the inversion branch as the author's own proposal and the baseline-return branch.
    - > Pacemaker-like signals lacking a pronounced high peak, waveforms dominated by a single peak, and mixed or atypical morphologies are described in hiPSC-CM cultures (Mäki, 2023), and hiPSC-CM preparations contain nodal-like cells (Park et al., 2026). — main.md:143
    - > The opinion paper (Mäki, 2023) explicitly addresses these cases by proposing morphology-aware handling strategies, including specialized interpretation of pacemaker-like signals and pragmatic preprocessing — such as waveform inversion for "only high peak" cases, an approach internally validated in that work but not yet independently replicated — prior to standard analysis. — main.md:145
    - > The signal-inversion branch is the author's own proposal (Mäki, 2023) and has not been independently validated.* — main.md:147
    - > J -->|Baseline return| L[Full repolarization Mäki, 2023] — main.md:163
    - > Such variation is not new: the opinion paper summarises large differences in FP signal forms and repolarization phases and cites earlier work explaining them by where the activity arises relative to the electrode and by overlapping signals in later cultures (Mäki, 2023). — main.md:171
    - > Nonetheless, fiducial definitions remain inconsistent across open platforms: PhysioMEA, for instance, defines FPD as the interval from the R-peak to the T-wave peak (Weiser-Bitoun et al., 2026) rather than the return to baseline (Mäki, 2023), and FPD values are therefore not directly comparable across tools without explicit knowledge of the underlying convention. — main.md:171
- [x] (8) [Morphology] waveform variation is not new: the paper summarises large differences in FP signal forms and repolarization phases and cites earlier work explaining them by where the activity arises relative to the electrode and by overlapping signals in later cultures.
    - > Pacemaker-like signals lacking a pronounced high peak, waveforms dominated by a single peak, and mixed or atypical morphologies are described in hiPSC-CM cultures (Mäki, 2023), and hiPSC-CM preparations contain nodal-like cells (Park et al., 2026). — main.md:143
    - > The opinion paper (Mäki, 2023) explicitly addresses these cases by proposing morphology-aware handling strategies, including specialized interpretation of pacemaker-like signals and pragmatic preprocessing — such as waveform inversion for "only high peak" cases, an approach internally validated in that work but not yet independently replicated — prior to standard analysis. — main.md:145
    - > The signal-inversion branch is the author's own proposal (Mäki, 2023) and has not been independently validated.* — main.md:147
    - > J -->|Baseline return| L[Full repolarization Mäki, 2023] — main.md:163
    - > Such variation is not new: the opinion paper summarises large differences in FP signal forms and repolarization phases and cites earlier work explaining them by where the activity arises relative to the electrode and by overlapping signals in later cultures (Mäki, 2023). — main.md:171
    - > Nonetheless, fiducial definitions remain inconsistent across open platforms: PhysioMEA, for instance, defines FPD as the interval from the R-peak to the T-wave peak (Weiser-Bitoun et al., 2026) rather than the return to baseline (Mäki, 2023), and FPD values are therefore not directly comparable across tools without explicit knowledge of the underlying convention. — main.md:171
- [ ] (9) [Morphology] PhysioMEA's R-to-T-peak FPD differs from the baseline return of this paper.
    - > Pacemaker-like signals lacking a pronounced high peak, waveforms dominated by a single peak, and mixed or atypical morphologies are described in hiPSC-CM cultures (Mäki, 2023), and hiPSC-CM preparations contain nodal-like cells (Park et al., 2026). — main.md:143
    - > The opinion paper (Mäki, 2023) explicitly addresses these cases by proposing morphology-aware handling strategies, including specialized interpretation of pacemaker-like signals and pragmatic preprocessing — such as waveform inversion for "only high peak" cases, an approach internally validated in that work but not yet independently replicated — prior to standard analysis. — main.md:145
    - > The signal-inversion branch is the author's own proposal (Mäki, 2023) and has not been independently validated.* — main.md:147
    - > J -->|Baseline return| L[Full repolarization Mäki, 2023] — main.md:163
    - > Such variation is not new: the opinion paper summarises large differences in FP signal forms and repolarization phases and cites earlier work explaining them by where the activity arises relative to the electrode and by overlapping signals in later cultures (Mäki, 2023). — main.md:171
    - > Nonetheless, fiducial definitions remain inconsistent across open platforms: PhysioMEA, for instance, defines FPD as the interval from the R-peak to the T-wave peak (Weiser-Bitoun et al., 2026) rather than the return to baseline (Mäki, 2023), and FPD values are therefore not directly comparable across tools without explicit knowledge of the underlying convention. — main.md:171
- [ ] (10) [3D] it cautions that analysis frameworks optimised for 2D monolayers may not transfer directly to 3D models.
    - > The opinion paper cautions that analysis frameworks optimised for 2D monolayers may not transfer to them directly (Mäki, 2023), and the studies examined give partial answers. — main.md:176
- [x] (11) [Outlook] the outlook builds on it: the doubt that machine learning on raw MEA signals would work, given how much FP amplitude, frequency and shape differ between cultures; the two-step approach (parameters from detected peaks, then machine learning); estimating and separating the recording-system contribution (see the references therein).
    - > Both are prospective views of the present author, build on the author's opinion paper (Mäki, 2023; see the references therein) and are not results of the studies reviewed; they should be read as hypotheses, not as findings. — main.md:191
    - > The proposal is not to feed raw MEA signals to a model, which the author has doubted would work given how much FP amplitude, frequency and shape differ between cultures (Mäki, 2023). — main.md:197
    - > It would then measure cell-level changes and drug responses more directly (Mäki, 2023; see the references therein). — main.md:201
- [ ] (12) [Limitations] not peer reviewed; inversion not independently replicated; its FPD-end convention is one of several (Table 2); the outlook builds on it.
    - > - (iv) The evaluative framework is the author's own opinion paper (Mäki, 2023), which is not peer reviewed. — main.md:218
    - > It states hypotheses of the author, builds on the author's own opinion paper (Mäki, 2023), and none of its proposals was tested in the studies examined. — main.md:221
- [x] (13) [Conclusion] analysis of inverted signals is an example of case-by-case morphology handling.
    - > In the studies examined, morphology handling is described case by case: analysis of inverted signals, exclusion of electrodes, or interpretation restricted to biphasic T waves (Mäki, 2023; Ernault et al., 2024; Weiser-Bitoun et al., 2026). — main.md:232
- [x] (14) [Declarations] competing-interest statement: the author wrote this paper and DatAnalyzer.
    - > The author wrote the opinion paper used here as the evaluative framework (Mäki, 2023) and the *DatAnalyzer* tool listed in Table 1, and therefore has an interest in how they are assessed. — main.md:244
    - > "Mäki (2023)" refers to the opinion paper whose first version was posted on Zenodo in 2023; the text assessed here is version v3 of the same record, published on 23 June 2026, which slightly updated the original text (mainly outlook). — main.md:246
- [ ] (15) [Declarations] version note: first version on Zenodo in 2023; the text assessed is v3 of the same record, published 23 June 2026.
    - > The author wrote the opinion paper used here as the evaluative framework (Mäki, 2023) and the *DatAnalyzer* tool listed in Table 1, and therefore has an interest in how they are assessed. — main.md:244
    - > "Mäki (2023)" refers to the opinion paper whose first version was posted on Zenodo in 2023; the text assessed here is version v3 of the same record, published on 23 June 2026, which slightly updated the original text (mainly outlook). — main.md:246

Pointers: (3)(6) the sections on FPD start and end; 10 % thresholds in the algorithm description (wiki page, steps 4 and 6). (8) section "Understanding FP signals": "measured FP-signals have large differences in i) amplitude ... ii) frequency ... iii) signal forms: "high and low peak" vs "only low peak", large differences in repolarization phases"; "FP-signals may overlap in recordings from later stages, resulting in complex mixed waveforms" (Meyer et al. 2004; Egert and Meyer 2005, not sources of this review). (10) its Limitations: the analysis "might not be as easily ... extrapolated to the 3D model". (15) Zenodo record 20807245 version list ("Version v3, 10.5281/zenodo.20807245, Jun 23, 2026").

## Matsuda et al. (2025)

Local file: `raw/matsuda-2025-uhd.pdf`; page `wiki/papers/matsuda-2025-uhd.md`. Status: checked against the abstract, the comparison with a conventional MEA and the discussion 2026-10-24.

- [ ] (1) [Timeline] "Ultra-high-density MEA field potential imaging" (reworded 2026-11-06: detail and abbreviations not needed for the argument removed).
    - > 2025 : Ultra-high-density MEA field potential imaging (Matsuda et al.) — main.md:73
- [ ] (2) [FPDc] its recordings were of spontaneous beating only, and the authors name the absence of pacing as a limitation.
    - > Matsuda et al. (2025), however, recorded spontaneous beating only and name the absence of pacing as a limitation, and the proposed acceptance standard is defined for spontaneously beating cells: more mature cells can beat with periods longer than its 3000 ms upper limit, which makes recordings impractically long, so pacing would probably be needed, a paced assay being left to a possible future standard (Clements et al., 2025). — main.md:123
- [ ] (3) [High-throughput] one of the two examples (with Altrocchi et al., 2023) of multi-parameter feature sets.
    - > In the studies examined, single conventional metrics are complemented by multi-parameter feature sets: beat rate, beat-to-beat variability, conduction properties and event-based descriptors (Altrocchi et al., 2023; Matsuda et al., 2025). — main.md:183
    - > Ultra-high-density MEA platforms with close to a quarter million electrodes give spatially resolved excitation origin counts, propagation area and conduction velocity maps, in addition to conventional endpoints such as beat rate and inter-beat interval (Matsuda et al., 2025). — main.md:185
- [ ] (4) [High-throughput] ultra-high-density MEA platforms (CMOS; dropped from the text 2026-11-06) with close to a quarter million electrodes give spatially resolved excitation origin counts, propagation area and conduction velocity maps, in addition to conventional endpoints such as beat rate and inter-beat interval.
    - > In the studies examined, single conventional metrics are complemented by multi-parameter feature sets: beat rate, beat-to-beat variability, conduction properties and event-based descriptors (Altrocchi et al., 2023; Matsuda et al., 2025). — main.md:183
    - > Ultra-high-density MEA platforms with close to a quarter million electrodes give spatially resolved excitation origin counts, propagation area and conduction velocity maps, in addition to conventional endpoints such as beat rate and inter-beat interval (Matsuda et al., 2025). — main.md:185
- [ ] (5) [High-throughput] doxorubicin-induced cardiotoxicity was detected at lower concentrations than reported in earlier studies (0.03 µM within 24 h, 10-fold lower; numbers dropped from the text 2026-11-06).
    - > In the studies examined, single conventional metrics are complemented by multi-parameter feature sets: beat rate, beat-to-beat variability, conduction properties and event-based descriptors (Altrocchi et al., 2023; Matsuda et al., 2025). — main.md:183
    - > Ultra-high-density MEA platforms with close to a quarter million electrodes give spatially resolved excitation origin counts, propagation area and conduction velocity maps, in addition to conventional endpoints such as beat rate and inter-beat interval (Matsuda et al., 2025). — main.md:185

Pointers: (4) abstract p. 1 (236,880 electrodes, 5.9 × 5.5 mm); the paper reports no FPD or FPDc for its own recordings. (5) p. 15 ("detected doxorubicin-induced cardiotoxicity at a 10-fold lower concentration (0.03 µM) and within a shorter time frame (24 h)" than prior studies, >0.3 µM). (2) p. 15 (stimulation upgrade under way).

## Maurissen et al. (2024)

Local file: `raw/maurissen-2024-mutation.pdf`; page `wiki/papers/maurissen-2024-mutation.md`. Status: checked against the abstract and Results 2026-10-24.

- [ ] (1) [Timeline] "KCNH2 mutation phenotyping in 3D tissues".
    - > : KCNH2 mutation phenotyping in 3D tissues (Maurissen et al.) — main.md:70
- [ ] (2) [Motivation] example of mechanistic electrophysiological phenotyping.
    - > In the studies examined, multielectrode array (MEA) recordings from human induced pluripotent stem cell–derived cardiomyocytes (hiPSC-CMs) are used not only for basic measurements such as beating rate and field potential duration (FPD), but also for mechanistic electrophysiological phenotyping (Maurissen et al., 2024; Park et al., 2025; Park et al., 2026), proarrhythmia risk assessment (Blinova et al., 2018; Pramudito et al., 2026), chronic drug testing (Altrocchi et al., 2023) and recordings repeated over days in culture (Guerrelli et al., 2024). — main.md:46
- [ ] (3) [FPDc] the study uses Fridericia-corrected FPD.
    - > By analogy with the clinical QT interval, the Fridericia formula ($FPDc = FPD/RR^{0.33}$, where RR is the interval between beats) is the correction used in the studies examined here that report rate-corrected FPD (Altrocchi et al., 2023; Hwang et al., 2023; Maurissen et al., 2024; Park et al., 2026); Park et al. (2025) also report corrected FPD but do not name the formula. — main.md:121
- [ ] (4) [3D] gene-edited long QT and short QT KCNH2 lines (N588D and N588K; codes dropped from the text 2026-11-06) were recorded both as 2D monolayers and as 3D cardiac tissue sheets on MEAs.
    - > Maurissen et al. (2024) recorded gene-edited long QT and short QT *KCNH2* lines both as 2D monolayers and as 3D cardiac tissue sheets on MEAs. — main.md:176
- [ ] (5) [3D, Conclusion] Fridericia-corrected FPD was close in the two formats for both mutant lines and the isogenic control (reworded 2026-11-06 from "all three genotypes").
    - > Maurissen et al. (2024) recorded gene-edited long QT and short QT *KCNH2* lines both as 2D monolayers and as 3D cardiac tissue sheets on MEAs. — main.md:176
    - > In one study, Fridericia-corrected FPD was similar in 2D monolayers and 3D tissue sheets (Maurissen et al., 2024), but in simulations the 3D geometry alone changed FP shape (Hwang et al., 2023), and conventional MEAs contact 3D tissue only on one surface (Lin et al., 2023). — main.md:233
- [ ] (6) [3D] TdP- and VT-like waveforms with E-4031 were reported in the 3D sheets, which the authors, citing their earlier work, consider necessary for inducing them; the same conditions were not tested in 2D; the cardiomyocyte purity of the sheets was 25–41 %.
    - > Maurissen et al. (2024) recorded gene-edited long QT and short QT *KCNH2* lines both as 2D monolayers and as 3D cardiac tissue sheets on MEAs. — main.md:176

Pointers: (3)(5) p. 3 (FPDcF; 2D 231/82/323 ms, 3D 225/87/320 ms for parent/SQT/LQT, wiki page Findings). (6) wiki page Findings and Limitations (cTnT purity 25–41 %).

## Park et al. (2025)

Local file: `raw/park-2025-cardiotoxicity.pdf`; page `wiki/papers/park-2025-cardiotoxicity.md`. Status: checked against the abstract and Methods 2026-10-24.

- [ ] (1) [Timeline] "Healthy vs. long QT hiPSC-CM CiPA drug comparison" (2025; LQTS spelled out 2026-11-06).
    - > : Healthy vs. long QT hiPSC-CM CiPA drug comparison (Park et al.) — main.md:74
- [ ] (2) [Intro] cited, with Blinova et al. (2018) and Altrocchi et al. (2023), for MEA use in cardiac safety pharmacology, drug discovery and disease modelling, and, with Blinova, for FPD metrics being integral to CiPA.
    - > Multielectrode arrays (MEAs) recording extracellular field potentials (FPs) from human induced pluripotent stem cell–derived cardiomyocytes (hiPSC-CMs) are widely used in cardiac safety pharmacology, drug discovery, and disease modelling (Blinova et al., 2018; Altrocchi et al., 2023; Park et al., 2025). — main.md:43
    - > The field potential duration (FPD) and related metrics serve as surrogates for repolarization and are integral to initiatives such as the Comprehensive in Vitro Proarrhythmia Assay (CiPA) (Blinova et al., 2018; Park et al., 2025). — main.md:43
- [ ] (3) [Motivation] example of mechanistic electrophysiological phenotyping.
    - > In the studies examined, multielectrode array (MEA) recordings from human induced pluripotent stem cell–derived cardiomyocytes (hiPSC-CMs) are used not only for basic measurements such as beating rate and field potential duration (FPD), but also for mechanistic electrophysiological phenotyping (Maurissen et al., 2024; Park et al., 2025; Park et al., 2026), proarrhythmia risk assessment (Blinova et al., 2018; Pramudito et al., 2026), chronic drug testing (Altrocchi et al., 2023) and recordings repeated over days in culture (Guerrelli et al., 2024). — main.md:46
- [ ] (4) [Open pipelines] the recordings were analysed with the vendor's Cardiac Analysis Tool.
    - > The studies examined here do not show that this has displaced vendor software: the studies of Park et al. (2025) and Park et al. (2026), for example, analysed their recordings with the vendor's Cardiac Analysis Tool, and no usage data are available to estimate adoption of the open tools. — main.md:89
- [ ] (5) [FPDc] it reports corrected FPD but does not name the formula.
    - > By analogy with the clinical QT interval, the Fridericia formula ($FPDc = FPD/RR^{0.33}$, where RR is the interval between beats) is the correction used in the studies examined here that report rate-corrected FPD (Altrocchi et al., 2023; Hwang et al., 2023; Maurissen et al., 2024; Park et al., 2026); Park et al. (2025) also report corrected FPD but do not name the formula. — main.md:121
    - > The latter shares its group, platform and apparently a long QT line with Park et al. (2025), so the two are better read as one body of evidence than as independent replication, and its two Brugada lines consisted largely of atrial-like cells, so their comparison with ventricular-like normal lines is confounded by cell identity. — main.md:125
- [ ] (6) [FPDc] Park et al. (2026) share its group, platform and apparently a long QT line, so the two are one body of evidence rather than independent replication.
    - > By analogy with the clinical QT interval, the Fridericia formula ($FPDc = FPD/RR^{0.33}$, where RR is the interval between beats) is the correction used in the studies examined here that report rate-corrected FPD (Altrocchi et al., 2023; Hwang et al., 2023; Maurissen et al., 2024; Park et al., 2026); Park et al. (2025) also report corrected FPD but do not name the formula. — main.md:121
    - > The latter shares its group, platform and apparently a long QT line with Park et al. (2025), so the two are better read as one body of evidence than as independent replication, and its two Brugada lines consisted largely of atrial-like cells, so their comparison with ventricular-like normal lines is confounded by cell identity. — main.md:125
- [ ] (7) [High-throughput] eight arrhythmia-inducing drugs were compared on healthy and long QT syndrome–derived lines, with disease-specific drug sensitivities.
    - > Disease-line screening is another application: Park et al. (2025) compared eight arrhythmia-inducing drugs on healthy and long QT syndrome–derived hiPSC-CM lines, and the same group later tested 28 compounds on patient-derived long QT and Brugada syndrome lines (Park et al., 2026). — main.md:181

Pointers: (4)(5) p. 4, p. 7–11 ("corrected FPD (FPDc)", "Axion's Cardiac Analysis Software"; Fridericia not mentioned). (2) p. 2 (CiPA "facilitated the use of hiPSC-CMs") and p. 4 (protocol "in line with the CiPA core protocol"). (7) abstract p. 1.

## Park et al. (2026)

Local files: `raw/park-2026-genotype-ml.pdf` (+ supplementary methods and Data set S1); page `wiki/papers/park-2026-genotype-ml.md`. Status: checked (full text, supplementary, all eight figures) 2026-10-18. Reference year 2026 (volume 82; online July 2025).

- [ ] (1) [Motivation] example of mechanistic electrophysiological phenotyping.
    - > In the studies examined, multielectrode array (MEA) recordings from human induced pluripotent stem cell–derived cardiomyocytes (hiPSC-CMs) are used not only for basic measurements such as beating rate and field potential duration (FPD), but also for mechanistic electrophysiological phenotyping (Maurissen et al., 2024; Park et al., 2025; Park et al., 2026), proarrhythmia risk assessment (Blinova et al., 2018; Pramudito et al., 2026), chronic drug testing (Altrocchi et al., 2023) and recordings repeated over days in culture (Guerrelli et al., 2024). — main.md:46
- [ ] (2) [Open pipelines] the recordings were analysed with the vendor's Cardiac Analysis Tool.
    - > The studies examined here do not show that this has displaced vendor software: the studies of Park et al. (2025) and Park et al. (2026), for example, analysed their recordings with the vendor's Cardiac Analysis Tool, and no usage data are available to estimate adoption of the open tools. — main.md:89
- [ ] (3) [FPDc] the study uses Fridericia-corrected FPD.
    - > By analogy with the clinical QT interval, the Fridericia formula ($FPDc = FPD/RR^{0.33}$, where RR is the interval between beats) is the correction used in the studies examined here that report rate-corrected FPD (Altrocchi et al., 2023; Hwang et al., 2023; Maurissen et al., 2024; Park et al., 2026); Park et al. (2025) also report corrected FPD but do not name the formula. — main.md:121
    - > A stacking ensemble of several classifiers outperformed each of its constituent classifiers in predicting torsades de pointes (TdP) risk on 16 held-out CiPA reference compounds (Pramudito et al., 2026), and a patient-line study trained machine-learning classifiers on Fridericia-corrected FPDc and other MEA parameters from long QT and Brugada syndrome lines (Park et al., 2026). — main.md:125
- [ ] (4) [FPDc] it trained machine-learning classifiers on Fridericia-corrected FPDc and other MEA parameters from long QT and Brugada syndrome lines; it took the rate correction as given and did not test how the choice of correction affects classifier performance.
    - > By analogy with the clinical QT interval, the Fridericia formula ($FPDc = FPD/RR^{0.33}$, where RR is the interval between beats) is the correction used in the studies examined here that report rate-corrected FPD (Altrocchi et al., 2023; Hwang et al., 2023; Maurissen et al., 2024; Park et al., 2026); Park et al. (2025) also report corrected FPD but do not name the formula. — main.md:121
    - > A stacking ensemble of several classifiers outperformed each of its constituent classifiers in predicting torsades de pointes (TdP) risk on 16 held-out CiPA reference compounds (Pramudito et al., 2026), and a patient-line study trained machine-learning classifiers on Fridericia-corrected FPDc and other MEA parameters from long QT and Brugada syndrome lines (Park et al., 2026). — main.md:125
- [ ] (5) [FPDc] it shares its group, platform and apparently a long QT line (KCNH2 c.453delC) with Park et al. (2025).
    - > By analogy with the clinical QT interval, the Fridericia formula ($FPDc = FPD/RR^{0.33}$, where RR is the interval between beats) is the correction used in the studies examined here that report rate-corrected FPD (Altrocchi et al., 2023; Hwang et al., 2023; Maurissen et al., 2024; Park et al., 2026); Park et al. (2025) also report corrected FPD but do not name the formula. — main.md:121
    - > A stacking ensemble of several classifiers outperformed each of its constituent classifiers in predicting torsades de pointes (TdP) risk on 16 held-out CiPA reference compounds (Pramudito et al., 2026), and a patient-line study trained machine-learning classifiers on Fridericia-corrected FPDc and other MEA parameters from long QT and Brugada syndrome lines (Park et al., 2026). — main.md:125
- [ ] (6) [FPDc] its two Brugada lines consisted largely of atrial-like cells (100 % and 87.5 %), so their comparison with ventricular-like normal lines is confounded by cell identity.
    - > By analogy with the clinical QT interval, the Fridericia formula ($FPDc = FPD/RR^{0.33}$, where RR is the interval between beats) is the correction used in the studies examined here that report rate-corrected FPD (Altrocchi et al., 2023; Hwang et al., 2023; Maurissen et al., 2024; Park et al., 2026); Park et al. (2025) also report corrected FPD but do not name the formula. — main.md:121
    - > A stacking ensemble of several classifiers outperformed each of its constituent classifiers in predicting torsades de pointes (TdP) risk on 16 held-out CiPA reference compounds (Pramudito et al., 2026), and a patient-line study trained machine-learning classifiers on Fridericia-corrected FPDc and other MEA parameters from long QT and Brugada syndrome lines (Park et al., 2026). — main.md:125
- [ ] (7) [FPDc] it evaluated on a small test set (15 drugs) by repeated resampling.
    - > By analogy with the clinical QT interval, the Fridericia formula ($FPDc = FPD/RR^{0.33}$, where RR is the interval between beats) is the correction used in the studies examined here that report rate-corrected FPD (Altrocchi et al., 2023; Hwang et al., 2023; Maurissen et al., 2024; Park et al., 2026); Park et al. (2025) also report corrected FPD but do not name the formula. — main.md:121
    - > A stacking ensemble of several classifiers outperformed each of its constituent classifiers in predicting torsades de pointes (TdP) risk on 16 held-out CiPA reference compounds (Pramudito et al., 2026), and a patient-line study trained machine-learning classifiers on Fridericia-corrected FPDc and other MEA parameters from long QT and Brugada syndrome lines (Park et al., 2026). — main.md:125
- [ ] (8) [Maturation] patch-clamp data show ventricular-, atrial- and nodal-like subtypes in its lines.
    - > Whether ventricular-, atrial- and nodal-like cells form distinct subpopulations within one preparation is debated (Ismaili et al., 2023), but patch-clamp data show such subtypes in the lines of Park et al. (2026). — main.md:128
- [ ] (9) [Morphology] hiPSC-CM preparations contain nodal-like cells.
    - > Pacemaker-like signals lacking a pronounced high peak, waveforms dominated by a single peak, and mixed or atypical morphologies are described in hiPSC-CM cultures (Mäki, 2023), and hiPSC-CM preparations contain nodal-like cells (Park et al., 2026). — main.md:143
- [ ] (10) [High-throughput] the same group tested 28 compounds on patient-derived long QT and Brugada syndrome lines, with disease-specific drug sensitivities.
    - > Disease-line screening is another application: Park et al. (2025) compared eight arrhythmia-inducing drugs on healthy and long QT syndrome–derived hiPSC-CM lines, and the same group later tested 28 compounds on patient-derived long QT and Brugada syndrome lines (Park et al., 2026). — main.md:181
- [ ] (11) [Outlook] its machine-learning classifiers were trained on a small dataset.
    - > A further caution is that machine-learning classifiers in the studies examined were trained on small datasets (Scheurer et al., 2025; Park et al., 2026; Pramudito et al., 2026). — main.md:197
- [ ] (12) [Conclusion] genotype-specific risk models are one of the machine-learning uses in the studies examined.
    - > Looking forward, machine learning is used in several of the studies examined — from ensemble classifiers for TdP risk prediction (Pramudito et al., 2026) and genotype-specific risk models (Park et al., 2026) to automated feature ranking in an open platform (Lee et al., 2024) — and it may become a more integral layer of cardiomyocyte MEA workflows. — main.md:236

Pointers: (6)(8) Figure 3 (patch-clamp subtype classification; normal lines about 70 % ventricular-, 20 % atrial- and 9 % nodal-like). (7) Figure 6–7 (11 training and 15 test drugs; 10,000 resamplings).

## Pramudito et al. (2026)

Local file: `raw/pramudito-2026-ensemble.pdf` (git-ignored); page `wiki/papers/pramudito-2026-ensemble.md`. Status: checked (full text and figures) 2026-10-18.

- [ ] (1) [Timeline, Conclusion] "Stacking ensemble machine learning for TdP risk prediction" (ML spelled out 2026-11-06); the Conclusion's "ensemble classifiers for TdP risk prediction".
    - > : Stacking ensemble machine learning for TdP risk prediction (Pramudito et al.) — main.md:80
    - > Looking forward, machine learning is used in several of the studies examined — from ensemble classifiers for TdP risk prediction (Pramudito et al., 2026) and genotype-specific risk models (Park et al., 2026) to automated feature ranking in an open platform (Lee et al., 2024) — and it may become a more integral layer of cardiomyocyte MEA workflows. — main.md:236
- [ ] (2) [Motivation] example of proarrhythmia risk assessment.
    - > In the studies examined, multielectrode array (MEA) recordings from human induced pluripotent stem cell–derived cardiomyocytes (hiPSC-CMs) are used not only for basic measurements such as beating rate and field potential duration (FPD), but also for mechanistic electrophysiological phenotyping (Maurissen et al., 2024; Park et al., 2025; Park et al., 2026), proarrhythmia risk assessment (Blinova et al., 2018; Pramudito et al., 2026), chronic drug testing (Altrocchi et al., 2023) and recordings repeated over days in culture (Guerrelli et al., 2024). — main.md:46
- [ ] (3) [FPDc] a stacking ensemble of several classifiers outperformed each of its constituent classifiers in predicting TdP risk on 16 held-out CiPA reference compounds.
    - > A stacking ensemble of several classifiers outperformed each of its constituent classifiers in predicting torsades de pointes (TdP) risk on 16 held-out CiPA reference compounds (Pramudito et al., 2026), and a patient-line study trained machine-learning classifiers on Fridericia-corrected FPDc and other MEA parameters from long QT and Brugada syndrome lines (Park et al., 2026). — main.md:125
    - > Both machine-learning studies took the rate correction as given: Pramudito et al. (2026) used ΔFPDc values already corrected in the multisite CiPA dataset, and neither tested how the choice of correction affects classifier performance. — main.md:125
- [ ] (4) [FPDc] it used ΔFPDc values already corrected in the multisite CiPA dataset and did not test how the correction affects performance.
    - > A stacking ensemble of several classifiers outperformed each of its constituent classifiers in predicting torsades de pointes (TdP) risk on 16 held-out CiPA reference compounds (Pramudito et al., 2026), and a patient-line study trained machine-learning classifiers on Fridericia-corrected FPDc and other MEA parameters from long QT and Brugada syndrome lines (Park et al., 2026). — main.md:125
    - > Both machine-learning studies took the rate correction as given: Pramudito et al. (2026) used ΔFPDc values already corrected in the multisite CiPA dataset, and neither tested how the choice of correction affects classifier performance. — main.md:125
- [ ] (5) [FPDc] it evaluated on a small test set (16 drugs) by repeated resampling.
    - > A stacking ensemble of several classifiers outperformed each of its constituent classifiers in predicting torsades de pointes (TdP) risk on 16 held-out CiPA reference compounds (Pramudito et al., 2026), and a patient-line study trained machine-learning classifiers on Fridericia-corrected FPDc and other MEA parameters from long QT and Brugada syndrome lines (Park et al., 2026). — main.md:125
    - > Both machine-learning studies took the rate correction as given: Pramudito et al. (2026) used ΔFPDc values already corrected in the multisite CiPA dataset, and neither tested how the choice of correction affects classifier performance. — main.md:125
- [ ] (6) [Outlook] its classifiers were trained on a small dataset.
    - > A further caution is that machine-learning classifiers in the studies examined were trained on small datasets (Scheurer et al., 2025; Park et al., 2026; Pramudito et al., 2026). — main.md:197

Pointers: Tables 3 and 4 (single versus stacked classifiers); Datasets and Methods sections (pre-corrected ΔFPDc from Blinova et al., 2018; 12 training and 16 test drugs; 10,000 resamplings).

## Ryynänen et al. (2018)

Local file: `raw/ryynanen-2018-single-cell-mea.pdf`; page `wiki/papers/ryynanen-2018-single-cell-mea.md`. Status: checked against the full text 2026-10-25 (text extraction; figures not viewed; supplementary videos not available). The researcher is not an author.

- [ ] (1) [FPDc] an exception to Fridericia: this pre-2022 single-cell study corrected FPD with Bazett's formula.
    - > An exception is the pre-2022 single-cell study of Ryynänen et al. (2018), which corrected FPD with Bazett's formula. — main.md:121
- [ ] (2) [Outlook] an MEA with transparent electrodes was used to record the field potential and the video-based motion of the same single hPS-CM at the same time, although the two recordings were not automatically synchronised.
    - > Video-based beating features have also been classified with an interpretable machine-learning model, although without MEA data (Scheurer et al., 2025), and an MEA with transparent electrodes has been used to record the field potential and the video-based motion of the same single human pluripotent stem cell–derived cardiomyocyte at the same time, although the two recordings were not automatically synchronised (Ryynänen et al., 2018). — main.md:193
- [ ] (3) [Limitations] pre-2022 work cited as background.
    - > - (vi) A few works from before 2022, such as Blinova et al. (2018), Hayakawa et al. (2014) and Ryynänen et al. (2018), are cited only as background for conventions, datasets and earlier multimodal work. — main.md:220
- [ ] (4) [Declarations] several of its authors are colleagues of the researcher from the Centre of Excellence in Body-on-Chip Research (CoEBoC) collaboration at Tampere University; the researcher is not an author.
    - > Several authors of the review Vuorenpää et al. (2023) and of Ryynänen et al. (2018), both cited in this review, are colleagues of the author from the Centre of Excellence in Body-on-Chip Research ([CoEBoC](https://research.tuni.fi/coeboc/)) research collaboration at Tampere University; the author is not an author of either. — main.md:244

Pointers: (1) p. 4 ("Bazett's formula was used to calculate the beat-rate-corrected FPD (cFPD)"). (2) pp. 2–3 (aim), p. 5 ("the recordings were not automatically synchronized in this study"), p. 7.

## Scheurer et al. (2025)

Local files: `raw/scheurer-2025-optical-ai.pdf` (+ supplementary, not read); page `wiki/papers/scheurer-2025-optical-ai.md`. Status: checked against the abstract, Results and Discussion 2026-10-24.

- [x] (1) [Timeline] "Video-based interpretable-AI maturity classifier".
    - > : Video-based interpretable-AI maturity classifier (Scheurer et al.) — main.md:75
- [ ] (2) [Maturation] hiPSC-CMs retain a fetal-like phenotype (cited with Correia et al., 2024).
    - > Maturation adds a further complication for comparisons between studies, distinct from but interacting with rate correction. hiPSC-CMs are electrophysiologically immature compared with adult cardiomyocytes and retain a fetal-like phenotype (Correia et al., 2024; Scheurer et al., 2025). — main.md:128
    - > Scheurer et al. (2025) showed that an interpretable machine-learning classifier can separate immature (day 21) from more mature (day 42, maturation medium) hiPSC-CM cultures with 99.5% accuracy on a hold-out test set of 46 videos. — main.md:138
    - > Scheurer et al. also cite earlier evidence linking field potential duration to contraction duration; in that work, the two were linearly related across drug concentrations under non-arrhythmic conditions, with a different slope for each drug (Hayakawa et al., 2014). — main.md:138
    - > Taken together, some ingredients of an MEA-based maturity classifier have been reported separately: an interpretable machine-learning method validated on video features (Scheurer et al., 2025), MEA parameters that differ between the same maturation conditions (Li et al., 2025, whose B27 and maturation-medium groups Scheurer et al. follow), a reported link between FPD and contraction (Hayakawa et al., 2014), and evidence that maturation status matters for translation (Correia et al., 2024). — main.md:140
- [ ] (3) [Maturation] an interpretable machine-learning classifier separated immature (day 21) from more mature (day 42, maturation medium) iPSC-CM cultures with 99.5 % accuracy on a hold-out test set of 46 videos, using only non-invasive, video-based beating features.
    - > Maturation adds a further complication for comparisons between studies, distinct from but interacting with rate correction. hiPSC-CMs are electrophysiologically immature compared with adult cardiomyocytes and retain a fetal-like phenotype (Correia et al., 2024; Scheurer et al., 2025). — main.md:128
    - > Scheurer et al. (2025) showed that an interpretable machine-learning classifier can separate immature (day 21) from more mature (day 42, maturation medium) hiPSC-CM cultures with 99.5% accuracy on a hold-out test set of 46 videos. — main.md:138
    - > Scheurer et al. also cite earlier evidence linking field potential duration to contraction duration; in that work, the two were linearly related across drug concentrations under non-arrhythmic conditions, with a different slope for each drug (Hayakawa et al., 2014). — main.md:138
    - > Taken together, some ingredients of an MEA-based maturity classifier have been reported separately: an interpretable machine-learning method validated on video features (Scheurer et al., 2025), MEA parameters that differ between the same maturation conditions (Li et al., 2025, whose B27 and maturation-medium groups Scheurer et al. follow), a reported link between FPD and contraction (Hayakawa et al., 2014), and evidence that maturation status matters for translation (Correia et al., 2024). — main.md:140
- [ ] (4) [Maturation] it cites earlier evidence linking field potential duration to contraction duration (Hayakawa et al.).
    - > Maturation adds a further complication for comparisons between studies, distinct from but interacting with rate correction. hiPSC-CMs are electrophysiologically immature compared with adult cardiomyocytes and retain a fetal-like phenotype (Correia et al., 2024; Scheurer et al., 2025). — main.md:128
    - > Scheurer et al. (2025) showed that an interpretable machine-learning classifier can separate immature (day 21) from more mature (day 42, maturation medium) hiPSC-CM cultures with 99.5% accuracy on a hold-out test set of 46 videos. — main.md:138
    - > Scheurer et al. also cite earlier evidence linking field potential duration to contraction duration; in that work, the two were linearly related across drug concentrations under non-arrhythmic conditions, with a different slope for each drug (Hayakawa et al., 2014). — main.md:138
    - > Taken together, some ingredients of an MEA-based maturity classifier have been reported separately: an interpretable machine-learning method validated on video features (Scheurer et al., 2025), MEA parameters that differ between the same maturation conditions (Li et al., 2025, whose B27 and maturation-medium groups Scheurer et al. follow), a reported link between FPD and contraction (Hayakawa et al., 2014), and evidence that maturation status matters for translation (Correia et al., 2024). — main.md:140
- [ ] (5) [Maturation, Conclusion] an interpretable machine-learning method validated on video features, as one component of an MEA-based maturity classifier; its groups follow Li et al. (2025).
    - > Maturation adds a further complication for comparisons between studies, distinct from but interacting with rate correction. hiPSC-CMs are electrophysiologically immature compared with adult cardiomyocytes and retain a fetal-like phenotype (Correia et al., 2024; Scheurer et al., 2025). — main.md:128
    - > Scheurer et al. (2025) showed that an interpretable machine-learning classifier can separate immature (day 21) from more mature (day 42, maturation medium) hiPSC-CM cultures with 99.5% accuracy on a hold-out test set of 46 videos. — main.md:138
    - > Scheurer et al. also cite earlier evidence linking field potential duration to contraction duration; in that work, the two were linearly related across drug concentrations under non-arrhythmic conditions, with a different slope for each drug (Hayakawa et al., 2014). — main.md:138
    - > Taken together, some ingredients of an MEA-based maturity classifier have been reported separately: an interpretable machine-learning method validated on video features (Scheurer et al., 2025), MEA parameters that differ between the same maturation conditions (Li et al., 2025, whose B27 and maturation-medium groups Scheurer et al. follow), a reported link between FPD and contraction (Hayakawa et al., 2014), and evidence that maturation status matters for translation (Correia et al., 2024). — main.md:140
    - > Some ingredients for such a reference have been reported separately: an interpretable machine-learning approach validated on non-invasive beating features (Scheurer et al., 2025), MEA parameters that differ between maturation conditions (Li et al., 2025) and a reported link between field potential duration and contraction duration (Hayakawa et al., 2014); what is missing is an independent maturity measure taken on the same MEA cultures. — main.md:234
- [ ] (6) [Outlook] video-based beating features were classified with an interpretable machine-learning model without MEA data; its classifier was trained on a small dataset.
    - > Video-based beating features have also been classified with an interpretable machine-learning model, although without MEA data (Scheurer et al., 2025), and an MEA with transparent electrodes has been used to record the field potential and the video-based motion of the same single human pluripotent stem cell–derived cardiomyocyte at the same time, although the two recordings were not automatically synchronised (Ryynänen et al., 2018). — main.md:193
    - > A further caution is that machine-learning classifiers in the studies examined were trained on small datasets (Scheurer et al., 2025; Park et al., 2026; Pramudito et al., 2026). — main.md:197
- [ ] (7) [Limitations] example of a modality other than field potentials (was "non-MEA modalities" until 2026-11-05; video-based analysis, no FPs).
    - > Most methodological statements rest on one or two studies, and some rest on rat cells (Ernault et al., 2024), fetal mouse cells (Hu et al., 2026), simulations (Hwang et al., 2023; Botti et al., 2026), tissue-embedded electrodes (Lin et al., 2023) or modalities other than field potentials (Fetterman et al., 2024; Scheurer et al., 2025). — main.md:216

Pointers: (3) abstract p. 1 (230 videos, 10 features, accuracy 99.5 ± 1.1 %); p. 5 table (test set n = 46). (4) p. 9 ("Hayakawa et al. simultaneously measured field potentials and motion in iPSC-CMs and observed strong correlations between field potential duration (FPD) and contraction duration"). (5) reference [11], pp. 5–6.

## Vuorenpää et al. (2023)

Local file: `raw/vuorenpaa-2023-mps-building-blocks.pdf`; page `wiki/papers/vuorenpaa-2023-mps-building-blocks.md`. Status: checked against the full text 2026-10-24 (text extraction; figures and tables not viewed). Two of the authors are colleagues of the researcher from CoEBoC; disclosed in the Declarations.

- [ ] (1) [Motivation] the review describes the parametrization of action potentials and field potentials as well established and as enabling clear comparison of results between studies.
    - > The studies reviewed below show that conventions differ and that FPD does not always track the action potential, but none of them measures how much variability analysis methods cause, and a review of cardiac microphysiological systems describes the parametrization of action potentials and field potentials as well established and as enabling clear comparison of results between studies (Vuorenpää et al., 2023). — main.md:46
- [ ] (2) [Outlook] it sees potential in combining different measurement modalities, which heart-on-chip systems can monitor concurrently.
    - > A review of cardiac microphysiological systems also sees potential in combining different measurement modalities, which heart-on-chip systems can monitor concurrently (Vuorenpää et al., 2023). — main.md:195
    - > The review of cardiac microphysiological systems cited above notes that continuous, multimodal measurements give a holistic data set for parameterising and validating computational models and that, to its authors' knowledge, integrative simulations of all building blocks of a microphysiological system had not been published (Vuorenpää et al., 2023). — main.md:207
- [ ] (3) [Outlook] it notes that continuous, multimodal measurements give a holistic data set for parameterising and validating computational models, and that, to its authors' knowledge, integrative simulations of all building blocks of a microphysiological system had not been published.
    - > A review of cardiac microphysiological systems also sees potential in combining different measurement modalities, which heart-on-chip systems can monitor concurrently (Vuorenpää et al., 2023). — main.md:195
    - > The review of cardiac microphysiological systems cited above notes that continuous, multimodal measurements give a holistic data set for parameterising and validating computational models and that, to its authors' knowledge, integrative simulations of all building blocks of a microphysiological system had not been published (Vuorenpää et al., 2023). — main.md:207
- [ ] (4) [Declarations] several of its authors are colleagues of the researcher from CoEBoC at Tampere University; the researcher is not an author (Declarations: "both cited in this review", generalised 2026-11-01).
    - > Several authors of the review Vuorenpää et al. (2023) and of Ryynänen et al. (2018), both cited in this review, are colleagues of the author from the Centre of Excellence in Body-on-Chip Research ([CoEBoC](https://research.tuni.fi/coeboc/)) research collaboration at Tampere University; the author is not an author of either. — main.md:244

Pointers: (1) section 6.1.1 ("The parametrization of APs and field potentials has been well established, enabling clear comparison of results between studies"). (2) section 6.1 (p. 12–13). (3) section 7 (p. 20) and 7.3 (p. 21, "To our knowledge, multiphysics models that would put together all the building blocks of MPS in integrative simulations have not yet been published"). The text contains no machine learning or digital twin discussion.

## Weiser-Bitoun et al. (2026)

Local file: `raw/weiser-bitoun-2026-physiomea.pdf`; page `wiki/papers/weiser-bitoun-2026-physiomea.md`. Status: checked against the abstract, Methods and Discussion 2026-10-24.

- [ ] (1) [Timeline] "PhysioMEA — cardiac organoid beat rate variability and 2D heatmaps" (reworded 2026-11-06: detail and abbreviations not needed for the argument removed).
    - > : PhysioMEA — cardiac organoid beat rate variability and 2D heatmaps (Weiser-Bitoun et al.) — main.md:78
- [ ] (2) [Open pipelines] one of the new open tools built for a new kind of data (cardiac organoids); its software, source code and documentation are freely available; per-electrode biomarkers, two-dimensional spatiotemporal heatmaps of signal propagation and beat rate variability analysis (reworded 2026-11-06: detail and abbreviations not needed for the argument removed); details in Table 1.
    - > Such tools are not new, as MultiElec and CardioMDA, for example, existed before 2022 (Dunham et al., 2022; Lee et al., 2024), but several new ones have appeared since 2022, some of them built for new kinds of data such as high-density arrays (Lee et al., 2024) and cardiac organoids (Weiser-Bitoun et al., 2026). — main.md:85
    - > PhysioMEA (Weiser-Bitoun et al., 2026) extended this trajectory with a platform whose software, source code and documentation are freely available, designed for cardiac organoids and providing per-electrode biomarkers, two-dimensional spatiotemporal heatmaps of signal propagation and beat rate variability analysis. — main.md:87
- [ ] (3) [Table 1] MATLAB; R-to-T-wave peak; per-electrode biomarkers and 2D spatiotemporal heatmaps; beat rate variability (45 measures) (reworded 2026-11-06: detail and abbreviations not needed for the argument removed).
    - > | PhysioMEA (Weiser-Bitoun et al., 2026) | 2026 | MATLAB | R-to-T-wave peak | Per-electrode biomarkers and 2D spatiotemporal heatmaps; beat rate variability (45 measures) | — main.md:98
- [ ] (4) [Fiducial, Table 2, Morphology] FPD runs from the R peak to the T-wave peak, not to the return to baseline.
    - > - **CardioMEA** (Lee et al., 2024) and **PhysioMEA** (Weiser-Bitoun et al., 2026): from the R peak to the T-wave peak — main.md:107
    - > | R-to-T-peak | R peak (Hayakawa et al., 2014: initial negative peak) | T-wave peak | T-wave peak coincided with APD90 only for biphasic T waves (a minority morphology; NRVM, not hiPSC-CM; Ernault et al., 2024); in hiPSC-CMs, R-to-T-peak FPD correlated only minimally with APD50 and APD90 (Lee et al., 2024); the peak of the positive deflection appeared to match the upstroke of relaxation (Hayakawa et al., 2014) | Hayakawa et al., 2014; Lee et al., 2024; Weiser-Bitoun et al., 2026; described as a common convention and criticised in Mäki, 2023 | — main.md:116
    - > The studies examined do not adopt identical rules, but two of them show an awareness of waveform heterogeneity: they report morphology-dependent analysis branches or document that T-wave morphology varies between preparations, which indicates that a single canonical FP shape cannot be assumed (Ernault et al., 2024; Weiser-Bitoun et al., 2026). — main.md:171
    - > Nonetheless, fiducial definitions remain inconsistent across open platforms: PhysioMEA, for instance, defines FPD as the interval from the R-peak to the T-wave peak (Weiser-Bitoun et al., 2026) rather than the return to baseline (Mäki, 2023), and FPD values are therefore not directly comparable across tools without explicit knowledge of the underlying convention. — main.md:171
- [ ] (5) [Morphology] with Ernault et al. (2024), one of two studies showing awareness of waveform heterogeneity (morphology-dependent analysis branches).
    - > The studies examined do not adopt identical rules, but two of them show an awareness of waveform heterogeneity: they report morphology-dependent analysis branches or document that T-wave morphology varies between preparations, which indicates that a single canonical FP shape cannot be assumed (Ernault et al., 2024; Weiser-Bitoun et al., 2026). — main.md:171
    - > Nonetheless, fiducial definitions remain inconsistent across open platforms: PhysioMEA, for instance, defines FPD as the interval from the R-peak to the T-wave peak (Weiser-Bitoun et al., 2026) rather than the return to baseline (Mäki, 2023), and FPD values are therefore not directly comparable across tools without explicit knowledge of the underlying convention. — main.md:171
- [ ] (6) [3D] an analysis tool built for 3D preparations (cardiac organoids); not evidence on 2D-to-3D transfer.
    - > Analysis tools are beginning to target 3D preparations, such as PhysioMEA for cardiac organoids (Weiser-Bitoun et al., 2026), but no study examined here compared fiducial definitions between 2D and 3D recordings systematically. — main.md:176
- [ ] (7) [Conclusion] analysis of inverted signals and exclusion of electrodes are examples of case-by-case morphology handling.
    - > In the studies examined, morphology handling is described case by case: analysis of inverted signals, exclusion of electrodes, or interpretation restricted to biphasic T waves (Mäki, 2023; Ernault et al., 2024; Weiser-Bitoun et al., 2026). — main.md:232

Pointers: (2) abstract and p. 2–3 ("45 measures, including time domain, frequency domain, and nonlinear analysis", from PhysioZoo; MATLAB 2023b or standalone .exe). (4) p. 3 ("FPD ... defined as the time difference between the R- and T-peaks"). (5)(7) p. 3 (inverted T waves and low-amplitude R peaks analysed on the inverted signal; electrodes with inconsistent biomarker counts excluded).

## Register of the author's own inferences

These are statements in `main.md` that no single reference supports, generalisations from one or two studies, and the author's hypotheses. `main.md` does not mark them in the text, so this list is their only record; every new unsourced inference in `main.md` needs an item here. Tick `[x]` when you have decided that you stand behind the wording.

Reading guide for each item: **bold** = the item's topic and where it sits in `main.md`; "quoted" = the wording in `main.md`; **Based on** = the sources behind it; **Support** = my reading, one of `none` (no source supports it), `thin` (one or two studies) or `inference` (a reasoned step from sources).

- [x] **0. [Highlights]** the six highlights (added 2026-11-01) are uncited summaries
  - **Support:** as for the register items named
  - **(1)** "MEA tools define FPD differently; their FPD values are not directly comparable"
    - **Based on:** Table 1, Table 2, Fiducial list; register item 13
    - **Note:** the researcher removed "Open" because vendor tools also differ; the reviewed evidence documents the open tools' definitions, while the vendor tool's definition is not described in the studies that used it
  - **(2)** "No validated hiPSC-CM rate correction found; Fridericia can mislead at extreme rates" (was "No hiPSC-CM–specific rate correction exists"; aligned with (3) as an absence finding, 2026-11-02)
    - **Based on:** Blinova, Clements; one example, Lee et al., 2026; register items 3 and 14
  - **(3)** no validated MEA-derived maturation reference values
    - **Based on:** documented search; register items 6 and 19
  - **(4)** case-by-case morphology handling
    - **Based on:** Mäki, Ernault, Weiser-Bitoun; register item 4
  - **(5)** "Without these, machine learning may learn analysis differences rather than biology" (was "ML on MEA data …"; abbreviation spelled out, 2026-11-03)
    - **Based on:** register item 7
  - **(6)** raw MEA signals mix cell, tissue and device, and separating them is proposed as a hypothesis
    - **Based on:** Karami et al., 2026; Lee et al., 2026; Mäki, 2023; register items 25 and 26
- [ ] **1. [Intro, Motivation]** reliable recordings need consistent analysis (reworded 2026-11-04)
  - **Text:** "that reliability depends not only on the recording but also on consistent, physiologically meaningful analysis of FP waveforms"
  - **Text:** "This review examines methods and analysis practices in cardiomyocyte MEA studies published since 2022"; the Motivation heading "why analysis methods matter"
  - **Based on:** Botti (5) for the first half of the sentence ("reliable MEA recordings are essential")
  - **Note:** the trend framing ("As the use of MEA-based assays has grown, so has the need …", "have evolved since 2022", heading "why analysis methods became central after 2022") had no usage data and was removed; the step from reliable recordings to consistent analysis is the author's inference
  - **Support:** `inference`
- [x] **2. [Abstract, Motivation]** analysis methods as a possible source of inter-study variability
  - **Text:** analysis methods "have become a focus of attention as a possible source of inter-study variability"
  - **Text:** fiducial definitions "are a plausible source of variability and a possible limit to inter-study comparability"
  - **Text:** "none of them measures how much variability analysis methods cause", with Vuorenpää et al. (2023) as counterpoint
  - **Based on:** Mäki (2023); Lee, Ernault, Hayakawa (FPD not tracking the AP; end points matching different phases); Table 2
  - **Support:** `inference`; only plausibility is claimed
- [x] **3. [Abstract, Conclusion]** Gap 1: no validated rate correction for hiPSC-CMs
  - **Text:** Abstract "**four methodological gaps remain** in the studies examined … (*i*) the absence of a validated hiPSC-CM–specific rate correction formula" (scope stated once for all four gaps, 2026-11-03) and Conclusion heading "No validated FPD rate correction for hiPSC-CMs was found" (reworded 2026-11-03 as a finding of this review; were "the absence of …" and "FPD rate correction remains unsolved")
  - **Note:** no documented search lies behind this absence finding (unlike gap 4, docs/maturation-mea-search.md)
  - **Text:** Fridericia "lacks formal validation for the beating rate range and rate–FPD relationship of hiPSC-CM cultures"
  - **Text:** "borrowed from clinical electrocardiography"
  - **Text:** a cell-type–specific formula from multi-laboratory data "would make FPDc a more reliable pharmacological endpoint"
  - **Based on:** Blinova, Clements, Guerrelli, Altrocchi (vehicle drift)
  - **Support:** `thin` for the gap; the recommendation is an opinion
- [x] **4. [Abstract, Conclusion]** Gap 2: no shared morphology criteria
  - **Text:** shared, validated morphology criteria "were not identified"
  - **Text:** morphology handling is case by case, whereas well-acceptance criteria exist
  - **Text:** standardised morphology assessment "might reduce between-study variability at the data collection stage"
  - **Based on:** Mäki, Ernault, Weiser-Bitoun; Blinova, Clements
  - **Support:** `thin` (absence claim limited to the studies examined); the last part is an untested proposal
- [x] **5. [Abstract, Conclusion]** Gap 3: transfer from 2D to 3D and ultra-high-density platforms
  - **Text:** the transfer of 2D-calibrated frameworks to 3D models and ultra-high-density platforms "proceeds empirically"
  - **Text:** fiducial definitions and conduction metrics "need dedicated validation"
  - **Based on:** Hwang, Maurissen, Lin, Matsuda, Mäki
  - **Support:** `thin`
- [x] **6. [Abstract, Conclusion]** Gap 4: no validated maturation benchmark at recording
  - **Text:** such a benchmark "could only cover the electrophysiological axis"
  - **Text:** "even a partial reference would improve comparability between studies and support the translation of MEA findings to adult myocardium"
  - **Text:** the pieces "exist separately"
  - **Based on:** the documented search of 30 October 2026 (`docs/maturation-mea-search.md`), Fetterman, Correia, Scheurer, Li, Hayakawa, Lin, Clements (QC, not staging)
  - **Support:** absence claim as strong as that search; the benefit is an opinion
- [x] **7. [Abstract, Conclusion]** data-driven methods may learn analysis differences
  - **Text:** "Until these gaps are addressed, data-driven methods built on MEA parameters may learn differences in analysis methods rather than differences in the cells"
  - **Text:** "without them, models built on MEA parameters may reproduce the inconsistencies between studies instead of revealing biological effects"
  - **Support:** `inference`
- [x] **8. [Open pipelines, Conclusion]** open tools as a visible alternative and a trend towards transparency
  - **Text:** open tools "are a visible alternative" and "several new ones have appeared since 2022"
  - **Text:** "these platforms point toward reproducibility, transparency, and explicit reporting"
  - **Text:** the Conclusion's opening (reworded 2026-11-03): open platforms that state their fiducial definitions are used alongside vendor software, one convention was tested against intracellular recordings, some tools adapt to the waveform shape; "These are preconditions for comparing results between studies, but whether they have improved comparability cannot be judged from this small evidence base"
  - **Text:** Open pipelines: Cardio PyMEA "is the earliest of the open pipelines published since 2022 that are examined here" (was "represents an early example of this transition")
  - **Note:** the trend wording ("methodological development from opaque, vendor-defined workflows toward transparent … practices", "points toward progress in inter-study comparability", "this transition") was removed: Limitations states that no usage or prevalence data were collected; "preconditions" is the author's inference
  - **Based on:** the five tools in Table 1
  - **Counter-evidence:** Park et al. (2025, 2026) used the vendor tool, and no adoption data exist (both stated in the text)
  - **Support:** `inference` from five tools
- [x] **9. [Abstract, Fiducial]** explicitly stated fiducial definitions (trend wording removed 2026-11-02)
  - **Text:** "In the studies examined, the open platforms state how they define fiducial points, and one study tested a convention against intracellular recordings"
  - **Text:** the Abstract sentence "open analysis software is used alongside vendor software, and the open tools state how they place the waveform landmarks (fiducial points) that define the measured intervals; one study tested such a definition against intracellular recordings" and the section heading "Explicit and physiologically motivated fiducial definitions"
  - **Based on:** Dunham, Lee et al. (2024), Weiser-Bitoun, Kabanov (Fiducial list); Ernault (sharp-electrode comparison)
  - **Note:** the earlier wording ("growing emphasis", Mäki's algorithm "reflects trends increasingly seen in recent literature", Ernault's topic "has received renewed attention", heading "Increasing emphasis on…") had no counts behind it and was removed; "reflects trends" also contradicted the Fiducial list, where CardioMEA and PhysioMEA end FPD at the T-wave peak rather than at baseline return
  - **Support:** `thin` (a summary of the sources listed, no trend claimed)
- [x] **10. [Fiducial]** transparency is essential because definitions affect drug effects
  - **Text:** "Such transparency is essential because differences in fiducial definitions can influence measured drug effects and rate-corrected FPD or QT surrogates."
  - **Support:** `none` as stated (no study compared conventions on the same data)
- [x] **11. [Fiducial, Table 2]** the two FPD definitions may measure different quantities
  - **Text:** "This anchors the T-wave peak, when the waveform is biphasic, to APD90"
  - **Text:** "the two definitions may therefore measure different quantities rather than one being universally more correct"
  - **Text:** the Table 2 caption ("whether it and the T-wave-peak convention measure different physiological quantities is open")
  - **Based on:** Ernault (2), (3); Hayakawa (1)
  - **Support:** `inference`
- [x] **12. [Fiducial]** morphology assessment before fiducial analysis
  - **Text:** "These findings underscore the importance of waveform morphology assessment prior to any fiducial-point-based analysis."
  - **Support:** `inference`
- [x] **13. [Fiducial, Morphology]** FPD values not comparable across tools
  - **Text:** "the conventions differ"
  - **Text:** "FPD values are therefore not directly comparable across tools without explicit knowledge of the underlying convention"
  - **Based on:** Table 1 and Table 2
  - **Support:** `inference` from the definitions (no study compared tools on the same data)
- [x] **14. [FPDc]** raw FPD is rate-confounded; a fixed correction may fail at the extremes
  - **Text:** "the beating rate can change substantially during recordings. Therefore, raw FPD values are confounded by rate-dependent repolarization effects"
  - **Text:** "a fixed cube-root correction cannot be assumed to hold across the wide range of spontaneous rates ... so the formula may under- or over-correct at the extremes of this range"
  - **Based on:** Guerrelli (equilibration); Blinova and Clements (rate ranges)
  - **Support:** `inference`
  - **Update 2026-11-01:** the under- or over-correction point has a concrete example: Lee et al. (2026), doxorubicin day 1 (beat period about 8 s, FPDc fell while FPD rose); the general claim remains inference
- [x] **15. [FPDc]** the author's view on the missing hiPSC-CM–specific formula
  - **Text:** "In the author's view, the lack of a validated hiPSC-CM–specific formula is a methodological gap that directly limits the comparability of FPDc endpoints between studies."
  - **Note:** marked in the text as the author's view
  - **Support:** `inference`
- [x] **16. [FPDc]** fixed-rate pacing as an alternative (reworded 2026-11-02)
  - **Text:** "Pacing at a fixed rate removes the rate dependence"
  - **Based on:** Guerrelli (4), whose authors repeated their measurements under pacing because the metrics are rate dependent; Matsuda (2) and Clements for the rest of the sentence
  - **Note:** the generalisation "it is not the norm in the studies examined" (three examples, no count) was removed; the sentence now lists only what the three sources report
  - **Support:** `inference` (a general physiological statement; the rationale is Guerrelli's)
- [x] **17. [Maturation]** maturity differences between laboratories; drift is not only a rate effect
  - **Text:** "In the studies examined, maturation state is rarely quantified beyond culture duration"
  - **Text:** "two laboratories could report different results for the same compound because their cultures differ in maturity rather than in analysis method"
  - **Text:** "so the drift is not only a consequence of the slower beating rate, and rate correction alone would not remove it"
  - **Based on:** Guerrelli (5), (6); Ismaili
  - **Note:** our rough Fridericia check of Guerrelli's spontaneous means (FPDc about 279 ms on day 2 and 481 ms on day 14) is on the wiki page only
  - **Support:** `inference`
- [x] **18. [Maturation]** maturation is not a single quantity
  - **Text:** "Maturation is therefore not a single quantity. An MEA-derived reference value can only observe electrophysiology, so it would describe one axis of maturity"
  - **Based on:** Fetterman (2)
  - **Support:** `inference`
- [x] **19. [Maturation, Conclusion]** some ingredients of an MEA-based maturity classifier have been reported separately (reworded 2026-11-02)
  - **Text:** "some ingredients of an MEA-based maturity classifier have been reported separately"; Conclusion gap 4: "Some ingredients for such a reference have been reported separately"
  - **Text:** "The missing ingredient is an independent maturity measure taken on the same MEA cultures" (Conclusion: "what is missing is …")
  - **Text:** Lin et al. (2023) as "the closest step towards combining them"
  - **Text:** "No classifier or reference value for standard MEA recordings, validated against an independent maturity measure on the same cultures, has been reported"; Conclusion: "no classifier or reference values have been reported for standard MEA recordings"
  - **Based on:** Scheurer, Li, Hayakawa, Correia, Lin; the documented search
  - **Note:** the earlier wording "the components … exist separately" / "The pieces for such a reference exist separately" implied that combining them would give a classifier; two things are missing: an independent maturity measure on the same MEA cultures (the reference), and an MEA dataset across controlled maturity levels (Li et al. compare culture conditions, not measured maturity). Hayakawa links FPD to contraction, not to maturity
  - **Support:** `inference`; absence claim as strong as the search
- [x] **20. [Abstract, Morphology]** morphology varies, and some studies adapt their analysis to the waveform shape (reworded 2026-11-02)
  - **Text:** the Abstract sentence "Some tools adapt the analysis to the waveform shape, for example by inverting signals whose peaks point the other way" (replaced "structured handling of FP waveform morphology heterogeneity", which contradicted gap (ii) and the Conclusion's "case by case")
  - **Text:** "FP waveform morphology varies between preparations and over culture time, and some of the studies examined adapt their analysis to it, for example by detecting peaks on the inverted signal"
  - **Text:** "two of them show an awareness of waveform heterogeneity"
  - **Based on:** Mäki (variation between preparations and in later cultures); Weiser-Bitoun (peaks detected on the inverted signal for low R peaks and inverted T waves), Mäki (inversion of "only high peak" signals); Ernault is the reason to check the shape (T-wave peak tracks APD90 only for biphasic T waves), not a handling rule
  - **Note:** the earlier opening ("Another important methodological development … is the recognition that FP waveform morphology varies substantially across preparations, maturation states, and recording conditions") was removed: it presented old knowledge as a recent development, contradicting "Such variation is not new" later in the section, and "substantially" and "recording conditions" had no source
  - **Support:** `thin`
- [x] **21. [3D, Scope]** transfer to 3D and the scope limit
  - **Text:** "so this endpoint transferred in that setting" (Maurissen)
  - **Text:** "no study examined here compared fiducial definitions between 2D and 3D recordings systematically"
  - **Text:** the Scope sentence limiting 3D and in silico modelling to the transfer question (a scope decision)
  - **Support:** `inference` (first); `thin` (second)
- [x] **22. [High-throughput]** demands of high-throughput and chronic use
  - **Text:** high-throughput and chronic applications "require stable beat detection, robust handling of arrhythmic events, and consistent analysis across extended recording periods and large historical datasets"
  - **Text:** multi-parameter feature sets "make clearly defined analysis methods even more important"
  - **Text:** "temporal drift and culture equilibration effects can confound interpretation if fiducial definitions and quality control criteria are not reported"
  - **Based on:** Altrocchi (6), (7); Matsuda; Guerrelli
  - **Support:** `inference`; the drift itself is sourced
- [x] **23. [Motivation, Conclusion]** uses of MEAs and the machine learning outlook
  - **Text:** the list of uses in the studies examined
  - **Text:** machine learning "may become a more integral layer of cardiomyocyte MEA workflows"
  - **Based on:** the studies named
  - **Support:** supported for the list; the outlook is an opinion
- [x] **24. [Outlook]** sensor fusion
  - **Text:** "In most of these studies the modalities are analysed separately or side by side, and the one joint analysis is a small proof of concept outside hiPSC-CMs"
  - **Text:** interpreting them jointly with AI support "could give a more complete picture of a preparation than any single signal"
  - **Based on:** Altrocchi, Lee, Kabanov, Hayakawa, Scheurer, Ryynänen, Hu, Li, Vuorenpää, Mäki
  - **Support:** `thin` (observation; Hu et al., 2026, is the one joint analysis found, in fetal mouse cells); `none` for the hypothesis in hiPSC-CMs (stated as such)
  - **Update 2026-11-01:** also Lee et al. (2026) as a hiPSC-CM example of side-by-side FP and optical readouts
  - **Update 2026-11-08:** Hu et al. (2026) state the same direction in their conclusion (Hu (4)); the hypothesis for hiPSC-CMs remains the author's own
- [x] **25. [Outlook]** doubt about raw MEA signals; separated cellular signal as input
  - **Text:** the doubt "concerns the raw recording as it is, shaped by the culture and the recording system"
  - **Text:** a separated cellular signal "could be a useful input in its own right, beyond the parameters extracted from it", repeated at the end of the device-separation part
  - **Origin:** the researcher's idea (2026-11-01)
  - **Based on:** Mäki (the doubt, the two-step approach); Lin (6) is the only sourced part
  - **Support:** `none` for the separated-signal part
- [x] **26. [Outlook]** device separation by reverse engineering
  - **Text:** estimating and separating the MEA device and tissue contribution by reverse engineering (system identification), so that the remaining signal resembles the cellular AP more closely
  - **Text:** electroporation data and sensor fusion as training and validation data
  - **Text:** "removing the device contribution alone would not be sufficient"
  - **Text:** "The paired signals proposed above as training data share part of this limitation: a local extracellular action potential obtained by electroporation is not a recording of the local AP but is generated by current from neighbouring cardiomyocytes" (added 2026-11-03; a sourced caution against the electroporation-data proposal, Ernault (5))
  - **Text:** the recovery "may also be an ill-posed inverse problem, because a field potential is a weighted sum of the transmembrane currents of many surrounding cells"
  - **Text:** a calibrated model as a digital twin of the recording; more comparable results across hardware
  - **Based on:** Mäki, Lee, Ernault, Botti, Vuorenpää
  - **Support:** `none` (hypotheses; the ill-posed point is from extracellular recording theory, unsourced)
  - **Update 2026-11-01:** partly sourced: the FP shaped by tissue and hardware, the cell–electrode equivalent circuit and the superposition behind the ill-posed point (Karami et al., 2026), and hardware altering absolute signal values (Lee et al., 2026); the inverse approach, the digital twin and the comparability benefit remain hypotheses
- [x] **27. [Outlook]** impedance as an attachment marker
  - **Text:** "such an impedance channel could also indicate FP changes that stem from altered attachment, and thus from altered coupling between cells and electrodes, rather than from changes in the AP of the cells themselves"
  - **Origin:** the researcher's idea (2026-10-26)
  - **Based on:** Altrocchi (9)
  - **Support:** `none` (not tested in that study)
  - **Update 2026-11-01:** supported in mechanism by Karami et al. (2026) (impedance sensitive to cell–electrode distance, about 1 nm); its use to flag FP changes remains untested
- [ ] **28. [Morphology]** polarity as an unstated assumption
  - **Text:** Cardio PyMEA's analysis "presupposes the polarity of its recordings, which the paper does not state"; the sign of the repolarization wave "cannot simply be assumed"
  - **Origin:** the researcher's reading of Dunham et al. (2022), Figures 4–6 (2026-11-05); the inverted, pacemaker-like reading and the EAD interpretation are kept out of main.md, on wiki/fp-polarity.md
  - **Based on:** Dunham (7), Karami (5)
  - **Support:** `sourced` for the definitions and for the missing polarity statement; the inference that the analysis depends on polarity follows from the definitions
- [ ] **29. [Maturation]** the Clements amplitude criterion depends on recording day
  - **Text:** "Whether a culture meets the amplitude criterion also depends on when it is recorded"
  - **Origin:** the researcher's check of Guerrelli Supplementary Tables 2, 5 and 6 (2026-11-06)
  - **Based on:** Guerrelli (11), Clements (8)
  - **Support:** `sourced` for the values; the comparison is ours and loose, because Guerrelli reports well means from one electrode and Clements a share of electrodes ≥ 0.5 mV. Both lines are below 0.5 mV on day 2, so the day dependence holds across the two lines; the size of the rise differs by line (3.6 vs 8.1 mV on day 14; paced Cor.4U 0.72 mV on day 3, 8.38 mV on day 14, Table S6)
