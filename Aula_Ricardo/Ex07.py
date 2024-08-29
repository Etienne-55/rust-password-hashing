# Faça um programa em Python para gerar automaticamente numeros entre 0 e 99 de uma cartela de bingo. Sabendo que cada cartela devera conter 5 linhas de 5 numeros, gere estes dados de modo a nao ter numeros repetidos dentro das cartelas. O programa deve exibir na ´
# tela a cartela gerada.

from biblioteca import gerar_cartela

def main():
    cartela = gerar_cartela()
    print("Cartela de bingo:")
    for linha in cartela:
        print(linha)


if __name__ == "__main__":
    main()