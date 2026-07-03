import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from desafio import construir_stats, ranking_libros
import pandas as pd
from datetime import datetime

test_count = 0
failed_tests = 0

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH = os.path.join(BASE, "datos", "bibliotecas.csv")

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

# Preparar df limpio para los tests (el test lo hace por ti)
df = pd.read_csv(PATH, encoding='utf-8')
for i, row in df.iterrows():
    for col in ['Multas', 'Dias_Atraso']:
        if int(row[col]) < 0:
            df.at[i, col] = 0
    df.at[i, 'comuna_key'] = row['COMUNA'].strip().lower()
    d = datetime.strptime(str(row['Fecha']), '%Y/%m/%d')
    df.at[i, 'Tipo_Dia'] = 'FIN_DE_SEMANA' if d.weekday() >= 5 else 'DÍA_HÁBIL'

print("=== PANDAS NIVEL 3: Stats por comuna ===\n")

# -------------------------------------------------------
# construir_stats
# -------------------------------------------------------
print("-- construir_stats --")
try:
    stats = construir_stats(df)
    test_partial("retorna dict", isinstance(stats, dict))
    test_partial("tiene 3 comunas",
                 isinstance(stats, dict) and set(stats.keys()) == {'santiago', 'maipú', 'viña del mar'})

    s = stats.get('santiago', {}) if isinstance(stats, dict) else {}
    test("santiago: nombre_comuna = 'Santiago'", s.get('nombre_comuna'), 'Santiago')
    test("santiago: cod_region = 13",            s.get('cod_region'),    13)
    test("santiago: libros_total = 17",          s.get('libros_total'),  17)
    test("santiago: multas_total = 1500",        s.get('multas_total'),  1500)
    test("santiago: registros_fin_semana = 2",   s.get('registros_fin_semana'), 2)
    test("santiago: total_registros = 8",        s.get('total_registros'), 8)
    test("santiago: registros_por_mes = {3:2, 4:2, 5:2, 6:2}",
         s.get('registros_por_mes'), {3: 2, 4: 2, 5: 2, 6: 2})

    m = stats.get('maipú', {}) if isinstance(stats, dict) else {}
    test("maipú: libros_total = 14",         m.get('libros_total'), 14)
    test("maipú: multas_total = 500",        m.get('multas_total'), 500)
    test("maipú: registros_fin_semana = 5",  m.get('registros_fin_semana'), 5)
    test("maipú: registros_por_mes = {3:2, 4:1, 5:2, 6:1}",
         m.get('registros_por_mes'), {3: 2, 4: 1, 5: 2, 6: 1})

    v = stats.get('viña del mar', {}) if isinstance(stats, dict) else {}
    test("viña del mar: libros_total = 12",         v.get('libros_total'), 12)
    test("viña del mar: multas_total = 2000",       v.get('multas_total'), 2000)
    test("viña del mar: registros_fin_semana = 2",  v.get('registros_fin_semana'), 2)
    test("viña del mar: registros_por_mes = {3:1, 4:2, 5:1, 6:2}",
         v.get('registros_por_mes'), {3: 1, 4: 2, 5: 1, 6: 2})
except Exception as e:
    print(f"  [ERROR] {e}")

# -------------------------------------------------------
# ranking_libros
# -------------------------------------------------------
print("\n-- ranking_libros --")
try:
    ranking = ranking_libros(stats)
    test_partial("retorna lista", isinstance(ranking, list))
    test_partial("tiene 3 elementos", isinstance(ranking, list) and len(ranking) == 3)
    test("1ro: Santiago (17 libros)",
         ranking[0].get('comuna') if ranking else None, 'Santiago')
    test("2do: Maipú (14 libros)",
         ranking[1].get('comuna') if len(ranking) > 1 else None, 'Maipú')
    test("3ro: Viña del Mar (12 libros)",
         ranking[2].get('comuna') if len(ranking) > 2 else None, 'Viña del Mar')
    test("ordenado desc: 17 >= 14 >= 12",
         [r['libros_total'] for r in ranking] if ranking else [],
         [17, 14, 12])
except Exception as e:
    print(f"  [ERROR] {e}")

total = test_count
print(f"\n{'='*45}")
print(f"Resultado: {total - failed_tests}/{total} pasados")
if failed_tests == 0:
    print("¡Excelente! Todos los tests pasaron.")
else:
    print(f"Tienes {failed_tests} test(s) por corregir.")
