# Nivel 5: Analisis de Sentimientos
# Equivalente al Desafio 3 del examen real
import os
import json
from cargar_csv import cargar_sentimientos
import csv


def clasificacion(json_name, csv_name):
    """
    Clasifica cada post como positivo, negativo o neutro.
    Puntaje > 0 → positivo, < 0 → negativo, == 0 → neutro
    Para calcular el puntaje: sumar la intensidad de cada palabra del texto
    que aparezca en el diccionario de sentimientos.
    Retorna: {"publicaciones": {"1001": {"sentimiento": "positivo"}, ...}}
    """
    base = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(base, json_name)
    csv_path = os.path.join(base, csv_name)
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    datos = data["posts"]
    with open(csv_path, "r", encoding= "utf-8") as f:
        reader = csv.DictReader(f)
        valores = {}
        for row in reader:
            valores[row["palabra"]] = row["intensidad"]
        dic = {}    

        for post in datos:
            texto = post["text"].split()
            contador = 0
            sentimiento = ""
            for palabra in texto:
                if palabra in valores:
                    contador += int(valores[palabra])
            if contador > 0:
                dic[post["id"]] = {"sentimiento" :"positivo"}
            elif contador == 0:
                dic[post["id"]] = {"sentimiento" :"neutro"}
            elif contador < 0 :
                dic[post["id"]] = {"sentimiento" :"negativo"}
    
        final = {"publicaciones": dic}
        return final

        

def puntaje_sentimiento(json_name, csv_name):
    """
    Calcula puntaje por post y agrega resumen.
    Retorna: {
      "publicaciones": {"1001": {"sentimiento": "positivo", "puntaje": 11}, ...},
      "resumen": {"total_positivas": 2, "total_negativas": 4, "total_neutras": 0}
    }
    """
    base = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(base, json_name)
    csv_path = os.path.join(base, csv_name)
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    datos = data["posts"]
    with open(csv_path, "r", encoding= "utf-8") as f:
        reader = csv.DictReader(f)
        valores = {}
        for row in reader:
            valores[row["palabra"]] = row["intensidad"]
        dic = {}    

        for post in datos:
            texto = post["text"].split()
            contador = 0
            sentimiento = ""
            for palabra in texto:
                if palabra in valores:
                    contador += int(valores[palabra])
            if contador > 0:
                dic[post["id"]] = {"sentimiento" :"positivo", "puntaje": contador}
            elif contador == 0:
                dic[post["id"]] = {"sentimiento" :"neutro", "puntaje": contador}
            elif contador < 0 :
                dic[post["id"]] = {"sentimiento" :"negativo", "puntaje": contador}
    
        buenas = 0
        malas= 0
        neutras = 0
        for i in dic:
            if dic[i]["sentimiento"] == "positivo":  
                buenas +=1
            elif dic[i]["sentimiento"] == "neutro":
                neutras +=1
            elif dic[i]["sentimiento"] == "negativo":
                malas +=1
        final = {"publicaciones": dic, "resumen":{"total_positivas": buenas, "total_negativas": malas, "total_neutras":neutras}}
        return final

    

def palabras_mas_frecuentes(json_name, csv_name):
    """
    Cuenta la frecuencia de palabras del diccionario CSV en TODOS los textos combinados.
    Solo cuenta palabras que están en el diccionario de sentimientos.
    Lista ordenada por frecuencia descendente, luego alfabéticamente.
    Retorna el resultado de puntaje_sentimiento con un campo adicional:
    "frecuentes": [{"palabra": "malo", "frecuencia": 3}, ...]
    """
    base = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(base, json_name)
    csv_path = os.path.join(base, csv_name)
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    datos = data["posts"]
    with open(csv_path, "r", encoding= "utf-8") as f:
        reader = csv.DictReader(f)
        dic = {}
        for row in reader:
            if row["palabra"] not in dic:
                dic[row["palabra"]] = 0
        for post in datos:
            frase = post["text"].split()
            for palabra in frase:
                if palabra in dic:
                    dic[palabra] +=1
        
        
        aux = []
        for dupla in dic:
            x = {"palabra":dupla, "frecuencia": dic[dupla]}
            aux.append(x)
        orden = sorted(aux, key = lambda x : (-int(x["frecuencia"]),x["palabra"]))
        x = puntaje_sentimiento(json_name, csv_name)
        x["frecuentes"] = orden
        return x



