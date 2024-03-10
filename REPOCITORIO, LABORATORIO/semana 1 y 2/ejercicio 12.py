"12. Verifica si una palabra ingresada por el usuario es un palíndromo."

# Solicita al usuario que ingrese una palabra, la convierte a minúsculas y elimina los espacios
palabra = input("Ingrese una palabra: ").lower().replace(" ", "")
# Imprime si la palabra ingresada es un palíndromo o no, comparando la palabra con su versión invertida
print(f"¿'{palabra}' es un palíndromo? {palabra == palabra[::-1]}")