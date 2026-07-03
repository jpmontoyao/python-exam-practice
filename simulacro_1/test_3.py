import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from desafio_3 import reproducciones_por_pais_origen, genero_favorito_por_usuario, artistas_debut_tardio

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

print("=== SIMULACRO 1 — Desafio 3: Dos CSVs combinados ===\n")

# -------------------------------------------------------
# reproducciones_por_pais_origen
# -------------------------------------------------------
print("-- reproducciones_por_pais_origen('reproducciones.csv', 'artistas.csv') --")
try:
    res_pais = reproducciones_por_pais_origen("reproducciones.csv", "artistas.csv")
    test_partial("retorna dict", isinstance(res_pais, dict))
    test_partial("tiene 5 paises de origen",
                 isinstance(res_pais, dict) and set(res_pais.keys()) == {"Canada", "Puerto Rico", "Reino Unido", "Estados Unidos", "Australia"})
    test("Canada: 1 reproduccion",           res_pais.get("Canada")         if isinstance(res_pais, dict) else None, 1)
    test("Puerto Rico: 6 reproducciones",    res_pais.get("Puerto Rico")    if isinstance(res_pais, dict) else None, 6)
    test("Reino Unido: 3 reproducciones",    res_pais.get("Reino Unido")    if isinstance(res_pais, dict) else None, 3)
    test("Estados Unidos: 3 reproducciones", res_pais.get("Estados Unidos") if isinstance(res_pais, dict) else None, 3)
    test("Australia: 2 reproducciones",      res_pais.get("Australia")      if isinstance(res_pais, dict) else None, 2)
except Exception as e:
    print(f"  [ERROR] {e}")

# -------------------------------------------------------
# genero_favorito_por_usuario
# -------------------------------------------------------
print("\n-- genero_favorito_por_usuario('reproducciones.csv') --")
try:
    res_gen = genero_favorito_por_usuario("reproducciones.csv")
    test_partial("retorna dict", isinstance(res_gen, dict))
    test_partial("tiene los 4 usuarios",
                 isinstance(res_gen, dict) and set(res_gen.keys()) == {"user_a", "user_b", "user_c", "user_d"})
    test("user_a: Rock (5 de 5 son Rock)",   res_gen.get("user_a") if isinstance(res_gen, dict) else None, "Rock")
    test("user_b: Reggaeton (3 vs 2 Pop)",   res_gen.get("user_b") if isinstance(res_gen, dict) else None, "Reggaeton")
    test("user_c: Reggaeton (2 vs 1 Pop)",   res_gen.get("user_c") if isinstance(res_gen, dict) else None, "Reggaeton")
    test("user_d: Rock (2 vs 1 Reggaeton)",  res_gen.get("user_d") if isinstance(res_gen, dict) else None, "Rock")
except Exception as e:
    print(f"  [ERROR] {e}")

# -------------------------------------------------------
# artistas_debut_tardio
# -------------------------------------------------------
print("\n-- artistas_debut_tardio('reproducciones.csv', 'artistas.csv', 2000) --")
try:
    res_tardio = artistas_debut_tardio("reproducciones.csv", "artistas.csv", 2000)
    test_partial("retorna lista", isinstance(res_tardio, list))
    test_partial("tiene 3 artistas", isinstance(res_tardio, list) and len(res_tardio) == 3)
    test("primero es Tones and I (2018)",
         res_tardio[0] if res_tardio else None,
         {"artista": "Tones and I", "debut_ano": 2018, "reproducciones": 1})
    test("segundo es Billie Eilish (2015)",
         res_tardio[1] if isinstance(res_tardio, list) and len(res_tardio) > 1 else None,
         {"artista": "Billie Eilish", "debut_ano": 2015, "reproducciones": 1})
    test("tercero es The Weeknd (2010)",
         res_tardio[2] if isinstance(res_tardio, list) and len(res_tardio) > 2 else None,
         {"artista": "The Weeknd", "debut_ano": 2010, "reproducciones": 1})
except Exception as e:
    print(f"  [ERROR] {e}")

print("\n-- artistas_debut_tardio('reproducciones.csv', 'artistas.csv', 2014) --")
try:
    res_tardio2 = artistas_debut_tardio("reproducciones.csv", "artistas.csv", 2014)
    test_partial("tiene 2 artistas (> 2014)", isinstance(res_tardio2, list) and len(res_tardio2) == 2)
    test("debut_ano son enteros",
         all(isinstance(a["debut_ano"], int) for a in res_tardio2) if res_tardio2 else False, True)
except Exception as e:
    print(f"  [ERROR] {e}")

total = test_count
print(f"\n{'='*45}")
print(f"Resultado: {total - failed_tests}/{total} pasados")
if failed_tests == 0:
    print("¡Excelente! Todos los tests pasaron.")
else:
    print(f"Tienes {failed_tests} test(s) por corregir.")
