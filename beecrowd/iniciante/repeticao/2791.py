def main():
    posicoes = [int(x) for x in input().split()]

    for i in range(1, 5):
        if posicoes[i-1] == 1:
            print(i)
            break


if __name__ == '__main__':
    main()