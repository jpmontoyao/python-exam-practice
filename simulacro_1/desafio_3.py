# Simulacro 1 — Desafio 3: Analisis combinando dos CSVs
import os
import csv



def reproducciones_por_pais_origen(reproducciones_csv, artistas_csv):
    """
    Combina los dos CSVs usando el campo 'artista' como llave.
    Cuenta cuantas reproducciones tiene cada pais_origen de artista.

    Retorna dict:
        {"Canada": 1, "Puerto Rico": 6, "Reino Unido": 5, ...}
    """
    base = os.path.dirname(os.path.abspath(__file__))
    path_rep = os.path.join(base, reproducciones_csv)
    path_art = os.path.join(base, artistas_csv)
    with open(path_rep,"r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        reps = {}
        for row in reader:
            artista = row["artista"]
            if artista not in reps:
                reps[artista] = 1
            else:
                reps[artista] +=1


    with open(path_art,"r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        final = {}
        for row in reader:
            artista = row["artista"]
            if artista in reps and row["pais_origen"] not in final:
                final[row["pais_origen"]] = int(reps[artista])
            else:
                final[row["pais_origen"]] += int(reps[artista])
        return final


def genero_favorito_por_usuario(file_name):
    """
    Para cada usuario, determina el genero que mas veces escucho.
    En caso de empate, retorna el genero que aparece primero alfabeticamente.

    Retorna dict:
        {"user_a": "Rock", "user_b": "Reggaeton", "user_c": "Reggaeton", "user_d": "Rock"}
    """
    base = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base, file_name)
    with open(path,"r", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        usuarios = []
        for row in reader:
            if row["usuario"] not in usuarios:
                usuarios.append(row["usuario"])
    lista = []
    with open(path,"r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        
        return None

        


def artistas_debut_tardio(reproducciones_csv, artistas_csv, anio_minimo):
    """
    Combina los dos CSVs usando 'artista' como llave.
    Filtra artistas cuyo debut_ano es ESTRICTAMENTE mayor que anio_minimo.
    Retorna lista de dicts ordenada de MAYOR a MENOR debut_ano:
        [{"artista": "Tones and I", "debut_ano": 2018, "reproducciones": 1}, ...]

    Nota: debut_ano es entero. Solo incluye artistas que aparezcan en reproducciones.csv.
    """
    base = os.path.dirname(os.path.abspath(__file__))
    path_rep = os.path.join(base, reproducciones_csv)
    path_art = os.path.join(base, artistas_csv)

    with open(path_rep,"r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        reps = {}
        for row in reader:
            artista = row["artista"]
            if artista not in reps:
                reps[artista] = 1
            else:
                reps[artista] +=1


    with open(path_art,"r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        lista = []
        for row in reader:
            debut = int(row["debut_ano"])
            if debut > anio_minimo:
                x = {"artista":row["artista"],"debut_ano":debut,"reproducciones":reps[row["artista"]]}
                lista.append(x)
        lista.sort(key= lambda x: -x["debut_ano"])
        
        return lista
