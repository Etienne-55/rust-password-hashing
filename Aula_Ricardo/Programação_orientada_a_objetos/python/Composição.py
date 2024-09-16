class Motor:
    def __init__(self):
        self.estado = "desligado"

    def ligar(self):
        self.estado = "ligado"
        return "Motor ligado"
    
    def desligar(self):
        self.estado = "desligado"
        return "Motor desligado"
    
class Carro:
    def __init__(self):
        self.motor = Motor()

    def ligar_carro(self):
        return self.motor.ligar()
    
    def desligar_carro(self):
        return self.motor.desligar()
    
if __name__ == "__main__":
    carro = Carro()
    print(carro.ligar_carro())
    print(carro.desligar_carro())