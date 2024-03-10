"Convertir número decimal a binario:"
"7. Implementar un programa que convierta un número decimal a su representación en sistema binario utilizando una pila"

class Pila:
    def __init__(self):
        self.items = []  # Inicializa una lista vacía en el atributo 'items' de la pila

    def esta_vacia(self):
        return self.items == []  # Devuelve True si la pila está vacía, False si no lo está

    def apilar(self, item):
        self.items.append(item)  # Agrega un elemento a la pila

    def desapilar(self):
        return self.items.pop()  # Elimina y devuelve el último elemento agregado a la pila


def decimal_a_binario(numero_decimal):
    pila = Pila()  # Crea una nueva instancia de la clase Pila

    while numero_decimal > 0:
        residuo = numero_decimal % 2  # Calcula el residuo de dividir el número decimal entre 2
        pila.apilar(residuo)  # Agrega el residuo a la pila
        numero_decimal //= 2  # Actualiza el número decimal dividiéndolo entre 2

    binario = ""
    while not pila.esta_vacia():
        binario += str(pila.desapilar())  # Convierte y concatena los elementos de la pila a binario

    return binario  # Devuelve la representación binaria del número decimal


numero_decimal = 26
binario = decimal_a_binario(numero_decimal)  # Convierte el número decimal a binario
print(f"El número decimal {numero_decimal} en binario es: {binario}")  # Imprime el resultado en binario
