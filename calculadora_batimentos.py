from auxiliar_functions import *


def main():
    idade = get_int_number("idade em anos: ")

    fm = calcular_frequencia_cardiaca_maxima(idade)

    cinquenta_porcento, setenta_porcento, oitenta_e_cinco_porcento = calcular_faixas_de_batimento(
        fm)

    print(f"\nfrequência cardíca máxima: {fm}")
    print(
        f"\nfrequência cardíaca ideal para atividades físicas moderadas: entre {cinquenta_porcento:.1f} e {setenta_porcento:.1f}")
    print(
        f"\nfrequência cardíaca ideal para atividades físicas intensas: entre {setenta_porcento:.1f} e {oitenta_e_cinco_porcento:.1f}")


def calcular_faixas_de_batimento(fm):
    # calculando as faixas de batimento
    cinquenta_porcento = fm * (50 / 100)
    setenta_porcento = fm * (70 / 100)
    oitenta_e_cinco_porcento = fm * (85 / 100)

    return cinquenta_porcento, setenta_porcento, oitenta_e_cinco_porcento


def calcular_frequencia_cardiaca_maxima(idade):
    return 220 - idade


main()
