# Nivel 5g: Merge Sort
#
# Algoritmo de ordenamiento divide-and-conquer:
#   1. Dividir el arreglo en dos mitades
#   2. Ordenar cada mitad recursivamente
#   3. Fusionar las dos mitades ordenadas
#
# Dos funciones que se llaman entre sí — igual que en el buscaminas.
#


def merge(izq, der):
    """
    Fusiona dos listas ya ordenadas en una sola lista ordenada.

    Ejemplo:
        merge([1, 3, 5], [2, 4, 6]) → [1, 2, 3, 4, 5, 6]
    """
    resultado = []
    i = j = 0


    while i < len(izq) and j < len(der):
        if izq[i] < der[j]:
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1
   

    return resultado + izq[i:] + der[j:]  


def merge_sort(arr):
    """
    Ordena una lista de menor a mayor usando merge sort.

    Ejemplo:
        merge_sort([5, 2, 8, 1, 9]) → [1, 2, 5, 8, 9]
    """
    if len(arr) <= 1:
       
        return arr

    mid = len(arr) // 2
    izq = merge_sort(arr[:mid])
    der = merge_sort(arr[mid:])

    return merge(izq, der)

