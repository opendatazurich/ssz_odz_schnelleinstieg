# Scientifica 2026: Open Government Data — Stadt Zürich

Statistik Stadt Zürich (SSZ) nimmt an der [Scientifica 2026](https://scientifica.ch) teil. Dieses Repository enthält die OGD-Station: eine interaktive Web-Anwendung, an der Besucher*innen Open Government Data der Stadt Zürich entdecken können.

## Kontext

- **Event:** Scientifica 2026, 22.–30. August 2026
- **Ort:** Napfgasse 6, 8001 Zürich
- **Format:** Selbstbestimmter Rundgang, 5–10 Laptops im Kiosk-Modus

## Stationen

| # | Station | Beschreibung |
|---|---------|--------------|
| 1 | [OGD-Katalog](katalog/) | Über 900 Datensätze durchsuchen — Kategorien, Formate, Suchschritte |
| 2 | [Starter Code](starter-code/) | Python/R-Notebooks und SQL Workbench ausprobieren, aufklappbare Beispielauswertungen mit Copy-Funktion |
| 3 | [MCP-Abfragen](mcp-abfragen/) | Daten in natürlicher Sprache abfragen — Beispielfragen öffnen direkt Claude.ai mit dem passenden MCP-Server |
| 4 | [Anwendungen](anwendungen/) | 7 bestehende OGD-Anwendungen erkunden (Hanami, Wowoni, Velounfälle u.a.) |

## Lokal starten

```bash
python -m http.server 8080
```

Dann im Browser [http://localhost:8080](http://localhost:8080) öffnen.

## Kiosk-Modus (Event)

```bash
chrome.exe --kiosk --noerrdialogs "http://localhost:8080"
```

Nach 3 Minuten Inaktivität erscheint automatisch ein Reset-Overlay.

## Projektstruktur

```
├── index.html              Startseite (2×2 Kachel-Grid, viewport-füllend)
├── katalog/index.html      OGD-Katalog: Einführung, Kategorien, Formate
├── starter-code/index.html Starter Code: Video, Schritte, Beispielauswertungen
├── mcp-abfragen/index.html MCP-Server: Intro, Kurzanleitung, Server-Karten
├── anwendungen/index.html  7 OGD-Anwendungen als Bildkacheln
└── shared/
    ├── style.css           Gemeinsames CSS (CI/CD-Farben Stadt Zürich)
    └── kiosk.js            Auto-Reset nach 3 Min. Inaktivität
```

## Technologie

Rein statische HTML/CSS/JS-Seiten ohne Build-System oder Abhängigkeiten.

- Gemeinsames CSS über `shared/style.css` (Stadt Zürich Farbpalette)
- Kiosk-Overlay via `shared/kiosk.js`
- Starter Code: Tab-Wechsel Python/R, Copy-Buttons, aufklappbare `<details>`
- MCP-Abfragen: Beispiel-Chips öffnen `claude.ai/new?q=...` mit Server-Prefix, JS-Höhenangleichung der Karten
- Zielauflösung: 1920×1200 bei 150% Skalierung (effektiv 1280×800 CSS-Pixel)

## Lizenz

Inhalte und Code: Stadt Zürich, Statistik Stadt Zürich.
