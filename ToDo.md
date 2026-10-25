# Tarkistuslista 24.10.2026
<!-- temp file that will be deleted -->

## 1. main.md: oma läpilukeminen ja muokkaus (tehdään ensin)
- [ ] Lue koko main.md ja muokkaa tekstiä. Lähdetarkistus vasta tämän jälkeen, muuten väitelista vanhenee
- [ ] Mieti, voisiko ottaa esim Obsidianilla kuvan lähteiden riippuvuuksista, ns Graph View, toisiko lisäarvoa tähän
- [ ] Synteesikohdat: `docs/claims-by-source.md:n` osio *"Claims that rest on the author's own synthesis or are not cited"* (17 numeroitua kohtaa). Kohdat 1, 3, 9, 10, 14 ja 15 pehmennettiin 24.10. (ks.` docs/lint-fixes-2026-10-24.md`, ryhmä 7): lue uudet sanamuodot ja päätä, kelpaavatko. Jäljellä olevat kohdat (2, 4, 5–8, 11–13) ovat ennallaan; 16 ja 17 ovat outlookin hypoteeseja. Motivation-lauseen "needs citation(s)" -kommentti on yhä paikallaan (lause sai nyt lähteitä)
- [ ] Käy läpi omat HTML-kommenttisi main.md:ssä: `grep -n "<!--" main.md` (mm. "needs citation(s)" Motivation-osion lihavoidulla lauseella ja "Continue manual check here")
- [ ] Tyylimerkinnät: `grep -n "not really my style" main.md` (nyt 2 paria abstraktissa). Käydään läpi vasta kun olet lukenut koko main.md. Claude ehdottaa uudelleenkirjoitukset sinun tyylilläsi, kunhan annat esimerkin omasta tyylistäsi (esim. Mäki 2023 -teksti tai notes.md)
- [ ] Uusi osio "Discussion and future outlook" (ennen Limitations/Conclusion): lue ja muokkaa omalla tyylilläsi. Kaksi kohtaa: sensor fusion + AI, ja laitteen osuuden poisto signaalista (system identification). 
- [ ] Hankittava PDF: Hu, Sugita, Fujiu, Tixier-Mita & Toshiyoshi (2026), *Biomed. Phys. Eng. Express* 12(4), 045036, doi:10.1088/2057-1976/ae87aa (läpinäkyvä TFT-MEA, sähköisen ja optisen datan piirteet yhdistetty, ohjaamaton ML + SHAP, isoprenaliini-proof-of-concept). Viittaa Ryynänen 2018:aan. Vain abstrakti on nähty; kokotekstistä pitää tarkistaa solutyyppi, otoskoko, piirteet, menetelmät ja rajoitukset. allenna nimellä *raw/hu-2026-tft-mea-multimodal.pdf* ja lisää nimi .gitignoreen ennen committia. Sitten ingest ja outlookin päivitys (sensor fusion -kappale ja lause "mostly analysed separately", synteesikohta 16, wiki/multimodal-measurement.md)
  - Abstract lupaava: Microelectrode arrays (MEAs) provide powerful platforms for large-scale in vitro cardiac tissue analysis. We present a machine learning (ML)-assisted framework for multimodal characterization of cardiomyocyte activity recorded using a transparent thin-film-transistor MEA, allowing simultaneous acquisition of electrophysiological and optical data. The features of both modalities were integrated, and unsupervised learning identified contraction patterns without prior labels. Reliability was assessed with supervised models and SHapley Additive Explanations to confirm feature importance and label consistency. Pharmacological validation with isoprenaline showed the expected increase in beating frequency, detected automatically by our pipeline. Multimodal feature correlations with emergent labels demonstrated that interpretable ML can extract biologically meaningful insights from complex datasets. While isoprenaline served as a proof-of-concept, the framework is applicable for detecting diverse drug- or disease-induced cardiac network changes. This approach enables scalable, label-free and automated assessment of cardiomyocytes networks for drug discovery, toxicity screening, and mechanistic studies. 

Tehty
- [x] Tämä riittää, ei abstractissa tarvita: Conclusionin viimeinen kappale viittaa nyt osioon ja Limitationsissa on kohta (vii) "outlook is speculative" (lisätty 24.10.). Päätä vielä, mainitaanko osio Abstractissa
- [x] Korjattu: julkaisussa on minun nimi lyhennetty, mutta laitetaan nyt samalla tähänkin, eli muutettu muotoon Mäki, A.-J.
- [x] Välimäki ym. (2021) -viite korvattu 25.10. Ryynänen ym. (2018) -artikkelilla (JJAP 57, 117001; avoin, täysi teksti luettu, raw/ryynanen-2018-single-cell-mea.pdf): yhden solun MEA läpinäkyvillä elektrodeilla ja samanaikainen videoanalyysi. Declarationsin virke vahvistettu 25.10.: yhteys on CoEBoC-tutkimuskollaboraatio (Tampere)
- [x] Vuorenpää ym. (2023) ingestoitu 24.10. (raw/vuorenpaa-2023-mps-building-blocks.pdf) ja lisätty outlookiin kahteen kohtaan; Declarations mainitsee päällekkäiset kirjoittajat (Välimäki, Pekkanen-Mattila). Tarkista silti itse sanamuodot
- [x] Hayakawa ym. (2014) ingestoitu 24.10. (PDF nimetty raw/hayakawa-2014-motion-fp.pdf). Tarkista silti itse: onko main.md:n tiivistys (suora lineaarinen yhteys lääkekohtaisilla kulmakertoimilla, ei-arytmiset tilanteet) oikein. Kirjoittaja katsonut kuvat, tukevat väitteitä 
- [x] Figure 2 -vuokaavio: kolmas FPD-päätepistekäytäntö (Dunhamin T-aallon päätepiste, trapetsimenetelmä) lisätty 24.10. Tarkista renderöinnin jälkeen, että uuden reunan teksti ei veny liian pitkäksi

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

Tehty
- [x] Kohdan 4 virke (käänteisongelma huonosti asetettu) lisätty outlookiin 24.10.; muut peer review -korjaukset (1, 2, 3, 5, 6) tehty samana päivänä, ks. docs/lint-fixes-2026-10-24.md, ryhmät 10 ja 11
- [x] Lint 24.10.: korjaukset 1–4, 6 ja 7 tehty (indeksi, maturaatiosivu, critical assessment, Weiser-Bitoun-sivu, neljä uutta sivua, main.md:n pehmennykset). Kohta 5 ei vaadi muutosta (täystekstit luettiin aina kun mahdollista; Välimäki ei ollut mahdollinen). Lue koonti docs/lint-fixes-2026-10-24.md ennen committia
- [x] Committaa 24.10. asti tehdyt muutokset (git status oli tyhjä). Uudet muutokset (lint-korjaukset, ToDo, docs) vielä committaamatta. Avoimet PDF:t (Hayakawa, Vuorenpää) saavat olla seurannassa; Pramudito ja Clements pysyvät .gitignoressa

## 4. Zenodo-vienti vasta lopuksi
- [ ] pdf-muutos: valitse työkalu ja testaa taulukot, Unicode-merkit ja LaTeX-kaava (ks. docs/pdf-export-notes.md)
- [ ] Mermaid-kaaviot: 2 kpl renderöitävä kuviksi ennen PDF-vientiä. Tehdään lopuksi mermaid-liven kautta sopivaksi kuvamuodoksi
- [ ] Tarkista PDF:stä: HTML-kommentit eivät näy, hash-tunnisteet (\#CM01 jne.) näkyvät oikein, lähdeluettelo vastaa tekstiä
- [ ] Zenodo-metatiedot: lisenssi CC BY 4.0, rahoitus (ei rahoitusta, harrastus), avainsanat, tekijä "Antti-Juhana Mäki, Independent researcher", päivämäärä ja versio, tallennus liitetään Mäki-tietueeseen (Version v3)

Tehty
- [x] GitHub-linkki: pysyy ennallaan eikä main.md:tä muuteta; tagi on valinnainen (ks. docs/pdf-export-notes.md, osio "Repository link and snapshot")
- [x] Repon lisenssi: CC BY 4.0 kirjoitetulle sisällölle (LICENSE) ja MIT koodille (scripts/LICENSE) sekä README:n Licence-osio lisätty 24.10.; raw/-PDF:t eivät kuulu siihen. README:hen lisätään linkki Zenodoon julkaisun jälkeen
- [x] Declarations-teksti hyvä, pidetään näin
- [x] Zenodo-päätökset: jätetään GitHub-linkki Declarationsiin

## 5. Kun julkaistu Zenodossa
- [ ] Päivitä README.md:n alku viittaamaan myös julkaisuun: "The paper is in main.md and published in <link>"
- [ ] Linkitä README myös https://github.com/AnaHill/llm-wiki-academic-template
  - [ ] Päivitä tuo repo niillä tässä repossa löydetyillä hyvillä muutoksilla, esim skriptit yms
- [ ] Mieti postaus aiheesta
  - Tärkeimmät: 1) data laatu; uusien lähteiden ja niistä tehtyjen päätösten tarkastaminen heti, ettei väärä informaatio leviä moneen paikkaan, 2) good-old-googlettu ja lähteiden löytäminen ja niiden lähteiden sekä siihen viittaaminen lähteiden läpikäyminen, 3) skriptit yms testit varmistamaan datalaatua, 4) hämmentävä suuri ero Claude code vs Gemini notebook
  -  
  - kuinka tekisin uudelleen: datan eli lähteiden tarkasteleminen heti alussa paremmin, datalaatu kunniaan
    - kattavampi lähdehaku useammalla eri tavalla, esim. toinen LLM kuten Gemini, oma googlettelu/Scholar ja lähteiden viitteiden ja viittausten oma tarkastelu
    - esimerkkinä LLM-wikin riski: wikisivut sisälsivät lähteen vastaisia väitteitä (mm. Ismaili, Matsuda, Hwang, Kabanov), jotka löytyivät vasta lähdetekstin ja väitteiden rivi riviltä -vertailussa
  - Kuinka hyvin rakennettu wiki ja muut auttoivat joka kerta kun Claude teki jotain
    - Claude muisti päivittää pelkän main lisäksi myös login ja indeksit yms oleelliset
    - tulee aina kelpo Ehdotus commit-viestiksi: *reword the Declarations sentence about colleagues to name the CoEBoC collaboration* (koska haluan nämä aina varmistaa ilman automatisointia)
- [ ] Mieti kattavampi blogipostaus aiheesta, tukisi hyvin omaa kotisivua