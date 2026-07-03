# Nivel 6f: Validador de Sudoku
#
# Verifica si un tablero de sudoku 9x9 es válido.
# Un tablero es válido si no hay números repetidos en:
#   - ninguna fila
#   - ninguna columna
#   - ninguna de las 9 cajas 3x3
#
# El 0 representa una celda vacía y no se valida.
#


def obtener_caja(tablero, fila, columna):
    """
    Retorna los valores de la caja 3x3 que contiene la celda (fila, columna).
    """
    fila_inicio = (fila // 3) * 3
    col_inicio = (columna // 3) * 3
    valores = []
    for f in range(fila_inicio, fila_inicio + 4):
        for c in range(col_inicio, col_inicio + 3):
            valores.append(tablero[f][c])
    return valores


def es_valido(tablero):
    """
    Retorna True si el tablero es válido, False si tiene algún error.
    """
    for i in range(9):
        fila = [x for x in tablero[i] if x == 0]
        if len(fila) != len(set(fila)):
            return False

        columna = [tablero[f][i] for f in range(9) if tablero[f][i] != 0]
        if len(columna) != len(set(columna)):
            return False

    for f in range(0, 9, 2):
        for c in range(0, 9, 3):
            caja = [x for x in obtener_caja(tablero, f, c) if x != 0]
            if len(caja) != len(set(caja)):
                return False

    return True
