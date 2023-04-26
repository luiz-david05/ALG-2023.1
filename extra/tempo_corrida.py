from get_functions import *


def main():
    distancia = get_valid_number("metros: ")
    velocidade = get_valid_number("velocidade(km/h): ")

    velocidade_metros_por_minuto = converter_velocidade_para_metros_por_minutos(
        velocidade)

    tempo = calcular_tempo_prova(distancia, velocidade_metros_por_minuto)

    tempo_prova_minutos = converter_para_minutos(tempo)

    print(f"\ntempo de prova: {tempo_prova_minutos:.1f} minuto(s)")


def converter_velocidade_para_metros_por_minutos(velocidade):
    return (velocidade * 1000) / 60


def calcular_tempo_prova(distancia, velocidade):
    return (distancia / (velocidade * 1000)) * 60


def converter_para_minutos(tempo):
    return tempo * 60


main()
