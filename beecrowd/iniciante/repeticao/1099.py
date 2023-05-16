def main():
    n = int(input())

    for i in range(n):
        x, y = map(int, input().split())

        if x > y:
            x, y = y, x

        soma = 0
        for j in range(x + 1, y):
            if eh_impar(j):
                soma += j
        print(soma)


def eh_impar(n):
    return n % 2 != 0
    
if __name__ == '__main__':
    main()