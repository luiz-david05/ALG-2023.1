def main():
    par = []
    impar = []

    for i in range(15):
        n = int(input())

        if eh_par(n):
            par.append(n)
        else:
            impar.append(n)

        if len(par) == 5:
            for j in range(5):
                print(f'par[{j}] = {par[j]}')
            par = []
        if len(impar) == 5:
            for j in range(5):
                print(f'impar[{j}] = {impar[j]}')
            impar = []

    for i in range(len(impar)):
        print(f'impar[{i}] = {impar[i]}')

    for i in range(len(par)):
        print(f'par[{i}] = {par[i]}')


def eh_par(n):
    return n % 2 == 0


if __name__ == '__main__':
    main()