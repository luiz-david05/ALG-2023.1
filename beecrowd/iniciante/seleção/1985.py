def main():
    n = int(input())

    produtor = {
        1001: 1.50,
        1002: 2.50,
        1003: 3.50,
        1004: 4.50,
        1005: 5.50
    }

    total = 0

    for i in range(n):
        cod, qtd = map(int, input().split())

        total += produtor[cod] * qtd

    print(f'{total:.2f}')


if __name__ == '__main__':
    main()