def preencher_vetor(vetor):
    for i in range(len(vetor)):
        vetor[i] = int(input())
    return vetor


def substituir_valores(vetor):
    for i in range(len(vetor)):
        if vetor[i] <= 0:
            vetor[i] = 1
    return vetor


def preencher_vetorv2(vetor):
    vetor[0] = int(input())

    for i in range(1, len(vetor)):
        vetor[i] = vetor[i - 1] * 2

    return vetor