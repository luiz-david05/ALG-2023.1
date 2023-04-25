from get_functions import *

# tempo de resolução: 39 minutos

def main():
    objetivo = input("Informe o seu objetivo: ")
    valor_realizar_objetivo = get_valid_number("Valor necessário para realizar o seu objetivo: ")
    salario = get_valid_number("Informe seu salário: ")
    percent_salario = pegar_fatia_valida_do_salario("Percentual do seu salário que pretende investir %: ") / 100
    taxa_juros_escolhido = pegar_taxa_de_investimento_valida("Taxa de juros do investimento escolhido %: ") / 100

    print()

    rendimento_mensal = 0
    qtd_meses = 0

    while rendimento_mensal < valor_realizar_objetivo:
        rendimento_mensal += salario * percent_salario
        rendimento_mensal += rendimento_mensal * taxa_juros_escolhido

        qtd_meses += 1

        print(f"Saldo acumulado após {qtd_meses} mês(es): R$ {rendimento_mensal:.2f}")

    if qtd_meses >= 12:
        qtd_anos = qtd_meses // 12
        qtd_meses = qtd_meses % 12

        print(f"\nVocê levará {qtd_anos} ano(s) e {qtd_meses} mes(es) para alcançar seu objetivo de : R${valor_realizar_objetivo:.2f}")   

    else:
        print(f"\nVocê levará mês(es) para alcançar seu objetivo de R$ {valor_realizar_objetivo:.2f}")   


def pegar_taxa_de_investimento_valida(texto):
    taxa = get_valid_number(texto)

    if taxa < 0.01 and taxa > 1:
        print("Digite uma taxa válida: entre [0,01% e 1,00%]")

        taxa = pegar_taxa_de_investimento_valida(texto)

    return taxa


def pegar_fatia_valida_do_salario(texto):
    fatia = get_valid_number(texto)

    if fatia >= 30:
        print("Digite um percentual válido inferior a 30%")

        fatia = pegar_fatia_valida_do_salario(texto)

    return fatia


if __name__ == "__main__":
    main()

