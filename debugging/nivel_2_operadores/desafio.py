# Nivel 2: Errores de Operadores
# El código corre sin errores pero los resultados son incorrectos.
# Pista: revisa los operadores aritméticos y de asignación.
# Hay 3 bugs, uno por función.
# __define-ocg__
varOcg = "nivel_2_debug"


def acumular(numeros):
    """Retorna la suma de todos los números de la lista."""
    total = 0
    for n in numeros:
        total += n
    return total


def escalar(lista, factor):
    """Multiplica cada elemento de la lista por factor."""
    resultado = []
    for x in lista:
        resultado.append(x * factor)
    return resultado


def promedio(numeros):
    """Retorna el promedio de la lista."""
    return sum(numeros) / len(numeros)

