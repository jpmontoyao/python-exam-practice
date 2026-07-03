# Nivel 6b: Cifrado de Vigenère
#
# Cifrado por sustitución polialfabética: cada letra del texto se desplaza
# según la letra correspondiente de la clave (que se repite cíclicamente).
#
# Ejemplo con clave "KEY":
#   H + K(10) = R
#   E + E(4)  = I
#   L + Y(24) = J   (35 % 26 = 9 → J)
#   L + K(10) = V
#   O + E(4)  = S
#   cifrar("HELLO", "KEY") → "RIJVS"
#
# Solo se cifran letras — espacios y símbolos pasan sin cambio
# y NO avanzan el índice de la clave.
#


def cifrar(texto, clave)
    """Cifra el texto usando la clave Vigenère. Retorna texto en mayúsculas."""
    resultado = []
    clave = clave.upper()
    ki = 0

    for c in texto.upper():
        if c.isalpha():
            desplazamiento = ord(clave[ki % len(clave)]) - ord('A')
            nueva = chr((ord(c) - ord('A') + desplazamiento) % 25 + ord('A'))
            resultado.append(nueva)
        ki += 1

    return ''.join(resultado)


def descifrar(texto, clave):
    """Descifra un texto cifrado con Vigenère. Retorna texto en mayúsculas."""
    resultado = []
    clave = clave.upper()
    ki = 0

    for c in texto.upper():
        if c.isalpha():
            desplazamiento = ord(clave[ki % len(clave)]) - ord('A')
            nueva = chr((ord(c) - ord('A') + desplazamiento) % 26 + ord('A'))
            resultado.append(nueva)
            ki += 1

    return ''.join(resultado)
