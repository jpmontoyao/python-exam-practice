# Nivel 4: Analisis Temporal
# Equivalente al Desafio 2 del examen real
# __define-ocg__
import os
import json

varOcg = "nivel_4"

def distribucion_publicaciones(file_name):
    """
    Retorna distribución de publicaciones por hora del día (0-23).
    Retorna: {"distribucion": {"10": 3, "14": 1, ...}}
    Las claves son strings del número de hora.
    Solo incluye horas que tienen al menos una publicación.
    """
    base = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base, file_name)
    with open(path, "r", encoding= "utf-8") as f:
        data = json.load(f)
    df = data["posts"]
    dic = {}
    for post in df:
        x = post["created_at"][11:13]
        if x not in dic and x != "00":
            dic[post["created_at"][11:13]] = 1
        elif x not in dic and x == "00":
            dic["0"] = 1
        elif x in dic and x != "00":
            dic[post["created_at"][11:13]] += 1
        elif x in dic and x == "00": 
            dic["0"] += 1
    aux = {"distribucion": dic}
    return aux

def rango_temporal(file_name):
    """
    Retorna el rango temporal (primera y última publicación).
    La primera publicación es la de menor created_at.
    La última publicación es la de mayor created_at.
    Retorna: {"rango": {"inicio": "...", "fin": "..."}}
    Las fechas se retornan en el mismo formato que están en el JSON.
    """
    base = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base, file_name)
    with open(path, "r", encoding= "utf-8") as f:
        data = json.load(f)
    df = data["posts"]
    fechas = []
    for post in df:
        fechas.append(post["created_at"])

    maxima = max(fechas)
    minima = min(fechas)
    rango = {"rango":{"inicio":minima, "fin": maxima}}
    return rango