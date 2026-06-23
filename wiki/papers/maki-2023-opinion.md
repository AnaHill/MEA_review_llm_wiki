# Opinion: The correct way to analyze FP signals

**Authors:** Antti-Juhana Mäki, PhD  
**Year:** 2023  
**Venue:** Zenodo (report, version v3; iterative document with version control)  
**File:** [[raw/maki-2023-opinion.html]]  
**DOI:** 10.5281/zenodo.20807245

> **Note:** This is an opinion / methodology paper by the same author as main.md. The document is explicitly designed to be iterative and versioned for transparency. The HTML file contains embedded base64 figures and a full reference list.

## Contribution

Argues that the two most common conventions for measuring FPD from hiPSC-CM MEA recordings are physiologically wrong, and proposes an alternative algorithmic method that is implemented in the open-source *DatAnalyzer* tool (GitHub: https://github.com/AnaHill/DatAnalyzer).

The two challenged conventions:
1. Using the **first positive peak** as the start of FPD — this peak reflects depolarization of *neighboring* cells, not the locally recorded cell
2. Defining FPD end at the **repolarization peak** — the signal should instead be measured until it returns to baseline, capturing the full repolarization wave (RW)

## Methodology

Opinion paper with annotated figures demonstrating the proposed analysis on real hiPSC-CM FP signals. No new experimental data are collected; the argument is made by annotated waveform examples and comparison to AP signals from the literature. The method is implemented in *DatAnalyzer*.

**Algorithmic steps (non-pacemaker standard case):**
1. Beat-aligned segmentation of the raw recording
2. Beat averaging across multiple beats to reduce noise
3. Baseline amplitude A0 estimated from the pre-beat flat region
4. **FPD start (point 0'):** defined as the time when the signal drops 10% below baseline toward the negative (depolarization) peak: A0 − 0.1 × |Apeak|
5. **Depolarization time (tdep):** from point 0' to the minimum of the negative depolarization peak (determined from filtered signal to avoid noise effects)
6. **FPD end (point 4'):** defined as the time when the signal, after the repolarization peak, returns to within 10% of baseline: A0 + 0.1 × (Arep − A0)
7. **FPD = time from point 0' to point 4'**

**Morphology cases handled:**

| Morphology | Diagnosis | Handling |
|---|---|---|
| High peak + depolarization trough + repolarization peak | Non-pacemaker cell | Standard analysis above |
| No high peak | Pacemaker cell | Start FPD from when signal begins drifting; no high peak to skip |
| Only high peak (no depolarization trough) | Distance between the dominant cell and the measurement electrode | Flip signal (multiply by −1), then analyze as pacemaker cell |

## Findings

- Conventional peak-to-peak FPD systematically underestimates the true repolarization duration because it stops at the repolarization peak rather than baseline return
- The first positive high peak is a neighbor-cell depolarization artifact; including it as FPD start shifts the measurement window and conflates conduction delay with repolarization duration
- Pacemaker-like cells (no high peak) require different fiducial logic; most published analysis pipelines do not describe how these waveforms are handled, creating an undisclosed source of inter-study variability
- The "only high peak" morphology is addressable by signal inversion before applying pacemaker-cell analysis

## Limitations

- The method is defined for 2D hiPSC-CM cultures; applicability to 3D spheroids, cardiac tissue sheets, or high-density electrode arrays is not formally addressed
- The 10% threshold for start/end detection is empirically chosen; no sensitivity analysis is provided
- The comparison to AP signals is qualitative (figure-based), not a quantitative validation study

## Relevance to our paper

This is the evaluative anchor for main.md. The review explicitly uses this opinion paper as a framework against which post-2022 studies are assessed. Specific elements cited in main.md:
- Peak-to-peak vs. baseline-return FPD definition (fiducial definitions section)
- Morphology-aware handling of pacemaker-like and inverted signals (morphology section)
- Caution that 2D-calibrated heuristics may not transfer to 3D systems (3D section)

## See also

- [[wiki/papers/ernault-2024-interpretation.md]]
- [[wiki/papers/guerrelli-2024-hipscm.md]]
- [[wiki/papers/ismaili-2023-hamburg.md]]
