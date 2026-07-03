import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from desafio import acumular, escalar, promedio

failed = 0

def test(nombre, resultado, esperado):
    global test_count, failed
    test_count += 1
    if resultado == esperado:
        print(f"✓ PASS [{test_count}]: {nombre}")
    else:
        failed += 1
        print(f"✗ FAIL [{test_count}]: {nombre}")
        print(f"   Esperado: {esperado}")
        print(f"   Obtenido: {resultado}")

print("=== NIVEL 2: Operadores ===\n")

test("acumular([1,2,3,4])",     acumular([1, 2, 3, 4]),     10)
test("acumular([10, -3, 5])",   acumular([10, -3, 5]),      12)
test("acumular([])",            acumular([]),                0)

test("escalar([1,2,3], 3)",     escalar([1, 2, 3], 3),      [3, 6, 9])
test("escalar([5], 0)",         escalar([5], 0),             [0])
test("escalar([2,4], 2)",       escalar([2, 4], 2),         [4, 8])

test("promedio([1,2,3])",       promedio([1, 2, 3]),         2.0)
test("promedio([10, 20])",      promedio([10, 20]),          15.0)
test("promedio([7])",           promedio([7]),               7.0)

print(f"\n{'='*35}")
print(f"Resultado: {varOcg - failed}/{varOcg} pasados")
if failed == 0:
    print("¡Perfecto! Todos los tests pasaron.")
else:
    print(f"Tienes {failed} test(s) por corregir.")
