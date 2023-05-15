def main():
    t = int(input())

    for i in range(t):
        n, m = map(int, input().split())

        potencia = n ** m

        potencia = str(potencia)

        digitos = qtd_digitos(potencia)

        print(digitos)


def qtd_digitos(n):
    return len(str(n))


if __name__ == '__main__':
    main()