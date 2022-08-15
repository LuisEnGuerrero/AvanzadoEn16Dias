def numeros_perfumeria():
    for n in range(1, 10000):
        yield f"P - {n}"


def numeros_farmacia():
    for n in range(1, 10000):
        yield f"F - {n}"


def numeros_cosmetica():
    for n in range(1, 10000):
        yield f"C - {n}"


p = numeros_perfumeria()
f = numeros_farmacia()
c = numeros_cosmetica()


def decorador(departamento):

    print("\n" + "*" * 23)
    print("Su Turno es: ")

    if departamento == "P":
        print(next(p))

    if departamento == "F":
        print(next(f))

    if departamento == "C":
        print(next(c))

    print("Pronto será atendido!")
    print("*" * 23 + "\n")


