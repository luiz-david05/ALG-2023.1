def main():
    x = int(input())
    z = int(input())

    while z <= x:
        z = int(input())

    soma = 0
    contador = 0
    while soma < z:
        soma += x
        x += 1
        contador += 1
        
    print(contador)


if __name__ == '__main__':
    main()