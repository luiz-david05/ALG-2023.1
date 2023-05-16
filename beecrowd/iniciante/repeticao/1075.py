def main():
    n = int(input())

    for i in range(1, 10001):
        if resto_2(i, n):
            print(i)


def resto_2(n1, n2):
    return n1 % n2 == 2


if __name__ == "__main__":
    main()