def main():
    operacao = input()
    soma = 0

    for i in range(12):
        for j in range(12):
            valor = float(input())
            if j < i:
                soma += valor
    
    if operacao == 'S':
        print(f'{soma:.1f}')
    else:
        print(f'{soma/66:.1f}')


if __name__ == "__main__":
    main()