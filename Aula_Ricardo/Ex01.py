#Somar posiçao X e Y de um vetor. O vetor é de 2 elementos. A função deve retornar a soma.

from biblioteca import criar_vetor, somar_valores_do_vetor


def main():
    vetor = criar_vetor()
    soma = somar_valores_do_vetor(vetor)
    print("A soma dos valores nas posições X e Y é {}.".format(soma))

if __name__ == "__main__":
    main()