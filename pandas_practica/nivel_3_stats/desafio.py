# Nivel 3 Pandas — Stats: construir diccionario desde DataFrame limpio
import pandas as pd



def construir_stats(df):
    """
    Recibe el DataFrame ya limpio (con columnas 'comuna_key' y 'Tipo_Dia').
    Construye y retorna stats_comunas (dict) recorriendo con iterrows().

    Clave: comuna_key (str en minúsculas)
    Valor: dict con:
        - nombre_comuna      : str  (valor original de COMUNA)
        - cod_region         : int  (COD_REGION)
        - libros_total       : int  (suma de Libros_Prestados)
        - multas_total       : int  (suma de Multas, ya corregidas)
        - registros_fin_semana: int (filas donde Tipo_Dia == 'FIN_DE_SEMANA')
        - total_registros    : int  (total de filas de esa comuna)
        - registros_por_mes  : dict {mes_int: conteo}

    Ejemplo de resultado:
        {
          'santiago': {
              'nombre_comuna': 'Santiago', 'cod_region': 13,
              'libros_total': 17, 'multas_total': 1500,
              'registros_fin_semana': 2, 'total_registros': 8,
              'registros_por_mes': {3: 2, 4: 2, 5: 2, 6: 2}
          }, ...
        }
    """
    stats = {}
    for i, row in df.iterrows():
        key = row["comuna_key"]
        if row["comuna_key"] not in stats:
            stats[row["comuna_key"]]={
                "nombre_comuna":row["COMUNA"],
                "cod_region": row["COD_REGION"],
                "libros_total": 0,
                "multas_total": 0,
                "registros_fin_semana": 0,
                "total_registros" : 0,
                "registros_por_mes": {}
            }
        
        stats[key]["libros_total"] += int(row["Libros_Prestados"])
        stats[key]["multas_total"] += int(row["Multas"])
        if row["Tipo_Dia"]== "FIN_DE_SEMANA":
            stats[key]["registros_fin_semana"] += 1 
        stats[key]["total_registros"] += 1
        mes = int(row["Mes"])
        if mes not in stats[key]["registros_por_mes"]:
            stats[key]["registros_por_mes"][mes] =1
        else:
            stats[key]["registros_por_mes"][mes] +=1
    print(stats)
    return stats







def ranking_libros(stats_comunas):
    """
    Recorre stats_comunas con un ciclo for y construye una lista de dicts:
        [{'comuna': str, 'cod_region': int, 'libros_total': int,
          'registros_fin_semana': int, 'total_registros': int}, ...]

    Ordena la lista de MAYOR a MENOR libros_total usando un ciclo for
    (selection sort). No uses sorted() ni lambda.

    Retorna la lista ordenada.

    Pista selection sort:
        for i in range(len(lista)):
            max_idx = i
            for j in range(i+1, len(lista)):
                if lista[j]['libros_total'] > lista[max_idx]['libros_total']:
                    max_idx = j
            lista[i], lista[max_idx] = lista[max_idx], lista[i]
    """
    lista = []

    for comuna in stats_comunas:
    
        x = {"comuna":stats_comunas[comuna]["nombre_comuna"],
             "cod_region": stats_comunas[comuna]["cod_region"],
             "libros_total": stats_comunas[comuna]["libros_total"],
             "registros_fin_semana": stats_comunas[comuna]["registros_fin_semana"],
             "total_registros": stats_comunas[comuna]["total_registros"]
             }
        lista.append(x)

        lista.sort(key= lambda x : -x["libros_total"])
   
    return lista
