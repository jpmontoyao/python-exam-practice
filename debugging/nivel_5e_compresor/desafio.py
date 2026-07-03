# Nivel 5e: Compresor/Descompresor RLE (Run-Length Encoding)
#
# RLE es un algoritmo de compresión que reemplaza secuencias repetidas
# por un conteo seguido del carácter.
#
# Formato: número primero, luego carácter
#   comprimir("aaabbc")  → "3a2b1c"
#   comprimir("abcd")    → "1a1b1c1d"
#
# Para descomprimir se lee el número y se repite el carácter:
#   descomprimir("3a2b1c") → "aaabbc"
#
# Suposición: los conteos son siempre de un solo dígito (1-9).
#


def comprimir(texto):
    """Comprime un string usando RLE. Retorna string vacío si la entrada es vacía."""
    if not texto:
        return ""

    resultado = []
    actual = texto[0]
    contador = 0

    for c in texto:
        if c == actual:
            contador += 1
        else:
            resultado.append(str(contador) + actual )
            actual = c
            contador = 1

    resultado.append(str(contador)+ actual )
    return ''.join(resultado)


def descomprimir(texto):
    """Descomprime un string codificado con RLE."""
    resultado = []
    i = 0
    while i < len(texto):
        contador = int(texto[i])
        caracter = texto[i + 1]
        resultado.append(caracter * contador)

        i += 2

    return ''.join(resultado)

comp = "3a2b1c"
print(descomprimir(comp))