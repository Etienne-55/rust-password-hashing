#descobrir o maior e o menor elemento de um vetor.

from biblioteca import criar_vetor_zerado, descobrir_maior_menor

def main():

    vetor = criar_vetor_zerado()
    resultado = descobrir_maior_menor(vetor)
    print("O maior elemento do vetor é %d." % resultado[0])
    print("O menor elemento do vetor é %d." % resultado[1])

if __name__ == "__main__":
    main()