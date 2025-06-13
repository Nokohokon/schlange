"""
Einfaches Beispiel für deutsche Python-Syntax
"""

# Verwendung der deutschen Funktionen
from schlange.einfach import *

# Direkte Verwendung der deutschen Funktionen
drucke("Hallo Welt!")

name = "Max"
alter = 25

drucke(f"Name: {name}")
drucke(f"Alter: {alter}")

# Listen-Operationen
zahlen = [1, 2, 3, 4, 5]
drucke(f"Zahlen: {zahlen}")
drucke(f"Länge der Liste: {länge(zahlen)}")

# Bereich verwenden
drucke("Zahlen von 1 bis 5:")
for i in bereich(1, 6):
    drucke(i)

# Deutscher Code als String ausführen
deutscher_code = """
drucke("=== Deutscher Code ===")

funktion addiere(a, b):
    ergebnis = a + b
    drucke(f"{a} + {b} = {ergebnis}")
    gib_zurück ergebnis

x = 10
y = 5

wenn x > y:
    drucke("x ist größer als y")
    summe = addiere(x, y)
    drucke(f"Summe: {summe}")
sonst:
    drucke("y ist größer oder gleich x")

für i in bereich(3):
    drucke(f"Iteration: {i}")
"""

# Führe den deutschen Code aus
drucke("\n=== Führe deutschen Code aus ===")
evaluiere_deutschen_code(deutscher_code)
