# Umbau-Plan: von der Scientifica-Station zur allgemeinen OGD-Webseite

**Stand:** 2026-09-09 · **Repo:** `ssz_odz_entdecken` · **Quelle:** `ssz_odz_scientifica` (Commit `81d566d`)

> **Fortschritt:** Phasen 0–3 erledigt, Teile von Phase 6 vorgezogen.
> **Als Nächstes: Phase 4 (Responsive Layout)** — der grösste verbleibende Posten.

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
| Ersatz für das Scientifica-Auge | **Stadt-Zürich-Logo** (`logo_stzh_rgb_weiss_digital.svg`) | Offizielles Absenderlogo, weiss auf Züriblau, als SVG frei skalierbar |

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

### Phase 1 — Branding und Titel ✅ erledigt

Betrifft alle 5 HTML-Seiten.

- [x] `<h1>` ersetzt: `Scientifica 2026: Open Government Data` → `Open Government Data entdecken`
- [x] `<title>` ersetzt, Schema: `Open Government Data entdecken — <Seitenthema>`
- [x] `<img class="header-eye">` durch `<img class="header-logo-stzh">` mit dem
      Stadt-Zürich-Logo ersetzt
- [x] `.header-eye`-Regel in `shared/style.css` durch `.header-logo-stzh` ersetzt
- [x] Header-Layout neu ausbalanciert: Logo links und OGD-Sticker rechts erhalten dieselbe
      Flex-Basis (`170px`), damit der Titel exakt mittig steht
- [x] Logogrösse auf die Höhe des Textblocks aus Titel und Untertitel gesetzt
      (57px hoch → 240px breit; Flex-Basis beider Seiten entsprechend auf 240px).
      `header h1` hat dafür eine fixe `line-height: 1.2` bekommen, damit die
      Höhenrechnung nicht von den Schriftmetriken des Systems abhängt.
- [x] Bilddateien gelöscht: `eth_Auge1_transparent.png`, `eth_Auge1_CMYK_100Prozent.jpg`,
      `Scientifica_Auge_Einzel.png`, `Scientifica_Augen_Keyvisual.jpg`,
      `scientifica_wide.jpg` (~7.9 MB)
- [x] Geprüft: alle 5 Seiten und alle lokalen Assets liefern HTTP 200, keine toten
      Referenzen mehr auf gelöschte Dateien

> **Rechtlich:** Das ETH-/Scientifica-Keyvisual (Auge) ist an das Event gebunden und darf
> ausserhalb davon nicht weiterverwendet werden. Diese Dateien müssen weg — das ist kein
> optionaler Schönheitsschritt.

### Phase 2 — Kiosk-Logik entschärfen ✅ erledigt

- [x] `shared/kiosk.js` komplett überarbeitet: Die Logik startet nur noch, wenn `?kiosk=1`
      in der URL steht. Im Normalbetrieb passiert nichts.
- [x] Kiosk-Parameter wird beim Navigieren automatisch an interne Links weitergegeben
      (`propagateKioskParam()`) — sonst wäre der Modus nach dem ersten Klick weg.
      Externe Links, Anker und `mailto:` bleiben unangetastet.
- [x] Null-Guards ergänzt: Das Script lief bisher auf Seiten ohne Overlay-Markup auf einen
      Fehler.
- [x] `shared/kiosk.js` und Reset-Overlay auf `index.html` ergänzt — beides fehlte dort
- [x] `body { user-select: none }` entfernt; gilt jetzt nur noch unter `body.kiosk`,
      die Klasse setzt das Script im Kiosk-Modus
- [x] Reset-Overlay-Markup in allen 5 Seiten belassen — ohne aktiven Kiosk-Modus unsichtbar

**Kiosk-Betrieb neu:** `chrome.exe --kiosk --noerrdialogs "http://localhost:8080/?kiosk=1"`

### Phase 3 — Startseite entrümpeln (`index.html`) ✅ erledigt

- [x] «Station 1»–«Station 4» durch die Navigationsbezeichnungen ersetzt
      («Daten erleben», «Daten finden», «Daten abfragen», «Daten nutzen»); CSS-Klasse
      `.station-number` → `.station-topic`. Das erhält die Bildkomposition der Kachel und
      stellt zugleich den Bezug zur Navigation her.
- [x] Skill-Badges «Einstieg / Erkunden / Vertiefen» behalten
- [x] Viewport-Fixierung gelöst: `flex: 1`, `grid-template-rows` und `min-height: 360px`
      entfernt, `main`-Padding von `0.6rem` auf `2rem`, Footer-Sonderpadding entfernt
      (nutzt jetzt den gemeinsamen Stil aus `style.css`)
- [x] Kachel-Header von `85px` auf `100px` erhöht — die gequetschte Höhe war eine Folge
      der Viewport-Fixierung
- [ ] CSS-Klassen `.station-*` → `.topic-*` umbenennen (optional, rein kosmetisch; die
      Klassennamen sind der letzte verbliebene Event-Begriff im Code)

> **Korrektur zum ursprünglichen Plan:** Die Kachel-Reihenfolge musste nicht angepasst
> werden — sie entsprach bereits der Navigationsreihenfolge (Anwendungen, Katalog, MCP,
> Starter Code). Der Punkt entfällt.

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
- [x] `README.md` neu geschrieben (vorgezogen, damit der Einstieg beim Weiterarbeiten stimmt)
- [x] `CLAUDE.md` neu geschrieben (dito; liegt in `.gitignore`, also nur lokal). Die
      detaillierten Beschreibungen der vier Themenseiten sind unverändert übernommen —
      sie stimmen weiterhin.
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
