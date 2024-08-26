# Faça um programa em Python que receba 6 numeros inteiros e mostre: ´
#  • Os numeros pares digitados; 
#  • A soma dos numeros pares digitados; 
#  • Os numeros   ımpares digitados;
#  • A quantidade de numeros  ımpares 

from biblioteca import adicionar_numeros, somar_numeros_pares

def main():

    numeros, numeros_pares, numeros_impares, soma_pares = adicionar_numeros(6)
    numeros_pares, numeros_impares, soma_pares = somar_numeros_pares(numeros, numeros_pares, numeros_impares, soma_pares)
    
    print("Os números pares digitados são:")
    for numero in numeros_pares:
        print(numero)
    
    print("A soma dos números pares digitados é:", soma_pares)
    
    print("Os números ímpares digitados são:")
    for numero in numeros_impares:
        print(numero)
    
    print("A quantidade de números ímpares digitados é:", len(numeros_impares))

if __name__ == "__main__":  
    main()