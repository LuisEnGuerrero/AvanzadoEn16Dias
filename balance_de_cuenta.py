from BalanceDeCuentas.cliente import Cliente


def crear_cliente():
    nombre_cl = input("Ingrese su nombre: ")
    apellido_cl = input("Ingrese su apellido: ")
    numero_cuenta = input("Ingrese su numero de cuenta: ")
    cliente = Cliente(nombre_cl, apellido_cl, numero_cuenta)
    return cliente


def inicio():
    mi_cliente = crear_cliente()
    print(mi_cliente)
    opcion = 0

    while opcion != 'S':
        print('Elije: \n\tDepositar (D)\n\tRetirar (R) o\n\tSalir (S)')
        opcion = input()

        if opcion == 'D':
            monto_dep = int(input("\nMonto a Depositar: "))
            mi_cliente.depositar(monto_dep)
        elif opcion == 'R':
            monto_ret = int(input("\nMonto a Retirar: "))
            mi_cliente.retirar(monto_ret)
        else:
            print("ERROR! Elige una Opción válida!!!")
        print(mi_cliente)

    print("\nGracias por Operar en Banco Python!")


inicio()
