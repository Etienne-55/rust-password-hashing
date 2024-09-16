class Animal():
    def __init__(self, especie, nome):
        self._especie = especie
        self._nome = nome
    
    @property
    def especie(self):
        return self._especie
    
    @especie.setter
    def especie(self, value):
        self._especie = value
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, value):
        self._nome = value
    
    def emitir_som(self):
        pass

def main():

    
    animal = Animal("aaa", "aaa")
     
    print(animal.especie)  
    print(animal.nome)  
    
    animal.especie = "gato"
    animal.nome = "gato1"
    
    print(animal.especie)  
    print(animal.nome) 

if __name__ == "__main__":
    main()