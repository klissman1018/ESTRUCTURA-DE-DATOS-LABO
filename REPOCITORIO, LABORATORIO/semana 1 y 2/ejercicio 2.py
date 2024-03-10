"2.Solicita un número al usuario y determina si es par o impar."

numero = int(input("Ingrese un número: "))  # Esta línea solicita al usuario que ingrese un número y lo convierte a entero.

if numero % 2 == 0:  # Esta línea verifica si el número ingresado es divisible entre 2 (es decir, si es par).
    print(f"{numero} es un número par.")  # Si el número es par, imprime que el número es par.
else:  # Si el número no es par (es decir, es impar),
    print(f"{numero} es un número impar.")  # imprime que el número es impar.
