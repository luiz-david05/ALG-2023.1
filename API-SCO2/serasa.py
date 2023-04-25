from get_functions import *

# tempo de resolução: 20 minutos
def main():
    a = pegar_numero_na_faixa("a: ") / 100
    b = pegar_numero_na_faixa("b: ") / 100
    c = pegar_numero_na_faixa("c: ") / 100

    # verificar faixa
    score_1a = a * 260
    score_2a = a * 620

    score_1b = b * 570
    score_2b = b * 190

    score_1c = c * 170
    score_2c = c * 190

    # calcular score

    score_1 = score_1a + score_1b + score_1c
    score_2 = score_2a + score_2b + score_2c

    print(f"score = {score_1}")

    # verificar score 1.0

    if score_1 >= 800 and score_1 <= 1000:
        score_1_0 = "Muito bom"

    elif score_1 >= 600 and score_1 < 800:
        score_1_0 = "Bom"

    elif score_1 >= 400 and score_1 < 600:
        score_1_0 = "Regular"

    elif score_1 >= 0 and score_1 < 400:
        score_1_0 = "Baixo"

    # verificar score 2.0

    if score_2 > 700 and score_2 <= 1000:
        score_2_0 = "Muito bom"

    elif score_2 > 500 and score_2 <= 700:
        score_2_0 = "Bom"

    elif score_2 > 300 and score_2 <= 500:
        score_2_0 = "Regular"

    elif score_2 >= 0 and score_2 <= 300:
        score_2_0 = "Baixo"

    print(f"\nScore 1.0: {score_1} - {score_1_0}")
    print(f"Score 2.0: {score_2} - {score_2_0}")


def pegar_numero_na_faixa(texto):
    valor = get_valid_number(texto)

    if valor > 100:
        print("digite valores entre 0 e 100")

        valor = pegar_numero_na_faixa(texto)

    return valor


if __name__ == "__main__":
    main()