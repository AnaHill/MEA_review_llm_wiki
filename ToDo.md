# ToDo (päivitetty 14.11.2026)
<!-- temp file that will be deleted -->
Järjestys: **A → B → C -> D.** D-luonnostelu ei odota mitään. Tehdyt kohdat poistetaan (git-historia säilyttää ne).

## A. Paperin sisältö (main.md ja tukitiedostot)
Valmis, kun teksti on lukittu ja jokainen väite on tarkistettu lähdettä vasten.

### A1. Oma läpiluku ja muokkaus (tehdään ensin, muuten väitelista vanhenee)
- [x] käyty

### A2. Lähdetarkistus (docs/claims-by-source.md)
**Näin käyt yhden lähteen läpi (toista jokaiselle):**
1. Avaa `docs/claims-by-source.md` ja hyppää lähteen otsikkoon (esim. `## Correia et al. (2024)`).
2. Avaa lähteen PDF `raw/`-kansiosta (tiedosto lukee otsikon alla "Local file").
3. Käytä `/grinding <authorname>` skills saadaksesi koosteen väitteistä läpikäyntiin
   1. Lue väite (`- [ ] (n) …`) ja sen alla oleva `- >` -rivi: se on main.md:n nykyinen virke.
   2. Etsi kohta PDF:stä. Apuna lähteen lopun "Pointers"-kappale (sivu, kuva, taulukko).
4. Pitääkö virke paikkansa lähteen mukaan? Kyllä → vaihda `[ ]` → `[x]`. Ei tai epävarma → kirjoita Claudelle: "Correia (5) ei pidä: …" tai "tarkista Correia (5)". Claude korjaa main.md:n, väitelistan ja lokin.
5. Kun lähde on valmis, siirry seuraavaan. Jos main.md muuttui, aja `python -I scripts/claim_quotes.py --write` (päivittää `- >` -rivit). Kun kaikki lähteen ruudut on rastitettu, sama komento (tai `--write --only Hwang`) lisää otsikkoon ✅.

**Järjestys (rasti kun lähde valmis):**
- [x] 1. Altrocchi: vain (6) vertailuliuottimen ajelehtiminen (Table 2) jäljellä
- [ ] 2. Eniten korjatut (jäljellä): Matsuda, Maurissen, Park 2025 (kaikki tarkistettu 24.10. vain osittain)
- [ ] 3. Uusimmat (jäljellä): Vuorenpää 2023, Ryynänen 2018 (kummankin kuvat katsomatta)
- [ ] 4. Loput (jäljellä): Park 2026, Pramudito, Weiser-Bitoun
- [x] 5. Omien päätelmien rekisteri (claims-tiedoston viimeinen osio): kaikki kohdat hyväksytty 14.11. Jos uusia omia päätelmiä lisätään, käy ne läpi samalla tavalla

**Erikseen muistettavat kohdat:**
- Vuorenpään ja Ryynäsen kuvia (Vuorenpää myös taulukot) ei ole katsottu; hoituu niiden grindingissa
- Correian ja Scheurerin liitteet lukematta, mutta yksikään väite ei nojaa niihin (molemmat ✅)

**Vinkit:**
- Clauden tarkistusraportti yhdestä lähteestä (ei muuta mitään): `/grinding Correia`
- Kuivaharjoitus yhdelle lähteelle, ei muuta mitään: `python -I scripts/claim_quotes.py --only Correia`
- Isompi päätös (esim. poistetaanko väite)? Käytä `/grill-paper`
- Lopuksi aja `python -I scripts/check.py`


### A3. Lyhenteet ja kursivointi
- [x] Tehty 1.11.: `# Abbreviations` highlightsien jälkeen 
- [ ] Jos main.md muuttuu: aja `python -I scripts/check_abbreviations.py`

### A4. Lopputarkistukset
- [ ] Valinnainen: uusi tarkistus toisella mallilla (esim. OpenAI; Geminillä tehty)
- [ ] Totea, että Declarationsin AI-lauseen väite lähteiden tarkistuksesta pitää paikkansa (nyt: väitteet "listed in a checklist for verification"); kun A2 valmis, voi vahvistaa muotoon "…was checked against that source by the author"
- [ ] `python -I scripts/check.py`: 0 virhettä (odotettu varoitus yksi: Clements 2025 -posterilla ei DOI:ta)
- [ ] Pohdi, kannattaako tehdä dokumentoitu haku aukolle (i), hiPSC-CM-kohtainen FPD:n taajuuskorjaus (lint 3.11., kohta 13). Esim. PubMed: "iPSC cardiomyocyte" + "rate correction" / "FPDc" / "Fridericia" / "Bazett" + "field potential". Tulos joko tukee Highlight 2:ta ("No validated … found") tai muuttaa sitä. Mallina `docs/maturation-mea-search.md`
- [ ] Matalampi prioriteetti: vastaava haku aukolle (ii), morfologian luokittelukriteerit (lint 3.11., kohta 16). "In the studies examined" -rajaus suojaa nykyistä väitettä, joten haku tarvitaan vain, jos väitettä halutaan laajentaa

#### Valinnaisia muualle kuin main.md tiedostoon
- [ ] Wiki kuntoon lopuksi: 
  - [ ] saisiko backlinkit ja tagit paremmaksi, jotta graafiesitys paranisi?
  - [ ] `wiki/index.md`:n "Last updated" -päiväys ja muu siistintä (lint 3.11., kohta 10)

- [ ]`README.md` päivityksiä
  - [ ] kuvat siirretty postauksen alla. Tuo sieltä tai luo lopulliset versiot READMEta varten jos näitä käytetään
  - [ ] toisiko Obsidianin Graph View - kuva lähteiden riippuvuuksista lisäarvoa? 
  - [ ] entä markmap esitys? Kuva postauksen ideoissa


## B. Julkaisu Zenodoon
Valmis, kun paperilla on DOI. Päätetty 31.10.: Zenodo (ei lehteä; Preprints.org hylätty seulonnan epävarmuuden vuoksi).

### B1. Vienti (ks. docs/pdf-export-notes.md, "Revised export plan": HTML on pohja, PDF HTML:stä selaimen tulostuksella)
- [ ] Mermaid-kaaviot (2 kpl) SVG-kuviksi mermaid-liven kautta, upotus kuvina alt-teksteineen (nyt versioimaton unpkg-CDN)
- [ ] HTML: näkyvä otsikkolohko (otsikko, tekijä, affiliaatio, päivä) ja `<title>`; front matter ei näy nyt
- [ ] HTML: DOI:t ja muut URL:t klikattaviksi (main.md:ssä noin 28 URL:ia)
- [ ] varmista, että tekijä löytyy alusta
- [ ] Poista HTML-kommentit main.md:stä; varmista `view source` -tarkistuksella
- [ ] PDF selaimella: `break-inside: avoid` kuville ja taulukoille, ei ylätunnisteita; tarkista kuvat, taulukot, kaava, ei `<!--`, `\#` tai tähtiä tekstissä

### B2. Zenodo-tietue
- [ ] Oma tietue omalla DOI:lla, tyyppi Publication → Preprint (ei uusi versio Mäki 2023 -tietueesta)
- [ ] Tiedostot: PDF pääasiallisena, HTML lisätiedostona (tarkista Zenodon HTML-käsittely)
- [ ] Metatiedot: CC BY 4.0; ei rahoitusta (harrasteprojekti); avainsanat; tekijä "Antti-Juhana Mäki, Independent researcher"; ORCID; päivämäärä ja versio
- [ ] Related identifiers: "references" → Mäki 2023 (10.5281/zenodo.20807245); "is supplemented by" → GitHub-repo (tai repon Zenodo-snapshot GitHub-releasen kautta)
- [ ] Zenodo Communities: etsi sopiva yhteisö (kardiologia, kantasolut, avoin tiede); liittäminen vaatii ylläpitäjän hyväksynnän

## C. Repot

### C1. Tämä repo (julkaisun jälkeen)
- [ ] README.md:n alkuun: "The paper is in main.md and published in <Zenodo-linkki>"
- [ ] README: linkki https://github.com/AnaHill/llm-wiki-academic-template ja omaan blogipostaukseen
- [ ] Tag tai GitHub-release julkaistusta versiosta
- [ ] Poista tämä ToDo.md

### C2. llm-wiki-academic-template
- [ ] tarkista lopuksi, ettei tässä repossa ole tullut mitään uutta hyödyllistä mitä kannattaisi laittaa templaattiin, tehty 1.11. asti muutokset mm `scripts/check_abbreviations.py`, vain sen jälkeiset
  - [ ] /grinding skills ainakin
  - [ ] `.claude/settings.json` (deny `raw/**` ja `notes.md`, PostToolUse-hook) ja `scripts/hooks/main_md_checks.py` (lisätty 11.11.)
  - [ ] `scripts/claim_quotes.py`: `--write`, `--only` ja otsikoiden ✅-merkinnät
  - [ ] `docs/private/` (git-ignored, yksityiset luonnokset) ja sen maininta AGENTS.md:ssä
  - [ ] täydennysaineistojen nimeäminen myös muille kuin PDF:ille (`<stem>-supplementary.docx`), ja .docx-kuvien purku `figure_analysis/`-kansioon tarkastelua varten
- [ ] myöhemmin: Ingest- ja Lint-menettelyt omiksi skilleiksi AGENTS.md:stä (ks. AGENTS.md "Schema evolution")

## D. Postaukset (kotisivun blogi kattava ensin, LinkedIn lyhyt sen jälkeen)
Sisältö ja ideat kotisivurepossa: AnaHill.github.io/_notes/llm-wiki-post/notes.md (osio "Ideat MEA_review_llm_wiki/ToDo.md:n D-osiosta", siirretty 2.11.). Luonnostelu rinnakkain, julkaisu vasta B:n jälkeen (tarvitsee linkin).
- [ ] Blogipostaus ensin (kokoa draft.md:hen notes.md:n ideoista)
  - [ ] tarkista, että /grinding skills mainittu
  - [ ] kuinka otettu toteutusideologiaa tästä https://claude.com/resources/articles/building-agents-when-to-fold-subagents-into-your-main-agent-loop
- [ ] LinkedIn-postaus blogin jälkeen: viittaa repoon, Zenodoon ja blogiin (AnaHill.github.io/_notes/llm-wiki-post/linkedin_draft.md)
  - [ ] tarkista, että /grinding skills mainittu
