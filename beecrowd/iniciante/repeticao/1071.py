def main():
    x = int(input())
    y = int(input())

    if x > y:
        x, y = y, x

    soma_impares_consecutivos = 0
    for i in range(x + 1, y):
        if not eh_par(i):
            soma_impares_consecutivos += i

    print(soma_impares_consecutivos)


def eh_par(n):
    return n % 2 == 0


if __name__ == "__main__":
    main()