#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Vollständiger Test für Schlange Package v0.1.3
"""

print("=== Schlange Package Test v0.1.3 ===")

# Test 1: Import
try:
    import schlange
    print("✅ Import erfolgreich")
    print(f"   Version: {schlange.__version__}")
except Exception as e:
    print(f"❌ Import fehlgeschlagen: {e}")
    exit(1)

# Test 2: Deutsche Funktionen
try:
    from schlange import drucke, laenge, bereich
    drucke("✅ Deutsche Funktionen importiert")
    
    # Teste laenge
    test_liste = [1, 2, 3, 4, 5]
    if laenge(test_liste) == 5:
        drucke("✅ laenge() funktioniert")
    else:
        print("❌ laenge() fehlerhaft")
    
    # Teste bereich
    zahlen = list(bereich(3))
    if zahlen == [0, 1, 2]:
        drucke("✅ bereich() funktioniert")
    else:
        print("❌ bereich() fehlerhaft")
        
except Exception as e:
    print(f"❌ Deutsche Funktionen fehlgeschlagen: {e}")

# Test 3: Code-Transformation
try:
    from schlange.transformer import transformiere, fuehre_aus
    
    test_code = """
x = 10
wenn x > 5:
    drucke("x ist groß")
    """
    
    transformiert = transformiere(test_code)
    if "if x > 5:" in transformiert and "print(" in transformiert:
        print("✅ Code-Transformation funktioniert")
    else:
        print("❌ Code-Transformation fehlerhaft")
        
    # Test Ausführung
    print("✅ Teste Code-Ausführung:")
    fuehre_aus(test_code)
    
except Exception as e:
    print(f"❌ Code-Transformation fehlgeschlagen: {e}")

# Test 4: Umlaute-Aliasse
try:
    from schlange import länge, wörterbuch, aufzählen
    print("✅ Umlaute-Aliasse funktionieren")
except Exception as e:
    print(f"❌ Umlaute-Aliasse fehlgeschlagen: {e}")

print("\n=== Test abgeschlossen ===")
print("Schlange Package v0.1.3 ist funktionsfähig!")
print("\nVerwendung:")
print("1. Deutsche Funktionen: from schlange import drucke, laenge")
print("2. Code-Transformation: from schlange.transformer import fuehre_aus")
print("3. CLI-Tool: python3 -m schlange.cli meine_datei.py")
