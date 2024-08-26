def criar_vetor():
    
    vetor = [0] * 8

    
    for i in range(8):
        vetor[i] = int(input("Digite o valor da posição {}: ".format(i)))
    return vetor

def somar_valores_do_vetor(vetor):
                            

    x = int(input("Digite o valor de X: "))
    y = int(input("Digite o valor de Y: "))

   
    soma = vetor[x] + vetor[y]
    return soma

def criar_vetor_zerado():

    vetor = []

    for i in range(10):
        vetor.append(int(input("Digite o elemento %d: " % i)))
    
    return vetor

def descobrir_maior_menor(vetor):
        
        maior = vetor[0]
        menor = vetor[0]
    
        for i in range(1, len(vetor)):
            if vetor[i] > maior:
                maior = vetor[i]
            elif vetor[i] < menor:
                menor = vetor[i]
        
        return maior, menor

def subtrair_vetores():

    vetor_a = []
    vetor_b = []
    vetor_c = []
    for i in range(2):
        vetor_a.append(int(input("Digite o elemento %d do vetor A: " % i)))
        vetor_b.append(int(input("Digite o elemento %d do vetor B: " % i)))

    for i in range(2):
        vetor_c.append(vetor_a[i] - vetor_b[i])

    print("Vetor C:")
    for i in range(2):
        print(vetor_c[i])
    
    return vetor_c


def adicionar_numeros(n):

    numeros = []
    numeros_pares = []
    numeros_impares = []
    soma_pares = 0

    for i in range(6):
        numeros.append(int(input("Digite um número: ")))
    return numeros, numeros_pares, numeros_impares, soma_pares

def somar_numeros_pares(numeros, numeros_pares, numeros_impares, soma_pares):

    for numero in numeros:
        if numero % 2 == 0:
            numeros_pares.append(numero)
            soma_pares += numero
        else:
            numeros_impares.append(numero)
    return numeros_pares, numeros_impares, soma_pares