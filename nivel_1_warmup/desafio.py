# Nivel 1: Warmup - Estructuras de Datos Básicas
# No se requiere leer archivos en este nivel
# __define-ocg__

varOcg = "nivel_1"

def filtrar_mayores(numeros, umbral):
    """Filtra números mayores que el umbral y retorna la lista ordenada."""
    lista_filtrada = []
    for num in numeros:
        if num > umbral:
            lista_filtrada.append(num)
    return sorted(lista_filtrada)


def contar_palabras(texto):
    """
    Cuenta la frecuencia de cada palabra en el texto (case-insensitive).
    Retorna un dict {palabra: frecuencia}.
    Ejemplo: "hola mundo hola" → {"hola": 2, "mundo": 1}
    """
    palabras = texto.lower().split()
    dic = {}
    for palabra in palabras: 
        if palabra in dic:
            dic[palabra] += 1
        else: 
            dic[palabra] = 1

    return dic


def top_n_frecuentes(frecuencias, n):
    """
    Dado un dict {elemento: frecuencia}, retorna los n más frecuentes.
    Retorna lista de dicts [{"elemento": ..., "frecuencia": ...}]
    ordenada de mayor a menor frecuencia, y en caso de empate por orden alfabético.
    """
    dic = frecuencias
    keys = list(dic.keys())
    values = list(dic.values())
    lista = []

    for i in range(len(keys)):
        dic= {}
        dic["elemento"] = keys[i]
        dic["frecuencia"] = values[i]
        lista.append(dic)

    ordenada = sorted(lista, key=lambda x: (-x["frecuencia"], x["elemento"]))     
    return ordenada[:n] 
    

def agrupar_por_longitud(palabras):
    """
    Agrupa palabras por su longitud.
    Retorna dict {longitud: [palabras]} con palabras en orden de aparición.
    """

    lista = palabras
    dic = {}
    for i in range(len(lista)):
        largo = len(lista[i])
        
        if largo in dic:
            dic[largo].append(lista[i])
        else: 
            value = [lista[i]]
            dic[largo] = value

    return dic


