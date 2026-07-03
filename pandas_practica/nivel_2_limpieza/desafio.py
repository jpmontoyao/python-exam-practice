# Nivel 2 Pandas — Limpieza: modificar columnas iterando
import pandas as pd
from datetime import datetime



def corregir_negativos(df):
    """
    Recorre el DataFrame fila a fila con iterrows().
    Si Multas o Dias_Atraso es negativo, reemplaza por 0.

    Modifica el DataFrame en el lugar y lo retorna.
    Imprime cuántos valores negativos corrigió en total.

    Pista para modificar una celda:
        df.at[i, 'Multas'] = 0
    """
    data = df
    contador = 0
    for i, row in data.iterrows():
        multas = row["Multas"]
        atraso = row["Dias_Atraso"]
        if multas < 0:
            contador +=1
            df.at[i,"Multas"] =0
        if atraso <0:
            contador +=1
            df.at[i,"Dias_Atraso"] = 0
    print(contador)
    return df



def agregar_columnas(df):
    """
    Recorre el DataFrame fila a fila con iterrows() y agrega
    dos columnas nuevas:

      - 'comuna_key': COMUNA.strip().lower()
      - 'Tipo_Dia':   usando datetime.strptime(row['Fecha'], '%Y/%m/%d')
                      weekday() >= 5 → 'FIN_DE_SEMANA'
                      weekday() <  5 → 'DÍA_HÁBIL'

    Retorna el DataFrame con las dos columnas nuevas.

    Pista para parsear fecha:
        d = datetime.strptime(row['Fecha'], '%Y/%m/%d')
        d.weekday()  →  0=lunes ... 5=sábado, 6=domingo
    """
    for i,row in df.iterrows():
        df.at[i,"comuna_key"] = row["COMUNA"].strip().lower()
        d = datetime.strptime(row["Fecha"], "%Y/%m/%d")
        if d.weekday() >4:
            df.at[i,"Tipo_Dia"] = "FIN_DE_SEMANA"
        else:
            df.at[i,"Tipo_Dia"] = "DÍA_HÁBIL"
    return df



def limpiar_completo(df):
    """
    Aplica corregir_negativos y luego agregar_columnas en ese orden.
    Retorna el DataFrame limpio y con las columnas nuevas.
    """
    data_limpia = corregir_negativos(df)
    final = agregar_columnas(data_limpia)
    return final
