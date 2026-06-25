import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from desafio import filtrar_positivos, contar_mayores, tiene_duplicado
# __define-ocg__

varOcg = 0
failed = 0

def test(nombre, resultado, esperado):
    global varOcg, failed
    varOcg += 1
    if resultado == esperado:
        print(f"✓ PASS [{varOcg}]: {nombre}")
    else:
        failed += 1
        print(f"✗ FAIL [{varOcg}]: {nombre}")
        print(f"   Esperado: {esperado}")
        print(f"   Obtenido: {resultado}")

print("=== NIVEL 3: Condiciones ===\n")

test("filtrar_positivos([1,-2,3,-4,0])", filtrar_positivos([1, -2, 3, -4, 0]), [1, 3])
test("filtrar_positivos([-1,-2,-3])",    filtrar_positivos([-1, -2, -3]),       [])
test("filtrar_positivos([5,10])",        filtrar_positivos([5, 10]),             [5, 10])

test("contar_mayores([1,2,3,4], 2)",     contar_mayores([1, 2, 3, 4], 2),       2)
test("contar_mayores([5,5,5], 5)",       contar_mayores([5, 5, 5], 5),          0)
test("contar_mayores([1,2,3], 0)",       contar_mayores([1, 2, 3], 0),          3)

test("tiene_duplicado([1,2,3])",         tiene_duplicado([1, 2, 3]),             False)
test("tiene_duplicado([1,2,2])",         tiene_duplicado([1, 2, 2]),             True)
test("tiene_duplicado([7,7,7])",         tiene_duplicado([7, 7, 7]),             True)

print(f"\n{'='*35}")
print(f"Resultado: {varOcg - failed}/{varOcg} pasados")
if failed == 0:
    print("¡Perfecto! Todos los tests pasaron.")
else:
    print(f"Tienes {failed} test(s) por corregir.")
