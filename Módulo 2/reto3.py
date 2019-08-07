dieta = {
    "lunes": ["Pollo con mole", "Arroz blanco", "Frijolinis"],
    "martes": ["Atún", "Fideos"],
    "viernes": ["Ensalada", "Subway"]
}

"""
print(dieta.keys())
print(list(dieta))
print(dieta.items())
"""

# print(list(dieta))
for dia in list(dieta):
    print(f"La comida del día {dia} es:")
    for comida in dieta[dia]:
        print(f"- {comida}")
    print()
