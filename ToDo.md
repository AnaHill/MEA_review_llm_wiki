# ToDo (päivitetty 1.11.2026)
<!-- temp file that will be deleted -->
Järjestys: **A → B → C1 ja D-julkaisu.** D-luonnostelu ei odota mitään. Tehdyt kohdat poistetaan (git-historia säilyttää ne).

## A. Paperin sisältö (main.md ja tukitiedostot)
Valmis, kun teksti on lukittu ja jokainen väite on tarkistettu lähdettä vasten.

### A1. Oma läpiluku ja muokkaus (tehdään ensin, muuten väitelista vanhenee)
- [x] käyty

### A2. Lähdetarkistus ja claims-by-source.md läpikäynti valmiista tekstistä
- Vinkki: isommat päätökset/pohdinnat voi käydä läpi komennolla `/grill-paper` 
- Jos main.md muuttuu tarkistuksen aikana: aja `python -I scripts/claim_quotes.py --write` uudelleen (kuivaharjoitus ei muuta mitään, esim. `python -I scripts/claim_quotes.py --only Hwang`)

- [ ] Omien päätelmien rekisteri, kohdat 1–27 (docs/claims-by-source.md, osio "Register of the author's own inferences", kirjoitettu uudelleen 1.11.): päätä, seisotko jokaisen sanamuodon takana. Erityisesti 1 ja 9 ovat trendiväitteitä ilman lähdettä (Introductionin "As the use of MEA-based assays has grown…" ja Fiducial-osion "growing emphasis" / "trends increasingly seen") ja 20 Morphology-osion "development … varies substantially"; 24–27 ovat outlookin hypoteeseja


- [ ] Käy jokainen lähde läpi claims-by-source.md:n kappaletta vasten Altrocchin tapaan (29 lähdettä, noin 190 väitettä; 1.11. tilanne: Altrocchi 8/9, Mäki 4/15, Clements 1/7, muut 0, rekisteri 0/28). Wikisivut on tarkistettu lähdetekstiä vasten (24.10. tai ingest-päivänä), mutta numerot ja kuvatulkinnat kannattaa varmistaa itse
  - Altrocchi: jäljellä vain (6) vertailuliuottimen ajelehtiminen (Table 2)
  - Erityisesti: Correia, Ernault, Fetterman, Guerrelli, Hwang, Ismaili, Matsuda, Maurissen, Park 2025 ja Scheurer (näistä on korjattu eniten); lukematta jääneet liitteet: Correia ja Scheurer supplementary
  - Clements (4): AIMS-sivun lainaus saatiin verkkotyökalun kautta, tarkista sanamuoto itse sivulta
  - Uudet: Hayakawa 2014 ja Vuorenpää 2023 luettu kokonaan (Vuorenpään kuvia ei katsottu); Ryynänen 2018 luettu kokonaan, kuvia ei katsottu; Li 2025 ja Lin 2023 luettu liitteineen, Li:n luvut tarkistettu Supplementary Tableista 2–3 (main.md käyttää S3:n CV- ja spike amplitude -lukuja); 1.11. lisätyt Hu 2026 (sikiövaiheen hiiren solut, kuvat 2–7 katsottu), Karami 2026 (katsaus, viitevirheitä, käytetään vain MEA-fysiikkaan) ja Lee 2026 (kuva 4 katsottu) luettu kokonaan. Lue main.md:n tiivistykset itse
  - Kaksi auki olevaa tarkistusta: Dunham (5) "R wave" vs R peak ja Lee et al. (2024) (5) "R spike" vs R peak

### A3B Highlights alkuun
- [x] Tehdään tiivistelmä / highlights tieteelliset havainnot

### A3C Abbreviations alkupuolelle? Pitääkö symbolit yms _kursivoida_ tms?
- Harkitse lyhennelmän listausta alkupuolelle, esim tiivistelmän jälkeen. siitä voisi tehdä myös skriptit tms joka tarkistaa asian. Jos tuollaista tulee, viedään se myös akateemiseen repoon
- lyhenteiden _kursivointi_ tai vastaava käsittely, kannattaako?!

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
- [ ] tarkista lopuksi, ettei tässä repossa ole tullut mitään uutta hyödyllistä mitä kannattaisi laittaa templaattiin
  - Vertailu 1.11.: templaattiin vietäväksi (1) claim_quotes.py:n Mermaid-korjaus (`\n` kaavion tekstissä piilotti nimen tunnistukselta), (2) rekisteriosion uusi nimi "Register of the author's own inferences" ja käytäntö: väitelista kirjoitetaan puhtaaksi valmiista tekstistä, rastit säilytetään muuttumattomille väitteille, historia jää lokiin, (3) valinnainen: yleinen ohje samannimisistä ensimmäisistä kirjoittajista (päätä etukirjaimet ja kirjaa AGENTS.md:hen)
  - Tehty 1.11.: kohdat (1)–(3) viety templaattiin paikallisesti (claim_quotes.py, AGENTS.md, docs/claims-by-source.md), ei commitoitu, pushaa itse; templaatin parempi check.py tuotu tähän repoon

Tehty 31.10. tehty llm-wiki-academic-template
- [x] Siirrä templaattiin tässä repossa hyväksi todetut, heti käytettävät osat: scripts/check.py, scripts/claim_quotes.py, scripts/render_pdf_pages.py, `.claude/skills/grill-paper`
- [x] Siirrä AGENTS.md:n käytännöt: raw-tiedostojen nimeäminen ingestissä, verify-before-ingest, ei hajatageja, finishing check, omien päätelmien rekisteri (claims-by-source), grill-osio ja lokin grill-etuliite
- [x] Templaatin README: linkki tähän repoon esimerkkinä

## D. Postaukset (kotisivun blogi kattava ensin, LinkedIn lyhyt sen jälkeen)
Sisältö kotisivurepossa: AnaHill.github.io/_notes/llm-wiki-post. Luonnostelu rinnakkain, julkaisu vasta B:n jälkeen (tarvitsee linkin).
- [x] Kopioi postausmuistiinpanot (entinen osio 6) kotisivurepoon; tiedosto on valmiina Clauden scratchpadissa (ks. 31.10. chat)
- [ ] Blogipostaus ensin. 
  - [ ] lisää sinne tätä "samalla ne korostavat entisestään laadukkaan dataperustan, hyvän datan hallinnan ja oikeiden arkkitehtuuripäätösten merkitystä." kohtaa, voisiko saada muutakin kuin datalaatu mukaan
- [ ] LinkedIn-postaus: viittaa repoon, zenodoon ja blogiin
