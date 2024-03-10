"8 Validar el estado de una variable después de una operación."


# Definición de la clase Nodo con su constructor
class Nodo:
    def __init__(self, dato):
        self.dato = dato  # Asigna el dato al atributo 'dato' del nodo
        self.siguiente = None  # Inicializa el atributo 'siguiente' como None


# Definición de la clase ListaEnlazada con su constructor
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None  # Inicializa el atributo 'cabeza' como None

    # Método para insertar un nuevo nodo en la lista enlazada
    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)  # Crea un nuevo nodo con el dato proporcionado
        if self.cabeza is None:  # Verifica si la lista está vacía
            self.cabeza = (
                nuevo_nodo  # Si está vacía, el nuevo nodo se convierte en la cabeza
            )
        else:
            nodo_actual = self.cabeza
            while (
                nodo_actual.siguiente is not None
            ):  # Recorre la lista hasta el último nodo
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = (
                nuevo_nodo  # Conecta el nuevo nodo al último nodo de la lista
            )

    # Método para validar si un dato ha sido insertado correctamente en la lista
    def validar_insercion(self, dato):
        nodo_actual = self.cabeza
        while nodo_actual is not None:  # Recorre la lista
            if (
                nodo_actual.dato == dato
            ):  # Comprueba si el dato coincide con el dato a validar
                return True  # Retorna True si el dato está presente en la lista
            nodo_actual = nodo_actual.siguiente
        return False  # Retorna False si el dato no está presente en la lista


# Creación de una lista enlazada
lista = ListaEnlazada()

# Insertar un nuevo nodo con el valor 5 en la lista
lista.insertar(5)

# Validar si el dato 5 se ha insertado correctamente en la lista
if lista.validar_insercion(5):
    print("La inserción fue exitosa.")
else:
    print("La inserción no tuvo el resultado esperado.")
