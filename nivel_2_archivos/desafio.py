# Nivel 2: Lectura de Archivos JSON y CSV
# __define-ocg__
import os # es un mósulo de Pyhton para interactuar con el sistema operativo, principalmente para rutas y archivos.
import json
import csv


varOcg = "nivel_2"


def leer_posts(file_name):
    """
    Lee el archivo JSON y retorna la lista de posts.
    Retorna: lista de dicts con todos los campos de cada post.
    """
    archivo = file_name
    base = os.path.dirname(os.path.abspath(__file__)) # dirname me da la carpeta del archivo en donde quiero abrir el otro.
                                                      # abspath me da la ruta completa desde le directorio en donde estoy parada
    path = os.path.join(base, archivo) #esto me une la carpeta en la que estoy, con el nombre del archivo que quiero abrir
                                       # si el archivo que quiero abrir esta en una carpeta diferente a la del archivo en
                                       # donde estoy programando el comando tiene que ser 
                                       # path = os.path.join(base, "nombre_carpeta", file_name) 
                                       # para subir de nivel, en caso de que el archivo este en otra carpeta fue el comando es
                                       # path = os.path.join(base, "..", "nombre_carpeta", file_name)  
    # print (base)
    # print (path)

    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
        lista = list(data["posts"]) 
        return lista


def contar_posts_por_autor(file_name):
    """
    Lee el JSON y cuenta cuántos posts tiene cada autor.
    Retorna: dict {autor: cantidad}
    """
    archivo = file_name
    base = os.path.dirname(os.path.abspath(__file__)) 
    path = os.path.join(base, archivo)
    
    with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
            lista = list(data["posts"]) 
    dic ={}
    for i in range(len(lista)): 
        post = lista[i]
        autor = post["author"]
        if autor in dic:
             dic[autor] += 1
        else:
             dic[autor] = 1

    return dic
         


def leer_sentimientos(file_name):
    """
    Lee el CSV de sentimientos.
    Retorna: dict {palabra: {"polaridad": "...", "intensidad": int}}
    """
    archivo = file_name
    base = os.path.dirname(os.path.abspath(__file__)) 
    path = os.path.join(base, archivo)
    
    with open(path, "r", encoding="utf-8") as file:
        data = csv.DictReader(file) # para usar esto siemre se tiene que usar un for row in data
        dic = {}
        for row in data: # row es una diccionario con las key igual a las columnas del archivo csv, y los values los valores de cada fila
            dic[row["palabra"]] = {"polaridad" : row["polaridad"], "intensidad" : int(row["intensidad"])}
        return dic
    

def palabras_positivas(file_name):
    """
    Lee el CSV y retorna lista de palabras con polaridad positiva,
    ordenadas por intensidad descendente.
    En caso de empate de intensidad, orden alfabético.
    Retorna: lista de strings ["excelente", "maravilloso", ...]
    """
    archivo = file_name
    base = os.path.dirname(os.path.abspath(__file__)) 
    path = os.path.join(base, archivo)
    
    with open(path, "r", encoding="utf-8") as file:
        data = csv.DictReader(file)
        lista = []
        
        for row in data:
            dic = {}
            if row["polaridad"] == "positivo":
                dic["palabra"] = row["palabra"]
                dic["intensidad"] = int(row["intensidad"])
                lista.append(dic)
        
        ordenada = sorted(lista, key=lambda x: (-x["intensidad"], x["palabra"]))  
        
        palabras = []
        for i in range(len(ordenada)):
            palabras.append(ordenada[i]["palabra"])
        
        return palabras
        

            


palabras_positivas("sentimientos.csv")
