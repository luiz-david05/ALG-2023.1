def main():
    t = int(input())
    while True:
        try:
            for i in range(t):
                a, b = input().split()

                if a[-len(b):] == b:
                    print('encaixa')
                else:
                    print('nao encaixa')
        except EOFError:
            break   


if __name__ == '__main__':  
    main()