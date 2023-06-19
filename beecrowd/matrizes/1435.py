def main():
    n = int(input())

    while n != 0:
        matriz = []

        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                matriz[i][j] = 1
            
        print(matriz)


if __name__ == '__main__':
    main()