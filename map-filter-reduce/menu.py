from menu_utils import *


def main():
    menu()
    opcao = pegar_opcao_valida()

    while opcao != 0:
        if opcao == 1:
            vetor = criar_vetor_vazio()
            print("\nVetor criado com sucesso!")
            print()
            menu()
            opcao = pegar_opcao_valida()
        elif opcao == 2:
            vetor = preencher_vetor(vetor)
            print("\nVetor preenchido com sucesso!")
            print()
            menu()
            opcao = pegar_opcao_valida()
        elif opcao == 3:
            max = int(input("Digite o valor máximo: "))
            min = int(input("Digite o valor mínimo: "))

            vetor = preencher_vetor_automaticamente(vetor, min, max)
            print("\nVetor preenchido com sucesso!")
            print()
            menu()
            opcao = pegar_opcao_valida()
        elif opcao == 4:
            mostrar_vetor(vetor)
            print()
            menu()
            opcao = pegar_opcao_valida()
        elif opcao == 5:
            n = int(input("Digite o valor de n: "))
            vetor = elevar_elementos_do_vetor(vetor, n)
            print("\nVetor transformado com sucesso!")
            print()
            menu()
            opcao = pegar_opcao_valida()

    print("\nTchau, fim do programa!")    

def menu():
    print("1 - Criar vetor vazio")
    print("2 - Preencher vetor")
    print("3 - Preencher vetor com números aleatórios")
    print("4 - Mostrar vetor")
    print("5 - Transformar vetor: elevar a potência n")
    # print("6 - Contar elementos: positivos, negativos, nulos")
    # print("7 - Somatório: positivos, negativos, nulos")
    # print("8 - Exibir média e mediana")
    # print("9 - Exibir maior e menor elemento e seus índices")
    # print("10 - Sortear dois números: um positivo e outro negativo")
    # print("11 - Gerar N grupos de T tamanhos. Não repetir elementos")
    # print("12 - Gerar novo vetor e verificar se está contido no vetor original (e na mesma ordem)")
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


if __name__ == "__main__":
    main()