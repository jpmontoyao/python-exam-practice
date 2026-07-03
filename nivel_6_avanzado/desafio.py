# Nivel 6: Avanzado - Engagement, Búsqueda y Agrupación
import os
import json


def top_engagement(file_name, n):
    """
    Calcula la tasa de engagement de cada post y retorna los top N.
    Engagement = (retweets + likes + replies) / author_followers * 100
    Redondear a 2 decimales.
    En caso de empate, ordenar por id ascendente.

    Retorna: lista de dicts [{"id": ..., "author": ..., "engagement_rate": ...}]
    ordenada de mayor a menor engagement_rate.
    """
    base = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base, file_name)
    with open(path,"r", encoding="utf-8") as f:
        data = json.load(f)
    datos = data["posts"]
    lista = []
    for post in datos:
        aux = (float(len(post["retweets"])) + float(len(post["likes"])) + float(len(post["replies"])))/ float(post["author_followers"])
        dic = {"id":post["id"], "author":post["author"],"engagement_rate": aux*100 }
        lista.append(dic)
    
    final = sorted(lista, key= lambda x: (-x["engagement_rate"],x["id"]))
    out = []
    for i in range(n):
        out.append(final[i])
    return out


def buscar_en_textos(file_name, keywords):
    """
    Busca posts que contengan AL MENOS UNA de las keywords en su texto.
    Normalización: lowercase + eliminar caracteres en '.,!?¡¿:;()' antes de comparar.
    keywords también se normalizan (lowercase).

    Retorna: lista de dicts [{"id": ..., "author": ..., "text": ..., "palabras_encontradas": [...]}]
    - palabras_encontradas: lista de keywords que SÍ aparecen en el texto (sin duplicados, orden de aparición en keywords)
    - Solo incluir posts donde se encontró al menos una keyword
    - Mantener orden original del JSON
    """
    base = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base, file_name)
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    datos = data["posts"]
    final = []
    for post in datos:
        f1 = post["text"].lower()
        string = ""
        for letra in f1:
            if letra not in ".,!?¡¿:;()":
                string += str(letra)

        x = string.split()
        palabras_encontradas = []
        for palabra in x:
            if palabra in keywords and palabra not in palabras_encontradas:
                palabras_encontradas.append(palabra)
        
        if len(palabras_encontradas) > 0:
            dic = {"id":post["id"], "author":post["author"],"text":post["text"], "palabras_encontradas":palabras_encontradas}
            final.append(dic)
    return final


def resumen_diario(file_name):
    """
    Agrupa posts por fecha (YYYY-MM-DD) y calcula por cada día:
    - total_posts: cantidad de posts ese día
    - total_interacciones: suma de retweets + likes + replies de todos los posts del día
    - autor_mas_activo: autor con más posts ese día (empate → orden alfabético)

    Retorna: {"dias": {"2024-11-15": {"total_posts": ..., "total_interacciones": ..., "autor_mas_activo": ...}, ...}}
    """
    base = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base, file_name)
    with open(path,"r", encoding="utf-8") as f:
        data = json.load(f)
    datos = data["posts"]
    fechas = {}
    for post in datos:
        if post["created_at"][:10] not in fechas:
            fechas[post["created_at"][:10]] = 1
        else: 
            fechas[post["created_at"][:10]] +=1

    print(fechas)




    
