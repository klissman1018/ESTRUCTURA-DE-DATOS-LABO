"10.   Desarrollar el código de buscar nodo en la lista enlazada simple."



class Nodo:  # Define una clase llamada Nodo
    def __init__(self, dato):  # Define un método de inicialización para la clase Nodo que recibe un dato como parámetro
        self.dato = dato  # Asigna el dato recibido como parámetro al atributo 'dato' del objeto Nodo
        self.siguiente = None  # Inicializa el atributo 'siguiente' del objeto Nodo como None

def buscar_nodo(cabeza, valor):  # Define una función llamada buscar_nodo que recibe la cabeza de una lista y un valor a buscar
    actual = cabeza  # Inicializa una variable 'actual' con la cabeza de la lista
   
    while actual and actual.dato != valor:  # Mientras 'actual' no sea None y el dato de 'actual' sea diferente al valor a buscar
        actual = actual.siguiente  # Avanza al siguiente nodo en la lista
    return actual  # Retorna el nodo encontrado o None si no se encontró

cabeza = Nodo(1)  # Crea un nodo con dato 1 y lo asigna como cabeza de la lista
segundo = Nodo(2)  # Crea un nodo con dato 2
tercero = Nodo(3)  # Crea un nodo con dato 3

cabeza.siguiente = segundo  # Asigna el nodo 'segundo' como el siguiente nodo al nodo cabeza
segundo.siguiente = tercero  # Asigna el nodo 'tercero' como el siguiente nodo al nodo segundo

valor_a_buscar = 2  # Define el valor a buscar como 2
nodo_encontrado = buscar_nodo(cabeza, valor_a_buscar)  # Llama a la función buscar_nodo para encontrar el nodo con el valor 2

if nodo_encontrado:  # Si se encontró un nodo
    print("El valor encontrado es:", valor_a_buscar)  # Imprime que se encontró el valor
else:  # Si no se encontró un nodo
    print("El valor no fue encontrado:", valor_a_buscar)  # Imprime que el valor no fue encontrado