from get_functions import *


def main():
    peso_atual = get_valid_number("peso atual(kg): ")
    meta = get_valid_number("meta de redução de peso(%): ")
    semanas = get_valid_number(
        "Em quantas semanas você deseja alcançar essa meta: ")

    deficit = calcular_deficit_calorico(meta, peso_atual, semanas)

    print(
        f"\nPara alcançar sua meta de {meta}% em {semanas} semana(s)\nvocê precisa manter um déficit calórico diário médio de {deficit:.2f} kcal\n")

    kcal_diarias = get_valid_number(
        "Quantas kcal diárias você está disposto a consumir: ")

    qtd_exercicio = calcular_qtd_exexrcicio(deficit, kcal_diarias)

    print(
        f"\nIsso pode ser alcançado com {qtd_exercicio:.1f} horas de exercício por dia\nconsiderando sua ingestão calórica diária de {kcal_diarias:.2f} kcal.")


def calcular_deficit_calorico(meta, peso_atual, semanas):
    meta_kg = peso_atual * (meta / 100)
    deficit_calorico = (7700 * meta_kg) / (semanas * 7)

    return deficit_calorico


def calcular_qtd_exexrcicio(defict, kcal_diarias):
    return defict / kcal_diarias


main()
