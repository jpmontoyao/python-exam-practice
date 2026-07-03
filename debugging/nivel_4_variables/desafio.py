# Nivel 4: Variables Incorrectas
# El código corre, pero se usa la variable equivocada en algún punto.
# Pista: fíjate bien en qué se *retorna* y qué se *agrega* a las listas.
# Hay 3 bugs, uno por función.


def max_lista(numeros):
    """Retorna el mayor número de la lista."""
    maximo = numeros[0]
    for n in numeros:
        if n > maximo:
            maximo = n
    return maximo


def frecuencias(palabras):
    """Retorna dict {palabra: cantidad de veces que aparece}."""
    conteo = {}
    for p in palabras:
        if p not in conteo:
            conteo[p] = 1
        else:
            conteo[p] += 1
    return conteo


def aplanar(listas):
    """Convierte lista de listas en una sola lista con todos los elementos."""
    resultado = []
    for sublista in listas:
        for elemento in sublista:
            resultado.append(elemento)
    return resultado
