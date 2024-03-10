"13. Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que están duplicados."

def encontrar_duplicados(conjunto):
    # Esta función recibe un conjunto de números y busca los duplicados dentro de él.
   
    duplicados = set()  # Aquí se crea un conjunto vacío para almacenar los números duplicados.
    unicos = set()  # Aquí se crea un conjunto vacío para almacenar los números únicos.
    
    for num in conjunto:  # Se itera sobre cada número en el conjunto dado.
        if num in unicos:  # Si el número ya está en el conjunto de números únicos, entonces es un duplicado.
            duplicados.add(num)  # Se agrega el número duplicado al conjunto de duplicados.
        else:  # Si el número no está en el conjunto de números únicos, entonces es único.
            unicos.add(num)  # Se agrega el número único al conjunto de únicos.
    
    return duplicados  # Se devuelve el conjunto de números duplicados.

numeros = {1, 2, 3, 4, 5, 2, 3, 6}  # Se define un conjunto de números con duplicados.
print("Los números duplicados son:", encontrar_duplicados(numeros))  # Se llama a la función para encontrar los duplicados y se imprime el resultado.



