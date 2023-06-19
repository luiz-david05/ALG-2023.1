from menu_utils import *
from function_utils import *


def main():
    menu()
    opcao = pegar_opcao_valida()

    while opcao != 0:
        if opcao == 1:
            vetor = criar_vetor_vazio()
            print("\nVetor criado com sucesso!")
            print()
            valor_padrao = get_int("Digite o valor padrão: ")
            vetor = preencher_vetor_com_valor_padrao(vetor, valor_padrao)
            print("\nVetor preenchido com sucesso!")
            print()
            continuar()
            menu()
            opcao = pegar_opcao_valida()
        elif opcao == 2:
            vetor = preencher_vetor(vetor)
            print("\nVetor preenchido com sucesso!")
            print()
            continuar()
            menu()
            opcao = pegar_opcao_valida()
        elif opcao == 3:
            min = get_int("Digite o valor mínimo: ")
            max = get_int("Digite o valor máximo: ")
            vetor = preencher_vetor_automaticamente(vetor, min, max)
            print("\nVetor preenchido com sucesso!")
            print()
            continuar()
            menu()
            opcao = pegar_opcao_valida()
        elif opcao == 4:
            mostrar_vetor(vetor)
            print()
            continuar()
            menu()
            opcao = pegar_opcao_valida()
        elif opcao == 5:
            n = get_int("Digite o valor de n: ")
            vetor = map(elevar_elementos_por_n(n), vetor)
            print("\nVetor transformado com sucesso!")
            print()
            continuar()
            menu()
            opcao = pegar_opcao_valida()
        elif opcao == 6:
            positivos = filter(eh_positivo, vetor)
            negativos = filter(eh_negativo, vetor)
            nulos = filter(eh_nulo, vetor)
            print()
            print(f"Quantidade de elementos positivos: {len(positivos)}")
            print(f"Quantidade de elementos negativos: {len(negativos)}")
            print(f"Quantidade de elementos nulos: {len(nulos)}")
            print()
            continuar()
            menu()
            opcao = pegar_opcao_valida()
        elif opcao == 7:
            positivos = filter(eh_positivo, vetor)
            negativos = filter(eh_negativo, vetor)
            print()
            print(f"Somatório dos elementos: {reduce(somar_elementos, vetor)}")
            print(f"Somatório dos elementos positivos: {reduce(somar_elementos, positivos)}")
            print(f"Somatório dos elementos negativos: {reduce(somar_elementos, negativos)}")
            print()
            continuar()
            menu()
            opcao = pegar_opcao_valida()
        elif opcao == 8:
            positivos = filter(eh_positivo, vetor)
            negativos = filter(eh_negativo, vetor)
            print()
            print(f"Média dos elementos: {media_elementos(vetor)}")
            print(f"Mediana dos elementos: {mediana_elementos(vetor)}")
            print()
            print(f"Média dos elementos positivos: {media_elementos(positivos)}")
            print(f"Mediana dos elementos positivos: {mediana_elementos(positivos)}")
            print()
            print(f"Média dos elementos negativos: {media_elementos(negativos)}")
            print(f"Mediana dos elementos negativos: {mediana_elementos(negativos)}")
            print()
            continuar()
            menu()
            opcao = pegar_opcao_valida()
        elif opcao == 9:
            print()
            maior, indice = maior_indice_elemento(vetor)
            print(f"Maior elemento: {maior} - Índice: {indice}")
            print()
            menor, indice = menor_indice_elemento(vetor)
            print(f"Menor elemento: {menor} - Índice: {indice}")
            print()
            continuar()
            menu()
            opcao = pegar_opcao_valida()
        elif opcao == 10:
            positivos = filter(eh_positivo, vetor)
            negativos = filter(eh_negativo, vetor)
            print()
            print(f"Sorteando um número positivo: {sortear_elemento(positivos)}")
            print(f"Sorteando um número negativo: {sortear_elemento(negativos)}")
            print()
            continuar()
            menu()
            opcao = pegar_opcao_valida()
        # elif opcao == 11:
        
        elif opcao == 12:
            novo_vetor = criar_vetor_vazio()
            novo_vetor = preencher_vetor(novo_vetor)
            print()
            print(f"O vetor {novo_vetor} está contido 100%  no vetor {vetor}?")
            print()
            if verificar_se_ventor_contido_em_outro(novo_vetor, vetor):
                print("Resposta: Sim")
            else:
                print("Resposta: Não")
            print()
            continuar()
            menu()
            opcao = pegar_opcao_valida()

    tchau_personalizado()    

def menu():
    print("1 - Criar vetor vazio e preencher com valor padrão")
    print("2 - Preencher vetor")
    print("3 - Preencher vetor com números aleatórios")
    print("4 - Mostrar vetor")
    print("5 - Transformar vetor: elevar a potência n")
    print("6 - Contar elementos: positivos, negativos, nulos")
    print("7 - Somatório: todos os elementos, positivos e os negativos")
    print("8 - Exibir média e mediana: todos os elementos, positivos e os negativos")
    print("9 - Exibir maior e menor elemento e seus índices")
    print("10 - Sortear dois números: um positivo e outro negativo")
    # print("11 - Gerar N grupos de T tamanhos. Não repetir elementos")
    print("12 - Gerar novo vetor e verificar se está contido no vetor original (e na mesma ordem)")
    # print("13 - Top N maiores elementos")
    # print("14 - Top N menores elementos")
    # print("15 - Listar valor médio, e listar números maiores que a média e menores que a média")
    # print("16 - Somatório da média dos números positivos múltiplos de dois com o produto acumulado dos números negativos pares reduzidos pela metade")
    # print("17 - Ordenar elementos do vetor em ordem crescente")
    # print("18 - Ordenar elementos do vetor em ordem decrescente")
    # print("19 - Remover elementos múltiplos de N e M do vetor (simultaneamente)")
    print("0 - SAIR DO PROGRAMA")


def pegar_opcao_valida():
    opcao = int(input("\nDigite a opção desejada: "))

    while opcao < 0 or opcao > 19:
        print("\nOpção inválida!")
        opcao = int(input("\nDigite a opção desejada: "))
    
    return opcao


def continuar():
    continuar = input("\nPressione ENTER para continuar...")
    clear()


def clear():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


def tchau_personalizado():
    import random
    tchau = ["Hasta la vista, baby", "I am Groot!", "I'll be back", "Que a Força esteja com você... sempre"]
    print(random.choice(tchau))


if __name__ == "__main__":
    main()