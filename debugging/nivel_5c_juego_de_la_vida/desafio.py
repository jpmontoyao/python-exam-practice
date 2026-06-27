# Nivel 5c: El Juego de la Vida (Conway's Game of Life)
#
# Mismo patrón que el buscaminas: grilla 2D + contar vecinos + aplicar reglas.
# El código corre sin errores pero los resultados son incorrectos.
# No hay pistas de cuántos bugs hay ni de qué tipo son.
#
# Reglas del juego:
#   - Celda VIVA con 2 o 3 vecinos vivos → sobrevive
#   - Celda MUERTA con exactamente 3 vecinos vivos → nace
#   - Cualquier otro caso → muere o permanece muerta
#
# True = celda viva, False = celda muerta
#
# __define-ocg__
varOcg = "nivel_5c_debug"

DIRECCIONES = [(-1, -1), (-1, 0), (-1, 1),
               ( 0, -1),          ( 0, 1),
               ( 1, -1), ( 1, 0), ( 1, 1)]


def contar_vecinos_vivos(tablero, fila, columna):
    """Cuenta cuántas de las 8 celdas vecinas están vivas (True)."""
    filas = len(tablero)
    columnas = len(tablero[0])
    contador = 0

    for df, dc in DIRECCIONES:
        f, c = fila + df, columna + dc
        if 0 <= f < filas and 0 <= c < columnas:
            if tablero[f][c]:
                contador += 1

    return contador


def siguiente_generacion(tablero):
    """
    Aplica las reglas del Juego de la Vida y retorna el nuevo estado del tablero.
    El tablero original NO debe modificarse.

    Ejemplo — blinker (oscilador):
        tablero = [[False, False, False],
                   [True,  True,  True ],
                   [False, False, False]]

        siguiente_generacion(tablero) →
                  [[False, True,  False],
                   [False, True,  False],
                   [False, True,  False]]
    """
    filas = len(tablero)
    columnas = len(tablero[0])
    nuevo = [[False] * columnas for _ in range(filas)]

    for i in range(filas):
        for j in range(columnas):
            vecinos = contar_vecinos_vivos(tablero, i, j)

            if tablero[i][j]:
                nuevo[i][j] = vecinos == 2 or vecinos == 3
            else:
                nuevo[i][j] = vecinos == 3
    print(nuevo)
    return nuevo

tablero = [[False, False, False],
            [True,  True,  True ],
            [False, False, False]]

x = siguiente_generacion(tablero)
print(contar_vecinos_vivos(tablero,1,1))