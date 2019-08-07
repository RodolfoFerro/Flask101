# 1. Escribir un programa que pida una edad como input.
# 2. Convertir la variable de entrada a número entero.
# 3. Comparar el valor del número entero para ver si es legal.

edad = input("Introduce tu edad: ")
edad = int(edad)

if edad >= 18:
    print("Eres legal.")
else:
    print("No eres legal.")
