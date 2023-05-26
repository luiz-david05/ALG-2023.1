def main():
    n = int(input())

    lista = list(map(int, input().split()))

    multiplos_2 = 0
    multiplos_3 = 0
    multiplos_4 = 0
    multiplos_5 = 0
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            multiplos_2 += 1
        if lista[i] % 3 == 0:
            multiplos_3 += 1
        if lista[i] % 4 == 0:
            multiplos_4 += 1
        if lista[i] % 5 == 0:
            multiplos_5 += 1
        
    print(f'{multiplos_2} Multiplo(s) de 2')
    print(f'{multiplos_3} Multiplo(s) de 3')
    print(f'{multiplos_4} Multiplo(s) de 4')
    print(f'{multiplos_5} Multiplo(s) de 5')


if __name__ == '__main__':
    main()