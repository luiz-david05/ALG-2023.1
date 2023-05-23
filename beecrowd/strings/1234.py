def main():
    while True:
        try:
            frase = input()

            nova_frase = ''
            contador = 0
            for i in range(len(frase)):
                if frase[i].isalpha():
                    if eh_par(contador):
                        nova_frase += frase[i].upper()
                    else:
                        nova_frase += frase[i].lower()
                    contador += 1
                else:
                    nova_frase += frase[i]
        
            print(nova_frase)      
        except EOFError:
            break


def eh_par(n):
    return n % 2 == 0


if __name__ == "__main__":
    main()

