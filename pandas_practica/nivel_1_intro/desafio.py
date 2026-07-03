# Nivel 1 Pandas — Introducción: cargar e iterar
import pandas as pd



def cargar_datos(path):
    """
    Carga bibliotecas.csv usando pandas.
    Imprime número de filas y número de columnas.
    Retorna el DataFrame cargado.

    Pista:
        df = pd.read_csv(path, sep=',', encoding='utf-8')
        df.shape → (filas, columnas)
    """
    df = pd.read_csv(path, sep=",",encoding= "utf-8")
    print(df.shape[0])
    print(df.shape[1])
    return df


def contar_por_tipo_usuario(df):
    """
    Recorre el DataFrame fila a fila con iterrows() y cuenta
    cuántos registros hay por cada TIPO_USUARIO.

    Retorna dict:
        {"Estudiante": 11, "Adulto": 9}

    Pista:
        for i, row in df.iterrows():
            tipo = row['TIPO_USUARIO']
    """
    datos = df
    dic = {}
    for i, row in datos.iterrows():
        tipo = row["TIPO_USUARIO"]
        if tipo not in dic:
            dic[tipo] = 1
        else:
            dic[tipo] +=1
    return dic
    


def total_libros_por_mes(df):
    """
    Recorre el DataFrame fila a fila con iterrows() y suma
    Libros_Prestados agrupando por Mes.

    Retorna dict con claves int (el número de mes):
        {3: 12, 4: 10, 5: 12, 6: 9}
    """
    datos = df
    dic = {}
    for i, row in datos.iterrows():
        mes = row["Mes"]
        if mes not in dic:
            dic[mes] = row["Libros_Prestados"]
        else:
            dic[mes] += row["Libros_Prestados"]
    return dic

