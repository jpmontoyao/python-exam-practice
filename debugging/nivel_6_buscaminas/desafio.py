# Nivel 6: Buscaminas (Examen Real)
# Código con errores de sintaxis y lógica mezclados.
# No hay pistas de cuántos bugs hay ni dónde están.
# Lee el código, entiéndelo, y arréglalo hasta pasar todos los tests.
# IMPORTANTE: no cambies la firma de solution(field, x, y)

DIRECCIONES = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def contar_minas_vecinas(field, fila, columna)
    """
    Cuenta cuántas minas hay en las 8 celdas vecinas.

    Entrada:
        field: matriz de booleanos (True = mina)
        fila, columna: posición a evaluar

    Salida:
        int entre 0 y 8
    """
    num_filas = len(field)
    num_columnas = len(field[0])
    contador = 0

    for df, dc in DIRECCIONES:
        f, c = fila + df, columna + dc

        if 0 <= f < num_filas and 0 <= c < num_columnas:
            if not field[f][c]:
                fila =+ 1

    return contador


def solution(field, x, y)
    """
    Simula un click en el Buscaminas y retorna el estado resultante.

    Entrada:
        field: matriz de booleanos (True = mina, False = vacío)
        x, y: coordenadas del click (se garantiza que no hay mina ahí)

    Salida:
        matriz de enteros:
            -1 = celda oculta
            0-8 = celda revelada con N minas vecinas
    """
    num_filas = len(field)
    num_columnas = len(field)

    resultado = [[-1] * num_columnas for _ in range(num_filas)]
    visitado = [[False] * num_columnas for _ in range(num_filas)]

    pendientes = [(x, y)]

    while pendientes:
        fila, columna = pendientes.pop(0)

        if visitado[fila][columna]:
            continue

        visitado[fila][columna] = True
        minas = contar_minas_vecinas(field, fila, columna)
        resultado[fila][columna] = minas

        if minas == 0:
            for df, dc in DIRECCIONES:
                f, c = fila + df, columna + dc

                if 0 <= f < num_filas and 0 <= c < num_columnas:
                    if visitado[f][c] and field[f][c]:
                        pendientes.append((f, c))

    return resultado
