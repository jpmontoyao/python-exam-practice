# Nivel 3: Filtros y Extraccion de Datos
# Equivalente al Desafio 1 del examen real
# __define-ocg__
import os
import json

varOcg = "nivel_3"

def mas_de_1000_seguidores(file_name):
    """
    Filtra posts donde el autor tiene más de 1000 seguidores.
    Retorna: lista de dicts [{"id": ..., "text": ..., "author": ...}]
    en el mismo orden que aparecen en el JSON.
    """
    archivo = file_name
    base = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base, archivo)

    with open(path, "r", encoding="utf-8") as file: 
        data = json.load(file)
        lista = list(data["posts"])
        list_filtrada = []
        for i in range(len(lista)):
            if lista[i]["author_followers"] > 1000:
                dic = {}
                dic["id"] = lista[i]["id"]
                dic["text"] = lista[i]["text"]
                dic["author"] = lista[i]["author"]
                list_filtrada.append(dic)
    return list_filtrada
    


def al_menos_100_interacciones_totales(file_name):
    """
    Filtra posts con al menos 100 interacciones totales (retweets + likes + replies).
    Retorna: lista de dicts [{"id": ..., "text": ..., "author": ...}]
    en el mismo orden que aparecen en el JSON.
    """
    archivo = file_name
    base = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base, archivo)

    with open(path, "r", encoding="utf-8") as file: 
        data = json.load(file)
        lista = list(data["posts"])
        list_filtrada = []
        for i in range(len(lista)):
            total_interacciones = len(lista[i]["retweets"]) + len(lista[i]["likes"]) + len(lista[i]["replies"])
            if total_interacciones >= 100: 
                dic = {}
                dic["id"] = lista[i]["id"]
                dic["text"] = lista[i]["text"]
                dic["author"] = lista[i]["author"]
                list_filtrada.append(dic)
    return list_filtrada



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
    archivo = file_name
    base = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base, archivo)

    with open(path, "r", encoding="utf-8") as file: 
        data = json.load(file)
        lista = list(data["posts"])
        list_filtrada = []
        for i in range(len(lista)):
            total_interacciones = len(lista[i]["retweets"]) + len(lista[i]["likes"]) + len(lista[i]["replies"])
            if total_interacciones >= 100: 
                dic = {}
                dic_interacciones = {}
                dic_interacciones["last_retweet"] = lista[i]["retweets"][-1]["date"]
                dic_interacciones["last_like"] = lista[i]["likes"][-1]["date"]
                dic_interacciones["last_reply"] = lista[i]["replies"][-1]["date"]
                dic["id"] = lista[i]["id"]
                dic["text"] = lista[i]["text"]
                dic["author"] = lista[i]["author"]
                dic["last_interactions"] = dic_interacciones
                
                list_filtrada.append(dic)
    return list_filtrada

