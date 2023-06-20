from entrada_utils import *


def mostrar_pontos(pontos):
    print("Pontos:")
    for i in range(len(pontos)):
        print(f"{i+1} - {pontos[i]}")


def adicionar_ponto(pontos):
    print("Pontos disponíveis:")
    for i in range(len(pontos)):
        if pontos[i] == "-":
            print(f"{i+1} - {pontos[i]} - {pontos[i]}")

    ponto_escolhido = get_number("Digite o número do ponto que deseja adicionar: ")

    if ponto_escolhido < 1 or ponto_escolhido > len(pontos) or pontos[ponto_escolhido-1] != "-":
        print("Ponto inválido!")
        adicionar_ponto(pontos)
    
    nome = get_string("Digite o nome da pessoa: ")

    pontos[ponto_escolhido-1] = nome

    print("Ponto adicionado com sucesso!")


def get_valor_ponto():
    valor = get_number("Digite o valor do ponto: ")

    if valor < 0:
        print("Valor inválido!")
        valor = get_valor_ponto()
    
    return valor


def sortear_premios(pontos, quantidade_premios):
    # . Mostrar o número sorteado e o nome da pessoa.
    from random import randint
    print("Sorteando prêmios...")
    print("Prêmios sorteados:")

    for i in range(quantidade_premios):
        numero_sorteado = randint(0, len(pontos)-1)
        
        while pontos[numero_sorteado] == "-":
            numero_sorteado = randint(0, len(pontos)-1)
        
        print(f"{i+1} - {pontos[numero_sorteado]} - {numero_sorteado+1}")
        

    
    print("\nPrêmios sorteados com sucesso!")