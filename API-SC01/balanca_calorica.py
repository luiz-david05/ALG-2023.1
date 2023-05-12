from get_functions import *


def main():
    # receber dados
    nome = 'rock lee'
    sexo = pegar_sexo_valido()
    idade = 35
    peso = 84
    altura = 1.80
    perfil_atividade = 'moderada'
    af = verificar_af(sexo, perfil_atividade)
    necessecidade_calorica = calular_necessidade_diaria(sexo, idade, peso, altura, af)

    # necessidade calórica diária
    print(f"\n{nome}, sua necessidade calórica diária: {necessecidade_calorica:.1f}kcal")


def verificar_af(sexo, perfil_atividade):
    # sexo masculino
    # inicia o valor do af = perfil sedentário 
    af = 1
    if perfil_atividade == "pouco ativo":
        af = 1.11
    elif perfil_atividade == "ativo":
        af = 1.25
    elif perfil_atividade == "muito ativo":
        af = 1.48

    if sexo == "f":
        af = 1
        if perfil_atividade == "pouco ativo":
            af = 1.12
        elif perfil_atividade == "ativo":
            af = 1.27
        elif perfil_atividade == "muito ativo":
            af = 1.45

    return af


def calular_necessidade_diaria(sexo, idade, peso, altura, af):
    # sexo masculino
    necessidade_diaria = 662 - 9.53 * idade + af * 15.91 * peso + 539.6 * altura

    if sexo == 'f':
        necessidade_diaria = 354 - 6.91 * idade + af * 9.36 * peso + 726 * altura

    return necessidade_diaria


def pegar_sexo_valido(texto = "sexo: "):
    sexo = input(texto)

    if sexo != "f" and sexo != "m":
        print("sexo inválido, opções válidas: m - masculino e f - feminino")

        sexo = pegar_sexo_valido(texto)

    return sexo

if __name__ == "__main__":
    main()