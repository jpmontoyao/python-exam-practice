import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from desafio import corregir_negativos, agregar_columnas, limpiar_completo
import pandas as pd

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

print("=== PANDAS NIVEL 2: Limpieza ===\n")

# -------------------------------------------------------
# corregir_negativos
# -------------------------------------------------------
print("-- corregir_negativos --")
try:
    df_orig = pd.read_csv(PATH, encoding='utf-8')
    df_clean = corregir_negativos(df_orig.copy())
    test_partial("retorna DataFrame", isinstance(df_clean, pd.DataFrame))
    test_partial("no quedan Multas negativas",
                 all(df_clean['Multas'] >= 0))
    test_partial("no quedan Dias_Atraso negativos",
                 all(df_clean['Dias_Atraso'] >= 0))
    test("suma Multas tras corrección = 4000",
         int(df_clean['Multas'].sum()), 4000)
    test("suma Dias_Atraso tras corrección = 20",
         int(df_clean['Dias_Atraso'].sum()), 20)
except Exception as e:
    print(f"  [ERROR] {e}")

# -------------------------------------------------------
# agregar_columnas
# -------------------------------------------------------
print("\n-- agregar_columnas --")
try:
    df_base = pd.read_csv(PATH, encoding='utf-8')
    df_cols = agregar_columnas(df_base.copy())
    test_partial("tiene columna 'comuna_key'", 'comuna_key' in df_cols.columns)
    test_partial("tiene columna 'Tipo_Dia'",   'Tipo_Dia'   in df_cols.columns)
    test("primera fila: comuna_key = 'santiago'",
         df_cols.at[0, 'comuna_key'], 'santiago')
    test("primera fila: Tipo_Dia = DÍA_HÁBIL (lunes 2024/03/04)",
         df_cols.at[0, 'Tipo_Dia'], 'DÍA_HÁBIL')
    test("fila 2: Tipo_Dia = FIN_DE_SEMANA (sábado 2024/03/09)",
         df_cols.at[2, 'Tipo_Dia'], 'FIN_DE_SEMANA')
    test("fila 7: Tipo_Dia = FIN_DE_SEMANA (domingo 2024/04/07)",
         df_cols.at[7, 'Tipo_Dia'], 'FIN_DE_SEMANA')
    fin_sem = (df_cols['Tipo_Dia'] == 'FIN_DE_SEMANA').sum()
    test("total FIN_DE_SEMANA = 9",  int(fin_sem), 9)
    test("total DÍA_HÁBIL = 11",
         int((df_cols['Tipo_Dia'] == 'DÍA_HÁBIL').sum()), 11)
except Exception as e:
    print(f"  [ERROR] {e}")

# -------------------------------------------------------
# limpiar_completo
# -------------------------------------------------------
print("\n-- limpiar_completo --")
try:
    df_raw = pd.read_csv(PATH, encoding='utf-8')
    df_listo = limpiar_completo(df_raw.copy())
    test_partial("sin negativos en Multas",      all(df_listo['Multas'] >= 0))
    test_partial("sin negativos en Dias_Atraso", all(df_listo['Dias_Atraso'] >= 0))
    test_partial("tiene 'comuna_key'", 'comuna_key' in df_listo.columns)
    test_partial("tiene 'Tipo_Dia'",   'Tipo_Dia'   in df_listo.columns)
    test("suma Multas limpio = 4000",
         int(df_listo['Multas'].sum()), 4000)
    test("total FIN_DE_SEMANA en df limpio = 9",
         int((df_listo['Tipo_Dia'] == 'FIN_DE_SEMANA').sum()), 9)
except Exception as e:
    print(f"  [ERROR] {e}")

total = test_count
print(f"\n{'='*45}")
print(f"Resultado: {total - failed_tests}/{total} pasados")
if failed_tests == 0:
    print("¡Excelente! Todos los tests pasaron.")
else:
    print(f"Tienes {failed_tests} test(s) por corregir.")
