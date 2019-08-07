# Ejemplo 1:
#   Caso de los números pares/impares

number = float(input("Introduce un número: "))
number = int(number)

if number % 2 == 0:
    print(f"El número {number} es par.")
else:
    print(f"El número {number} es impar.")
print()


# Ejemplo 2:
#   Caso de colores de perritos
color = input("Ingresa el color de tu perrito: ")

if color == "café":
    print("Ay, qué bonito perrito.")
elif color == "negro" or color == "Negro":
    print("Ay, de seguro es juguetón.")
elif color == "morado":
    print("Ay, lamento mucho tu pérdida.")
else:
    print("Ay, no conozco ese color.")
