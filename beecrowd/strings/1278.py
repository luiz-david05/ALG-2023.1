def main():
    n = int(input())

    while n > 0:
        for i in range(n):
            linhas = input().split()

            for j in range(len(linhas)):
                if j == 0:
                    print(linhas[j], end='')
                else:
                    print(" " + linhas[j], end='')
            print()

        n = int(input())

        if n > 0:
            print()
    

if __name__ == "__main__":
    main()