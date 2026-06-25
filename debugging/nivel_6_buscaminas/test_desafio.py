import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from desafio import solution
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
        print(f"   Esperado:  {esperado}")
        print(f"   Obtenido:  {resultado}")

print("=== NIVEL 6: Buscaminas ===\n")

field1 = [[False, True,  True],
          [True,  False, True],
          [False, False, True]]
test("click en centro, 5 minas vecinas",
     solution(field1, 1, 1),
     [[-1, -1, -1], [-1, 5, -1], [-1, -1, -1]])

field2 = [[True,  False, True,  True,  False],
          [True,  False, False, False, False],
          [False, False, False, False, False],
          [True,  False, False, False, False]]
test("BFS se expande por ceros",
     solution(field2, 3, 2),
     [[-1, -1, -1, -1, -1],
      [-1,  3,  2,  2,  1],
      [-1,  2,  0,  0,  0],
      [-1,  1,  0,  0,  0]])

field3 = [[False, False, False],
          [False, False, False],
          [False, False, False]]
test("campo sin minas, todo se revela",
     solution(field3, 0, 0),
     [[0, 0, 0], [0, 0, 0], [0, 0, 0]])

field4 = [[True,  False],
          [False, True]]
test("solo se revela la celda clickeada",
     solution(field4, 0, 1),
     [[-1, 2], [-1, -1]])

print(f"\n{'='*35}")
print(f"Resultado: {varOcg - failed}/{varOcg} pasados")
if failed == 0:
    print("¡Perfecto! Todos los tests pasaron.")
else:
    print(f"Tienes {failed} test(s) por corregir.")
