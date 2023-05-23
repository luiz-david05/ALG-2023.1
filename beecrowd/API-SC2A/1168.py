def main():
    n = int(input())

    for i in range(n):
        leds = 0
        numero = input()

        leds = atribuir_leds(numero)

        print(f'{leds} leds')


def atribuir_leds(numero):
    leds = 0
    for j in numero:
        if j == '1':
            leds += 2
        elif j == '2':
            leds += 5
        elif j == '3':
            leds += 5
        elif j == '4':
            leds += 4
        elif j == '5':
            leds += 5
        elif j == '6':
            leds += 6
        elif j == '7':
            leds += 3
        elif j == '8':
            leds += 7
        elif j == '9':
            leds += 6
        elif j == '0':
            leds += 6
    return leds


if __name__ == '__main__':
    main() 