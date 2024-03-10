"Ejercicios parte 02:"
"Invertir una cadena:"
"6. Utilizar una pila para invertir el orden de los caracteres de una cadena."

class Pila:
    def __init__(self):
        self.items = (
            []
        )  # Inicializamos una lista para almacenar los elementos de la pila

    def esta_vacia(self):
        return self.items == []  # Verificamos si la pila está vacía

    def apilar(self, item):
        self.items.append(item)  # Agregamos un elemento a la pila

    def desapilar(self):
        return (
            self.items.pop()
        )  # Removemos y devolvemos el elemento superior de la pila


def invertir_cadena(cadena):
    pila = (
        Pila()
    )  # Creamos una instancia de la clase Pila para usar como pila de caracteres

    for caracter in cadena:  # Iteramos sobre cada caracter de la cadena original
        pila.apilar(caracter)  # Apilamos cada caracter en la pila

    cadena_invertida = (
        ""  # Inicializamos una cadena vacía para almacenar la cadena invertida
    )

    while not pila.esta_vacia():  # Mientras la pila no esté vacía
        cadena_invertida += (
            pila.desapilar()
        )  # Desapilamos cada caracter de la pila y lo agregamos a la cadena invertida

    return cadena_invertida  # Devolvemos la cadena invertida


# Ejemplo de uso
cadena_original = "Hola mundo!"
cadena_invertida = invertir_cadena(cadena_original)
print("Cadena original:", cadena_original)
print("Cadena invertida:", cadena_invertida)
