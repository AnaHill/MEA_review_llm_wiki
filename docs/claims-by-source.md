# Claims in main.md, by source

A checklist for verifying the paper against its sources. Each source has a checklist of every claim that `main.md` attributes to it, with the section in brackets; tick `[x]` when you have checked a claim against the source (a number such as 8b marks a second claim that had the same number in the earlier paragraph format). Compiled 2026-10-18 and verified against the source documents on 2026-10-24 (see "Corrections made in the 2026-10-24 verification" at the end); regenerate or update it if `main.md` changes. Verify each claim in the local file named under the source (all files are in `raw/`; page and figure pointers are given where known). "Checked" below means that the claims were compared with the full text of the source (the date is given in each status line); where the check found a mismatch, the wording in `main.md` was corrected and the correction is described under the source. Even so, the verification was done by reading and searching the extracted text of the PDFs, and figures were viewed only where stated, so your own check is still needed for numbers, figure readings and nuances of wording.

Sections cited in brackets: Intro, Motivation, Scope, Timeline (Figure 1), Open pipelines (section "Open analysis pipelines alongside vendor-defined metrics"), Table 1, Fiducial (definitions section), Table 2, FPDc (rate correction), Maturation, Morphology (incl. Figure 2), Model complexity, High-throughput/longitudinal (High-throughput and longitudinal assays section), Limitations, Conclusion, Outlook (Discussion and future outlook).

<!-- temporary Finnish  version
Rakenne: tiedostossa on yksi osio per lähde, ja kunkin osion lopussa yksi kappale, jossa on jokainen väite, jonka main.md liittää kyseiseen lähteeseen. Väitteet on numeroitu ja merkitty osion tunnuksella (Intro, FPDc, Maturation jne.).

Jokaisessa osiossa: paikallinen tiedosto raw/-kansiossa, wikisivu ja tarkistustila.
Tarkistustila kertoo rehellisesti, mitä olen oikeasti tarkistanut täystekstistä.
-->


## Altrocchi et al. (2023)

Local file: `raw/altrocchi-2023-chronic.pdf`; page `wiki/papers/altrocchi-2023-chronic.md`. Status: checked against the full text 2026-10-24.

Claims (tick `[x]` when you have checked the claim against the source):

- [x] (1) [FPDc] the study reports rate-corrected FPD with the Fridericia formula (listed among the studies that use it).
- [x] (2) [High-throughput/longitudinal] it used 48-well MEA plates to evaluate acute (<2 h) and delayed (≥24 h) electrophysiological and cytotoxic effects of reference compounds, including tyrosine-kinase inhibitors, an anthracycline (doxorubicin) and ion-channel trafficking inhibitors, over 4 days, combining field potential recordings with impedance readouts, on a platform the authors describe as medium-throughput (added 2026-10-27; Discussion: "a medium-throughput, human-based platform, suitable for further upscaling"; the paper also contrasts its chronic approach with "acute (high throughput) assays").
- [x] (3) [High-throughput/longitudinal] "A chronic MEA assay with repeated recordings over four days has been validated for both acute and delayed cardiotoxicity" (revised 2026-10-27; earlier "Chronic and longitudinal MEA assays have been validated ...", a plural generalisation from this one study, and "longitudinal" is not the paper's term). Pointers: abstract ("recordings were conducted for 4 days"); Methods 2.3 (baseline and 2, 24, 48, 72 and 96 h); "developed and validated a functional assay" (p. 3).
- [x] (4) [High-throughput/longitudinal] it is one of the two examples (with Matsuda et al., 2025) of multi-parameter feature sets encompassing beat rate, beat-to-beat variability, conduction properties and event-based descriptors.
- [x] (5) [Intro] cited, with Blinova et al. (2018) and Park et al. (2025), for MEA recordings of hiPSC-CMs being widely used in cardiac safety pharmacology, drug discovery and disease modelling.
- [x] (6) [Outlook] impedance is read alongside FP, as an example of a second measurement added to the MEA recording.
- [x] (7) [Motivation] example of chronic drug testing (revised 2026-10-27 from "longitudinal drug testing": the paper's own term is "chronic").
- [x] (8) [Outlook] a background impedance signal was recorded alongside the FP; its drop reflects reduced attachment of the cells to the bottom of the well, owing to cell death or changes in the monolayer morphology; it was used as a cytotoxicity readout to help separate electrophysiological effects from cell death. (The further step, that impedance could also flag FP changes caused by altered attachment, is the author's hypothesis, stated as such in the text, and was not tested in the paper.) Pointers: Methods, data analysis paragraph on Imp (p. 5; the passage "a reduction in the attachment of hiPSC-CMs to the bottom of the well due to cell death or changes in the monolayer morphology, causes a drop in the impedance signal"); Discussion on doxorubicin ("the impedance assay also detects changes in shape and morphology of the hiPSC-CMs monolayer, as well as cell detachment from the electrodes").

Check 2026-10-24: (1) confirmed, the paper writes "Fredericia correction formula, FPDc (Blinova et al., 2018)" (p. 5). (2) confirmed: abstract p. 1 (acute <2 h, delayed ≥24 h, 48-well plates, recordings for 4 days), Methods p. 3 (Axion Cytoview M768-tMEA-48B, up to 96 h); doxorubicin is the only anthracycline (BMS-986094 is the other direct cardiotoxic drug), so the text was changed from "anthracyclines" to "an anthracycline (doxorubicin)". (3) the paper says it "developed and validated a functional assay" with 13 reference compounds (p. 3). (4) partly: the study itself reports beating rate, FP amplitude, FPD/FPDc, impedance and arrhythmic events; beat-to-beat variability and conduction properties come from Matsuda et al. (2025), not from this study.

## Blinova et al. (2018)

Local file: `raw/blinova-2018-multisite.pdf`; page `wiki/papers/blinova-2018-multisite.md`. Status: checked (Methods, Results, Discussion; Figures 1, 2, 5–7 viewed) 2026-10-18.

Claims (tick `[x]` when you have checked the claim against the source):

- [ ] (1) [Intro] cited, with Altrocchi et al. (2023) and Park et al. (2025), for MEA recordings of hiPSC-CMs being widely used in cardiac safety pharmacology, drug discovery and disease modelling, and, with Park et al. (2025), for FPD and related metrics being integral to the CiPA initiative.
- [ ] (2) [FPDc] it was a "blinded multisite CiPA study" that applied Fridericia correction to all 28 reference drugs across ten sites.
- [ ] (3) [FPDc] it states that the Fridericia formula was not thoroughly validated for hiPSC-CMs, and this is described as a recognised methodological gap.
- [ ] (4) [FPDc] spontaneous rates of hiPSC-CMs are "accepted at 20–90 BPM" in this study (inclusion criterion for baseline beating rate).
- [ ] (5) [Limitations] it is cited only as pre-2022 background for conventions and datasets that later studies build on, not as one of the post-2022 developments reviewed. Pointers: Fridericia statement in the Data Analysis section of the Experimental Procedures; the 20–90 bpm criterion in the same section; ten sites and 28 drugs in the Summary.
- [ ] (6) [Motivation] example of proarrhythmia risk assessment.
- [ ] (7) [Conclusion] quantitative acceptance criteria exist for well acceptance (amplitude, rate, beat period).

## Botti et al. (2026)

Local file: `raw/botti-2026-insilico.pdf` (+ peer review history); page `wiki/papers/botti-2026-insilico.md`. Status: checked against the Europe PMC full text 2026-10-18; compare with the PDF.

Claims (tick `[x]` when you have checked the claim against the source):

- [ ] (1) [Timeline] "In silico MEA–tissue biophysical model (Botti et al.)", listed under 2026.
- [ ] (2) [Model complexity] it is a two-dimensional bidomain model of a six-well MEA with phenotype-specific ventricular-like and atrial-like ionic models.
- [ ] (3) it simulated how the atrial-like fraction changes conduction velocity and repolarization.
- [ ] (4) it reproduced Brugada-like field potentials.
- [ ] (5) it compared simulated effects of four ion-channel blockers (mexiletine, nifedipine, dofetilide, E-4031) with previously published MEA data, without new experiments and with a fixed 30 % atrial-like fraction in the drug simulations.
- [ ] (6) it is a monolayer model and does not address the 3D question directly.
- [ ] (7) [Limitations] it is an example of simulation-based evidence.
- [ ] (8) The reference year is 2026 (issue 604(19), October 2026; online 11 May 2025).
- [ ] (8b) [Outlook] a bidomain model with a resistor–capacitor electrode model simulates FPs from phenotype-specific cell models (forward modelling that includes the electrode).

## Clements et al. (2025)

Local file: `raw/clements-2025-aims-poster.pdf` (git-ignored); page `wiki/papers/clements-2025-aims-poster.md`. Status: checked (poster text read in full; layout not viewed) 2026-10-18.

Claims (tick `[x]` when you have checked the claim against the source):

- [ ] (1) [FPDc] a recent proposed acceptance standard for hiPSC-ventricular-CM MEA assays builds the Fridericia correction into quality control by requiring an FPDc of 200–700 ms.
- [ ] (2) [FPDc] spontaneous rates are accepted at 20–80 BPM in that proposal.
- [ ] (3) [Maturation] it is an industry-led proposal (Axion BioSystems' "AIMS \#CM01", presented as a poster at ISSCR 2025) defining minimum well-acceptance criteria for spontaneous-beating hiPSC-ventricular-CM MEA assays: spike amplitude ≥ 0.5 mV and synchronized beating on at least half of the electrodes, a spontaneous beat period of 750–3000 ms, and FPDc of 200–700 ms.
- [ ] (4) it targets assay quality control, not maturation staging.
- [ ] (5) it has been presented as a conference poster and vendor document rather than a peer-reviewed methods paper. Pointers: the "AIMS \#CM01: Proposed standards" box; "Presented at ISSCR 2025, Hong Kong, June 11, 2025". The standard document on the vendor's website (last revised 2 December 2024) was read only through a web-fetch summary.
- [ ] (4b) [Conclusion] quantitative acceptance criteria exist for well acceptance (amplitude, synchrony, beat period, FPDc).
- [ ] (6) [FPDc] the proposed acceptance criteria are for spontaneous-beating hiPSC-ventricular-CM assays.

## Correia et al. (2024)

Local files: `raw/correia-2024-acc2.pdf` (+ supplementary); page `wiki/papers/correia-2024-acc2.md`. Status: checked against the full text and Figure 7F 2026-10-24.

Claims (tick `[x]` when you have checked the claim against the source):

- [ ] (1) [Timeline] ACC2-inhibitor maturation medium improves in vitro-to-in vivo translatability (2024).
- [ ] (2) [Maturation] they developed a maturation medium, a galactose- and fatty-acid-based formulation with a triiodothyronine/IGF-1/dexamethasone cocktail, augmented with a small-molecule acetyl-CoA carboxylase 2 (ACC2) inhibitor.
- [ ] (3) it improved patch-clamp-defined electrophysiological maturity (a more hyperpolarized maximum diastolic potential, faster action potential upstroke velocity, and a six-fold increase in inward-rectifier K⁺ current) alongside metabolic and structural maturation.
- [ ] (4) an in vitro-to-in vivo target-engagement correlation (in vitro IC50 against in vivo IC50 in rat plasma) across 21 inhibitors of one drug target, BCKDK, was achieved only in matured cells (Pearson r = 0.85, R² = 0.72, p < 0.0001, data spanning roughly three orders of magnitude).
- [ ] (5) standard-medium cells showed no significant response to BCKDK inhibition, so no correlation could be computed.
- [ ] (6) therefore, for this target, maturation status can gate translational validity.
- [ ] (7) [Conclusion] for one drug target, in vitro-to-in vivo correlation was obtained only in matured cells.

Check 2026-10-24: (2) p. 3, medium with oleic and palmitic acid, 10 mM galactose, 1 µM dexamethasone, 100 nM T3, 100 ng/mL IGF1 and 5 µM ACC2 inhibitor (CP640186). (3) p. 14: maximum diastolic potential −79.2 ± 4 vs −74.3 ± 8.2 mV, dV/dt max 68.6 ± 43.5 vs 23.4 ± 25.6 V/s; p. 16: IK1 6-fold (−27.3 vs −4.1 pA/pF). (4) Figure 7F (p. 22) reads r 0.85, R² 0.72, p < 0.0001 and 21 BCKDK inhibitors; the x-axis spans four decades but the data span about three, so the earlier "four orders of magnitude" was changed to "roughly three"; "pharmacokinetic" was changed to "target-engagement". (5) p. 23: "not possible to obtain using standard medium"; BCAT inhibitors responded in both media, so the statement is restricted to BCKDK inhibition. (6)(7) one drug target only, so the earlier wording that translatability "itself depends on maturation status" was restricted.

## Dunham et al. (2022)

Local file: `raw/dunham-2022-cardiopyemea.pdf`; page `wiki/papers/dunham-2022-cardiopyemea.md`. Status: checked against the abstract and the FPD section 2026-10-24.

Claims (tick `[x]` when you have checked the claim against the source):

- [ ] (1) [Timeline] Cardio PyMEA, an open-source Python pipeline, 2022.
- [ ] (2) [Open pipelines] it is an open-source Python-based application for explicit analysis of cardiomyocyte MEA recordings including beat detection, pacemaker origin estimation, beat interval and amplitude analysis, local activation time, upstroke velocity and conduction velocity.
- [ ] (3) [Open pipelines] it is an early example of the transition away from vendor software.
- [ ] (4) [Fiducial, Table 1, Table 2] it measures FPD from the R wave to a T-wave endpoint located with a trapezoid-area algorithm (method of Vázquez-Seisdedos et al.), not validated against APD in the paper. To check (2026-10-29): main.md's Fiducial list now writes "R peak" for all three open platforms (the paper's term here is "R wave"); confirm that the paper's start point is the R peak and not, for example, the onset of the R wave.
- [ ] (5) [Figure 2] the T-wave endpoint (trapezoid area) is shown as a third FPD end convention in the flowchart, beside the T-wave peak (Ernault et al.) and baseline return (Mäki).

Check 2026-10-24: (2) matches the abstract (p. 1; free, modifiable, open source under GPL; Python 3 with a PyQt5 GUI). (3) the paper itself says that open-access tools existed before (p. 2: "open-access tools offering enhanced functionality beyond ... proprietary software"), so `main.md` now also notes that open tools such as MultiElec and CardioMDA predate 2022 (citing Lee et al., 2024, Table 3). (4) section "Field potential duration calculation" (R wave to the T-wave endpoint, the maximum first derivative between the T peak and baseline and an arbitrary point 50–200 ms past the T peak fit a trapezoid with a mobile point; maximising its area gives the endpoint, p. 10). (5) main.md Figure 2 added 2026-10-24 (branch 'T-wave endpoint, trapezoid area'); it follows (4).

## Ernault et al. (2024)

Local file: `raw/ernault-2024-interpretation.pdf`; page `wiki/papers/ernault-2024-interpretation.md`. Status: checked against the abstract and Results 2026-10-24.

Claims (tick `[x]` when you have checked the claim against the source):

- [ ] (1) [Timeline, Table 2, Figure 2] T-wave peak equals APD90 for biphasic T waves, in NRVM.
- [ ] (2) [Fiducial] using simultaneous MEA and sharp-microelectrode recordings from neonatal rat ventricular myocyte (NRVM) monolayers, the peak time of the T wave in FPs correlates strongly with APD90, but only when the T wave displays a biphasic pattern.
- [ ] (3) the authors report that morphology in only a minority of recorded monolayers.
- [ ] (4) [Fiducial, our inference] the T-wave peak, when biphasic, is better anchored to APD90 than a baseline-return convention, which extends into the repolarization tail; the two definitions measure different quantities.
- [ ] (5) [Morphology] together with Weiser-Bitoun et al., it is cited for post-2022 studies increasingly reporting morphology-dependent analysis branches or document that T-wave morphology varies between preparations.
- [ ] (6) [Limitations] example of evidence in rat cells.
- [ ] (7) [Outlook] the T-wave peak tracks APD90 only for biphasic T waves; the LEAP depends on current from neighbouring cells, so removing the device contribution alone would not suffice (the second half is our inference).
- [ ] (8) [Conclusion] interpretation restricted to biphasic T waves is an example of case-by-case morphology handling.

Check 2026-10-24: (2)(3) abstract p. 1 and p. 4: Tpeak coincided with APD90 and Tup with APD50 "only in the monolayers exhibiting field potentials with a biphasic T wave ... only the case in the minority of the monolayers"; p. 10 notes that the neonatal rat T wave may be monophasic or invisible. (5) the paper restricts interpretation to biphasic T waves, which supports "morphology-dependent" analysis in a limited sense.

## Fetterman et al. (2024)

Local file: `raw/fetterman-2024-maturation.pdf`; page `wiki/papers/fetterman-2024-maturation.md`. Status: checked against the full text 2026-10-24.

Claims (tick `[x]` when you have checked the claim against the source):

- [ ] (1) [Timeline] functional, metabolic and transcriptional maturation shown independent.
- [ ] (2) [Maturation] they systematically added and removed individual components of a defined maturation medium and compared nine medium formulations by RNA sequencing.
- [ ] (3) functional (electrophysiology and excitation-contraction coupling), metabolic and transcriptional maturation are induced largely independently by different medium components; for example, removing fatty acids lowered mitochondrial respiration without changing Ca²⁺ dynamics.
- [ ] (4) therefore maturation is not a single scalar quantity and any MEA-derived reference value could characterise only the electrophysiological axis.
- [ ] (5) [Conclusion] the same independence is the reason a benchmark would be scoped to the electrophysiological axis.
- [ ] (6) [Limitations] example of a non-MEA modality.

Check 2026-10-24: (3) summary p. 2 ("sub-specified into electrophysiological/EC coupling, metabolism, and gene expression and that induction of these attributes is largely independent"); p. 7 ("Fatty acids contribute to metabolism but not viability, Ca²⁺ dynamics, impedance, or Nav current"). (2) "nine medium formulations" applies to the RNA-seq comparison (Figure 6, p. 10); the main design is single-addition and single-subtraction experiments in minimal formulations (Figure 2, p. 6), so the earlier wording "systematically varied nine formulations" and the sentence about action potential kinetics and Na⁺ current having "no effect on mitochondrial respiration, and vice versa" were replaced by the verified example.

## Guerrelli et al. (2024)

Local file: `raw/guerrelli-2024-hipscm.pdf`; page `wiki/papers/guerrelli-2024-hipscm.md`. Status: checked against the abstract and p. 10 2026-10-24.

Claims (tick `[x]` when you have checked the claim against the source):

- [ ] (1) [Timeline] temporal and spatial confounders quantified.
- [ ] (2) [FPDc] one study reported that the beating rate increases by more than 22 % and FPD decreases by about 8 % during a 20-minute recording equilibration period.
- [ ] (3) [High-throughput/longitudinal] the same numbers more precisely: beating rate +22.6 % and FPD −7.7 % over a 20-minute equilibration window.
- [ ] (4) [High-throughput/longitudinal] from 2 to 14 days in culture the beating rate decreases while FPD lengthens substantially.
- [ ] (5) [Maturation] FPD lengthens by about 257 ms and beating rate declines over days 2–14 in culture.
- [ ] (6) [Maturation] KCNJ2 (I_K1-encoding) gene expression rises 27.5-fold over 30 days.
- [ ] (7) [Maturation, our interpretation] this drift is consistent with ongoing maturation and rate correction alone does not address it.
- [ ] (8) [High-throughput/longitudinal] the findings highlight the need to standardise recording time points and culture age.
- [ ] (9) [Motivation] example of recordings repeated over days in culture (revised 2026-10-27 from "longitudinal drug testing": the paper records daily for 2–14 days, but tests drugs at two culture ages, day 4 and day 10, so it is not longitudinal drug testing; abstract and Methods, "Drug response").
- [ ] (10) [FPDc] it also recorded paced beating (paced recordings on days 3-14), besides spontaneous recordings.

Check 2026-10-24: all numbers confirmed in the abstract (p. 1): 22.6 % rate increase and 7.7 % FPD decrease in a 20-min equilibration, 12.7 beats/min decrease and +257 ms FPD from 2 to 14 days; KCNJ2 27.5-fold at p. 10 (iCell cardiomyocytes², 2–30 days; 5.0-fold in Cor.4U). The authors say daily variations "may be linked to the continued maturation" of the cells.

## Hayakawa et al. (2014)

Local file: `raw/hayakawa-2014-motion-fp.pdf`; page `wiki/papers/hayakawa-2014-motion-fp.md`. Status: checked against the full text 2026-10-24 (text extraction; figures not viewed; the supplementary materials are not available).

Claims (tick `[x]` when you have checked the claim against the source):

- [ ] (1) [Maturation, Conclusion] field potential duration and contraction–relaxation duration are linearly related across drug concentrations in iPSC-CMs, with a different slope for each drug and under non-arrhythmic conditions (also cited by Scheurer et al., 2025).
- [ ] (2) [Outlook] earlier work recorded image-based motion and MEA field potentials simultaneously in hiPSC-CM monolayers and found linear relationships between contraction–relaxation duration and FPD across drug concentrations, with drug-specific slopes.
- [ ] (3) [Limitations] pre-2022 work cited as background.
- [ ] (4) [Fiducial] simultaneous video and MEA recordings in iCell monolayers: the two FPD end points in use at the time, the peak of the positive deflection and the return of the positive deflection to baseline, appeared to correspond to different phases of the relaxation motion (upstroke and peak, respectively), and an accurate end point was difficult to establish.
- [ ] (5) [Fiducial] an accurate FP end point was difficult to establish in the simultaneous recordings (cited in the sentence on the robustness of the baseline-return end point).

Check 2026-10-24: (1) p. 1 (abstract: simultaneously recorded motion and FP, linear correlation between changes in motion and FPD for verapamil 30–150 nM, isoproterenol 0.1–10 µM and E-4031 10–50 nM), p. 5–6 (R = 0.915 and slope 1.362 for E-4031, R = 0.970 and 0.633 for verapamil, R = 0.943 and 0.738 for isoproterenol), p. 11 ("the CRD can be a surrogate of the FPD in non-arrhythmic conditions"; slopes differ between drugs; the time resolution of the motion data is about 6 ms; beating rate not considered). The earlier wording "correlates strongly with contraction duration" in `main.md` was made more precise (per drug, non-arrhythmic). (2) p. 3: MED-P515A probes with 64 platinum-black electrodes, imaging and MEA synchronised by the MEA trigger; iCell Cardiomyocytes; the "first simultaneous measurement" priority claim is in the authors' highlights and is not repeated in `main.md`. (4) p. 3: "The end of the FPD was previously defined as either the peak of the positive deflection ... or the point where the positive deflection returns to the baseline ... The former end-point appears to be correlated with the upstroke of relaxation motion, while the latter end-point appears to be correlated with the peak of relaxation motion. However, determination of an accurate end-point of FP proved difficult to establish." The wording in `main.md` keeps the authors' hedge ("appears"); the observation is for non-arrhythmic iCell monolayers on 64-electrode MEA probes. In the paper itself the FPD runs from the initial negative peak to the peak of the positive deflection (TTX section, p. 5).

## Hwang et al. (2023)

Local file: `raw/hwang-2023-spheroids.pdf`; page `wiki/papers/hwang-2023-spheroids.md` (rewritten 2026-10-24). Status: checked against the full text 2026-10-24.

Claims (tick `[x]` when you have checked the claim against the source):

- [ ] (1) [Timeline] 3D spheroid geometry as a source of FP variability.
- [ ] (2) [FPDc] the study uses Fridericia-corrected FPD (listed among the studies that use it).
- [ ] (3) [Model complexity] in silico three-dimensional models of hiPSC-CM spheroids on MEAs, compared with in vitro recordings, produced highly variable field potential shapes that depended on the stimulation and electrode locations even with a single cell type, indicating that three-dimensionality itself contributes to FP variability.
- [ ] (4) [Limitations] example of simulation-based evidence.

Check 2026-10-24: (3) abstract p. 1 and Discussion p. 7. The earlier `main.md` sentence called these "experimental studies" and named "tissue thickness, cell–electrode coupling, and propagation patterns"; the paper is an in silico study matched to in vitro data and names stimulation and electrode locations. (2) p. 5: "FPD corrected with Fridericia's formula".

## Ismaili et al. (2023)

Local file: `raw/ismaili-2023-hamburg.pdf`; page `wiki/papers/ismaili-2023-hamburg.md` (rewritten 2026-10-24). Status: checked against the full text 2026-10-24.

Claims (tick `[x]` when you have checked the claim against the source):

- [ ] (1) [Timeline] Hamburg perspective on hiPSC-CM limitations.
- [ ] (2) [Motivation] it discusses, from a critical perspective, broader methodological and biological challenges of hiPSC-CMs as electrophysiological models, including ion channel expression, resting membrane potential and the identity of cell subtypes.
- [ ] (3) [Maturation] hiPSC-CMs express ion channels that are absent from adult human working myocardium, notably the funny current (If) and occasionally the T-type Ca²⁺ current, although the presence of the latter is not necessarily a sign of immaturity.
- [ ] (4) [Maturation] whether ventricular-, atrial- and nodal-like cells form distinct subpopulations within the same preparation is debated (cited to Ismaili et al.; the patch-clamp subtype proportions are from Park et al., 2026).

Check 2026-10-24: (3) p. 3 ("clearly express ion channels that are absent in the adult human working myocardium"; HCN4; ICa,T "cannot necessarily be taken as an indication of immaturity"). (4) p. 4: a study of 320 cells found a single Gaussian APD90 distribution "arguing against ... a truly mixed cell population", with the caveat about the measurement method. The paper does not mention MEA, FPD or rate correction at all, so the earlier use of it in the Introduction for "MEA recordings ... widely used in cardiac safety pharmacology, drug discovery, and disease modelling" was replaced by Blinova et al. (2018), Altrocchi et al. (2023) and Park et al. (2025), and the "fetal-like phenotype" statement now cites Correia et al. (2024) and Scheurer et al. (2025).

## Kabanov et al. (2026)

Local file: `raw/kabanov-2026-cardioscripts.pdf`; page `wiki/papers/kabanov-2026-cardioscripts.md`. Status: checked against the abstract, Methods and the lidocaine experiment 2026-10-24.

Claims (tick `[x]` when you have checked the claim against the source):

- [ ] (1) [Timeline] CardioScripts, combined AFM and MEA electromechanical analysis.
- [ ] (2) [High-throughput/longitudinal] CardioScripts is an open-source Python toolbox tested on HL-1 cells and hESC-derived embryoid bodies.
- [ ] (3) it integrates MEA field potential analysis with simultaneous atomic force microscopy (AFM) recordings to quantify electromechanical coupling and decoupling.
- [ ] (4) dose-dependent lidocaine effects show that electrical and mechanical signals can dissociate in ways that neither modality detects alone.
- [ ] (5) [Table 1] Python; also named Myopyth; FPD end not reported, T peaks are detected.
- [ ] (6) [Outlook] contraction force from simultaneous AFM is added to MEA; the synchronous validation was done on embryoid bodies only.

Check 2026-10-24: (2) p. 2 ("fully open source and freely available"); the cells are HL-1 (Sigma) and embryoid bodies from hESC line CCTL14, so "hESC-derived cardiomyocytes" was changed to "hESC-derived embryoid bodies". (3)(4) p. 7–8 and Figure 10: lidocaine 25 and 30 µM increased the delay between field potential and contraction in embryoid bodies, dose-dependently; "neither modality alone" is the author's reading. (5) T peaks are detected (p. 3), FPD is not defined.

## Lee et al. (2024)

Local file: `raw/lee-2024-cardiomea.pdf`; page `wiki/papers/lee-2024-cardiomea.md`. Status: checked against the Europe PMC full text 2026-10-18 (Table 1, Table 3, Results); compare with the PDF.

Claims (tick `[x]` when you have checked the claim against the source):

- [ ] (1) [Timeline] CardioMEA platform, scalable open analysis.
- [ ] (2) [Open pipelines, Table 1] it was built for high-density MEA data, processes files in parallel into an SQL database, has a web-based dashboard, extracts features from extracellular and intracellular-like (electroporation-derived) signals, and has an automated machine-learning module ranking features that separate diseased from control lines; Python.
- [ ] (3) [Open pipelines] open tools such as MultiElec and CardioMDA already existed before 2022 (Table 3 of the paper lists them).
- [ ] (4) [Fiducial, Table 1, Table 2] FPD is measured from the R spike to the T-wave peak. To check (2026-10-29): main.md's Fiducial list now writes "R peak" for all three open platforms (the paper's term is "R spike"); confirm that the R spike means the peak of the spike.
- [ ] (5) [Fiducial] in iCell cardiomyocyte HD-MEA recordings, R-to-T-peak FPD correlated only minimally with APD50 and APD90 measured from intracellular-like signals on the same electrodes, which the authors attribute to small, noisy T waves.
- [ ] (6) [FPDc, Table 1] the published feature set contains FPD but no rate-corrected FPD. Pointers: Table 1 (features), Figure 4 (correlations), Table 3 (platform comparison).
- [ ] (7) [Outlook] intracellular-like signals are obtained through the same electrodes by electroporation; R-to-T-peak FPD correlated only minimally with APD50 and APD90 from those signals; electroporation gives paired FP and AP-like signals from the same electrodes (the use as training and validation data is our proposal).
- [ ] (8) [Conclusion] automated feature ranking in an open platform is one of the machine-learning uses in the studies examined.

## Mäki (2023, version v3)

Local file: `raw/maki-2023-opinion.html`; page `wiki/papers/maki-2023-opinion.md`; also `wiki/critical-assessment-maki-claims.md`. Status: claims 2–6 and 7 checked against the HTML 2026-10-24 (propagating monolayer, neighbouring cells, 10 % thresholds, Limitations sentence); the rest from the wiki page. This is the author's own opinion paper.

Claims (tick `[x]` when you have checked the claim against the source):

- [ ] (1) [Abstract, Motivation, Scope, Timeline] it is used as the evaluative framework; the Figure 1 timeline lists "DatAnalyzer / Mäki opinion paper — morphology-aware FPD" under 2023.
- [ ] (2) [Motivation] it challenged the physiological validity of commonly used FP annotation conventions, arguing that the widely adopted peak-to-peak FPD definition is often mismatched to the underlying electrophysiology.
- [ ] (3) it argues that the first positive FP peak in a propagating hiPSC-CM monolayer may reflect depolarization of neighbouring cells rather than the locally recorded cardiomyocyte.
- [ ] (4) it argues that FPD end should be measured to the return of the signal to baseline rather than the repolarization peak.
- [ ] (5) [Fiducial] it describes an algorithm: beat-aligned segmentation, averaging across beats to reduce noise, threshold-based identification of depolarization onset relative to FP amplitude, FPD end as return of the signal toward baseline.
- [ ] (6) [Morphology] morphology-aware handling of pacemaker-like signals and waveform inversion for "only high peak" cases, internally validated in that work but not independently replicated.
- [ ] (7) [Model complexity] its caution that analysis frameworks optimised for 2D cultures may not be directly transferable to 3D systems (its Limitations section says the analysis "might not be as easily … extrapolated to the 3D model").
- [ ] (8) [Table 1, Table 2, Figure 2] DatAnalyzer (Python): FPD from depolarization onset to baseline return; the merged peak-to-peak row of Table 2 also characterises that convention as common and criticised in this paper; Figure 2 and the Morphology paragraph also cite it for the baseline-return end.
- [ ] (9) [Declarations, References] the first version was posted on Zenodo in 2023; the text assessed is v3, published 23 June 2026 (the version list of the record zenodo.org/records/20807245 reads "Version v3, 10.5281/zenodo.20807245, Jun 23, 2026"; the "Updated 2025-08-07" date on the record page is a separate metadata field and not the publication date). The reference entry keeps the year 2023 of the original version and states "(Version v3, published 23 June 2026)"; the Declarations version note says the same.
- [ ] (10) [Limitations] it is the author's own, non-peer-reviewed opinion paper; its inversion approach is not independently replicated; its FPD-end convention is one of several.
- [ ] (11) [Declarations] competing-interest statement: the author wrote this paper and the DatAnalyzer tool.
- [ ] (12) [Outlook] the author's view that machine learning applied directly to raw MEA signals is unlikely to work, the two-step approach (extract parameters from detected peaks, then machine learning), and the idea of estimating the AP from the FP by modelling the recording system, ideally with electroporation through the MEA electrodes.
- [ ] (13) [Conclusion] analysis of inverted signals (waveform inversion) is an example of case-by-case morphology handling.

## Matsuda et al. (2025)

Local file: `raw/matsuda-2025-uhd.pdf`; page `wiki/papers/matsuda-2025-uhd.md` (two statements corrected 2026-10-24). Status: checked against the abstract, the comparison with a conventional MEA and the discussion 2026-10-24.

Claims (tick `[x]` when you have checked the claim against the source):

- [ ] (1) [Timeline] UHD-CMOS-MEA field potential imaging.
- [ ] (2) [High-throughput/longitudinal] it is one of the two examples (with Altrocchi et al., 2023) of multi-parameter feature sets; its parameters include beat rate, inter-beat interval, short-term variability of conduction velocity and of intervals, excitation origins and propagation area.
- [ ] (3) [High-throughput/longitudinal] ultra-high-density CMOS-MEA platforms with close to a quarter million electrodes enable spatially resolved extraction of excitation origin counts, propagation area and conduction velocity maps in addition to conventional endpoints such as beat rate and inter-beat interval.
- [ ] (4) it detected doxorubicin-induced cardiotoxicity at 0.03 µM within 24 h, a concentration 10-fold lower than reported in earlier studies.
- [ ] (5) [FPDc] its recordings were of spontaneous beating without pacing, which the authors name as a limitation (a stimulation upgrade was under way).

Check 2026-10-24: (3) abstract p. 1 (236,880 electrodes, 5.9 × 5.5 mm); the paper does not report FPD or rate-corrected FPD for its own recordings (FPDc appears only in a table of thresholds from earlier studies, p. 15), so the earlier statements that it uses Fridericia-corrected FPD and extracts maps "in addition to conventional FPD" were removed. (4) p. 15: "detected doxorubicin-induced cardiotoxicity at a 10-fold lower concentration (0.03 µM) and within a shorter time frame (24 h)" compared with prior studies (>0.3 µM); in the direct comparison with the conventional MEA at 0.1 µM the conventional system detected a spike-amplitude reduction at 48 h and the CMOS-MEA a conduction velocity decline at 24 h (p. 12), so the earlier wording "an order of magnitude below those detectable by conventional MEA endpoints" was corrected.

## Maurissen et al. (2024)

Local file: `raw/maurissen-2024-mutation.pdf`; page `wiki/papers/maurissen-2024-mutation.md`. Status: checked against the abstract and Results 2026-10-24.

Claims (tick `[x]` when you have checked the claim against the source):

- [ ] (1) [Timeline] KCNH2 mutation phenotyping in 3D tissues.
- [ ] (2) [FPDc] the study uses Fridericia-corrected FPD (FPDcF).
- [ ] (3) [Model complexity] it combined gene-edited KCNH2 variants (N588D, N588K) with hiPSC-derived cardiac tissue sheets and MEA analysis to recapitulate long QT and short QT phenotypes, with differential repolarization and susceptibility to pharmacologically induced arrhythmias, in 3D isogenic tissues.
- [ ] (4) [Motivation] example of mechanistic electrophysiological phenotyping.

Check 2026-10-24: (2) p. 3 ("potential duration collected by Fridericia's formula (FPDcF) was significantly shortened for the SQT mutants (SQT22, 82 ± 18 ms) and prolonged for the LQT mutants (LQT26, 323 ms)"). (3) abstract p. 1; note that repolarization phenotypes were recorded in both CM monolayers and 3D cardiac tissue sheets, and the differential arrhythmia susceptibility in the 3D sheets.

## Park et al. (2025)

Local file: `raw/park-2025-cardiotoxicity.pdf`; page `wiki/papers/park-2025-cardiotoxicity.md` (one statement corrected 2026-10-24). Status: checked against the abstract and Methods 2026-10-24; the overlap with Park et al. (2026) checked 2026-10-18.

Claims (tick `[x]` when you have checked the claim against the source):

- [ ] (1) [Timeline] healthy vs LQTS hiPSC-CM CiPA drug comparison (2025).
- [ ] (2) [Intro] cited, with Blinova et al. and Altrocchi et al., for MEA use in cardiac safety pharmacology, drug discovery and disease modelling, and, with Blinova et al., for FPD metrics being integral to CiPA.
- [ ] (3) [FPDc] it reports corrected FPD (FPDc) from the vendor software but does not name the formula.
- [ ] (4) [Open pipelines] the vendor's Cardiac Analysis Tool was used for the analysis.
- [ ] (5) [High-throughput/longitudinal] it compared eight arrhythmia-inducing drugs (for example E4031, moxifloxacin, quinidine) across healthy and long QT syndrome–derived hiPSC-CM lines via MEA, demonstrating dose-dependent FPD and arrhythmogenic risk and disease-specific sensitivity to hERG blockade.
- [ ] (6) [High-throughput/longitudinal] it shares group, platform and apparently an LQT line with Park et al. (2026), so the two are one body of evidence.
- [ ] (7) [Motivation] example of mechanistic electrophysiological phenotyping.

Check 2026-10-24: (3) the text (p. 4, p. 8–11) says "corrected FPD (FPDc)" and "Axion's Cardiac Analysis Software", and never mentions Fridericia, so the earlier statement that it uses Fridericia-corrected FPD was replaced. (4) p. 4 and p. 7. (5) matches the abstract (p. 1). (2) the paper says CiPA "facilitated the use of hiPSC-CMs" (p. 2) and that its protocol is "in line with the CiPA core protocol" (p. 4).

## Park et al. (2026)

Local files: `raw/park-2026-genotype-ml.pdf` (+ supplementary methods and Data set S1); page `wiki/papers/park-2026-genotype-ml.md`. Status: checked (full text, supplementary, all eight figures) 2026-10-18.

Claims (tick `[x]` when you have checked the claim against the source):

- [ ] (1) [FPDc] the study uses Fridericia-corrected FPDc and other MEA parameters.
- [ ] (2) [FPDc] it trained neural-network, random-forest and gradient-boosting classifiers on these features from long QT and Brugada syndrome lines, took the rate correction as given, and did not test how the choice of correction affects performance.
- [ ] (3) [FPDc] it evaluated on a small test set of 15 drugs by repeated resampling.
- [ ] (4) [Open pipelines] the vendor's Cardiac Analysis Tool was used.
- [ ] (5) [High-throughput/longitudinal] the same group applied a similar MEA workflow to patient-derived LQTS and BrS lines and 28 compounds, reporting disease-specific drug sensitivities.
- [ ] (6) [High-throughput/longitudinal] the two Brugada lines consisted largely of atrial-like cells (100 % and 87.5 % atrial-like in Figure 3), so their comparison with ventricular-like normal lines is confounded by cell identity.
- [ ] (7) [High-throughput/longitudinal] overlap with Park et al. (2025): same group and platform, apparently the same long QT line (KCNH2 c.453delC).
- [ ] (8) [Maturation] patch-clamp data show ventricular-, atrial- and nodal-like cells in the normal lines (about 70 %, 20 % and 9 %).
- [ ] (9) The reference year is 2026 (volume 82; online July 2025).
- [ ] (9b) [Outlook] the machine-learning classifiers were trained on small datasets.
- [ ] (10) [Motivation] example of mechanistic electrophysiological phenotyping.
- [ ] (11) [Morphology] hiPSC-CM preparations contain nodal-like cells (patch-clamp data).
- [ ] (12) [Conclusion] genotype-specific risk models are one of the machine-learning uses in the studies examined.

## Pramudito et al. (2026)

Local file: `raw/pramudito-2026-ensemble.pdf` (git-ignored); page `wiki/papers/pramudito-2026-ensemble.md`. Status: checked (full text and figures) 2026-10-18.

Claims (tick `[x]` when you have checked the claim against the source):

- [ ] (1) [Timeline, Conclusion] stacking ensemble ML for TdP risk prediction; the Conclusion mentions "ensemble classifiers for TdP risk prediction" without naming the paper.
- [ ] (2) [FPDc] ΔFPDc has become a primary input feature for machine-learning proarrhythmic risk classifiers.
- [ ] (3) [FPDc] a stacking ensemble of random forest, gradient boosting and neural network classifiers outperformed each of its single constituent classifiers in predicting TdP risk on 16 held-out CiPA reference compounds.
- [ ] (4) [FPDc] it used ΔFPDc values already corrected in the multisite CiPA dataset, took the correction as given, and did not test the effect of the correction.
- [ ] (5) [FPDc] it evaluated on a small test set (16 drugs) by repeated resampling. Pointers: Tables 3 and 4 for the comparison; Datasets and Methods sections for the pre-corrected ΔFPDc.
- [ ] (6) [Outlook] the machine-learning classifiers were trained on small datasets (test set of 16 drugs).
- [ ] (7) [Motivation] example of proarrhythmia risk assessment.

## Ryynänen et al. (2018)

Local file: `raw/ryynanen-2018-single-cell-mea.pdf`; page `wiki/papers/ryynanen-2018-single-cell-mea.md`. Status: checked against the full text 2026-10-25 (text extraction; figures not viewed; supplementary videos not available). The researcher is not an author.

Claims (tick `[x]` when you have checked the claim against the source):

- [ ] (1) [Outlook] an MEA with transparent electrodes has been used to record the field potential and the video-based motion of the same single hPS-CM at the same time, although the two recordings were not automatically synchronised.
- [ ] (2) [Limitations] pre-2022 work cited as background for earlier multimodal work.
- [ ] (3) [FPDc] it corrected FPD with Bazett's formula.
- [ ] (4) [Declarations] several of its authors (with those of Vuorenpää et al., 2023) are colleagues of the researcher from the Centre of Excellence in Body-on-Chip Research ([CoEBoC](https://research.tuni.fi/coeboc/)) collaboration at Tampere University; the researcher is not an author (confirmed by the researcher, 2026-10-25).

Check 2026-10-25: (1) pp. 2–3 (aim: transparent electrodes enable simultaneous imaging and video analysis of the same cardiomyocytes), p. 5 ("Video and MEA recordings were taken manually at the same time; therefore, the recordings were not automatically synchronized in this study"), p. 7 ("beating frequencies and beat-to-beat intervals were similar when recorded with the two methods"; the electromechanical correlation is left to future studies). (3) p. 4 ("Bazett's formula was used to calculate the beat-rate-corrected FPD (cFPD)"). Single-cell electrodes are 80 µm, versus about 30 µm in conventional MEAs. Verify the numbers in Table I yourself (figures and table were read from extracted text only).

## Scheurer et al. (2025)

Local files: `raw/scheurer-2025-optical-ai.pdf` (+ supplementary); page `wiki/papers/scheurer-2025-optical-ai.md`. Status: checked against the abstract, Results and Discussion 2026-10-24.

Claims (tick `[x]` when you have checked the claim against the source):

- [ ] (1) [Timeline] video-based interpretable-AI maturity classifier.
- [ ] (2) [Maturation] a support vector machine with Shapley-value feature attribution distinguished early immature (day 21) from more mature (day 42, maturation medium) iPSC-CM cultures with 99.5 % accuracy on a hold-out test set of 46 videos, using only non-invasive, video-based beating features.
- [ ] (3) [Maturation] iPSC-CMs have an "immature, fetal-like phenotype" (cited here together with Correia et al., 2024).
- [ ] (4) [Maturation, Conclusion] the paper cites prior evidence (Hayakawa et al.) that field potential duration correlates strongly with contraction duration in iPSC-CMs (the paper does not say MEA was used, but the cited Hayakawa et al. (2014) used MEA; main.md now also cites that primary source).
- [ ] (5) [Maturation, Conclusion, our synthesis] the components of an MEA-native maturity classifier already exist separately but have not been combined.
- [ ] (6) [Limitations] example of a non-MEA modality.
- [ ] (7) [Outlook] video-based beating features were classified with an interpretable machine-learning model, without MEA data; trained on a small dataset (230 videos from four healthy lines).

Check 2026-10-24: (2) abstract p. 1 (230 videos; 10 features; accuracy 99.5 ± 1.1 %); p. 5 table (test set n = 46); "stage" was changed to "distinguish" because only two conditions are classified. (4) p. 9: "Hayakawa et al. simultaneously measured field potentials and motion in iPSC-CMs and observed strong correlations between field potential duration (FPD) and contraction duration [40]".

## Vuorenpää et al. (2023)

Local file: `raw/vuorenpaa-2023-mps-building-blocks.pdf`; page `wiki/papers/vuorenpaa-2023-mps-building-blocks.md`. Status: checked against the full text 2026-10-24 (text extraction; figures and tables not viewed). Two of the authors (Välimäki, Pekkanen-Mattila) are colleagues of the researcher from the [CoEBoC](https://research.tuni.fi/coeboc/) collaboration at Tampere University (Pekkanen-Mattila also co-authored Ryynänen et al., 2018); disclosed in the Declarations.

Claims (tick `[x]` when you have checked the claim against the source):

- [ ] (1) [Outlook] a review of cardiac microphysiological systems sees potential in combining different measurement modalities, which heart-on-chip systems can monitor concurrently.
- [ ] (2) [Outlook] it notes that continuous, multimodal measurements give a holistic data set for parameterising and validating computational models and that, to its authors' knowledge, integrative simulations of all building blocks of a microphysiological system had not been published.
- [ ] (3) [Declarations] several of its authors (with those of Ryynänen et al., 2018) are colleagues of the researcher from the Centre of Excellence in Body-on-Chip Research (CoEBoC) collaboration at Tampere University (the CoEBoC affiliation is on the paper's title page); the researcher is not an author (confirmed by the researcher, 2026-10-25).
- [ ] (4) [Motivation] the review describes the parametrization of action potentials and field potentials as well established and as enabling clear comparison of results between studies (section 6.1.1; a counterpoint to the 'source of variability' statement).

Check 2026-10-24: (1) section 6.1 (p. 12–13): "An advantage of heart MPS is the capability to include multiple sensors and electrodes for continuous measurement and monitoring of multiple measurement modalities, even concurrently" and "The reviewed studies show the potential of combining different measurement modalities, which may be fruitful for perfusion-enabled heart-on-chip studies as the field matures". (2) section 7 (p. 20): "the capability for continuous/long-term and multimodal measurements and concurrent sensing of the central functional readouts ... generate unprecedently holistic dataset for parameterization and validation of computational models"; section 7.3 (p. 21): "To our knowledge, multiphysics models that would put together all the building blocks of MPS in integrative simulations have not yet been published." The text contains no artificial intelligence, machine learning or digital twin discussion, and `main.md` does not attribute any to it. Counterpoint to synthesis item 1 (section 6.1.1: "The parametrization of APs and field potentials has been well established, enabling clear comparison of results between studies").

## Weiser-Bitoun et al. (2026)

Local file: `raw/weiser-bitoun-2026-physiomea.pdf`; page `wiki/papers/weiser-bitoun-2026-physiomea.md`. Status: checked against the abstract, Methods and Discussion 2026-10-24.

Claims (tick `[x]` when you have checked the claim against the source):

- [ ] (1) [Timeline] PhysioMEA, cardiac organoid BRV and 2D heatmaps (2026).
- [ ] (2) [Open pipelines] a platform for cardiac organoids whose software, source code and documentation are freely available (written in MATLAB and also distributed as a standalone executable), providing one-dimensional biomarkers (FPD, spike amplitude, peak-to-peak duration, inter-beat interval) across all recording electrodes, two-dimensional spatiotemporal heatmaps quantifying electrode-to-electrode variability in signal propagation, and beat rate variability (BRV) analysis with 45 standardised measures adapted from heart rate variability frameworks.
- [ ] (3) [Fiducial, Table 1, Table 2, Morphology] FPD is defined as the interval from the R peak to the T-wave peak, not the return to baseline.
- [ ] (4) [Morphology] with Ernault et al., cited for post-2022 studies increasingly reporting morphology-dependent analysis branches or document that T-wave morphology varies between preparations.
- [ ] (5) [Conclusion] analysis of inverted signals and exclusion of electrodes are examples of case-by-case morphology handling.

Check 2026-10-24: (2) abstract and p. 2 ("45 measures, including time domain, frequency domain, and nonlinear analysis", from the PhysioZoo toolbox, p. 3); availability sentence on p. 1–2 and "The source code was implemented in MATLAB", "run using MATLAB 2023b or as a standalone executable file (.exe)" (p. 3). (3) p. 3 ("FPD ... defined as the time difference between the R- and T-peaks"). (4) p. 3: inverted T waves are analysed on the inverted signal, low-amplitude R peaks via the inverted signal, and electrodes with inconsistent biomarker counts are excluded.

## Claims that rest on the author's own synthesis or are not cited

These are statements in `main.md` that no single reference supports, or that are generalisations from one or two studies. Judge them yourself and tick `[x]` when you have. Each item gives the section, the wording in `main.md`, what it is based on (source claims above, by source name), and how strong the support is in my reading: "none" means no source in the reference list supports it, "thin" means one or two studies, "inference" means a reasoned step from sources that is the author's own. Items 1–4 include the four methodological gaps of the Abstract and Conclusion.

- [ ] 1. [Abstract, Motivation] "the methods used to analyse FP signals have become a focus of attention as a possible source of inter-study variability" and, in bold, "signal analysis methods—particularly the definition of fiducial points in field potential (FP) waveforms—are a plausible source of variability and a possible limit to inter-study comparability", followed by "none of them measures how much variability analysis methods cause" and the counterpoint that a review of cardiac microphysiological systems describes the parametrization of action potentials and field potentials as well established (Vuorenpää et al., 2023). Revised 2026-10-24; your "needs citation(s)" comment is still in `main.md`. Based on: Mäki (2023) as the argument; Lee et al. (2024), Ernault et al. (2024) and Hayakawa et al. (2014) for FPD not tracking APD or the end points appearing to match different phases; Table 2 for the spread of conventions; Vuorenpää et al. (2023, section 6.1.1) and Blinova et al. (2018) (site variability smaller than cell-line and concentration effects, without testing analysis methods) as counter-evidence. Support: the revised wording claims only plausibility and says that no reviewed study measures the effect; supported as written (inference).
- [ ] 2. [Abstract, Conclusion] Gap 1: "FPD rate correction remains unsolved: the Fridericia formula, borrowed from clinical electrocardiography, lacks formal validation for the beating rate range and rate–FPD relationship characteristic of hiPSC-CM cultures. Developing a cell-type–specific correction formula — ideally derived from large multi-laboratory datasets — would substantially improve the reliability of FPDc as a pharmacological endpoint." Based on: Blinova et al. (2018) (stated as not thoroughly validated, rates accepted at 20–90 BPM); Clements et al. (2025) (20–80 BPM and an FPDc window); Guerrelli et al. (2024) (drift during equilibration); Pramudito et al. (2026), Park et al. (2026) and Lee et al. (2024) (correction taken as given or absent). Not based on any study that tested an alternative correction (none reviewed). "Borrowed from clinical electrocardiography" and "would substantially improve" are uncited. Support: thin for the validation gap, none for the recommendation (it is an opinion).
- [ ] 3. [Abstract, Conclusion] Gap 2 (revised 2026-10-24): "the absence, in the studies examined, of shared and validated waveform morphology classification criteria" and "shared, validated waveform morphology classification criteria were not identified: in the studies examined, morphology handling is described case by case (analysis of inverted signals, exclusion of electrodes, interpretation restricted to biphasic T waves ...) rather than through common criteria, whereas quantitative acceptance criteria exist for well acceptance ... Standardised morphology assessment analogous to these acceptance thresholds might reduce between-study variability at the data collection stage, which is a proposal and not a tested effect." Based on: Mäki (2023) (three morphologies, own method), Ernault et al. (2024) (biphasic T waves a minority), Weiser-Bitoun et al. (2026) (inverted signals, electrode exclusion), Lee et al. (2024) (small T waves), and for the acceptance criteria Blinova et al. (2018) and Clements et al. (2025). Support: thin; the first part is an absence claim limited to the studies examined, the last sentence is an untested proposal and is labelled as such.
- [ ] 4. [Abstract, Conclusion] Gap 3: "the transfer of 2D-calibrated analysis frameworks to 3D models and ultra-high-density platforms proceeds empirically: dedicated validation of fiducial definitions and conduction metrics in 3D cardiac tissues and spatially resolved MEA recordings is needed". Based on: Hwang et al. (2023) (3D variability), Maurissen et al. (2024) (3D tissue sheets needed for TdP-like waveforms), Matsuda et al. (2025), Mäki (2023)'s own limitation sentence, Botti et al. (2026) (2D model only). No study tested the transfer of fiducial definitions to 3D, so "proceeds empirically" and "is needed" are inferences. Support: thin. Gap 4: "hiPSC-CM maturation status lacks MEA-derived reference values: no validated benchmark currently allows a laboratory to report how mature its preparation was at the time of recording". Based on: Guerrelli et al. (2024), Fetterman et al. (2024), Correia et al. (2024), Scheurer et al. (2025), Clements et al. (2025) (QC, not staging), and the targeted search of 2 July 2026 recorded in `wiki/hipsc-cm-maturation.md`. An absence claim, as strong as that single search; it is not independently reproducible.
- [ ] 5. [Open pipelines, Conclusion] "Together, these platforms point toward reproducibility, transparency, and explicit reporting of analysis parameters, enabling investigators to critically assess how electrophysiological features are derived rather than relying on opaque vendor defaults." Based on: the five open platforms in Table 1 (Dunham, Lee, Weiser-Bitoun, Kabanov, Mäki). Counter-evidence in the paper itself: Park et al. (2025) and Park et al. (2026) used the vendor tool; there are no adoption data. Support: inference from five tools. The PhysioMEA wording is settled: `main.md` says its software, source code and documentation are freely available (written in MATLAB, also distributed as a standalone executable) instead of calling it "open-source MATLAB".
- [ ] 6. [Fiducial, Morphology] "the conventions differ" and "FPD values are therefore not directly comparable across tools without explicit knowledge of the underlying convention". Based on: Table 1 and Table 2 (Dunham, Lee, Weiser-Bitoun, Mäki). No study compared tools or conventions on the same data. Support: inference from the definitions.
- [ ] 7. [Fiducial, Table 2] "this implies that the T-wave peak — when the waveform is biphasic — is better anchored to APD90 ... than a baseline-return convention, which captures an interval extending into the repolarization tail beyond APD90; the two definitions measure different quantities rather than one being universally more correct", and the Table 2 entry "Full repolarization (APD95–100 range)". Based on: Ernault et al. (2024) for the T-peak–APD90 correlation (biphasic, NRVM); Mäki (2023) for the baseline-return definition. Hayakawa et al. (2014) add that the two end points appear to match different phases of the relaxation motion, which supports the claim that the definitions measure different quantities. The "APD95–100" range and "extends beyond APD90" are the author's reading, developed in `wiki/critical-assessment-maki-claims.md`; no source states them. Support: inference.
- [ ] 8. [Fiducial] "Such transparency is essential because differences in fiducial definitions can substantially influence measured drug effects and rate-corrected FPD or QT surrogates." Uncited reasoning. Weak hints: Blinova et al. (2018) (FPD of hERG blockers is hard to measure because the T wave shrinks), Lee et al. (2024). Support: none as stated.
- [ ] 9. [Morphology] (revised 2026-10-24) "The studies examined do not adopt identical rules, but two of them show an awareness of waveform heterogeneity: they report morphology-dependent analysis branches or document that T-wave morphology varies between preparations ... (Ernault et al., 2024; Weiser-Bitoun et al., 2026). Whether this differs from earlier studies was not assessed here." and "Pacemaker-like signals ... are described in hiPSC-CM cultures (Mäki, 2023), and hiPSC-CM preparations contain nodal-like cells (Park et al., 2026)." Based on the two studies named (checked against their texts), Mäki (2023) and the patch-clamp data of Park et al. (2026). Support: supported as written; the comparison with earlier studies is explicitly left open.
- [ ] 10. [Model complexity] (revised 2026-10-24) "Three-dimensional (3D) cardiomyocyte models ... are a setting in which FP analysis heuristics originally developed for two-dimensional monolayers may not transfer directly." and "The two studies discussed here state the model format explicitly; whether model-aware quality control and interpretation are becoming general practice was not assessed." Based on Hwang et al. (2023), Maurissen et al. (2024) and the caution in Mäki (2023). Support: the possibility is supported by those three sources (thin); the trend is explicitly not claimed.
- [ ] 11. [Maturation] "this maturation state is rarely quantified in MEA studies beyond loosely controlling culture duration" and "two laboratories could report different pharmacological endpoints for the same compound simply because their cultures differ in maturation state rather than in analysis methodology". A reasoned step from Guerrelli et al. (2024) (drift over culture time) and Ismaili et al. (2023); "rarely quantified" rests on the non-systematic selection. Support: inference.
- [ ] 12. [Maturation, Conclusion] "the components required for an MEA-native maturity classifier ... already exist in the literature, but have not yet been assembled into a validated, MEA-derived maturation reference value." Based on: Scheurer et al. (2025) and the field potential duration–contraction link it cites from earlier work (Hayakawa et al., named on the wiki page, not in the reference list), Correia et al. (2024), Fetterman et al. (2024). A synthesis proposed by the author; the FPD–contraction link is cited to its primary source (Hayakawa et al., 2014, read in full), which relates FPD to contraction duration per drug in non-arrhythmic conditions and does not study maturation. Support: inference.
- [ ] 13. [FPDc] "Despite this limitation, FPDc change (ΔFPDc) has become a primary input feature for machine-learning-based proarrhythmic risk classifiers", and the observations that Pramudito et al. (2026) and Park et al. (2026) "took the rate correction as given" and that "neither tested how the choice of correction affects classifier performance". Based on those two studies (checked against the full texts); the generalisation "has become a primary input feature" comes from two ML studies plus the predictors of Blinova et al. (2018). Support: checked for the two studies, thin for the generalisation.
- [ ] 14. [High-throughput/longitudinal] (revised 2026-10-24) "several of the post-2022 studies examined address high-throughput and longitudinal applications" and "In the studies examined, single conventional metrics are complemented by multi-parameter feature sets encompassing beat rate, beat-to-beat variability, conduction properties, and event-based descriptors (Altrocchi et al., 2023; Matsuda et al., 2025)." Based on Altrocchi et al. (2023), Matsuda et al. (2025) and Park et al. (2025, 2026); the trends are no longer claimed. Support: supported as worded for the studies named (thin: two studies for the feature sets).
- [ ] 15. [Motivation, Conclusion] (revised 2026-10-24) "In the studies examined, MEA recordings from hiPSC-CMs are used not only for basic measurements ... but also for mechanistic electrophysiological phenotyping (Maurissen et al., 2024; Park et al., 2025; Park et al., 2026), proarrhythmia risk assessment (Blinova et al., 2018; Pramudito et al., 2026) and chronic drug testing (Altrocchi et al., 2023) and recordings repeated over days in culture (Guerrelli et al., 2024)" (wording revised 2026-10-27) and "machine learning is used in several of the studies examined — ... (Pramudito et al., 2026), ... (Park et al., 2026), ... (Lee et al., 2024) — and it may become a more integral layer of cardiomyocyte MEA workflows." Based on the studies named. Support: supported as worded; the earlier trend wording ('increasingly', 'rapidly becoming') and the uncited 'AI-driven interpretation of UHD-MEA data' were removed.

- [ ] 16. [Outlook] Sensor fusion: "interpreting them jointly (sensor fusion), with AI support, could give a more complete picture of a preparation than any single signal, for example by adding MEA-derived parameters to a video-based classifier of maturation status", and "In these studies the modalities are mostly analysed separately or side by side". Based on: Altrocchi et al. (2023), Lee et al. (2024), Kabanov et al. (2026), Scheurer et al. (2025), Ryynänen et al. (2018), Hayakawa et al. (2014), Vuorenpää et al. (2023), Mäki (2023). No study tested joint interpretation by a fusion model; marked in the text as a hypothesis of the author. Support: none (stated as a hypothesis); the observation about separate analysis is thin.

- [ ] 17. [Outlook] Device separation: "with system identification or reverse engineering, the contribution of the MEA device ... could be estimated and removed, so that the remaining signal resembles the cellular AP more closely", electroporation data as a source of training and validation data, a digital twin of the recording ("a calibrated model of the cells, tissue and device, with parameters fitted to the measured signals"), and "it would also make FP-derived results from different hardware more comparable". Based on: Mäki (2023), Lee et al. (2024), Ernault et al. (2024), Botti et al. (2026) (a forward model not fitted to new measurements, the only digital-twin-like component cited), Vuorenpää et al. (2023) (multimodal data for parameterising and validating models; integrative models not yet published, to their knowledge). A proposal of the author; no reviewed study attempted it, and Ernault et al. suggest the FP also depends on neighbouring cells. The text adds, as the author's reasoning from extracellular recording theory with no source, that the recovery may be an ill-posed inverse problem because the FP is a weighted sum of the currents of many surrounding cells (added 2026-10-24). Support: none (stated as a hypothesis); the comparability claim is flagged in the text as untested.

## Corrections made in the 2026-10-24 verification

Each row is a change to `main.md` that followed from comparing a claim with its source; the earlier wording is quoted in short. Wiki pages that carried the same error were corrected as well (Hwang, Ismaili, Matsuda, Park 2025).

1. Introduction, first sentence: MEA use in cardiac safety pharmacology, drug discovery and disease modelling was cited to Ismaili et al. (2023), which does not mention MEAs; it now cites Blinova et al. (2018), Altrocchi et al. (2023) and Park et al. (2025).
2. Motivation: Ismaili et al. were described as discussing "ion channel expression, maturity, and recording conditions"; now "ion channel expression, resting membrane potential, and the identity of cell subtypes".
3. Open pipelines: added that open tools such as MultiElec and CardioMDA existed before 2022 (Lee et al., 2024, Table 3; Dunham et al., 2022, p. 2), because the text spoke of "the appearance of open ... pipelines" since 2022.
4. FPDc, first paragraph: the list of studies using Fridericia correction named Matsuda et al. (2025), whose recordings report no FPD or FPDc, and Park et al. (2025), who report FPDc without naming the formula; the list is now Altrocchi, Hwang, Maurissen and Park et al. (2026), with a note on Park et al. (2025).
5. Maturation: "fetal-like phenotype ... T-type Ca²⁺ current largely absent from mature adult ventricular myocytes, with ventricular-, atrial-, and nodal-like subtypes coexisting" cited to Ismaili et al.; Ismaili et al. say that ICa,T presence is not necessarily a sign of immaturity and that a mixed population is debated, and do not use "fetal-like"; the sentence was rewritten accordingly (fetal-like: Correia, Scheurer; subtype proportions: Park et al., 2026).
6. Maturation, Fetterman et al.: "systematically varied nine ... formulations" and the "vice versa" statement replaced by what the paper shows (single addition and subtraction of components; nine formulations compared by RNA-seq; fatty acids lower respiration without changing Ca²⁺ dynamics).
7. Maturation, Correia et al.: "pharmacokinetic correlation ... four orders of magnitude ... direct evidence that maturation status gates translational validity" replaced by a target-engagement correlation across 21 BCKDK inhibitors, roughly three orders of magnitude, evidence for this target; the Conclusion was restricted in the same way.
8. Maturation, Scheurer et al.: "stage hiPSC-CM maturity with over 99 % accuracy" replaced by the two-condition result with the test-set size.
9. Model complexity, Hwang et al.: "Experimental studies ... tissue thickness, cell–electrode coupling, and propagation patterns" replaced by the in silico finding that FP shapes depend on stimulation and electrode locations.
10. High-throughput, Altrocchi et al.: "anthracyclines" replaced by "an anthracycline (doxorubicin)".
11. High-throughput, Matsuda et al.: "in addition to conventional FPD" and "an order of magnitude below those detectable by conventional MEA endpoints" replaced by "conventional endpoints such as beat rate and inter-beat interval" and the 10-fold comparison with earlier studies at 0.03 µM within 24 h.
12. High-throughput, Kabanov et al.: "validated on HL-1 cells and hESC-derived cardiomyocytes" replaced by "tested on HL-1 cells and hESC-derived embryoid bodies".
13. Limitations (ii): Hwang et al. (2023) added to the simulation-based evidence.

Found by the check but not changed in `main.md` (judgement for you): the statements listed in the previous section, especially items 1, 3, 9, 10, 14 and 15, which are generalisations or trends without a source.

See also `docs/lint-fixes-2026-10-24.md` for the changes made in the lint pass of 2026-10-24 (wiki pages, index, new concept and method pages, and the softened sentences of `main.md` behind synthesis items 1, 3, 9, 10, 14 and 15).
