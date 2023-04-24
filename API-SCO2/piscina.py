from get_functions import *
import math

# tempo de resolução: 45 minutos

def main():
    largura = get_valid_number("Largura em cm: ")
    comprimento = get_valid_number("Comprimento em cm: ")
    profundidade = get_valid_number("Profundidade em cm: ")

    capacidade_maxima = largura * comprimento * profundidade / 1000

    capacidade_recomendada = capacidade_maxima * 0.85

    print(f"\nRecomenda-se encher até 85% da capacidade máxima da piscina ({capacidade_maxima} litros), ou seja: {capacidade_recomendada} litros.")

    print()
    valor_agua = get_valid_number("valor de 1000 litros de água na sua cidade: ")

    gasto_piscina = math.ceil(capacidade_recomendada / 1000) * valor_agua

    print(f"Para encher a piscina conforme a capacidade recomendada, você gastará: R$ {gasto_piscina:.2f}")

    qtd_repo = capacidade_recomendada * 0.10
    gasto_mensal = gasto_piscina * 0.10

    print(f"\nSeu gasto mensal para repor 10% da piscina com água ({qtd_repo} litros) será de: R$ {gasto_mensal:.2f}")


if __name__ == "__main__":
    main()




