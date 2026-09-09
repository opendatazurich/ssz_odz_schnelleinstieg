# Schnelleinstieg Open Government Data — Stadt Zürich

Eine Webseite von Statistik Stadt Zürich (SSZ), die zeigt, was mit den offenen Daten der
Stadt Zürich möglich ist: bestehende Anwendungen anschauen, den Datenkatalog durchsuchen,
Daten in natürlicher Sprache abfragen und mit fertigem Starter Code sofort loslegen.

Die Seite ist aus der OGD-Station für die [Scientifica 2026](https://scientifica.ch)
hervorgegangen und für den dauerhaften Betrieb ausserhalb eines Anlasses umgebaut.
Der Umbau ist in [UMBAU-PLAN.md](UMBAU-PLAN.md) dokumentiert — dort steht auch, was noch offen ist.

## Inhalt

| Seite | Beschreibung |
|---|---|
| [Anwendungen](anwendungen/) | Bestehende OGD-Anwendungen erkunden (Hanami, Velounfälle, OGD4All u.a.) |
| [OGD-Katalog](katalog/) | Über 900 Datensätze durchsuchen — Kategorien, Formate, Suchschritte |
| [MCP-Abfragen](mcp-abfragen/) | Daten in natürlicher Sprache abfragen — Beispielfragen öffnen Claude.ai mit dem passenden MCP-Server |
| [Starter Code](starter-code/) | Python/R-Notebooks und SQL Workbench ausprobieren, Beispielauswertungen zum Kopieren |

## Lokal starten

```bash
python -m http.server 8080
```

Dann im Browser [http://localhost:8080](http://localhost:8080) öffnen.

Das Video auf der Starter-Code-Seite funktioniert nur über einen HTTP-Server, nicht via `file:///`.

## Kiosk-Modus (für Anlässe)

Die Seite lässt sich weiterhin als selbstzurücksetzende Station an Messen und Anlässen
betreiben. Der Modus ist **opt-in** und wird über den URL-Parameter `?kiosk=1` aktiviert:

```bash
chrome.exe --kiosk --noerrdialogs "http://localhost:8080/?kiosk=1"
```

Im Kiosk-Modus erscheint nach 3 Minuten Inaktivität ein Reset-Overlay, und das Markieren von
Text ist gesperrt (Code-Blöcke ausgenommen). Der Parameter wird beim Navigieren automatisch
an alle internen Links weitergegeben. Ohne den Parameter verhält sich die Seite wie eine
normale Webseite.

## Projektstruktur

```
├── index.html              Startseite (Kachel-Übersicht der vier Themen)
├── anwendungen/index.html  OGD-Anwendungen als Bildkacheln
├── katalog/index.html      OGD-Katalog: Einführung, Kategorien, Formate
├── mcp-abfragen/index.html MCP-Server: Intro, Kurzanleitung, Server-Karten
├── starter-code/index.html Starter Code: Video, Schritte, Beispielauswertungen
├── UMBAU-PLAN.md           Stand und offene Schritte des Umbaus
└── shared/
    ├── style.css           Gemeinsames CSS (CI/CD-Farben Stadt Zürich)
    ├── kiosk.js            Kiosk-Modus, nur aktiv mit ?kiosk=1
    └── logo_stzh_rgb_weiss_digital.svg
```

## Technologie

Rein statische HTML/CSS/JS-Seiten ohne Build-System oder Abhängigkeiten.

- Gemeinsames CSS über `shared/style.css` (Farbpalette Stadt Zürich)
- Starter Code: Tab-Wechsel Python/R, Copy-Buttons, aufklappbare `<details>`
- MCP-Abfragen: Beispiel-Chips öffnen `claude.ai/new?q=...` mit Server-Prefix,
  JS-Höhenangleichung der Karten

> **Bekannte Einschränkung:** Die Seite ist noch nicht responsiv — sie stammt aus dem
> Kiosk-Betrieb auf Geräten mit 1280×800 CSS-Pixeln. Siehe Phase 4 im
> [UMBAU-PLAN.md](UMBAU-PLAN.md).

## Lizenz

Inhalte und Code: Stadt Zürich, Statistik Stadt Zürich.
