# Nivel 3: Filtros y Extraccion de Datos
# Equivalente al Desafio 1 del examen real
import os
import json


def mas_de_1000_seguidores(file_name):
    """
    Filtra posts donde el autor tiene más de 1000 seguidores.
    Retorna: lista de dicts [{"id": ..., "text": ..., "author": ...}]
    en el mismo orden que aparecen en el JSON.
    """
    base = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base, file_name)
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    df = data["posts"]
    lista = []
    for post in df:
        dic = {}
        if post["author_followers"] > 1000:
            dic = {"id": post["id"], "text": post["text"], "author": post["author"]}
            lista.append(dic)
    return lista


def al_menos_100_interacciones_totales(file_name):
    """
    Filtra posts con al menos 100 interacciones totales (retweets + likes + replies).
    Retorna: lista de dicts [{"id": ..., "text": ..., "author": ...}]
    en el mismo orden que aparecen en el JSON.
    """
    base = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base, file_name)
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    df = data["posts"]
    lista = []
    for post in df:
        dic = {}
        if int(len(post["retweets"])) + int(len(post["likes"])) + int(len(post["replies"])) >= 100:
            dic = {"id": post["id"], "text": post["text"], "author": post["author"]}
            lista.append(dic)
    return lista



def fecha_ultimo_retweet_like_respuesta(file_name):
    """
    Para posts con >= 100 interacciones totales, incluye las últimas fechas.
    Retorna: lista de dicts con id, text, author, y last_interactions:
    {
      "last_retweet": "...",
      "last_like": "...",
      "last_reply": "..."
    }
    El orden de los posts es el mismo que en el JSON.
    Nota: la última fecha es el último elemento de la lista (índice -1).
    """
    base = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base, file_name)
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    df = data["posts"]

    lista = []
    for post in df:
        dic = {}
        if int(len(post["retweets"])) + int(len(post["likes"])) + int(len(post["replies"])) >= 100:
            dic = {"id": post["id"], "text": post["text"], "author": post["author"], "last_interactions":{"last_retweet": post["retweets"][-1]["date"],
             "last_like": post["likes"][-1]["date"],
             "last_reply": post["replies"][-1]["date"]}}
            lista.append(dic)
    return lista


