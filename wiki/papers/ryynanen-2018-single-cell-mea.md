---
tags: [multimodal, video, single-cell, field-potential]
---

# Microelectrode array for noninvasive analysis of cardiomyocytes at the single-cell level

**Authors:** Tomi Ryynänen, Mari Pekkanen-Mattila, Disheet Shah, Joose Kreutzer, Pasi Kallio, Jukka Lekkala, Katriina Aalto-Setälä (the first two contributed equally)
**Year:** 2018
**Venue:** Japanese Journal of Applied Physics 57, 117001 (regular paper, open access CC BY 4.0; published online 19 October 2018)
**File:** [[raw/ryynanen-2018-single-cell-mea.pdf]]
**DOI:** 10.7567/JJAP.57.117001

Note: ingested 2026-10-25 from the full text (8 pages, text extraction; figures not viewed; the online supplementary videos were not available). Before 2022, so it is background in main.md (Limitations vi). The researcher is not an author. Funding stated: Business Finland, the Council of Tampere Region and two foundations. Replaces the conference contribution of Välimäki et al. (2021) that was cited earlier.

## Contribution
A custom MEA platform for recording the field potential from single beating human pluripotent stem cell-derived cardiomyocytes (hPS-CMs), with electrode size and position optimised for single cells. With transparent indium tin oxide (ITO) electrodes the same cell can also be imaged, so that image-based analysis of its mechanical beating can be done simultaneously with the electrical recording.

## Methodology
- **Electrode layouts:** Layout 1 (long finger electrodes), Layout 2 (circular, oval and split electrodes of different sizes) and Layout 3 (80 µm circular electrodes around the perimeter of a 3.5 mm culture opening, centre-to-centre distance 250–460 µm, some with stripes, holes or split halves), in opaque titanium and transparent ITO versions; conventional MEAs have about 30 µm electrodes at about 200 µm pitch.
- **Characterisation:** impedance at 1 kHz about 250 kΩ (ITO) and 190 kΩ (Ti); baseline RMS noise 5.4 ± 0.9 µV for both; electrodes above 10 µV RMS were excluded; the impedance was 5–10 times that of standard 30 µm porous-material electrodes.
- **Cells:** hPS-CMs differentiated from a healthy iPSC line (UTA.04602.WT) by temporal modulation of Wnt signalling; about 200–300 cells per well plated so that at most one cell lands on an electrode.
- **Recording:** field potential 5–11 days after plating, 30 s at 20 kHz with a conventional MEA amplifier (MEA2100), during spontaneous beating and after 50–100 nM E-4031 (2 min incubation); an in-house analysis module in Origin extracted beats per minute, inter-beat interval and FPD; **Bazett's formula** gave the rate-corrected FPD (cFPD).
- **Video:** phase-contrast video of the same cells (60 fps, 20×, 30 s), analysed with CellVisus software (digital image correlation) for contraction duration, time of contraction, relaxation duration, incomplete relaxation time and time of relaxation. **Video and MEA recordings were taken manually at the same time and were not automatically synchronised.**
- Immunostaining for cardiac troponin T confirmed that the cells on the electrodes were cardiomyocytes.

## Findings
- Layout 1 gave mostly noise (one cell on a 100 µm test electrode gave a preliminary signal); Layout 2 gave signals from some electrodes; with Layout 3 the electrical activity of all beating cells on electrodes was detectable (4 MEA chambers, 1–4 signals per chamber).
- Signals were clear enough to measure beating rate, beat-to-beat interval and FPD, and resembled those of hPS-CM aggregates on commercial MEAs.
- E-4031 prolonged the FPD at the single-cell level in the examples of Table I (for example cell 4: FPD 604 to 829 ms, cFPD 673 to 786 ms; cell 5: 1563 to 1821 ms, cFPD 844 to 858 ms; cell 6: 702 to 825 ms, cFPD 714 to 735 ms).
- On the transparent electrodes the beating rate and beat-to-beat interval from the MEA and from the video were similar (Table I, cells 1–3). The authors conclude that the platform records electrophysiological and biomechanical data simultaneously from single cells; opaque electrodes allowed beating to be seen but not video analysis.

## Limitations
Stated by the authors: the correlation between the electrical and mechanical function of single cells was left to future studies; the impedance of the transparent electrodes is higher than that of conventional electrodes and lowering it without losing transparency is difficult; the stimulation (pacing) capability of the electrodes was not studied; only a small share of the plated cells ended up on electrodes (selective patterning of matrix proteins or cell printing are suggested).

Our observations (not from the paper): the evidence is a small number of representative cells (Table I, cells 1–6) from four chambers and one iPSC line; the two recordings were not synchronised, so beat-by-beat electromechanical timing could not be derived; the rate correction is Bazett's, not Fridericia's.

## Relevance to our paper
Cited in main.md (Discussion and future outlook) as an example of simultaneous field potential and video-based motion recording from the same single hPS-CM (sensor-fusion paragraph), in Limitations (vi) as pre-2022 background, and in the rate-correction paragraph as a study that used Bazett's formula. It replaces the conference contribution of Välimäki et al. (2021), for which only a portal record was available.

## See also
- [[wiki/papers/hayakawa-2014-motion-fp.md]]
- [[wiki/papers/vuorenpaa-2023-mps-building-blocks.md]]
- [[wiki/papers/kabanov-2026-cardioscripts.md]]
- [[wiki/multimodal-measurement.md]]
