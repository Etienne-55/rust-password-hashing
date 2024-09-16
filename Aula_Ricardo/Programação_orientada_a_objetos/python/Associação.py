class Professor:
    def __init__(self, nome):
        self.nome = nome
        self.escolas = []

    def adicionar_escola(self, escola):
        if escola not in self.escolas:
            self.escolas.append(escola)
            escola.adicionar_professor(self)

    def __repr__(self):
        return f"Professor({self.nome})"


class Escola:
    def __init__(self, nome):
        self.nome = nome
        self.professores = []

    def adicionar_professor(self, professor):
        if professor not in self.professores:
            self.professores.append(professor)
            professor.adicionar_escola(self)

    def __repr__(self):
        return f"Escola({self.nome})"



prof1 = Professor("Prof. João")
prof2 = Professor("Prof. Maria")

escola1 = Escola("Escola A")
escola2 = Escola("Escola B")

prof1.adicionar_escola(escola1)
prof1.adicionar_escola(escola2)
prof2.adicionar_escola(escola1)

print(escola1.professores)  
print(escola2.professores)  
print(prof1.escolas)        
print(prof2.escolas)        