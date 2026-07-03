import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from desafio import dar_cambio, cantidad_por_denominacion

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

print("=== NIVEL 5h: Calculadora de Cambio ===\n")

MONEDAS = [100, 50, 10, 5, 1]

test("cambio exacto 160",      dar_cambio(160, MONEDAS),  [100, 50, 10])
test("cambio exacto 75",       dar_cambio(75, MONEDAS),   [50, 10, 10, 5])
test("cambio exacto 1",        dar_cambio(1, MONEDAS),    [1])
test("cambio exacto 100",      dar_cambio(100, MONEDAS),  [100])
test("imposible dar cambio",   dar_cambio(30, [25, 10]),  [])

test("denominacion básico",
     cantidad_por_denominacion([100, 50, 10]),
     {100: 1, 50: 1, 10: 1})
test("denominacion con repetidos",
     cantidad_por_denominacion([10, 10, 5]),
     {10: 2, 5: 1})
test("denominacion un elemento",
     cantidad_por_denominacion([50]),
     {50: 1})
test("ida y vuelta: 160",
     cantidad_por_denominacion(dar_cambio(160, MONEDAS)),
     {100: 1, 50: 1, 10: 1})

print(f"\n{'='*35}")
print(f"Resultado: {varOcg - failed}/{varOcg} pasados")
if failed == 0:
    print("¡Perfecto! Todos los tests pasaron.")
else:
    print(f"Tienes {failed} test(s) por corregir.")
