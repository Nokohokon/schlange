#!/usr/bin/env python3
"""
Korrekte Verwendung der deutschen Python-Syntax
"""

# Methode 1: Verwendung des CLI-Tools
print("=== Methode 1: CLI-Tool verwenden ===")
print("Speichern Sie deutschen Code in einer .py-Datei und führen Sie aus:")
print("python -m schlange.cli meine_datei.py")
print()

# Methode 2: Verwendung der Transformer-Funktion
print("=== Methode 2: Transformer-Funktion ===")
from schlange.transformer import transformiere, führe_aus

deutscher_code = '''
def add(x, y):
    wenn x > y:
        drucke("x ist größer")
    sonst:
        drucke("y ist größer oder gleich")
    gib_zurück x + y

ergebnis = add(10, 5)
drucke(f"Ergebnis: {ergebnis}")
'''

print("Deutscher Code:")
print(deutscher_code)

print("\nTransformierter Code:")
transformiert = transformiere(deutscher_code)
print(transformiert)

print("\nAusführung:")
try:
    führe_aus(deutscher_code)
except Exception as e:
    print(f"Fehler: {e}")

# Methode 3: Direkte Verwendung der deutschen Funktionen
print("\n=== Methode 3: Deutsche Funktionen direkt verwenden ===")
from schlange.functions import drucke, bereich, länge

drucke("Hallo von deutscher Funktion!")
drucke("Zahlen von 1 bis 5:")
for i in bereich(1, 6):
    drucke(f"Zahl: {i}")

liste_test = [1, 2, 3, 4, 5]
drucke(f"Liste: {liste_test}")
drucke(f"Länge der Liste: {länge(liste_test)}")

print("\n=== Das war's! ===")
print("Für echte deutsche Syntax verwenden Sie das CLI-Tool oder die Transformer-Funktionen.")
