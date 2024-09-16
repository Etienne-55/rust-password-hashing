class Carro: 
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0

    def exibir_detalhes(self):
        print(f'Marca:{self.marca}, Modelo:{self.modelo}, Ano:{self.ano}')

    def acelerar(self, incremento):
        self.velocidade += incremento
    
    def frear(self, decremento):
        self.velocidade = max(0, self.velocidade - decremento)

    def exibir_velocidade(self):
        print(f'A velocidade atual é de {self.velocidade} km/h')


carro1 = Carro('Toyota', 'Land cruiser', 2010)
carro2 = Carro('honda', 'civic', 2018)
carro1.exibir_detalhes()
carro2.exibir_detalhes()


carro1.acelerar(70)
carro1.exibir_velocidade()
carro1.frear(25)
carro1.exibir_velocidade()
carro2.acelerar(120)
carro2.exibir_velocidade()
