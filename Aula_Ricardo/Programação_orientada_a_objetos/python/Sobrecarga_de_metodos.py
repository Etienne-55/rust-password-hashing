class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor 

    def __add__(self, other):
        if isinstance(other, Produto):
            return Produto(self.nome+ ' & ' + other.nome, self.valor + other.valor)
        return NotImplemented
    
    def __str__(self):
        return f'{self.nome}: R${self.valor:.2f}'
    

produto1 = Produto("Produto A", 22)
produto2 = Produto("Produto B", 33)
produto3 = Produto("Produto C", 65)

produto4 = produto1 + produto2 + produto3

print(produto4)