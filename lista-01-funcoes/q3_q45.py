 # múltiplos de 3 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45]

from auxiliar_functions import *
import math

def q3():
    min = get_int_number("minutos: ")

    hr, resto = minutos_para_horas_minutos(min)

    print(f"\n{min} minuto(s) = {hr} hora(s) e {resto} minuto(s)")


def minutos_para_horas_minutos(minutos):
    resto = minutos

    hr = resto // 60
    resto %= 60

    return hr, resto


def q6():
    vkm = get_float_number("velocidade km/h: ")

    vms = vkm_para_vms(vkm)

    print(f"\n{vkm} km/h = {vms:.2f} m/s")

  
def vkm_para_vms(vkm):
    return vkm / 3.6


def q9():
    a = get_int_number("A: ")
    b = get_int_number("B: ")

    print(numeros_na_ordem_inversa(a, b))


def numeros_na_ordem_inversa(a, b):
    return f"\nnúmeros na ordem inversa: [{b}, {a}]"


def q12():
    salario = get_float_number("sálario atual: ")

    aumento = calcular_percentual_de_aumento_25_porcento(salario)

    novo_salario = salario + aumento

    print(f"\naumento de 25%: R$ {aumento:.2f}\nsalário após reajuste: R$ {novo_salario:.2f}")



def calcular_percentual_de_aumento_25_porcento(salario):
    return salario * (25 / 100)


def q15():
    base = get_float_number("base: ")
    altura = get_float_number("altura: ")

    area = calcular_area_triangulo(base, altura)

    print(f"\nárea do triângulo = {area}")


def calcular_area_triangulo(base, altura):
    return (base * altura) / 2


def q18():
    raio = get_float_number("raio da circunferência: ")

    c = calcular_comprimento_da_circunferencia(raio)

    print(f"\ncomprimento da circunferência: {c:.2f}")


def calcular_comprimento_da_circunferencia(raio):
    return 2 * math.pi * raio


def q21():
    f = get_float_number("temperatura fahrenheit: ")

    c = fahrenheit_para_celsius(f)

    print(f"\n{f}° Grau Fahrenheit = {c}° Grau Celsius")


def fahrenheit_para_celsius(f):
    return (f - 32) * 5 / 9


def q24():
    m = get_int_number("metro: ")

    cm = m_para_cm(m)

    print(f"\n{m} metro(s) = {cm} centímetro(s)")


def m_para_cm(m):
    return m * 100


def q27():
    segundos = get_int_number("Digite um número inteiro de segundos: ")

    [horas, minutos, resto] = segundos_para_horas_minutos_segundos(segundos)

    print(f"\n{segundos} segundo(s) = {horas} hora(s), {minutos} minuto(s) e {resto} segundo(s)")

def segundos_para_horas_minutos_segundos(segundos):
    resto = segundos

    horas = resto // 3600
    resto %= 3600
    minutos = resto // 60
    resto %= 60

    return [horas, minutos, resto]


def q30():
    minutos = get_int_number("Digite um número inteiro de minutos: ")

    [dias, horas, resto] = minutos_para_dias_horas_minutos(minutos)

    print(f"\n{minutos} minuto(s) = {dias} dia(s), {horas} hora(s) e {resto} minuto(s)")

def minutos_para_dias_horas_minutos(minutos):
    resto = minutos

    dias = resto // 1440
    resto %= 1440
    horas = resto // 60
    resto %= 60

    return [dias, horas, resto]


def q33():
    n = get_int_number("Digite um número inteiro de 3 dígitos: ")

    inverso = numero_inverso(n)

    soma = n + inverso

    print(f"\nA soma de {n} + {inverso} = {soma}")


def numero_inverso(n):
    return int(str(n)[::-1])


def q36():
    ano = int(input("Digite o ano de nascimento (AAAA): "))
    mes = int(input("Digite o mês de nascimento (MM): "))
    dia = int(input("Digite o dia de nascimento (DD): "))

    idade_em_dias = calcular_idade_em_dias(ano, mes, dia)

    print(f"\nidade em dias = {idade_em_dias}")


def calcular_idade_em_dias(ano, mes, dia):
    # importando função date da biblioteca datetime 
    from datetime import date

    # calcula a diferença entre a data atual(função today) e a data de nascimento em dias,
    # usando o metódo days.
    data_nascimento = date(ano, mes, dia)
    dias_de_vida = (date.today() - data_nascimento).days

    return dias_de_vida


def q39():
    a = get_int_number("Digite um valor inteiro para A: ")
    b = get_int_number("Digite um valor inteiro para B: ")
    c = get_int_number("Digite um valor inteiro para C: ")

    r = calcular_valor_r(a, b)
    s = calcular_valor_s(b, c)
    d = calcular_expressao(r, s)

    print(f"\nD = {d}")


def calcular_valor_r(a, b):
    return (a + b) ** 2


def calcular_valor_s(b, c):
    return (b + c) ** 2


def calcular_expressao(r, s):
    return (r + s) // 2


def q42():
    x1 = get_float_number("Digite o valor do ponto x1: ")
    y1 = get_float_number("Digite o valor do ponto y1: ")
    x2 = get_float_number("Digite o valor do ponto x2: ")
    y2 = get_float_number("Digite o valor do ponto y2: ")

    distancia = calcular_distancia_entre_pontos(x1, y1, x2, y2)

    print(f"\ndistância = {distancia:.4f}")


def calcular_distancia_entre_pontos(x1, y1, x2, y2):
    return math.sqrt((x2 - x1 ) ** 2 + (y2 - y1) ** 2)


def q45():
    valor_saque = get_int_number("Digite um valor inteiro para o saque R$: ")

    [nota_100, nota_50, nota_20, nota_10, nota_5, nota_2, nota_1] = distribuir_notas(valor_saque)

    print(f"\n{nota_100} nota(s) de R$ 100")
    print(f"{nota_50} nota(s) de R$ 50")
    print(f"{nota_20} nota(s) de R$ 20")
    print(f"{nota_10} nota(s) de R$ 10")
    print(f"{nota_5} nota(s) de R$ 5")
    print(f"{nota_2} nota(s) de R$ 2")
    print(f"{nota_1} nota(s) de R$ 1")


def distribuir_notas(valor_saque):
    resto = valor_saque

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
    nota_2 = resto // 2
    resto %= 2
 
    return [nota_100, nota_50, nota_20, nota_10, nota_5, nota_2, resto]


q45()