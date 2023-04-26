#  O Índice de Adiposidade Corporal, mais conhecido como IAC, é um método utilizado para medir a gordura corporal.

from get_functions import *
import math


def main():
    tamanho_quadril = get_valid_number("tamanho do quadril(cm): ")
    altura = get_valid_number("altura(m): ")

    iac = calcular_iac(tamanho_quadril, altura)

    tamanho_minimo_quadril = calcular_tamanho_minimo_quadril(altura)

    tamanho_maximo_quadril = calcular_tamanho_maximo_quadril(altura)

    print(f"\nentre 0 e 8.9 = abaixo do peso")
    print(f"entre 9 e 20.9 = normal")
    print(f"entre 21 e 25.9 = sobrepeso")
    print(f"entre 26 e 29.9 = obesidade grau 1")
    print(f"\nseu IAC é de = {iac:.2f}")
    print(f"\ncircunferencia minima do quadril para estar na faixa normal: {tamanho_minimo_quadril:.2f}")
    print(f"\ncircunferencia maxima do quadril para estar na faixa normal: {tamanho_maximo_quadril:.2f}")


def calcular_iac(quadril, altura):
    return (quadril / (altura * math.sqrt(altura))) - 18


def calcular_tamanho_minimo_quadril(altura):
    return 27 * (altura * math.sqrt(altura))


def calcular_tamanho_maximo_quadril(altura):
    return 38.19 * (altura * math.sqrt(altura))


main()
