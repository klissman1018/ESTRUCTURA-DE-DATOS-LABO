"15. Toma un número entero y calcula la suma de sus dígitos."

# Solicita al usuario que ingrese un número entero y lo almacena en la variable 'numero'.
numero = input("Ingrese un número entero: ")

# Utiliza una comprensión de lista para convertir cada dígito del número ingresado a entero,
# luego suma todos los dígitos convertidos y almacena el resultado en 'suma_digitos'.
suma_digitos = sum(int(digito) for digito in numero)

# Imprime el resultado de la suma de los dígitos.
print(f"La suma de los dígitos es: {suma_digitos}")
