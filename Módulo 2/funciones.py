def legal_o_no(edad):
    resultado = False

    if edad >= 18:
        resultado = True
    else:
        resultado = False

    return resultado


def pide_edad():
    edad = int(input("Introduce tu edad: "))
    return edad


def func_para_calcular_una_derivad():
    pass


# edad = pide_edad()
# print(legal_o_no(edad))
