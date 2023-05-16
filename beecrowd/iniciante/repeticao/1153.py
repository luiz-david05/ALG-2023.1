def main():
    n = int(input())

    numero_fatorial = fatorial(n)


    print(numero_fatorial)


def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)


if __name__ == "__main__":
    main()