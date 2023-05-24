def main():
    vetor = [0] * 10

    vetor = preencher_vetorv2(vetor)
    for i in range(len(vetor)):
        print(f'N[{i}] = {vetor[i]}')


def preencher_vetorv2(vetor):
    vetor[0] = int(input())

    for i in range(1, len(vetor)):
        vetor[i] = vetor[i - 1] * 2

    return vetor


if __name__ == '__main__':
    main()
    