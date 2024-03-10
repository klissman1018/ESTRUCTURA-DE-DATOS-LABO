#Diseño de un sistema de gestión de tareas (Avanzado)
#4.    Implementa  un  sistema  de  gestión  de  tareas  que  permita  agregar  tareas,  marcar  tareas  como 
#completadas y mostrar la próxima tarea pendiente.

class GestorTareas:
    def __init__(self):
        self.tareas = []  # Inicializa una lista vacía para almacenar las tareas.

    def agregar_tarea(self, tarea):
        self.tareas.append({'tarea': tarea, 'completada': False})  # Añade una nueva tarea a la lista con el estado 'completada' en False.
        print(f"Tarea '{tarea}' agregada.")  # Imprime un mensaje indicando que la tarea fue agregada.

    def marcar_como_completada(self, tarea):
        for tarea_en_lista in self.tareas:  # Recorre la lista de tareas.
            if tarea_en_lista['tarea'] == tarea:  # Verifica si la tarea actual es la que se quiere marcar como completada.
                tarea_en_lista['completada'] = True  # Marca la tarea como completada.
                print(f"Tarea '{tarea}' marcada como completada.")  # Imprime un mensaje indicando que la tarea fue marcada como completada.
                return  # Sale de la función.
        print(f"Tarea '{tarea}' no encontrada.")  # Si la tarea no se encuentra, imprime un mensaje indicándolo.

    def mostrar_proxima_tarea_pendiente(self):
        for tarea in self.tareas:  # Recorre la lista de tareas.
            if not tarea['completada']:  # Verifica si la tarea actual no está completada.
                print(f"Próxima tarea pendiente: {tarea['tarea']}")  # Imprime la tarea pendiente.
                return  # Sale de la función.
        print("No hay tareas pendientes.")  # Si no hay tareas pendientes, imprime un mensaje indicándolo.

gestor = GestorTareas()  # Crea una instancia de la clase GestorTareas.

# Agregar tareas
gestor.agregar_tarea("Hacer la compra")  # Llama al método para agregar una tarea.
gestor.agregar_tarea("Llamar al médico")  # Llama al método para agregar otra tarea.
gestor.agregar_tarea("Estudiar para el examen")  # Llama al método para agregar otra tarea.

gestor.marcar_como_completada("Hacer la compra")  # Llama al método para marcar una tarea como completada.

gestor.mostrar_proxima_tarea_pendiente()  # Llama al método para mostrar la próxima tarea pendiente.