"Comprobar palíndromos:"
"13. Utilizar una pila para comprobar si una palabra o frase es un palíndromo."


class Pila:
    def __init__(self):
        self.items = (
            []
        )  # Inicializamos una lista para almacenar los elementos de la pila

    def esta_vacia(self):
        return len(self.items) == 0  # Verificamos si la pila está vacía

    def apilar(self, item):
        self.items.append(item)  # Agregamos un elemento a la pila

    def desapilar(self):
        if not self.esta_vacia():
            return (
                self.items.pop()
            )  # Removemos y devolvemos el elemento superior de la pila


def calcular_expresion(expresion):
    pila = (
        Pila()
    )  # Creamos una instancia de la clase Pila para usar como pila de operandos

    tokens = (
        expresion.split()
    )  # Dividimos la expresión en tokens (números y operadores)

    for token in tokens:  # Iteramos sobre cada token de la expresión
        if token.isdigit():  # Si el token es un número
            pila.apilar(
                float(token)
            )  # Apilamos el número convertido a flotante en la pila
        else:  # Si el token es un operador
            operando2 = pila.desapilar()  # Desapilamos el segundo operando
            operando1 = pila.desapilar()  # Desapilamos el primer operando
            # Realizamos la operación correspondiente y apilamos el resultado en la pila
            if token == "+":
                pila.apilar(operando1 + operando2)
            elif token == "-":
                pila.apilar(operando1 - operando2)
            elif token == "*":
                pila.apilar(operando1 * operando2)
            elif token == "/":
                if operando2 == 0:  # Manejo de división por cero
                    return "Error: división por cero"
                pila.apilar(operando1 / operando2)

    return pila.desapilar()  # Devolvemos el resultado final de la expresión


# Ejemplo de uso
expresion = "3 4 + 5 * 6 -"  # Expresión en notación posfija: 3 + 4 * 5 - 6
resultado = calcular_expresion(expresion)
print("Resultado de la expresión:", resultado)
