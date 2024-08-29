# Faça um programa em Python para gerar automaticamente numeros entre 0 e 99 de uma cartela de bingo. Sabendo que cada cartela devera conter 5 linhas de 5 numeros, gere estes dados de modo a nao ter numeros repetidos dentro das cartelas. O programa deve exibir na ´
# tela a cartela gerada.

from biblioteca import gerar_cartela, gerar_cartela_completa

def main():
    cartela = gerar_cartela()
    print("Cartela de bingo:")
    for linha in cartela:
        print(linha)

    print("\n")
    
    cartela_completa = gerar_cartela_completa()
    print("Cartela completa:")
    for linha in cartela_completa:
        print(linha)


if __name__ == "__main__":
    main()