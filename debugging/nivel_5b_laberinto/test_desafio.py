import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from desafio import resolver_laberinto
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

print("=== NIVEL 5b: Laberinto ===\n")

# Camino directo de 2 pasos
test("camino recto 2 pasos",
     resolver_laberinto(["S.E"]),
     2)

# Camino en L
test("camino en L",
     resolver_laberinto(["S.",
                         ".E"]),
     2)

# Laberinto con obstáculo, rodear por abajo
test("rodear obstáculo — 4 pasos",
     resolver_laberinto(["S##",
                         "...",
                         "..E"]),
     4)

# Sin camino — pared total
test("sin camino",
     resolver_laberinto(["S#",
                         "#E"]),
     -1)

# Laberinto más largo
test("laberinto largo — 10 pasos",
     resolver_laberinto(["S....",
                         "####.",
                         "E...."]),
     10)

print(f"\n{'='*35}")
print(f"Resultado: {varOcg - failed}/{varOcg} pasados")
if failed == 0:
    print("¡Perfecto! Ya estás listo para el boss.")
else:
    print(f"Tienes {failed} test(s) por corregir.")
