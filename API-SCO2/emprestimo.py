from get_functions import *


def main():
    pass
    # max de parcelas = 24, min = 2 parcelas
    # valor minímo do emprestimo = salario minimo
    # valor náximo da parcela = 40% da renda mensal informada

    renda_mensal = get_valid_number("informe sua renda mensal: ")
    valor_emprestimo = get_valid_number("valor do empréstimo: ")
    prazo_desejado = get_valid_number("escolha a quantidade de parcelas(máximo = 24 parcelas, mínimo = 2 parcelas): ")

    print(f"valor do empréstimo: R$ {valor_emprestimo:.2f}")

    valor_parcela = valor_emprestimo / prazo_desejado

    if valor_parcela > renda_mensal * 0.40:
        print(f"Seu salário não suporta a parcela")

    else:
        pass
