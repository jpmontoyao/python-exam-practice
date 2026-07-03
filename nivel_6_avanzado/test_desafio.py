import sys
import os


sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from desafio import top_engagement, buscar_en_textos, resumen_diario

DATA_FILE = "data.json"

passed = 0
failed = 0

def check(test_name, expected, obtained):
    global passed, failed
    if expected == obtained:
        print(f"  PASS | {test_name}")
        passed += 1
    else:
        print(f"  FAIL | {test_name}")
        print(f"         Expected: {expected}")
        print(f"         Obtained: {obtained}")
        failed += 1

# ─────────────────────────────────────────────
print("\n=== top_engagement ===")

result_3 = top_engagement(DATA_FILE, 3)
result_5 = top_engagement(DATA_FILE, 5)

check("1. top_engagement returns a list", True, isinstance(result_3, list))

check("2. top_engagement(n=3) length is 3", 3, len(result_3) if isinstance(result_3, list) else None)

check(
    "3. First result id='2001' engagement_rate=60.0",
    {"id": "2001", "author": "power_user", "engagement_rate": 60.0},
    result_3[0] if isinstance(result_3, list) and len(result_3) >= 1 else None
)

check(
    "4. Second result id='2004' engagement_rate=43.0",
    {"id": "2004", "author": "power_user", "engagement_rate": 43.0},
    result_3[1] if isinstance(result_3, list) and len(result_3) >= 2 else None
)

check(
    "5. Third result id='2006' engagement_rate=15.4",
    {"id": "2006", "author": "micro_influencer", "engagement_rate": 15.4},
    result_3[2] if isinstance(result_3, list) and len(result_3) >= 3 else None
)

check(
    "6. top_engagement(n=5) ids in order (tiebreaker: id asc)",
    ["2001", "2004", "2006", "2002", "2005"],
    [p["id"] for p in result_5] if isinstance(result_5, list) and len(result_5) == 5 else None
)

check(
    "7. Each dict has keys: id, author, engagement_rate",
    True,
    all(set(p.keys()) == {"id", "author", "engagement_rate"} for p in result_3)
    if isinstance(result_3, list) and len(result_3) == 3 else False
)

check(
    "8. engagement_rate is a float",
    True,
    isinstance(result_3[0]["engagement_rate"], float)
    if isinstance(result_3, list) and len(result_3) >= 1 else False
)

# ─────────────────────────────────────────────
print("\n=== buscar_en_textos ===")

result_sv_malo = buscar_en_textos(DATA_FILE, ["servicio", "malo"])
result_satisfecho = buscar_en_textos(DATA_FILE, ["satisfecho"])
result_inexistente = buscar_en_textos(DATA_FILE, ["inexistente"])

check("1. buscar_en_textos returns a list", True, isinstance(result_sv_malo, list))

check(
    "2. buscar_en_textos(['servicio','malo']) length is 4",
    4,
    len(result_sv_malo) if isinstance(result_sv_malo, list) else None
)

check(
    "3. IDs found: ['2001','2002','2003','2005']",
    ["2001", "2002", "2003", "2005"],
    [p["id"] for p in result_sv_malo] if isinstance(result_sv_malo, list) and len(result_sv_malo) == 4 else None
)

check(
    "4. Post 2004 NOT included",
    True,
    "2004" not in [p["id"] for p in result_sv_malo]
    if isinstance(result_sv_malo, list) else False
)

check(
    "5. Post 2006 NOT included",
    True,
    "2006" not in [p["id"] for p in result_sv_malo]
    if isinstance(result_sv_malo, list) else False
)

check(
    "6. Post 2001 palabras_encontradas == ['servicio']",
    ["servicio"],
    next((p["palabras_encontradas"] for p in result_sv_malo if p["id"] == "2001"), None)
    if isinstance(result_sv_malo, list) else None
)

check(
    "7. Post 2002 palabras_encontradas == ['malo']",
    ["malo"],
    next((p["palabras_encontradas"] for p in result_sv_malo if p["id"] == "2002"), None)
    if isinstance(result_sv_malo, list) else None
)

check(
    "8. buscar_en_textos(['satisfecho']) → ids: ['2001','2006']",
    ["2001", "2006"],
    [p["id"] for p in result_satisfecho]
    if isinstance(result_satisfecho, list) else None
)

check(
    "9. buscar_en_textos(['inexistente']) → []",
    [],
    result_inexistente
)

check(
    "10. Each result has keys: id, author, text, palabras_encontradas",
    True,
    all(set(p.keys()) == {"id", "author", "text", "palabras_encontradas"} for p in result_sv_malo)
    if isinstance(result_sv_malo, list) and len(result_sv_malo) == 4 else False
)

# ─────────────────────────────────────────────
print("\n=== resumen_diario ===")

result_rd = resumen_diario(DATA_FILE)

check("1. resumen_diario returns dict with 'dias' key", True, isinstance(result_rd, dict) and "dias" in result_rd)

dias = result_rd.get("dias", {}) if isinstance(result_rd, dict) else {}

check("2. Has exactly 2 days", 2, len(dias))

check("3. '2024-11-15' exists", True, "2024-11-15" in dias)

check("4. '2024-11-16' exists", True, "2024-11-16" in dias)

day_15 = dias.get("2024-11-15", {})
day_16 = dias.get("2024-11-16", {})

check("5. 2024-11-15 total_posts == 4", 4, day_15.get("total_posts"))

check("6. 2024-11-15 total_interacciones == 1633", 1633, day_15.get("total_interacciones"))

check("7. 2024-11-15 autor_mas_activo == 'power_user'", "power_user", day_15.get("autor_mas_activo"))

check("8. 2024-11-16 total_posts == 2", 2, day_16.get("total_posts"))

check("9. 2024-11-16 total_interacciones == 92", 92, day_16.get("total_interacciones"))

check(
    "10. 2024-11-16 autor_mas_activo == 'cliente_normal' (alphabetical tiebreaker)",
    "cliente_normal",
    day_16.get("autor_mas_activo")
)

# ─────────────────────────────────────────────
print(f"\n{'='*40}")
print(f"  Resultado: {passed} PASS / {failed} FAIL")
print(f"{'='*40}\n")
