import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from desafio import filtrar_mayores, contar_palabras, top_n_frecuentes, agrupar_por_longitud

test_count = 0
failed_tests = 0

def test(name, result, expected):
    global test_count, failed_tests
    test_count += 1
    if result == expected:
        print(f"✓ PASS [{test_count}]: {name}")
    else:
        failed_tests += 1
        print(f"✗ FAIL [{test_count}]: {name}")
        print(f"   Esperado: {expected}")
        print(f"   Obtenido: {result}")

print("=== NIVEL 1: Warmup - Estructuras de Datos ===\n")

# filtrar_mayores
test("filtrar_mayores básico", filtrar_mayores([1, 5, 3, 8, 2], 4), [5, 8])
test("filtrar_mayores vacío", filtrar_mayores([], 4), [])
test("filtrar_mayores sin mayores", filtrar_mayores([1, 2, 3], 10), [])
test("filtrar_mayores umbral exacto (no incluye igual)", filtrar_mayores([4, 5, 6], 4), [5, 6])

# contar_palabras
test("contar_palabras básico", contar_palabras("hola mundo hola"), {"hola": 2, "mundo": 1})
test("contar_palabras case-insensitive", contar_palabras("Hola hola HOLA"), {"hola": 3})
test("contar_palabras vacío", contar_palabras(""), {})
test("contar_palabras una palabra", contar_palabras("python"), {"python": 1})

# top_n_frecuentes
freq = {"manzana": 3, "banana": 3, "cereza": 1, "durazno": 2}
test("top_n_frecuentes n=2", top_n_frecuentes(freq, 2),
     [{"elemento": "manzana", "frecuencia": 3}, {"elemento": "banana", "frecuencia": 3}])
test("top_n_frecuentes n=1", top_n_frecuentes({"a": 5, "b": 3}, 1),
     [{"elemento": "a", "frecuencia": 5}])

# agrupar_por_longitud
test("agrupar_por_longitud básico",
     agrupar_por_longitud(["hola", "hi", "mundo", "yo", "python"]),
     {4: ["hola"], 2: ["hi", "yo"], 5: ["mundo"], 6: ["python"]})
test("agrupar_por_longitud vacío", agrupar_por_longitud([]), {})

total = test_count
print(f"\n{'='*45}")
print(f"Resultado: {total - failed_tests}/{total} pasados")
if failed_tests == 0:
    print("¡Excelente! Todos los tests pasaron.")
else:
    print(f"Tienes {failed_tests} test(s) por corregir.")
