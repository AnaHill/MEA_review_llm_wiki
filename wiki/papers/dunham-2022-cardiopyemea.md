---
tags: [open-platform, fiducial-definition, conduction-velocity]
---

# Cardio PyMEA: A user-friendly, open-source Python application for cardiomyocyte microelectrode array analysis

**Authors:** Christopher S. Dunham, Madelynn E. Mackenzie, Haruko Nakano, Alexis R. Kim, Atsushi Nakano, Adam Z. Stieg, James K. Gimzewski  
**Year:** 2022  
**Venue:** PLOS ONE 17(5):e0266647  
**File:** [[raw/dunham-2022-cardiopyemea.pdf]]  
**DOI:** 10.1371/journal.pone.0266647


## Contribution
Cardio PyMEA is a free, modifiable, open-source Python application (PyQt5 GUI) for cardiomyocyte MEA analysis, written to complement closed-source proprietary tools and to avoid the MATLAB licence barrier of earlier open tools.

Note: page checked against the source text on 2026-10-24; statements not supported by the paper were removed or reworded.

## Methodology
Python application developed at UCLA. Features implemented:
- Beat detection
- Pacemaker origin estimation
- Beat interval and amplitude analysis
- Local activation time (LAT) mapping
- Upstroke velocity
- Conduction velocity (CV)
- Field potential duration (FPD): interval from the R wave (field potential peak) to a T-wave endpoint, located with the trapezoid-area method of Vázquez-Seisdedos et al. (T wave found by peak detection; the maximum first derivative between the T peak and baseline and an arbitrary point 50–200 ms past the T peak fit a trapezoid with a mobile point; maximising the area gives the endpoint); a per-beat, per-electrode plot allows visual confirmation. Read from the PDF text on 2026-10-18; this corrects an earlier 'not reported' note on the FPD end convention.
- Property-distance relationship analysis (mean R² = 0.898 for CV versus distance, pp. 13–14)
- Power law analysis (powerlaw library) of the quiescent periods between pacemaker translocations; distribution comparison by log-likelihood ratio

Demonstrated on 30 recordings from hESC-CM and hiPSC-CM monolayers (3 differentiations) on 120-electrode Multichannel Systems MEAs (mean beat rate 36.64 ± 14.48 bpm). The methods describe only hESC differentiation.

## Findings
- Beat detection and pacemaker origin estimation run in open-source Python code, but the input must be Multichannel Systems MC_Rack/MC_Data exports (.txt; 60- or 120-electrode arrays).
- Applied to pacemaker translocations, a doubly truncated power law fitted best (exponent -1.583, a result taken from the authors' earlier work, ref. 25); the authors suggest critical dynamics may play a role.
- Conduction velocity mapping from the LAT maps.

## Limitations
Stated by the authors (pp. 17–18): the GUI freezes during calculations (Python GIL); loading is slow (a 1.9 GB file takes about 45 s); input is limited to .txt files from MC_Data and to Multichannel Systems 60- and 120-electrode layouts. A GUI and PyInstaller executables (Linux, macOS, Windows 10) are provided for non-programmers.

Our observation (not from the paper): validation is by manual inspection only (beat detection, electrode exclusion); no FPD values or T-wave endpoint validation are reported.

## Relevance to our paper
Cited in main.md as an early example (2022) of the transition from vendor-defined to open analysis pipelines. The paper's stated aims are openness, extensibility and accessibility, and it says it complements, not replaces, proprietary tools.

## See also
- [[wiki/papers/lee-2024-cardiomea.md]]
- [[wiki/papers/weiser-bitoun-2026-physiomea.md]]
- [[wiki/papers/kabanov-2026-cardioscripts.md]]
- [[wiki/papers/maki-2023-opinion.md]]
