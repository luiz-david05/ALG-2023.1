def main():
    matriz = [[0] * 12 for _ in range(12)]
    operacao = input()

    for i in range(12):
        for j in range(12):
            matriz[i][j] = float(input())
        
    soma = 0
    for i in range(7,12):
        for j in range(12 - i, i):
            soma += matriz[i][j]

    if operacao == 'S':
        print(f'{soma:.1f}')
    else:
        print(f'{soma/30:.1f}')


if __name__ == "__main__":
    main()