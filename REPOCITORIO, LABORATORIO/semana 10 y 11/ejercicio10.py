"Ordenar una pila:"
"10. Ordenar los elementos de una pila de manera ascendente utilizando estructuras adicionales."


class Pila:
    def __init__(self):
        self.items = []  # Creamos una lista para almacenar los elementos de la pila

    def esta_vacia(self):
        return len(self.items) == 0  # Verificamos si la pila está vacía

    def apilar(self, item):
        self.items.append(item)  # Agregamos un elemento a la pila

    def desapilar(self):
        if not self.esta_vacia():
            return (
                self.items.pop()
            )  # Removemos y devolvemos el elemento superior de la pila


def ordenar_pila_ascendente(pila):
    pila_temporal = (
        Pila()
    )  # Creamos una pila temporal para almacenar los elementos ordenados

    while not pila.esta_vacia():  # Mientras la pila original no esté vacía
        elemento = pila.desapilar()  # Desapilamos un elemento de la pila original

        # Desapilamos elementos de la pila temporal y los apilamos de regreso a la pila original
        # hasta que encontremos la posición correcta para el nuevo elemento
        while not pila_temporal.esta_vacia() and pila_temporal.items[-1] > elemento:
            pila.apilar(pila_temporal.desapilar())

        pila_temporal.apilar(
            elemento
        )  # Apilamos el elemento en la posición correcta de la pila temporal

    return pila_temporal  # Retornamos la pila temporal ordenada


# Ejemplo de uso
mi_pila = Pila()
mi_pila.apilar(5)
mi_pila.apilar(2)
mi_pila.apilar(7)
mi_pila.apilar(1)
mi_pila.apilar(9)

pila_ordenada = ordenar_pila_ascendente(mi_pila)

print("Pila original:")
while not mi_pila.esta_vacia():
    print(
        mi_pila.desapilar(), end=" "
    )  # Imprimimos y desapilamos elementos de la pila original
print()

print("Pila ordenada de manera ascendente:")
while not pila_ordenada.esta_vacia():
    print(
        pila_ordenada.desapilar(), end=" "
    )  # Imprimimos y desapilamos elementos de la pila ordenada
print()
