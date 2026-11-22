# ToDo (päivitetty 22.11.2026)
<!-- temp file that will be deleted -->
Järjestys: **A → B → C -> D.** D-luonnostelu ei odota mitään. Tehdyt kohdat poistetaan (git-historia säilyttää ne; A1–A4 poistettu 22.11.).

## A. Paperin sisältö (main.md ja tukitiedostot)
Valmis, kun teksti on lukittu ja jokainen väite on tarkistettu lähdettä vasten. Lähdetarkistus (A2), lyhenteet (A3) ja lopputarkistukset kahdella ulkopuolisella mallilla (A4: ChatGPT ja NotebookLM/Gemini) on tehty; kohdat poistettu 22.11.

- [ ] Rastita Weiser-Bitoun (9) `docs/claims-by-source.md`:ssä (lisätty 22.11. Motivationiin: kehittäjien suositus standardoida piikkien tunnistus ja biomarkkerien laskenta, Discussion 4.2, s. 11). Rastin jälkeen `python -I scripts/claim_quotes.py --write` palauttaa otsikon ✅:n
- [ ] Kuvan 1 teksti "Functional/metabolic/transcriptional" valuu laatikon yli renderöidyssä SVG:ssä (22.11.). Korjaus vaatii tekstimuutoksen `main.md`:n Mermaid-lohkoon; sen jälkeen `figures.py --write`, renderöinti uudelleen ja `claim_quotes.py --write` (Timeline-väite lainaa tätä riviä)
- Päätetty 22.11.: kaksi highlightia saa ylittää 85 merkkiä (87 ja 88); `check.py` näyttää ne INFO-rivinä

**Vinkit, jos main.md vielä muuttuu:**
- Clauden tarkistusraportti yhdestä lähteestä (ei muuta mitään): `/grinding Correia`
- Kuivaharjoitus yhdelle lähteelle: `python -I scripts/claim_quotes.py --only Correia`
- Isompi päätös (esim. poistetaanko väite)? `/grill-paper`
- Hook ajaa main.md:n muokkauksen jälkeen `check_abbreviations.py`:n, `check.py`:n ja `claim_quotes.py --check`:n; lue Notes

## A5. Valinnaisia muualle kuin main.md tiedostoon
- [ ] `README.md` päivityksiä
  - [x] kuvat siirretty postauksen alla. Tuo sieltä tai luo lopulliset versiot READMEta varten jos näitä käytetään
  - [ ] toisiko Obsidianin Graph View - kuva lähteiden riippuvuuksista lisäarvoa? 
  - [ ] entä markmap esitys? Kuva postauksen ideoissa
    - **Ongelma (mitattu 21.11.2026):** `main.md`:n markmap toimii vain `foldLevel: 1`:llä. Tasolla 2 markmap 0.3 tekee solmun jokaisesta listakohdasta (kappaleista ei), eli kuvaan tulee 40 listasolmua: Conclusion 4 kpl (pisin **1304 merkkiä**, ka 960), Limitations 7 kpl (628 / 320), Abstract 4 kpl (141 / 128), Abbreviations 15 kpl, Highlights 7 kpl. `wrapWidth: 300` muuttaa tuhannen merkin solmun kymmenen rivin palstaksi — siksi kuva hajoaa. Otsikon pituus ei ole syy.
    - **Ratkaisu: erillinen `docs/paper-outline.md`**, jossa on vain otsikkopuu ja lyhyt otsikko. Markmap näyttää silloin rakenteen (Literature review'n 7 alalukua, Discussionin 2) ilman listakohinaa, eikä paperin lähdetiedostoon tule esitysasiaa.
      - [ ] `scripts/outline.py`: lue `main.md`:n `#`- ja `##`-otsikot (ohita front matter ja `# References`, sama logiikka kuin `claim_quotes.py`:n `main_sentences`), kirjoita `docs/paper-outline.md`: front matter (lyhyt `title`, `markmap: foldLevel/theme/wrapWidth`) ja otsikot sellaisinaan, ei listoja
      - [ ] pidä ajan tasalla samalla tavalla kuin kuvat: tallenna otsikkopuun hash, ja anna `check.py`:n varoittaa kun `main.md`:n otsikot ovat muuttuneet mutta jäsennystä ei ole ajettu uudelleen (`figures.py`/`figures.json` on valmis malli)
      - [ ] renderöi kuva vasta kun paperin otsikot ovat lukossa (otsikko vaihtui 21.11., Discussion sai 2 alalukua)
    - **Hylätty vaihtoehto:** `foldLevel: 2` + `<!-- markmap: fold -->` -direktiivit. Asennettu markmap-vscode 0.3.1 tunnistaa `fold`- ja `foldAll`-direktiivit (varmistettu laajennuksen koodista), mutta direktiivi tarvittaisiin viiteen osioon, ja rivi `# Highlights <!-- markmap: fold -->` rikkoisi `check_abbreviations.py`:n: sen `section()` vaatii otsikkorivin päättyvän otsikkoon, joten Highlights ei enää rajautuisi pois lyhennetarkistuksesta ja APD90, FPD ja MEA alkaisivat varoittaa. Korjattavissa yhden rivin muutoksella skriptiin, mutta hinta on esitysasiaa paperin lähdekoodissa

## A6. Työkalut ja säännöt ennen vientiä (lokin läpikäynti 22.11.)
- [x] Vaihe 1: vanhentuneet luvut ja tiedot (README pyöristetty; blogi ja LinkedIn)
- [x] Vaihe 2: `check.py`:hin ensimmäinen kirjoittaja, tuplanumerot ja highlightien pituus; hookiin `claim_quotes.py --check`
- [ ] Vaihe 3: rekisterin kohtiin generoidut lainaukset (`{q:}`), jotta highlightien, abstraktin ja otsikon muutos näkyy diffissä (virhetyyppi D: tiivistelmä jää jälkeen leipätekstistä). Kertaluonteinen iso diffi claims-tiedostoon, oma commit
- [ ] Vaihe 4: säännöt ja loki
  - [ ] AGENTS.md: vuosisääntö (issue year, ei online-first; päätetty kolmesti: Botti, Park 2026, Weiser-Bitoun)
  - [ ] AGENTS.md: päätökset kirjataan lokiin, ei ToDo:hon (ToDo poistetaan julkaisussa)
  - [ ] grinding-skill: muutoksen jälkeen lue rekisterin kohta 0, abstrakti ja otsikko
  - [ ] loki: kesä–lokakuu arkistoon omaan tiedostoonsa (loki on noin 100 000 tokenia, ei mahdu yhteen lukuun); otsakkeen formaattilistaan `grill`
  - [ ] valinnainen: `docs/lessons.md`, lokista poimitut opit (pohja blogille ja templaatille)
- [x] Vaihe 5: Weiser-Bitoun p. 11 Motivationiin (22.11.; rastitus kohdassa A)

## B. Julkaisu Zenodoon
Valmis, kun paperilla on DOI. Päätetty 31.10.: Zenodo (ei lehteä; Preprints.org hylätty seulonnan epävarmuuden vuoksi).

### B0. Ulkopuolinen itsearviointi ennen vientiä — **luovuttu 20.11.2026**
Open ScholarPeeriä ei kokeilla. Ulkopuolinen arviointi tehtiin kahdella mallilla (ChatGPT ja NotebookLM/Gemini; `docs/ai-review-brief.md` + `main.md`). Perustelu kirjattu lokiin 20.11.2026. Jos kattavuus alkaa epäilyttää ennen vientiä, päätös on avattavissa — mutta silloin ennen B1:tä, koska uusi lähde tarkoittaa ingestiä, uusia väitteitä ja grindausta.

### B1. Vienti (ks. `docs/pdf-export-notes.md`: "Figure workflow" ja "Build checklist"; HTML on pohja, PDF HTML:stä selaimen tulostuksella)
- [x] Kuvat SVG:ksi: **tehty 22.11.2026** komennolla `python -I scripts/figures.py --render` (Mermaid Liven vienti hylätty: tallensi esikatselun tumman teeman ja zoomauksen). Kuvan 2 solmut K ja L mahtuvat; kuvan 1 ylivuoto on kohdassa A
- [x] HTML: näkyvä otsikkolohko, URL:ien linkitys ja HTML-kommenttien poisto — koneellistettu 20.11.2026 `scripts/export.py --write`:iin
- [ ] aja `python -I scripts/export.py --write` (tekee `main-export.md`:n, josta HTML ja PDF tehdään)
- [ ] Rakennus ja tarkistukset: `docs/pdf-export-notes.md`, "Build checklist" (6 askelta + tarkistuslista). Print-CSS valmiina: `docs/print.css` (`break-inside: avoid` kuville ja taulukoille, hanging indent lähdeluetteloon, taulukot 8,5 pt)
- [ ] tee PDF selaimesta, taustagrafiikat päällä; ylä- ja alatunnisteet pois selaimen tulostusvalinnasta (CSS ei poista niitä)
- [ ] leimaa `wiki/index.md`:n "Last updated" viennin päivälle

### B2. Zenodo-tietue
- [ ] Oma tietue omalla DOI:lla, tyyppi Publication → Preprint (ei uusi versio Mäki 2023 -tietueesta)
- [ ] Tiedostot: PDF pääasiallisena, HTML lisätiedostona (tarkista Zenodon HTML-käsittely)
- [ ] Metatiedot: CC BY 4.0; ei rahoitusta (harrasteprojekti); avainsanat; tekijä "Antti-Juhana Mäki, D.Sc. (Tech.), Independent researcher"; ORCID; päivämäärä ja versio
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
  - [ ] `.claude/settings.json` (deny `notes.md`, ask `raw/**`, PostToolUse-hook) ja `scripts/hooks/main_md_checks.py` (lisätty 11.11., `claim_quotes.py --check` 22.11.)
  - [ ] `scripts/claim_quotes.py`: `--write`, `--only`, `--check`, otsikoiden ✅-merkinnät, `{q:}`-regexit, ei tallennettuja rivinumeroita (21.11.), ilmoitus kartoittamattomasta otsikosta (`SECTION_TAG`) ja sukunimestä johdetut `SOURCES`-kuviot
  - [ ] `scripts/check.py`: Support-sanaston tarkistus, kuvien hash-tarkistus, ensimmäinen kirjoittaja, tuplanumerot, highlightien pituus (22.11.)
  - [ ] `scripts/figures.py` (`--write`, `--render`), `scripts/export.py` ja `docs/print.css`: vienti generoidusta kopiosta, main.md pysyy lähteenä
  - [ ] AGENTS.md: "Register of the author's own inferences" ja Support-arvot; "Figures stay as Mermaid in main.md"
  - [ ] `docs/ai-review-brief.md` (ohje ulkopuoliselle AI-arvioijalle) yleistettynä
  - [ ] `docs/private/` (git-ignored, yksityiset luonnokset) ja sen maininta AGENTS.md:ssä
  - [ ] täydennysaineistojen nimeäminen myös muille kuin PDF:ille (`<stem>-supplementary.docx`), ja .docx-kuvien purku `figure_analysis/`-kansioon tarkastelua varten
  - [ ] wikin paluusuunta (14.11.): AGENTS.md Draft-askel 5 "Write back to the wiki", Lint-kohta, Tag vocabulary -konventio, `check.py`:n kaksi tarkistusta (samassa virkkeessä siteeratut mutta wikissä yhdistämättömät lähteet; tagit sanaston ulkopuolelta) ja README:n "Rule plus mechanical check" -periaate
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
  - [x] `/grinding` skills mainittu
  - [x] Anthropicin single-loop-artikkeli mukana (osio "One agent, thin tools, hard limits")
  - [ ] **pääviesti: wikin ylläpito on se osa, joka unohtuu.** Karpathyn gistin kaksi kohtaa ("The synthesis already reflects everything you've read" ja "I browse the results in real time — following links, checking the graph view, reading the updated pages") — jälkimmäinen on se, mikä tekee edellisestä totta. Näyttö tästä reposta: keksityt lähteet (Galli 2024 ei ole olemassa, Dunham/Hwang tekijälistat, Blinova 2025), yli 200 väitteen läpikäynti lähde kerrallaan ja lähes 40 omaa päätelmää erikseen kirjattuna. README:ssä osio "The work that is easy to skip: keeping the wiki honest" — käytä sitä runkona
  - [ ] Vaihe 6: lokista poimitut opit sopiviin osioihin: virhetyyppi D (tiivistelmä ja otsikko jäävät jälkeen leipätekstistä), luettava diff (rivinumerot olivat 91 % diffistä), työkalu joka epäonnistuu tuottamalla ei mitään, mitä läpikäynti muutti ("organoid"-sana, "two of them"), 24.10. verifioinnin tulos (kaikilla 12 sivulla lähteen ylittäviä väitteitä), kuvat ja liitteet paljastavat tekstiekstraktion ohittamaa, AI-arvioijat (abstrakti ei ole lähde; varo ylivarovaisuutta), poissaoloväite on hakunsa kokoinen, liian kova deny-sääntö → ask, lähteissäkin on virheitä, rekisteri ja Support-arvot
  - [ ] järjestys-TODO (osio "The workflow in practice") lokin aikajanalla
  - [ ] katkennut "Rem…"-kohta (TODO-kommentti blogissa)
- [ ] LinkedIn-postaus blogin jälkeen `docs\private\llm-wiki-post\linkedin_draft.md`: viittaa repoon, Zenodoon ja blogiin
  - [ ] tarkista, että `/grinding` skills mainittu
  - [ ] uusi avausvaihtoehto "The strongest claim in my paper was its title." ja mahdollisesti bulletti tiivistelmien jälkeen jäämisestä
