# ToDo (päivitetty 22.11.2026)
<!-- temp file that will be deleted -->
Järjestys: **A → B → C -> D.** D-luonnostelu ei odota mitään. Tehdyt kohdat poistetaan (git-historia säilyttää ne).

## A. Paperin sisältö ja säännöt
Lähdetarkistus, lyhenteet ja kahden ulkopuolisen mallin arviointi (ChatGPT ja NotebookLM/Gemini) on tehty; jäljellä:

- [x] Rastita Fetterman (1) `docs/claims-by-source.md`:ssä (kuvan 1 label muotoiltu 22.11. uudelleen ylivuodon takia) ja katso uusi `figures/fig1-timeline.svg`
- Päätetty 22.11.: kaksi highlightia saa ylittää 85 merkkiä (87 ja 88); `check.py` näyttää ne INFO-rivinä

**Vinkit, jos main.md vielä muuttuu:**
- Clauden tarkistusraportti yhdestä lähteestä (ei muuta mitään): `/grinding Correia`
- Kuivaharjoitus yhdelle lähteelle: `python -I scripts/claim_quotes.py --only Correia`
- Isompi päätös (esim. poistetaanko väite)? `/grill-paper`
- Hook ajaa main.md:n muokkauksen jälkeen `check_abbreviations.py`:n, `check.py`:n ja `claim_quotes.py --check`:n; lue Notes

## A5. Valinnaisia muualle kuin main.md tiedostoon
- [ ] `README.md`:n kuvat (kuvat siirretty postauksen alle; tuo sieltä tai luo lopulliset versiot, jos käytetään)
  - [ ] toisiko Obsidianin Graph View -kuva lähteiden riippuvuuksista lisäarvoa?
  - [ ] entä markmap-esitys? Kuva postauksen ideoissa
    - **Ongelma (mitattu 21.11.2026):** `main.md`:n markmap toimii vain `foldLevel: 1`:llä. Tasolla 2 markmap 0.3 tekee solmun jokaisesta listakohdasta (kappaleista ei), eli kuvaan tulee 40 listasolmua: Conclusion 4 kpl (pisin **1304 merkkiä**, ka 960), Limitations 7 kpl (628 / 320), Abstract 4 kpl (141 / 128), Abbreviations 15 kpl, Highlights 7 kpl. `wrapWidth: 300` muuttaa tuhannen merkin solmun kymmenen rivin palstaksi — siksi kuva hajoaa. Otsikon pituus ei ole syy.
    - **Ratkaisu: erillinen `docs/paper-outline.md`**, jossa on vain otsikkopuu ja lyhyt otsikko. Markmap näyttää silloin rakenteen (Literature review'n 7 alalukua, Discussionin 2) ilman listakohinaa, eikä paperin lähdetiedostoon tule esitysasiaa.
      - [ ] `scripts/outline.py`: lue `main.md`:n `#`- ja `##`-otsikot (ohita front matter ja `# References`, sama logiikka kuin `claim_quotes.py`:n `main_sentences`), kirjoita `docs/paper-outline.md`: front matter (lyhyt `title`, `markmap: foldLevel/theme/wrapWidth`) ja otsikot sellaisinaan, ei listoja
      - [ ] pidä ajan tasalla samalla tavalla kuin kuvat: tallenna otsikkopuun hash, ja anna `check.py`:n varoittaa kun `main.md`:n otsikot ovat muuttuneet mutta jäsennystä ei ole ajettu uudelleen (`figures.py`/`figures.json` on valmis malli)
      - [ ] renderöi kuva vasta kun paperin otsikot ovat lukossa (otsikko vaihtui 21.11., Discussion sai 2 alalukua)
    - **Hylätty vaihtoehto:** `foldLevel: 2` + `<!-- markmap: fold -->` -direktiivit. Asennettu markmap-vscode 0.3.1 tunnistaa `fold`- ja `foldAll`-direktiivit (varmistettu laajennuksen koodista), mutta direktiivi tarvittaisiin viiteen osioon, ja rivi `# Highlights <!-- markmap: fold -->` rikkoisi `check_abbreviations.py`:n: sen `section()` vaatii otsikkorivin päättyvän otsikkoon, joten Highlights ei enää rajautuisi pois lyhennetarkistuksesta ja APD90, FPD ja MEA alkaisivat varoittaa. Korjattavissa yhden rivin muutoksella skriptiin, mutta hinta on esitysasiaa paperin lähdekoodissa

## B. Julkaisu Zenodoon
Valmis, kun paperilla on DOI. Päätetty 31.10.: Zenodo (ei lehteä; Preprints.org hylätty seulonnan epävarmuuden vuoksi). Ulkopuolisesta itsearviointityökalusta (Open ScholarPeer) luovuttiin 20.11. (perustelu lokissa); jos kattavuus alkaa epäilyttää, päätös on avattava ennen B1:tä, koska uusi lähde tarkoittaa ingestiä, uusia väitteitä ja grindausta.

### B1. Vienti (ks. `docs/pdf-export-notes.md`: "Figure workflow" ja "Build checklist"; HTML on pohja, PDF HTML:stä selaimen tulostuksella)
Kuvat on renderöity 22.11. (`python -I scripts/figures.py --render`), ja otsikkolohko, URL:ien linkitys ja kommenttien poisto on koneellistettu `export.py`:hin. Jäljellä:
- [ ] aja `python -I scripts/export.py --write` (tekee `main-export.md`:n, josta HTML ja PDF tehdään)
- [ ] Rakennus ja tarkistukset: `docs/pdf-export-notes.md`, "Build checklist" (6 askelta + tarkistuslista). Print-CSS valmiina: `docs/print.css` (`break-inside: avoid` kuville ja taulukoille, hanging indent lähdeluetteloon, taulukot 8,5 pt)
- [ ] tee PDF selaimesta, taustagrafiikat päällä; ylä- ja alatunnisteet pois selaimen tulostusvalinnasta (CSS ei poista niitä)
- [ ] leimaa `wiki/index.md`:n "Last updated" viennin päivälle

### B2. Zenodo-tietue
- [ ] Oma tietue omalla DOI:lla, tyyppi Publication → Preprint (ei uusi versio Mäki 2023 -tietueesta)
- [ ] Tiedostot: PDF pääasiallisena, HTML lisätiedostona (tarkista Zenodon HTML-käsittely)
- [ ] Metatiedot: CC BY 4.0; ei rahoitusta (harrasteprojekti); avainsanat; tekijä "Antti-Juhana Mäki, D.Sc. (Tech.), Independent researcher"; ORCID; päivämäärä ja versio
- [ ] Related identifiers: "references" → Mäki 2023 (10.5281/zenodo.20807245); "is supplemented by" → GitHub-repo (tai repon Zenodo-snapshot GitHub-releasen kautta)
- [ ] **Arkistoi repon tilannevedos Zenodoon** (GitHub-release → Zenodon GitHub-integraatio) samassa yhteydessä kuin preprint, ja käytä sen DOI:ta yllä olevassa "is supplemented by" -kohdassa GitHub-URL:n sijaan tai rinnalla. Perustelu (21.11.2026): Scope vetoaa hakukirjaukseen todisteena ja nimeää tiedoston `docs/maturation-mea-search.md`, ja Declarations linkittää GitHubiin, joka on muuttuva — repo voi siirtyä, muuttua tai kadota, mutta preprint jää. Snapshot antaa version, joka vastaa julkaistua tekstiä. Tämä koskee myös Highlightsin riviä "A PubMed search found no MEA-derived reference values for hiPSC-CM maturation", joka nojaa samaan kirjaukseen
- [ ] Zenodo Communities: etsi sopiva yhteisö (kardiologia, kantasolut, avoin tiede); liittäminen vaatii ylläpitäjän hyväksynnän

## C. Repot

### C1. Tämä repo (julkaisun jälkeen)
- [ ] README.md:n alkuun: "The paper is in main.md and published in <Zenodo-linkki>"
- [ ] README: linkki https://github.com/AnaHill/llm-wiki-academic-template ja omaan blogipostaukseen
- [ ] Tag tai GitHub-release julkaistusta versiosta
- [ ] Poista tämä ToDo.md

### C2. llm-wiki-academic-template
- [ ] Siirrä templaattiin 1.11. jälkeen tähän repoon tulleet hyödylliset asiat (1.11. asti tehty, mm. `scripts/check_abbreviations.py`). `docs/lessons.md` kertoo, mikä muutos syntyi mistäkin virheestä:
  - [ ] `/grinding`-skill
  - [ ] `.claude/settings.json` (deny `notes.md`, ask `raw/**`, PostToolUse-hook) ja `scripts/hooks/main_md_checks.py` (sis. `claim_quotes.py --check`)
  - [ ] `scripts/claim_quotes.py`: `--write`, `--only`, `--check`, otsikoiden ✅-merkinnät, `{q:}`-regexit, ei tallennettuja rivinumeroita, ilmoitus kartoittamattomasta otsikosta (`SECTION_TAG`), sukunimestä johdetut `SOURCES`-kuviot ja rekisterin lainausten tarkistus
  - [ ] `scripts/check.py`: Support-sanaston tarkistus, kuvien hash-tarkistus, ensimmäinen kirjoittaja, tuplanumerot, highlightien pituus, lokin koko ja arkistot, lessons-evidenssi
  - [ ] `scripts/rotate_log.py` (lokin jako arkistoihin)
  - [ ] `scripts/figures.py` (`--write`, `--render`), `scripts/export.py` ja `docs/print.css`: vienti generoidusta kopiosta, main.md pysyy lähteenä
  - [ ] AGENTS.md: "Register of the author's own inferences" ja Support-arvot; "Figures stay as Mermaid in main.md"; vuosisääntö; "Decisions go in the log"
  - [ ] `docs/lessons.md` -malli (teemat, Evidence/Changed/Status)
  - [ ] `docs/ai-review-brief.md` (ohje ulkopuoliselle AI-arvioijalle) yleistettynä
  - [ ] `docs/private/` (git-ignored, yksityiset luonnokset) ja sen maininta AGENTS.md:ssä
  - [ ] täydennysaineistojen nimeäminen myös muille kuin PDF:ille (`<stem>-supplementary.docx`), ja .docx-kuvien purku `figure_analysis/`-kansioon tarkastelua varten
  - [ ] wikin paluusuunta: AGENTS.md Draft-askel 5 "Write back to the wiki", Lint-kohta, Tag vocabulary -konventio, `check.py`:n kaksi tarkistusta (samassa virkkeessä siteeratut mutta wikissä yhdistämättömät lähteet; tagit sanaston ulkopuolelta) ja README:n "Rule plus mechanical check" -periaate
  - [ ] valinnainen: päätöskirjaus `grill-paper`-skillin loppuun (idea Matt Pocockin `grill-with-docs`/`domain-modeling`-skilleistä): päätös, perustelu ja hylätyt vaihtoehdot lyhyinä merkintöinä esim. `docs/decisions.md`:hen, ettei päätöksiä tarvitse kaivaa lokista
- [ ] myöhemmin: Ingest- ja Lint-menettelyt omiksi skilleiksi AGENTS.md:stä (ks. AGENTS.md "Schema evolution")
  - Ingest-skillin tarkistuslista lokin perusteella: kuvien katsominen, liitteiden lukeminen, kirjoittajajärjestys PDF:n sivulta 1, vuosisääntö, lähteen omien ristiriitojen kirjaaminen, `SOURCES`-kuvio samannimisille
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
Sisältö ja ideat `docs\private\llm-wiki-post`. Luonnostelu rinnakkain, julkaisu vasta B:n jälkeen (tarvitsee linkin). Luvut pyöristetään ("yli 200 väitettä", "yli 30 lähdettä", "lähes 40 omaa päätelmää"), kun tarkka arvo ei ole oleellinen.
- [ ] Blogipostaus ensin `2026-11-10-llm-wiki-and-academic-review.md`
  - [ ] **pääviesti: wikin ylläpito on se osa, joka unohtuu.** Karpathyn gistin kaksi kohtaa ("The synthesis already reflects everything you've read" ja "I browse the results in real time — following links, checking the graph view, reading the updated pages") — jälkimmäinen on se, mikä tekee edellisestä totta. Näyttö tästä reposta: keksityt lähteet (Galli 2024 ei ole olemassa, Dunham/Hwang tekijälistat, Blinova 2025), yli 200 väitteen läpikäynti lähde kerrallaan ja lähes 40 omaa päätelmää erikseen kirjattuna. README:ssä osio "The work that is easy to skip: keeping the wiki honest" — käytä sitä runkona
  - [ ] tarkista blogin `[CLAUDE 22.11.]`-merkityt kohdat (11 kpl) ja poista merkinnät
  - [ ] blogin muut TODO-kommentit (mm. Markmap-kuva, työnkulkukaavio, uusi graafikuva, käännöksen tarkistus, Zenodo-DOI)
  - [ ] postaus on noin 6 700 sanaa; lyhennysehdokkaat "Co-writing without git skills" (kokeilematon idea) ja "Where the paper is published"
- [ ] LinkedIn-postaus blogin jälkeen `docs\private\llm-wiki-post\linkedin_draft.md`: viittaa repoon, Zenodoon ja blogiin
  - [ ] tarkista, että `/grinding` skills mainittu
  - [ ] valitse avaus A tai B ja mahdollinen bulletinvaihto (vaihtoehdot `linkedin_draft.md`:ssä, "Vaihtoehtoja versioon E")
