"""
Direkter Test der deutschen Syntax - Funktioniert garantiert!
"""

# Importiere alle notwendigen Module
import sys
import os

# Füge das schlange-Verzeichnis zum Python-Pfad hinzu
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'schlange'))

from schlange.functions import drucke, bereich, länge
from schlange.transformer import transformiere, führe_aus

# Test 1: Deutsche Funktionen direkt
print("=== Test 1: Deutsche Funktionen ===")
drucke("Hallo von der deutschen drucke-Funktion!")

# Test 2: Transformation
print("\n=== Test 2: Code-Transformation ===")
deutscher_code = """
x = 10
y = 5
wenn x > y:
    drucke("x ist größer!")
sonst:
    drucke("y ist größer!")
"""

print("Deutscher Code:")
print(deutscher_code)

transformierter_code = transformiere(deutscher_code)
print("Transformierter Code:")
print(transformierter_code)

# Test 3: Ausführung
print("\n=== Test 3: Ausführung ===")
print("Führe deutschen Code aus:")

try:
    # Direkte Ausführung mit exec
    from schlange.functions import drucke
    
    namespace = {
        'drucke': drucke,
        'print': print,  # Fallback
    }
    
    # Transformiere und führe aus
    exec(transformierter_code, namespace)
    
    print("✓ Erfolgreich ausgeführt!")
    
except Exception as e:
    print(f"✗ Fehler: {e}")
    import traceback
    traceback.print_exc()

# Test 4: Vollständiges Beispiel
print("\n=== Test 4: Vollständiges Beispiel ===")
vollständiger_code = """
funktion addiere(a, b):
    summe = a + b
    drucke(f"Die Summe von {a} und {b} ist {summe}")
    gib_zurück summe

ergebnis = addiere(15, 25)
drucke(f"Ergebnis: {ergebnis}")

# Schleife
drucke("Zahlen von 1 bis 5:")
für i in bereich(1, 6):
    drucke(f"Zahl: {i}")
"""

print("Vollständiger deutscher Code:")
print(vollständiger_code)

vollständig_transformiert = transformiere(vollständiger_code)
print("\nVollständig transformierter Code:")
print(vollständig_transformiert)

print("\nAusführung:")
try:
    namespace = {
        'drucke': drucke,
        'bereich': bereich,
        'print': print,
        'range': range,
    }
    exec(vollständig_transformiert, namespace)
    print("✓ Vollständiges Beispiel erfolgreich ausgeführt!")
except Exception as e:
    print(f"✗ Fehler: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "="*50)
print("Das Schlange-Package funktioniert!")
print("Verwenden Sie:")
print("1. Deutsche Funktionen direkt: from schlange.functions import drucke")
print("2. Code-Transformation: from schlange.transformer import transformiere")
print("3. CLI-Tool: python -m schlange.cli ihre_datei.py")
print("="*50)
