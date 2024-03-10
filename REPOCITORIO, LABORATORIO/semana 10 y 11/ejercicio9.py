"Validar operadores anidados:"
"9. Verificar si los operadores en una expresión matemática están correctamente anidados utilizando una pila"


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


def operadores_anidados(expresion):
    pila = Pila()  # Creamos una instancia de la clase Pila

    pares_operadores = {
        "(": ")",
        "[": "]",
        "{": "}",
    }  # Definimos el mapeo de pares de operadores

    for caracter in expresion:  # Recorremos cada caracter de la expresión
        if caracter in pares_operadores.keys():  # Si es un operador de apertura
            pila.apilar(caracter)  # Apilamos el operador
        elif caracter in pares_operadores.values():  # Si es un operador de cierre
            if pila.esta_vacia():  # Si la pila está vacía
                return False  # Los operadores están mal anidados
            else:
                operador_abierto = (
                    pila.desapilar()
                )  # Desapilamos el último operador de apertura
                if (
                    pares_operadores[operador_abierto] != caracter
                ):  # Si los operadores no coinciden
                    return False  # Los operadores están mal anidados

    return (
        pila.esta_vacia()
    )  # Si la pila está vacía al final, los operadores están correctamente anidados


# Ejemplo de uso
expresion1 = "(3 + 5) * [7 - {2 * (9 - 3)}]"
expresion2 = "(3 + 5) * [7 - {2 * (9 - 3)}"
expresion3 = "3 + 5) * [7 - {2 * (9 - 3)}]"

print("Expresión 1:", "Correcta" if operadores_anidados(expresion1) else "Incorrecta")
print("Expresión 2:", "Correcta" if operadores_anidados(expresion2) else "Incorrecta")
print("Expresión 3:", "Correcta" if operadores_anidados(expresion3) else "Incorrecta")
