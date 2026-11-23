# ToDo (päivitetty 22.11.2026)
<!-- temp file that will be deleted -->
Järjestys: **A → B → C -> D.** D-luonnostelu ei odota mitään. Tehdyt kohdat poistetaan (git-historia säilyttää ne).
Pohditut mutta nyt toteuttamatta jätetyt ideat ovat tiedostossa [docs/ideas.md](docs/ideas.md) (mm. Ingest- ja Lint-skillit, päätöskirjaus `/grill-paper`-skilliin, Matt Pocockin muut skillit).

## A. Paperin sisältö ja säännöt
- Lähdetarkistus, lyhenteet ja kahden ulkopuolisen mallin arviointi ✅
- Päätetty 22.11.: highlight saa ylittää 85 merkkiä ✅; `check.py` näyttää ne INFO-rivinä

**Vinkit, jos main.md vielä muuttuu:**
- Clauden tarkistusraportti yhdestä lähteestä (ei muuta mitään): `/grinding Correia`
- Kuivaharjoitus yhdelle lähteelle: `python -I scripts/claim_quotes.py --only Correia`
- Isompi päätös (esim. poistetaanko väite)? `/grill-paper`
- Hook ajaa main.md:n muokkauksen jälkeen `check_abbreviations.py`:n, `check.py`:n ja `claim_quotes.py --check`:n; lue Notes

## B. Julkaisu Zenodoon
Valmis, kun paperilla on DOI Zenodossa ✅

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

## D. Postaukset (kotisivun blogi kattava ensin, LinkedIn lyhyt sen jälkeen)
Sisältö ja ideat `docs\private\llm-wiki-post`. Luonnostelu rinnakkain, julkaisu vasta B:n jälkeen (tarvitsee linkin). Luvut pyöristetään ("yli 200 väitettä", "yli 30 lähdettä", "lähes 40 omaa päätelmää"), kun tarkka arvo ei ole oleellinen.
- [ ] Blogipostaus ensin `2026-11-10-llm-wiki-and-academic-review.md`
  - [ ] **pääviesti: wikin ylläpito on se osa, joka unohtuu.** Karpathyn gistin kohdat kuten "The synthesis already reflects everything you've read" ja "I browse the results in real time — following links, checking the graph view, reading the updated pages" 
  - [ ] tarkista blogin `[CLAUDE 22.11.]`-merkityt kohdat (11 kpl) ja poista merkinnät
  - [ ] blogin muut TODO-kommentit (mm. työnkulkukaavio, graafikuvan kopiointi kotisivulle, käännöksen tarkistus, Zenodo-DOI)
  - [ ] postaus on noin 6 700 sanaa; lyhennysehdokkaat "Co-writing without git skills" (kokeilematon idea) ja "Where the paper is published"
- [ ] LinkedIn-postaus blogin jälkeen `docs\private\llm-wiki-post\linkedin_draft.md`: viittaa repoon, Zenodoon ja blogiin
  - [ ] tarkista, että `/grinding` skills mainittu
  - [ ] valitse avaus A tai B ja mahdollinen bulletinvaihto (vaihtoehdot `linkedin_draft.md`:ssä, "Vaihtoehtoja versioon E")
