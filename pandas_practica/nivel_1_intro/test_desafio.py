import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from desafio import cargar_datos, contar_por_tipo_usuario, total_libros_por_mes

test_count = 0
failed_tests = 0

BASE  = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH  = os.path.join(BASE, "datos", "bibliotecas.csv")

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

def test_partial(name, condition, detail=""):
    global test_count, failed_tests
    test_count += 1
    if condition:
        print(f"✓ PASS [{test_count}]: {name}")
    else:
        failed_tests += 1
        print(f"✗ FAIL [{test_count}]: {name}")
        if detail:
            print(f"   Detalle: {detail}")

print("=== PANDAS NIVEL 1: Introducción ===\n")

# -------------------------------------------------------
# cargar_datos
# -------------------------------------------------------
print("-- cargar_datos --")
try:
    import pandas as pd
    df = cargar_datos(PATH)
    test_partial("retorna DataFrame", isinstance(df, pd.DataFrame))
    test("20 filas",    len(df), 20)
    test("10 columnas", len(df.columns), 10)
    test_partial("tiene columna COMUNA",       "COMUNA"          in df.columns)
    test_partial("tiene columna Libros_Prestados", "Libros_Prestados" in df.columns)
except Exception as e:
    print(f"  [ERROR] {e}")

# -------------------------------------------------------
# contar_por_tipo_usuario
# -------------------------------------------------------
print("\n-- contar_por_tipo_usuario --")
try:
    res_tipo = contar_por_tipo_usuario(df)
    test_partial("retorna dict", isinstance(res_tipo, dict))
    test_partial("tiene 2 tipos", set(res_tipo.keys()) == {"Estudiante", "Adulto"})
    test("Estudiante: 11", res_tipo.get("Estudiante"), 11)
    test("Adulto: 9",      res_tipo.get("Adulto"),      9)
except Exception as e:
    print(f"  [ERROR] {e}")

# -------------------------------------------------------
# total_libros_por_mes
# -------------------------------------------------------
print("\n-- total_libros_por_mes --")
try:
    res_mes = total_libros_por_mes(df)
    test_partial("retorna dict", isinstance(res_mes, dict))
    test_partial("tiene 4 meses", set(res_mes.keys()) == {3, 4, 5, 6})
    test("Mes 3: 12 libros", res_mes.get(3), 12)
    test("Mes 4: 10 libros", res_mes.get(4), 10)
    test("Mes 5: 12 libros", res_mes.get(5), 12)
    test("Mes 6:  9 libros", res_mes.get(6),  9)
except Exception as e:
    print(f"  [ERROR] {e}")

total = test_count
print(f"\n{'='*45}")
print(f"Resultado: {total - failed_tests}/{total} pasados")
if failed_tests == 0:
    print("¡Excelente! Todos los tests pasaron.")
else:
    print(f"Tienes {failed_tests} test(s) por corregir.")
