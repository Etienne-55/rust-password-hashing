import json
import re
import random

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

def coletar_dados():
    
    dados = []
    while True:
        nome = input("Digite o nome (ou 'sair' para encerrar): ")
        if nome.lower() == 'sair':
            break
        idade = input("Digite a idade: ")
        try:
            idade = int(idade)
        except ValueError:
            print("Idade deve ser um número inteiro. Tente novamente.")
            continue
        
        dados.append({'nome': nome, 'idade': idade})
    return dados

def salvar_em_arquivo(dados, nome_arquivo):
    
    with open(nome_arquivo, 'w') as arquivo:
        for item in dados:
            linha = f"Nome: {item['nome']}, Idade: {item['idade']}\n"
            arquivo.write(linha)

def validar_numero(numero):
    
    padrao = re.compile(r"^\(\d{2}\) \d{5}-\d{4}$")
    return bool(padrao.match(numero))

def coletar_dados():
    
    contatos = {}
    while True:
        nome = input("Digite o nome do contato (ou 'sair' para encerrar): ")
        if nome.lower() == 'sair':
            break

        numero = input("Digite o número de telefone (formato: (11) 12345-6789): ")
        if not validar_numero(numero):
            print("Número de telefone inválido. Tente novamente.")
            continue

        contatos[nome] = numero
    return contatos

def salvar_em_arquivo(contatos, nome_arquivo):
    
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(contatos, arquivo, indent=4)

def carregar_do_arquivo(nome_arquivo):
    
    try:
        with open(nome_arquivo, 'r') as arquivo:
            contatos = json.load(arquivo)
    except FileNotFoundError:
        contatos = {}
    return contatos

def exibir_contatos(contatos):
    
    if contatos:
        for nome, numero in contatos.items():
            print(f"Nome: {nome}, Telefone: {numero}")
    else:
        print("Nenhum contato encontrado.")

def gerar_cartela():
    numeros = set()
    cartela = []
    for i in range(5):
        numero = random.randint(0, 99)
        while numero in numeros:
            numero = random.randint(0, 99)
        numeros.add(numero)
        cartela.append(numero)
    return cartela

def gerar_cartela_completa():
    numeros = set()
    cartela = []
    for i in range(5):
        linha = []
        for j in range(5):
            numero = random.randint(0, 99)
            while numero in numeros:
                numero = random.randint(0, 99)
            numeros.add(numero)
            linha.append(numero)
        cartela.append(linha)
    return cartela