class Carro: 
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir_detalhes(self):
        print(f'Marca:{self.marca}, Modelo:{self.modelo}, Ano:{self.ano}')

carro1 = Carro('Toyota', 'Land cruiser', '2010')
carro1.exibir_detalhes()