# Simulacro 1 — Desafio 2: Analisis Temporal sobre CSV de Reproducciones
import os
import csv



def reproducciones_por_hora(file_name):
    """
    Cuenta cuantas reproducciones hay por hora del dia.
    La hora se extrae del campo 'hora' (formato HH:MM) tomando los primeros 2 caracteres.

    Retorna dict con claves string de 2 digitos, solo horas con al menos una reproduccion:
        {"08": 3, "09": 2, ...}
    """
    base = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base, file_name)
    with open(path,"r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        dic = {}
        for row in reader:
            hora = row["hora"][:2]
            if hora not in dic:
                dic[hora] =1
            else:
                dic[hora] +=1
        return dic


def duracion_total_por_fecha(file_name):
    """
    Suma la duracion_seg total de todas las reproducciones por fecha.

    Retorna dict:
        {"2024-05-01": 1243, "2024-05-02": 1590, "2024-05-03": 1228}

    Nota: duracion_seg es entero.
    """
    base = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base, file_name)
    with open(path,"r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        dic = {}
        for row in reader:
            fecha = row["fecha"]
            if fecha not in dic:
                dic[fecha] = int(row["duracion_seg"])
            else:
                dic[fecha] += int(row["duracion_seg"])
        return dic



def artista_mas_escuchado_por_dia(file_name):
    """
    Para cada fecha, encuentra el artista con mas reproducciones ese dia.
    En caso de empate, retorna el que aparece primero alfabeticamente.

    Retorna dict:
        {"2024-05-01": "Daddy Yankee", "2024-05-02": "Daddy Yankee", "2024-05-03": "Daddy Yankee"}
    """
    base = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base, file_name)
    with open(path,"r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fechas = []
        for row in reader:
            fecha = row["fecha"]
            if fecha not in fechas:
                fechas.append(fecha)
    with open(path,"r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        maximo = []
        for fecha in fechas:
            artistas = {}
            for row in reader:
                if fecha == row["fecha"]:
                    artista = row["artista"]
                    if artista not in artistas:
                        artistas[artista] = 1
                    else:
                        artistas[artista] +=1
            ordenados = sorted(artistas,key=lambda x: x[1])
            print(ordenados)
                
      


        
