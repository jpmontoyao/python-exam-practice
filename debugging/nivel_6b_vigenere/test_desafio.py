import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from desafio import cifrar, descifrar

failed = 0

def test(nombre, resultado, esperado):
    global test_count, failed
    test_count += 1
    if resultado == esperado:
        print(f"✓ PASS [{test_count}]: {nombre}")
    else:
        failed += 1
        print(f"✗ FAIL [{test_count}]: {nombre}")
        print(f"   Esperado: {esperado!r}")
        print(f"   Obtenido: {resultado!r}")

print("=== NIVEL 6b: Cifrado Vigenère ===\n")

test('cifrar("HELLO", "KEY")',       cifrar("HELLO", "KEY"),        "RIJVS")
test('cifrar("ABC", "A")',           cifrar("ABC", "A"),            "ABC")
test('cifrar("ABC", "B")',           cifrar("ABC", "B"),            "BCD")
test('cifrar("XYZ", "B")',           cifrar("XYZ", "B"),            "YZA")
test('cifrar clave más corta',       cifrar("ATTACK", "KEY"),       "KXVMEE")

test('descifrar("RIJVS", "KEY")',    descifrar("RIJVS", "KEY"),     "HELLO")
test('descifrar("ABC", "A")',        descifrar("ABC", "A"),         "ABC")
test('descifrar("BCD", "B")',        descifrar("BCD", "B"),         "ABC")
test('descifrar("YZA", "B")',        descifrar("YZA", "B"),         "XYZ")

test('ida y vuelta',
     descifrar(cifrar("PYTHON", "CLAVE"), "CLAVE"), "PYTHON")

print(f"\n{'='*35}")
print(f"Resultado: {varOcg - failed}/{varOcg} pasados")
if failed == 0:
    print("¡Perfecto! Todos los tests pasaron.")
else:
    print(f"Tienes {failed} test(s) por corregir.")
