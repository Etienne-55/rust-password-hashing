# Programa em Python para gerenciar uma agenda telefônica:

# Valida Dados de Contato: Recebe e valida nomes e números de telefone.
# Armazena Dados em um Dicionário: Usa um dicionário para armazenar contatos, onde a chave é o nome e o valor é o número de telefone.
# Salva e Carrega Dados em Arquivo .json: Grava e lê os dados em um arquivo JSON.
# Estrutura do Programa
# Coletar e Validar Dados:

# Receber nome e número de telefone do usuário.
# Validar o formato do número de telefone.
# Manipular Dados:

# Adicionar, editar e excluir contatos no dicionário.
# Salvar e Carregar Dados:

# Gravar e ler dados em um arquivo JSON.

from biblioteca import coletar_dados, salvar_em_arquivo, carregar_do_arquivo,exibir_contatos


def main():
    
    nome_arquivo = 'agenda_telefonica.json'
    contatos = carregar_do_arquivo(nome_arquivo)
    
    while True:
        print("\nMenu:")
        print("1. Adicionar/Editar Contato")
        print("2. Exibir Contatos")
        print("3. Salvar e Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            novos_contatos = coletar_dados()
            contatos.update(novos_contatos)
        elif escolha == '2':
            exibir_contatos(contatos)
        elif escolha == '3':
            salvar_em_arquivo(contatos, nome_arquivo)
            print(f"Dados salvos em '{nome_arquivo}'.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()