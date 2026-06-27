import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from desafio import siguiente_generacion
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

T = True
F = False

print("=== NIVEL 5c: Juego de la Vida ===\n")

# Tablero muerto — nada cambia
test("tablero muerto",
     siguiente_generacion([[F, F],
                           [F, F]]),
     [[F, F],
      [F, F]])

# Block (still life) — un cuadrado 2x2 vivo no cambia
test("block — still life",
     siguiente_generacion([[F, F, F, F],
                           [F, T, T, F],
                           [F, T, T, F],
                           [F, F, F, F]]),
     [[F, F, F, F],
      [F, T, T, F],
      [F, T, T, F],
      [F, F, F, F]])

# Blinker horizontal → blinker vertical
test("blinker horizontal → vertical",
     siguiente_generacion([[F, F, F],
                           [T, T, T],
                           [F, F, F]]),
     [[F, T, F],
      [F, T, F],
      [F, T, F]])

# Blinker vertical → blinker horizontal
test("blinker vertical → horizontal",
     siguiente_generacion([[F, T, F],
                           [F, T, F],
                           [F, T, F]]),
     [[F, F, F],
      [T, T, T],
      [F, F, F]])

# Celda sola muere (menos de 2 vecinos)
test("celda sola muere",
     siguiente_generacion([[F, F, F],
                           [F, T, F],
                           [F, F, F]]),
     [[F, F, F],
      [F, F, F],
      [F, F, F]])

print(f"\n{'='*35}")
print(f"Resultado: {varOcg - failed}/{varOcg} pasados")
if failed == 0:
    print("¡Perfecto! Ya estás listo para el boss.")
else:
    print(f"Tienes {failed} test(s) por corregir.")
