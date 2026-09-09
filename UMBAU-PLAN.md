# Umbau-Plan: von der Scientifica-Station zur allgemeinen OGD-Webseite

**Stand:** 2026-09-09 · **Repo:** `ssz_odz_entdecken` · **Quelle:** `ssz_odz_scientifica` (Commit `81d566d`)

## 1. Vorhaben

Die für die [Scientifica 2026](https://scientifica.ch) gebaute OGD-Station wird zu einer
dauerhaft nutzbaren, event-unabhängigen Webseite umgebaut. Sie soll Interessierten auch
ausserhalb eines betreuten Anlasses zeigen, was mit den offenen Daten der Stadt Zürich
möglich ist — auffindbar, selbsterklärend und auf allen Geräten benutzbar.

**Einsatzzwecke nach dem Umbau:** Verlinkung von `stadt-zuerich.ch/opendata`, Workshops und
Schulungen, Hackathons, Schulen/Hochschulen — und weiterhin der Kiosk-Betrieb an Messen und
Anlässen (dann als bewusst aktivierter Modus, siehe Phase 2).

### Ausgangslage

Die inhaltliche Substanz ist bereits event-neutral: keine einzige Formulierung wie «hier am
Stand» oder «an dieser Station» in den vier Themenseiten. Der Scientifica-Bezug steckt
ausschliesslich in **Titel, Keyvisual, Kiosk-Logik und Stations-Nummerierung**. Der Umbau ist
darum überschaubar; der grösste technische Posten ist das fehlende Responsive-Layout.

### Entscheide

| Frage | Entscheid | Begründung |
|---|---|---|
| Neues Repo oder Branch? | **Neues Repo** (`ssz_odz_entdecken`) | Scientifica-Repo bleibt als Event-Archiv eingefroren; die Versionen driften auseinander (Kiosk vs. offenes Web) |
| Haupttitel (H1) | **«Open Government Data entdecken»** | Zeitlos, kein Jahr/Event, beschreibt die vier Themen, passt in die Header-Breite |
| Untertitel | Bleiben seitenspezifisch wie bisher | Sind bereits event-neutral formuliert |
| Kiosk-Modus | Bleibt erhalten, aber **opt-in via `?kiosk=1`** | Wiederverwendbar für den nächsten Anlass, ohne die normale Webseite zu stören |

---

## 2. Phasen

### Phase 0 — Setup ✅ erledigt

- [x] Kopie nach `G:\sszsim\1_github_odz\ssz_odz_entdecken` (ohne `.git`)
- [x] Neues Git-Repo initialisiert, Branch `main`
- [x] Baseline-Commit als 1:1-Kopie des Ausgangsstands
- [x] Dieses Dokument

> **Hinweis zur History:** Der Baseline-Commit enthält noch die Scientifica-/ETH-Bilddateien
> (~8 MB). Sie werden in Phase 1 gelöscht, bleiben aber in der Git-History. Da dieselben
> Dateien bereits im öffentlichen Repo `opendatazurich/ssz_odz_scientifica` liegen, entsteht
> dadurch keine neue Exposition. Wer eine saubere History will, squasht die ersten beiden
> Commits vor dem ersten Push.

### Phase 1 — Branding und Titel

Betrifft alle 5 HTML-Seiten.

- [ ] `<h1>` ersetzen: `Scientifica 2026: Open Government Data` → `Open Government Data entdecken`
      — `index.html:197`, `katalog/index.html:115`, `starter-code/index.html:348`,
      `mcp-abfragen/index.html:164`, `anwendungen/index.html:22`
- [ ] `<title>` ersetzen (jeweils Zeile 6), Schema: `Open Government Data entdecken — <Seitenthema>`
- [ ] `<img class="header-eye">` aus allen 5 Seiten entfernen (`index.html:195`,
      `katalog:113`, `starter-code:346`, `mcp-abfragen:162`, `anwendungen:20`)
- [ ] `.header-eye`-Regel aus `shared/style.css` entfernen
- [ ] Header-Layout ohne Auge neu ausbalancieren (Titel und OGD-Sticker)
- [ ] Bilddateien löschen: `shared/eth_Auge1_transparent.png`, `shared/eth_Auge1_CMYK_100Prozent.jpg`,
      `shared/Scientifica_Auge_Einzel.png`, `shared/Scientifica_Augen_Keyvisual.jpg`,
      `shared/scientifica_wide.jpg` (~8 MB)

> **Rechtlich:** Das ETH-/Scientifica-Keyvisual (Auge) ist an das Event gebunden und darf
> ausserhalb davon nicht weiterverwendet werden. Diese Dateien müssen weg — das ist kein
> optionaler Schönheitsschritt.

### Phase 2 — Kiosk-Logik entschärfen

- [ ] `shared/kiosk.js`: Overlay-Logik nur starten, wenn `?kiosk=1` in der URL steht
- [ ] `shared/kiosk.js` auf allen Seiten einbinden — aktuell fehlt das Script auf `index.html`
      (Inkonsistenz aus dem Ausgangsstand)
- [ ] `body { user-select: none }` in `shared/style.css:22` entfernen; die Ausnahme für
      `pre, code` wird damit hinfällig
- [ ] Reset-Overlay-Markup in den 4 Themenseiten belassen (`katalog:262`, `anwendungen:102`,
      `mcp-abfragen:278`, `starter-code:679`) — es ist ohne aktiven Kiosk-Modus unsichtbar

### Phase 3 — Startseite entrümpeln (`index.html`)

- [ ] «Station 1»–«Station 4» entfernen bzw. durch Themenlabels ersetzen (`.station-number`)
- [ ] Skill-Badges «Einstieg / Erkunden / Vertiefen» **behalten** — sie sind generisch und
      ohne Event-Rundgang sogar wertvoller als vorher
- [ ] Kachel-Reihenfolge an die Navigation angleichen (aktuell Rundgang-Logik:
      Anwendungen zuerst)
- [ ] Viewport-Fixierung lösen: `min-height: 360px`, `flex: 1` und das feste 2×2-Raster
      dürfen scrollen (bisher bewusst nicht)
- [ ] CSS-Klassen umbenennen: `.station-*` → `.topic-*` (optional, kosmetisch)

### Phase 4 — Responsive Layout

Grösster technischer Posten: Im gesamten Projekt existiert **keine einzige `@media`-Regel**.
Die Seite ist hart auf die Event-Laptops optimiert (1920×1200 bei 150 % = 1280×800 CSS-Pixel).

- [ ] Breakpoints in `shared/style.css` definieren (Vorschlag: 1024px / 768px / 480px)
- [ ] Kachelraster 2×2 → 1 Spalte auf Mobile
- [ ] `main`/`nav`/`header`/`footer`-Padding von fixen `3rem` auf flexible Werte
- [ ] Schriftgrössen und Header-Höhe skalieren
- [ ] Navigation auf schmalen Bildschirmen prüfen (scrollt aktuell horizontal — akzeptabel,
      aber testen)
- [ ] `mcp-abfragen/index.html`: die JS-Höhenangleichung der Karten muss bei `resize`
      neu rechnen und auf Mobile deaktiviert werden
- [ ] `starter-code/index.html`: das links gefloatete Video auf Mobile über den Text stellen
- [ ] Test auf Mobile, Tablet, Desktop

### Phase 5 — Inhalte für den Standalone-Betrieb

An der Scientifica erklärte Standpersonal die Station. Im Web muss die Seite das selbst tun.

- [ ] Abschnitt «Über diese Seite» auf `index.html`: 2–3 Sätze, was OGD ist und was man
      hier findet
- [ ] Footer erweitern: Impressum- und Datenschutz-Link (für eine öffentliche
      Stadt-Zürich-Seite erforderlich)
- [ ] Kontakt/Feedback: `opendata@stadt-zuerich.ch`
- [ ] Lizenzhinweis (CC BY) und «Stand: <Datum>»
- [ ] Prüfen, ob ein Hinweis auf den OGD-Newsletter sinnvoll ist

### Phase 6 — Aufräumen und Dokumentation

- [ ] `anwendungen/index.html`: 2 Links enthalten hartkodiert `anwendungen-2026` — auf eine
      jahresunabhängige URL umstellen oder als Wartungspunkt dokumentieren
- [ ] `README.md` neu schreiben (aktuell vollständig Scientifica-bezogen)
- [ ] `CLAUDE.md` neu schreiben (dito; liegt in `.gitignore`, also nur lokal)
- [ ] `farbskalen.html` bleibt als internes Arbeitsdokument liegen — steht bereits
      in `.gitignore` und wird nicht publiziert
- [ ] `shared/starterCode.mp4` (1.8 MB) funktioniert nur über HTTP, nicht via `file:///` —
      unter GitHub Pages unproblematisch, aber nach dem Deployment verifizieren
- [ ] Alle externen Links durchklicken

### Phase 7 — Veröffentlichung

- [ ] GitHub-Repo unter `opendatazurich/` anlegen und Remote setzen
- [ ] GitHub Pages aktivieren
- [ ] Verlinkung ab `stadt-zuerich.ch/opendata` mit STEZ/Kommunikation absprechen
- [ ] Vorschaubild und Meta-Tags (`og:title`, `og:description`, `og:image`) ergänzen —
      fehlen bisher komplett, relevant sobald der Link geteilt wird

---

## 3. Was bewusst nicht angefasst wird

Die vier Themenseiten bleiben **inhaltlich unverändert**. Katalog, Starter Code,
MCP-Abfragen und Anwendungen sind bereits vollständig event-neutral geschrieben. Angefasst
werden dort nur Header, Titel und das Responsive-Verhalten.

Ebenfalls unverändert bleiben:

- Farbpalette und CI/CD der Stadt Zürich (`--blue: #0F05A0`, `--accent: #009ee0`)
- Der Ansatz «rein statisches HTML/CSS/JS ohne Build-System»
- Navigationsstruktur: Übersicht / Daten erleben / Daten finden / Daten abfragen / Daten nutzen

## 4. Offene Punkte

- Mehrsprachigkeit (FR/EN/IT)? Aktuell nur Deutsch, `lang="de"`. Falls je gewünscht, sollte
  die Struktur jetzt darauf vorbereitet werden statt später.
- Soll die Seite eine eigene Domain/Subdomain bekommen oder unter `opendatazurich.github.io`
  laufen?
- Wer pflegt die Seite laufend (Anwendungen und MCP-Server ändern sich)?
