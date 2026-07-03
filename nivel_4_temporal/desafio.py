# Nivel 4: Analisis Temporal
# Equivalente al Desafio 2 del examen real
# __define-ocg__
import os
import json
import datetime

varOcg = "nivel_4"

def distribucion_publicaciones(file_name):
    """
    Retorna distribución de publicaciones por hora del día (0-23).
    Retorna: {"distribucion": {"10": 3, "14": 1, ...}}
    Las claves son strings del número de hora.
    Solo incluye horas que tienen al menos una publicación.
    """
    archivo = file_name
    base = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base, archivo)

    with open(path, "r", encoding="utf-8") as file: 
        data = json.load(file)
        lista = list(data["posts"])
        dic = {}
        distribucion = {}
        for i in range(len(lista)):
            created = lista[i]["created_at"].split("T")
            hora_lista = created[1].split(":")
            hora = str(hora_lista[0])
            if hora == "00":
                hora ="0"
            if hora in distribucion:
                distribucion[hora] += 1
            else:
                distribucion[hora] = 1
        dic["distribucion"] = distribucion
    
    return dic
            
    

def rango_temporal(file_name):
    """
    Retorna el rango temporal (primera y última publicación).
    La primera publicación es la de menor created_at.
    La última publicación es la de mayor created_at.
    Retorna: {"rango": {"inicio": "...", "fin": "..."}}
    Las fechas se retornan en el mismo formato que están en el JSON.
    """
    
    archivo = file_name
    base = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base, archivo)

    with open(path, "r", encoding="utf-8") as file: 
        data = json.load(file)
        lista = list(data["posts"])
        fechas = []

        for i in range(len(lista)):
            fechas.append(lista[i]["created_at"])

        rango = {}
        dic = {}
        
        dic["inicio"] = min(fechas)
        dic["fin"] = max(fechas)
        
        rango["rango"] = dic

    return rango
