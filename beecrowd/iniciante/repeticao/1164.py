def main():
    n = int(input())

    for i in range(n):
        x = int(input())

        print(f'{x} eh perfeito' if eh_numero_perfeito(x) else f'{x} nao eh perfeito')


def eh_numero_perfeito(n):
    if n < 0:
        return False

    if n == 0:
        return True

    soma = 0

    for i in range(1, n):
        if n % i == 0:
            soma += i

    return soma == n


if __name__ == '__main__':
    main()