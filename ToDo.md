# Tarkistuslista 24.10.2026
<!-- temp file that will be deleted -->

## 1. main.md: oma läpilukeminen ja muokkaus (tehdään ensin)
- [ ] Lue koko main.md ja muokkaa tekstiä. Lähdetarkistus vasta tämän jälkeen, muuten väitelista vanhenee
- [ ] Synteesikohdat: docs/claims-by-source.md:n osio "Claims that rest on the author's own synthesis or are not cited" (17 numeroitua kohtaa). Kohdissa 1, 3, 9, 10, 14 ja 15 on yleistyksiä ilman lähdettä: lisää lähde, pehmennä tai poista. Niitä ovat mm. neljä aukkoa, päätelmä avoimista alustoista ja MEA-natiivin maturaatioindeksin kokoaminen olemassa olevista osista. Kohdat 16 ja 17 ovat outlookin hypoteeseja (tekstissä merkitty hypoteeseiksi). Kohdan 1 vasta-argumentti: Vuorenpää ym. 2023 (osio 6.1.1) sanoo, että AP:iden ja FP:iden parametrisointi on vakiintunutta ja mahdollistaa tulosten vertailun, joten pehmennä "major source of variability" (Abstract, Motivation) tai perustele se paremmin
- [ ] Käy läpi omat HTML-kommenttisi main.md:ssä: `grep -n "<!--" main.md` (mm. "needs citation(s)" Motivation-osion lihavoidulla lauseella ja "Continue manual check here")
- [ ] Tyylimerkinnät: `grep -n "not really my style" main.md` (nyt 2 paria abstraktissa). Käydään läpi vasta kun olet lukenut koko main.md. Claude ehdottaa uudelleenkirjoitukset sinun tyylilläsi, kunhan annat esimerkin omasta tyylistäsi (esim. Mäki 2023 -teksti tai notes.md)
- [ ] Uusi osio "Discussion and future outlook" (ennen Limitations/Conclusion): lue ja muokkaa omalla tyylilläsi. Kaksi kohtaa: sensor fusion + AI, ja laitteen osuuden poisto signaalista (system identification). 
- [x] Tämä riittää, ei abstractissa tarvita: Conclusionin viimeinen kappale viittaa nyt osioon ja Limitationsissa on kohta (vii) "outlook is speculative" (lisätty 24.10.). Päätä vielä, mainitaanko osio Abstractissa
- [x] Korjattu: julkaisussa on minun nimi lyhennetty, mutta laitetaan nyt samalla tähänkin, eli muutettu muotoon Mäki, A.-J.
- [x] Välimäki ym. (2021): vahvistettu 24.10., että kyseessä on MEA + video; DOI:ta tai PDF:ää ei ole, joten viite pysyy portaalin tietueen varassa (kohdat a–c suljettu)
- [x] Vuorenpää ym. (2023) ingestoitu 24.10. (raw/vuorenpaa-2023-mps-building-blocks.pdf) ja lisätty outlookiin kahteen kohtaan; Declarations mainitsee päällekkäiset kirjoittajat (Välimäki, Pekkanen-Mattila). Tarkista silti itse sanamuodot
- [x] Hayakawa ym. (2014) ingestoitu 24.10. (PDF nimetty raw/hayakawa-2014-motion-fp.pdf). Tarkista silti itse: onko main.md:n tiivistys (suora lineaarinen yhteys lääkekohtaisilla kulmakertoimilla, ei-arytmiset tilanteet) oikein. Kirjoittaja katsonut kuvat, tukevat väitteitä 
- [x] Figure 2 -vuokaavio: kolmas FPD-päätepistekäytäntö (Dunhamin T-aallon päätepiste, trapetsimenetelmä) lisätty 24.10. Tarkista renderöinnin jälkeen, että uuden reunan teksti ei veny liian pitkäksi

## 2. Oma lähdetarkistus (kun main.md:n teksti on valmis)
- [ ] Pyydä Claudea päivittämään docs/claims-by-source.md uudelleen valmiista tekstistä
- [ ] Käy jokainen lähde läpi claims-by-source.md:n kappaletta vasten. Wikisivut on jo tarkistettu lähdetekstiä vasten (24.10.), mutta numerot ja kuvatulkinnat kannattaa varmistaa itse, ja kaksi lisätiedostoa jäi lukematta (Correia ja Scheurer, supplementary)
  - Erityisesti: Altrocchi, Correia, Ernault, Fetterman, Guerrelli, Hwang, Ismaili, Matsuda, Maurissen, Park 2025 ja Scheurer (näistä on korjattu eniten)
  - Uudet lähteet: Hayakawa 2014 ja Vuorenpää 2023 on luettu kokonaan (kuvia ei katsottu Vuorenpäältä), mutta main.md:n tiivistykset kannattaa lukea itse; Välimäki 2021 perustuu vain portaalin tietueeseen ja sinun vahvistukseesi (MEA + video), eikä sisältöä ole luettu
  - Katso erityisesti outlookin lauseet ja synteesikohdat 16 ja 17 (hypoteeseja, ei löydöksiä)
- [ ] Kun valmis, totea että Declarations-kohdan AI-lauseen väite lähteiden tarkistuksesta pitää paikkansa

## 3. Ennen vientiä
- [ ] Lint 24.10. tehty (ks. wiki/log.md, merkintä lint): korjausehdotukset odottavat päätöstäsi: indeksin vanhentuneet rivit (Ismaili, Matsuda, Park 2025, Hwang, Scheurer, Ernault, Mäki v2/v3, Hayakawa-järjestys, Last updated), wiki/hipsc-cm-maturation.md (Fetterman ja Correia -yleistykset), wiki/critical-assessment-maki-claims.md (Ernault "majority", "field converging", PhysioMEA ja kääntäminen, Fig. 6), Weiser-Bitoun-sivulta puuttuva käänteis-/inversiokäsittely, Limitations (v) ja Välimäki
- [ ] Aja `python -I scripts/check.py`: 0 virhettä (odotetut varoitukset nyt kolme: Clements 2025 -posterilla ei ole DOI:ta; Välimäki 2021 -viitteellä ei ole DOI:ta eikä raw-tiedostoa)
- [x] Committaa 24.10. asti tehdyt muutokset (git status oli tyhjä). Uudet muutokset (lint-korjaukset, ToDo, docs) vielä committaamatta. Avoimet PDF:t (Hayakawa, Vuorenpää) saavat olla seurannassa; Pramudito ja Clements pysyvät .gitignoressa
- [ ] Poista tämä ToDo.md (temp-tiedosto)

## 4. Zenodo-vienti vasta lopuksi
- [ ] GitHub-repo julkaisuhetken tilaan: tee viimeisen commitin jälkeen tagi (esim. `v1.0-preprint`) ja GitHub-release, ja harkitse virkettä Declarationsin Data and code availability -kohtaan ("The state of the repository at the time of deposit is tagged v1.0-preprint."). Tagi pitää tehdä sen commitin päälle, jossa virke jo on. Ks. docs/pdf-export-notes.md, osio "Repository snapshot"
- [ ] Repon lisenssi: repossa ei ole LICENSE-tiedostoa eikä README mainitse lisenssiä; Declarations lupaa vain tekstille CC BY 4.0. Päätä koodin (scripts/) ja wiki-sisällön lisenssi ja kirjaa se README:hen; avoimet raw-PDF:t ovat omien lisenssiensä alaisia (esim. CC BY-NC-ND), ei-avoimet pysyvät .gitignoressa
- [ ] pdf-muutos: valitse työkalu ja testaa taulukot, Unicode-merkit ja LaTeX-kaava (ks. docs/pdf-export-notes.md)
- [ ] Mermaid-kaaviot: 2 kpl renderöitävä kuviksi ennen PDF-vientiä. Tehdään lopuksi mermaid-liven kautta sopivaksi kuvamuodoksi
- [ ] Tarkista PDF:stä: HTML-kommentit eivät näy, hash-tunnisteet (\#CM01 jne.) näkyvät oikein, lähdeluettelo vastaa tekstiä
- [ ] Zenodo-metatiedot: lisenssi CC BY 4.0, rahoitus (ei rahoitusta, harrastus), avainsanat, tekijä "Antti-Juhana Mäki, Independent researcher", päivämäärä ja versio, tallennus liitetään Mäki-tietueeseen (Version v3)
- [x] Declarations-teksti hyvä, pidetään näin
- [x] Zenodo-päätökset: jätetään GitHub-linkki Declarationsiin

## 5. Kun julkaistu Zenodossa
- [ ] Päivitä README.md:n alku viittaamaan myös julkaisuun: "The paper is in main.md and published in <link>"
- [ ] Mieti postaus aiheesta
  - kuinka tekisin uudelleen: datan eli lähteiden tarkasteleminen heti alussa paremmin, datalaatu kunniaan
  - kattavampi lähdehaku useammalla eri tavalla, esim. toinen LLM kuten Gemini, oma googlettelu/Scholar ja lähteiden viitteiden ja viittausten oma tarkastelu
  - esimerkkinä LLM-wikin riski: wikisivut sisälsivät lähteen vastaisia väitteitä (mm. Ismaili, Matsuda, Hwang, Kabanov), jotka löytyivät vasta lähdetekstin ja väitteiden rivi riviltä -vertailussa
