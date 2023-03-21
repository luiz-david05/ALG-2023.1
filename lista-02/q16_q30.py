from auxiliar_functions import *


def q16():
    nota_1 = get_float_number("1° nota: ")
    nota_2 = get_float_number("2° nota: ")

    media = calcular_media_duas_notas(nota_1, nota_2)

    print(f"\nmédia = {media:.1f}")

    if media >= 7:
        print(f"\nresultado: aprovado")

    elif media < 7 and media >= 4:
        print(f"\nresultado: em exame final")

        nota_exame = get_float_number("nota exame final: ")

        media_exame = calcular_media_duas_notas(media, nota_exame)

        print(f"\nmédia exame final: {media_exame:.1f}")

        if nota_exame >= 5:
            print(f"\nresultado exame final: aprovado")

        else:
            print(f"\nresultado exame final: reprovado")

    elif media < 4:
        print(f"\nresultado: reprovado")


def calcular_media_duas_notas(n1, n2):
    return (n1 + n2) / 2


def q17():
    n1 = get_int_number("1° número: ")
    n2 = get_int_number("2° número: ")

    resto = n1 % n2

    soma = n1 + n2

    print(f"\nresto = {resto}")

    if resto == 1:
        soma_resto = n1 + n2 + resto

        print(f"\nsoma de {n1} + {n2} + {resto} = {soma_resto}")

    elif resto == 2:
        pares = []
        impares = []

        if numero_par(n1):
            pares.append(n1)

        else:
            impares.append(n1)

        if numero_par(n2):
            pares.append(n2)

        else:
            impares.append(n2)

        print(f"\npares: {pares}\nimpares: {impares}")

    elif resto == 3:

        mulplicacao_soma = soma * n1

        print(
            f"\nmultiplicação da soma {soma} pelo 1° número lido {n1} = {mulplicacao_soma}")

    elif resto == 4:
        if n2 != 0:
            divisao_soma = soma / n2

            print(
                f"\ndivisão da soma {soma} pelo 2° número {n2} = {divisao_soma}")

        else:
            print(f"\ndivisão impossível")

    else:
        n1_quadrado = numero_ao_quadrado(n1)
        n2_quadrado = numero_ao_quadrado(n2)

        print(
            f"\n1° número ao quadrado: {n1_quadrado}\n2° número ao quadrado: {n2_quadrado}")


def q18():
    n1 = get_int_number("1° número: ")
    n2 = get_int_number("2° número: ")

    print("\n1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão")

    opcao = get_int_number("opção: ")

    if opcao == 1:
        soma = somar_dois_numeros(n1, n2)

        print(f"\nsoma = {soma}")

    elif opcao == 2:
        subtracao = subtrair_dois_numeros(n1, n2)

        print(f"\nsubtração = {subtracao}")

    elif opcao == 3:
        multiplicao = multiplicar_dois_numeros(n1, n2)

        print(f"\nmultiplicação = {multiplicao}")

    elif opcao == 4:
        if n2 != 0:
            divisao = dividir_dois_numeros(n1, n2)

            print(f"\ndivisão = {divisao}")

        else:
            print(f"\ndivisão impossível")


def somar_dois_numeros(n1, n2):
    return n1 + n2


def subtrair_dois_numeros(n1, n2):
    return n1 - n2


def dividir_dois_numeros(n1, n2):
    return n1 / n2


def multiplicar_dois_numeros(n1, n2):
    return n1 * n2


def q19():
    altura = get_float_number("altura(m): ")
    peso = get_float_number("peso(kg): ")

    imc = calcular_imc(peso, altura)

    print(f"\nimc = {imc:.1f}")

    if imc < 25:
        print(f"\nimc abaixo de 25: peso normal")

    elif 25 <= imc <= 30:
        print(f"\nimc entre 25 e 30: obeso")

    elif imc > 30:
        print(f"\nimc acima de 30: obesidade mórbida")


def calcular_imc(peso, altura):
    return peso / altura ** 2


def q20():
    angulo = get_int_number("medida do ângulo(entre 0° e 360°): ")

    if 0 < angulo <= 90:
        print(f"\nprimeiro quadrante entre 0° e 90°")

    elif 90 < angulo <= 180:
        print(f"\nsegundo quadrante entre 90° e 180°")

    elif 180 < angulo <= 270:
        print(f"\nterceiro quadrante entre 180° e 270°")

    elif 270 < angulo <= 360:
        print(f"\nquarto quadrante entre 270° e 360°")

    else:
        print(f"\nângulo inválido")


def q21():
    n = get_float_number("número: ")

    [parte_real, parte_fracionaria] = str(n).split('.')

    parte_real = int(parte_real)
    parte_fracionaria = int(parte_fracionaria)

    if parte_fracionaria >= 5:
        parte_real += 1

    print(
        f"\narredondamento de números utilizando a regra usual da matemática\nnúmero arredondado: {parte_real}")


def q22():
    inicio_jogo = input("Tempo inicial do jogo (hh:mm): ").split(":")
    fim_jogo = input("Tempo final do jogo: ").split(":")

    [hr_inicial, min_inicial] = list(map(int, inicio_jogo))
    [hr_final, min_final] = list(map(int, fim_jogo))

    [duracao_hr, duracao_min] = calcular_duracao_jogo(
        hr_inicial, min_inicial, hr_final, min_final)

    if hr_inicial == hr_final and min_final > min_inicial:
        print(f"\nO tempo do jogo excedeu as 24 horas")

    else:
        print(
            f"\nO jogo durou: {duracao_hr} hora(s) e {duracao_min} minuto(s)")


def calcular_duracao_jogo(hr_inicial, min_inicial, hr_final, min_final):
    duracao_hr = hr_final - hr_inicial
    duracao_min = min_final - min_inicial

    if duracao_hr < 0:
        duracao_hr += 24

    if duracao_min < 0:
        duracao_min += 60
        duracao_hr -= 1

    if duracao_hr == 0 == duracao_min:
        duracao_hr = 24

    return [duracao_hr, duracao_min]


def q23():
    data_1 = input("1° data(dd/mm/aaaa): ")
    data_2 = input("2° data(dd/mm/aaaa): ")

    primeira_data = data_1.split("/")
    segunda_data = data_2.split("/")

    [dia_1, mes_1, ano_1] = list(map(int, primeira_data))
    [dia_2, mes_2, ano_2] = list(map(int, segunda_data))

    if ano_1 > ano_2:
        print(f"\n{data_1} é a data mais recente")

    elif ano_2 > ano_1:
        print(f"\n{data_2} é a data mais recente")

    elif ano_1 == ano_2:
        if mes_1 > mes_2:
            print(f"\n{data_1} é a data mais recente")

        elif mes_2 > mes_1:
            print(f"\n{data_2} é a data mais recente")

        elif mes_1 == mes_2:
            if dia_1 > dia_2:
                print(f"\n{data_1} é a data mais recente")

            elif dia_2 > dia_1:
                print(f"\n{data_2} é a data mais recente")


def q24():
    a = get_coeficient_a("Valor de A: ")
    b = get_int_number("Valor de B: ")
    c = get_int_number("Valor de C: ")

    if b == 0 and c != 0:
        print(f"\nEquação incompleta")

    elif b != 0 and c == 0:
        print(f"\nEquação incompleta")

    else:
        print(f"\nEquação completa")

    [x1, x2] = calcular_raizes_segundo_grau(a, b, c)

    if isinstance(x1, complex) or isinstance(x2, complex):
        print("A equação do 2° grau não possui raízes reais.")

    else:
        print(f"\nx1 = {x1}\nx2 = {x2}")


def calcular_delta(a, b, c):
    return b ** 2 - (4 * a * c)


def calcular_raizes_segundo_grau(a, b, c):
    if b == 0 and c != 0:
        # isolar incógnita x

        x1 = ((- c) / a) ** 0.5
        x2 = - x1

    elif b != 0 and c == 0:
        x1 = 0
        x2 = (- b) / a

    else:
        delta = calcular_delta(a, b, c)

        x1 = (- b + delta ** 0.5) / (2 * a)
        x2 = ((- b) - delta ** 0.5) / (2 * a)

    return [x1, x2]


def get_coeficient_a(texto):
    a = int(input(texto))

    if a == 0:
        print("O valor de A deve ser diferente de 0")

        a = get_coeficient_a(texto)

    return a


def q25():
    usuario = input("usuário: ")
    get_password("senha: ")

    print(f"\nAcesso permitido\nBem-vindo(a) {usuario}")


def get_password(texto):
    senha = get_int_number(texto)

    if senha != 1234:
        print(f"Acesso negado")

        senha = get_password(texto)

    return senha


def q26():
    a = get_int_number("1° lado: ")
    b = get_int_number("2° lado: ")
    c = get_int_number("3° lado: ")

    [hipotenusa, cateto_1,
        cateto_2] = identificar_hipotenusa_e_catetos(a, b, c)

    print(f"\nhipotenusa = {hipotenusa}\ncatetos = {cateto_1} e {cateto_2}")


def identificar_hipotenusa_e_catetos(a, b, c):
    hipotenusa = max(a, b, c)

    if hipotenusa == a:
        cateto_1 = b
        cateto_2 = c

    elif hipotenusa == b:
        cateto_1 = a
        cateto_2 = c

    elif hipotenusa == c:
        cateto_1 = a
        cateto_2 = b

    return [hipotenusa, cateto_1, cateto_2]


def q27():
    data_nascimento = input("data de nascimento (dd/mm/aaaa): ").split("/")
    data_atual = input("data atual (dd/mm/aaaa): ").split("/")

    [dia_nasc, mes_nasc, ano_nasc] = list(map(int, data_nascimento))
    [dia_atual, mes_atual, ano_atual] = list(map(int, data_atual))

    [idade_anos, idade_meses, idade_dias] = calcular_idade_anos_meses_dias(
        dia_nasc, mes_nasc, ano_nasc, dia_atual, mes_atual, ano_atual)

    print(
        f"\nA idade é {idade_anos} ano(s), {idade_meses} mes(es) e {idade_dias} dia(s)")


def calcular_idade_anos_meses_dias(dia_nasc, mes_nasc, ano_nasc, dia_atual, mes_atual, ano_atual):
    from datetime import date

    idade_anos = ano_atual - ano_nasc
    idade_meses = mes_atual - mes_nasc
    idade_dias = dia_atual - dia_nasc

    if mes_atual < mes_nasc or (mes_atual == mes_nasc and dia_atual < dia_nasc):
        idade_anos -= 1

    if idade_dias < 0:
        mes_anterior = mes_atual - 1 if mes_atual > 1 else 12
        dias_mes_anterior = (date(ano_atual, mes_atual, 1)) - \
            date(ano_atual, mes_anterior, 1).days
        idade_dias += dias_mes_anterior
        idade_meses -= 1

    if idade_meses < 0:
        idade_meses += 12
        idade_anos -= 1

    return [idade_anos, idade_meses, idade_dias]


def q28():
    ponto_a = input(
        "Digite as coordenadas do primeiro ponto (x1, y1): ").split(" ")
    ponto_b = input(
        "Digite as coordenadas do segundo ponto (x2, y2): ").split(" ")

    [x1, y1] = list(map(int, ponto_a))
    [x2, y2] = list(map(int, ponto_b))

    area = calcular_area_retangulo(x1, y1, x2, y2)

    if area < 0:
        print(f"O valor da área não pode ser negativo.")

    else:
        print(f"\nÁrea do retângulo = {area:.3f}")


def calcular_area_retangulo(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def q29():
    n = get_int_number_four_digits("número: ")

    msg = quadrado_perfeito(n)

    print(msg)


def get_int_number_four_digits(texto):
    n = input(texto)

    if len(n) != 4:
        print("digite um número de quatro dígitos")

        n = get_int_number_four_digits(texto)

    return n


def dividir_numero_duas_dezenas(n):
    [m, c, d, u] = n
    mc = m + c
    du = d + u
    mc = int(mc)
    du = int(du)

    return [mc, du]


def quadrado_perfeito(n):
    [mc, du] = dividir_numero_duas_dezenas(n)
    soma_elementos = mc + du
    n = int(n)
    raiz_quadrada_n = round(n ** 0.5)

    if soma_elementos == raiz_quadrada_n:
        msg = f"\nraiz quadrada de {n} = {raiz_quadrada_n}\nsoma dos elementos = {mc} + {du} = {soma_elementos}\no número {n} é um quadrado perfeito"

    else:
        msg = f"\nraiz quadrada de {n} = {raiz_quadrada_n}\nsoma dos elementos = {mc} + {du} = {soma_elementos}\no número {n} não é um quadrado perfeito"

    return msg


def q30():
    n = get_int_number_four_digits("número: ")

    msg = verificar_caracteristica(n)

    print(msg)


def verificar_caracteristica(n):
    [mc, du] = dividir_numero_duas_dezenas(n)

    soma = mc + du

    soma_ao_quadrado = soma ** 2
    n = int(n)

    if n == soma_ao_quadrado:
        msg = f"\nnúmero: {n}\ndividindo = {mc} e {du}\nsomando = {soma}\nnúmero apresenta a característica: {soma}² = {n}"

    else:
        msg = f"\nnúmero: {n}\ndividindo = {mc} e {du}\nsomando = {soma}\nnúmero não apresenta a característica: {soma}² != {n}"

    return msg
