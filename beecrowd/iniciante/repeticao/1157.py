def main():
    n = int(input())
    
    for i in range(1, n+1):
        if eh_divisor(n, i):
            print(i)


def eh_divisor(n, i):
    return n % i == 0


if __name__ == '__main__':
    main()