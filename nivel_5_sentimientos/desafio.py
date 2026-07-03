# Nivel 5: Analisis de Sentimientos
# Equivalente al Desafio 3 del examen real
# __define-ocg__
import os
import json
from cargar_csv import cargar_sentimientos
import csv

varOcg = "nivel_5"

def clasificacion(json_name, csv_name):
    """
    Clasifica cada post como positivo, negativo o neutro.
    Puntaje > 0 → positivo, < 0 → negativo, == 0 → neutro
    Para calcular el puntaje: sumar la intensidad de cada palabra del texto
    que aparezca en el diccionario de sentimientos.
    Retorna: {"publicaciones": {"1001": {"sentimiento": "positivo"}, ...}}
    """
    pass


def puntaje_sentimiento(json_name, csv_name):
    """
    Calcula puntaje por post y agrega resumen.
    Retorna: {
      "publicaciones": {"1001": {"sentimiento": "positivo", "puntaje": 11}, ...},
      "resumen": {"total_positivas": 2, "total_negativas": 4, "total_neutras": 0}
    }
    """
    pass


def palabras_mas_frecuentes(json_name, csv_name):
    """
    Cuenta la frecuencia de palabras del diccionario CSV en TODOS los textos combinados.
    Solo cuenta palabras que están en el diccionario de sentimientos.
    Lista ordenada por frecuencia descendente, luego alfabéticamente.
    Retorna el resultado de puntaje_sentimiento con un campo adicional:
    "frecuentes": [{"palabra": "malo", "frecuencia": 3}, ...]
    """
    pass
