def main():
    a, b = map(int, input().split())

    tempo_jogo = 0

    if a > b:
        tempo_jogo = abs(a - (b + 24))
    elif a == b:
        tempo_jogo = 24
    elif b > a:
        tempo_jogo = abs(a - b)

    print(f"O JOGO DUROU {tempo_jogo} HORA(S)")


main()