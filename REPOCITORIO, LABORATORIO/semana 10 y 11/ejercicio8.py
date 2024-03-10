"Evaluar expresión posfija:"
"8. Crear un programa que evalúe una expresión matemática en notación posfija utilizando una pila."

class Pila:
    def __init__(self):
        self.items = []  # Creamos una lista para almacenar los elementos de la pila

    def esta_vacia(self):
        return self.items == []  # Verificamos si la pila está vacía

    def apilar(self, item):
        self.items.append(item)  # Agregamos un elemento a la pila

    def desapilar(self):
        return (
            self.items.pop()
        )  # Removemos y devolvemos el elemento superior de la pila


def evaluar_expresion_posfija(expresion):
    pila = Pila()  # Creamos una instancia de la clase Pila

    tokens = (
        expresion.split()
    )  # Dividimos la expresión en tokens (operadores y operandos)

    operadores = {"+", "-", "*", "/"}  # Definimos los operadores válidos

    for token in tokens:  # Recorremos cada token de la expresión
        if token not in operadores:  # Si el token no es un operador
            pila.apilar(float(token))  # Apilamos el operando convertido a tipo flotante
        else:
            operando2 = pila.desapilar()  # Desapilamos el segundo operando
            operando1 = pila.desapilar()  # Desapilamos el primer operando

            if token == "+":  # Si el token es una suma
                pila.apilar(operando1 + operando2)  # Apilamos el resultado de la suma
            elif token == "-":  # Si el token es una resta
                pila.apilar(operando1 - operando2)  # Apilamos el resultado de la resta
            elif token == "*":  # Si el token es una multiplicación
                pila.apilar(
                    operando1 * operando2
                )  # Apilamos el resultado de la multiplicación
            elif token == "/":  # Si el token es una división
                pila.apilar(
                    operando1 / operando2
                )  # Apilamos el resultado de la división

    return pila.desapilar()  # Retornamos el resultado final de la expresión
