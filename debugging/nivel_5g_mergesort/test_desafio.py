import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from desafio import merge, merge_sort

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

print("=== NIVEL 5g: Merge Sort ===\n")

# merge directo
test("merge básico",          merge([1,3,5],[2,4,6]),    [1,2,3,4,5,6])
test("merge izq vacía",       merge([],[1,2,3]),          [1,2,3])
test("merge der vacía",       merge([1,2,3],[]),          [1,2,3])
test("merge con duplicados",  merge([1,2,2],[2,3]),       [1,2,2,2,3])

# merge_sort completo
test("sort básico",           merge_sort([5,2,8,1,9]),   [1,2,5,8,9])
test("sort ya ordenado",      merge_sort([1,2,3,4,5]),   [1,2,3,4,5])
test("sort invertido",        merge_sort([5,4,3,2,1]),   [1,2,3,4,5])
test("sort un elemento",      merge_sort([7]),            [7])
test("sort vacío",            merge_sort([]),             [])
test("sort con duplicados",   merge_sort([3,1,2,1,3]),   [1,1,2,3,3])

print(f"\n{'='*35}")
print(f"Resultado: {varOcg - failed}/{varOcg} pasados")
if failed == 0:
    print("¡Perfecto! Todos los tests pasaron.")
else:
    print(f"Tienes {failed} test(s) por corregir.")
