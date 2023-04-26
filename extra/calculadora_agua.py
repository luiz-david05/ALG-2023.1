from get_functions import *


def main():
    peso = get_valid_number("peso: ")

    qtd_agua_moderada = calcular_qtd_agua(peso, 35)

    # convertendo a quantidade de ml em litros
    qtd_litros_agua = converter_ml_para_litro(qtd_agua_moderada)

    print(
        f"\nquantidade recomendada de água atividade moderada: {qtd_litros_agua:.1f} litro(s) ")

    qtd_agua_intensa = calcular_qtd_agua(peso, 45)

    qtd_litros_agua = converter_ml_para_litro(qtd_agua_intensa)

    print(
        f"\nquantidade recomendada de água atividade intensa: {qtd_litros_agua:.1f} litro(s) ")


def calcular_qtd_agua(peso, ml):
    # arredondando o peso para ignorar a parte fracionaria do peso (se tiver)
    return ml * int(peso)


def converter_ml_para_litro(n):
    return n / 1000


main()
