from get_functions import *

# tempo de resolução: 60 minutos

def main():  
    # max de parcelas = 24, min = 2 parcelas
    # valor minímo do emprestimo = salario minimo
    # valor náximo da parcela = 40% da renda mensal informada

    renda_mensal = get_valid_number("informe sua renda mensal: ")
    valor_emprestimo = pegar_valor_do_emprestimo_valido("valor do empréstimo: ")
    prazo_desejado = pegar_numero_de_parcelas_valido("escolha a quantidade de parcelas(máximo = 24 parcelas, mínimo = 2 parcelas): ")

    prazo_dias = prazo_desejado // 30

    iof = valor_emprestimo * (0.38 / 100) + prazo_dias * 0.0082

    taxa_selic = 13.75 / 100

    # calcular quanto aplicar da taxa selic sobre o juros

    if prazo_desejado <= 6:
        porcentagem_selic = taxa_selic * 0.5
    
    elif prazo_desejado > 6 and prazo_desejado <= 12:
        porcentagem_selic = taxa_selic * 0.75

    elif prazo_desejado > 12 and prazo_desejado <= 18:
        porcentagem_selic = taxa_selic

    elif prazo_desejado > 18:
        porcentagem_selic = taxa_selic + taxa_selic * 0.30

    valor_juros = (valor_emprestimo + iof) * porcentagem_selic 

    # calcular valor das parcelas

    valor_parcelas = (valor_emprestimo + iof + valor_juros) / prazo_desejado

    # calcular valor total do empréstimo

    valor_total_emprestimo = valor_parcelas * prazo_desejado

    # % comprometimento da renda mensal sobre o valor da percela

    percentual_da_renda = (valor_parcelas / renda_mensal) * 100

    # exibindo os dados

    print(f"\nvalor do empréstimo: R$ {valor_emprestimo:.2f}")
    print(f"valor do iof: R$ {iof:.2f}")
    print(f"valor do juros: R$ {valor_juros:.2f}")
    print(f"valor total a pagar: R$ {valor_total_emprestimo:.2f}")
    print(f"valor da parcela mensal: {prazo_desejado}x de R${valor_parcelas:.2f}")
    print(f"você terá que comprometer {percentual_da_renda:.2f}% da sua renda mensal para pagar a parcela mensalmente")
    
    # verificando se a renda mensal se encaixa na regra

    if renda_mensal * 0.4 < valor_parcelas:
        print(f"Empréstimo negado!")

    else:
        print(f"Empréstimo aprovado!")


def pegar_numero_de_parcelas_valido(texto):
    numero_parcelas = get_valid_number(texto)

    if numero_parcelas > 24 and numero_parcelas < 2:
        print("informe a quantidade parcelas conforme a regra")

        numero_parcelas = pegar_numero_de_parcelas_valido(texto)

    return numero_parcelas


def pegar_valor_do_emprestimo_valido(texto):
    valor_emprestimo = get_valid_number(texto)

    if valor_emprestimo < 1302:
        print("valor minímo possível: R$ 1302.00")

        valor_emprestimo = pegar_valor_do_emprestimo_valido(texto)

    return valor_emprestimo


if __name__ == "__main__":
    main()
