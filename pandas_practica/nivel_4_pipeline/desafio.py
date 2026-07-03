# Nivel 4 Pandas — Pipeline completo con dos fuentes
# Tema: ventas de farmacias por sucursal y comuna
import os
import csv
import pandas as pd
from datetime import datetime


def cargar_ventas(path):
    """
    Carga ventas.csv (sep=',', encoding='utf-8').
    Imprime: número de filas, columnas y distribución de registros por mes.
    Retorna el DataFrame.
    """
    pass


def cargar_sucursales(path):
    """
    Carga sucursales.csv (sep=',', encoding='utf-8') con pandas.
    Con un ciclo for sobre iterrows(), construye un dict:
        { nombre_sucursal: poblacion_int }
    Imprime las sucursales cargadas con su población.
    Retorna el dict.
    """
    pass


def limpiar_ventas(df):
    """
    Recorre fila a fila con iterrows(). Para cada fila:
      - Si Descuento es negativo → reemplaza por 0.
      - Agrega columna 'sucursal_key' = SUCURSAL.strip().lower()
      - Agrega columna 'Tipo_Dia':
            weekday() >= 5 → 'FIN_DE_SEMANA', si no → 'DÍA_HÁBIL'
      - Agrega columna 'venta_total' = Unidades * Precio_Unit  (int)
    Imprime distribución de Tipo_Dia y suma total de Descuento corregido.
    Retorna el DataFrame modificado.
    """
    pass


def construir_stats(df, pob_dict):
    """
    Recorre df fila a fila con iterrows() y construye stats_sucursales (dict).

    Clave: sucursal_key
    Valor: dict con:
        - nombre_sucursal  : str
        - region           : str   (desde sucursales.csv, 'Desconocida' si no hay match)
        - poblacion        : int   (desde pob_dict, 0 si no hay match)
        - ventas_total     : int   (suma de venta_total)
        - unidades_total   : int   (suma de Unidades)
        - ventas_fin_semana: int   (conteo de filas con Tipo_Dia == 'FIN_DE_SEMANA')
        - total_registros  : int
        - ventas_por_mes   : dict  {mes_int: conteo}

    Imprime total de sucursales y cuántas sin match de población.
    Retorna stats_sucursales.
    """
    pass


def ventas_por_mes(stats_sucursales):
    """
    Recorre stats_sucursales con ciclo for anidado sobre ventas_por_mes
    para construir resumen_meses (dict):
        { mes_int: { 'total_registros': int, 'es_peak': bool } }
    donde es_peak = True solo para el mes con más registros a nivel nacional.
    Para encontrar el peak usa un ciclo for (sin max()).
    Imprime los meses con su total e indica cuál es el peak.
    Retorna resumen_meses.
    """
    pass


def sucursales_eficientes(stats_sucursales):
    """
    Calcula la tasa de ventas nacional:
        tasa_nacional = (suma ventas_total / suma poblacion) * 100000

    Filtra sucursales que cumplen AMBAS condiciones:
        - poblacion > 300000
        - tasa_ventas < tasa_nacional
          donde tasa_ventas = (ventas_total / poblacion) * 100000

    Para cada sucursal filtrada agrega:
        - 'tasa_ventas'    : round(ventas_total / poblacion * 100000, 2)
        - 'pct_fin_semana' : round(ventas_fin_semana / total_registros * 100, 2)

    Imprime cuántas sucursales cumplen el criterio.
    Retorna lista de dicts: [{ sucursal, region, poblacion, ventas_total,
                                tasa_ventas, pct_fin_semana }, ...]
    """
    pass


def calcular_ivs(stats_sucursales):
    """
    Calcula el Índice de Ventas por Sucursal (IVS):
        IVS = round((ventas_total / poblacion) * 100000, 2)

    Omite sucursales con poblacion == 0.

    Construye lista de dicts:
        { 'sucursal', 'region', 'poblacion', 'ventas_total',
          'unidades_total', 'pct_fin_semana', 'ivs' }

    donde pct_fin_semana = round(ventas_fin_semana / total_registros * 100, 2)

    Ordena de MAYOR a MENOR ivs.
    Retorna la lista ordenada.
    """
    pass


def clasificar_y_exportar(lista_ivs, output_path):
    """
    Recorre lista_ivs con un ciclo while y asigna campo 'categoria':
        IVS >= 25000        → 'ALTA'
        15000 <= IVS < 25000 → 'MEDIA'
        IVS < 15000         → 'BAJA'

    Exporta a output_path un CSV con el módulo csv estándar (no pandas)
    con columnas: sucursal, region, poblacion, ventas_total,
                  unidades_total, pct_fin_semana, ivs, categoria

    Imprime conteo por categoría.
    Retorna lista_ivs con el campo 'categoria' añadido.
    """
    pass
