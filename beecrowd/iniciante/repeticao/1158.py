def main():
    n = int(input())
    
    for i in range(n):
        x, y = map(int, input().split())
        print(soma_impares(x, y))


def soma_impares(x, y):
    if eh_par(x):
        x += 1

    soma = 0
    for i in range(x, x + y * 2, 2):
        soma += i
    return soma


def eh_par(n):
    return n % 2 == 0


if __name__ == '__main__':
    main()