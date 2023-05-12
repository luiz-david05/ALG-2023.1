from get_functions import *


def main():
    valor_veiculo = 89000
    percentual_valor_veiculo = get_valid_number("percentual da fipe pelo qual ira vender o argo %: ") / 100
    valor_novo_veiculo = 185000
    parcelas = pegar_qtd_parcelas_validas()
    juros = pegar_taxa_juros_valida()
    administracao = pegar_taxa_adm_valida()

    # consorcio
    entrada = valor_veiculo * percentual_valor_veiculo
    valor_parcelado = valor_novo_veiculo + (valor_novo_veiculo * administracao)
    juros_totais = valor_novo_veiculo * administracao
    valor_total = valor_parcelado - entrada
    valor_parcelas = valor_total / parcelas
    total_a_pagar = valor_parcelado + entrada

    print("\n", 4 * "-", "consórcio", 4 * "-")
    print(f"\nvalor do veículo a ser comprado: R$ {valor_novo_veiculo:.2f}")
    print(f"valor a ser parcelado: R$ {valor_parcelado:.2f}")
    print(f"juros totais: R$ {juros_totais:.2f}")
    print(f"parcelamento: {parcelas} prestações de R$ {valor_parcelas:.2f}")
    print(f"total a pagar (entrada + prestações): R$ {total_a_pagar:.2f}")


    # cdc 
    juros_mensal = valor_novo_veiculo * juros
    juros_totais = juros_mensal * parcelas
    valor_parcelado = valor_novo_veiculo + juros_totais
    valor_total = valor_parcelado - entrada
    valor_parcelas = valor_total / parcelas
    total_a_pagar_cdc = valor_parcelado + entrada


    print("\n", 4 * "-", "cdc", 4 * "-")
    print(f"\nvalor do veículo a ser comprado: R$ {valor_novo_veiculo:.2f}")
    print(f"valor a ser parcelado: R$ {valor_parcelado:.2f}")
    print(f"juros totais: R$ {juros_totais:.2f}")
    print(f"parcelamento: {parcelas} prestações de R$ {valor_parcelas:.2f}")
    print(f"total a pagar (entrada + prestações): R$ {total_a_pagar_cdc:.2f}")

    if total_a_pagar < total_a_pagar_cdc:
        print(f"\nmodalidade mais vantajosa: consórcio")
    else:
        print(f"\nmodalidade mais vantajosa: cdc")


def pegar_qtd_parcelas_validas(texto = "quantidade de parcelas: "):
    qtd = get_valid_number(texto)
    opcoes = [36, 48, 60]

    if qtd not in opcoes:
        print("quantidade de parcelas válidas: 36, 48 ou 60")

        qtd = pegar_qtd_parcelas_validas(texto)
    
    return qtd


def pegar_taxa_juros_valida(texto = "taxa de juros cdc: "):
    taxa = get_valid_number(texto)
    
    if taxa < 1.2 or taxa > 2.5:
        print("taxa de juros válida: entre 1.2 e 2.5%")

        taxa = pegar_taxa_juros_valida(texto)
    
    return taxa / 100


def pegar_taxa_adm_valida(texto = "taxa de administração: "):
    taxa = get_valid_number(texto)

    if taxa < 10 or taxa > 20:
        print("taxa de administração válida: entre 10 e 20%")

        taxa = pegar_taxa_adm_valida(texto)

    return taxa / 100


if __name__ == "__main__":
    main()