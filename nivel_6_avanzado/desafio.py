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
    pass


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
    pass


def resumen_diario(file_name):
    """
    Agrupa posts por fecha (YYYY-MM-DD) y calcula por cada día:
    - total_posts: cantidad de posts ese día
    - total_interacciones: suma de retweets + likes + replies de todos los posts del día
    - autor_mas_activo: autor con más posts ese día (empate → orden alfabético)

    Retorna: {"dias": {"2024-11-15": {"total_posts": ..., "total_interacciones": ..., "autor_mas_activo": ...}, ...}}
    """
    pass
