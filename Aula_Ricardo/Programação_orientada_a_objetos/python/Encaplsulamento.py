class Conta_bancaria():
    def __init__(self, titular):

        self.titular = titular
        self.saldo = 0

    def depositar(self, adicionar):
        self.saldo += adicionar

    def sacar(self, remover):
        self.saldo = max(0, self.depositar - remover)

    def exibir_saldo(self):
        print(f"Saldo: {self.saldo}")
    

titular1 = Conta_bancaria("etienne")

titular1.depositar(100000)
titular1.exibir_saldo()