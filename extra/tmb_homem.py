# A taxa de metabolismo basal (TMB) indica a quantidade de calorias que o corpo necessita para realizar funções metabólicas básicas.

from get_functions import *
import math


def main():
    print("calcular taxa metabólica basal (TMB) para o gênero masculino")
    peso = get_valid_number("peso(kg): ")
    altura = get_valid_number("altura(cm): ")
    idade = get_valid_number("idade em anos: ")

    tmb = calcular_tmb_homem(peso, altura, idade)

    print(f"\ntmb = {tmb}")


def calcular_tmb_homem(peso, altura, idade):
    return round(88.36 + 13.4 * peso + 4.8 * altura - 5.7 * idade)


main()
