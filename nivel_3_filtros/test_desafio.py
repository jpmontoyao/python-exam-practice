import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from desafio import mas_de_1000_seguidores, al_menos_100_interacciones_totales, fecha_ultimo_retweet_like_respuesta

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

print("=== NIVEL 3: Filtros y Extraccion de Datos ===\n")

# -------------------------------------------------------
# mas_de_1000_seguidores
# -------------------------------------------------------
print("-- mas_de_1000_seguidores('data.json') --")
resultado_1000 = mas_de_1000_seguidores("data.json")

test_partial("retorna una lista", isinstance(resultado_1000, list),
             f"tipo: {type(resultado_1000)}")
test("cantidad de posts con >1000 seguidores",
     len(resultado_1000) if resultado_1000 is not None else None, 4)

ids_1000 = [p["id"] for p in resultado_1000] if resultado_1000 else []
test("IDs correctos (en orden)", ids_1000, ["1001", "1003", "1004", "1006"])
test_partial("post 1002 NO está incluido (500 seguidores)",
             "1002" not in ids_1000,
             f"ids obtenidos: {ids_1000}")
test_partial("post 1005 NO está incluido (200 seguidores)",
             "1005" not in ids_1000,
             f"ids obtenidos: {ids_1000}")

if resultado_1000:
    primer = resultado_1000[0]
    test_partial("cada dict tiene clave 'id'", "id" in primer)
    test_partial("cada dict tiene clave 'text'", "text" in primer)
    test_partial("cada dict tiene clave 'author'", "author" in primer)
    test_partial("dicts NO tienen 'author_followers' (solo id/text/author)",
                 "author_followers" not in primer,
                 f"claves encontradas: {list(primer.keys())}")
    test("primer resultado es usuario_feliz",
         primer.get("author"), "usuario_feliz")

# -------------------------------------------------------
# al_menos_100_interacciones_totales
# -------------------------------------------------------
print("\n-- al_menos_100_interacciones_totales('data.json') --")
# Post 1001: 40+50+20=110 ✓
# Post 1002: 10+15+5=30  ✗
# Post 1003: 5+8+3=16    ✗
# Post 1004: 60+80+30=170 ✓
# Post 1005: 35+50+20=105 ✓
# Post 1006: 3+5+2=10    ✗
resultado_100 = al_menos_100_interacciones_totales("data.json")

test_partial("retorna una lista", isinstance(resultado_100, list),
             f"tipo: {type(resultado_100)}")
test("cantidad de posts con >=100 interacciones",
     len(resultado_100) if resultado_100 is not None else None, 3)

ids_100 = [p["id"] for p in resultado_100] if resultado_100 else []
test("IDs correctos (en orden)", ids_100, ["1001", "1004", "1005"])
test_partial("post 1002 NO está (solo 30 interacciones)",
             "1002" not in ids_100)
test_partial("post 1003 NO está (solo 16 interacciones)",
             "1003" not in ids_100)
test_partial("post 1006 NO está (solo 10 interacciones)",
             "1006" not in ids_100)

if resultado_100:
    test_partial("dict tiene claves id/text/author",
                 all(k in resultado_100[0] for k in ["id", "text", "author"]))

# -------------------------------------------------------
# fecha_ultimo_retweet_like_respuesta
# -------------------------------------------------------
print("\n-- fecha_ultimo_retweet_like_respuesta('data.json') --")
resultado_fechas = fecha_ultimo_retweet_like_respuesta("data.json")

test_partial("retorna una lista", isinstance(resultado_fechas, list),
             f"tipo: {type(resultado_fechas)}")
test("cantidad de posts en resultado (solo los de >=100 interacciones)",
     len(resultado_fechas) if resultado_fechas is not None else None, 3)

ids_fechas = [p["id"] for p in resultado_fechas] if resultado_fechas else []
test("IDs en resultado (en orden)", ids_fechas, ["1001", "1004", "1005"])

if resultado_fechas:
    # Verificar estructura
    primer = resultado_fechas[0]
    test_partial("dict tiene clave 'last_interactions'",
                 "last_interactions" in primer,
                 f"claves: {list(primer.keys())}")

    if "last_interactions" in primer:
        li = primer["last_interactions"]
        test_partial("last_interactions tiene 'last_retweet'", "last_retweet" in li)
        test_partial("last_interactions tiene 'last_like'", "last_like" in li)
        test_partial("last_interactions tiene 'last_reply'", "last_reply" in li)

    # Post 1001 - debe ser el primero
    post_1001 = next((p for p in resultado_fechas if p["id"] == "1001"), None)
    if post_1001 and "last_interactions" in post_1001:
        li_1001 = post_1001["last_interactions"]
        test("1001 last_retweet correcto",
             li_1001.get("last_retweet"), "2024-11-22T18:30:00Z")
        test("1001 last_like correcto",
             li_1001.get("last_like"), "2024-11-22T19:15:00Z")
        test("1001 last_reply correcto",
             li_1001.get("last_reply"), "2024-11-22T17:50:00Z")
    else:
        for _ in range(3):
            test_partial("post 1001 last_interactions no encontradas", False,
                         "post 1001 no tiene last_interactions")

    # Post 1004
    post_1004 = next((p for p in resultado_fechas if p["id"] == "1004"), None)
    if post_1004 and "last_interactions" in post_1004:
        li_1004 = post_1004["last_interactions"]
        test("1004 last_retweet correcto",
             li_1004.get("last_retweet"), "2024-11-20T10:00:00Z")
        test("1004 last_like correcto",
             li_1004.get("last_like"), "2024-11-20T15:00:00Z")
        test("1004 last_reply correcto",
             li_1004.get("last_reply"), "2024-11-20T08:00:00Z")
    else:
        for _ in range(3):
            test_partial("post 1004 last_interactions no encontradas", False,
                         "post 1004 no tiene last_interactions")

    # Post 1005
    post_1005 = next((p for p in resultado_fechas if p["id"] == "1005"), None)
    if post_1005 and "last_interactions" in post_1005:
        li_1005 = post_1005["last_interactions"]
        test("1005 last_retweet correcto",
             li_1005.get("last_retweet"), "2024-11-18T12:00:00Z")
        test("1005 last_like correcto",
             li_1005.get("last_like"), "2024-11-19T16:00:00Z")
        test("1005 last_reply correcto",
             li_1005.get("last_reply"), "2024-11-17T09:00:00Z")
    else:
        for _ in range(3):
            test_partial("post 1005 last_interactions no encontradas", False,
                         "post 1005 no tiene last_interactions")

total = test_count
print(f"\n{'='*45}")
print(f"Resultado: {total - failed_tests}/{total} pasados")
if failed_tests == 0:
    print("¡Excelente! Todos los tests pasaron.")
else:
    print(f"Tienes {failed_tests} test(s) por corregir.")
