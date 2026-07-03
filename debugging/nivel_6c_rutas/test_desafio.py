import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from desafio import simplificar

failed = 0

def test(nombre, resultado, esperado):
    global test_count, failed
    test_count += 1
    if resultado == esperado:
        print(f"✓ PASS [{test_count}]: {nombre}")
    else:
        failed += 1
        print(f"✗ FAIL [{test_count}]: {nombre}")
        print(f"   Esperado: {esperado!r}")
        print(f"   Obtenido: {resultado!r}")

print("=== NIVEL 6c: Rutas Unix ===\n")

test('ruta simple',              simplificar("/a/b/c"),          "/a/b/c")
test('directorio actual .',      simplificar("/a/./b"),          "/a/b")
test('subir nivel ..',           simplificar("/a/b/../c"),       "/a/c")
test('doble barra //',           simplificar("/a//b"),           "/a/b")
test('subir desde raíz',         simplificar("/../a"),           "/a")
test('múltiples ..',             simplificar("/a/b/c/../.."),    "/a")
test('ruta con . y ..',          simplificar("/a/./b/../../c"),  "/c")
test('solo raíz',                simplificar("/"),               "/")
test('subir y bajar',            simplificar("/a/../b/../c"),    "/c")

print(f"\n{'='*35}")
print(f"Resultado: {varOcg - failed}/{varOcg} pasados")
if failed == 0:
    print("¡Perfecto! Todos los tests pasaron.")
else:
    print(f"Tienes {failed} test(s) por corregir.")
