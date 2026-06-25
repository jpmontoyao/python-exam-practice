import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from desafio import top_palabras, agrupar_pares_impares, invertir_dict
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

print("=== NIVEL 5: Combinado ===\n")

test("top_palabras n=2",
     top_palabras("hola mundo hola python mundo hola", 2),
     ["hola", "mundo"])
test("top_palabras n=1",
     top_palabras("sol luna sol", 1),
     ["sol"])
test("top_palabras case-insensitive",
     top_palabras("Hola hola HOLA", 1),
     ["hola"])

test("agrupar_pares_impares([1,2,3,4])",
     agrupar_pares_impares([1, 2, 3, 4]),
     {"pares": [2, 4], "impares": [1, 3]})
test("agrupar_pares_impares([2,4,6])",
     agrupar_pares_impares([2, 4, 6]),
     {"pares": [2, 4, 6], "impares": []})
test("agrupar_pares_impares([])",
     agrupar_pares_impares([]),
     {"pares": [], "impares": []})

test("invertir_dict({'a':1,'b':2})",
     invertir_dict({"a": 1, "b": 2}),
     {1: "a", 2: "b"})
test("invertir_dict({'x':10})",
     invertir_dict({"x": 10}),
     {10: "x"})

print(f"\n{'='*35}")
print(f"Resultado: {varOcg - failed}/{varOcg} pasados")
if failed == 0:
    print("¡Perfecto! Todos los tests pasaron.")
else:
    print(f"Tienes {failed} test(s) por corregir.")
