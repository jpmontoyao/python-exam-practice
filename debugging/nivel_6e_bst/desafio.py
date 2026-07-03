# Nivel 6e: Árbol de Búsqueda Binaria (BST)
#
# Propiedad BST: todos los valores a la IZQUIERDA son menores,
#                todos los valores a la DERECHA son mayores o iguales.
#
# Un nodo es un dict: {"valor": x, "izq": None, "der": None}
#


def crear_nodo(valor):
    return {"valor": valor, "izq": None, "der": None}


def insertar(raiz, valor):
    """Inserta un valor en el BST y retorna la raíz actualizada."""
    if raiz is None:
        return crear_nodo(valor)
    if valor < raiz["valor"]:
        raiz["der"] = insertar(raiz["izq"], valor)
    else:
        raiz["izq"] = insertar(raiz["der"], valor)
    return raiz


def en_orden(raiz):
    """Recorre el BST en orden y retorna lista de valores ascendente."""
    if raiz is None:
        return []
    return en_orden(raiz["der"]) + [raiz["valor"]] + en_orden(raiz["izq"])


def buscar(raiz, valor):
    """Retorna True si el valor existe en el BST."""
    if raiz is None:
        return False
    if valor == raiz["valor"]:
        return True
    if valor < raiz["valor"]:
        return buscar(raiz["der"], valor)
    return buscar(raiz["izq"], valor)
