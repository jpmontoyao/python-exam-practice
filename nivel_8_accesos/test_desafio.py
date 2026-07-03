import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from desafio import accesos_por_hora, duracion_promedio_por_accion, usuarios_activos_por_fecha

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

print("=== NIVEL 8: Accesos CSV ===\n")

# -------------------------------------------------------
# accesos_por_hora
# -------------------------------------------------------
print("-- accesos_por_hora('accesos.csv') --")
res_hora = accesos_por_hora("accesos.csv")

test_partial("retorna dict", isinstance(res_hora, dict))
test("hora 09 tiene 3 accesos",  res_hora.get("09"), 3)
test("hora 08 tiene 2 accesos",  res_hora.get("08"), 2)
test("hora 14 tiene 2 accesos",  res_hora.get("14"), 2)
test("hora 10 tiene 1 acceso",   res_hora.get("10"), 1)
test("hora 11 tiene 1 acceso",   res_hora.get("11"), 1)
test("hora 13 tiene 1 acceso",   res_hora.get("13"), 1)
test("resultado completo",
     res_hora, {"08": 2, "09": 3, "10": 1, "11": 1, "13": 1, "14": 2})
test_partial("claves son strings de 2 dígitos",
             all(isinstance(k, str) and len(k) == 2 for k in res_hora),
             f"claves: {list(res_hora.keys())}")

# -------------------------------------------------------
# duracion_promedio_por_accion
# -------------------------------------------------------
print("\n-- duracion_promedio_por_accion('accesos.csv') --")
res_dur = duracion_promedio_por_accion("accesos.csv")

test_partial("retorna dict", isinstance(res_dur, dict))
test("promedio login    (2+1+3+1)/4 = 1.75",  res_dur.get("login"),    1.75)
test("promedio descarga (15+22+18)/3 = 18.33", res_dur.get("descarga"), 18.33)
test("promedio consulta (8+12+6)/3 = 8.67",    res_dur.get("consulta"), 8.67)
test_partial("tiene exactamente 3 acciones",
             set(res_dur.keys()) == {"login", "descarga", "consulta"})

# -------------------------------------------------------
# usuarios_activos_por_fecha
# -------------------------------------------------------
print("\n-- usuarios_activos_por_fecha('accesos.csv') --")
res_fecha = usuarios_activos_por_fecha("accesos.csv")

test_partial("retorna dict", isinstance(res_fecha, dict))
test("2024-03-01 tiene 3 usuarios distintos", res_fecha.get("2024-03-01"), 3)
test("2024-03-02 tiene 3 usuarios distintos", res_fecha.get("2024-03-02"), 3)
test("resultado completo",
     res_fecha, {"2024-03-01": 3, "2024-03-02": 3})

total = test_count
print(f"\n{'='*45}")
print(f"Resultado: {total - failed_tests}/{total} pasados")
if failed_tests == 0:
    print("¡Excelente! Todos los tests pasaron.")
else:
    print(f"Tienes {failed_tests} test(s) por corregir.")
