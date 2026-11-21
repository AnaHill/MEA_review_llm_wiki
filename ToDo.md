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
- [x] 2. Eniten korjatut (jäljellä): Matsuda, Maurissen, Park 2025 (kaikki tarkistettu 24.10. vain osittain)
- [x] 3. Uusimmat (jäljellä): Vuorenpää 2023, Ryynänen 2018 (kummankin kuvat katsomatta)
- [x] 4. Loput (jäljellä): Park 2026, Pramudito, Weiser-Bitoun
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
- [x] Jos main.md muuttuu: aja `python -I scripts/check_abbreviations.py`

### A4. Lopputarkistukset
- [x] Uusi tarkistus toisella mallilla (esim. OpenAI; Geminillä tehty). **Anna arvioijalle `docs/ai-review-brief.md` + `main.md`, ei muuta** — main.md on itsenäinen (koko teksti, molemmat kuvat, lähdeluettelo). Brief kertoo arvioijalle, mitä katsaus jo myöntää itsestään (ei toisteta rajoituksia), mikä palaute on hyödyllistä, DOI-vaatimuksen jokaiselle ehdotetulle lähteelle ja palautusmuodon (koko vastaus yhdessä nelibacktick-lohkossa, valmiina liitettäväksi). Liitä vastaus Claudelle: kritiikki käsitellään listana, mahdolliset lähde-ehdotukset verify-before-ingest -vaiheen kautta
- [x] Totea, että Declarationsin AI-lauseen väite lähteiden tarkistuksesta pitää paikkansa (nyt: väitteet "listed in a checklist for verification"); kun A2 valmis, voi vahvistaa muotoon "…was checked against that source by the author"
- [x] `python -I scripts/check.py`: 0 virhettä (odotettu varoitus yksi: Clements 2025 -posterilla ei DOI:ta)

### A5 Valinnaisia muualle kuin main.md tiedostoon
- [x] Wiki kuntoon lopuksi: 
  - [x] saisiko backlinkit ja tagit paremmaksi, jotta graafiesitys paranisi?
  - [x] `wiki/index.md`:n "Last updated" -päiväys ja muu siistintä (lint 3.11., kohta 10)

- [x] ota lähteet talteen lopuksi omaan paikkaan

- [ ]`README.md` päivityksiä
  - [x] kuvat siirretty postauksen alla. Tuo sieltä tai luo lopulliset versiot READMEta varten jos näitä käytetään
  - [ ] toisiko Obsidianin Graph View - kuva lähteiden riippuvuuksista lisäarvoa? 
  - [ ] entä markmap esitys? Kuva postauksen ideoissa

## B. Julkaisu Zenodoon
Valmis, kun paperilla on DOI. Päätetty 31.10.: Zenodo (ei lehteä; Preprints.org hylätty seulonnan epävarmuuden vuoksi).

- [ ] Seuraava vaihe on `docs/pdf-export-notes.md`:n kuusivaiheinen lista: 
  - [ ] Renderöi `figures/fig1-timeline.mmd` ja `figures/fig2-morphology-pipeline.mmd` Mermaid Livessä SVG:ksi. Katso kuvan 2 solmut K ja L: niiden tekstit pitenivät tänään, ja laatikot voivat levitä.
  - [ ] aja `python -I scripts/export.py --write` 
  - [ ] tee PDF selaimesta, taustagrafiikat päällä ja ylä- ja alatunnisteet pois.

### B0. Ulkopuolinen itsearviointi ennen vientiä — **luovuttu 20.11.2026**
Open ScholarPeeriä ei kokeilla. Ulkopuolinen arviointi hoidetaan A4:n toisen mallin tarkistuksella (`docs/ai-review-brief.md` + `main.md`), joka antaa tekstitason kritiikin ilman asennusta. Perustelu kirjattu lokiin 20.11.2026. Jos kattavuus alkaa epäilyttää ennen vientiä, päätös on avattavissa — mutta silloin ennen B1:tä, koska uusi lähde tarkoittaa ingestiä, uusia väitteitä ja grindausta.

### B1. Vienti (ks. docs/pdf-export-notes.md, "Revised export plan": HTML on pohja, PDF HTML:stä selaimen tulostuksella)
- [ ] Mermaid-kaaviot (2 kpl) SVG-kuviksi mermaid-liven kautta, upotus kuvina alt-teksteineen (nyt versioimaton unpkg-CDN). **Työkalut valmiina 20.11.2026** (`docs/pdf-export-notes.md`, "Figure workflow"): `figures/*.mmd` on jo irrotettu, enää puuttuu Mermaid Live -renderöinti nimillä `figures/fig1-timeline.svg` ja `figures/fig2-morphology-pipeline.svg`; sen jälkeen `python -I scripts/figures.py --export` ja vienti tiedostosta `main-export.md`. check.py varoittaa kunnes kuvat ovat olemassa
- [x] HTML: näkyvä otsikkolohko, URL:ien linkitys ja HTML-kommenttien poisto — **koneellistettu 20.11.2026** `scripts/export.py --write`:iin (otsikkolohko front matterista, 31 URL:ia linkitetty, kommentit pois; main.md pysyy siistinä). main.md:ssä ei ollut enää yhtään HTML-kommenttia
- [ ] Rakennus ja tarkistukset: `docs/pdf-export-notes.md`, "Build checklist" (6 askelta + tarkistuslista). Print-CSS valmiina: `docs/print.css` (`break-inside: avoid` kuville ja taulukoille, hanging indent lähdeluetteloon, taulukot 8,5 pt). **Ylätunnisteita ei poisteta CSS:llä** — selaimen tulostusvalinnasta "Headers and footers" pois

### B2. Zenodo-tietue
- [ ] Oma tietue omalla DOI:lla, tyyppi Publication → Preprint (ei uusi versio Mäki 2023 -tietueesta)
- [ ] Tiedostot: PDF pääasiallisena, HTML lisätiedostona (tarkista Zenodon HTML-käsittely)
- [ ] Metatiedot: CC BY 4.0; ei rahoitusta (harrasteprojekti); avainsanat; tekijä "Antti-Juhana Mäki, Independent researcher"; ORCID; päivämäärä ja versio
- [ ] Related identifiers: "references" → Mäki 2023 (10.5281/zenodo.20807245); "is supplemented by" → GitHub-repo (tai repon Zenodo-snapshot GitHub-releasen kautta)
- [ ] **Arkistoi repon tilannevedos Zenodoon** (GitHub-release → Zenodon GitHub-integraatio) samassa yhteydessä kuin preprint, ja käytä sen DOI:ta yllä olevassa "is supplemented by" -kohdassa GitHub-URL:n sijaan tai rinnalla. Perustelu (21.11.2026): Scope vetoaa hakukirjaukseen todisteena ja nimeää nyt tiedoston `docs/maturation-mea-search.md`, ja Declarations linkittää GitHubiin, joka on muuttuva — repo voi siirtyä, muuttua tai kadota, mutta preprint jää. Snapshot antaa version, joka vastaa julkaistua tekstiä. Tämä koskee myös Highlightsin riviä "A PubMed search found no MEA-derived reference values for hiPSC-CM maturation", joka nojaa samaan kirjaukseen
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
  - [ ] wikin paluusuunta (14.11.): AGENTS.md Draft-askel 5 "Write back to the wiki", Lint-kohta, Tag vocabulary -konventio, `check.py`:n kaksi tarkistusta (samassa virkkeessä siteeratut mutta wikissä yhdistämättömät lähteet; tagit sanaston ulkopuolelta) ja README:n "Rule plus mechanical check" -periaate
  - [ ] valinnainen: päätöskirjaus `grill-paper`-skillin loppuun (idea Matt Pocockin `grill-with-docs`/`domain-modeling`-skilleistä): päätös, perustelu ja hylätyt vaihtoehdot lyhyinä merkintöinä esim. `docs/decisions.md`:hen, ettei päätöksiä tarvitse kaivaa lokista
- [ ] myöhemmin: Ingest- ja Lint-menettelyt omiksi skilleiksi AGENTS.md:stä (ks. AGENTS.md "Schema evolution")
  - Ohjeena Matt Pocockin `writing-for-agents` (https://github.com/mattpocock/skills/blob/main/skills/productivity/writing-for-agents/SKILL.md, MIT). Käytä silloin, kun teet Ingest- ja Lint-skillit, ja templaatin AGENTS.md:n siistimiseen, ei paperin loppusuoralla. Mitä tehdä:
    - karsi toistot: kukin sääntö yhteen paikkaan ("raw/ muuttumaton" nyt kolmessa kohdassa, `notes.md`-sääntö kahdessa)
    - korjaa otsikko "Four operations" (operaatioita on nyt seitsemän)
    - kiellot ("Never", "Do not") vain koville rajoille, muut myönteisiksi ohjeiksi
    - jokaiselle vaiheelle tarkistettava valmiin kriteeri (Finishing check on hyvä malli, Ingestistä se puuttuu)
    - siirretyille osille lyhyet osoittimet, laukaisusana ensin ("When ingesting, read …")

#### Valinnaisia muita Matt Pocockin skillejä (https://github.com/mattpocock/skills, MIT)
- `handoff`: tiivistää pitkän keskustelun dokumentiksi, jolla uusi keskustelu jatkaa (hyödyllinen pitkissä istunnoissa)
- `retro`: ehdottaa istunnon jälkeen parannuksia agentin ympäristöön (vrt. 11.11. hook ja estosäännöt)
- `research`: tutkii kysymyksen primäärilähteistä ja tallentaa lähdeviitteellisen markdownin; lähellä Queryä ja kirjallisuushakua, oma prosessi tiukempi

## D. Postaukset (kotisivun blogi kattava ensin, LinkedIn lyhyt sen jälkeen)
Sisältö ja ideat `docs\private\llm-wiki-post` Luonnostelu rinnakkain, julkaisu vasta B:n jälkeen (tarvitsee linkin).
- [ ] Blogipostaus ensin `2026-11-10-llm-wiki-and-academic-review.md`
  - [ ] tarkista, että `/grinding` skills mainittu
  - [ ] kuinka otettu toteutusideologiaa tästä https://claude.com/resources/articles/building-agents-when-to-fold-subagents-into-your-main-agent-loop
  - [ ] **pääviesti: wikin ylläpito on se osa, joka unohtuu.** Karpathyn gistin kaksi kohtaa ("The synthesis already reflects everything you've read" ja "I browse the results in real time — following links, checking the graph view, reading the updated pages") — jälkimmäinen on se, mikä tekee edellisestä totta. Näyttö tästä reposta: keksityt lähteet (Galli 2024 ei ole olemassa, Dunham/Hwang tekijälistat, Blinova 2025), 199 väitteen läpikäynti lähde kerrallaan ja 35 omaa päätelmää erikseen kirjattuna. README:ssä nyt osio "The work that is easy to skip: keeping the wiki honest" — käytä sitä runkona
- [ ] LinkedIn-postaus blogin jälkeen `docs\private\llm-wiki-post\linkedin_draft.md`: viittaa repoon, Zenodoon ja blogiin
  - [ ] tarkista, että `/grinding` skills mainittu
