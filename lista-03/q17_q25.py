from get_functions import *
import math


def q17():
    n = get_number("n: ")

    i = 1
    s = 0

    while i <= n:
        s += i / 1

        i += 1

    print(f"\n s = {s}")


def q18():
    n = get_number("n: ")

    i = 1
    s = 0

    while i < n + 1:
        s += i / (n - i + 1)

        i += 1

    print(f"\n s = {s}")


def q19():
    n = get_number("n: ")

    i = 1
    s = 0
    sinal = 1

    while i <= n:
        termo = (sinal * i) / (n - i + 1)
        s += termo
        sinal *= -1
        i += 1

    print(f"\n s = {s}")


def q20():
    n = get_number("n: ")

    i = 1
    s = 0
    sinal = 1

    while i <= n:
        s += (1 / i) * sinal
        sinal *= -1
        i += 1

    print(f"\n s = {s}")


def q21():
    i = 1
    s = 0
    j = 1

    while i <= 99:
        s += i / j

        i += 1
        j += 2

    print(f"\n s = {s}")


def q22():
    n = get_number("número de fichas: ")

    id = 0
    peso = 0
    i = 1
    id_maior = 0
    peso_maior = 0
    id_menor = 0
    peso_menor = math.inf

    while i <= n:
        id = get_number("id: ")
        peso = get_number("peso(kg): ")

        if peso > peso_maior:
            peso_maior = peso
            id_maior = id

        if peso < peso_menor:
            peso_menor = peso
            id_menor = id

        i += 1

    print(
        f"\nBoi mais gordo: ID {id_maior}, peso = {peso_maior} kg\nBoi mais magro: ID {id_menor}, peso = {peso_menor} kg")


def q23():
    qtd_funcionarios = get_number("Quantidade de funcionários: ")

    i = 1

    while i <= qtd_funcionarios:
        cod = get_number("código: ")
        hr_trabalhada = get_number("qtd hrs trabalhadas: ")
        qtd_dependentes = get_number("qtd de dependentes: ")

        valor_dependentes = 40 * qtd_dependentes
        salario_hr = hr_trabalhada * 12
        salario_bruto = valor_dependentes + salario_hr
        inss = salario_bruto * (8.5 / 100)
        ir = salario_bruto * (5 / 100)
        salario_liquido = salario_bruto - inss - ir

        print(f"codigo: {cod}")
        print(f"\nSalário Bruto: R$ ${salario_bruto:.2f}")
        print(f"(-) INSS (8,5%): R$ ${inss:.2f}")
        print("(-) IR(5%): R$ ${ir.toFixed(2)}")
        print(f"Salário Líquido: R$ ${salario_liquido:.2f}")
        print()

        i += 1


def q24():
    qtd_habitantes = get_valid_number("quantidade de habitantes: ")

    i = 1
    total_salario = 0
    total_filhos = 0

    # contador para as familias com salario  ate 1000 R$
    total_salario_1000 = 0

    while i <= qtd_habitantes:
        salario = get_valid_number("salario: ")
        qtd_filhos = get_valid_number("quantidade de filhos: ")

        print(f"proximo habitante  >>>>")
        print()

        if salario <= 1000:
            total_salario_1000 += salario

        total_filhos += qtd_filhos
        total_salario += salario

        i += 1

    media_salarial = total_salario / qtd_habitantes
    media_filhos = total_filhos / qtd_habitantes
    percentual_salario_1000 = total_salario_1000 / qtd_habitantes * 100

    print(f"\na) média de salário da população: R$ {media_salarial:.2f}")
    print(f"b) média de números de filhos: {media_filhos}")
    print(
        f"c) percentual de pessoas com salário de até R$ 1000: {percentual_salario_1000}%")


def q25():
    qtd_eleitores = get_valid_number("quantidade de eleitores: ")

    # iniciar contadores para armazenar os votos para cada candidato
    i = 1
    qtd_votos_1 = 0
    qtd_votos_2 = 0
    qtd_votos_3 = 0
    qtd_votos_nulos = 0
    qtd_votos_brancos = 0

    # definir numeros dos candidatos

    candidato1 = 1
    candidato2 = 2
    candidato3 = 3
    voto_nulo = 9
    voto_branco = 0

    while i <= qtd_eleitores:
        voto = pegar_voto_valido()

        # exibir mensagem apos pedir o voto

        if i < qtd_eleitores:
            print("bip\npróximo voto.")
        else:
            print("bip\nvotação encerrada.")

        # apurar votacao

        if voto == candidato1:
            qtd_votos_1 += 1
        elif voto == candidato2:
            qtd_votos_2 += 1
        elif voto == candidato3:
            qtd_votos_3 += 1
        elif voto == voto_nulo:
            qtd_votos_nulos += 1
        elif voto == voto_branco:
            qtd_votos_brancos += 1

        i += 1

    # averiguar quem recebeu mais votos

    recebeu_mais_votos = max(qtd_votos_1, qtd_votos_2, qtd_votos_3)

    empate = qtd_votos_1 == qtd_votos_2 and qtd_votos_2 == qtd_votos_3

    # apurar resultado da votacao

    if empate:
        resultado = "empate"
    elif recebeu_mais_votos == qtd_votos_1:
        resultado = "candidato 1 venceu"
    elif recebeu_mais_votos == qtd_votos_2:
        resultado = "candidato 2 venceu"
    elif recebeu_mais_votos == qtd_votos_3:
        resultado = "candidato 3 venceu"

    # exibir resultado

    print(f"\na) total de votos para cada candidato:")
    print(f"candidato 1 = {qtd_votos_1}")
    print(f"candidato 2 = {qtd_votos_2}")
    print(f"candidato 3 = {qtd_votos_3}")
    print(f"\nb) total de votos nulos: {qtd_votos_nulos}")
    print(f"\nc) total de votos em branco: {qtd_votos_brancos}")
    print(f"\nd) resultado da eleição: {resultado}")


def pegar_voto_valido(texto="voto: "):
    voto = get_valid_number(texto)
    opcoes_validas = [1, 2, 3, 0, 9]

    if voto not in opcoes_validas:
        print("Opção inválida\nOpções válidas: 1, 2, 3, 9, 0")

        voto = pegar_voto_valido(texto)

    return voto
