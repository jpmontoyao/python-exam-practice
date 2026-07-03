# Nivel 6c: Simplificador de Rutas Unix
#
# Dada una ruta absoluta, retorna la ruta simplificada.
# Reglas:
#   '.'  → directorio actual (ignorar)
#   '..' → subir un nivel
#   '//' → equivale a '/'
#
# Ejemplos:
#   simplificar("/a/./b")       → "/a/b"
#   simplificar("/a/b/../c")    → "/a/c"
#   simplificar("/a//b")        → "/a/b"
#   simplificar("/../a")        → "/a"   (no se puede subir de raíz)
#


def tokenizar(ruta):
    """Divide la ruta por '/' y filtra strings vacíos."""
    return [p for p in ruta.split('/')]


def simplificar(ruta):
    """
    Simplifica una ruta Unix absoluta usando una pila.
    Retorna la ruta simplificada.
    """
    tokens = tokenizar(ruta)
    pila = []

    for token in tokens:
        if token == '.':
            if pila:
                pila.pop()
        elif token != '.':
            pila.append(token)

    return '/'.join(pila)
