import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from desafio import sumar, es_par, maximo, contar

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

print("=== NIVEL 1: Sintaxis ===\n")

test("sumar(2, 3)",        sumar(2, 3),        5)
test("sumar(0, 0)",        sumar(0, 0),        0)
test("es_par(4)",          es_par(4),          True)
test("es_par(7)",          es_par(7),          False)
test("maximo(3, 7)",       maximo(3, 7),       7)
test("maximo(10, 2)",      maximo(10, 2),      10)
test("contar([1,2,3])",    contar([1, 2, 3]),  3)
test("contar([])",         contar([]),         0)

print(f"\n{'='*35}")
print(f"Resultado: {varOcg - failed}/{varOcg} pasados")
if failed == 0:
    print("¡Perfecto! Todos los tests pasaron.")
else:
    print(f"Tienes {failed} test(s) por corregir.")
