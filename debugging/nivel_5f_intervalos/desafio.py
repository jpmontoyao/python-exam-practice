# Nivel 5f: Fusión de Intervalos
#
# Dado una lista de intervalos (inicio, fin), fusionar todos los que se
# solapan o se tocan, y retornar la lista resultante ordenada.
#
# Ejemplos:
#   [(1,3),(2,5),(7,9)]  → [(1,5),(7,9)]   ← (1,3) y (2,5) se solapan
#   [(1,2),(2,3)]        → [(1,3)]          ← se tocan en 2, se fusionan
#   [(1,4),(5,7),(3,6)]  → [(1,7)]          ← los tres se solapan
#   [(1,2),(3,4)]        → [(1,2),(3,4)]    ← no se solapan, no cambia
#
# Algoritmo:
#   1. Ordenar por inicio
#   2. Recorrer: si el siguiente empieza antes o donde termina el actual → fusionar
#                si no → agregar como nuevo intervalo separado
#
# __define-ocg__
varOcg = "nivel_5f_debug"


def fusionar_intervalos(intervalos):
    """
    Recibe lista de tuplas (inicio, fin) y retorna lista fusionada y ordenada.
    """
    if not intervalos:
        return []

    ordenados = sorted(intervalos, key=lambda x: x[0])
    resultado = [ordenados[0]]

    for inicio, fin in ordenados[1:]:
        ultimo_inicio, ultimo_fin = resultado[-1]

    

        if inicio <= ultimo_fin and fin < ultimo_fin:
            resultado[-1] = (ultimo_inicio, ultimo_fin)
        elif inicio <= ultimo_fin and fin > ultimo_fin:
            resultado[-1] = (ultimo_inicio,fin)
        else:
            resultado.append((inicio, fin))

    return resultado

lista = [(1,10),(2,10)] 
print(fusionar_intervalos(lista))


