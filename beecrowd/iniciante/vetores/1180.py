def main():
    tamanho = int(input())

    vetor = [int(i) for i in input().split()]
    for i in range(tamanho):
        if vetor[i] == min(vetor):
            print(f'Menor valor: {vetor[i]}')
            print(f'Posicao: {i}')

if __name__ == '__main__':
    main()