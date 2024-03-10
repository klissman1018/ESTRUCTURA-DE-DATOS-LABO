"6 Asegurar que un ciclo while se ejecuta al menos una vez."


# Definición de la clase Nodo para representar un nodo en una lista enlazada
class Nodo:
    # Constructor de la clase Nodo que recibe un dato como parámetro
    def __init__(self, dato):
        self.dato = dato  # Asigna el dato recibido al atributo dato del nodo
        self.siguiente = None  # Inicializa el atributo siguiente como None

    # Método para obtener el dato almacenado en el nodo
    def obtenerDato(self):
        return self.dato

    # Método para obtener el siguiente nodo en la lista enlazada
    def obtenerSiguiente(self):
        return self.siguiente

    # Método para asignar un nuevo dato al nodo
    def asignarDato(self, nuevo_dato):
        self.dato = nuevo_dato

    # Método para asignar el siguiente nodo en la lista enlazada
    def asignarSiguiente(self, nuevo_siguiente):
        self.siguiente = nuevo_siguiente


# Inicialización de la lista enlazada con dos nodos
nodo_inicial = Nodo(1)  # Crea el primer nodo con dato 1
nodo_segundo = Nodo(2)  # Crea el segundo nodo con dato 2
nodo_inicial.asignarSiguiente(
    nodo_segundo
)  # Conecta el primer nodo con el segundo nodo

# Ejecución de un ciclo while que se ejecuta al menos una vez
nodo_actual = nodo_inicial  # Inicializa el nodo actual con el primer nodo
ejecutar = True  # Variable que controla la ejecución del ciclo

while True:  # Inicia un ciclo while que se ejecuta al menos una vez
    print(
        f"Nodo actual: {nodo_actual.obtenerDato()}"
    )  # Imprime el dato del nodo actual

    if ejecutar:
        ejecutar = False  # Cambia la condición para salir en el próximo ciclo
    else:
        break  # Sale del ciclo

    nodo_actual = nodo_actual.obtenerSiguiente()  # Avanza al siguiente nodo en la lista

print("Este bloque se ejecuta después del ciclo do-while.")
