import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from desafio import flood_fill

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

print("=== NIVEL 5i: Flood Fill ===\n")

test("rellenar región esquina",
     flood_fill([[1,1,1],[1,2,2],[1,2,2]], 0, 0, 3),
     [[3,3,3],[3,2,2],[3,2,2]])

test("rellenar región interior",
     flood_fill([[1,1,1],[1,2,2],[1,2,2]], 1, 1, 3),
     [[1,1,1],[1,3,3],[1,3,3]])

test("imagen uniforme — todo cambia",
     flood_fill([[2,2],[2,2]], 0, 0, 5),
     [[5,5],[5,5]])

test("color nuevo igual al original — no cambia nada",
     flood_fill([[1,1],[1,1]], 0, 0, 1),
     [[1,1],[1,1]])

test("región con forma irregular",
     flood_fill([[1,2,1],[1,1,1],[1,2,1]], 0, 0, 9),
     [[9,2,9],[9,9,9],[9,2,9]])

test("celda aislada",
     flood_fill([[1,2,1],[2,2,2],[1,2,1]], 0, 0, 5),
     [[5,2,1],[2,2,2],[1,2,1]])

print(f"\n{'='*35}")
print(f"Resultado: {varOcg - failed}/{varOcg} pasados")
if failed == 0:
    print("¡Perfecto! ¡Listo para el buscaminas!")
else:
    print(f"Tienes {failed} test(s) por corregir.")
