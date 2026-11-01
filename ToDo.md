# ToDo (päivitetty 1.11.2026)
<!-- temp file that will be deleted -->
Järjestys: **A → B → C1 ja D-julkaisu.** C2 ja D-luonnostelu eivät odota mitään. Tehdyt kohdat poistetaan (git-historia säilyttää ne).

## A. Paperin sisältö (main.md ja tukitiedostot)
Valmis, kun teksti on lukittu ja jokainen väite on tarkistettu lähdettä vasten.

### A1. Oma läpiluku ja muokkaus (tehdään ensin, muuten väitelista vanhenee)
- [ ] Omien päätelmien rekisteri, kohdat 1–27 (docs/claims-by-source.md, osio "Register of the author's own inferences", kirjoitettu uudelleen 1.11.): päätä, seisotko jokaisen sanamuodon takana. Erityisesti 1 ja 9 ovat trendiväitteitä ilman lähdettä (Introductionin "As the use of MEA-based assays has grown…" ja Fiducial-osion "growing emphasis" / "trends increasingly seen") ja 20 Morphology-osion "development … varies substantially"; 24–27 ovat outlookin hypoteeseja
- [ ] Valinnainen: toisiko Obsidianin Graph View -kuva lähteiden riippuvuuksista lisäarvoa? Ainakin README.md, ei 
- Vinkki: isommat päätökset voi käydä läpi komennolla `/grill-paper` ennen muokkausta

### A2. claims-by-source.md uudelleen valmiista tekstistä
- [x] Väitelista kirjoitettu puhtaaksi nykyisestä main.md:stä 1.11. (historia lokissa); rastit säilytetty muuttumattomille väitteille (Altrocchi 1–5 ja 7–9, Clements 4, Mäki 8, 11, 13, 14); `claim_quotes.py --write` ajettu, jokaisella väitteellä on virke main.md:stä
- [ ] Jos main.md muuttuu tarkistuksen aikana: aja `python -I scripts/claim_quotes.py --write` uudelleen (kuivaharjoitus ei muuta mitään, esim. `python -I scripts/claim_quotes.py --only Hwang`)

### A3. Oma lähdetarkistus
- [ ] Käy jokainen lähde läpi claims-by-source.md:n kappaletta vasten Altrocchin tapaan. Wikisivut on tarkistettu lähdetekstiä vasten 24.10., mutta numerot ja kuvatulkinnat kannattaa varmistaa itse
  - Erityisesti: Altrocchi, Correia, Ernault, Fetterman, Guerrelli, Hwang, Ismaili, Matsuda, Maurissen, Park 2025 ja Scheurer (näistä on korjattu eniten); lukematta jääneet liitteet: Correia ja Scheurer supplementary
  - Uudet: Hayakawa 2014 ja Vuorenpää 2023 luettu kokonaan (Vuorenpään kuvia ei katsottu); Ryynänen 2018 luettu kokonaan, kuvia ei katsottu; Li 2025 ja Lin 2023 luettu liitteineen, Li:n luvut tarkistettu Supplementary Tableista 2–3 (main.md käyttää S3:n CV- ja spike amplitude -lukuja); 1.11. lisätyt Hu 2026 (sikiövaiheen hiiren solut, kuvat 2–7 katsottu), Karami 2026 (katsaus, viitevirheitä, käytetään vain MEA-fysiikkaan) ja Lee 2026 (kuva 4 katsottu) luettu kokonaan. Lue main.md:n tiivistykset itse
  - Kaksi auki olevaa tarkistusta: Dunham (5) "R wave" vs R peak ja Lee et al. (2024) (5) "R spike" vs R peak

### A3B Highlights alkuun
- [x] Tehdään tiivistelmä / highlights tieteelliset havainnot
  - [x] HUOM! Ei tehdä tähän: postauksissa/repossa sitten "LLM-wiki kehityskohdat mitä tässä opittin", ei tässä

### A3C Abbreviations alkupuolelle? Pitääkö symbolit yms _kursivoida_ tms?
- Harkitse lyhennelmän listausta alkupuolelle, esim tiivistelmän jälkeen. siitä voisi tehdä myös skriptit tms joka tarkistaa asian. Jos tuollaista tulee, viedään se myös akateemiseen repoon
- lyhenteiden _kursivointi_ tai vastaava käsittely, kannattaako?!

### A4. Lopputarkistukset
- [ ] Valinnainen: uusi tarkistus toisella mallilla (esim. OpenAI; Geminillä tehty)
- [ ] Totea, että Declarationsin AI-lauseen väite lähteiden tarkistuksesta pitää paikkansa
- [ ] `python -I scripts/check.py`: 0 virhettä (odotettu varoitus yksi: Clements 2025 -posterilla ei DOI:ta)

### Ei tähän versioon
- Aktivaatio-palautumisintervalli (ARI) vaihtoehtona peak-to-peak-FPD:lle: todellinen tutkimuskäsite: oma Mäki 2023 -paperisi käsittelee jo ARI:ta. Riedel et al. (2014) käyttivät ARI:ta FPD:n sijaan ja ehdottivat sitä "the gold standard measure of repolarization ... in MEA analyses of iPSC CMs"; sinä kritisoit, ettei ARI kuvaa koko repolarisaatiota (loppu repolarisaatioaallon maksimiderivaatassa) ja että se vastaa APD50:tä, joten se ei ehkä havaitse EAD:ta. Viite Mäki 2023:n lähdeluettelosta: Riedel et al. (2014), Functional and pharmacological analysis of cardiomyocytes differentiated from human peripheral blood mononuclear-derived pluripotent stem cells, *Stem Cell Reports* 3(1), 131–141, doi:10.1016/j.stemcr.2014.04.017

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

Tehty 31.10. paikallisesti (../llm-wiki-academic-template), ei commitoitu eikä pushattu: tarkista `git diff`, commitoi ja pushaa itse.
- [x] Siirrä templaattiin tässä repossa hyväksi todetut, heti käytettävät osat: scripts/check.py, scripts/claim_quotes.py, scripts/render_pdf_pages.py, `.claude/skills/grill-paper`
- [x] Siirrä AGENTS.md:n käytännöt: raw-tiedostojen nimeäminen ingestissä, verify-before-ingest, ei hajatageja, finishing check, omien päätelmien rekisteri (claims-by-source), grill-osio ja lokin grill-etuliite
- [x] Templaatin README: linkki tähän repoon esimerkkinä

## D. Postaukset (LinkedIn lyhyt, kotisivun blogi kattava)
Sisältö kotisivurepossa: AnaHill.github.io/_notes/llm-wiki-post. Luonnostelu rinnakkain, julkaisu vasta B:n jälkeen (tarvitsee linkin).
- [x] Kopioi postausmuistiinpanot (entinen osio 6) kotisivurepoon; tiedosto on valmiina Clauden scratchpadissa (ks. 31.10. chat)
- [ ] Blogipostaus ensin. 
  - [ ] lisää sinne tätä "samalla ne korostavat entisestään laadukkaan dataperustan, hyvän datan hallinnan ja oikeiden arkkitehtuuripäätösten merkitystä." kohtaa, voisiko saada muutakin kuin datalaatu mukaan
- [ ] LinkedIn-postaus: viittaa repoon, zenodoon ja blogiin
