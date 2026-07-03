import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from desafio import insertar, en_orden, buscar

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

def construir(valores):
    raiz = None
    for v in valores:
        raiz = insertar(raiz, v)
    return raiz

print("=== NIVEL 6e: BST ===\n")

arbol = construir([5, 3, 7, 1, 4])

test("en_orden [5,3,7,1,4]",    en_orden(arbol),          [1, 3, 4, 5, 7])
test("en_orden árbol vacío",     en_orden(None),           [])
test("en_orden un nodo",         en_orden(construir([5])), [5])

test("buscar existente (3)",     buscar(arbol, 3),  True)
test("buscar existente (7)",     buscar(arbol, 7),  True)
test("buscar existente (1)",     buscar(arbol, 1),  True)
test("buscar inexistente (6)",   buscar(arbol, 6),  False)
test("buscar inexistente (0)",   buscar(arbol, 0),  False)
test("buscar en árbol vacío",    buscar(None, 5),   False)

arbol2 = construir([10, 5, 15, 3, 7, 12, 20])
test("en_orden árbol grande",
     en_orden(arbol2), [3, 5, 7, 10, 12, 15, 20])

print(f"\n{'='*35}")
print(f"Resultado: {varOcg - failed}/{varOcg} pasados")
if failed == 0:
    print("¡Perfecto! Todos los tests pasaron.")
else:
    print(f"Tienes {failed} test(s) por corregir.")
