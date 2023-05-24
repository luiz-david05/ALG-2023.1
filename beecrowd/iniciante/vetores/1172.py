def main():
    vetor = [0] * 10

    vetor = preencher_vetor(vetor)
    vetor = substituir_valores(vetor)
    
    for i in range(len(vetor)):
        print(f'X[{i}] = {vetor[i]}')


def preencher_vetor(vetor):
    for i in range(len(vetor)):
        vetor[i] = int(input())
    return vetor


def substituir_valores(vetor):
    for i in range(len(vetor)):
        if vetor[i] <= 0:
            vetor[i] = 1
    return vetor

if __name__ == '__main__':
    main()