from get_functions import *


def main():
    valor_iphone = 3500
<<<<<<< HEAD
    forma_pagamento = 'cartão de crédito'
=======
    forma_pagamento = pegar_forma_de_pagamento_valida()
>>>>>>> e91a96a63978650ca0613319dcf8458bfd8ce461

    if forma_pagamento == 'pix' or forma_pagamento == 'dinheiro':
        desconto = valor_iphone * 0.15
        valor_total = valor_iphone - desconto
    elif forma_pagamento == 'cartão de débito':
        desconto = valor_iphone * 0.10
        valor_total = valor_iphone - desconto
    elif forma_pagamento == 'cartão de crédito':
        desconto = 0
        entrada = get_number("valor da entrada: ")
        parcelas = pegar_qtd_parcelas_validas()
        valor_total = valor_iphone - entrada
        valor_juros = valor_total * 0.039 + parcelas * 0.015
        valor_total += valor_juros
        valor_parcelas = valor_total / parcelas

    # mostrar dados
    print("\n", 4 * "-", "simulador de compra", 4 * "-")
    print(f"\nproduto: iphone")
    print(f"forma de pagamento escolhida: {forma_pagamento}")
    print(f"valor a ser pago: R$ {valor_total:.2f}")
    print(f"valor das parcelas: R$ {valor_parcelas:.2f}")

    if forma_pagamento == "cartão de crédito":
        print(f"você pagará: R$ {valor_juros:.2f} em juros")
    else:
        print(f"você economizou: R$ {desconto:.2f}")


def pegar_forma_de_pagamento_valida(texto = "forma de pagamento: "):
    forma = input(texto)
    opcoes = ["pix", "dinheiro", "cartão de débito","cartão de crédito"]

    if forma not in opcoes:
        print("forma de pagamento inválida, formas válidas: pix, dinheiro, cartão de débito ou cartão de crédito")

        forma = pegar_forma_de_pagamento_valida(texto)

    return forma


def pegar_qtd_parcelas_validas(texto = "quantidade de parcelas: "):
    parcelas = get_number(texto)

    if parcelas < 1 or parcelas > 12:
        print("quantidade de parcelas inválidas, é possível parcelar em até 12x")

        parcelas = pegar_qtd_parcelas_validas(texto)

    return parcelas


if __name__ == "__main__":
<<<<<<< HEAD
    main()
=======
    main()
>>>>>>> e91a96a63978650ca0613319dcf8458bfd8ce461
