
def main():

    lado_maior = input(print("Informe valor da área maior: "))
    lado_menor = input(print("Informe valor da área menor: "))

    resultado = int(lado_maior) * int(lado_menor)

    print(resultado)

    return resultado, lado_maior, lado_menor


if __name__ == "__main__":
    main()