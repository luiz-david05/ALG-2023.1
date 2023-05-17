def main():
    while True:
        try:
            n = int(input())

            entrada = list(map(int, input().split()))

            maior = max(entrada)

            if maior < 10:
                print(1)
            elif maior >= 10 and maior < 20:
                print(2)
            else:
                print(3)
        except EOFError:
            break

if __name__ == "__main__":
    main()