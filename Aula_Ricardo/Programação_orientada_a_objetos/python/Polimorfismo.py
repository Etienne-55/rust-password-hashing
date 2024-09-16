class Animal:
    def som(self):
        raise NotImplementedError("")
    
class Vaca(Animal):
    def som(self):
        return "Auau"
    
class gato(Animal):
    def som(self):
        return "MUUU"
    
def emitir_som(animais):
    for animal in animais:
        print(animal.som())

animais = [Vaca(), gato()]
emitir_som(animais)