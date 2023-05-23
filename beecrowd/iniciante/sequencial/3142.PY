def main():
    while True:
        try:
            s = input()

            soma = 0
            for i in range(len(s)):
                soma += ord(s[i]) - 65 + 1 if s[i].isupper() else ord(s[i]) - 97 + 1

            if soma <= 16384:
                print(soma)
            else:
                print('Essa coluna nao existe Tobias!')
        except EOFError:
            break


if __name__ == '__main__':
    main()

            





        


        