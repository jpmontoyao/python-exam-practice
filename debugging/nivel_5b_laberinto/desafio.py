# Nivel 5b: Laberinto — Preparación para el Boss
#
# Este código implementa BFS para encontrar el camino más corto en un laberinto.
# Tiene bugs de lógica — el código corre pero los resultados son incorrectos.
# No hay pistas de cuántos bugs hay ni dónde están.
# Para encontrarlos necesitas ENTENDER el algoritmo, no puedes borrarlo y rehacerlo.
#
# El laberinto es una lista de strings:
#   'S' = inicio      '#' = pared (no se puede pasar)
#   'E' = salida      '.' = camino libre
#

DIRECCIONES = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def encontrar_inicio(laberinto):
    """Busca y retorna la posición (fila, columna) de 'S' en el laberinto."""
    for i in range(len(laberinto)):
        for j in range(len(laberinto[i])):
            if laberinto[i][j] == 'S':
                return (i, j)
    return None


def resolver_laberinto(laberinto):
    """
    Encuentra el camino más corto desde 'S' hasta 'E' usando BFS.
    Retorna el número mínimo de pasos, o -1 si no hay camino.

    Ejemplo:
        laberinto = ["S..",
                     "##.",
                     "..E"]
        resolver_laberinto(laberinto) → 4
    """
    filas = len(laberinto) 
    columnas = len(laberinto[0])

    inicio = encontrar_inicio(laberinto)
    visitado = [[False] * columnas for _ in range(filas)]

    # Cola BFS: cada elemento es (fila, columna, pasos_recorridos)
    cola = [(*inicio, 0)]
    visitado[inicio[0]][inicio[1]] = True

    while cola:
        fila, columna, pasos = cola.pop(0)


        if laberinto[fila][columna] == 'E':
            return int(pasos)

        for df, dc in DIRECCIONES:
            f, c = fila + df, columna + dc

            print(f,c)

            if 0 <= f < filas and 0 <= c < columnas:
                if not visitado[f][c] and laberinto[f][c] != "#":
                    visitado[f][c] = True
                    print(visitado)
                    cola.append((f, c, pasos + 1))

    return -1
[(0, 1), (0, -1), (1, 0), (-1, 0)]
laberinto = ["S...",
             "##..",
            "...E"]


print(resolver_laberinto(laberinto))