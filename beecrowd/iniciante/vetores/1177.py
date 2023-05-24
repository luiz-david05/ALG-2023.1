def main():
    t = int(input())

    vetor = criar_vetorv2(1000)

    for i in range(1000):
        vetor[i] = i % t

    for i in range(1000):
        print(f'N[{i}] = {vetor[i]}')


def criar_vetorv2(tamanho):
    vetor = [0] * tamanho
    return vetor


if __name__ == '__main__':
    main()