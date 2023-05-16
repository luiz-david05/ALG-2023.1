def main():
    maior = 0
    posicao = 0

    for i in range(1, 101):
        x = int(input())

        if x > maior:
            maior = x
            posicao = i 

    print(maior)
    print(posicao)


if __name__ == "__main__":
    main()
