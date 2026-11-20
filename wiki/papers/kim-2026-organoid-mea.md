---
tags: [3d-model, waveform-morphology, disease-model, multimodal]
---

# Conformable Microelectrode Arrays Integrated with a Scoop-Shaped Slide-Well for Dynamic Electrophysiological Profiling of Patient-Derived Cardiac Organoids

**Authors:** Kim, Y. S., Jeong, J., Heo, G., Kwon, Y. W., Lee, J., Jeong, Y. J., Park, G. T., Jeong, S., Hwang, K. W., Choi, M., Shin, J., Hong, S. W., & Kim, J. H.  
**Year:** 2026  
**Venue:** *Advanced Science*, 13(31), e14365  
**File:** [[raw/kim-2026-organoid-mea.pdf]] (supplement: [[raw/kim-2026-organoid-mea-supplementary.docx]])  
**DOI:** 10.1002/advs.202514365  
**Affiliation:** Pusan National University, Republic of Korea (with Seoul National University); open access, CC BY

Suggested by an external AI reviewer of `main.md` (see `docs/feedback1-from-AI-reviewer.md`, 2026-11-20) as one of two missing 3D MEA developments. The DOI, title, author list, journal and volume were checked against the Crossref record before the PDF was obtained. Page written 2026-11-20 from the full text (16 pp.), the supplement and Figures 1 and 4.

## Contribution

A six-channel MEA, about 4 µm thick, is bonded by capillary adhesion into the concave floor of a PDMS "scoop" well, so that a millimetre-scale cardiac organoid rolls down the incline and settles on the electrodes under gravity. The claim is a geometric one: conformal electrode–tissue contact with a curved 3D construct, where a rigid planar MEA touches it only at points. The platform is applied to organoids from the urine-derived hiPSCs of two healthy donors and two Duchenne muscular dystrophy (DMD) patients, with simultaneous video-based motion analysis and an E-4031 challenge.

## Methodology

- **Device:** SU-8 / Cr-Au / PEDOT:PSS multilayer, about 4 µm thick, released from a Si/SiO₂ wafer by BOE etching and attached to the PDMS well by a drying water droplet; tether structures at the centre take up the strain of conforming to the curved surface (FEA in COMSOL, Fig. 1f, Fig. S26). Six recording electrodes, 20 µm diameter, 125 µm centre-to-centre, plus one enlarged stimulation electrode (Fig. 1k).
- **Two well geometries** share the same MEA: a hemispherical scoop for the systematic studies and a tapered microfluidic end for Figure 4 (Experimental Section 5.2).
- **Signal processing (Section 5.6):** fourth-order Butterworth notch at 59–61 Hz, downsampling to 500 Hz, discrete wavelet transform denoising (coif5, soft thresholding, rigrsure). **That is the whole of the EFP analysis description.**
- **Motion analysis:** grayscale frames at 0.15 s intervals, a manually drawn ROI, inter-frame absolute pixel differences.
- **Cells:** organoids from urine-derived hiPSCs, two healthy donors and two DMD patients (nonsense c.8994C>T and frameshift c.6655_6656delGA); scaffold-free, no Matrigel; characterised by WES, scRNA-seq, Western blot, qPCR and Fluo-4 calcium imaging.
- **Drug:** E-4031 at 10, 100 and 1000 nM.
- **Coupling check (Fig. S25):** impedance magnitude at 300 Hz in culture medium before and after organoid placement, 16 channels, paired t-test.

## Findings

- Six-channel EFPs (about 1 mV) were recorded from organoids, and the channels differed markedly in amplitude and waveform shape. The authors read this as region-specific ion channel expression (p. 6) and as evidence that multipoint conformal interfacing is needed rather than planar single-site recording (p. 10).
- E-4031 prolonged the field potential duration (FPD) in normal organoids and at 1000 nM produced early-afterdepolarization-like activity; DMD organoids developed arrhythmia already at 10 nM and chaotic activity at 1000 nM.
- Mechanically, E-4031 at 100 nM broke up the contraction pattern of DMD organoids (Fig. 4i,j), which the authors call electromechanical dissociation.
- DMD organoids were larger, lacked CD31-positive vascular structures, and showed upregulated *SCN5A* with downregulated *KCNJ2*, *KCNJ12*, *CACNA1C* and *RYR2*; scRNA-seq gave a profibrotic ECM signature in their ventricular cardiomyocytes. *KCNH2* transcript levels did not differ, so the authors attribute the E-4031 hypersensitivity to reduced repolarization reserve rather than to hERG expression.
- Impedance at 300 Hz fell consistently across 16 channels when an organoid made contact (Fig. S25).

## Limitations

- **No FPD fiducial definition anywhere.** Neither the Experimental Section nor the supplement (whose Supplemental Methods cover only WES, bulk RNA-seq and PPI analysis) says where the FPD begins or ends, or how a peak is detected. "Prolonged FPD" is read off representative traces; no FPD or FPDc value is reported for an organoid, and Figures 1l,m and 4e,g,h carry no fiducial markers or measured intervals.
- **Repolarization metrics are reported case by case.** The authors state that they report repolarization-related metrics "only where waveform morphology supports interval quantification" (p. 12) and that the fragmented, non-stationary DMD waveforms violate the assumptions of standard peak detection and may require expert-guided annotation. No criterion is given for when a waveform qualifies.
- **The calcium imaging does not validate the EFPs electrode by electrode.** Fluo-4 imaging compares whole normal and DMD organoids (Fig. S21c); it is not a per-electrode comparison with the field potential, although the abstract's "validated by calcium imaging" invites that reading.
- **Channel differences are attributed, not tested.** The inter-channel variation is interpreted as regional biology; contact quality as an alternative explanation is not tested, even though Fig. S25 shows that contact changes the impedance.
- Six electrodes per organoid; n for the electrophysiology is not stated per figure; representative traces throughout.
- **Contact is still from one side.** The electrodes lie in the floor of the well, so the organoid is contacted on its lower curved surface, not encapsulated.
- The Conclusion claims suitability for "targeted high-throughput drug screening" while the Discussion names manual loading and inter-operator variability as a throughput bottleneck.
- Figure S22, the 2D cardiomyocyte comparison, uses an adaptive threshold spike detector and a stable/unstable beat classification, but the thresholds are not given.

## Relevance to our paper

Supports the 3D section and two of the four gaps, without closing either.

- **Gap 3 (2D-calibrated analysis in 3D and spatially resolved settings).** A 2026 hiPSC-CM study that advances the *recording* geometry — conformal contact with a curved organoid, confirmed by an impedance drop — while stating no analysis convention at all. It is therefore evidence that acquisition is moving ahead of analytical validation, which is the gap. It does not overturn [[wiki/papers/lin-2023-nanoelectronics.md]]: contact is still at one surface.
- **Gap 2 (morphology criteria).** "Only where waveform morphology supports interval quantification" is a clean instance of case-by-case morphology handling, and the authors' remark that diseased waveforms break standard peak detection is the same problem the review raises, stated by other authors.
- **Discussion, separating the recording system from the cellular signal.** Fig. S25 measures impedance at 300 Hz before and after contact and uses it as a coupling check. [[wiki/papers/altrocchi-2023-chronic.md]] used impedance as a cytotoxicity readout; main.md then asks whether such a channel could indicate FP changes caused by altered coupling. Kim et al. use impedance for exactly that purpose, on contact rather than on detachment, which is one step closer to the idea — though they do not test whether FP features change with contact quality.

Not used for: conduction velocity or propagation mapping (none reported), maturation, rate correction (no FPDc).

## See also
- [[wiki/3d-models.md]]
- [[wiki/fpd-end-conventions.md]] — a 3D organoid study that states no convention at all
- [[wiki/multimodal-measurement.md]] — EFP with video motion analysis, and impedance as a contact check
- [[wiki/papers/lin-2023-nanoelectronics.md]] — the one-surface contact limitation that this device partly addresses
- [[wiki/papers/weiser-bitoun-2026-physiomea.md]] — the other 2026 organoid MEA study: analysis convention stated, geometry planar
- [[wiki/papers/maurissen-2024-mutation.md]] — the counterexample where FPD was measured and compared between 2D and 3D
- [[wiki/papers/altrocchi-2023-chronic.md]] — impedance recorded alongside the field potential
- [[wiki/papers/park-2026-genotype-ml.md]] — patient-derived disease lines on MEA
