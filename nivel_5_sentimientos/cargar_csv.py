import csv

def cargar_sentimientos(csv_path):
    # __define-ocg__
    varOcg = {}
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            varOcg[row['palabra']] = {
                'polaridad': row['polaridad'],
                'intensidad': int(row['intensidad'])
            }
    return varOcg
