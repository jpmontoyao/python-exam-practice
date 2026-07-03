# Nivel 1: Warmup - Estructuras de Datos Básicas
# No se requiere leer archivos en este nivel


def filtrar_mayores(numeros, umbral):
    """Filtra números mayores que el umbral y retorna la lista ordenada."""
    n  = len(numeros)
    aux = []
    for i in range(n):
        if numeros[i] > umbral:
            aux.append(numeros[i])
    return aux

def contar_palabras(texto):
    """
    Cuenta la frecuencia de cada palabra en el texto (case-insensitive).
    Retorna un dict {palabra: frecuencia}.
    Ejemplo: "hola mundo hola" → {"hola": 2, "mundo": 1}
    """
    dic = {}
    aux = texto.lower()
    lista = aux.split()

    for i in range(len(lista)):
        if lista[i] not in dic:
            dic[lista[i]] = 1
        else:
            dic[lista[i]] +=1
    return dic


def top_n_frecuentes(frecuencias, n):
    """
    Dado un dict {elemento: frecuencia}, retorna los n más frecuentes.
    Retorna lista de dicts [{"elemento": ..., "frecuencia": ...}]
    ordenada de mayor a menor frecuencia, y en caso de empate por orden alfabético.
    """
    orden = [{"elemento": x , "frecuencia": y} for x,y in frecuencias.items()]
    filtro_1 = sorted(orden, key = lambda x: x["frecuencia"], reverse= True)
    aux = []
    for i in range(n):
        aux.append(filtro_1[i])
    filtro_2 = sorted(aux, key= lambda x: x["elemento"], reverse= True)
    return filtro_2

def agrupar_por_longitud(palabras):
    """
    Agrupa palabras por su longitud.
    Retorna dict {longitud: [palabras]} con palabras en orden de aparición.
    """
    dic = {}
    for i in range(len(palabras)):
        if len(palabras[i]) not in dic:
            dic[len(palabras[i])] = []
        dic[len(palabras[i])].append(palabras[i])
    return dic
            

