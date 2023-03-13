# Exercícios - ESTRUTURA SEQUENCIAL

from auxiliar_functions import *
import math

def q1():
    velocidade_ms = get_float_number("velocidade m/s: ")

    velocidade_km = velocidade_ms * 3.6

    print(f"\n{velocidade_ms} m/s = {velocidade_km:.1f} km/h")


def q2():
    hr, min = input("insira as horas e os minutos(ex: 10:30): ").split(':')

    total_mins = int(hr) * 60 + int(min)

    print(f"\n{hr}:{min} = {total_mins} minuto(s)")


def q3():
    min = get_int_number("minuto(s): ")

    hr = min // 60
    resto_min = min % 60

    print(f"\n{min} minuto(s) = {hr}:{resto_min}")


def q4():
    valor = get_float_number("valor em dólar: ")
    cotacao = get_float_number("cotação do dólar: ")

    valor_reais = valor * cotacao

    print(f"\n$ {valor:.2f} = R$ {valor_reais:.2f}")


def q5():
    n = input("número: ")

    c, d, u = n

    print(f"\n{c} + {d} + {u} = {int(c) + int(d) + int(u)}")


def q6():
    velocidade_km = get_float_number("velocidade km/h: ")

    velocidade_ms = velocidade_km / 3.6

    print(f"\n{velocidade_km} km/h = {velocidade_ms:.1f} m/s")


def q7():
    n1 = get_int_number("1° número: ")
    n2 = get_int_number("2° número: ")
    n3 = get_int_number("3° número: ")

    soma = n1 + n2
    diferenca = n2 - n3

    print(f"\na soma dos 2 primeiros = {soma}\na diferença entre os 2 últimos = {diferenca}")


def q8():
    n1 = get_int_number("1° número: ")
    n2 = get_int_number("2° número: ")

    soma = n1 + n2
    subtracao = n1 - n2

    divisao = soma / subtracao

    print(f"\na divisão da soma ({soma}) pela subtração ({subtracao}) = {divisao}")

def q9():
    a = get_int_number("1° número: ")
    b = get_int_number("2° número: ")

    print(f"\nnúmeros na ordem: ({a}, {b})\nnúmeros na ordem inversa: ({b}, {a})")


def q10():
    n1 = get_int_number("1° número: ")
    n2 = get_int_number("2° número: ")

    quociente = n1 / n2
    resto = n1 % n2

    print(f"\nquociente = {quociente}\nresto da divisão = {resto}")


def q11():
    n = input("número: ")

    invertido = n[::-1]

    print(f"\n{n} = {invertido}")


def q12():
    salario = get_float_number("salario: ")

    aumento = salario * (25 / 100)

    salario_pos_aumento = salario + aumento

    print(f"\nsalario pre-reajuste = R$ {salario:.2f}\nvalor do aumento (25%) = R$ {aumento:.2f}\nsalario pos-aumento = R$ {salario_pos_aumento:.2f}")


def q13():
    valor = get_float_number("valor em real: ")

    print(f"\nvalor = R$ {valor:.2f}\n70% = R$ {(valor * (70 / 100)):.2f}")


def q14():
    (n1, p1) = pedir_nota_peso("1° nota e peso: ")
    (n2, p2) = pedir_nota_peso("2° nota e peso: ")
    (n3, p3) = pedir_nota_peso("3° nota e peso: ")
    
    media_ponderada = ((n1 * p1) + (n2 * p2) + (n3 * p3)) / (p1 + p2 + p3)

    print(f"\nmedia = {media_ponderada:.1f}")

def pedir_nota_peso(texto):
    (n, p) = input(texto)

    return (float(n), float(p))


def q15():
    base = get_float_number("valor da base: ")
    altura = get_float_number("valor da altura: ")

    area = (base * altura) / 2

    print(f"\narea do triangulo = {area}")


def q16():
    lado = get_float_number("valor do lado: ")

    print(f"\narea do quadrado = {lado * lado}")


def q17():
    base = get_float_number("valor da base: ")
    altura = get_float_number("valor da altura: ")

    print(f"\narea do retângulo = {base * altura}")


def q18():
    raio = get_float_number("raio: ")

    comprimento = 2 * math.pi * raio

    print(f"\ncomprimento da circunferência = {comprimento:.2f}")


def q19():
    raio = get_float_number("raio: ")

    volume = (4 * math.pi * math.pow(raio, 3)) / 3

    print(f"\nvolume da esfera = {volume:.2f}")


def q20():
    temperatura_celsius = get_float_number("temperatura em graus celsius: ")

    temperatura_fahrenheit = temperatura_celsius * 1.8 + 32

    print(f"\n{temperatura_celsius}° Graus Celsius = {temperatura_fahrenheit:.1f}° Graus Fahrenheit")


def q21():
    temperatura_fahrenheit = get_float_number("temperatura em graus fahrenheit: ")

    temperatura_celsius = (temperatura_fahrenheit - 32) / 1.8

    print(f"\n {temperatura_fahrenheit:.1f}° Graus Fahrenheit = {temperatura_celsius:.1f}° Graus Celsius")


def q22():
    km = get_float_number("distancia(km): ")

    m = km * 1000

    print(f"\n{km} km = {m} m")


def q23():
    kg = get_float_number("peso(kg): ")

    g = kg * 1000

    print(f"\n{kg} kg = {g} g")

