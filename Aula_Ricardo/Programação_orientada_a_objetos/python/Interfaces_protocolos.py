from typing  import Protocol

class Imprimivel(Protocol):
    def imprimir(self) -> None:
        ...

class Relatorio:
    def imprimir(self) -> None:
        print("Imprimindo relatorio.")

class Contrato:
    def imprimir(self) -> None:
        print("Imprimindo contrato.")

def processar_impressao(documento: Imprimivel) -> None:
    documento.imprimir()

relatorio = Relatorio()
contrato = Contrato()

processar_impressao(relatorio)
processar_impressao(contrato)