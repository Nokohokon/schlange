#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test der neuen deutschen Syntax-Integrationen
"""

print("=== Test der erweiterten deutschen Syntax-Features ===")

# Test 1: Direkte Code-Ausführung mit deutsch()
print("\n1. Test: deutsch() Funktion")
from schlange import deutsch

deutscher_code = """
x = int(eingabe("Geben Sie eine Zahl ein (oder 7 für Test): ") or "7")
wenn x > 5:
    drucke(f"x ({x}) ist größer als 5")
sonst:
    drucke(f"x ({x}) ist kleiner oder gleich 5")
"""

print("Führe deutschen Code aus:")
print(deutscher_code)
print("Ausgabe:")
deutsch(deutscher_code)

# Test 2: Magic System (falls verfügbar)
print("\n2. Test: Magic System")
try:
    from schlange import aktiviere_deutsche_syntax, deaktiviere_deutsche_syntax
    print("Magic System verfügbar!")
    
    # Aktiviere Magic
    aktiviere_deutsche_syntax()
    
    # Teste exec mit deutschem Code
    print("Teste exec mit deutschem Code:")
    exec("""
y = 15
wenn y > 10:
    drucke(f"Magic funktioniert! y = {y}")
""")
    
    # Deaktiviere Magic
    deaktiviere_deutsche_syntax()
    
except ImportError:
    print("Magic System nicht verfügbar")

# Test 3: Context Manager
print("\n3. Test: Context Manager")
try:
    from schlange import deutsche_syntax
    
    with deutsche_syntax():
        print("In deutschem Kontext:")
        exec("""
z = 20
wenn z > 15:
    drucke(f"Context Manager funktioniert! z = {z}")
""")
    
    print("Außerhalb deutschem Kontext")
    
except ImportError:
    print("Context Manager nicht verfügbar")

# Test 4: Code-String direkt
print("\n4. Test: Verschiedene Code-Ausführung")
from schlange import fuehre_aus

test_codes = [
    """
drucke("Test 1: Einfache Ausgabe")
""",
    """
numbers = [1, 2, 3, 4, 5]
summe_wert = 0
für num in numbers:
    summe_wert += num
drucke(f"Summe: {summe_wert}")
""",
    """
funktion begrüße(name):
    drucke(f"Hallo {name}!")
    gib_zurück f"Begrüßung für {name} abgeschlossen"

result = begrüße("Welt")
drucke(result)
"""
]

for i, code in enumerate(test_codes, 1):
    print(f"\nTest {i}:")
    fuehre_aus(code)

print("\n=== Tests abgeschlossen ===")
print("Deutsche Syntax funktioniert mit verschiedenen Ansätzen!")
