# Tarkistuslista 24.10.2026
<!-- temp file that will be deleted -->

## 1. main.md: oma läpilukeminen ja muokkaus (tehdään ensin)
- [ ] Lue koko main.md ja muokkaa tekstiä. Lähdetarkistus vasta tämän jälkeen, muuten väitelista vanhenee
- [ ] Synteesikohdat: docs/claims-by-source.md:n osio "Claims that rest on the author's own synthesis or are not cited" (15 numeroitua kohtaa). Kohdissa 1, 3, 9, 10, 14 ja 15 on yleistyksiä ilman lähdettä: lisää lähde, pehmennä tai poista. Niitä ovat mm. neljä aukkoa, päätelmä avoimista alustoista ja MEA-natiivin maturaatioindeksin kokoaminen olemassa olevista osista
- [ ] Käy läpi omat HTML-kommenttisi main.md:ssä: `grep -n "<!--" main.md` (mm. "needs citation(s)" Motivation-osion lihavoidulla lauseella ja "Continue manual check here")
- [ ] Tyylimerkinnät: `grep -n "not really my style" main.md` (nyt 2 paria abstraktissa). Käydään läpi vasta kun olet lukenut koko main.md. Claude ehdottaa uudelleenkirjoitukset sinun tyylilläsi, kunhan annat esimerkin omasta tyylistäsi (esim. Mäki 2023 -teksti tai notes.md)
- [ ] Uusi osio "Discussion and future outlook" (ennen Limitations/Conclusion): lue ja muokkaa omalla tyylilläsi. Kaksi kohtaa: sensor fusion + AI, ja laitteen osuuden poisto signaalista (system identification). Päätä, viitataanko osioon Abstractissa, Conclusionin viimeisessä kappaleessa ("Looking forward ...") ja Limitationsissa (esim. "outlook is speculative")
- [x] Figure 2 -vuokaavio: kolmas FPD-päätepistekäytäntö (Dunhamin T-aallon päätepiste, trapetsimenetelmä) lisätty 24.10. Tarkista renderöinnin jälkeen, että uuden reunan teksti ei veny liian pitkäksi

## 2. Oma lähdetarkistus (kun main.md:n teksti on valmis)
- [ ] Pyydä Claudea päivittämään docs/claims-by-source.md uudelleen valmiista tekstistä
- [ ] Käy jokainen lähde läpi claims-by-source.md:n kappaletta vasten. Wikisivut on jo tarkistettu lähdetekstiä vasten (24.10.), mutta numerot ja kuvatulkinnat kannattaa varmistaa itse, ja kaksi lisätiedostoa jäi lukematta (Correia ja Scheurer, supplementary)
  - Erityisesti: Altrocchi, Correia, Ernault, Fetterman, Guerrelli, Hwang, Ismaili, Matsuda, Maurissen, Park 2025, Scheurer (näistä on korjattu eniten)
- [ ] Kun valmis, totea että Declarations-kohdan AI-lauseen väite lähteiden tarkistuksesta pitää paikkansa

## 3. Ennen vientiä
- [ ] Aja `python -I scripts/check.py`: 0 virhettä (odotettu varoitus: Clements 2025 -posterilla ei ole DOI:ta)
- [ ] Committaa: uudet tiedostot (wikisivut, raw-PDF:t, docs, scripts, ToDo.md ellei poisteta) ovat vielä git-seurannan ulkopuolella. Tarkista, että ei-avoimet PDF:t (Pramudito, Clements) pysyvät .gitignoressa
- [ ] Poista tämä ToDo.md (temp-tiedosto)

## 4. Zenodo-vienti vasta lopuksi
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
