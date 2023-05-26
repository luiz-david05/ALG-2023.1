def main():
    n = int(input())

    for i in range(n):
        m = int(input())
        
        if eh_par(m):
            print(0)
        else:
            print(1)


def eh_par(n):
    return n % 2 == 0


if __name__ == '__main__':
    main()


