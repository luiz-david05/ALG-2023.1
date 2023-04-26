from get_functions import *
import math


def main():
    # pedir dados   
    valor_veiculo = 13674
    prazo_pagamento = 48
    taxa_adm = 0.15
    lance_proposto = 5000

    renda_cliente = 1302
    # get_valid_number("informe sua renda mensal: ")

    # calcular valor taxa administração

    valor_taxa_adm = valor_veiculo * taxa_adm

    # calcular valor do financiamento

    valor_financiado = valor_veiculo + valor_taxa_adm

    # calcular valor das parcelas

    valor_parcela = valor_financiado / prazo_pagamento

    # calcular renda necessaria para resgate do bem

    renda_minima = renda_cliente / 0.30

    # mostrar dados da simulação

    print(f"\nvalor das parcelas: R$ {valor_parcela:.2f}")
    print(f"total a pagar: R$ {valor_financiado:.2f}")
    print(f"total da taxa de administração: R$ {valor_taxa_adm:.2f}")

    # verificar se a renda é suficiente para resgatar o bem

    if valor_parcela > renda_cliente * 0.30:
        print(f"sua renda não permite o resgate")
        print(f"renda miníma para realizar o resgate: R$ {renda_minima:.2f}")

    else:

        # manter prazo ou parcela

        reduzir = pegar_resposta_valida()

        # verificar escolha do cliente

        if reduzir == "prazo":
            novo_prazo = math.floor(prazo_pagamento - lance_proposto / valor_parcela)

            # corrigindo valor da ultima parcela

            novo_valor_parcela = valor_parcela


        else:
            novo_prazo = prazo_pagamento
            novo_valor_parcela = (valor_financiado - lance_proposto) / prazo_pagamento

        print(f"\nsua renda permite o resgate")
        print(f"novo valor das parcelas: R$ {novo_valor_parcela:.2f}")
        print(f"novo prazo: {novo_prazo} mês(es)")


        if novo_valor_parcela > renda_cliente * 0.30:
            print(f"renda mínima para realizar o resgate: R$ {renda_minima:.2f}")



def pegar_resposta_valida( texto ='reduzir "prazo" ou "parcela": '):
    resposta = input(texto)

    if resposta != "prazo" and resposta != "parcela":
        print('digite "prazo" ou "parcela"')
    
        resposta = pegar_resposta_valida(texto)

    return resposta


if __name__ == "__main__":
    main()