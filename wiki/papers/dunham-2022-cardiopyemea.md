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
Cardio PyMEA is an open-source Python application for cardiomyocyte MEA analysis that makes the analytical pipeline explicit and reproducible, replacing vendor black-box software.

## Methodology
Python application developed at UCLA. Features implemented:
- Beat detection
- Pacemaker origin estimation
- Beat interval and amplitude analysis
- Local activation time (LAT) mapping
- Upstroke velocity
- Conduction velocity (CV)
- Field potential duration (FPD): interval from the R wave (field potential peak) to a T-wave endpoint, located with the trapezoid-area method of Vázquez-Seisdedos et al. (T wave found by peak detection; a trapezoid is fitted between the maximum first derivative after the T peak and a point 50–200 ms beyond it, and the area-maximising vertex gives the endpoint); a per-beat, per-electrode plot allows visual confirmation. Read from the PDF text on 2026-10-18; this corrects an earlier 'not reported' note on the FPD end convention.
- Power law analysis of FP statistics

Applied to cardiomyocyte MEA recordings from UCLA-derived hiPSC-CM preparations.

## Findings
- Cardio PyMEA enables transparent, reproducible MEA analysis with accessible Python code.
- Beat detection and pacemaker origin estimation can be performed without vendor tools.
- Power law analysis provides additional statistical characterization of FP dynamics.
- Conduction velocity mapping possible with standard MEA electrode arrays.

## Limitations
Early open-source tool; feature set less comprehensive than more recent platforms (e.g., CardioMEA). Python-based, requiring some technical familiarity. Publication does not provide formal validation against clinical gold standards.

## Relevance to our paper
Cited in main.md as an early example (2022) of the transition from vendor-defined to open, transparent analysis pipelines — a key trend in the post-2022 methodological shift described in the review. Illustrates reproducibility and transparency goals.

## See also
- [[wiki/papers/lee-2024-cardiomea.md]]
- [[wiki/papers/weiser-bitoun-2026-physiomea.md]]
- [[wiki/papers/kabanov-2026-cardioscripts.md]]
- [[wiki/papers/maki-2023-opinion.md]]
