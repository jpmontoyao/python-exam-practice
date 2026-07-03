import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from desafio import evaluar_postfix

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

print("=== NIVEL 5d: Evaluador Postfijo ===\n")

test('"3 4 +"  → 7',          evaluar_postfix("3 4 +"),          7)
test('"5 3 -"  → 2',          evaluar_postfix("5 3 -"),          2)
test('"3 4 *"  → 12',         evaluar_postfix("3 4 *"),          12)
test('"8 4 /"  → 2.0',        evaluar_postfix("8 4 /"),          2.0)
test('"3 4 + 2 *" → 14',      evaluar_postfix("3 4 + 2 *"),      14)
test('"5 1 2 + 4 * + 3 -" → 14', evaluar_postfix("5 1 2 + 4 * + 3 -"), 14)
test('"10 2 /" → 5.0',        evaluar_postfix("10 2 /"),         5.0)

print(f"\n{'='*35}")
print(f"Resultado: {varOcg - failed}/{varOcg} pasados")
if failed == 0:
    print("¡Perfecto! Todos los tests pasaron.")
else:
    print(f"Tienes {failed} test(s) por corregir.")
