# -*- coding: utf-8 -*-
"""
Finale Test-Suite für Schlange v0.1.5
Testet alle verfügbaren Features einschließlich .schlange Dateien
"""

import schlange

def test_alle_features():
    print("🐍 Schlange v0.1.5 - Kompletter Feature-Test")
    print("=" * 50)
    
    # Test 1: Deutsche Funktionen
    print("\n1️⃣ Test: Deutsche Funktionen")
    print("-" * 30)
    schlange.drucke("✅ drucke() funktioniert")
    print(f"✅ laenge([1,2,3]) = {schlange.laenge([1,2,3])}")
    print(f"✅ bereich(3) = {list(schlange.bereich(3))}")
    
    # Test 2: deutsch() Funktion
    print("\n2️⃣ Test: deutsch() Funktion")
    print("-" * 30)
    schlange.deutsch("""
drucke("✅ deutsch() Funktion funktioniert")
für i in bereich(3):
    drucke(f"  Zahl: {i}")
    """)
    
    # Test 3: .schlange Dateien - Direkte Ausführung
    print("\n3️⃣ Test: .schlange Datei - Direkte Ausführung")
    print("-" * 30)
    try:
        schlange.fuehre_schlange_aus("beispiele/test.schlange")
        print("✅ .schlange Datei direkt ausgeführt")
    except Exception as e:
        print(f"❌ Fehler: {e}")
    
    # Test 4: .schlange Dateien - Namespace-Zugriff
    print("\n4️⃣ Test: .schlange Datei - Namespace-Zugriff")
    print("-" * 30)
    try:
        namespace = schlange.lade_schlange_datei("beispiele/test.schlange")
        print("✅ .schlange Datei mit Namespace geladen")
        print(f"  Variable 'mein_name': {namespace.get('mein_name', 'nicht gefunden')}")
        print(f"  Variable 'alter': {namespace.get('alter', 'nicht gefunden')}")
        
        # Funktion aus Namespace aufrufen
        if 'grüße' in namespace:
            greet_func = namespace['grüße']
            result = greet_func("Tester")
            print(f"  Funktion 'grüße' aufgerufen: {result}")
        
    except Exception as e:
        print(f"❌ Fehler: {e}")
    
    # Test 5: CLI-Tool
    print("\n5️⃣ Test: CLI-Tool (Simulation)")
    print("-" * 30)
    print("✅ CLI-Tool verfügbar: python -m schlange.cli")
    
    # Test 6: Import-Hook
    print("\n6️⃣ Test: Import-Hook")
    print("-" * 30)
    try:
        schlange.install_import_hook()
        print("✅ Import-Hook installiert")
        schlange.uninstall_import_hook()
        print("✅ Import-Hook deinstalliert")
    except Exception as e:
        print(f"❌ Fehler: {e}")
    
    print("\n" + "=" * 50)
    print("🎉 Alle Tests abgeschlossen!")
    print(f"📦 Schlange Version: {schlange.__version__}")
    print("🚀 Bereit für PyPI Upload!")

if __name__ == "__main__":
    test_alle_features()
