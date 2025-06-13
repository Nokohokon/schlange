"""
Beispiel für deutsche Python-Syntax mit Schlange
"""

from schlange import *

# Teste Ihr Beispiel
def add(x, y):
    wenn x > y:
        drucke(f"x ({x}) ist größer als y ({y})")
    sonst:
        drucke(f"y ({y}) ist größer oder gleich x ({x})")
    
    gib_zurück x + y

# Teste die Funktion
ergebnis = add(10, 5)
drucke(f"Ergebnis: {ergebnis}")

# Weitere Tests
drucke("=== Weitere Tests ===")

# Schleife
für i in bereich(3):
    drucke(f"Iteration {i}")

# While-Schleife
x = 0
solange x < 3:
    drucke(f"x = {x}")
    x += 1

# Klasse
klasse MeineKlasse:
    funktion __init__(selbst, name):
        selbst.name = name
    
    funktion sage_hallo(selbst):
        drucke(f"Hallo, ich bin {selbst.name}")

obj = MeineKlasse("Test")
obj.sage_hallo()
