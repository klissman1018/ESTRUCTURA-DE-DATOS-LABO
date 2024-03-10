#Diseño de un sistema de gestión de pedidos
#2. Crea un sistema de gestión de pedidos que utilice una cola para procesar los pedidos en el orden en que 
#fueron recibidos. Implementa funciones para agregar pedidos, procesar pedidos y mostrar el estado 
#actual de la cola.

from collections import deque  # Importa deque de collections para usar una cola

class Pedido:
    def __init__(self, id_pedido, descripcion):
        self.id_pedido = id_pedido  # Guarda el id del pedido
        self.descripcion = descripcion  # Guarda la descripción del pedido

    def __str__(self):
        return f"Pedido {self.id_pedido}: {self.descripcion}"  # Devuelve una representación en cadena del pedido

class GestorPedidos:
    def __init__(self):
        self.cola_pedidos = deque()  # Inicializa una cola para almacenar los pedidos

    def agregar_pedido(self, pedido):
        self.cola_pedidos.append(pedido)  # Agrega un pedido al final de la cola
        print(f"Pedido {pedido.id_pedido} agregado a la cola.")  # Imprime un mensaje indicando que el pedido fue agregado

    def procesar_pedido(self):
        if not self.cola_pedidos:
            print("No hay pedidos en la cola.")  # Si la cola está vacía, imprime un mensaje
            return
        pedido_procesado = self.cola_pedidos.popleft()  # Remueve y devuelve el primer pedido de la cola
        print(f"Procesando: {pedido_procesado}")  # Imprime un mensaje indicando que el pedido está siendo procesado
        # Aquí puedes agregar el código para procesar el pedido

    def mostrar_estado(self):
        print("Estado actual de la cola de pedidos:")  # Imprime un mensaje sobre el estado actual
        for pedido in self.cola_pedidos:
            print(pedido)  # Imprime cada pedido en la cola

# Ejemplo de uso
gestor = GestorPedidos()  # Crea una instancia de GestorPedidos

# Agregar pedidos a la cola
gestor.agregar_pedido(Pedido(1, "Pizza grande"))  # Agrega un pedido de pizza grande
gestor.agregar_pedido(Pedido(2, "Hamburguesa"))  # Agrega un pedido de hamburguesa

# Procesar el primer pedido en la cola
gestor.procesar_pedido()  # Procesa el primer pedido en la cola

# Mostrar el estado actual de la cola
gestor.mostrar_estado()  # Muestra el estado actual de la cola de pedidos