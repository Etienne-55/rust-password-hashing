class Calculadora: 
    def somar(self,a, b, c= None):
        if c is not None:
            return a + b + c
        return a + b

calc = Calculadora()
print(calc.somar(1, 2))
print(calc.somar(1, 2, 3))