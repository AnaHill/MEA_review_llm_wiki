# ToDo (päivitetty 1.11.2026)
<!-- temp file that will be deleted -->
Järjestys: **A → B → C1 ja D-julkaisu.** D-luonnostelu ei odota mitään. Tehdyt kohdat poistetaan (git-historia säilyttää ne).

## A. Paperin sisältö (main.md ja tukitiedostot)
Valmis, kun teksti on lukittu ja jokainen väite on tarkistettu lähdettä vasten.

### A1. Oma läpiluku ja muokkaus (tehdään ensin, muuten väitelista vanhenee)
- [x] käyty

### A2. Lähdetarkistus (docs/claims-by-source.md)
Tilanne 1.11.: 29 lähdettä, noin 190 väitettä + rekisteri 28 kohtaa. Tehty: Altrocchi 8/9, Mäki 4/15, Clements 1/7.

**Näin käyt yhden lähteen läpi (toista jokaiselle):**
1. Avaa `docs/claims-by-source.md` ja hyppää lähteen otsikkoon (esim. `## Correia et al. (2024)`).
2. Avaa lähteen PDF `raw/`-kansiosta (tiedosto lukee otsikon alla "Local file").
3. Lue väite (`- [ ] (n) …`) ja sen alla oleva `- >` -rivi: se on main.md:n nykyinen virke.
4. Etsi kohta PDF:stä. Apuna lähteen lopun "Pointers"-kappale (sivu, kuva, taulukko).
5. Pitääkö virke paikkansa lähteen mukaan? Kyllä → vaihda `[ ]` → `[x]`. Ei tai epävarma → kirjoita Claudelle: "Correia (5) ei pidä: …" tai "tarkista Correia (5)". Claude korjaa main.md:n, väitelistan ja lokin.
6. Kun lähde on valmis, siirry seuraavaan. Jos main.md muuttui, aja `python -I scripts/claim_quotes.py --write` (päivittää `- >` -rivit).

**Järjestys (rasti kun lähde valmis):**
- [ ] 1. Altrocchi: vain (6) vertailuliuottimen ajelehtiminen (Table 2) jäljellä
- [ ] 2. Eniten korjatut: Correia, Ernault, Fetterman, Guerrelli, Hwang, Ismaili, Matsuda, Maurissen, Park 2025, Scheurer
- [ ] 3. Uusimmat (luettu kokonaan, mutta tarkistamatta itse): Hu 2026, Karami 2026, Lee 2026, Li 2025, Lin 2023, Hayakawa 2014, Vuorenpää 2023, Ryynänen 2018
- [ ] 4. Loput: Blinova, Botti, Clements, Dunham, Kabanov, Lee 2024, Mäki, Park 2026, Pramudito, Weiser-Bitoun
- [ ] 5. Omien päätelmien rekisteri (claims-tiedoston viimeinen osio, kohdat 0–27): tässä ei etsitä lähdettä, vaan päätät, seisotko sanamuodon takana. Rasti kun hyväksyt; muuten pyydä Claudelta pehmennystä tai poistoa

**Erikseen muistettavat kohdat:**
- Clements (4): AIMS-sivun lainaus saatiin verkkotyökalun kautta, katso sanamuoto itse sivulta (URL väitteen kohdalla)
- Dunham (5) "R wave" ja Lee et al. (2024) (5) "R spike": varmista, että tarkoittavat R-huippua
- Rekisteri 1 ja 9 ovat trendiväitteitä ilman lähdettä (Introduction "As the use of MEA-based assays has grown…", Fiducial "growing emphasis" / "trends increasingly seen"); 20 on Morphology-osion "development … varies substantially"
- Lukematta jääneet liitteet: Correia ja Scheurer (supplementary); Vuorenpään ja Ryynäsen kuvia ei katsottu

**Vinkit:**
- Kuivaharjoitus yhdelle lähteelle, ei muuta mitään: `python -I scripts/claim_quotes.py --only Correia`
- Isompi päätös (esim. poistetaanko väite)? Käytä `/grill-paper`
- Lopuksi aja `python -I scripts/check.py`


### A3 Abbreviations alkupuolelle? Pitääkö symbolit yms _kursivoida_ tms?
- toteutetaan

### A4. Lopputarkistukset
- [ ] Valinnainen: uusi tarkistus toisella mallilla (esim. OpenAI; Geminillä tehty)
- [ ] Totea, että Declarationsin AI-lauseen väite lähteiden tarkistuksesta pitää paikkansa
- [ ] `python -I scripts/check.py`: 0 virhettä (odotettu varoitus yksi: Clements 2025 -posterilla ei DOI:ta)
- [ ] Valinnainen: toisiko Obsidianin Graph View - kuva lähteiden riippuvuuksista lisäarvoa? pohdi lisäämistä `README.md`, ei tähän mainiin


## B. Julkaisu Zenodoon
Valmis, kun paperilla on DOI. Päätetty 31.10.: Zenodo (ei lehteä; Preprints.org hylätty seulonnan epävarmuuden vuoksi).

### B1. Vienti (ks. docs/pdf-export-notes.md, "Revised export plan": HTML on pohja, PDF HTML:stä selaimen tulostuksella)
- [ ] Mermaid-kaaviot (2 kpl) SVG-kuviksi mermaid-liven kautta, upotus kuvina alt-teksteineen (nyt versioimaton unpkg-CDN)
- [ ] HTML: näkyvä otsikkolohko (otsikko, tekijä, affiliaatio, päivä) ja `<title>`; front matter ei näy nyt
- [ ] HTML: DOI:t ja muut URL:t klikattaviksi (main.md:ssä noin 28 URL:ia)
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
- [ ] tarkista lopuksi, ettei tässä repossa ole tullut mitään uutta hyödyllistä mitä kannattaisi laittaa templaattiin, tehty 1.11. asti muutokset, vain sen jälkeiset

## D. Postaukset (kotisivun blogi kattava ensin, LinkedIn lyhyt sen jälkeen)
Sisältö kotisivurepossa: AnaHill.github.io/_notes/llm-wiki-post. Luonnostelu rinnakkain, julkaisu vasta B:n jälkeen (tarvitsee linkin).
- [x] Kopioi postausmuistiinpanot (entinen osio 6) kotisivurepoon; tiedosto on valmiina Clauden scratchpadissa (ks. 31.10. chat)
- [ ] Blogipostaus ensin. 
  - [ ] lisää sinne tätä "samalla ne korostavat entisestään laadukkaan dataperustan, hyvän datan hallinnan ja oikeiden arkkitehtuuripäätösten merkitystä." kohtaa, voisiko saada muutakin kuin datalaatu mukaan
- [ ] LinkedIn-postaus: viittaa repoon, zenodoon ja blogiin
