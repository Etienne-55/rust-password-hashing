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