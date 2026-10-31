# ToDo (päivitetty 31.10.2026)
<!-- temp file that will be deleted -->
<!-- Continue manual check here -->
jatka kohdasta:
- 

Järjestys: **A → B → C1 ja D-julkaisu.** C2 ja D-luonnostelu eivät odota mitään. Tehdyt kohdat poistetaan (git-historia säilyttää ne).

## A. Paperin sisältö (main.md ja tukitiedostot)
Valmis, kun teksti on lukittu ja jokainen väite on tarkistettu lähdettä vasten.

Jo tehty: Table 1 ok; Declarations alaspäin ok; uusi kypsyyshaku 30.10. (docs/maturation-mea-search.md), Li 2025 ja Lin 2023 ingestoitu ja lisätty main.md:hen.

### A1. Oma läpiluku ja muokkaus (tehdään ensin, muuten väitelista vanhenee)
Jos lukiessa herää epäily lähteeseen liittyvästä kohdasta, merkitse se kommentilla ja jatka eteenpäin.
- [ ] Lue koko main.md ja muokkaa tekstiä
- [ ] Morphology-osion alku: "FP waveform morphology varies substantially across preparations, maturation states, …". Tukevatko Ernault 2024 ja Mäki 2023 sanaa "substantially", vai riittääkö "varies"? (Sama tyyppi kuin 29.10. korjattu "can substantially influence".)
- [ ] "Discussion and future outlook": lue ja muokkaa omalla tyylilläsi (sensor fusion + AI; laitteen osuuden poisto signaalista)
- [ ] Synteesikohdat 1–21 (docs/claims-by-source.md, osio "Claims that rest on the author's own synthesis or are not cited", ainoa rekisteri omille päätelmille): kohdat 1, 3, 9, 10, 14 ja 15 pehmennettiin 24.10. (docs/lint-fixes-2026-10-24.md, ryhmä 7), päätä kelpaavatko; 16, 17 ja 21 ovat outlookin hypoteeseja; 18–20 lisättiin 30.10.
- [ ] Omat HTML-kommentit: `grep -n "<!--" main.md` (30.10. jäljellä `<!-- jatka -->` Open pipelines -osiossa)
- [ ] Päätä Hu et al. (2026), *Biomed. Phys. Eng. Express* 12(4), 045036, doi:10.1088/2057-1976/ae87aa (läpinäkyvä TFT-MEA, sähköinen + optinen data, ohjaamaton ML + SHAP; vain abstrakti nähty). Jos mukaan: hanki PDF nimellä raw/hu-2026-tft-mea-multimodal.pdf, lisää nimi .gitignoreen ennen committia, ingest ja outlookin päivitys (sensor fusion -kappale, "mostly analysed separately", synteesikohta 16, wiki/multimodal-measurement.md). Jos ei: siirrä "ei tähän versioon" -listalle
- [ ] Valinnainen: toisiko Obsidianin Graph View -kuva lähteiden riippuvuuksista lisäarvoa?
- Vinkki: isommat päätökset voi käydä läpi komennolla `/grill-paper` ennen muokkausta

### A2. claims-by-source.md uudelleen valmiista tekstistä
- [ ] Pyydä Claudea päivittämään numeroidut väitteet valmiista tekstistä. Huomioi: synteesikohta 8 lainaa vielä vanhaa "can substantially influence measured drug effects" (main.md: "can influence", 29.10.); samoin kaikki 27.–30.10. muutetut kohdat (abstrakti, Open pipelines, Fiducial-lista ja Table 2, FPDc-kappaleet, Maturation, High-throughput, Outlook, Conclusion; ks. wiki/log.md). Samalla yhtenäistetään tunnisteet, joista skripti huomautti ([Figure 2], [our interpretation])
- [ ] Aja `python -I scripts/claim_quotes.py --write`, jolloin jokaisen väitteen alle tulee nykyinen virke main.md:stä. (Kuivaharjoitus ei muuta mitään, esim. `python -I scripts/claim_quotes.py --only Hwang.`)

### A3. Oma lähdetarkistus
- [ ] Käy jokainen lähde läpi claims-by-source.md:n kappaletta vasten Altrocchin tapaan. Wikisivut on tarkistettu lähdetekstiä vasten 24.10., mutta numerot ja kuvatulkinnat kannattaa varmistaa itse
  - Erityisesti: Altrocchi, Correia, Ernault, Fetterman, Guerrelli, Hwang, Ismaili, Matsuda, Maurissen, Park 2025 ja Scheurer (näistä on korjattu eniten); lukematta jääneet liitteet: Correia ja Scheurer supplementary
  - Uudet: Hayakawa 2014 ja Vuorenpää 2023 luettu kokonaan (Vuorenpään kuvia ei katsottu); Ryynänen 2018 luettu kokonaan, kuvia ei katsottu; Li 2025 ja Lin 2023 luettu liitteineen, Li:n luvut tarkistettu Supplementary Tableista 2–3 (main.md käyttää S3:n CV- ja spike amplitude -lukuja). Lue main.md:n tiivistykset itse
  - Outlookin lauseet ja synteesikohdat 16 ja 17 ovat hypoteeseja, eivät löydöksiä

### A4. Lopputarkistukset
- [ ] Päätä highlights-kohdasta (tieteelliset havainnot, esim. FPDc-korjauksen validoinnin puute ja MEA-pohjaisten kypsyysviitearvojen puute; LLM-wikin kehityskohdat)
- [ ] Valinnainen: uusi tarkistus toisella mallilla (esim. OpenAI; Geminillä tehty)
- [ ] Totea, että Declarationsin AI-lauseen väite lähteiden tarkistuksesta pitää paikkansa
- [ ] `python -I scripts/check.py`: 0 virhettä (odotettu varoitus yksi: Clements 2025 -posterilla ei DOI:ta)

### Ei tähän versioon
- Aktivaatio-palautumisintervalli (ARI) vaihtoehtona peak-to-peak-FPD:lle: todellinen tutkimuskäsite, mutta lähde (Chinushi 2001 / Haws & Lux 1990, varmistamatta) pitää ensin löytää ja lukea; alkuperäinen ehdotus on poistetussa docs/peer_review_missing_references_main.md:ssä (git-historia). Ei viitteitä ennen lukemista

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
- [ ] README: linkki https://github.com/AnaHill/LLM-wiki-academic-template ja omaan blogipostaukseen
- [ ] Tag tai GitHub-release julkaistusta versiosta
- [ ] Poista tämä ToDo.md

### C2. LLM-wiki-academic-template (voi tehdä jo nyt)
- [ ] Siirrä templaattiin tässä repossa hyväksi todetut, heti käytettävät osat: scripts/check.py, scripts/claim_quotes.py, scripts/render_pdf_pages.py, `.claude/skills/grill-paper`
- [ ] Siirrä AGENTS.md:n käytännöt: raw-tiedostojen nimeäminen ingestissä, verify-before-ingest, ei hajatageja, finishing check, omien päätelmien rekisteri (claims-by-source), grill-osio ja lokin grill-etuliite
- [ ] Templaatin README: linkki tähän repoon esimerkkinä

## D. Postaukset (LinkedIn lyhyt, kotisivun blogi kattava)
Sisältö kotisivurepossa: AnaHill.github.io/_notes/llm-wiki-post. Luonnostelu rinnakkain, julkaisu vasta B:n jälkeen (tarvitsee linkin).
- [ ] Kopioi postausmuistiinpanot (entinen osio 6) kotisivurepoon; tiedosto on valmiina Clauden scratchpadissa (ks. 31.10. chat)
- [ ] LinkedIn-postaus
- [ ] Blogipostaus
