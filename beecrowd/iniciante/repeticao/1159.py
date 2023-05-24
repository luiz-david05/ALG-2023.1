def main():
    while True:
        n = int(input())
        if n == 0:
            break
        print(soma_pares_consectivos(n))


def soma_pares_consectivos(n):
    if eh_impar(n):
        n += 1

    soma = 0
    for i in range(n, n + 10, 2):
        soma += i
    return soma


def eh_impar(n):
    return n % 2 != 0


if __name__ == '__main__':
    main()