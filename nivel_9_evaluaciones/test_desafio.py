import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from desafio import promedio_por_curso, clasificar_estudiantes, analisis_por_departamento

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

print("=== NIVEL 9: Evaluaciones CSV ===\n")

# -------------------------------------------------------
# promedio_por_curso
# -------------------------------------------------------
print("-- promedio_por_curso('evaluaciones.csv') --")
res_prom = promedio_por_curso("evaluaciones.csv")

test_partial("retorna dict", isinstance(res_prom, dict))
test_partial("tiene los 4 cursos",
             set(res_prom.keys()) == {"MAT101","FIS101","INF101","HUM101"})
test("promedio MAT101 (85+92+71)/3 = 82.67", res_prom.get("MAT101"), 82.67)
test("promedio FIS101 (67+78+82)/3 = 75.67", res_prom.get("FIS101"), 75.67)
test("promedio INF101 (95+88+90)/3 = 91.0",  res_prom.get("INF101"), 91.0)
test("promedio HUM101 (76+88+65)/3 = 76.33", res_prom.get("HUM101"), 76.33)

# -------------------------------------------------------
# clasificar_estudiantes
# -------------------------------------------------------
print("\n-- clasificar_estudiantes('evaluaciones.csv', 70) --")
res_clas = clasificar_estudiantes("evaluaciones.csv", 70)

test_partial("retorna dict", isinstance(res_clas, dict))
test_partial("tiene los 3 estudiantes",
             set(res_clas.keys()) == {"juan","maria","pedro"})
# juan: MAT=85✓ FIS=67✗ → reprobado
test("juan reprueba (FIS101=67 < 70)", res_clas.get("juan"),  "reprobado")
# maria: MAT=92 FIS=82 INF=95 HUM=88 → todas >= 70
test("maria aprueba (todas >= 70)",    res_clas.get("maria"), "aprobado")
# pedro: FIS=78 INF=88 MAT=71 HUM=65✗ → reprobado
test("pedro reprueba (HUM101=65 < 70)", res_clas.get("pedro"), "reprobado")

print("\n-- clasificar_estudiantes('evaluaciones.csv', 80) --")
res_clas2 = clasificar_estudiantes("evaluaciones.csv", 80)
# juan: MAT=85✓ FIS=67✗ → reprobado
# maria: MAT=92 FIS=82 INF=95 HUM=88 → aprobado
# pedro: FIS=78✗ → reprobado
test("juan reprueba con umbral 80",  res_clas2.get("juan"),  "reprobado")
test("maria aprueba con umbral 80",  res_clas2.get("maria"), "aprobado")
test("pedro reprueba con umbral 80", res_clas2.get("pedro"), "reprobado")

# -------------------------------------------------------
# analisis_por_departamento
# -------------------------------------------------------
print("\n-- analisis_por_departamento('evaluaciones.csv', 'cursos.csv') --")
res_dep = analisis_por_departamento("evaluaciones.csv", "cursos.csv")

test_partial("retorna dict", isinstance(res_dep, dict))
test_partial("tiene los 4 departamentos",
             set(res_dep.keys()) == {"Matematicas","Ciencias","Informatica","Humanidades"})
test("Matematicas  = 82.67", res_dep.get("Matematicas"),  82.67)
test("Ciencias     = 75.67", res_dep.get("Ciencias"),     75.67)
test("Informatica  = 91.0",  res_dep.get("Informatica"),  91.0)
test("Humanidades  = 76.33", res_dep.get("Humanidades"),  76.33)

total = test_count
print(f"\n{'='*45}")
print(f"Resultado: {total - failed_tests}/{total} pasados")
if failed_tests == 0:
    print("¡Excelente! Todos los tests pasaron.")
else:
    print(f"Tienes {failed_tests} test(s) por corregir.")
