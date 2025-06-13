# Changelog

## Version 0.1.3 (2025-06-13)

### Kritische Bugfixes:
- ✅ Behoben: Encoding-Probleme mit deutschen Umlauten in Python-Dateien
- ✅ Behoben: SyntaxError durch UTF-8 Zeichen in Funktionsnamen
- ✅ Hinzugefügt: Proper encoding declarations (# -*- coding: utf-8 -*-)
- ✅ Verbessert: ASCII-kompatible Funktionsnamen mit Umlauten-Aliassen
- ✅ Behoben: Python 2/3 Kompatibilitätsprobleme

### Neue Features:
- ASCII-kompatible Funktionsnamen: `laenge()` (mit Alias `länge()`)
- ASCII-kompatible Funktionsnamen: `woerterbuch()` (mit Alias `wörterbuch()`)
- ASCII-kompatible Funktionsnamen: `aufzaehlen()` (mit Alias `aufzählen()`)
- ASCII-kompatible Funktionsnamen: `loesche_attribut()` (mit Alias `lösche_attribut()`)
- ASCII-kompatible Transformer-Funktion: `fuehre_aus()` (mit Alias `führe_aus()`)

### Technische Verbesserungen:
- Entfernt: Type hints für bessere Python-Versions-Kompatibilität
- Vereinfacht: Funktionsdefinitionen für stabilere Ausführung
- Verbessert: Import-System funktioniert jetzt zuverlässig
- Getestet: CLI-Tool funktioniert vollständig

### Erfolgreiche Tests:
- ✅ `import schlange` funktioniert ohne Fehler
- ✅ Deutsche Funktionen (`drucke`, `laenge`, `bereich`) funktionieren
- ✅ Code-Transformation funktioniert korrekt
- ✅ CLI-Tool funktioniert: `python3 -m schlange.cli datei.py`
- ✅ Alle Beispiele laufen erfolgreich

## Version 0.1.1 (2025-06-13)

### Verbesserte Funktionen:
- ✅ Verbesserte Code-Transformation für deutsche Syntax
- ✅ Bessere Behandlung von deutschen Operatoren ('ist', 'als')
- ✅ Stabileres CLI-Tool für deutsche .py-Dateien
- ✅ Erweiterte Fehlerbehandlung im Transformer
- ✅ Vollständige Dokumentation und Beispiele

### Neue Features:
- Deutsche Schlüsselwörter funktionieren zuverlässig
- Verbesserter Import-Hook für deutsche Syntax
- Umfassende Beispielsammlung
- Detaillierte Verwendungsanleitung

### Bugfixes:
- Korrigierte Transformation von 'ist' vs 'is'
- Korrigierte Transformation von 'als' vs 'as'
- Bessere Behandlung von f-strings mit deutschen Begriffen
- Stabilere Ausführung von deutschem Code

### Technische Verbesserungen:
- Optimierter Code-Transformer
- Bessere Regex-Patterns für deutsche Begriffe
- Erweiterte Funktionsmappings
- Verbesserte Fehlerbehandlung

## Version 0.1.0 (2025-06-13)

### Erste Veröffentlichung:
- Grundlegende deutsche Python-Funktionen
- Code-Transformation für deutsche Syntax
- CLI-Tool für deutsche .py-Dateien
- PyPI-Veröffentlichung
