def main():
    vetor = criar_vetor_v2(20)

    vetor = preencher_vetor(vetor)
    vetor = inverter_vetor(vetor)

    for i in range(len(vetor)):
        print(f'N[{i}] = {vetor[i]}')    


def preencher_vetor(vetor):
    for i in range(len(vetor)):
        vetor[i] = int(input())
    return vetor


def criar_vetor_v2(tamanho):
    vetor = [0] * tamanho
    return vetor


def inverter_vetor(vetor):
    vetor_invertido = criar_vetor_v2(len(vetor))

    for i in range(len(vetor)):
        vetor_invertido[i] = vetor[len(vetor) - 1 - i]
    return vetor_invertido


if __name__ == '__main__':
    main()