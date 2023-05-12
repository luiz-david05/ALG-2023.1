def main():
    a, b = list(map(int, input().split()))

    maior = a if a > b else b
    menor = a if a < b else b

    eh_multiplo = maior % menor == 0

    mensagem = "Sao Multiplos" if eh_multiplo else "Nao sao Multiplos"

    print(mensagem)


main()