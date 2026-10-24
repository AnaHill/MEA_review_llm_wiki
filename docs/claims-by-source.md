# Claims in main.md, by source

A checklist for verifying the paper against its sources. Each source has one paragraph listing every claim that `main.md` attributes to it, with the section in brackets. Compiled 2026-10-18 from `main.md` as it stood after the review edits; regenerate or update it if `main.md` changes. Verify each claim in the local file named under the source (all files are in `raw/`; page and figure pointers are given where known). "Checked" below means checked against the full text during the 2026-10-18 session; "from the wiki page" means the claim was written from the ingest page (an earlier session) and has not been re-checked since, so those need your closest look.

Sections cited in brackets: Intro, Motivation, Scope, Timeline (Figure 1), Open pipelines (Transition section), Table 1, Fiducial (definitions section), Table 2, FPDc (rate correction), Maturation, Morphology (incl. Figure 2), Model complexity, High-throughput, Limitations, Conclusion.

<!-- temporary Finnish  version
Rakenne: tiedostossa on yksi osio per lähde (21 kpl), ja kunkin osion lopussa yksi kappale, jossa on jokainen väite, jonka main.md liittää kyseiseen lähteeseen. Väitteet on numeroitu ja merkitty osion tunnuksella (Intro, FPDc, Maturation jne.).

Jokaisessa osiossa: paikallinen tiedosto raw/-kansiossa, wikisivu ja tarkistustila.
Tarkistustila kertoo rehellisesti, mitä olen oikeasti tarkistanut täystekstistä.

 Tarkistettu on Blinova, Botti, Clements, Lee, Park 2026 ja Pramudito. Dunhamilta, Kabanovilta ja Weiser-Bitounilta olen tarkistanut vain FPD-määritelmän PDF:stä. 

Kaikki muut kohdat on kirjoitettu wikisivuilta aiemmissa sessioissa, eikä niitä ole tarkistettu uudelleen, joten ne tarvitsevat tarkimman silmäsi. Näitä ovat Altrocchi, Correia, Ernault, Fetterman, Guerrelli, Hwang, Ismaili, Matsuda, Maurissen, Park 2025 ja Scheurer.
-->


## Altrocchi et al. (2023)

Local file: `raw/altrocchi-2023-chronic.pdf`; page `wiki/papers/altrocchi-2023-chronic.md`. Status: from the wiki page.

Claims: (1) [FPDc] the study reports rate-corrected FPD with the Fridericia formula (listed among the studies that use it). (2) [High-throughput] it used 48-well MEA plates to evaluate acute (<2 h) and delayed (≥24 h) electrophysiological and cytotoxic effects of reference compounds, including tyrosine-kinase inhibitors, anthracyclines and ion-channel trafficking inhibitors, over 4 days, combining field potential recordings with impedance readouts. (3) [High-throughput] chronic and longitudinal MEA assays "have been validated for both acute and delayed cardiotoxicity" (this study is the example). (4) [High-throughput] it is an example of multi-parameter feature sets encompassing beat rate, beat-to-beat variability, conduction properties and event-based descriptors (cited together with Matsuda et al., 2025).

## Blinova et al. (2018)

Local file: `raw/blinova-2018-multisite.pdf`; page `wiki/papers/blinova-2018-multisite.md`. Status: checked (Methods, Results, Discussion; Figures 1, 2, 5–7 viewed).

Claims: (1) [Intro] the study is a source for FPD and related metrics being integral to the CiPA initiative (cited with Park et al., 2025). (2) [FPDc] it was a "blinded multisite CiPA study" that applied Fridericia correction to all 28 reference drugs across ten sites. (3) [FPDc] it states that the Fridericia formula was not thoroughly validated for hiPSC-CMs, and this is described as a recognised methodological gap. (4) [FPDc] spontaneous rates of hiPSC-CMs are "accepted at 20–90 BPM" in this study (inclusion criterion for baseline beating rate). (5) [Limitations] it is included as context only (2018, outside the 2022+ window). Pointers: Fridericia statement in the Data Analysis section of the Experimental Procedures; the 20–90 bpm criterion in the same section; ten sites and 28 drugs in the Summary.

## Botti et al. (2026)

Local file: `raw/botti-2026-insilico.pdf` (+ peer review history); page `wiki/papers/botti-2026-insilico.md`. Status: checked against the Europe PMC full text; compare with the PDF.

Claims: (1) [Model complexity] it is a two-dimensional bidomain model of a six-well MEA with phenotype-specific ventricular-like and atrial-like ionic models. (2) it simulated how the atrial-like fraction changes conduction velocity and repolarization. (3) it reproduced Brugada-like field potentials. (4) it compared simulated effects of four ion-channel blockers (mexiletine, nifedipine, dofetilide, E-4031) with previously published MEA data, without new experiments and with a fixed 30 % atrial-like fraction in the drug simulations. (5) it is a monolayer model and does not address the 3D question directly. (6) [Limitations] it is an example of simulation-based evidence. (7) The reference year is 2026 (issue 604(19), October 2026; online 11 May 2025).

## Clements et al. (2025)

Local file: `raw/clements-2025-aims-poster.pdf` (git-ignored); page `wiki/papers/clements-2025-aims-poster.md`. Status: checked (poster text read in full; layout not viewed).

Claims: (1) [FPDc] a recent proposed acceptance standard for hiPSC-ventricular-CM MEA assays builds the Fridericia correction into quality control by requiring an FPDc of 200–700 ms. (2) [FPDc] spontaneous rates are accepted at 20–80 BPM in that proposal. (3) [Maturation] it is an industry-led proposal (Axion BioSystems' "AIMS \#CM01", presented as a poster at ISSCR 2025) defining minimum well-acceptance criteria for spontaneous-beating hiPSC-ventricular-CM MEA assays: spike amplitude ≥ 0.5 mV and synchronized beating on at least half of the electrodes, a spontaneous beat period of 750–3000 ms, and FPDc of 200–700 ms. (4) it targets assay quality control, not maturation staging. (5) it has been presented as a conference poster and vendor document rather than a peer-reviewed methods paper. Pointers: the "AIMS \#CM01: Proposed standards" box; "Presented at ISSCR 2025, Hong Kong, June 11, 2025". The standard document on the vendor's website (last revised 2 December 2024) was read only through a web-fetch summary.

## Correia et al. (2024)

Local files: `raw/correia-2024-acc2.pdf` (+ supplementary); page `wiki/papers/correia-2024-acc2.md`. Status: from the wiki page.

Claims: (1) [Timeline] ACC2-inhibitor maturation medium improves in vitro-to-in vivo translatability (2024). (2) [Maturation] they developed a maturation medium, a galactose- and fatty-acid-based formulation with a triiodothyronine/IGF-1/dexamethasone cocktail, augmented with a small-molecule acetyl-CoA carboxylase 2 (ACC2) inhibitor. (3) it improved patch-clamp-defined electrophysiological maturity (a more hyperpolarized maximum diastolic potential, faster action potential upstroke velocity, and a six-fold increase in inward-rectifier K⁺ current) alongside metabolic and structural maturation. (4) an in vitro-to-in vivo pharmacokinetic correlation for a drug target across 21 compounds was achieved only in matured cells (Pearson r = 0.85, R² = 0.72, p < 0.0001, spanning about four orders of magnitude). (5) standard-medium cells largely failed to respond to the same compounds at all, so no correlation could be computed. (6) therefore maturation status gates translational validity. (7) [Conclusion] in vitro-to-in vivo translatability depends on maturation status. Pointer: Figure 7F for the correlation.

## Dunham et al. (2022)

Local file: `raw/dunham-2022-cardiopyemea.pdf`; page `wiki/papers/dunham-2022-cardiopyemea.md`. Status: FPD convention checked against the PDF text (section "Field potential duration calculation"); other claims from the wiki page.

Claims: (1) [Timeline] Cardio PyMEA, an open-source Python pipeline, 2022. (2) [Open pipelines] it is an open-source Python-based application for explicit analysis of cardiomyocyte MEA recordings including beat detection, pacemaker origin estimation, beat interval and amplitude analysis, local activation time, upstroke velocity and conduction velocity. (3) [Open pipelines] it is an early example of the transition away from vendor software. (4) [Fiducial, Table 1, Table 2] it measures FPD from the R wave to a T-wave endpoint located with a trapezoid-area algorithm (method of Vázquez-Seisdedos et al.), not validated against APD in the paper.

## Ernault et al. (2024)

Local file: `raw/ernault-2024-interpretation.pdf`; page `wiki/papers/ernault-2024-interpretation.md`. Status: from the wiki page.

Claims: (1) [Timeline, Table 2, Figure 2] T-wave peak equals APD90 for biphasic T waves, in NRVM. (2) [Fiducial] using simultaneous MEA and sharp-microelectrode recordings from neonatal rat ventricular myocyte (NRVM) monolayers, the peak time of the T wave in FPs correlates strongly with APD90, but only when the T wave displays a biphasic pattern. (3) the authors report that morphology in only a minority of recorded monolayers. (4) [Fiducial, our inference] the T-wave peak, when biphasic, is better anchored to APD90 than a baseline-return convention, which extends into the repolarization tail; the two definitions measure different quantities. (5) [Morphology] together with Weiser-Bitoun et al., it is cited for post-2022 studies increasingly reporting morphology-dependent exclusion criteria or analysis branches. (6) [Limitations] example of evidence in rat cells.

## Fetterman et al. (2024)

Local file: `raw/fetterman-2024-maturation.pdf`; page `wiki/papers/fetterman-2024-maturation.md`. Status: from the wiki page.

Claims: (1) [Timeline] functional, metabolic and transcriptional maturation shown independent. (2) [Maturation] they systematically varied nine cardiomyocyte culture-medium formulations. (3) functional (electrophysiology and excitation-contraction coupling), metabolic and transcriptional maturation are induced largely independently by different medium components. (4) interventions that improved action potential kinetics and Na⁺ current density had no effect on mitochondrial respiration, and vice versa. (5) therefore maturation is not a single scalar quantity and any MEA-derived reference value could characterise only the electrophysiological axis. (6) [Conclusion] the same independence is the reason a benchmark would be scoped to the electrophysiological axis. (7) [Limitations] example of a non-MEA modality.

## Guerrelli et al. (2024)

Local file: `raw/guerrelli-2024-hipscm.pdf`; page `wiki/papers/guerrelli-2024-hipscm.md`. Status: from the wiki page.

Claims: (1) [Timeline] temporal and spatial confounders quantified. (2) [FPDc] one study reported that the beating rate increases by more than 22 % and FPD decreases by about 8 % during a 20-minute recording equilibration period. (3) [High-throughput] the same numbers more precisely: beating rate +22.6 % and FPD −7.7 % over a 20-minute equilibration window. (4) [High-throughput] from 2 to 14 days in culture the beating rate decreases while FPD lengthens substantially. (5) [Maturation] FPD lengthens by about 257 ms and beating rate declines over days 2–14 in culture. (6) [Maturation] KCNJ2 (I_K1-encoding) gene expression rises 27.5-fold over 30 days. (7) [Maturation, our interpretation] this drift is consistent with ongoing maturation and rate correction alone does not address it. (8) [High-throughput] the findings highlight the need to standardise recording time points and culture age.

## Hwang et al. (2023)

Local file: `raw/hwang-2023-spheroids.pdf`; page `wiki/papers/hwang-2023-spheroids.md`. Status: from the wiki page.

Claims: (1) [Timeline] 3D spheroid geometry as a source of FP variability. (2) [Model complexity] experimental studies of hiPSC-CM spheroids have demonstrated that three-dimensionality contributes substantially to FP variability, reflecting differences in tissue thickness, cell–electrode coupling and propagation patterns.

## Ismaili et al. (2023)

Local file: `raw/ismaili-2023-hamburg.pdf`; page `wiki/papers/ismaili-2023-hamburg.md`. Status: from the wiki page.

Claims: (1) [Timeline] Hamburg perspective on hiPSC-CM limitations. (2) [Intro] MEA recordings of hiPSC-CMs are widely used in cardiac safety pharmacology, drug discovery and disease modelling. (3) [Motivation] it discusses, from a critical perspective, the broader methodological and biological challenges of hiPSC-CMs as electrophysiological models, including ion channel expression, maturity and recording conditions. (4) [Maturation] hiPSC-CMs retain a fetal-like phenotype, expressing funny current (If) and T-type Ca²⁺ current largely absent from mature adult ventricular myocytes, with ventricular-, atrial- and nodal-like subtypes coexisting in the same preparation.

## Kabanov et al. (2026)

Local file: `raw/kabanov-2026-cardioscripts.pdf`; page `wiki/papers/kabanov-2026-cardioscripts.md`. Status: "T peaks detected" checked against the PDF text; other claims from the wiki page.

Claims: (1) [Timeline] CardioScripts, combined AFM and MEA electromechanical analysis. (2) [High-throughput] CardioScripts is an open-source Python toolbox validated on HL-1 cells and hESC-derived cardiomyocytes. (3) it integrates MEA field potential analysis with simultaneous atomic force microscopy (AFM) recordings to quantify electromechanical coupling and decoupling. (4) dose-dependent lidocaine effects show that electrical and mechanical signals can dissociate in ways that neither modality detects alone. (5) [Table 1] Python; also named Myopyth; FPD end not reported, T peaks are detected.

## Lee et al. (2024)

Local file: `raw/lee-2024-cardiomea.pdf`; page `wiki/papers/lee-2024-cardiomea.md`. Status: checked against the Europe PMC full text (Table 1, Table 3, Results); compare with the PDF.

Claims: (1) [Timeline] CardioMEA platform, scalable open analysis. (2) [Open pipelines, Table 1] it was built for high-density MEA data, processes files in parallel into an SQL database, has a web-based dashboard, extracts features from extracellular and intracellular-like (electroporation-derived) signals, and has an automated machine-learning module ranking features that separate diseased from control lines; Python. (3) [Fiducial, Table 1, Table 2] FPD is measured from the R spike to the T-wave peak. (4) [Fiducial] in iCell cardiomyocyte HD-MEA recordings, R-to-T-peak FPD correlated only minimally with APD50 and APD90 measured from intracellular-like signals on the same electrodes, which the authors attribute to small, noisy T waves. (5) [FPDc, Table 1] the published feature set contains FPD but no rate-corrected FPD. Pointers: Table 1 (features), Figure 4 (correlations), Table 3 (platform comparison).

## Mäki (2023, version v3)

Local file: `raw/maki-2023-opinion.html`; page `wiki/papers/maki-2023-opinion.md`; also `wiki/critical-assessment-maki-claims.md`. Status: the 3D limitation sentence and the inversion statements checked against the HTML; others from the wiki page. This is the author's own opinion paper.

Claims: (1) [Abstract, Motivation, Scope] it is used as the evaluative framework. (2) [Motivation] it challenged the physiological validity of commonly used FP annotation conventions, arguing that the widely adopted peak-to-peak FPD definition is often mismatched to the underlying electrophysiology. (3) it argues that the first positive FP peak in a propagating hiPSC-CM monolayer may reflect depolarization of neighbouring cells rather than the locally recorded cardiomyocyte. (4) it argues that FPD end should be measured to the return of the signal to baseline rather than the repolarization peak. (5) [Fiducial] it describes an algorithm: beat-aligned segmentation, averaging across beats to reduce noise, threshold-based identification of depolarization onset relative to FP amplitude, FPD end as return of the signal toward baseline. (6) [Morphology] morphology-aware handling of pacemaker-like signals and waveform inversion for "only high peak" cases, internally validated in that work but not independently replicated. (7) [Model complexity] its caution that analysis frameworks optimised for 2D cultures may not be directly transferable to 3D systems (its Limitations section says the analysis "might not be as easily … extrapolated to the 3D model"). (8) [Table 1, Table 2, Figure 2] DatAnalyzer (Python): FPD from depolarization onset to baseline return; the table also characterises the "peak-to-peak" convention as common and criticised in this paper. (9) [Declarations] the first version was posted on Zenodo in 2023; the text assessed is v3, published 23 June 2026.

## Matsuda et al. (2025)

Local file: `raw/matsuda-2025-uhd.pdf`; page `wiki/papers/matsuda-2025-uhd.md`. Status: from the wiki page.

Claims: (1) [Timeline] UHD-CMOS-MEA field potential imaging. (2) [FPDc] the study uses Fridericia-corrected FPD (FPDcF). (3) [High-throughput] it is an example of multi-parameter feature sets (with Altrocchi et al., 2023). (4) [High-throughput] ultra-high-density CMOS-MEA platforms with close to a quarter million electrodes enable spatially resolved extraction of excitation origin counts, propagation area and conduction velocity maps in addition to conventional FPD. (5) it demonstrated sensitivity for doxorubicin-induced cardiotoxicity at concentrations an order of magnitude below those detectable by conventional MEA endpoints.

## Maurissen et al. (2024)

Local file: `raw/maurissen-2024-mutation.pdf`; page `wiki/papers/maurissen-2024-mutation.md`. Status: from the wiki page.

Claims: (1) [Timeline] KCNH2 mutation phenotyping in 3D tissues. (2) [FPDc] the study uses Fridericia-corrected FPD (FPDcF). (3) [Model complexity] it combined gene-edited KCNH2 variants (N588D, N588K) with hiPSC-derived cardiac tissue sheets and MEA analysis to recapitulate long QT and short QT phenotypes, with differential repolarization and susceptibility to pharmacologically induced arrhythmias, in 3D isogenic tissues.

## Park et al. (2025)

Local file: `raw/park-2025-cardiotoxicity.pdf`; page `wiki/papers/park-2025-cardiotoxicity.md`. Status: from the wiki page; the overlap with Park et al. (2026) checked in the 2026-10-18 session.

Claims: (1) [Timeline] healthy vs LQTS hiPSC-CM CiPA drug comparison (2025). (2) [Intro] cited, with Blinova et al., for FPD metrics being integral to CiPA. (3) [FPDc] the study uses Fridericia-corrected FPD (FPDcF). (4) [Open pipelines] the vendor's Cardiac Analysis Tool was used for the analysis. (5) [High-throughput] it compared eight arrhythmia-inducing drugs (for example E4031, moxifloxacin, quinidine) across healthy and long QT syndrome–derived hiPSC-CM lines via MEA, demonstrating dose-dependent FPD and arrhythmogenic risk and disease-specific sensitivity to hERG blockade. (6) [High-throughput] it shares group, platform and apparently an LQT line with Park et al. (2026), so the two are one body of evidence.

## Park et al. (2026)

Local files: `raw/park-2026-genotype-ml.pdf` (+ supplementary methods and Data set S1); page `wiki/papers/park-2026-genotype-ml.md`. Status: checked (full text, supplementary, all eight figures).

Claims: (1) [FPDc] the study uses Fridericia-corrected FPDc and other MEA parameters. (2) [FPDc] it trained neural-network, random-forest and gradient-boosting classifiers on these features from long QT and Brugada syndrome lines, took the rate correction as given, and did not test how the choice of correction affects performance. (3) [FPDc] it evaluated on a small test set of 15 drugs by repeated resampling. (4) [Open pipelines] the vendor's Cardiac Analysis Tool was used. (5) [High-throughput] the same group applied a similar MEA workflow to patient-derived LQTS and BrS lines and 28 compounds, reporting disease-specific drug sensitivities. (6) [High-throughput] the two Brugada lines consisted largely of atrial-like cells (100 % and 87.5 % atrial-like in Figure 3), so their comparison with ventricular-like normal lines is confounded by cell identity. (7) [High-throughput] overlap with Park et al. (2025): same group and platform, apparently the same long QT line (KCNH2 c.453delC). (8) The reference year is 2026 (volume 82; online July 2025).

## Pramudito et al. (2026)

Local file: `raw/pramudito-2026-ensemble.pdf` (git-ignored); page `wiki/papers/pramudito-2026-ensemble.md`. Status: checked (full text and figures).

Claims: (1) [Timeline, Conclusion] stacking ensemble ML for TdP risk prediction; ensemble classifiers for TdP risk are named as an example of machine learning becoming integral to MEA workflows. (2) [FPDc] ΔFPDc has become a primary input feature for machine-learning proarrhythmic risk classifiers. (3) [FPDc] a stacking ensemble of random forest, gradient boosting and neural network classifiers outperformed each of its single constituent classifiers in predicting TdP risk on 16 held-out CiPA reference compounds. (4) [FPDc] it used ΔFPDc values already corrected in the multisite CiPA dataset, took the correction as given, and did not test the effect of the correction. (5) [FPDc] it evaluated on a small test set (16 drugs) by repeated resampling. Pointers: Tables 3 and 4 for the comparison; Datasets and Methods sections for the pre-corrected ΔFPDc.

## Scheurer et al. (2025)

Local files: `raw/scheurer-2025-optical-ai.pdf` (+ supplementary); page `wiki/papers/scheurer-2025-optical-ai.md`. Status: from the wiki page.

Claims: (1) [Timeline] video-based interpretable-AI maturity classifier. (2) [Maturation] an interpretable machine-learning classifier (a support vector machine with Shapley-value feature attribution) can stage hiPSC-CM maturity with over 99 % accuracy using only non-invasive, video-based beating features. (3) [Maturation, Conclusion] the paper cites prior evidence that MEA-derived FPD correlates strongly with contraction duration in hiPSC-CMs (the primary source is not cited in main.md; the wiki page names Hayakawa et al.). (4) [Maturation, Conclusion, our synthesis] the components of an MEA-native maturity classifier already exist separately but have not been combined. (5) [Limitations] example of a non-MEA modality.

## Weiser-Bitoun et al. (2026)

Local file: `raw/weiser-bitoun-2026-physiomea.pdf`; page `wiki/papers/weiser-bitoun-2026-physiomea.md`. Status: the FPD definition (R peak to T peak) checked against the PDF text; other claims from the wiki page.

Claims: (1) [Timeline] PhysioMEA, cardiac organoid BRV and 2D heatmaps (2026). (2) [Open pipelines] an open-source MATLAB platform for cardiac organoids providing one-dimensional biomarkers (FPD, spike amplitude, peak-to-peak duration, inter-beat interval) across all recording electrodes, two-dimensional spatiotemporal heatmaps quantifying electrode-to-electrode variability in signal propagation, and beat rate variability (BRV) analysis with 45 standardised measures adapted from heart rate variability frameworks. (3) [Fiducial, Table 1, Table 2, Morphology] FPD is defined as the interval from the R peak to the T-wave peak, not the return to baseline. (4) [Morphology] with Ernault et al., cited for post-2022 studies increasingly reporting morphology-dependent exclusion criteria or analysis branches.

## Claims that rest on the author's own synthesis rather than a single source

These are statements in `main.md` that no single reference supports and that you should judge yourself: 
1. the four "methodological gaps" in the Conclusion and Abstract; 
2. the statement that open analysis platforms point toward reproducibility and transparency; 
3. the observation that FPD conventions differ across open platforms and are therefore not directly comparable; 
4. the inference that an MEA-native maturity reference could be assembled from existing components; 
5. and the observations about the Park and Pramudito studies' resampling and uncorrected-correction assumptions (these are derived from the papers but are the author's reading).
