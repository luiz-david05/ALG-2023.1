def main():
    n = int(input())

    valores = [int(input()) for _ in range(n)]

    for valor in valores:
        if valor == 0:
            print("NULL")
        else:
            if eh_par(valor):
                print("EVEN", end=" ")
            else:
                print("ODD", end=" ")
            
            if eh_positivo(valor):
                print("POSITIVE")
            else:
                print("NEGATIVE")


def eh_par(n):
    return n % 2 == 0


def eh_positivo(n):
    return n > 0


if __name__ == "__main__":
    main()

