class Animal:

    def som(self):
        raise NotImplementedError("")
    
    
class Cachorro(Animal):
    def som(self):
        return "auau"

class Gato(Animal):
    def som(self):
        return "miauu"


if __name__ == "__main__":
    cachorro = Cachorro()
    gato = Gato()
    print(f"Cachorro: {cachorro.som()}")
    print(f"Gato: {gato.som()}")
    print(gato.som())