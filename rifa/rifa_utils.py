from entrada_utils import *


def mostrar_pontos(pontos):
    print("Pontos:")
    for i in range(len(pontos)):
        print(f"{i+1} - {pontos[i]}")


def adicionar_ponto(pontos):
    for i in range(len(pontos)):
        if pontos[i] == "-":
            pontos[i] = input("Digite o nome do ponto: ")
            print("Ponto adicionado com sucesso!")
            return pontos


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