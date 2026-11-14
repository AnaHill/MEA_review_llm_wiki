---
tags: [maturation, rate-correction, cardiac-safety]
---

# Human induced pluripotent stem cell-derived closed-loop cardiac tissue for drug assessment

**Authors:** Junjun Li, Ying Hua, Yuting Liu, Xiang Qu, Jingbo Zhang, Masako Ishida, Noriko Yoshida, Akiko Tabata, Hayato Miyoshi, Mikio Shiba, Shuichiro Higo, Nagako Sougawa, Maki Takeda, Takuji Kawamura, Ryohei Matsuura, Daisuke Okuzaki, Toshihiko Toyofuku, Yoshiki Sawa, Li Liu, Shigeru Miyagawa
**Year:** 2024 (published 23 January 2024; the researcher's file name said 2025)
**Venue:** iScience 27, 108992 (open access, CC BY)
**File:** [[raw/li-2024-closed-loop.pdf]]
**Supplementary:** [[raw/li-2024-closed-loop-supplementary.pdf]] (Figures S1–S8)
**DOI:** 10.1016/j.isci.2024.108992
**Affiliation:** Osaka University (Department of Cardiovascular Surgery and others); one author from Fujifilm Corporation. Funding JSPS, AMED and Fujifilm; several authors filed a provisional Japanese patent application on the method.

Note: ingested 2026-11-14 from the text dump (pages 1–13 and the STAR Methods); main-text figures not viewed; supplement read and Figure S4 viewed the same day. Not to be confused with Li et al. (2025, [[wiki/papers/li-2025-maturation.md]]), a different group.

## Contribution
A 2D hiPSC-CM monolayer cultured in a ring-shaped PDMS well around a central pillar ("closed-loop cardiac tissue", iCT), in which a traveling wave (TW) arises spontaneously and paces the cells at a high rate (220 ± 74 bpm against 32.4 ± 30.1 bpm without a TW, day 6) for 14 days. The authors show that this matures the cells and changes their drug responses on an MEA, and present it as adapted to 2D MEA paradigms such as CiPA and JiCSA.

## Methodology
- **Cells:** 253G1-derived hiPSC-CMs and commercial iCell2; control tissues without a TW in the same device.
- **Device:** PDMS well (8 mm) with a 3 mm pillar; for drug tests the tissue grows on a permeable PLGA fibre layer in a 24-well plate and is moved onto the MEA only for recording, so MEA chips can be reused.
- **MEA:** Multi Channel Systems USB-ME64 (8 × 8 electrodes, 200 µm spacing), MC_Rack; local activation time from the minimum of the first derivative; activation maps by linear interpolation.
- **"QT interval":** the paper calls the field potential duration a QT interval and corrects it with Fridericia's formula (cQT). The FP is described as a Na⁺ peak "followed by the T wave determined as the repolarization phase"; how the end of the interval is located is not stated.
- **Pacing and drug tests:** the TW was stopped before drug testing, because its 3–4 Hz rate "may interfere with the CM response"; the tissues then beat at about 1 Hz (p. 11). Cumulative dosing, 5 min per concentration, 1 min recordings. Drugs: isoproterenol, verapamil, ranolazine, mexiletine, E-4031, aspirin, quinidine (high TdP risk), pimozide (intermediate).
- **Other readouts:** RNA-seq, immunostaining, TEM, western blot, Seahorse respiration, video motion analysis.

### Supplementary material
Figures S1–S8 (captions read, Figure S4 viewed 2026-11-14):
- **S1–S3:** cTnT flow cytometry of the 253G1 cells; heatmaps of maturation genes (FPKM); network of enriched GO terms.
- **S4:** the ring device on an MEA with the permeable fibre layer; beat frequency of 253G1 and iCell tissues on days 2–14 (TW about 2.5–3.6 Hz against about 0.6–0.9 Hz in controls, all significant); and the "QT interval" of 253G1 tissues on days 6 and 14, about 0.6 s in controls against about 0.15 s with TW (P < 0.01). These QT values come from tissues while the TW was running, so the short QT reflects the 3–4 Hz rate; after the TW was stopped, QT was about 300 ms in both groups (main text Fig. 4D). The caption does not say whether S4b is rate-corrected (our reading).
- **S5–S7:** drug responses of iCell tissues (isoproterenol, verapamil, ranolazine) and of both lines to E-4031, mexiletine and aspirin; yellow arrows mark the T wave in the example traces; n = 4–10 per group.
- **S8:** example trace and activation maps with quinidine.

The supplement changes neither main.md sentence.

## Findings
- **Maturation markers:** higher expression of conduction, structural and metabolic genes (GJA1, KCNJ2, SCN5A, MYH7, TNNI3 and others), lower CACNA1C and KCNH2, Cx43 and β-MHC up, better-organised sarcomeres (TEM) but no difference in sarcomere length; higher contraction and relaxation velocity and mitochondrial ATP production.
- **MEA:** higher conduction velocity and smaller maximum activation delay in the TW group (Fig. 4B–C; n = 3–5); "QT" about 300 ms in both groups (Fig. 4D).
- **Drug responses (253G1 unless noted):** isoproterenol chronotropy across the whole range in TW tissues (EC50 95.2 nM against 6.7 nM); verapamil IC50 1.1 µM (TW) against 0.05 µM (control), but similar in iCell2 (2.59 and 2.73 µM); ranolazine caused fewer EADs and no cessation in TW tissues; quinidine (3/4 TW against 1/5 control) and pimozide (2/4 against 0/4) caused more arrhythmia-like events in TW tissues; E-4031 prolonged "QT" in both groups without arrhythmias (Table 1).
- **Pacing timing (Discussion, p. 11):** pacing before drug assessment (to mature) differs from pacing during it (to control rate); the authors cite reports that electrical pacing during tests reduced rate-related variation and that optical pacing did not improve proarrhythmic prediction, and conclude that stimulation time and delivery method may matter.

## Limitations
Stated by the authors: the TW is spontaneous and cannot be controlled precisely, with sample-to-sample variation in conduction velocity and transcriptome; it does not reach the 6 Hz of electrical stimulation studies; restarting it is time-consuming; tissue digestion may disrupt properties; the MEA covers a limited area; PDMS may adsorb compounds; site-to-site and line-to-line validation is still to be done.

Our observations (not from the paper): small groups (n = 4–9 per drug), arrhythmia events reported as counts without statistics; one maturation intervention compared with an unpaced control in the same ring device, not with a standard MEA plate culture; the end point of the "QT interval" is not defined; the EMA review by Mondéjar-Parreño et al. (2026, not ingested) describes this work as MEA with "controlled pacing and closed-loop stimulation", although the pacing was spontaneous and stopped before the drug tests.

## Relevance to our paper
Cited in main.md (2026-11-14) in two places, kept short: the maturation section (rapid pacing by a traveling wave raised MEA conduction velocity and changed drug responses, alongside Li et al., 2025) and the rate-correction section (pacing before recording as a maturation step, stopped before drug tests, as opposed to pacing during recording). Also an example of an FPD ("QT") whose end point is not stated, kept on this page only.

## See also
- [[wiki/papers/li-2025-maturation.md]] — another maturation intervention with MEA conduction velocity rising
- [[wiki/papers/guerrelli-2024-hipscm.md]] — pacing during recording, for comparison with pacing before it
- [[wiki/papers/matsuda-2025-uhd.md]] — spontaneous beating only, absence of pacing named as a limitation
- [[wiki/hipsc-cm-maturation.md]]
- [[wiki/fridericia-rate-correction.md]]
