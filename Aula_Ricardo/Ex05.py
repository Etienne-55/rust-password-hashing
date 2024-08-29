
# Coleta Dados do Usuário: Recebe uma lista de nomes e idades.
# Armazena Dados em um Dicionário: Usa um dicionário para associar cada nome à sua idade.
# Salva Dados em um Arquivo .txt: Grava os dados armazenados no dicionário em um arquivo de texto.
# Autor: Ricardo Roberto de Lima..

from biblioteca import coletar_dados, salvar_em_arquivo


def main():
    
    dados = coletar_dados()
    if dados:
        salvar_em_arquivo(dados, 'dados_pessoas.txt')
        print("Dados salvos no arquivo 'dados_pessoas.txt'.")
    else:
        print("Nenhum dado foi coletado.")

if __name__ == "__main__":
    main()