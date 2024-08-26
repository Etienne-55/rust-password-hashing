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