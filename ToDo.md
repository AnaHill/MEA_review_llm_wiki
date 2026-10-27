# Tarkistuslista 24.10.2026
<!-- temp file that will be deleted -->
Ehdotettu järjestys 27.10.

1. Lue ja muokkaa main.md kokonaan. Jos lukiessa herää epäily jostain lähteeseen liittyvästä kohdasta, merkitse se kommentilla ja jatka eteenpäin.
   - [ ] Tarkista onko Table1 ok
   - kohtaan asti ok
   - Declarations kohdasta alaspäin ok 

<!-- check: -->
1. Pyydä minua päivittämään claims-by-source.md:n numeroidut väitteet valmiista tekstistä (alla oleva 2). Samalla yhtenäistän tunnisteet, joista skripti antoi huomautukset, kuten [Figure 2] ja [our interpretation].
2. Aja seuraava, jolloin jokaisen väitteen alle tulee nykyinen virke main.md:stä.
`python -I scripts/claim_quotes.py --write`
1. Käy lähteet läpi Altrocchin tapaan.

Skriptin kuivaharjoitusta voi käyttää välillä apuna, jos haluat nähdä, missä kohdissa jotain lähdettä viitataan, esimerkiksi 
```python
# tämä ei muuta mitään
python -I scripts/claim_quotes.py --only Hwang. 
```


## 1. main.md: oma läpilukeminen ja muokkaus (tehdään ensin)
- [ ] Lue koko main.md ja muokkaa tekstiä. Lähdetarkistus vasta tämän jälkeen, muuten väitelista vanhenee
- [ ] Mieti, voisiko ottaa esim Obsidianilla kuvan lähteiden riippuvuuksista, ns Graph View, toisiko lisäarvoa tähän
- [ ] Synteesikohdat: `docs/claims-by-source.md:n` osio *"Claims that rest on the author's own synthesis or are not cited"* (17 numeroitua kohtaa). Kohdat 1, 3, 9, 10, 14 ja 15 pehmennettiin 24.10. (ks.` docs/lint-fixes-2026-10-24.md`, ryhmä 7): lue uudet sanamuodot ja päätä, kelpaavatko. Jäljellä olevat kohdat (2, 4, 5–8, 11–13) ovat ennallaan; 16 ja 17 ovat outlookin hypoteeseja. Motivation-lauseen "needs citation(s)" -kommentti on yhä paikallaan (lause sai nyt lähteitä)
- [ ] Käy läpi omat HTML-kommenttisi main.md:ssä: `grep -n "<!--" main.md` (mm. "needs citation(s)" Motivation-osion lihavoidulla lauseella ja "Continue manual check here")
- [ ] Tyylimerkinnät: `grep -n "not really my style" main.md` (nyt 2 paria abstraktissa). Käydään läpi vasta kun olet lukenut koko main.md. Claude ehdottaa uudelleenkirjoitukset sinun tyylilläsi, kunhan annat esimerkin omasta tyylistäsi (esim. Mäki 2023 -teksti tai notes.md)
- [ ] Uusi osio "Discussion and future outlook" (ennen Limitations/Conclusion): lue ja muokkaa omalla tyylilläsi. Kaksi kohtaa: sensor fusion + AI, ja laitteen osuuden poisto signaalista (system identification). 
- [ ] Hankittava PDF: Hu, Sugita, Fujiu, Tixier-Mita & Toshiyoshi (2026), *Biomed. Phys. Eng. Express* 12(4), 045036, doi:10.1088/2057-1976/ae87aa (läpinäkyvä TFT-MEA, sähköisen ja optisen datan piirteet yhdistetty, ohjaamaton ML + SHAP, isoprenaliini-proof-of-concept). Viittaa Ryynänen 2018:aan. Vain abstrakti on nähty; kokotekstistä pitää tarkistaa solutyyppi, otoskoko, piirteet, menetelmät ja rajoitukset. allenna nimellä *raw/hu-2026-tft-mea-multimodal.pdf* ja lisää nimi .gitignoreen ennen committia. Sitten ingest ja outlookin päivitys (sensor fusion -kappale ja lause "mostly analysed separately", synteesikohta 16, wiki/multimodal-measurement.md)
  - Abstract lupaava: Microelectrode arrays (MEAs) provide powerful platforms for large-scale in vitro cardiac tissue analysis. We present a machine learning (ML)-assisted framework for multimodal characterization of cardiomyocyte activity recorded using a transparent thin-film-transistor MEA, allowing simultaneous acquisition of electrophysiological and optical data. The features of both modalities were integrated, and unsupervised learning identified contraction patterns without prior labels. Reliability was assessed with supervised models and SHapley Additive Explanations to confirm feature importance and label consistency. Pharmacological validation with isoprenaline showed the expected increase in beating frequency, detected automatically by our pipeline. Multimodal feature correlations with emergent labels demonstrated that interpretable ML can extract biologically meaningful insights from complex datasets. While isoprenaline served as a proof-of-concept, the framework is applicable for detecting diverse drug- or disease-induced cardiac network changes. This approach enables scalable, label-free and automated assessment of cardiomyocytes networks for drug discovery, toxicity screening, and mechanistic studies. 

## 2. Oma lähdetarkistus (kun main.md:n teksti on valmis)
- [ ] Pyydä Claudea päivittämään `docs/claims-by-source.md` uudelleen valmiista tekstistä
- [ ] Käy jokainen lähde läpi claims-by-source.md:n kappaletta vasten. Wikisivut on jo tarkistettu lähdetekstiä vasten (24.10.), mutta numerot ja kuvatulkinnat kannattaa varmistaa itse, ja kaksi lisätiedostoa jäi lukematta (Correia ja Scheurer, supplementary)
  - Erityisesti: Altrocchi, Correia, Ernault, Fetterman, Guerrelli, Hwang, Ismaili, Matsuda, Maurissen, Park 2025 ja Scheurer (näistä on korjattu eniten)
  - Uudet lähteet: Hayakawa 2014 ja Vuorenpää 2023 on luettu kokonaan (kuvia ei katsottu Vuorenpäältä), mutta main.md:n tiivistykset kannattaa lukea itse; Ryynänen 2018 (korvasi Välimäki 2021:n 25.10.) on luettu kokonaan, kuvia ei katsottu
  - Katso erityisesti outlookin lauseet ja synteesikohdat 16 ja 17 (hypoteeseja, ei löydöksiä)
- [ ] Kun valmis, totea että Declarations-kohdan AI-lauseen väite lähteiden tarkistuksesta pitää paikkansa

## 3. Ennen vientiä
- [ ] Idea tutkittavaksi (valinnainen): *aktivaatio-palautumisintervalli (ARI)* vaihtoehtona peak-to-peak-FPD:lle on todellinen tutkimuskäsite. Se pitää ensin löytää ja lukea; alkuperäinen ehdotus (Chinushi 2001 / Haws & Lux 1990, tarkka nimi ja julkaisu varmistamatta) on `docs/peer_review_missing_references_main.md`:ssä (tiedosto on sittemmin poistettu, ks. git-historia). Ei viitteitä paperiin ennen lukemista (AGENTS: ei keksittyjä viitteitä)
- [ ] Aja `python -I scripts/check.py`: 0 virhettä (odotettu varoitus nyt yksi: Clements 2025 -posterilla ei ole DOI:ta)
- [ ] Poista tämä ToDo.md (temp-tiedosto)

## 4. Zenodo-vienti vasta lopuksi
- [x] Työkalun valinta ja testi tehty 26.10.: VS Code Markdown PDF -lisäosan HTML on hyvä (taulukot, Unicode, kaava, `\#CM01` ok), PDF ei (kuvat jakautuvat sivuille). Päätös: HTML on pohja, PDF tehdään HTML:stä selaimen tulostuksella (ks. docs/pdf-export-notes.md, "Revised export plan")
- [ ] Mermaid-kaaviot: 2 kpl renderöitävä SVG-kuviksi mermaid-liven kautta ja upotettava kuvina (alt-teksteineen), jotta HTML ei lataa Mermaidia ulkoa (nyt versioimaton unpkg-CDN)
- [ ] HTML: lisää näkyvä otsikkolohko (otsikko, tekijä, affiliaatio, päivä) ja `<title>`; front matter ei näy nyt lainkaan
- [ ] HTML: tee DOI- ja muista URL-osoitteista klikattavia (nyt 1 linkki, 26 URL:ia main.md:ssä)
- [ ] Poista HTML-kommentit main.md:stä ennen vientiä (kohta 1); varmista `view source` -tarkistuksella
- [ ] PDF: tulosta valmiista HTML:stä selaimella, `break-inside: avoid` kuville ja taulukoille, ei sivun ylätunnisteita; tarkista kuvat, taulukot, kaava, ei `<!--`/`\#`/tähtiä tekstissä
- [ ] Zenodo: PDF pääasiallisena tiedostona, HTML lisätiedostona; tarkista Zenodon HTML-tiedostojen käsittely ennen kuin luotat pelkkään HTML:ään
- [ ] Zenodo-metatiedot: lisenssi CC BY 4.0, rahoitus (ei rahoitusta, harrastus), avainsanat, tekijä "Antti-Juhana Mäki, Independent researcher", päivämäärä ja versio, tallennus liitetään Mäki-tietueeseen (Version v3)

## 5. Päivitykset repoihin kun julkaistu Zenodossa
- [ ] Päivitä README.md:n alku viittaamaan myös julkaisuun: "The paper is in main.md and published in <link>"
- [ ] Linkitä README myös https://github.com/AnaHill/llm-wiki-academic-template
  - [ ] Päivitä tuo akateeminen repo niillä tässä repossa löydetyillä hyvillä muutoksilla, esim skriptit yms, jotka toimisivat heti uuden LLM-wiki akateemisen paperin prosessissa

## 6. Postaus aiheesta
- DISCLAIMER alkuun: Vältetään AI sloppya, joten kävin itse läpi kaikki lähteet ja varsinkin väitökset

Tärkeimpiä kohtia: 
- 1) data laatu; uusien lähteiden ja niistä tehtyjen päätösten tarkastaminen heti, ettei väärä informaatio leviä moneen paikkaan, "even though 'vibe-researching' is fun, going through sources as soon as possible infront pays in the end" 
  - kuinka tekisin uudelleen: datan eli lähteiden tarkasteleminen heti alussa paremmin, datalaatu kunniaan
  - miten virheellinen tieto leviää tässä repossa (kolme lähtökohtaa):
    ```
    Virhe A, lähteen väärinluku (esim. Ismaili, Matsuda, Hwang, Kabanov):
    raw/lähde.pdf
      -> wiki/papers/lähde.md          (tiivistys liioittelee tai lukee väärin)
      -> wiki/<käsitesivu>.md          (esim. hipsc-cm-maturation.md, critical-assessment-maki-claims.md)
      -> wiki/index.md                 (yhden rivin tiivistelmä)
      -> main.md                       (useaan osioon: tekstiin, taulukkoon, kuvatekstiin)
      -> main.md Abstract/Conclusion   (yleistyy entisestään tiivistyksessä)
      -> docs/claims-by-source.md      (väitelista kopioi virheen main.md:stä)

    Virhe B, tekoälyn oma täydennys ilman lähdettä (esim. "longitudinal" ensimmäisestä luonnoksesta, keksitty "Galli et al. 2024"):
    AI-luonnos -> main.md -> docs/claims-by-source.md -> (wiki-sivujen "Relevance"-osiot)

    Virhe C, paikkakorjaus (esim. Open pipelines -virke 27.10.):
    korjaus yhteen kohtaan -> ristiriita saman virkkeen tai muiden kohtien kanssa
    ```
    - mikä pysäyttää mitäkin: `check.py` pysäyttää rakennevirheet (puuttuvat viitteet, DOI-erot, rikkinäiset linkit), mutta ei sisältöä, joten A, B ja C menevät siitä läpi; claims-by-source ja lähteen lukeminen pysäyttävät A:n ja B:n, kun väite tarkistetaan lähdettä eikä wikisivua vasten; ihmisen kokonaisluenta pysäyttää C:n ja osioiden väliset ristiriidat
    - opetus: mitä aikaisemmassa vaiheessa virhe syntyy, sitä useampaan paikkaan se kopioituu, joten tarkistus kannattaa tehdä jo ingestissä eikä vasta main.md:stä
  - 
  - kattavampi lähdehaku useammalla eri tavalla, esim. toinen LLM kuten Gemini, oma googlettelu/Scholar ja lähteiden viitteiden ja viittausten oma tarkastelu
  - esimerkkinä LLM-wikin riski: wikisivut sisälsivät lähteen vastaisia väitteitä (mm. Ismaili, Matsuda, Hwang, Kabanov), jotka löytyivät vasta lähdetekstin ja väitteiden rivi riviltä -vertailussa
  - esimerkki human-in-the-loopin tärkeydestä (27.10.): Open pipelines -osion avausvirke oli ristiriitainen. Alku sanoi avoimien analyysiputkien ilmestyneen 2022 jälkeen, ja loppu kumosi sen ("open tools such as MultiElec and CardioMDA already existed before 2022"). Loppu oli lisätty 24.10. tarkistuksessa korjaukseksi, koska sekä Lee et al. (2024, Table 3) että Dunham et al. (2022, s. 2) toteavat, että avoimia työkaluja oli jo ennen, mutta alkua ei silloin muutettu vastaamaan sitä. Automaattiset tarkistukset eivät huomanneet ristiriitaa; löysin sen itse lukiessa. Lähteiden perusteella uutta 2022 jälkeen ei ole avoimuus vaan se, että uusia avoimia työkaluja on tehty uusille datatyypeille: CardioMEA HD-MEA-datalle (Lee) ja PhysioMEA sydänorganoideille (Weiser-Bitoun). Opetus: AI:n tekemä paikkakorjaus voi jättää virkkeen ristiriitaiseksi, joten korjauksen jälkeen koko virke pitää lukea uudelleen
  - > When correcting a claim, re-read and if needed rewrite the whole sentence, not only the part that was wrong.
- 2) good-old-googlettu ja lähteiden löytäminen ja niiden lähteiden sekä siihen viittaaminen lähteiden läpikäyminen, 
- 3) skriptit yms testit varmistamaan datalaatua, 
  - Kuinka hyvin rakennettu wiki ja muut auttoivat joka kerta kun Claude teki jotain
    - Claude muisti päivittää pelkän main lisäksi myös login ja indeksit yms oleelliset
    - tulee aina kelpo Ehdotus commit-viestiksi: *reword the Declarations sentence about colleagues to name the CoEBoC collaboration* (koska haluan nämä aina varmistaa ilman automatisointia)
- 4) (mieti vielä onko tarpeen) hämmentävä suuri ero Claude code vs Gemini notebook 

- [x] kattavampi blogipostaus aiheesta, joka tukisi hyvin omaa kotisivua, osuus siirretty kotisivun _notes/llm-wiki-post kansioon jonne vapaamuotoista hahmotelmaa aloiteltu