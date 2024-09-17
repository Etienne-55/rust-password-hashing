class Empresa:
    def __init__(self):
        self.funcionario = []

    def adicionar_funcionario(self, funcionario):
        self.funcionario.append(funcionario)

    def listar_funcionario(self):
        for funcionario in self.funcionario:
            print(funcionario)


class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return f"Funcionario Nome: {self.nome}, Cargo: {self.cargo}, salario: {self.salario}"
    

if __name__ == "__main__":
    empresa = Empresa()

    func1 = Funcionario("Pedro", "vigia", 2000)


    empresa.adicionar_funcionario(func1)

    empresa.listar_funcionario()


