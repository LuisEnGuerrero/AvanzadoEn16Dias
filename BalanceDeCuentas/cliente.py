from BalanceDeCuentas.persona import Persona


class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance=0) -> None:
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}\n balance de cuenta {self.numero_cuenta}: ${self.balance}"

    def depositar(self, monto_deposito):
        self.balance += monto_deposito
        print("Deposito Aceptado!")

    def retirar(self, monto_retiro):
        if self.balance >= monto_retiro:
            self.balance -= monto_retiro
            print("Retiro Realizado!")
        else:
            print("Fondos Insuficientes")
