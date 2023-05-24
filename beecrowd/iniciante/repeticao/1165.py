def main():
    n = int(input())

    for i in range(n):
        x = int(input())
        print(f'{x} eh primo' if eh_primo(x) else f'{x} nao eh primo')


def eh_primo(n):
    if n <= 1:
        return False
    
    i = 2

    while i < n:
        if eh_multiplo(n, i):
            return False
        
        i += 1

    return True


def eh_multiplo(n1, n2): return n1 % n2 == 0


if __name__ == '__main__':
    main()