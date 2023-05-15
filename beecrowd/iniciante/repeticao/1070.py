def main():
    n = int(input())

    for i in range(n, n+12):
        if i % 2 != 0:
            print(i)


if __name__ == '__main__':
    main()