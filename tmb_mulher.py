# A taxa de metabolismo basal (TMB) indica a quantidade de calorias que o corpo necessita para realizar funções metabólicas básicas.

from auxiliar_functions import *


def main():
    print("calcular taxa metabólica basal (TMB) para o gênero feminino")
    peso = get_float_number("peso(kg): ")
    altura = get_int_number("altura(cm): ")
    idade = get_int_number("idade em anos: ")

    tmb = calcular_tmb_mulher(peso, altura, idade)

    print(f"\ntmb = {(tmb)}")


def calcular_tmb_mulher(peso, altura, idade):
    return round(447.6 + 9.2 * peso + 3.1 * altura - 4.3 * idade)


main()