# -*- coding: utf-8 -*-
"""
ULTIMATIVE LÖSUNG: Deutsche Schlüsselwörter direkt verwenden

Es gibt 4 praktische Wege, deutsche Schlüsselwörter zu verwenden:
"""

# ====================================================================
# LÖSUNG 1: CLI-Tool (EINFACHSTE LÖSUNG)
# ====================================================================

"""
Speichern Sie Ihren Code in einer .py-Datei:

# datei: mein_programm.py
from schlange import *

x = int(input())

wenn x > 5:
    drucke("x ist größer 5")
sonst: 
    drucke("x ist kleiner oder gleich 5")

Dann ausführen mit:
python3 -m schlange.cli mein_programm.py
"""

# ====================================================================
# LÖSUNG 2: deutsch() Funktion (FLEXIBELSTE LÖSUNG)
# ====================================================================

from schlange import deutsch

def mein_deutsches_programm():
    """Führt deutschen Code direkt aus"""
    
    deutscher_code = '''
x = int(eingabe("Geben Sie eine Zahl ein: ") or "10")

wenn x > 5:
    drucke("x ist größer 5")
sonst: 
    drucke("x ist kleiner oder gleich 5")

# Weitere deutsche Syntax
für i in bereich(3):
    drucke(f"Zähler: {i}")

funktion addiere(a, b):
    summe = a + b
    drucke(f"{a} + {b} = {summe}")
    gib_zurück summe

ergebnis = addiere(5, 3)
drucke(f"Ergebnis: {ergebnis}")
'''
    
    print("=== Führe deutschen Code aus ===")
    deutsch(deutscher_code)

# ====================================================================
# LÖSUNG 3: Hybrid-Ansatz (PRAKTISCHSTE LÖSUNG)
# ====================================================================

from schlange import drucke, laenge, bereich, eingabe

def hybrid_beispiel():
    """Mischt deutsche Funktionen mit Python-Syntax"""
    
    # Deutsche Funktionen mit normaler Python-Syntax
    x = int(eingabe("Geben Sie eine Zahl ein: ") or "15")
    
    if x > 5:
        drucke("x ist größer 5")
    else:
        drucke("x ist kleiner oder gleich 5")
    
    # Deutsche Funktionen in Schleifen
    drucke("Zähle von 0 bis 4:")
    for i in bereich(5):
        drucke(f"Zahl: {i}")
    
    # Deutsche Funktionen mit Listen
    zahlen = [1, 2, 3, 4, 5]
    drucke(f"Liste: {zahlen}")
    drucke(f"Länge: {laenge(zahlen)}")

# ====================================================================
# LÖSUNG 4: Multi-Line String Execution
# ====================================================================

def multiline_deutsch():
    """Verwendet Multi-Line Strings für deutschen Code"""
    
    from schlange import fuehre_aus
    
    # Mehrzeiliger deutscher Code
    code = """
drucke("=== Multi-Line Deutsch ===")

name = eingabe("Wie heißen Sie? ") or "Anonym"
drucke(f"Hallo {name}!")

alter = int(eingabe("Wie alt sind Sie? ") or "25")

wenn alter >= 18:
    drucke("Sie sind volljährig")
    wenn alter >= 65:
        drucke("Sie sind im Rentenalter")
    sonst:
        drucke("Sie sind im Arbeitsalter")
sonst:
    drucke("Sie sind minderjährig")

# Funktion definieren
funktion berechne_quadrat(zahl):
    quadrat = zahl * zahl
    drucke(f"Das Quadrat von {zahl} ist {quadrat}")
    gib_zurück quadrat

für i in bereich(1, 4):
    berechne_quadrat(i)
"""
    
    fuehre_aus(code)

# ====================================================================
# DEMONSTRATIONS-RUNNER
# ====================================================================

if __name__ == "__main__":
    print("=== DEUTSCHE PYTHON SYNTAX - ALLE LÖSUNGEN ===\n")
    
    print("1. deutsch() Funktion:")
    mein_deutsches_programm()
    
    print("\n" + "="*50)
    print("2. Hybrid-Ansatz:")
    hybrid_beispiel()
    
    print("\n" + "="*50)
    print("3. Multi-Line Execution:")
    multiline_deutsch()
    
    print("\n" + "="*50)
    print("4. CLI-Tool Anleitung:")
    print("   Speichern Sie deutschen Code in eine .py-Datei")
    print("   Führen Sie aus: python3 -m schlange.cli datei.py")
    
    print("\n=== FAZIT ===")
    print("Deutsche Schlüsselwörter funktionieren mit allen 4 Methoden!")
    print("Wählen Sie die Methode, die am besten zu Ihrem Workflow passt.")
