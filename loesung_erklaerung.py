#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lösung für deutsches Python - Verschiedene Ansätze
"""

print("=== Lösungen für deutsche Python-Syntax ===\n")

# Lösung 1: CLI-Tool (Empfohlen)
print("1. CLI-Tool Lösung (EMPFOHLEN):")
print("   Speichern Sie Ihren Code in eine .py-Datei und führen Sie aus:")
print("   python3 -m schlange.cli ihr_beispiel.py")
print()

# Lösung 2: deutsch() Funktion  
print("2. deutsch() Funktion:")
from schlange import deutsch

ihr_code = '''
x = int(eingabe("Geben Sie eine Zahl ein (oder 8 für Test): ") or "8")

wenn x > 5:
    drucke("x ist größer 5")
sonst: 
    drucke("x ist kleiner oder gleich 5")
'''

print("   Code:")
print(ihr_code)
print("   Ausführung:")
deutsch(ihr_code)
print()

# Lösung 3: Transformer direkt
print("3. Transformer direkt:")
from schlange.transformer import transformiere, fuehre_aus

print("   Transformation:")
transformiert = transformiere(ihr_code)
print(transformiert)
print("   Ausführung:")
fuehre_aus(ihr_code)
print()

# Lösung 4: Step-by-step für Verständnis
print("4. Was passiert intern:")
print("   Deutscher Code wird zu Python transformiert:")
print("   'wenn x > 5:' → 'if x > 5:'")
print("   'drucke(...)' → 'print(...)'")
print("   'sonst:' → 'else:'")
print()

# Das eigentliche Problem erklären
print("=== WARUM IHR CODE NICHT FUNKTIONIERT ===")
print()
print("Ihr Code:")
print("""
from schlange import *

x = int(input())

wenn x > 5:
    drucke("x ist größer 5")
sonst: drucke("x ist kleiner oder gleich 5")
""")
print()
print("Problem: Python kennt das Schlüsselwort 'wenn' nicht!")
print("'wenn' ist kein gültiges Python-Keyword.")
print()

print("=== LÖSUNGEN ===")
print()
print("A) CLI-Tool verwenden:")
print("   python3 -m schlange.cli ihre_datei.py")
print()
print("B) deutsch() Funktion:")
print("""
from schlange import deutsch
deutsch('''
x = int(eingabe("Zahl: "))
wenn x > 5:
    drucke("größer 5")
''')
""")
print()
print("C) Nur deutsche Funktionen (ohne Schlüsselwörter):")
print("""
from schlange import drucke, eingabe
x = int(eingabe("Zahl: "))
if x > 5:
    drucke("größer 5")
else:
    drucke("kleiner gleich 5")
""")

print("\n=== Empfehlung ===")
print("Verwenden Sie das CLI-Tool für vollständige deutsche Syntax!")
print("Erstellen Sie eine .py-Datei und führen Sie aus:")
print("python3 -m schlange.cli ihre_datei.py")
