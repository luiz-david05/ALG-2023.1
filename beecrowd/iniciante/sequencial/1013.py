def main():
    n1, n2, n3 = list(map(int, input().split(" ")))
    maior = eh_maior(n1, n2, n3)

    print(f"{maior} eh o maior")


def eh_maior(n1, n2, n3):
    return max(n1, n2, n3)


if __name__ == "__main__":
    main()

# with open("1013.txt" , "r") as entrada:
# n1, n2, n3 = list(map(int, entrada.readline().split(" ")))