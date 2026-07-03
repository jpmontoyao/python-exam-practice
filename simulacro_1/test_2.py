import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from desafio_2 import reproducciones_por_hora, duracion_total_por_fecha, artista_mas_escuchado_por_dia

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

print("=== SIMULACRO 1 — Desafio 2: Analisis Temporal ===\n")

# -------------------------------------------------------
# reproducciones_por_hora
# -------------------------------------------------------
print("-- reproducciones_por_hora('reproducciones.csv') --")
res_hora = reproducciones_por_hora("reproducciones.csv")

test_partial("retorna dict", isinstance(res_hora, dict))
test_partial("las claves son strings de 2 digitos",
             all(isinstance(k, str) and len(k) == 2 for k in res_hora))
test("hora 08: 2 reproducciones", res_hora.get("08"), 2)
test("hora 09: 3 reproducciones", res_hora.get("09"), 3)
test("hora 10: 3 reproducciones", res_hora.get("10"), 3)
test("hora 11: 2 reproducciones", res_hora.get("11"), 2)
test("hora 14: 2 reproducciones", res_hora.get("14"), 2)
test("hora 15: 1 reproduccion",   res_hora.get("15"), 1)
test("hora 16: 1 reproduccion",   res_hora.get("16"), 1)
test("hora 17: 1 reproduccion",   res_hora.get("17"), 1)

# -------------------------------------------------------
# duracion_total_por_fecha
# -------------------------------------------------------
print("\n-- duracion_total_por_fecha('reproducciones.csv') --")
res_dur = duracion_total_por_fecha("reproducciones.csv")

test_partial("retorna dict", isinstance(res_dur, dict))
test_partial("tiene las 3 fechas",
             set(res_dur.keys()) == {"2024-05-01", "2024-05-02", "2024-05-03"})
test("2024-05-01: 1243 seg", res_dur.get("2024-05-01"), 1243)
test("2024-05-02: 1590 seg", res_dur.get("2024-05-02"), 1590)
test("2024-05-03: 1228 seg", res_dur.get("2024-05-03"), 1228)

# -------------------------------------------------------
# artista_mas_escuchado_por_dia
# -------------------------------------------------------
print("\n-- artista_mas_escuchado_por_dia('reproducciones.csv') --")
res_art = artista_mas_escuchado_por_dia("reproducciones.csv")

test_partial("retorna dict", isinstance(res_art, dict))
test_partial("tiene las 3 fechas",
             set(res_art.keys()) == {"2024-05-01", "2024-05-02", "2024-05-03"})
# 2024-05-01: Daddy Yankee 2x, resto 1x
test("2024-05-01: Daddy Yankee (2 repros)", res_art.get("2024-05-01"), "Daddy Yankee")
# 2024-05-02: Led Zeppelin 2x (Stairway x2), resto 1x
test("2024-05-02: Led Zeppelin (2 repros)", res_art.get("2024-05-02"), "Led Zeppelin")
# 2024-05-03: Daddy Yankee 2x (Con Calma + Gasolina), resto 1x
test("2024-05-03: Daddy Yankee (2 repros)", res_art.get("2024-05-03"), "Daddy Yankee")

total = test_count
print(f"\n{'='*45}")
print(f"Resultado: {total - failed_tests}/{total} pasados")
if failed_tests == 0:
    print("¡Excelente! Todos los tests pasaron.")
else:
    print(f"Tienes {failed_tests} test(s) por corregir.")
