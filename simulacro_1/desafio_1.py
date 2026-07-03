# Simulacro 1 — Desafio 1: Filtros sobre CSV de Reproducciones
import os
import csv



def canciones_por_genero(file_name, genero):
    """
    Filtra reproducciones donde el genero coincide exactamente con el parametro.
    Para cada reproduccion retorna: id, cancion, artista, duracion_seg (como entero).

    Retorna lista de dicts en el mismo orden del CSV:
        [{"id": "1", "cancion": "Blinding Lights", "artista": "The Weeknd", "duracion_seg": 200}, ...]
    """
    base = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base, file_name)
    with open(path,"r", encoding="utf-8") as f:
        reader =  csv.DictReader(f)

        lista = []
        for row in reader:
            gen = row["genero"]
            if gen == genero:
                x = {"id":row["id"],"cancion":row["cancion"],"artista":row["artista"],"duracion_seg":int(row["duracion_seg"])}
                lista.append(x)
        return lista


def reproducciones_largas(file_name, duracion_minima):
    """
    Filtra reproducciones donde duracion_seg es ESTRICTAMENTE mayor que duracion_minima.
    Retorna lista de dicts ordenada de MAYOR a MENOR duracion_seg:
        [{"id": "7", "cancion": "Stairway to Heaven", "duracion_seg": 482}, ...]

    Nota: duracion_seg es entero.
    """
    base = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base, file_name)
    with open(path,"r", encoding="utf-8") as f:
        reader =  csv.DictReader(f)
        lista = []
        for row in reader:
            duracion = row["duracion_seg"]
            if int(duracion) > duracion_minima:
                x = {"id":row["id"],"cancion":row["cancion"],"duracion_seg":int(row["duracion_seg"])}
                lista.append(x)
        final = lista.sort(key= lambda x: -int(x["duracion_seg"]))
        return lista



def usuarios_por_pais(file_name):
    """
    Cuenta cuantos usuarios DISTINTOS hay en cada pais.

    Retorna dict:
        {"CL": 2, "MX": 1, "AR": 1}
    """
    base = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base, file_name)
    with open(path,"r", encoding="utf-8") as f:
        reader =  csv.DictReader(f)
        dic = {}
        for row in reader:
            usuario = row["usuario"]
            if usuario not in dic:
                dic[usuario] = row["pais"]
        final = {}
        for usuario in dic:
            if dic[usuario] not in final:
                final[dic[usuario]] = 1
            else:
                final[dic[usuario]] +=1
        return final

