def main():
    n = int(input())

    for i in range(1, n + 1):
        if eh_par(i):
            print(f"{i}^2 = {i ** 2}")
        

def eh_par(n):
    return n % 2 == 0


if __name__ == "__main__":
    main()