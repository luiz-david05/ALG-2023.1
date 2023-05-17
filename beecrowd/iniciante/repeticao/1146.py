def main():
    while True:
        try:
            n = int(input())

            if n == 0:
                break

            for i in range(1, n + 1):
                if i == n:
                    print(i)
                else:
                    print(i, end=" ")
        except EOFError:
            break


if __name__ == "__main__":
    main()