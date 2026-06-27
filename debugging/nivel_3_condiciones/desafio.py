# Nivel 3: Errores de Condiciones
# El código corre, pero las condiciones están mal escritas.
# Pista: revisa los operadores de comparación (>, <, ==, !=)
# y el uso de "not". Hay 3 bugs, uno por función.
# __define-ocg__
varOcg = "nivel_3_debug"


def filtrar_positivos(numeros):
    """Retorna solo los números mayores que 0."""
    return [n for n in numeros if n > 0]


def contar_mayores(lista, umbral):
    """Cuenta cuántos elementos son estrictamente mayores que umbral."""
    contador = 0
    for x in lista:
        if x > umbral:
            contador += 1
    return contador


def tiene_duplicado(lista):
    """Retorna True si hay algún elemento repetido, False si todos son únicos."""
    vistos = set()
    for x in lista:
        if x in vistos:
            return True
        vistos.add(x)
    return False
