"""
Beispiel-Programm mit deutscher Syntax

WICHTIG: Diese Datei muss mit dem CLI-Tool oder deutsch() ausgeführt werden!
Nicht direkt mit python ausführen!
"""

from schlange import *

x = int(input("Geben Sie eine Zahl ein: "))

wenn x > 5:
    drucke("x ist größer 5")
sonst: 
    drucke("x ist kleiner oder gleich 5")

# Zusätzliche Tests
drucke("Weitere Tests:")

für i in bereich(3):
    drucke(f"Iteration {i}")

zahlen = [1, 2, 3, 4, 5]
drucke(f"Länge der Liste: {laenge(zahlen)}")

funktion addiere(a, b):
    ergebnis = a + b
    drucke(f"{a} + {b} = {ergebnis}")
    gib_zurück ergebnis

summe = addiere(10, 5)
drucke(f"Summe ist: {summe}")
