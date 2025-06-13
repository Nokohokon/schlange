"""
Schlange - Verwendungsanleitung
===============================

Dieses Dokument zeigt, wie Sie das Schlange-Package verwenden können.
"""

# Methode 1: Deutsche Funktionen direkt verwenden
print("=== Methode 1: Deutsche Funktionen direkt ===")
from schlange.functions import drucke, bereich, länge, eingabe

drucke("Hallo Welt!")
drucke("Deutsche Funktionen funktionieren direkt!")

zahlen = [1, 2, 3, 4, 5]
drucke(f"Liste: {zahlen}")
drucke(f"Länge: {länge(zahlen)}")

drucke("Zähle von 1 bis 5:")
for i in bereich(1, 6):
    drucke(f"Zahl: {i}")

# Methode 2: Code-Transformation verwenden
print("\n=== Methode 2: Code-Transformation ===")
from schlange.transformer import transformiere, führe_aus

# Deutscher Code als String
deutscher_code = """
# Deutsche Funktionen
drucke("Hallo aus deutschem Code!")

# Deutsche Kontrollstrukturen
x = 10
y = 5

wenn x > y:
    drucke("x ist größer als y")
sonst:
    drucke("y ist größer oder gleich x")

# Deutsche Schleifen
drucke("Zähle von 1 bis 3:")
für i in bereich(1, 4):
    drucke(f"Schleife {i}")

# Deutsche Funktionen definieren
funktion sage_hallo(name):
    drucke(f"Hallo {name}!")
    gib_zurück f"Hallo {name}!"

nachricht = sage_hallo("Welt")
drucke(f"Nachricht: {nachricht}")
"""

# Zeige Transformation
print("Transformierter Code:")
transformiert = transformiere(deutscher_code)
print(transformiert)

print("\nAusführung des deutschen Codes:")
führe_aus(deutscher_code)

# Methode 3: CLI-Tool verwenden
print("\n=== Methode 3: CLI-Tool ===")
print("Speichern Sie deutschen Code in einer .py-Datei und führen Sie aus:")
print("python -m schlange.cli ihre_datei.py")

# Verfügbare deutsche Begriffe
print("\n=== Verfügbare deutsche Begriffe ===")
print("Schlüsselwörter:")
print("- wenn (if)")
print("- sonst (else)")
print("- sonstwenn (elif)")
print("- für (for)")
print("- solange (while)")
print("- funktion (def)")
print("- klasse (class)")
print("- gib_zurück (return)")
print("- Wahr (True)")
print("- Falsch (False)")
print("- Nichts (None)")
print("- und (and)")
print("- oder (or)")
print("- nicht (not)")
print("- selbst (self)")

print("\nFunktionen:")
print("- drucke() (print)")
print("- eingabe() (input)")
print("- länge() (len)")
print("- bereich() (range)")
print("- typ() (type)")
print("- liste() (list)")
print("- wörterbuch() (dict)")
print("- zeichenkette() (str)")
print("- ganze_zahl() (int)")
print("- dezimal_zahl() (float)")

print("\n=== Schlange ist bereit! ===")
drucke("Viel Spaß beim Programmieren auf Deutsch! 🐍🇩🇪")
