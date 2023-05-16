def main():
    t = int(input())

    distancia = 0
    for i in range(t):
        tempo, velocidade = map(int, input().split())

        distancia += tempo * velocidade

    print(distancia)


if __name__ == '__main__':
    main()

        