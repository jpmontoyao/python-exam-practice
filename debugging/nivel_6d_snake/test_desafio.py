import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from desafio import mover, estado

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

print("=== NIVEL 6d: Snake ===\n")

# mover
test("mover derecha",
     mover([(2,2),(2,1),(2,0)], 'R'),
     [(2,3),(2,2),(2,1)])

test("mover arriba",
     mover([(2,2),(3,2)], 'U'),
     [(1,2),(2,2)])

test("mover izquierda",
     mover([(2,2),(2,3)], 'L'),
     [(2,1),(2,2)])

test("mover abajo",
     mover([(1,2),(0,2)], 'D'),
     [(2,2),(1,2)])

# estado
test("continuar normal",
     estado([(2,2),(2,1)], 5, 5, (0,0)),
     'continuar')

test("victoria — come comida",
     estado([(2,2),(2,1)], 5, 5, (2,2)),
     'victoria')

test("derrota — pared derecha",
     estado([(2,5),(2,4)], 5, 5, (0,0)),
     'derrota')

test("derrota — pared arriba",
     estado([(-1,2),(0,2)], 5, 5, (0,0)),
     'derrota')

test("derrota — choca consigo misma",
     estado([(2,2),(2,3),(2,4),(2,2)], 5, 5, (0,0)),
     'derrota')

test("continuar — serpiente larga sin colisión",
     estado([(0,0),(0,1),(0,2)], 5, 5, (4,4)),
     'continuar')

print(f"\n{'='*35}")
print(f"Resultado: {varOcg - failed}/{varOcg} pasados")
if failed == 0:
    print("¡Perfecto! Todos los tests pasaron.")
else:
    print(f"Tienes {failed} test(s) por corregir.")
