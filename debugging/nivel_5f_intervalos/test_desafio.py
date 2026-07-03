import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from desafio import fusionar_intervalos

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

print("=== NIVEL 5f: Fusión de Intervalos ===\n")

test("solapamiento simple",
     fusionar_intervalos([(1,3),(2,5),(7,9)]),
     [(1,5),(7,9)])

test("intervalos que se tocan en el borde",
     fusionar_intervalos([(1,2),(2,3)]),
     [(1,3)])

test("desordenados que resultan en uno",
     fusionar_intervalos([(1,4),(5,7),(3,6)]),
     [(1,7)])

test("sin solapamiento",
     fusionar_intervalos([(1,2),(3,4),(5,6)]),
     [(1,2),(3,4),(5,6)])

test("uno contiene al otro",
     fusionar_intervalos([(1,10),(2,3)]),
     [(1,10)])

test("lista vacía",
     fusionar_intervalos([]),
     [])

test("un solo intervalo",
     fusionar_intervalos([(3,7)]),
     [(3,7)])

print(f"\n{'='*35}")
print(f"Resultado: {varOcg - failed}/{varOcg} pasados")
if failed == 0:
    print("¡Perfecto! Todos los tests pasaron.")
else:
    print(f"Tienes {failed} test(s) por corregir.")
