def main():
    vetor = [0] * 100

    vetor = preencher_vetorv3(vetor)

    for i in range(len(vetor)):
        if vetor[i] <= 10:
            print(f'A[{i}] = {vetor[i]}')


def preencher_vetorv3(vetor):
    for i in range(len(vetor)):
        vetor[i] = float(input())
    return vetor


if __name__ == '__main__':
    main()