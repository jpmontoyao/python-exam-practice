# Nivel 5: Bugs Combinados
# Cada función tiene 2 bugs de tipos distintos.
# Ya no hay pistas de qué tipo es cada bug — igual que en el examen real.
# Hay 6 bugs en total, 2 por función.


def top_palabras(texto, n):
    """
    Retorna las n palabras más frecuentes del texto (case-insensitive),
    ordenadas de mayor a menor frecuencia.
    """
    palabras = texto.lower().split()
    conteo = {}
    for p in palabras:
        if p not in conteo:
            conteo[p] = 1
        else:
            conteo[p] += 1
    ordenado = sorted(conteo.items(), key=lambda x: -x[1])
    return [p for p, _ in ordenado[:n]]


def agrupar_pares_impares(numeros):
    """
    Retorna un dict {"pares": [...], "impares": [...]}
    con los números agrupados según su paridad.
    """
    grupos = {"pares": [], "impares": []}
    for n in numeros:
        if n % 2 == 0:
            grupos["pares"].append(n)
        else:
            grupos["impares"].append(n)
    return grupos


def invertir_dict(d):
    """
    Dado un dict {clave: valor}, retorna uno nuevo {valor: clave}.
    Ejemplo: {"a": 1, "b": 2} → {1: "a", 2: "b"}
    """
    nuevo = {}
    for clave in d:
        nuevo[d[clave]] = clave
    return nuevo

