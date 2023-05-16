def main():
    h, z, l = map(int, input().split())

    maior = max(h, z, l)
    menor = min(h, z, l)

    if maior == h and menor == z:
        print("luisinho")
    elif maior == z and menor == h:
        print("luisinho")
    elif maior == h and menor == l:
        print("zezinho")
    elif maior == l and menor == h:
        print("zezinho")
    elif maior == z and menor == l:
        print("huguinho")
    elif maior == l and menor == z:
        print("huguinho")
    

if __name__ == '__main__':
    main()