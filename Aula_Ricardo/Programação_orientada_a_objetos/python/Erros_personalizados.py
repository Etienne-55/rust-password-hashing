class SaldoInsuficente(Exception):
    def __init__(self, message="Saldo insuficiente"):
        self.message = message
        super().__init__(self.message)

class Conta_bancaria:
    def __init__(self, saldo=0):
        self.saldo = saldo

    def depositar(self, quantia):
        self.saldo += quantia

    def sacar(self, quantia):
        if quantia > self.saldo:
            raise SaldoInsuficente()
        self.saldo -= quantia

conta = Conta_bancaria(500)
try: 
    conta.sacar(499)
except SaldoInsuficente as e:
    print(e)