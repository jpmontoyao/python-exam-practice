# Nivel 5d: Evaluador de Expresiones Postfijas
#
# En notación postfija (Reverse Polish Notation), los operadores van DESPUÉS
# de sus operandos. Se evalúa con una pila (stack).
#
# Ejemplos:
#   "3 4 +"   → 3 + 4 = 7
#   "5 3 -"   → 5 - 3 = 2
#   "3 4 + 2 *" → (3 + 4) * 2 = 14
#   "8 4 /"   → 8 / 4 = 2.0
#
# Algoritmo:
#   - Si el token es número → apilarlo
#   - Si el token es operador → sacar dos números de la pila,
#     operar, y apilar el resultado
#

OPERADORES = {'+', '-', '*', '/'}


def evaluar_postfix(expresion):
    """
    Evalúa una expresión en notación postfija y retorna el resultado numérico.
    Los tokens están separados por espacios.
    """
    pila = []

    for token in expresion.split():
        if token in OPERADORES:
            b = int(pila.pop())
            a = int(pila.pop())

            if token == '+':
                pila.append(a + b)
            elif token == '-':
                pila.append(a - b)
            elif token == '*':
                pila.append(a * b)
            elif token == '/':
                pila.append(a / b)
        else:
            pila.append(token)
    

    return pila[0]

expresion = "3 4 +"

print(evaluar_postfix(expresion))

