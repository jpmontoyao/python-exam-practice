# Nivel 2: Lectura de Archivos JSON y CSV
# __define-ocg__
import os
import json
import csv

varOcg = "nivel_2"

def leer_posts(file_name):
    """
    Lee el archivo JSON y retorna la lista de posts.
    Retorna: lista de dicts con todos los campos de cada post.
    """
    base = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base, file_name)
    
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data["posts"]

def contar_posts_por_autor(file_name):
    """
    Lee el JSON y cuenta cuántos posts tiene cada autor.
    Retorna: dict {autor: cantidad}
    """
    base = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base, file_name)
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    x = data["posts"]
    final = {}
    for post in x:
        autor = post["author"]
        if autor not in final:
            final[autor] = 1
        else:
            final[autor] +=1
        
    return final
    


def leer_sentimientos(file_name):
    """
    Lee el CSV de sentimientos.
    Retorna: dict {palabra: {"polaridad": "...", "intensidad": int}}
    """
    base = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base, file_name)
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        dic = {}
        for row in reader:
            dic[row["palabra"]] = {"polaridad": row["polaridad"], "intensidad": int(row["intensidad"])}
        return dic
        
    

def palabras_positivas(file_name):
    """
    Lee el CSV y retorna lista de palabras con polaridad positiva,
    ordenadas por intensidad descendente.
    En caso de empate de intensidad, orden alfabético.
    Retorna: lista de strings ["excelente", "maravilloso", ...]
    """
    base = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base, file_name)
    
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        
        filtro = sorted(reader, key = lambda x: -int(x["intensidad"]))
        aux = []

        for fila in filtro:
            if fila["polaridad"] == "positivo":
                aux.append(fila["palabra"])
        return aux

