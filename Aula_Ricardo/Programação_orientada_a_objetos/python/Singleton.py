class Configuracao:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, valor=None):
        if not hasattr(self, 'initialized'):
            self.valor = valor
            self.initialized = True

config1 = Configuracao(valor="Configuração 1")
print(config1.valor)  

config2 = Configuracao(valor="Configuração 2")
print(config2.valor)  

print(config1 is config2) 