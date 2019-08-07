def F(m, a):
    return m*a


def saludo(name):
    return f"Hola {name}."


def print_directory(names):
    for name in names:
        print(f"- {name}")


def in_list(name, names):
    for element in names:
        if name == element:
            return True
    return False


nombres = ["Bubu", "Zaido", "Rodo", "Clau"]
print(in_list("Chava", nombres))
