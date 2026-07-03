import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from desafio_1 import canciones_por_genero, reproducciones_largas, usuarios_por_pais

test_count = 0
failed_tests = 0

def test(name, result, expected):
    global test_count, failed_tests
    test_count += 1
    if result == expected:
        print(f"✓ PASS [{test_count}]: {name}")
    else:
        failed_tests += 1
        print(f"✗ FAIL [{test_count}]: {name}")
        print(f"   Esperado: {expected}")
        print(f"   Obtenido: {result}")

def test_partial(name, condition, detail=""):
    global test_count, failed_tests
    test_count += 1
    if condition:
        print(f"✓ PASS [{test_count}]: {name}")
    else:
        failed_tests += 1
        print(f"✗ FAIL [{test_count}]: {name}")
        if detail:
            print(f"   Detalle: {detail}")

print("=== SIMULACRO 1 — Desafio 1: Filtros CSV ===\n")

# -------------------------------------------------------
# canciones_por_genero
# -------------------------------------------------------
print("-- canciones_por_genero('reproducciones.csv', 'Rock') --")
res_rock = canciones_por_genero("reproducciones.csv", "Rock")

test_partial("retorna lista", isinstance(res_rock, list))
test_partial("tiene 6 canciones Rock", len(res_rock) == 6)
test("primera cancion es Bohemian Rhapsody",
     res_rock[0] if res_rock else None,
     {"id": "3", "cancion": "Bohemian Rhapsody", "artista": "Queen", "duracion_seg": 354})
test("duracion_seg es entero",
     isinstance(res_rock[0]["duracion_seg"], int) if res_rock else False, True)

print("\n-- canciones_por_genero('reproducciones.csv', 'Reggaeton') --")
res_reg = canciones_por_genero("reproducciones.csv", "Reggaeton")

test_partial("tiene 6 canciones Reggaeton", len(res_reg) == 6)
test("primera cancion es Gasolina",
     res_reg[0] if res_reg else None,
     {"id": "2", "cancion": "Gasolina", "artista": "Daddy Yankee", "duracion_seg": 201})

# -------------------------------------------------------
# reproducciones_largas
# -------------------------------------------------------
print("\n-- reproducciones_largas('reproducciones.csv', 300) --")
res_largas = reproducciones_largas("reproducciones.csv", 300)

test_partial("retorna lista", isinstance(res_largas, list))
test_partial("tiene 5 canciones (> 300 seg)", len(res_largas) == 5)
test("primera es Stairway to Heaven (482)",
     res_largas[0] if res_largas else None,
     {"id": "7", "cancion": "Stairway to Heaven", "duracion_seg": 482})
test("segunda es Stairway to Heaven (482)",
     res_largas[1] if len(res_largas) > 1 else None,
     {"id": "9", "cancion": "Stairway to Heaven", "duracion_seg": 482})
test("ultima es Smells Like Teen Spirit (301)",
     res_largas[-1] if res_largas else None,
     {"id": "5", "cancion": "Smells Like Teen Spirit", "duracion_seg": 301})

print("\n-- reproducciones_largas('reproducciones.csv', 400) --")
res_largas2 = reproducciones_largas("reproducciones.csv", 400)
test_partial("tiene 2 canciones (> 400 seg)", len(res_largas2) == 2)
test("primera es Stairway to Heaven (482)",
     res_largas2[0] if res_largas2 else None,
     {"id": "7", "cancion": "Stairway to Heaven", "duracion_seg": 482})

# -------------------------------------------------------
# usuarios_por_pais
# -------------------------------------------------------
print("\n-- usuarios_por_pais('reproducciones.csv') --")
res_pais = usuarios_por_pais("reproducciones.csv")

test_partial("retorna dict", isinstance(res_pais, dict))
test_partial("tiene 3 paises", set(res_pais.keys()) == {"CL", "MX", "AR"})
test("CL tiene 2 usuarios distintos", res_pais.get("CL"), 2)
test("MX tiene 1 usuario distinto",   res_pais.get("MX"), 1)
test("AR tiene 1 usuario distinto",   res_pais.get("AR"), 1)

total = test_count
print(f"\n{'='*45}")
print(f"Resultado: {total - failed_tests}/{total} pasados")
if failed_tests == 0:
    print("¡Excelente! Todos los tests pasaron.")
else:
    print(f"Tienes {failed_tests} test(s) por corregir.")
