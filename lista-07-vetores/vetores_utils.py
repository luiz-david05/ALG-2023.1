from function_utils import *

def criar_vetor(tamanho):
    vetor = [0] * tamanho

    for i in range(len(vetor)):
        vetor[i] = pegar_numero(f"Valor para a posição[{i}]: ")
    return vetor


def criar_vetor_v2(tamanho):
    vetor = [0] * tamanho
    return vetor

def mostrar_vetor(vetor):
    print(vetor)


def inverter_vetor(vetor):
    vetor_invertido = criar_vetor_v2(len(vetor))

    for i in range(len(vetor)):
        vetor_invertido[i] = vetor[len(vetor) - 1 - i]
    return vetor_invertido


def elementos_iguais_nos_vetores(vetor_a, vetor_b):
    elementos_iguais = []

    for i in range(len(vetor_a)):
        for j in range(len(vetor_b)):
            if vetor_a[i] == vetor_b[j]:
                elementos_iguais.append(vetor_a[i])
    return elementos_iguais


def juntar_vetores(vetor_a, vetor_b):
    vetor_c = criar_vetor_v2(len(vetor_a) + len(vetor_b))

    for i in range(len(vetor_a)):
        vetor_c[i] = vetor_a[i]
    
    for i in range(len(vetor_b)):
        vetor_c[len(vetor_a) + i] = vetor_b[i]
    return vetor_c


def uniao_vetores(vetor_a, vetor_b):
    vetor_c = criar_vetor_v2(len(vetor_a) + len(vetor_b))
    vetor_c = juntar_vetores(vetor_a, vetor_b)
    vetor_c = ordenar_vetor(vetor_c)
    vetor_c = remover_repetidos(vetor_c)
    return vetor_c


def ordenar_vetor(vetor):
    for i in range(len(vetor)):
        for j in range(len(vetor)):
            if vetor[i] < vetor[j]:
                aux = vetor[i]
                vetor[i] = vetor[j]
                vetor[j] = aux
    return vetor


def remover_repetidos(vetor):
    vetor_sem_repetidos = []
    for i in range(len(vetor)):
        if vetor[i] not in vetor_sem_repetidos:
            vetor_sem_repetidos.append(vetor[i])
    return vetor_sem_repetidos


