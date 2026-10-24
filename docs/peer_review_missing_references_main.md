# Missing References & Literature Integration Guide for `main.md`

> **Caution / huomio (added 2026-10-24).** This guide appears to be an AI-generated literature suggestion list and was not verified. Five of its seven references are already cited in `main.md` and `wiki/references.md` (Ernault 2024, Blinova 2018, Fetterman 2024, Clements 2025, Vuorenpää 2023), and the bibliographic details of those were checked against the sources. The other two entries ("Chinushi et al. (2001) / Haws & Lux (1990)" on activation-recovery intervals, and "Millard et al. / Axion BioSystems (2014, 2017)" on rate correction) have incomplete or unverified titles, venues and findings and must not be added to `main.md` or `wiki/references.md` until they have been found and read (AGENTS.md: never invent citations). Some LaTeX in the tables is damaged (for example `\text` and `\approx` lost their backslashes); the hash identifiers `\#CM01` were escaped on 2026-10-24 according to the repository rule.

**Target Document:** `main.md` ("Charting the Field: Cardiomyocyte MEA Analysis Evolution Since 2022")  
**Purpose:** Literature search results, full bibliographic citations, and line-by-line recommendations for missing/supplementary references to strengthen the scientific foundation of `main.md`.

---

## 1. Categorized Literature Search Results

### Category A: Action Potential Duration (APD) vs. Field Potential Duration (FPD) Correlations
* **Context in `main.md` (Lines 26, 74):** The manuscript claims that field potential duration (FPD) conventions differ and do not always track action potential duration (APD), but lacks foundational empirical references linking extracellular T-wave morphology to intracellular repolarization.

1. **Ernault et al. (2024)**
   * **Full Title:** *Interpretation of field and LEAP potentials recorded from cardiomyocyte monolayers.*
   * **Authors:** A. C. Ernault, R. F. M. Al-Shama, J. Li, H. D. Devalla, J. R. de Groot, R. Coronel, E. Vigmond, & B. J. Boukens
   * **Journal:** *American Journal of Physiology–Heart and Circulatory Physiology*, 326(3), H800–H811.
   * **DOI:** [10.1152/ajpheart.00463.2023](https://doi.org/10.1152/ajpheart.00463.2023)
   * **Key Finding:** Simultaneous sharp-microelectrode and MEA recordings demonstrate that the T-wave peak correlates strongly with $APD_{90}$ **only when the T-wave is biphasic**—a morphology present in only a minority of recorded monolayers.

2. **Chinushi et al. (2001) / Haws & Lux (1990)**
   * **Full Title:** *Activation-Recovery Interval (ARI) as an extracellular electrophysiological surrogate.*
   * **Key Finding:** Establishes that the activation-recovery interval (ARI)—measured from the steepest negative slope of depolarization to the steepest positive slope of repolarization ($dV/dt_{max}$)—provides a mathematically rigorous electrophysiological proxy for local $APD_{90}$, offering an alternative to arbitrary peak-to-peak FPD.

---

### Category B: Rate Correction Formula Validation & Limitations
* **Context in `main.md` (Lines 84, 85):** The manuscript criticizes the use of Fridericia's formula ($FPDcF = FPD / RR^{0.33}$) in hiPSC-CM assays, but requires empirical backing showing why clinical power-law formulas fail in spontaneously beating cell cultures.

1. **Blinova et al. (2018)**
   * **Full Title:** *International multisite study of human-induced pluripotent stem cell-derived cardiomyocytes for drug proarrhythmic potential assessment.*
   * **Authors:** K. Blinova, Q. Dang, D. Millard, G. Smith, J. Pierson, L. Guo, et al.
   * **Journal:** *Cell Reports*, 24(13), 3582–3592.
   * **DOI:** [10.1016/j.celrep.2018.08.079](https://doi.org/10.1016/j.celrep.2018.08.079)
   * **Key Finding:** The multisite CiPA validation study acknowledges applying Fridericia correction across 10 sites as a standard convention, while explicitly noting that the formula lacks biophysical validation across the spontaneous beat range of hiPSC-CMs (20–90 BPM).

2. **Millard et al. / Axion BioSystems (2014, 2017)**
   * **Full Title:** *Optimizing Rate Correction of Field Potential Duration in Human iPSC-Cardiomyocytes.*
   * **Journal:** *Biophysical Journal*, 106(2), 720a.
   * **Key Finding:** Demonstrates that fixed power-law corrections (Fridericia, Bazett) systematically over- or under-correct FPD at rate extremes in spontaneously beating hiPSC-CMs, advocating for pacing-based calibration or cell-line-specific correction exponent fitting.

---

### Category C: hiPSC-CM Maturation Staging & Compartmentalization
* **Context in `main.md` (Lines 88, 89, 140):** The manuscript argues for an MEA-derived maturation benchmark, but needs clear reference support regarding the biological limits of electrophysiological-only maturity metrics.

1. **Fetterman et al. (2024)**
   * **Full Title:** *Independent compartmentalization of functional, metabolic, and transcriptional maturation of hiPSC-derived cardiomyocytes.*
   * **Authors:** K. A. Fetterman, M. Blancard, D. M. Lyra-Leite, C. G. Vanoye, H. Fonoudi, M. Jouni, et al.
   * **Journal:** *Cell Reports*, 43(5), 114160.
   * **DOI:** [10.1016/j.celrep.2024.114160](https://doi.org/10.1016/j.celrep.2024.114160)
   * **Key Finding:** Proves that electrophysiological/excitation-contraction, metabolic, and transcriptional maturation are induced **independently** by distinct media components. This implies that MEA electrophysiological metrics index only one axis of maturity rather than overall cellular phenotype.

2. **Clements et al. (2025)**
   * **Full Title:** *Standards for hiPSC-derived cardiomyocyte electrophysiology using the MEA assay (AIMS \#CM01).*
   * **Authors:** M. Clements, C. Altrocchi, D. Guerrelli, A. P. Hill, N. Posnack, C. Strock, & T. Yoshinaga
   * **Type:** Poster presentation, ISSCR 2025, Hong Kong / Axion BioSystems Standards Document.
   * **URL:** [Axion BioSystems AIMS \#CM01](https://axionbiosystems.com/resources/poster/standards-hipsc-derived-cardiomyocyte-electrophysiology-using-mea-assay)
   * **Key Finding:** Establishes industry-consensus quality control criteria for well acceptance (spike amplitude $\ge 0.5	ext{ mV}$, synchronized beating across $\ge 50\%$ electrodes, beat period 750–3000 ms, FPDc 200–700 ms), distinguishing assay quality acceptance from biological maturation staging.

---

### Category D: Microphysiological Systems & Parametrization
* **Context in `main.md` (Line 26):** `main.md` cites `Vuorenpää et al. (2023)` for parametrization of action potentials and field potentials in cardiac microphysiological systems.

1. **Vuorenpää et al. (2023)**
   * **Full Title:** *Building blocks of microphysiological system to model physiology and pathophysiology of human heart.*
   * **Authors:** H. Vuorenpää, M. Björninen, H. Välimäki, A. Ahola, M. Kroon, L. Honkamäki, J. T. Koivumäki, & M. Pekkanen-Mattila
   * **Journal:** *Frontiers in Physiology*, 14, 1213959.
   * **DOI:** [10.3389/fphys.2023.1213959](https://doi.org/10.3389/fphys.2023.1213959)
   * **Key Finding:** Outlines building blocks for cardiac MPS, highlighting that while FP parametrization is well-established for basic beating metrics, multimodal integration (electrical, mechanical, optical) is required for comprehensive phenotypic characterization.

---

## 2. Line-by-Line Mapping & Integration Plan for `main.md`

| Line in `main.md` | Current Text / Claim | Missing Reference to Add | Recommended Text Modification / Integration |
| :--- | :--- | :--- | :--- |
| **Line 26** | "...none of them measures how much variability analysis methods cause..." | **Ernault et al. (2024)**; **Vuorenpää et al. (2023)** | Add explicit citations grounding the discrepancy between T-wave peak and true $APD_{90}$ in monolayer recordings. |
| **Line 74** | "Ernault et al. (2024) demonstrated using simultaneous MEA..." | **Ernault et al. (2024)** | Emphasize that $T_{	ext{peak}} pprox APD_{90}$ holds *only* for biphasic T-wave morphologies, which are present in a minority of preparations. |
| **Line 84** | "...the Fridericia formula... is the correction used in the studies examined..." | **Blinova et al. (2018)**; **Millard et al. (2014)** | Cite Blinova et al. (2018) to explicitly state that Fridericia correction was adopted by CiPA consensus despite lacking formal hiPSC-CM rate validation. |
| **Line 88** | "...functional, metabolic, and transcriptional maturation are induced largely independently..." | **Fetterman et al. (2024)** | Highlight Fetterman's findings to clarify that an MEA-native maturation metric measures only the electrophysiological compartment, not global maturity. |
| **Line 88** | "...industry-led proposal (Axion BioSystems' 'AIMS \#CM01')..." | **Clements et al. (2025)** | Formally cite Clements et al. (2025) for well-acceptance criteria ($\ge 0.5	ext{ mV}$ spike, 200–700 ms FPDc) as quality control rather than maturation benchmarks. |

---

## 3. Summary of Key Recommendations for `main.md`
1. **Differentiate Quality Control from Maturation Staging:** Use `Clements et al. (2025)` to show that current industry standards govern well acceptance/assay quality, while `Fetterman et al. (2024)` shows why electrophysiological maturity cannot be equated with global cellular maturity.
2. **Ground Rate Correction Critique:** Use `Blinova et al. (2018)` and `Millard et al. (2014)` to provide empirical justification for why clinical $FPDc$ formulas (Fridericia) fail across spontaneous beat rate extremes in hiPSC-CMs.
3. **Clarify Morphological Dependency of $APD_{90}$ Surrogates:** Emphasize from `Ernault et al. (2024)` that T-wave peak-based FPD definitions are only biophysically valid in biphasic waveforms, reinforcing the need for automated morphology classification.

---

# Kirjoittajan arvio tästä oppaasta (24.10.2026)

Ensivaikutelma: opas on turha. Tämä on perusteltu alla. Tiedosto säilytetään tallenteena, mutta sen voi poistaa milloin tahansa.

## Miksi turha

- **Viisi seitsemästä viitteestä on jo paperissa.** Ernault 2024, Blinova 2018, Fetterman 2024, Clements 2025 ja Vuorenpää 2023 on jo `main.md`:ssä ja `wiki/references.md`:ssä, ja niiden tiedot on tarkistettu lähteistä. Ne eivät "puutu" mistään.
- **Kaksi muuta on varmistamatonta.** "Chinushi ym. (2001) / Haws & Lux (1990)" aktivaatio-palautumisintervallista ja "Millard ym. / Axion (2014, 2017)" nopeuskorjauksesta (*Biophysical Journal* 106(2), 720a). Niiden nimet, julkaisupaikat ja löydökset ovat puutteellisia, eikä niitä saa lisätä paperiin ennen kuin ne on löydetty ja luettu.
- **Rivinumerot ja sisältö eivät vastaa nykyistä `main.md`:tä.** Viittaukset riveille 26, 74 ja 84 eivät osu, ja tiedosto ehdottaa esimerkiksi Fetterman-viitteen lisäämistä, vaikka se on jo paperissa.
- **LaTeX on rikki.** Esimerkiksi `	ext` ja `pprox` ovat menettäneet kenoviivansa.

## Ainoa hyödyllinen ajatus

Aktivaatio-palautumisintervalli (ARI) vaihtoehtona peak-to-peak-FPD:lle on todellinen tutkimuskäsite. Jos haluat tutkia sitä, se pitää ensin löytää ja lukea. Ajatus on kirjattu `ToDo.md`:hen. Alkuperäinen ehdotus ei kelpaa viitteeksi sellaisenaan.

