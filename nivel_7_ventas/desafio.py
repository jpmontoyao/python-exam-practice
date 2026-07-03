# Nivel 7: Filtros sobre CSV de Ventas
# Equivalente al Desafio 1 del examen — pero con CSV en vez de JSON
import os
import csv



def ventas_por_categoria(file_name, categoria):
    """
    Filtra ventas donde la categoría coincide exactamente con el parámetro.
    Para cada venta calcula: total = precio * cantidad.

    Retorna lista de dicts en el mismo orden del CSV:
        [{"id": "1", "producto": "Laptop", "vendedor": "Maria", "total": 1700000}, ...]

    Nota: precio, cantidad y total son enteros.
    """
    base = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base, file_name)
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        lista = []
        for row in reader:
            if row["categoria"] == categoria:
                lista.append({"id":row["id"],"producto":row["producto"],"vendedor":row["vendedor"],"total":int(row["precio"])*int(row["cantidad"])})
        return lista


def ventas_sobre_monto(file_name, monto_minimo):
    """
    Filtra ventas donde total = precio * cantidad es ESTRICTAMENTE mayor que monto_minimo.
    Retorna lista de dicts ordenada de MAYOR a MENOR total:
        [{"id": "1", "producto": "Laptop", "total": 1700000}, ...]

    Nota: precio, cantidad y total son enteros.
    """
    base = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base, file_name)
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        lista = []
        for row in reader:
            total = int(row["precio"]) * int(row["cantidad"])
            if total > monto_minimo:
                lista.append({"id":row["id"],"producto":row["producto"],"total":total})
        
        lista.sort(key= lambda x: -x["total"])
        return lista



def resumen_por_vendedor(file_name):
    """
    Agrupa las ventas por vendedor y suma el total de cada uno.
    Retorna dict:
        {"Maria": 2167000, "Carlos": 225000, "Pedro": 300000}

    Nota: los totales son enteros.
    """
    base = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base, file_name)
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        dict = {}
        for row in reader:
            total = int(row["precio"]) * int(row["cantidad"])
            if row["vendedor"] not in dict:
                dict[row["vendedor"]] = 0
            dict[row["vendedor"]] += total
        return dict
            

