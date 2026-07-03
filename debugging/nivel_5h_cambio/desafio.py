# Nivel 5h: Calculadora de Cambio
#
# Dos funciones que trabajan juntas:
#   - dar_cambio: algoritmo greedy que usa la moneda más grande posible
#   - cantidad_por_denominacion: agrupa el resultado por tipo de moneda
#
# Las dos funciones tienen bugs — si dar_cambio falla, la segunda
# también falla aunque su lógica esté bien. Igual que en el buscaminas.
#


def dar_cambio(monto, monedas):
    """
    Retorna la lista de monedas usadas para dar cambio exacto (greedy).
    Usa siempre la moneda más grande posible.
    Retorna [] si no es posible dar cambio exacto.

    Ejemplo:
        dar_cambio(160, [100, 50, 10, 5, 1]) → [100, 50, 10]
        dar_cambio(30, [25, 10])             → []  (no se puede dar exacto)
    """
    monedas_ordenadas = sorted(monedas, reverse= True)
    resultado = []

    for moneda in monedas_ordenadas:
        while monto >= moneda:
            resultado.append(moneda)
            monto -= moneda

    if monto == 0:
        return resultado
    return []


def cantidad_por_denominacion(cambio):
    """
    Dado el resultado de dar_cambio, retorna cuántas monedas hay de cada tipo.

    Ejemplo:
        cantidad_por_denominacion([100, 50, 10]) → {100: 1, 50: 1, 10: 1}
        cantidad_por_denominacion([10, 10, 5])   → {10: 2, 5: 1}
    """
    conteo = {}
    for moneda in cambio:
        if moneda not in conteo:
            conteo[moneda] = 1
        else:
            conteo[moneda] += 1
    return conteo

