from abc import ABC, abstractmethod

class Funcionario(ABC):
    @abstractmethod    
    def calcular_salario(self):
        pass
    

class FuncionarioHorista(Funcionario):
    def __init__(self, valor_hora, horas_trabalhadas):
        self.valor_hora = valor_hora
        self.horas_trabalhasdas = horas_trabalhadas

    def calcular_salario(self):
            return self.horas_trabalhasdas * self.valor_hora


class FuncionarioAssalariado(Funcionario):
    def __init__(self, salario_mensal):
        self.salario_mensal = salario_mensal

    def calcular_salario(self):
        return self.salario_mensal
    
horista = FuncionarioHorista(100, 20)
assalariado = FuncionarioAssalariado(2000)

print(horista.calcular_salario())
print(assalariado.calcular_salario())