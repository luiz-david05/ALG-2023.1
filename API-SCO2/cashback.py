from get_functions import *
import math

# tempo de resolução: 1 hora e 5 minutos

def main():
    numero_de_clientes = get_valid_number("Número de clientes: ")

    total_faturamento = 0
    qtd_compras = 0
    total_gasto_cashback = 0
    maior_valor_cashback = 0
    menor_valor_cashback = math.inf
    cliente_maior_cashback = ""
    cliente_menor_cashback = ""


    while numero_de_clientes != 0:
        nome_cliente = input("nome do cliente: ")
        valor_compra_cliente = get_valid_number("valor da compra: ")
        print(f"próximo cliente >>>")
        print()

        if valor_compra_cliente <= 250:
            valor_cashback = valor_compra_cliente * 0.05

        elif valor_compra_cliente > 250 and valor_compra_cliente <= 500:
            valor_cashback = valor_compra_cliente * 0.07

        elif valor_compra_cliente > 500 and valor_compra_cliente <= 750:
            valor_cashback = valor_compra_cliente * 0.08

        else:
            valor_cashback = (valor_compra_cliente - 750) * 0.25 + 250 * 0.05 + 250 * 0.07 + 250 * 0.08
        
        # verificar menor e maior cashback
        if valor_cashback > maior_valor_cashback:
            maior_valor_cashback = valor_cashback
            cliente_maior_cashback = nome_cliente

        if valor_cashback < menor_valor_cashback:
            menor_valor_cashback = valor_cashback
            cliente_menor_cashback = nome_cliente

        qtd_compras += 1
        total_faturamento += valor_compra_cliente
        total_gasto_cashback += valor_cashback
        numero_de_clientes -=1

    percentual_investido_cashback = (total_gasto_cashback / total_faturamento) * 100
    valor_medio_cashback = total_gasto_cashback / qtd_compras

    print(f"\nFaturamento total: R$ {total_faturamento:.2f}")
    print(f"Valor total distribuído em cashback: R$ {total_gasto_cashback:.2f}")
    print(f"Percentual do valor total distribuído em cashbak(baseado no faturamento total): {percentual_investido_cashback}%")
    print(f"Maior valor cashback: R$ {maior_valor_cashback:.2f}")
    print(f"Nome do cliente: {cliente_maior_cashback}")
    print(f"Menor valor cashback: R$ {menor_valor_cashback:.2f}")
    print(f"Nome do cliente: {cliente_menor_cashback}")
    print(f"Valor médio cashback: R$ {valor_medio_cashback:.2f}")


if __name__ == "__main__":
    main()