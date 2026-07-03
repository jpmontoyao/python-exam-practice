# Nivel 9: Análisis de Evaluaciones — dos CSVs combinados
# Equivalente al Desafio 3 del examen — pero con CSV en vez de JSON
import os
import csv



def promedio_por_curso(eval_csv):
    """
    Calcula el promedio de nota por curso, redondeado a 2 decimales.

    Retorna dict:
        {"MAT101": 82.67, "FIS101": 75.67, "INF101": 91.0, "HUM101": 76.33}
    """
    base = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base, eval_csv)
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        dic = {}
        alumnos = {}
        for row in reader:
            curso  = row["curso"]
            if curso not in dic:
                dic[curso] = int(row["nota"])
                alumnos[curso] = 1
            else:
                dic[curso] += int(row["nota"])
                alumnos[curso] +=1
        final = {}

        for ramo in dic:
            if ramo not in final:
                final[ramo] = round(dic[ramo]/alumnos[ramo],2)
        return final




def clasificar_estudiantes(eval_csv, nota_minima):
    """
    Clasifica cada estudiante como "aprobado" o "reprobado".
    Un estudiante aprueba si TODAS sus notas son >= nota_minima.
    Si tiene al menos una nota bajo nota_minima, reprueba.

    Retorna dict:
        {"juan": "reprobado", "maria": "aprobado", "pedro": "reprobado"}
    """
    base = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base, eval_csv)
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        alumnos = []
        for row in reader:
            estudiante = row["estudiante"]
            if estudiante not in alumnos:
                alumnos.append(estudiante)
    notas = {}
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for persona in alumnos:
            for row in reader:
                estudiante = row["estudiante"]
                if int(row["nota"]) < nota_minima:
                    notas[estudiante] = 1     
               

        final = {}     

        for persona in alumnos:
            if persona in notas:
                final[persona] = "reprobado"
            else:
                final[persona] = "aprobado"
        return final
            

def analisis_por_departamento(eval_csv, cursos_csv):
    """
    Combina los dos CSVs usando el campo 'curso' como llave.
    Calcula el promedio de nota por departamento, redondeado a 2 decimales.

    Retorna dict:
        {"Matematicas": 82.67, "Ciencias": 75.67, "Informatica": 91.0, "Humanidades": 76.33}
    """
    base = os.path.dirname(os.path.abspath(__file__))
    path_eval = os.path.join(base, eval_csv)
    path_cursos = os.path.join(base, cursos_csv)
    with open(path_cursos, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        promedio = promedio_por_curso(eval_csv)
        print(promedio)
        final = {}
        for row in reader:
            curso = row["curso"]
            if curso in promedio:
                final[row["departamento"]] = promedio[curso]
        return final

        
