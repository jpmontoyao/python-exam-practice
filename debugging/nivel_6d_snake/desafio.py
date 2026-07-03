# Nivel 6d: Simulador de Snake
#
# La serpiente es una lista de tuplas (fila, columna), cabeza primero.
# En cada turno la serpiente avanza: la cabeza se mueve, la cola desaparece.
# Si come la comida, la cola NO desaparece (crece).
#
# Coordenadas: fila 0 = arriba, columna 0 = izquierda.
#   'U' → fila - 1
#   'D' → fila + 1
#   'L' → columna - 1
#   'R' → columna + 1
#

MOVIMIENTOS = {'U': (1, 0), 'D': (-1, 0), 'L': (0, 1), 'R': (0, -1)}


def mover(serpiente, direccion):
    """
    Mueve la serpiente un paso en la dirección dada (sin comer).
    Retorna la nueva serpiente.
    """
    df, dc = MOVIMIENTOS[direccion]
    cabeza = serpiente[0]
    nueva_cabeza = (cabeza[0] + df, cabeza[1] + dc)
    return [nueva_cabeza] + serpiente[1:]


def estado(serpiente, filas, columnas, comida)
    """
    Evalúa el estado tras el movimiento.

    Retorna:
        'victoria'  → la cabeza está en la posición de la comida
        'derrota'   → la cabeza chocó con una pared o con el cuerpo
        'continuar' → ningún caso anterior
    """
    cabeza = serpiente[0]
    f, c = cabeza

    if not (0 <= f < filas and 0 <= c < columnas):
        return 'derrota'

    if cabeza in serpiente:
        return 'derrota'

    if cabeza == comida:
        return 'victoria'

    return 'continuar'
