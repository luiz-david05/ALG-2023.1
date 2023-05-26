def main():
    n = int(input())

    for i in range(n):
        jogador1, escolha1, jogados_2, escolha_2 = input().split()

        n1, n2 = map(int, input().split())

        soma = n1 + n2
        if eh_par(soma):
            if escolha1 == 'PAR':
                print(jogador1)
            else:
                print(jogados_2)
        else:
            if escolha1 == 'IMPAR':
                print(jogador1)
            else:
                print(jogados_2)


def eh_par(n):
    return n % 2 == 0


if __name__ == '__main__':
    main()