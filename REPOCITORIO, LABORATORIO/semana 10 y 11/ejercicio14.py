"Simular el proceso de deshacer (undo):"
"14. Implementar un sistema simple de deshacer utilizando dos pilas, una para las acciones y otra para los deshaceres."


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


def deshacer(accion_pila, deshacer_pila):
    if not accion_pila.esta_vacia():  # Verificamos si la pila de acciones no está vacía
        accion = accion_pila.desapilar()  # Desapilamos la última acción realizada
        deshacer_pila.apilar(accion)  # Apilamos la acción en la pila de deshaceres


def rehacer(accion_pila, deshacer_pila):
    if (
        not deshacer_pila.esta_vacia()
    ):  # Verificamos si la pila de deshaceres no está vacía
        accion = deshacer_pila.desapilar()  # Desapilamos la última acción deshecha
        accion_pila.apilar(accion)  # Apilamos la acción en la pila de acciones


# Ejemplo de uso
accion_pila = Pila()  # Creamos una pila para almacenar las acciones realizadas
deshacer_pila = Pila()  # Creamos una pila para almacenar las acciones deshechas

# Simulamos algunas acciones
accion_pila.apilar("Editar texto")
accion_pila.apilar("Guardar archivo")
accion_pila.apilar("Eliminar elemento")

# Simulamos un deshacer
deshacer(accion_pila, deshacer_pila)

# Simulamos un rehacer
rehacer(accion_pila, deshacer_pila)

# Mostramos el estado actual de las pilas
print("Pila de acciones:", accion_pila.items)
print("Pila de deshaceres:", deshacer_pila.items)
