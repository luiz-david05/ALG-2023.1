from auxiliar_functions import *

import math


def q24():
    m = get_float_number("m: ")

    cm = m * 100

    print(f"\n{m} m = {cm} cm")


def q25():
    m = get_int_number("m: ")

    km = m // 1000
    resto = m % 1000

    print(f"\n{m} m = {km} km e {resto} m")


def q26():
    dias = get_int_number("dias: ")

    semanas = dias // 7
    resto = dias % 7

    print(f"\n{dias} dia(s) = {semanas} semana(s) e {resto} dia(s)")


def q27():
    segundos = get_int_number("segundos: ")

    resto = segundos

    hr = segundos // 3600
    resto %= 3600
    min = resto // 60
    resto %= 60

    print(
        f"\n{segundos} segundo(s) = {hr} hora(s) :{min} minuto(s) :{resto} minuto(s)")


def q28():
    hr = get_int_number("hr: ")

    resto = hr
    semanas = hr // 168
    resto %= 168
    dias = resto // 24
    resto %= 24

    print(f"\n{hr} hora(s) = {semanas} semana(s), {dias} dia(s) e {resto} hora(s)")


def q29():
    meses = get_int_number("meses: ")

    resto = meses
    anos = meses // 12
    resto %= 12

    print(f"\n{meses} mes(es) = {anos} ano(s) e {resto} mes(es)")


def q30():
    minutos = get_int_number("minutos: ")

    resto = minutos
    dias = minutos // (144 * 10)
    resto %= (144 * 10)
    hr = resto // 60
    resto %= 60

    print(f"\n{minutos} minuto(s) = {dias} dia(s), {hr} hora(s) e {resto} minuto(s)")


def q31():
    numero_binario = input("numero binario: ")

    b1, b2, b3, b4 = numero_binario

    numero_decimal = int(b1) * 2 ** 3 + int(b2) * 2 ** 2 + \
        int(b3) * 2 ** 1 + int(b4) * 2 ** 0

    print(f"\n{numero_binario} = {numero_decimal}")


def q32():
    n = get_int_number("numero: ")

    c, d, u = str(n)
    inverso = u + d + c
    diferenca = n - int(inverso)

    print(f"\n{n} - {inverso} = {diferenca}")


def q33():
    n = get_int_number("numero: ")

    c, d, u = str(n)
    inverso = u + d + c
    soma = n + int(inverso)

    print(f"\n{n} + {inverso} = {soma}")


def q34():
    n1 = get_float_number("1° número: ")
    n2 = get_float_number("2° número: ")
    n3 = get_float_number("3° número: ")

    media = (n1 + n2 + n3) / 3

    print(f"\nmedia = {media:.1f}")


def q35():
    n = get_int_number("numero: ")

    m, c, d, u = str(n)

    soma_elementos = int(m) + int(c) + int(d) + int(u)

    print(
        f"\nnumero = {n}\nsoma dos elementos: {m} + {c} + {d} + {u} = {soma_elementos}")


def q36():
    anos = get_int_number("anos: ")
    meses = get_int_number("meses: ")
    dias = get_int_number("dias: ")

    idade = anos * 365 + meses * 30 + dias

    print(f"\n{anos} ano(s), {meses} mes(es) e {dias} dia(s) = {idade} dia(s)")


def q37():
    dias = get_int_number("dias: ")

    resto = dias
    anos = resto // 365
    resto %= 365
    meses = resto // 30
    resto %= 30

    print(f"\n{dias} dia(s) = {anos:} ano(s), {meses} mes(es) e {resto} dia(s)")


def q38():
    numerador_1, denominador_1 = input("1° fração (ex: 1/3): ").split("/")
    numerador_2, denominador_2 = input("2° fração: ").split("/")

    print(f"\n{numerador_1}/{denominador_1} + {numerador_2}/{denominador_2} = {int(numerador_1) + int(numerador_2)}/{denominador_1}")


q38()

def q39():
    a = get_int_number("A: ")
    b = get_int_number("B: ")
    c = get_int_number("C: ")

    expressao_r = (a + b) ** 2
    expressao_s = (b + c) ** 2
    expressao_d = (expressao_r + expressao_s) // 2

    print(f"\nD = R + S / 2\nD = {expressao_r} + {expressao_s} / 2 = {expressao_d}")


def q40():
   anos = get_int_number("números de anos fumando: ")
   cigarros = get_int_number("estimativa de cigarros fumados por dia: ")
   valor_carteira = get_float_number("valor da carteira de cigarro R$: ")

   idade_dias = anos * 365
   qtd_cigarros = cigarros * idade_dias
   qtd_carteiras = qtd_cigarros // 20
   valor_total = qtd_carteiras * valor_carteira

   print(f"\nvalor gasto em cigarro, durante o período de {anos} ano(s) = R$ {valor_total:.2f}")


def q41():
    custo_fabrica = get_float_number("custo de fabricação do carro: ")

    taxa_distrubuidor = custo_fabrica * (28 / 100)
    imposto = custo_fabrica * (45 / 100)
    custo_consumidor = taxa_distrubuidor + imposto + custo_fabrica

    print(f"\ntaxa distribuidor (28%)= R$ {taxa_distrubuidor:.2f}\nimposto (45%)= R$ {imposto:.2f}\ncusto final ao consumidor = R$ {custo_consumidor:.2f}")


def q42():
    x1 = get_int_number("ponto x1: ")
    y1 = get_int_number("ponto y1: ")
    x2 = get_int_number("ponto x2: ")
    y2 = get_int_number("ponto y2: ")

    distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    print(f"\ndistância = {distancia}")


def q43():
    a = get_int_number("a: ")
    b = get_int_number("b: ")
    c = get_int_number("c: ")
    d = get_int_number("d: ")
    e = get_int_number("e: ")
    f = get_int_number("f: ")

    x = (c * e - b * f) / (a * e - b * d)
    y = (a * f - c * d) / (a * e - b * d)

    print(f"\nx = {x}\ny = {y}")


def q44():
    latao = get_int_number("quantidade latão: ")

    cobre = latao * (70 / 100)
    zinco = latao * (30 / 100)

    print(f"\n{latao}kg de latão\n70% cobre = {cobre}kg\n30% zinco = {zinco}kg ")


def q45():
    valor = get_int_number("valor para saque: ")

    resto = valor
    nota_100 = resto // 100
    resto %= 100
    nota_50 = resto // 50
    resto %= 50
    nota_20 = resto // 20
    resto %= 20
    nota_10 = resto // 10
    resto %= 10
    nota_5 = resto // 5
    resto %= 5

    print(f"\nvalor: R$ {valor:.2f}")
    print(f"{nota_100} nota(s) R$ 100")
    print(f"{nota_50} nota(s) R$ 50")
    print(f"{nota_20} nota(s) R$ 20")
    print(f"{nota_10} nota(s) R$ 10")
    print(f"{nota_5} nota(s) R$ 5")
    print(f"{resto} nota(s) R$ 1")


def q46():
    valor = get_int_number("valor do produto: ")

    resto = valor % 3
    entrada = valor // 3 + resto
    prestacao = valor // 3

    print(f"\nvalor = R$ {valor:.2f}\nentrada = R$ {entrada:.2f}\nprestações = R$ {prestacao:.2f}")

