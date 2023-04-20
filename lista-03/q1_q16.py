from get_functions import *
from auxiliar_functions import *


def q1():
    n = get_number("n: ")

    exibir_numeros_inteiros(n)


def exibir_numeros_inteiros(n):
    print(f"números inteiros entre 1 e {n}")

    i = 1

    while i <= n:
        print(f"> {i}")

        i += 1


def q2():
    n = get_number("n: ")

    print(f"números pares entre 1 e {n}")
    exibir_numeros_pares(n)


def exibir_numeros_pares(n):
    i = 1

    while i <= n:
        if eh_par(i):
            print(f"> {i}")

        i += 1


def q3():
    a0 = get_number("a0: ")
    limite = get_number("limite: ")
    r = get_number("razão: ")

    print(f"termos gerados pela PA menores que o limite:")
    gerar_pa(a0, limite, r)


def gerar_pa(a0, limite, r):
    i = a0

    while i < limite:
        print(f"> {i}")

        i += r


def q4():
    a0 = get_number("a0: ")
    limite = get_number("limite: ")
    r = get_number("razão: ")

    print(f"termos gerados pela PG menores que o limite:")
    gerar_pg(a0, limite, r)


def gerar_pg(a0, limite, r):
    i = a0

    while i < limite:
        print(f"> {i}")

        i *= r


def q5():
    n = get_number("n: ")

    fatorial = calcular_fatorial(n)
    print(f"{n}! = {fatorial}")


def calcular_fatorial(n):
    fatorial = 1
    i = 1

    while i < n + 1:
        fatorial *= i

        i += 1

    return fatorial


def q6():
    print(f"tabuada dos números de 1 a 10")

    j = 1

    while j <= 10:
        exibir_tabuada(j)
        print()

        j += 1


def exibir_tabuada(n):
    i = 1

    while i <= 10:
        print(f"{n} x {i} = {n * i}")

        i += 1


def q7():
    n = get_number("n: ")

    exibir_numeros_inteiros(n)
    soma = soma_dos_numeros_inteiros(n)
    print(f"\nsoma dos números = {soma}")


def soma_dos_numeros_inteiros(n):
    i = 1
    soma = 0

    while i <= n:
        i += 1

        soma += i

    return soma


def q8():
    n = get_number("n: ")
    limite_inferior = get_number("limite inferior: ")
    limite_superior = get_number("limite superior: ")

    exibir_multiplos(n, limite_inferior, limite_superior)


def exibir_multiplos(n, menor, maior):
    candidato = menor

    print(f"múltiplos de {n} entre os limites:")

    while candidato <= maior:
        if eh_multiplo(candidato, n):
            print(f"> {candidato}")

        candidato += 1


def q9():
    limite_inferior = get_number("limite inferior: ")
    limite_superior = get_number("limite superior: ")

    exibir_pares_entre_limites(limite_inferior, limite_superior)

    # questão 10
    exibir_impares_entre_limites(limite_inferior, limite_superior)

    # questão 11
    exibir_primos_entre_limites(limite_inferior, limite_superior)


def exibir_pares_entre_limites(menor, maior):
    i = menor

    print(f"números pares entre os limites:")
    while i <= maior:
        if eh_par(i):
            print(f"> {i}")

        i += 1


def exibir_impares_entre_limites(menor, maior):
    i = menor

    print(f"números impares entre os limites:")
    while i <= maior:
        if not eh_par(i):
            print(f"> {i}")

        i += 1


def exibir_primos_entre_limites(menor, maior):
    i = menor

    print(f"números primos entre os limites:")
    while i <= maior:
        if eh_primo(i):
            print(f"> {i}")

        i += 1


def q12():
    qtd_n = get_number("quantidade de números: ")

    soma = 0
    i = 1

    while i <= qtd_n:
        n = get_number(f"digite o {i}° número: ")

        soma += n
        i += 1

    media = calcular_media(qtd_n, soma)

    print(f"\nsoma = {soma}")
    print(f"média = {media:.1f}")


def calcular_media(qtd, soma): return soma / qtd


def q13():
    qtd_n = get_number("quantidade de números: ")

    exibir_maior_numero_digitado(qtd_n)


def exibir_maior_numero_digitado(qtd_n):
    i = 1
    maior = 0

    while i <= qtd_n:
        n = get_number(f"digite o {i}° número: ")

        if n > maior:
            maior = n

        i += 1

    print(f"\nmaior número digitado: {maior}")


def q14():
    n = get_number("n: ")

    exibir_maior_quadrado(n)


def exibir_maior_quadrado(n):
    i = 1

    while i * i < n:
        maior_quadrado = i * i

        i += 1

    print(
        f"\nmaior quadrado menor que {n} = {maior_quadrado} (quadrado de {i - 1})")


def q15():
    n = get_number("n: ")

    exibir_sequencia(n)


def exibir_sequencia(n):
    qtd_termos = 0
    termo = 1
    i = 2

    print(f"\n{n} primeiros termos da sequência:")
    while qtd_termos < n:
        print(f"> {termo}")

        termo += i
        i += 1
        qtd_termos += 1


def q16():
    n = get_number("n: ")

    exibir_n_termos_fibonacci(n)


def exibir_n_termos_fibonacci(n):
    qtd_termos = 0
    a = 0
    b = 1

    print(f"{n} primeiros termos da sequência de fibonacci:")
    while qtd_termos < n:
        print(f"> {a}")
        c = a + b

        a = b
        b = c

        qtd_termos += 1


q16()
