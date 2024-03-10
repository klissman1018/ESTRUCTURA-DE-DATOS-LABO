"1. Realiza la suma, resta, multiplicación y división de dos números ingresados por el usuario."

num1 = float(input("Ingrese el primer número: ")) # Esta línea solicita al usuario que ingrese un número y lo convierte a tipo flotante. Este será el primer número para realizar operaciones.
num2 = float(input("Ingrese el segundo número: ")) # Similar a la línea anterior, solicita un segundo número al usuario y lo convierte a tipo flotante.

suma = num1 + num2 # Realiza la suma de los dos números ingresados y almacena el resultado en la variable 'suma'.
resta = num1 - num2 # Realiza la resta del primer número menos el segundo número y almacena el resultado en la variable 'resta'.
multiplicacion = num1 * num2 # Realiza la multiplicación de los dos números ingresados y almacena el resultado en la variable 'multiplicacion'.

if num2 != 0: # Verifica si el segundo número es diferente de cero para proceder con la división.
    division = num1 / num2 # Si el segundo número no es cero, realiza la división del primer número entre el segundo y almacena el resultado en 'division'.
else:
    division = "No es posible dividir por cero." # Si el segundo número es cero, almacena un mensaje indicando que no es posible realizar la división en la variable 'division'.

print(f"Suma: {suma}") # Imprime el resultado de la suma.
print(f"Resta: {resta}") # Imprime el resultado de la resta.
print(f"Multiplicación: {multiplicacion}") # Imprime el resultado de la multiplicación.
print(f"División: {division}") # Imprime el resultado de la división o el mensaje de error si el segundo número fue cero.
