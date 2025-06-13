"""
Einfacher Test für deutsche Syntax
"""

# Direkter Import und Test
from schlange.transformer import transformiere, führe_aus

# Sehr einfacher Test
print("=== Test 1: Einfache Transformation ===")
test_code = "drucke('Hallo Welt!')"
print(f"Original: {test_code}")
transformed = transformiere(test_code)
print(f"Transformiert: {transformed}")

print("\n=== Test 2: Deutsche Schlüsselwörter ===")
test_code2 = """
x = 10
y = 5
wenn x > y:
    drucke("x ist größer")
"""
print("Original Code:")
print(test_code2)

transformed2 = transformiere(test_code2)
print("Transformierter Code:")
print(transformed2)

print("\n=== Test 3: Ausführung ===")
try:
    führe_aus(test_code2)
    print("Ausführung erfolgreich!")
except Exception as e:
    print(f"Fehler bei Ausführung: {e}")
    import traceback
    traceback.print_exc()

print("\n=== Test 4: Direkter exec Test ===")
try:
    # Direkte Transformation und Ausführung
    from schlange.functions import drucke
    
    transformed_code = transformed2
    globals_dict = {'drucke': drucke}
    
    print("Führe transformierten Code aus:")
    exec(transformed_code, globals_dict)
    
except Exception as e:
    print(f"Fehler: {e}")
    import traceback
    traceback.print_exc()
