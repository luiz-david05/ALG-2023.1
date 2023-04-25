from get_functions import *


def main():
    leitura_anterior = get_valid_number("valor  kWh da leitura anterior: ")
    leitura_atual = get_valid_number("valor kWh da leitura atual: ")

    # verificar valores das leituras
    if leitura_atual <= leitura_anterior:
        print("valor inválido, forneça um valor para a leitura atual maior que o valor da leitura anterior.")

        main()

    else:
        consumo = leitura_atual - leitura_anterior

        bandeira = consumo / 100 * 8

        # verificar faixas
        if consumo <= 30:
            tarifa = 0

        elif consumo > 30 and consumo <= 100:
            tarifa = consumo * 0.59

        elif consumo > 100:
            tarifa = consumo * 0.75

        # calculas impostos

        valor_tarifado = bandeira + tarifa

        icms = valor_tarifado * 0.25

        pis_confins = valor_tarifado * 0.15

        # verificar e calcular taxa de iluminação pública

        if consumo > 80:
            taxa_iluminacao_publica = valor_tarifado * 0.06

        else:
            taxa_iluminacao_publica = 0

        # valor total a pagar

        valor_total = icms + pis_confins + taxa_iluminacao_publica + valor_tarifado

        # exibir dados

        print(4 * "-", "talão de energia", "-" * 4)
        print(f"\nConsumo: {consumo} KWh")
        print(f"Valor Faturado: R$ {valor_tarifado:.2f}")
        print(f"Bandeira: R$ {bandeira:.2f}")
        print(f"ICMS: R$ {icms:.2f}")
        print(f"PIS/CONFINS: R$ {pis_confins:.2f}")
        print(f"Taxa de iluminação pública: R$ {taxa_iluminacao_publica:.2f}")
        print(f"Total a pagar: R$ {valor_total:.2f}")


if __name__ == "__main__":
    main()
