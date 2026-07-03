# Nivel 8: Análisis Temporal sobre CSV de Accesos
# Equivalente al Desafio 2 del examen — pero con CSV en vez de JSON
import os
import csv



def accesos_por_hora(file_name):
    """
    Cuenta cuántos registros hay por hora del día.
    La hora se extrae del campo 'hora' (formato HH:MM) tomando los primeros 2 caracteres.

    Retorna dict con claves string de 2 dígitos, solo horas con al menos un acceso:
        {"08": 2, "09": 3, "10": 1, ...}
    """
    base = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base, file_name)
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        
        dic = {}
        for row in reader:
            hora = row["hora"][:2]
            if hora not in dic:
                dic[str(hora)] = 1
            else:
                dic[str(hora)] += 1
        return dic



def duracion_promedio_por_accion(file_name):
    """
    Calcula la duración promedio en minutos por tipo de acción.
    Redondea a 2 decimales.

    Retorna dict:
        {"login": 1.75, "descarga": 18.33, "consulta": 8.67}
    """
    base = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base, file_name)
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        lista = []
        dic = {}
        cantidad = {}
        for row in reader:
            duracion =  row["duracion_minutos"]
            if row["accion"] not in dic:
                dic[row["accion"]] = 0
            dic[row["accion"]] += int(duracion)
            if row["accion"] not in cantidad:
                cantidad[row["accion"]] = 1
            else:
                cantidad[row["accion"]] += 1
            
        final = {}
        for accion in dic:
            if accion in cantidad:
                final[accion] = round(int(dic[accion])/int(cantidad[accion]),2)
        print(final)
        return final


def usuarios_activos_por_fecha(file_name):
    """
    Cuenta cuántos usuarios DISTINTOS accedieron cada día.

    Retorna dict:
        {"2024-03-01": 3, "2024-03-02": 3}
    """
    base = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base, file_name)
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        dic = {}
        for row in reader:
            fecha = row["fecha"]
            lista = []
            if fecha not in dic:
                dic[fecha] = 0
                if row["usuario"] not in lista:
                    dic[fecha] +=1
                    lista.append(row["usuario"])
            else:
                if row["usuario"] not in lista:
                    dic[fecha] +=1
                    lista.append(row["usuario"])
        return dic

