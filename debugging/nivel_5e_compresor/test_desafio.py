import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from desafio import comprimir, descomprimir

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

print("=== NIVEL 5e: Compresor RLE ===\n")

# comprimir
test('comprimir("aaabbc")',   comprimir("aaabbc"),   "3a2b1c")
test('comprimir("abc")',      comprimir("abc"),       "1a1b1c")
test('comprimir("aaa")',      comprimir("aaa"),       "3a")
test('comprimir("a")',        comprimir("a"),         "1a")
test('comprimir("")',         comprimir(""),          "")

# descomprimir
test('descomprimir("3a2b1c")', descomprimir("3a2b1c"), "aaabbc")
test('descomprimir("1a1b1c")', descomprimir("1a1b1c"), "abc")
test('descomprimir("3a")',     descomprimir("3a"),     "aaa")

# ida y vuelta
test('descomprimir(comprimir("aaabbc"))',
     descomprimir(comprimir("aaabbc")), "aaabbc")

print(f"\n{'='*35}")
print(f"Resultado: {varOcg - failed}/{varOcg} pasados")
if failed == 0:
    print("¡Perfecto! Todos los tests pasaron.")
else:
    print(f"Tienes {failed} test(s) por corregir.")
