import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from desafio import leer_posts, contar_posts_por_autor, leer_sentimientos, palabras_positivas

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

print("=== NIVEL 2: Lectura de Archivos JSON y CSV ===\n")

# --- leer_posts ---
print("-- leer_posts('data.json') --")
posts = leer_posts("data.json")
test_partial("leer_posts retorna lista", isinstance(posts, list),
             f"tipo obtenido: {type(posts)}")
test("leer_posts cantidad de posts", len(posts) if posts else None, 6)
test_partial("leer_posts primer post tiene id='1001'",
             posts[0]["id"] == "1001" if posts else False,
             f"id obtenido: {posts[0].get('id') if posts else 'None'}")
test_partial("leer_posts posts tienen campo 'author'",
             all("author" in p for p in posts) if posts else False)
test_partial("leer_posts posts tienen campo 'retweets' (lista)",
             all(isinstance(p.get("retweets"), list) for p in posts) if posts else False)
test("leer_posts ultimo post tiene id='1006'",
     posts[-1]["id"] if posts else None, "1006")

# --- contar_posts_por_autor ---
print("\n-- contar_posts_por_autor('data.json') --")
conteo = contar_posts_por_autor("data.json")
expected_conteo = {
    "usuario_feliz": 1,
    "cliente_frustrado": 1,
    "analista_tech": 1,
    "influencer_digital": 1,
    "usuario_nuevo": 1,
    "empresa_grande": 1
}
test("contar_posts_por_autor resultado completo", conteo, expected_conteo)
test_partial("contar_posts_por_autor tiene 6 autores",
             len(conteo) == 6 if conteo else False,
             f"autores: {len(conteo) if conteo else 0}")

# --- leer_sentimientos ---
print("\n-- leer_sentimientos('sentimientos.csv') --")
sentimientos = leer_sentimientos("sentimientos.csv")
test_partial("leer_sentimientos retorna dict", isinstance(sentimientos, dict),
             f"tipo: {type(sentimientos)}")
test("leer_sentimientos tiene 14 palabras",
     len(sentimientos) if sentimientos else None, 14)
test("leer_sentimientos 'excelente' correcto",
     sentimientos.get("excelente") if sentimientos else None,
     {"polaridad": "positivo", "intensidad": 3})
test("leer_sentimientos 'pesimo' correcto",
     sentimientos.get("pesimo") if sentimientos else None,
     {"polaridad": "negativo", "intensidad": -3})
test("leer_sentimientos 'lento' correcto",
     sentimientos.get("lento") if sentimientos else None,
     {"polaridad": "negativo", "intensidad": -1})

# --- palabras_positivas ---
print("\n-- palabras_positivas('sentimientos.csv') --")
positivas = palabras_positivas("sentimientos.csv")
expected_positivas = ["excelente", "increible", "maravilloso", "bueno", "satisfecho", "agradable"]
test("palabras_positivas resultado completo", positivas, expected_positivas)
test("palabras_positivas cantidad", len(positivas) if positivas else None, 6)
test_partial("palabras_positivas primer elemento es 'excelente'",
             positivas[0] == "excelente" if positivas else False)
test_partial("palabras_positivas último elemento es 'agradable'",
             positivas[-1] == "agradable" if positivas else False)

total = test_count
print(f"\n{'='*45}")
print(f"Resultado: {total - failed_tests}/{total} pasados")
if failed_tests == 0:
    print("¡Excelente! Todos los tests pasaron.")
else:
    print(f"Tienes {failed_tests} test(s) por corregir.")
