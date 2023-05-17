def main():
    x, y = map(int, input().split())

    while x != 0 and y != 0:
        print(quadrante(x, y))
        x, y = map(int, input().split())


def quadrante(x, y):
    if x > 0 and y > 0:
        return "primeiro"
    elif x < 0 and y > 0:
        return "segundo"
    elif x < 0 and y < 0:
        return "terceiro"
    elif x > 0 and y < 0:
        return "quarto"
    else:
        return ""


if __name__ == "__main__":
    main()