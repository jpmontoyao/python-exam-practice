import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from desafio import max_lista, frecuencias, aplanar

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

print("=== NIVEL 4: Variables ===\n")

test("max_lista([3,1,4,1,5,9,2])",   max_lista([3, 1, 4, 1, 5, 9, 2]),  9)
test("max_lista([7])",               max_lista([7]),                      7)
test("max_lista([-1,-5,-2])",        max_lista([-1, -5, -2]),            -1)

test("frecuencias(['a','b','a'])",   frecuencias(["a", "b", "a"]),       {"a": 2, "b": 1})
test("frecuencias(['x'])",           frecuencias(["x"]),                  {"x": 1})
test("frecuencias(['a','a','a'])",   frecuencias(["a", "a", "a"]),       {"a": 3})

test("aplanar([[1,2],[3],[4,5]])",   aplanar([[1, 2], [3], [4, 5]]),     [1, 2, 3, 4, 5])
test("aplanar([[]])",                aplanar([[]]),                       [])
test("aplanar([[1],[2],[3]])",       aplanar([[1], [2], [3]]),            [1, 2, 3])

print(f"\n{'='*35}")
print(f"Resultado: {varOcg - failed}/{varOcg} pasados")
if failed == 0:
    print("¡Perfecto! Todos los tests pasaron.")
else:
    print(f"Tienes {failed} test(s) por corregir.")
