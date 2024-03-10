"Eliminar duplicados:"
"11. Eliminar los elementos duplicados de una pila."


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


def eliminar_duplicados_pila(pila):
    elementos_vistos = (
        set()
    )  # Creamos un conjunto para almacenar los elementos únicos que hemos visto
    pila_temporal = (
        Pila()
    )  # Creamos una pila temporal para almacenar los elementos sin duplicados

    while not pila.esta_vacia():  # Mientras la pila original no esté vacía
        elemento = pila.desapilar()  # Desapilamos un elemento de la pila original

        if (
            elemento not in elementos_vistos
        ):  # Si el elemento no está en el conjunto de elementos vistos
            elementos_vistos.add(
                elemento
            )  # Agregamos el elemento al conjunto de elementos vistos
            pila_temporal.apilar(elemento)  # Apilamos el elemento en la pila temporal

    while not pila_temporal.esta_vacia():  # Mientras la pila temporal no esté vacía
        pila.apilar(
            pila_temporal.desapilar()
        )  # Reapilamos los elementos de la pila temporal en la pila original


# Ejemplo de uso
mi_pila = Pila()  # Creamos una instancia de la clase Pila
mi_pila.apilar(5)  # Apilamos elementos en la pila
mi_pila.apilar(2)
mi_pila.apilar(7)
mi_pila.apilar(2)
mi_pila.apilar(5)

eliminar_duplicados_pila(
    mi_pila
)  # Llamamos a la función para eliminar duplicados de la pila

# Imprimimos y desapilamos elementos de la pila original
while not mi_pila.esta_vacia():
    print(mi_pila.desapilar(), end=" ")
print()
