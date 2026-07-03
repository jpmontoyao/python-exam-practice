import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from desafio import distribucion_publicaciones, rango_temporal

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

print("=== NIVEL 4: Analisis Temporal ===\n")

# Posts y sus horas:
# 1001: created_at="2024-11-15T10:30:00Z" → hora 10
# 1002: created_at="2024-11-15T14:00:00Z" → hora 14
# 1003: created_at="2024-11-15T10:15:00Z" → hora 10
# 1004: created_at="2024-11-15T00:30:00Z" → hora 0
# 1005: created_at="2024-11-15T22:45:00Z" → hora 22
# 1006: created_at="2024-11-15T10:00:00Z" → hora 10
# Distribucion: {"10": 3, "14": 1, "0": 1, "22": 1}

# -------------------------------------------------------
# distribucion_publicaciones
# -------------------------------------------------------
print("-- distribucion_publicaciones('data.json') --")
dist = distribucion_publicaciones("data.json")

test_partial("retorna dict", isinstance(dist, dict),
             f"tipo: {type(dist)}")
test_partial("tiene clave 'distribucion'", "distribucion" in dist if dist else False,
             f"claves: {list(dist.keys()) if dist else []}")

if dist and "distribucion" in dist:
    d = dist["distribucion"]
    test_partial("distribucion es un dict", isinstance(d, dict),
                 f"tipo: {type(d)}")
    test("resultado completo correcto",
         dist, {"distribucion": {"10": 3, "14": 1, "0": 1, "22": 1}})
    test("hora 10 tiene 3 publicaciones", d.get("10"), 3)
    test("hora 14 tiene 1 publicacion", d.get("14"), 1)
    test("hora 0 tiene 1 publicacion", d.get("0"), 1)
    test("hora 22 tiene 1 publicacion", d.get("22"), 1)
    test("total de horas con publicaciones", len(d), 4)
    test_partial("claves son strings (no ints)",
                 all(isinstance(k, str) for k in d.keys()),
                 f"tipos de claves: {[type(k).__name__ for k in d.keys()]}")
    test_partial("horas sin publicaciones no aparecen",
                 "1" not in d and "2" not in d and "15" not in d)
else:
    for _ in range(8):
        test_partial("no se puede testear: distribucion no retorno dict con clave correcta",
                     False)

# -------------------------------------------------------
# rango_temporal
# -------------------------------------------------------
print("\n-- rango_temporal('data.json') --")
# Inicio: 2024-11-15T00:30:00Z (post 1004, hora 0)
# Fin:    2024-11-15T22:45:00Z (post 1005, hora 22)
rango = rango_temporal("data.json")

test_partial("retorna dict", isinstance(rango, dict),
             f"tipo: {type(rango)}")
test_partial("tiene clave 'rango'", "rango" in rango if rango else False,
             f"claves: {list(rango.keys()) if rango else []}")

if rango and "rango" in rango:
    r = rango["rango"]
    test_partial("rango es un dict", isinstance(r, dict))
    test("resultado completo correcto",
         rango, {"rango": {"inicio": "2024-11-15T00:30:00Z", "fin": "2024-11-15T22:45:00Z"}})
    test("inicio correcto (publicacion mas temprana)",
         r.get("inicio"), "2024-11-15T00:30:00Z")
    test("fin correcto (publicacion mas reciente)",
         r.get("fin"), "2024-11-15T22:45:00Z")
    test_partial("inicio NO es el fin",
                 r.get("inicio") != r.get("fin"),
                 "inicio y fin son iguales, algo está mal")
else:
    for _ in range(4):
        test_partial("no se puede testear: rango no retorno dict con clave correcta", False)

total = test_count
print(f"\n{'='*45}")
print(f"Resultado: {total - failed_tests}/{total} pasados")
if failed_tests == 0:
    print("¡Excelente! Todos los tests pasaron.")
else:
    print(f"Tienes {failed_tests} test(s) por corregir.")
