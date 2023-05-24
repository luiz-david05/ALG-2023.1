def main():
    t = int(input())

    vetor = criar_vetor_v2(61)
    vetor = preencher_vetor(vetor)

    for i in range(t):
        n = int(input())
        print(f'Fib({n}) = {vetor[n]}')


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 2) + fib(n - 1)
    

def criar_vetor_v2(tamanho):
    vetor = [0] * tamanho
    return vetor


def preencher_vetor(vetor):
    vetor[0] = 0
    vetor[1] = 1

    for i in range(2, len(vetor)):
        vetor[i] = vetor[i - 2] + vetor[i - 1]
    return vetor

if __name__ == '__main__':
    main()