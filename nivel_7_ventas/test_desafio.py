import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from desafio import ventas_por_categoria, ventas_sobre_monto, resumen_por_vendedor

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

print("=== NIVEL 7: Ventas CSV ===\n")

# -------------------------------------------------------
# ventas_por_categoria
# -------------------------------------------------------
print("-- ventas_por_categoria('ventas.csv', 'Tecnologia') --")
res_tec = ventas_por_categoria("ventas.csv", "Tecnologia")

test_partial("retorna lista", isinstance(res_tec, list))
test("cantidad de ventas Tecnologia", len(res_tec), 5)

ids_tec = [v["id"] for v in res_tec]
test("IDs en orden", ids_tec, ["1","2","5","7","9"])
test("total Laptop (850000*2)", res_tec[0]["total"], 1700000)
test("total Mouse (15000*5)",   res_tec[1]["total"], 75000)
test_partial("dict tiene id/producto/vendedor/total",
             all(k in res_tec[0] for k in ["id","producto","vendedor","total"]))

print("\n-- ventas_por_categoria('ventas.csv', 'Ropa') --")
res_ropa = ventas_por_categoria("ventas.csv", "Ropa")
test("cantidad de ventas Ropa", len(res_ropa), 5)
ids_ropa = [v["id"] for v in res_ropa]
test("IDs Ropa en orden", ids_ropa, ["3","4","6","8","10"])

# -------------------------------------------------------
# ventas_sobre_monto
# -------------------------------------------------------
print("\n-- ventas_sobre_monto('ventas.csv', 100000) --")
res_monto = ventas_sobre_monto("ventas.csv", 100000)

test_partial("retorna lista", isinstance(res_monto, list))
test("cantidad de ventas sobre 100000", len(res_monto), 4)
test("primer resultado es el de mayor total",
     res_monto[0]["id"], "1")
test("totales en orden descendente",
     [v["total"] for v in res_monto], [1700000, 320000, 135000, 120000])
test_partial("dict tiene id/producto/total",
             all(k in res_monto[0] for k in ["id","producto","total"]))

print("\n-- ventas_sobre_monto('ventas.csv', 500000) --")
res_monto2 = ventas_sobre_monto("ventas.csv", 500000)
test("solo Laptop supera 500000", len(res_monto2), 1)
test("es la Laptop", res_monto2[0]["producto"], "Laptop")

# -------------------------------------------------------
# resumen_por_vendedor
# -------------------------------------------------------
print("\n-- resumen_por_vendedor('ventas.csv') --")
res_vend = resumen_por_vendedor("ventas.csv")

test_partial("retorna dict", isinstance(res_vend, dict))
test_partial("tiene los 3 vendedores",
             set(res_vend.keys()) == {"Maria","Carlos","Pedro"})
test("total Maria  (1700000+75000+320000+72000)", res_vend.get("Maria"),  2167000)
test("total Carlos (75000+70000+80000)",          res_vend.get("Carlos"), 225000)
test("total Pedro  (45000+120000+135000)",         res_vend.get("Pedro"),  300000)

total = test_count
print(f"\n{'='*45}")
print(f"Resultado: {total - failed_tests}/{total} pasados")
if failed_tests == 0:
    print("¡Excelente! Todos los tests pasaron.")
else:
    print(f"Tienes {failed_tests} test(s) por corregir.")
