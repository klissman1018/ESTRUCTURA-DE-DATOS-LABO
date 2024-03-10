"11. Ordena una lista de números ingresados por el usuario de menor a mayor."

# Solicita al usuario que ingrese números separados por comas y los almacena como una cadena de texto en la variable 'numeros'.
numeros = input("Ingrese una serie de números separados por comas: ")

# Convierte la cadena de texto almacenada en 'numeros' en una lista de enteros. 
# Primero, utiliza el método split(",") para dividir la cadena en una lista de cadenas, separadas por comas.
# Luego, con una comprensión de lista, convierte cada elemento de la lista en un entero.
numeros = [int(num) for num in numeros.split(",")]

# Ordena la lista de números enteros en orden ascendente.
numeros.sort()

# Imprime la lista de números ya ordenada.
print(numeros)