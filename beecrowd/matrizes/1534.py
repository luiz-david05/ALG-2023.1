def main():
    while True:
        try:
            n = int(input())
            matriz = [[0] * n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    if i == j:
                        matriz[i][j] = 1
                    elif i + j == n - 1:
                        matriz[i][j] = 2
                    else:
                        matriz[i][j] = 3
            for i in range(n):
                for j in range(n):
                    print(matriz[i][j], end='')
                print()
        except EOFError:
            break


if __name__ == "__main__":
    main()