def main():
    valores = input().split()

    a = int(valores[0])
    ultimo = int(valores[-1])
    soma = 0

    while ultimo <= 0:
        ultimo = int(input())

    for i in range(ultimo):
        soma += a + i
    
    print(soma)


if __name__ == '__main__':
    main()