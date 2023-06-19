from entrada_utils import *
from rifa_utils import *


def main():
    # pontos carregados do arquivo texto
    print("Carregando pontos...")
    print("Pontos carregados com sucesso!")
    pontos = get_pontos()

    menu()
    opcao = opcao_valida()

    while opcao != 0:
        if opcao == 1:
            mostrar_pontos(pontos)

            enter()
            menu()
            opcao = opcao_valida()
            enter()
        elif opcao == 2:
            adicionar_ponto(pontos)

            enter()
            menu()
            opcao = opcao_valida()
        elif opcao == 3:
            valor_ponto = get_valor_ponto()

            valor_da_rifa = valor_ponto * len(pontos)

            print(f"Valor do ponto: {valor_ponto}")

            enter()
            menu()
            opcao = opcao_valida()
        elif opcao == 4:
            taxa_administracao = get_number("Digite a taxa de administração %: ")

            enter()
            menu()
            opcao = opcao_valida()
        elif opcao == 5:
            valor_total_rifa = valor_da_rifa + (taxa_administracao / 100 * valor_da_rifa)

            print(f"\nValor total da rifa: {valor_total_rifa}")
            print(f"Valor da rifa: {valor_da_rifa}")
            print(f"Taxa de administração: {taxa_administracao}%")
            print(f"Valor da taxa de administração: {taxa_administracao / 100 * valor_da_rifa}")

            enter()
            menu()
            opcao = opcao_valida()
        elif opcao == 6:
            quantidade_premios = get_number("Digite a quantidade de prêmios que serão sorteados: ")

            enter()
            menu()
            opcao = opcao_valida()
        elif opcao == 7:
            sortear_premios(pontos, quantidade_premios)

            enter()
            menu()
            opcao = opcao_valida()
        elif opcao == 8:
            pontos = []
            print("Rifa resetada com sucesso!")

            enter()
            menu()
            opcao = opcao_valida()
        elif opcao == 9:
            pontos_nao_vendidos = []
            print("\nPontos não vendidos:")
            for i in range(len(pontos)):
                if pontos[i] == "-":
                    print(f"{i+1} - {pontos[i]}")
                    pontos_nao_vendidos.append(pontos[i])
            print(f"Quantidade de pontos disponíveis: {len(pontos_nao_vendidos)}")
            enter()

            pontos_vendidos = []
            print("\nPontos vendidos:")
            for i in range(len(pontos)):
                if pontos[i] != "-":
                    print(f"{i+1} - {pontos[i]}")
                    pontos_vendidos.append(pontos[i])
            print(f"Quantidade de pontos vendidos: {len(pontos_vendidos)}")
            
            enter()
            menu()
            opcao = opcao_valida()
    thanks()


def menu():
    print("\n1 - Mostrar pontos")
    print("2 - Adicionar ponto")
    print("3 - Valor do ponto da rifa")
    print("4 - Valor da taxa de administração")
    print("5 - Valor total da rifa")
    print("6 - Quantidade de prêmios que serão sorteados")
    print("7 - Realizar sorteio")
    print("8 - resetar rifa")
    print("9 - Dados gerais da rifa (Quantidade de pontos disponíveis, quantidade de pontos vendidos, quantidade de pontos não vendidos.")
    print("0 - Sair")


def opcao_valida():
    opcao = get_number("\nDigite uma opção: ")

    if opcao < 0 or opcao > 9:
        print("Opção inválida!")
        opcao_valida()
    
    return opcao


def enter():
    input("Pressione ENTER para continuar...")
    print()


def clear():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


def thanks():
    tchaus = ["Tchau!", "Até mais!", "Até logo!", "Até a próxima!", "Até breve!", "May the Force be with you!", "I'll be back.", "To infinity and beyond!", "Hasta la vista, baby!", "Live long and prosper.", "May the odds be ever in your favor!", "I have a dream.", "Carpe diem.", "Elementary, my dear Watson.", "Go ahead, make my day.", "I'm the king of the world!", "I see dead people.", "Frankly, my dear, I don't give a damn.", "Here's looking at you, kid.", "You can't handle the truth!"]

    from random import randint

    print(tchaus[randint(0, len(tchaus)-1)])


if __name__ == "__main__":
    main()