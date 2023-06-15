from function_utils import *
from random import randint

def criar_vetor_vazio():
    tamanho = get_positive_number("Digite o tamanho do vetor: ")
    return [0] * tamanho


def adicionar_elemento(vetor, elemento):
    for i in range(len(vetor)):
        vetor[i] = elemento


def preencher_vetor_com_valor_padrao(vetor, valor_padrao):
    for i in range(len(vetor)):
        adicionar_elemento(vetor, valor_padrao)
    return vetor


def preencher_vetor(vetor):
    for i in range(len(vetor)):
        vetor[i] = get_int(f"Digite o {i + 1}º elemento: ")
    return vetor


def preencher_vetor_automaticamente(vetor, min, max):
    for i in range(len(vetor)):
        vetor[i] = randint(min, max)
    return vetor


def mostrar_vetor(vetor):
    print(f"vetor = {vetor}")


def map (funcao, vetor):
    for i in range(len(vetor)):
        vetor[i] = funcao(vetor[i])
    return vetor


def filter (funcao, vetor):
    novo_vetor = []
    for i in range(len(vetor)):
        if funcao(vetor[i]):
            novo_vetor.append(vetor[i])
    return novo_vetor


eh_positivo = lambda x: x > 0
eh_negativo = lambda x: x < 0
eh_nulo = lambda x: x == 0
eh_par = lambda x: x % 2 == 0


def reduce (funcao, vetor):
    resultado = vetor[0]
    for i in range(1, len(vetor)):
        resultado = funcao(resultado, vetor[i])
    return resultado


elevar_elementos_por_n = lambda n: lambda x: x ** n


somar_elementos = lambda x, y: x + y


def media_elementos(vetor):
    return reduce(somar_elementos, vetor) / len(vetor)


def sorted(vetor):
    for i in range(len(vetor)):
        for j in range(i, len(vetor)):
            if vetor[i] > vetor[j]:
                vetor[i], vetor[j] = vetor[j], vetor[i]
    return vetor


def mediana_elementos(vetor):
    vetor = sorted(vetor)
    if eh_par(len(vetor)):
        return (vetor[len(vetor) // 2 - 1] + vetor[len(vetor) // 2]) / 2
    else:
        return vetor[len(vetor) // 2]
    

def maior_indice_elemento (vetor):
    maior = vetor[0]
    indice = 0
    for i in range(1, len(vetor)):
        if vetor[i] > maior:
            maior = vetor[i]
            indice = i
    return maior, indice + 1


def menor_indice_elemento (vetor):
    menor = vetor[0]
    indice = 0
    for i in range(1, len(vetor)):
        if vetor[i] < menor:
            menor = vetor[i]
            indice = i
    return menor, indice + 1


def sortear_elemento(vetor):
    return vetor[randint(0, len(vetor) - 1)]