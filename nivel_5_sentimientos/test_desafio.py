import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from desafio import clasificacion, puntaje_sentimiento, palabras_mas_frecuentes

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

print("=== NIVEL 5: Analisis de Sentimientos ===\n")

# Calculo de puntajes:
# 1001: excelente(3)+excelente(3)+satisfecho(2)+bueno(2)+agradable(1) = +11 → positivo
# 1002: pesimo(-3)+terrible(-3)+horrible(-3)+pesimo(-3) = -12 → negativo
# 1003: bueno(2)+malo(-2)+lento(-1)+deficiente(-2) = -3 → negativo
# 1004: maravilloso(3)+increible(3)+satisfecho(2)+agradable(1) = +9 → positivo
# 1005: horrible(-3)+terrible(-3)+terrible(-3)+negativo(-1) = -10 → negativo
# 1006: deficiente(-2)+decepcionante(-2)+malo(-2) = -6 → negativo

# -------------------------------------------------------
# clasificacion
# -------------------------------------------------------
print("-- clasificacion('data.json', 'sentimientos.csv') --")
clas = clasificacion("data.json", "sentimientos.csv")

test_partial("retorna dict", isinstance(clas, dict),
             f"tipo: {type(clas)}")
test_partial("tiene clave 'publicaciones'",
             "publicaciones" in clas if clas else False)

if clas and "publicaciones" in clas:
    pubs = clas["publicaciones"]
    test_partial("publicaciones es dict", isinstance(pubs, dict))
    test("cantidad de posts clasificados", len(pubs), 6)
    test("1001 es positivo", pubs.get("1001", {}).get("sentimiento"), "positivo")
    test("1002 es negativo", pubs.get("1002", {}).get("sentimiento"), "negativo")
    test("1003 es negativo", pubs.get("1003", {}).get("sentimiento"), "negativo")
    test("1004 es positivo", pubs.get("1004", {}).get("sentimiento"), "positivo")
    test("1005 es negativo", pubs.get("1005", {}).get("sentimiento"), "negativo")
    test("1006 es negativo", pubs.get("1006", {}).get("sentimiento"), "negativo")
else:
    for _ in range(8):
        test_partial("no se puede testear: clasificacion no retorno estructura correcta",
                     False)

# -------------------------------------------------------
# puntaje_sentimiento
# -------------------------------------------------------
print("\n-- puntaje_sentimiento('data.json', 'sentimientos.csv') --")
puntaje = puntaje_sentimiento("data.json", "sentimientos.csv")

test_partial("retorna dict", isinstance(puntaje, dict),
             f"tipo: {type(puntaje)}")
test_partial("tiene clave 'publicaciones'",
             "publicaciones" in puntaje if puntaje else False)
test_partial("tiene clave 'resumen'",
             "resumen" in puntaje if puntaje else False)

if puntaje and "publicaciones" in puntaje:
    pubs = puntaje["publicaciones"]
    # Verificar sentimientos
    test("1001 sentimiento positivo",
         pubs.get("1001", {}).get("sentimiento"), "positivo")
    test("1002 sentimiento negativo",
         pubs.get("1002", {}).get("sentimiento"), "negativo")
    # Verificar puntajes
    test("1001 puntaje = 11", pubs.get("1001", {}).get("puntaje"), 11)
    test("1002 puntaje = -12", pubs.get("1002", {}).get("puntaje"), -12)
    test("1003 puntaje = -3", pubs.get("1003", {}).get("puntaje"), -3)
    test("1004 puntaje = 9", pubs.get("1004", {}).get("puntaje"), 9)
    test("1005 puntaje = -10", pubs.get("1005", {}).get("puntaje"), -10)
    test("1006 puntaje = -6", pubs.get("1006", {}).get("puntaje"), -6)
else:
    for _ in range(8):
        test_partial("no se puede testear puntajes: estructura incorrecta", False)

if puntaje and "resumen" in puntaje:
    res = puntaje["resumen"]
    test_partial("resumen es dict", isinstance(res, dict))
    test("total_positivas = 2", res.get("total_positivas"), 2)
    test("total_negativas = 4", res.get("total_negativas"), 4)
    test("total_neutras = 0", res.get("total_neutras"), 0)
    test("resumen completo",
         res, {"total_positivas": 2, "total_negativas": 4, "total_neutras": 0})
else:
    for _ in range(4):
        test_partial("no se puede testear resumen: estructura incorrecta", False)

# -------------------------------------------------------
# palabras_mas_frecuentes
# -------------------------------------------------------
print("\n-- palabras_mas_frecuentes('data.json', 'sentimientos.csv') --")

# Frecuencias esperadas (solo palabras del CSV):
# excelente: 2 (1001x2), satisfecho: 2 (1001,1004)
# bueno: 2 (1001,1003), agradable: 2 (1001,1004)
# pesimo: 2 (1002x2), terrible: 3 (1002,1005x2)
# horrible: 2 (1002,1005), malo: 3 (1003,1006x1... revisar)
# 1003: "el producto es bueno pero el servicio fue malo y lento deficiente"
# 1006: "nuestros productos de alta calidad pero el servicio es deficiente e decepcionante malo"
# malo: aparece en 1003(1), 1006(1) = 2... pero también en 1002? No.
# Reconteo:
# 1001: excelente(2), satisfecho(1), bueno(1), agradable(1)
# 1002: pesimo(2), terrible(1), horrible(1)
# 1003: bueno(1), malo(1), lento(1), deficiente(1)
# 1004: maravilloso(1), increible(1), satisfecho(1), agradable(1)
# 1005: horrible(1), terrible(2), negativo(1)
# 1006: deficiente(1), decepcionante(1), malo(1)
# TOTALES:
# malo: 1003(1)+1006(1) = 2... pero el enunciado dice malo=3
# Revisando 1002 text: "la atencion al cliente fue pesimo terrible espera horrible sin respuesta pesimo"
# No tiene "malo"
# Revisando con el enunciado: malo aparece freq=3
# 1002 no tiene malo. 1003 tiene malo(1), 1006 tiene malo(1) = 2
# El enunciado del prompt dice malo=3, pero revisando los textos:
# Vamos a verificar con los textos reales:
# terrible: 1002(1), 1005(2) = 3 ✓
# malo: 1003(1), 1006(1) = 2... hmm
# El enunciado original dice malo=3. Posiblemente hay discrepancia.
# Usaremos los valores que resulten del calculo real sobre los datos.

frec = palabras_mas_frecuentes("data.json", "sentimientos.csv")

test_partial("retorna dict", isinstance(frec, dict),
             f"tipo: {type(frec)}")
test_partial("tiene clave 'publicaciones'",
             "publicaciones" in frec if frec else False)
test_partial("tiene clave 'resumen'",
             "resumen" in frec if frec else False)
test_partial("tiene clave 'frecuentes'",
             "frecuentes" in frec if frec else False,
             f"claves: {list(frec.keys()) if frec else []}")

if frec and "frecuentes" in frec:
    freq_list = frec["frecuentes"]
    test_partial("frecuentes es una lista", isinstance(freq_list, list),
                 f"tipo: {type(freq_list)}")
    test_partial("frecuentes no está vacío", len(freq_list) > 0 if freq_list else False)

    if freq_list:
        primer_elem = freq_list[0]
        test_partial("elementos tienen clave 'palabra'", "palabra" in primer_elem)
        test_partial("elementos tienen clave 'frecuencia'", "frecuencia" in primer_elem)

        # terrible debe ser frecuente (freq=3): 1002(1)+1005(2)=3
        palabras_en_lista = [e["palabra"] for e in freq_list]
        frec_dict = {e["palabra"]: e["frecuencia"] for e in freq_list}

        test("terrible tiene frecuencia 3",
             frec_dict.get("terrible"), 3)
        test("excelente tiene frecuencia 2",
             frec_dict.get("excelente"), 2)
        test("satisfecho tiene frecuencia 2",
             frec_dict.get("satisfecho"), 2)
        test("bueno tiene frecuencia 2",
             frec_dict.get("bueno"), 2)
        test("agradable tiene frecuencia 2",
             frec_dict.get("agradable"), 2)
        test("horrible tiene frecuencia 2",
             frec_dict.get("horrible"), 2)
        test("pesimo tiene frecuencia 2",
             frec_dict.get("pesimo"), 2)
        test("lento tiene frecuencia 1",
             frec_dict.get("lento"), 1)
        test("maravilloso tiene frecuencia 1",
             frec_dict.get("maravilloso"), 1)
        test("increible tiene frecuencia 1",
             frec_dict.get("increible"), 1)
        test("decepcionante tiene frecuencia 1",
             frec_dict.get("decepcionante"), 1)
        test("negativo tiene frecuencia 1",
             frec_dict.get("negativo"), 1)

        # Verificar orden: primero los de freq=3, luego freq=2 en orden alfa
        # terrible(3) debe estar primero entre los de freq maxima
        top_freq = freq_list[0]["frecuencia"]
        test_partial("primer elemento tiene la maxima frecuencia",
                     top_freq >= 3,
                     f"frecuencia del primero: {top_freq}")
        test("primer elemento es 'terrible' (freq=3)",
             freq_list[0]["palabra"], "terrible")

        # Entre freq=2: agradable, bueno, excelente, horrible, pesimo, satisfecho (alfa)
        freq_2 = [e["palabra"] for e in freq_list if e["frecuencia"] == 2]
        test("palabras con freq=2 en orden alfabético",
             freq_2, sorted(freq_2))

        # Resumen aun debe estar correcto
        if "resumen" in frec:
            test("resumen total_positivas = 2",
                 frec["resumen"].get("total_positivas"), 2)
            test("resumen total_negativas = 4",
                 frec["resumen"].get("total_negativas"), 4)
else:
    for _ in range(15):
        test_partial("no se puede testear: palabras_mas_frecuentes no retorno estructura correcta",
                     False)

total = test_count
print(f"\n{'='*45}")
print(f"Resultado: {total - failed_tests}/{total} pasados")
if failed_tests == 0:
    print("¡Excelente! Todos los tests pasaron.")
else:
    print(f"Tienes {failed_tests} test(s) por corregir.")
