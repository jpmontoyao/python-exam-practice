import sys, os, csv
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from desafio import (cargar_ventas, cargar_sucursales, limpiar_ventas,
                     construir_stats, ventas_por_mes, sucursales_eficientes,
                     calcular_ivs, clasificar_y_exportar)
import pandas as pd

test_count = 0
failed_tests = 0

BASE     = os.path.dirname(os.path.abspath(__file__))
PATH_V   = os.path.join(BASE, "ventas.csv")
PATH_S   = os.path.join(BASE, "sucursales.csv")
PATH_OUT = os.path.join(BASE, "ranking_ivs.csv")

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

print("=== PANDAS NIVEL 4: Pipeline Farmacias ===\n")

# -------------------------------------------------------
# cargar_ventas
# -------------------------------------------------------
print("-- cargar_ventas --")
try:
    df = cargar_ventas(PATH_V)
    test_partial("retorna DataFrame", isinstance(df, pd.DataFrame))
    test("20 filas",    len(df), 20)
    test("10 columnas", len(df.columns), 10)
except Exception as e:
    print(f"  [ERROR] {e}")

# -------------------------------------------------------
# cargar_sucursales
# -------------------------------------------------------
print("\n-- cargar_sucursales --")
try:
    pob = cargar_sucursales(PATH_S)
    test_partial("retorna dict", isinstance(pob, dict))
    test_partial("tiene 3 sucursales",
                 isinstance(pob, dict) and set(pob.keys()) == {'Santiago Centro', 'Maipú', 'Viña del Mar'})
    test("Santiago Centro: 404495",  pob.get('Santiago Centro'), 404495)
    test("Maipú: 586812",            pob.get('Maipú'),           586812)
    test("Viña del Mar: 330000",     pob.get('Viña del Mar'),    330000)
    test("valores son int",
         all(isinstance(v, int) for v in pob.values()) if isinstance(pob, dict) else False, True)
except Exception as e:
    print(f"  [ERROR] {e}")

# -------------------------------------------------------
# limpiar_ventas
# -------------------------------------------------------
print("\n-- limpiar_ventas --")
try:
    df_listo = limpiar_ventas(df.copy())
    test_partial("retorna DataFrame",              isinstance(df_listo, pd.DataFrame))
    test_partial("tiene columna 'sucursal_key'",  'sucursal_key' in df_listo.columns)
    test_partial("tiene columna 'Tipo_Dia'",      'Tipo_Dia'     in df_listo.columns)
    test_partial("tiene columna 'venta_total'",   'venta_total'  in df_listo.columns)
    test_partial("sin Descuento negativos",        all(df_listo['Descuento'] >= 0))
    test("FIN_DE_SEMANA = 13",
         int((df_listo['Tipo_Dia'] == 'FIN_DE_SEMANA').sum()), 13)
    test("Descuento total corregido = 2150",
         int(df_listo['Descuento'].sum()), 2150)
    test("venta_total fila 0 = 12500 (5*2500)",
         int(df_listo.at[0, 'venta_total']), 12500)
except Exception as e:
    print(f"  [ERROR] {e}")

# -------------------------------------------------------
# construir_stats
# -------------------------------------------------------
print("\n-- construir_stats --")
try:
    stats = construir_stats(df_listo, pob)
    test_partial("retorna dict", isinstance(stats, dict))
    test_partial("3 sucursales",
                 isinstance(stats, dict) and
                 set(stats.keys()) == {'santiago centro', 'maipú', 'viña del mar'})
    s = stats.get('santiago centro', {}) if isinstance(stats, dict) else {}
    test("santiago centro: ventas_total = 101800",    s.get('ventas_total'),      101800)
    test("santiago centro: unidades_total = 24",      s.get('unidades_total'),    24)
    test("santiago centro: poblacion = 404495",       s.get('poblacion'),         404495)
    test("santiago centro: total_registros = 7",      s.get('total_registros'),   7)
    test("santiago centro: ventas_fin_semana = 3",    s.get('ventas_fin_semana'), 3)
    test("santiago centro: ventas_por_mes",
         s.get('ventas_por_mes'), {1: 2, 2: 1, 3: 2, 4: 2})
    m = stats.get('maipú', {}) if isinstance(stats, dict) else {}
    test("maipú: ventas_total = 89900",   m.get('ventas_total'),   89900)
    test("maipú: unidades_total = 25",    m.get('unidades_total'), 25)
    test("maipú: poblacion = 586812",     m.get('poblacion'),      586812)
    v = stats.get('viña del mar', {}) if isinstance(stats, dict) else {}
    test("viña del mar: ventas_total = 85700",        v.get('ventas_total'),      85700)
    test("viña del mar: ventas_fin_semana = 6",       v.get('ventas_fin_semana'), 6)
    test("viña del mar: ventas_por_mes",
         v.get('ventas_por_mes'), {1: 2, 2: 1, 3: 2, 4: 2})
except Exception as e:
    print(f"  [ERROR] {e}")

# -------------------------------------------------------
# ventas_por_mes
# -------------------------------------------------------
print("\n-- ventas_por_mes --")
try:
    res_meses = ventas_por_mes(stats)
    test_partial("retorna dict", isinstance(res_meses, dict))
    test_partial("tiene 4 meses", isinstance(res_meses, dict) and len(res_meses) == 4)
    test_partial("cada entrada tiene 'total_registros' y 'es_peak'",
                 all('total_registros' in v and 'es_peak' in v
                     for v in res_meses.values()) if isinstance(res_meses, dict) else False)
    test("mes 1: 4 registros", res_meses.get(1, {}).get('total_registros'), 4)
    test("mes 2: 5 registros", res_meses.get(2, {}).get('total_registros'), 5)
    test("mes 3: 6 registros", res_meses.get(3, {}).get('total_registros'), 6)
    test("mes 4: 5 registros", res_meses.get(4, {}).get('total_registros'), 5)
    peaks = [m for m, v in res_meses.items() if v.get('es_peak')] if isinstance(res_meses, dict) else []
    test_partial("exactamente 1 mes peak", len(peaks) == 1)
    test("mes peak es el 3", peaks[0] if peaks else None, 3)
except Exception as e:
    print(f"  [ERROR] {e}")

# -------------------------------------------------------
# sucursales_eficientes
# -------------------------------------------------------
print("\n-- sucursales_eficientes --")
try:
    res_seg = sucursales_eficientes(stats)
    test_partial("retorna lista", isinstance(res_seg, list))
    test("1 sucursal eficiente", len(res_seg) if isinstance(res_seg, list) else -1, 1)
    test("es maipú",
         res_seg[0].get('sucursal') if res_seg else None, 'maipú')
    test("tasa_ventas maipú = 15320.07",
         res_seg[0].get('tasa_ventas') if res_seg else None, 15320.07)
    test("pct_fin_semana maipú = 66.67",
         res_seg[0].get('pct_fin_semana') if res_seg else None, 66.67)
except Exception as e:
    print(f"  [ERROR] {e}")

# -------------------------------------------------------
# calcular_ivs
# -------------------------------------------------------
print("\n-- calcular_ivs --")
try:
    lista_ivs = calcular_ivs(stats)
    test_partial("retorna lista", isinstance(lista_ivs, list))
    test_partial("tiene 3 elementos", isinstance(lista_ivs, list) and len(lista_ivs) == 3)
    test("1ro: viña del mar (IVS=25969.7)",
         lista_ivs[0].get('sucursal') if lista_ivs else None, 'viña del mar')
    test("2do: santiago centro (IVS=25167.18)",
         lista_ivs[1].get('sucursal') if len(lista_ivs) > 1 else None, 'santiago centro')
    test("3ro: maipú (IVS=15320.07)",
         lista_ivs[2].get('sucursal') if len(lista_ivs) > 2 else None, 'maipú')
    test("viña del mar IVS = 25969.7",   lista_ivs[0].get('ivs') if lista_ivs else None, 25969.7)
    test("santiago centro IVS = 25167.18", lista_ivs[1].get('ivs') if len(lista_ivs) > 1 else None, 25167.18)
    test("maipú IVS = 15320.07",         lista_ivs[2].get('ivs') if len(lista_ivs) > 2 else None, 15320.07)
    test("viña del mar pct_fin_semana = 85.71",
         lista_ivs[0].get('pct_fin_semana') if lista_ivs else None, 85.71)
    test("maipú pct_fin_semana = 66.67",
         lista_ivs[2].get('pct_fin_semana') if len(lista_ivs) > 2 else None, 66.67)
except Exception as e:
    print(f"  [ERROR] {e}")

# -------------------------------------------------------
# clasificar_y_exportar
# -------------------------------------------------------
print("\n-- clasificar_y_exportar --")
try:
    lista_cat = clasificar_y_exportar(lista_ivs, PATH_OUT)
    test_partial("retorna lista", isinstance(lista_cat, list))
    test_partial("tiene campo 'categoria'",
                 isinstance(lista_cat, list) and lista_cat and 'categoria' in lista_cat[0])
    test("viña del mar → ALTA",
         next((x['categoria'] for x in lista_cat if x.get('sucursal') == 'viña del mar'), None), 'ALTA')
    test("santiago centro → ALTA",
         next((x['categoria'] for x in lista_cat if x.get('sucursal') == 'santiago centro'), None), 'ALTA')
    test("maipú → MEDIA",
         next((x['categoria'] for x in lista_cat if x.get('sucursal') == 'maipú'), None), 'MEDIA')
    test_partial("exportó ranking_ivs.csv", os.path.exists(PATH_OUT))
    if os.path.exists(PATH_OUT):
        with open(PATH_OUT, encoding='utf-8') as f:
            rows = list(csv.DictReader(f))
        test("CSV tiene 3 filas", len(rows), 3)
        test_partial("CSV tiene columna 'ivs'",       'ivs'       in (rows[0] if rows else {}))
        test_partial("CSV tiene columna 'categoria'", 'categoria' in (rows[0] if rows else {}))
except Exception as e:
    print(f"  [ERROR] {e}")

total = test_count
print(f"\n{'='*45}")
print(f"Resultado: {total - failed_tests}/{total} pasados")
if failed_tests == 0:
    print("¡Excelente! Todos los tests pasaron.")
else:
    print(f"Tienes {failed_tests} test(s) por corregir.")
