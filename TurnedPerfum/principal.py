import numeros


def preguntar():
    print("Bienvenido a la Farmacia Python!")

    while True:
        print("[P] - Perfumeria\n[F] - Farmacia\n[C] - Cosmética")
        try:
            departamento = input("Elija la dependencia deseada: ").upper()
            ["P", "F", "C"].index(departamento)
        except ValueError:
            print("ERROR!! Esa No es una opción Válida!")
        else:
            break

    numeros.decorador(departamento)


def inicio():
    while True:
        preguntar()
        try:
            otro_turno = input("Quieres tomar otro turno? [S] [N]: ").upper()
            ["S", "N"].index(otro_turno)
        except ValueError:
            print("ERROR!! Esa No es una opción Válida!")
        else:
            if otro_turno == "N":
                print("Gracias por su Visita")
                break


inicio()
