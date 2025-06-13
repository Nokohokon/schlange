# 🐍 Schlange v0.1.6 Release Notes

## 🚀 Neue Version: 0.1.6 - Import-Bug Fix & Bereinigung

### 🔧 Bugfixes
- **Kritischer Import-Bug behoben**: `importiere os als betriebssystem` funktioniert jetzt korrekt
- **Syntaxfehler behoben**: Keine fälschlichen Rück-Transformationen von `as` zu `als` mehr
- **Stabile Python-Package-Integration**: Alle Standard- und Third-Party-Packages funktionieren in `.schlange` Dateien

### 🧹 Projekt-Bereinigung
- Entfernte unnötige `beispiele/` und `tests/` Verzeichnisse
- Entfernte Build-Artefakte (`build/`, `dist/`, `*.egg-info/`)
- Hinzugefügte `.gitignore` für saubere Entwicklung
- Optimierte Projektstruktur für Produktion

### ✨ Verbesserungen
- **Erweiterte pyproject.toml**: Bessere Metadaten und Keywords für PyPI
- **Vollständige Package-Kompatibilität**: Unterstützung für alle Python-Packages
- **Stabile API**: Alle Kernfunktionen bleiben unverändert

### 📦 Was funktioniert jetzt perfekt:
```python
# In .schlange Dateien oder mit schlange.deutsch():
importiere os als system
importiere math als mathe
von datetime importiere datetime als zeit
von json importiere dumps als zu_json

# Alle Standard-Python-Packages
importiere requests
importiere numpy als np
importiere pandas als pd

drucke("Alles funktioniert!")
```

### 🎯 Migration von v0.1.5:
Keine Breaking Changes! Alle bestehenden `.schlange` Dateien und Code funktionieren weiterhin.

### 👨‍💻 Für Entwickler:
- Bereinigte Codebasis
- Bessere Projektstruktur
- Produktionsreife Konfiguration

---

**Download**: `pip install schlange==0.1.6`

**Vollständige Changelog**: Siehe [CHANGELOG.md](CHANGELOG.md)
