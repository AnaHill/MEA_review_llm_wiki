# Tarkistuslista 24.10.2026
<!-- temp file that will be deleted -->
- [ ] Oma lähdetarkistus: 
  - Tarkista jokainen lähde docs/claims-by-source.md:n kappaletta vasten ja aloita niistä, joiden tilana on "from the wiki page"
  - Muokkaa main.md:tä ensin ja tarkista lähteet vasta sen jälkeen
  - Muuten väitelista vanhenee (docs/claims-by-source.md on koottu 18.10.). 
- [ ] kun oma lähdetarkistus valmis, aja listan päivitys uudelleen

main.md:ssä on yhä synteesikohtia (claims-by-source.md:n lopun lista 1–15), joissa on yleistyksiä ilman lähdettä (erityisesti 1, 3, 9, 10, 14, 15). Ne jäivät sinun harkittavaksi. Lokiin on kirjattu merkintä.

- main.md
  - [ ] Tyylimerkinnät: käydään läpi vasta kun olen lukenut koko main.md. Merkinnät löytää komennolla grep -n "not really my style" main.md (nyt 2 paria abstraktissa). Claude ehdottaa uudelleenkirjoitukset minun tyylilläni, kunhan annan esimerkin omasta tyylistäni (esim. Mäki 2023 -teksti tai notes.md).
  - [ ] olen merkannut main.md:ssä, mitkä kohdat ei mm. kuulosta minulta kuten tämä <!-- not really my style of text starts --> build on sound methodological foundations. <!-- not really my style of text ends -->
  - [ ] Viimeinen osio: väitteet, joilla ei ole yhtä lähdettä, vaan ne ovat oma synteesisi. Niitä ovat neljä aukkoa, päätelmä avoimista alustoista ja MEA-natiivin maturaatioindeksin kokoaminen olemassa olevista osista.
    - `docs\claims-by-source.md`, riviltä 173 alkane _## Claims that rest on the author's own synthesis or are not cited_
  - [ ] Valinnainen: Table 2:n rivi 1 (peak-to-peak) ja rivi 4 (R-to-T-peak) ovat lähes päällekkäiset. Voisin yhdistää ne, jos haluat selkeämmän taulukon.

- [ ] Oma lähdetarkistus listan avulla. Aloita lähteistä, jotka ovat vain wikisivujen varassa. Vertaa docs\claims-by-source.md sekä main.md: erityisen tarkasti katso *Altrocchi, Correia, Ernault, Fetterman, Guerrelli, Hwang, Ismaili, Matsuda, Maurissen, Park 2025 ja Scheurer*.
  - [ ] Kun valmis, todeta että Declarations kohdan AI-lauseen väite lähteiden tarkistuksesta pitää paikkansa



## Zenodo vienti vasta lopuksi
- [ ] pdf muutos: valitse työkalu ja testaa taulukot, Unicode-merkit ja LaTeX-kaava.
- [ ] Mermaid-kaaviot: 2 kpl on renderöitävä kuviksi ennen PDF-vientiä (ks. docs/pdf-export-notes.md)
  - tehdään lopuksi mermaid-liven kautta sopivaksi kuvamuodoksi 
- [x] Declarations-teksti hyvä, pidetään näin
- [x] Zenodo-päätökset: jätetään GitHub-linkki Declarationsiin.

## Kun julkaistu Zenodossa
- [ ] päivitä Readme.md alku kohta viittaamaan myös siihen  "The paper is in main.md and published in <link>
- [ ] mieti postaus aiheesta
  - kuinka tekisin uudelleen; datan, eli lähteiden tarkasteleminen heti alussa paremmin --> datalaatu kunniaan
  - kattavampi lähdehaku useammalla eri tavalla; esim toinen LLM kuten Gemini, oma googlettelu/Scholar ja lähteiden viitteiden ja viittausten oma tarkastelu