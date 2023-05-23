from function_utils import *
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


q4()