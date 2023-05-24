from function_utils import pegar_numero_positivo
from vetores_utils import *


def q1():
    tamanho = pegar_numero_positivo("Digite o tamanho do vetor: ")
    vetor_a = criar_vetor(tamanho)
    vetor_b = inverter_vetor(vetor_a)

    print("\nVetor A:")
    mostrar_vetor(vetor_a)
    print("\nVetor B:")
    mostrar_vetor(vetor_b)


def q2():
    tamanho_a = pegar_numero_positivo("Digite o tamanho do vetor A: ")
    vetor_a = criar_vetor(tamanho_a)
    tamanho_b = pegar_numero_positivo("Digite o tamanho do vetor B: ")
    vetor_b = criar_vetor(tamanho_b)

    vetor_elementos_iguais = elementos_iguais_nos_vetores(vetor_a, vetor_b)

    print("\nVetor A:")
    mostrar_vetor(vetor_a)
    print("\nVetor B:")
    mostrar_vetor(vetor_b)
    print("\nElementos iguais:")
    mostrar_vetor(vetor_elementos_iguais)
    print(f"\nQuantidade de elementos iguais: {len(vetor_elementos_iguais)}")


def q3():
    tamanho_a = pegar_numero_positivo("Digite o tamanho do vetor A: ")
    vetor_a = criar_vetor(tamanho_a)
    tamanho_b = pegar_numero_positivo("Digite o tamanho do vetor B: ")
    vetor_b = criar_vetor(tamanho_b)

    vetor_c = juntar_vetores(vetor_a, vetor_b)

    print("\nVetor A:")
    mostrar_vetor(vetor_a)
    print(f"tamanho: {len(vetor_a)}")
    print("\nVetor B:")
    mostrar_vetor(vetor_b)
    print(f"tamanho: {len(vetor_b)}")
    print("\nVetor C (união do vetor A com o vetor B):")
    mostrar_vetor(vetor_c)
    print(f"tamanho: {len(vetor_c)}")


def q4():
    tamanho_a = pegar_numero_positivo("Digite o tamanho do vetor A: ")
    vetor_a = criar_vetor(tamanho_a)
    tamanho_b = pegar_numero_positivo("Digite o tamanho do vetor B: ")
    vetor_b = criar_vetor(tamanho_b)

    vetor_c = uniao_vetores(vetor_a, vetor_b)
    vetor_d = elementos_iguais_nos_vetores(vetor_a, vetor_b)
    
    print("\nVetor A:")
    mostrar_vetor(vetor_a)
    print("\nVetor B:")
    mostrar_vetor(vetor_b)
    print("\nVetor C (união entre o vetor A e vetor B):")
    mostrar_vetor(vetor_c)
    print("\nVetor D (intersecção entre vetor A e vetor B):")
    mostrar_vetor(vetor_d)


def q5():
    vetor_a = criar_vetor(20)
    
    s = calcular_s(vetor_a)
    print(f"\nS = {s}")


def calcular_s(vetor):
    s = 0
    for i in range(1, 11):
        termo = (vetor[i -1] - vetor[21 - i - 1]) ** 2
        s += termo
    return s


def q6():
    vetor_binario = criar_vetor(8)

    hexadecimal = converter_binario_para_hexadecimal(vetor_binario)
    decimal = converter_binario_para_decimal(vetor_binario)


    print(f"\nDecimal: {decimal}")
    print(f"Hexadecimal: {hexadecimal}")

def converter_binario_para_decimal(vetor_binario):
    decimal = 0
    for i in range(len(vetor_binario)):
        decimal += vetor_binario[i] * (2 ** (len(vetor_binario) - 1 - i))
    return decimal


def converter_binario_para_hexadecimal(vetor_binario):
    hexadecimal = ""
    for i in range(0, len(vetor_binario), 4):
        hexadecimal += converter_4bits_para_hexadecimal(vetor_binario[i:i+4])
    return hexadecimal


def converter_4bits_para_hexadecimal(vetor_binario):
    decimal = converter_binario_para_decimal(vetor_binario)
    return converter_decimal_para_hexadecimal(decimal)


def converter_decimal_para_hexadecimal(decimal):
    if decimal < 10:
        return str(decimal)
    elif decimal == 10:
        return "A"
    elif decimal == 11:
        return "B"
    elif decimal == 12:
        return "C"
    elif decimal == 13:
        return "D"
    elif decimal == 14:
        return "E"
    elif decimal == 15:
        return "F"
    

def q7():
    tamanho_a = pegar_numero_positivo("Digite o tamanho do vetor: ")
    vetor_a = criar_vetor(tamanho_a)
    vetor_b = criar_vetor_b(vetor_a)

    print("\nVetor A:")
    mostrar_vetor(vetor_a)
    print("\nVetor B:")
    mostrar_vetor(vetor_b)


def q8():
    tamanho = pegar_numero_positivo("Digite o tamanho do vetor: ")
    vetor = criar_vetor(tamanho)

    maior_elemento, indice_maior_elemento, menor_elemento, indice_menor_elemento = maior_menor_elemento_e_indice_no_vetor(vetor)
    
    print("\nVetor:")
    mostrar_vetor(vetor)
    print(f"\nMaior elemento: {maior_elemento}")
    print(f"Índice do maior elemento: {indice_maior_elemento}")
    print(f"\nMenor elemento: {menor_elemento}")
    print(f"Índice do menor elemento: {indice_menor_elemento}")


def q9():
    tamanho = pegar_numero_positivo("Digite o tamanho do vetor: ")
    vetor = criar_vetor(tamanho)
    print("\nVetor:")
    mostrar_vetor(vetor)

    vetor = ordenar_vetor(vetor)

    print("\nVetor ordenado:")
    mostrar_vetor(vetor)


def q10():
    qtd_termos = pegar_numero_positivo("Digite a quantidade de termos: ")
    vetor = criar_vetor_v2(0)

    vetor = gerar_sequencia_fibonacci(qtd_termos)

    print("\nVetor:")
    mostrar_vetor(vetor)


q10()