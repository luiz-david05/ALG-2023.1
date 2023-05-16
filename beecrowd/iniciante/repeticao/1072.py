def main():
    n = int(input())

    valores = [int(input()) for _ in range(n)]

    soma_in = 0
    soma_out = 0
    for i in valores:
        if 10 <= i <= 20:
            soma_in += 1
        else:
            soma_out += 1
    
    print(f"{soma_in} in")
    print(f"{soma_out} out")


if __name__ == "__main__":
    main()