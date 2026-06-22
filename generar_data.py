import json
from datetime import datetime, timedelta

def make_dates(start_str, count, last_date_str=None):
    start = datetime.fromisoformat(start_str.replace('Z',''))
    dates = []
    for i in range(count):
        d = start + timedelta(minutes=5*i)
        dates.append({"date": d.strftime("%Y-%m-%dT%H:%M:%SZ")})
    if last_date_str and count > 0:
        dates[-1] = {"date": last_date_str}
    return dates

posts = [
    {
        "id": "1001",
        "text": "excelente servicio satisfecho excelente calidad bueno producto agradable",
        "author": "usuario_feliz",
        "author_followers": 2500,
        "created_at": "2024-11-15T10:30:00Z",
        "retweets": make_dates("2024-11-15T11:00:00Z", 40, "2024-11-22T18:30:00Z"),
        "likes": make_dates("2024-11-15T12:00:00Z", 50, "2024-11-22T19:15:00Z"),
        "replies": make_dates("2024-11-15T13:00:00Z", 20, "2024-11-22T17:50:00Z")
    },
    {
        "id": "1002",
        "text": "la atencion al cliente fue pesimo terrible espera horrible sin respuesta pesimo",
        "author": "cliente_frustrado",
        "author_followers": 500,
        "created_at": "2024-11-15T14:00:00Z",
        "retweets": make_dates("2024-11-15T15:00:00Z", 10),
        "likes": make_dates("2024-11-15T16:00:00Z", 15),
        "replies": make_dates("2024-11-15T17:00:00Z", 5)
    },
    {
        "id": "1003",
        "text": "el producto es bueno pero el servicio fue malo y lento deficiente",
        "author": "analista_tech",
        "author_followers": 1500,
        "created_at": "2024-11-15T10:15:00Z",
        "retweets": make_dates("2024-11-15T11:00:00Z", 5),
        "likes": make_dates("2024-11-15T12:00:00Z", 8),
        "replies": make_dates("2024-11-15T13:00:00Z", 3)
    },
    {
        "id": "1004",
        "text": "maravilloso equipo increible respuesta satisfecho cliente agradable",
        "author": "influencer_digital",
        "author_followers": 8000,
        "created_at": "2024-11-15T00:30:00Z",
        "retweets": make_dates("2024-11-15T01:00:00Z", 60, "2024-11-20T10:00:00Z"),
        "likes": make_dates("2024-11-15T02:00:00Z", 80, "2024-11-20T15:00:00Z"),
        "replies": make_dates("2024-11-15T03:00:00Z", 30, "2024-11-20T08:00:00Z")
    },
    {
        "id": "1005",
        "text": "horrible terrible terrible experiencia negativo impacto",
        "author": "usuario_nuevo",
        "author_followers": 200,
        "created_at": "2024-11-15T22:45:00Z",
        "retweets": make_dates("2024-11-15T23:00:00Z", 35, "2024-11-18T12:00:00Z"),
        "likes": make_dates("2024-11-16T00:00:00Z", 50, "2024-11-19T16:00:00Z"),
        "replies": make_dates("2024-11-16T01:00:00Z", 20, "2024-11-17T09:00:00Z")
    },
    {
        "id": "1006",
        "text": "nuestros productos de alta calidad pero el servicio es deficiente e decepcionante malo",
        "author": "empresa_grande",
        "author_followers": 50000,
        "created_at": "2024-11-15T10:00:00Z",
        "retweets": make_dates("2024-11-15T11:00:00Z", 3),
        "likes": make_dates("2024-11-15T12:00:00Z", 5),
        "replies": make_dates("2024-11-15T13:00:00Z", 2)
    }
]

import os
base = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(base, "datos", "data.json")
with open(output_path, "w", encoding="utf-8") as f:
    json.dump({"posts": posts}, f, ensure_ascii=False, indent=2)
print("data.json generado correctamente en datos/")
