def main():
    a, b, c, d = list(map(int, input().split(" ")))
    if realizar_teste_selecao(a, b, c , d):
        print("Valores aceitos")

    else:
        print("Valores nao aceitos")


def realizar_teste_selecao(a, b, c, d):
    return b > c and d > a and c + d > a + b and c > 1 and d > 1 and a % 2 == 0


if __name__ == "__main__":
    main()
    
    # with open("1035.txt" , "r") as entrada:
    #     a, b, c, d = list(map(int, entrada.readline().split(" ")))