"""
Funktionsfähige deutsche Python-Syntax
Dieses Modul zeigt, wie man deutsche Syntax korrekt verwendet.
"""

from schlange.transformer import transformiere, führe_aus

# Beispiel 1: Verwendung der Transformer-Funktion
deutscher_code = """
def add(x, y):
    wenn x > y:
        drucke(f"x ({x}) ist größer als y ({y})")
    sonst:
        drucke(f"y ({y}) ist größer oder gleich x ({x})")
    gib_zurück x + y

ergebnis = add(10, 5)
drucke(f"Ergebnis: {ergebnis}")
"""

print("=== Deutscher Code ===")
print(deutscher_code)

print("\n=== Transformierter Code ===")
englischer_code = transformiere(deutscher_code)
print(englischer_code)

print("\n=== Ausführung ===")
führe_aus(deutscher_code)

# Beispiel 2: Komplexerer deutscher Code
komplexer_code = """
klasse Person:
    funktion __init__(selbst, name, alter):
        selbst.name = name
        selbst.alter = alter
    
    funktion vorstellen(selbst):
        drucke(f"Hallo, ich bin {selbst.name} und {selbst.alter} Jahre alt.")
    
    funktion ist_erwachsen(selbst):
        wenn selbst.alter >= 18:
            gib_zurück Wahr
        sonst:
            gib_zurück Falsch

# Personen erstellen
person1 = Person("Anna", 25)
person2 = Person("Max", 16)

# Personen vorstellen
person1.vorstellen()
person2.vorstellen()

# Prüfen, ob erwachsen
für person in [person1, person2]:
    wenn person.ist_erwachsen():
        drucke(f"{person.name} ist erwachsen.")
    sonst:
        drucke(f"{person.name} ist noch minderjährig.")

# Zahlen-Beispiel
zahlen = [1, 2, 3, 4, 5]
drucke(f"Zahlen: {zahlen}")

summe = 0
für zahl in zahlen:
    summe += zahl

drucke(f"Summe: {summe}")

# Bedingte Anweisungen
für i in bereich(1, 6):
    wenn i % 2 == 0:
        drucke(f"{i} ist gerade")
    sonst:
        drucke(f"{i} ist ungerade")
"""

print("\n" + "="*50)
print("=== Komplexerer deutscher Code ===")
print("\n=== Ausführung ===")
führe_aus(komplexer_code)
