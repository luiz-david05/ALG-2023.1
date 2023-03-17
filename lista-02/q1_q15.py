from auxiliar_functions import *


def q1():
    n1 = get_int_number("1° número: ")
    n2 = get_int_number("2° número: ")
    n3 = get_int_number("3° número: ")

    vezes = 0

    if n1 == n2 and n2 == n3:
        vezes = 3

    elif n1 == n2 or n2 == n3 or n1 == n3:
        vezes = 2

    if vezes > 1:
        print(f"\nos números se repetem: {vezes} vezes")

    else:
        print(f"\nos números se repetem: {vezes} vez")


def q2():
    n1 = get_int_number("1° número: ")
    n2 = get_int_number("2° número: ")

    if n1 > n2:
        print(f"\nmaior = {n1}\nmenor = {n2}")

    elif n1 == n2:
        print(f"\nnúmeros iguais")

    else:
        print(f"\nmaior = {n2}\nmenor = {n1}")


def q3():
    n1 = get_int_number("1° número: ")
    n2 = get_int_number("2° número: ")
    n3 = get_int_number("3° número: ")

    if n1 > n2 and n1 > n3:
        maior = n1

    elif n2 > n1 and n2 > n3:
        maior = n2

    elif n3 > n1 and n3 > n2:
        maior = n3

    elif n1 == n2 and n2 == n3:
        print(f"\nnúmeros iguais")

    # se eu soubesse max
    # maior = max(n1, n2, n3)

    print(f"\nmaior = {maior}")


def q4():
    n = get_int_number("número de 2 (dois) dígitos: ")

    d, u = str(n)

    if d == u:
        resultado = "iguais"

    else:
        resultado = "diferentes"

    print(f"\nresultado: {resultado}")


def q5():
    n1 = get_int_number("1° número: ")
    n2 = get_int_number("2° número: ")
    n3 = get_int_number("3° número: ")

    maior, meio, menor = ordenar_numeros_ordem_crescente(n1, n2, n3)

    print(f"\nnúmeros em ordem crescente: [{menor}, {meio}, {maior}]")

   #  numbers = [n1, n2, n3]

   #  numbers.sort()

   #  print(f"\nnúmeros em ordem crescente: {numbers}")


def ordenar_numeros_ordem_crescente(n1, n2, n3):
    if n1 > n2 and n2 > n3:
        maior = n1
        meio = n2
        menor = n3

    elif n2 > n1 and n1 > n3:
        maior = n2
        meio = n1
        menor = n3

    elif n3 > n1 and n1 > n2:
        maior = n3
        meio = n1
        menor = n2

    elif n1 > n3 and n3 > n2:
        maior = n1
        meio = n3
        menor = n2

    elif n2 > n3 and n2 > n1:
        maior = n2
        meio = n2
        menor = n1

    elif n3 > n2 and n2 > n1:
        maior = n3
        meio = n2
        menor = n1

    elif n1 == n2 and n2 == n3:
        print("\nnúmeros iguais")

   #  se eu soubesse max, min
   #  maior = max(n1, n2, n3)
   #  menor = min(n1, n2, n3)

   #  if n1 != maior and n1 != menor:
   #      meio = n1

   #  elif n2 != maior and n2 != menor:
   #      meio = n2

   #  elif n3 != maior and n3 != menor:
   #      meio = n3

    return maior, meio, menor


def q6():
    a1 = get_int_number("1° ângulo: ")
    a2 = get_int_number("2° ângulo: ")
    a3 = get_int_number("3° ângulo: ")

    verificar_tipo_triangulo_angulo(a1, a2, a3)


def verificar_se_forma_triangulo(a1, a2, a3):
    return a1 + a2 + a3 == 180


def acutangulo(a1, a2, a3):
    return a1 < 90 and a2 < 90 and a3 < 90


def retangulo(a1, a2, a3):
    return a1 == 90 or a2 == 90 or a3 == 90


def obtusangulo(a1, a2, a3):
    return a1 > 90 or a2 > 90 or a3 > 90


def verificar_tipo_triangulo_angulo(a1, a2, a3):
    if verificar_se_forma_triangulo(a1, a2, a3):
        if acutangulo(a1, a2, a3):
            print("\nforma triângulo: acutângulo")

        elif retangulo(a1, a2, a3):
            print("\nforma triângulo: retângulo")

        elif obtusangulo(a1, a2, a3):
            print("\nforma triângulo: obtusângulo")

        else:
            print("\noutro tipo de triângulo")

    else:
        print("\nnão forma triângulo")


def q7():
    l1 = get_int_number("1° lado: ")
    l2 = get_int_number("2° lado: ")
    l3 = get_int_number("3° lado: ")

    verificar_tipo_triangulo_lado(l1, l2, l3)


def equilatero(l1, l2, l3):
    return l1 == l2 and l2 == l3


def isosceles(l1, l2, l3):
    return l1 == l2 or l2 == l3


def escaleno(l1, l2, l3):
    return l1 != l2 and l1 != l3 and l2 != l3


def verificar_tipo_triangulo_lado(l1, l2, l3):
    if verificar_se_forma_triangulo(l1, l2, l3):
        if equilatero(l1, l2, l3):
            print("\nforma triângulo: equilátero")

        elif isosceles(l1, l2, l3):
            print("\nforma triângulo: isósceles")

        elif escaleno(l1, l2, l3):
            print("\nforma triângulo: escaleno")

        else:
            print("\noutro tipo de triângulo")

    else:
        print("\nnão forma triângulo")


def q8():
    data_atual = input("data atual (dd/mm/aaaa): ")
    data_nascimento = input("data de nascimento: ")

    dia_atual, mes_atual, ano_atual = data_atual.split('/')
    dia_nascimento, mes_nascimento, ano_nascimento = data_nascimento.split('/')

    idade_anos = int(ano_atual) - int(ano_nascimento) - 1

    print(f"\nidade: {idade_anos} ano(s)")


def q9():
    n = get_int_number("número: ")

    if (numero_primo(n)):
        print(f"\n{n} é um número primo")

    else:
        print(f"\n{n} não é um número primo")


def numero_primo(n):
    if n < 2:
        return False

    elif n == 2:
        return True

    # utilizando for in para verificar se o número é divível por algum número entre 2 e n
    else:
        for i in range(2, n):
            if n % i == 0:
                return False

            else:
                return True


def q10():
    data = input("data(dd/mm/aaaa): ").split('/')

    if verificar_data(data):
        print(f"\n{data} é uma data válida")

    else:
        print(f"\n{data} não é uma data válida")


def verificar_data(data):
    numeros = list(map(int, data))
    dia, mes, ano = numeros

    if dia >= 1 and dia <= 31 and mes >= 1 and \
            mes <= 12 and ano >= 1 and ano <= 2023:
        return True

    else:
        return False


def q11():
    opcao = get_int_number("opção: ")
    n1 = get_int_number("1° número: ")
    n2 = get_int_number("2° número: ")
    n3 = get_int_number("3° número: ")

    if opcao == 1:
        valor = n1

    elif opcao == 2:
        valor = n2

    elif opcao == 3:
        valor = n3

    else:
        valor = "opção inválida"

    print(f"\nvalor = {valor}")


def q12():
    n = get_int_number("número: ")

    if numero_par(n):
        print(f"\n{n} é um número par")

    else:
        print(f"\n{n} é um número par")


def numero_par(n):
    return n % 2 == 0


def q13():
    n1 = get_int_number("1° número: ")
    n2 = get_int_number("2° número: ")
    n3 = get_int_number("3° número: ")
    n4 = get_int_number("4° número: ")
    n5 = get_int_number("5° número: ")

    maior = max(n1, n2, n3, n4, n5)
    menor = min(n1, n2, n3, n4, n5)

    print(f"\nmaior = {maior}\nmenor = {menor}")


def q14():
    n1 = get_float_number("1° número: ")
    n2 = get_float_number("2° número: ")
    n3 = get_float_number("3° número: ")
    n4 = get_float_number("4° número: ")
    n5 = get_float_number("5° número: ")

    media = calcular_media_cinco_notas(n1, n2, n3, n4, n5)

    maiores_media = []

    if n1 > media:
        maiores_media.append(n1)

    if n2 > media:
        maiores_media.append(n2)

    if n3 > media:
        maiores_media.append(n3)

    if n4 > media:
        maiores_media.append(n4)

    if n5 > media:
        maiores_media.append(n5)

    print(f"\nmédia = {media:.1f}\nmaiores que a média = {maiores_media}")


def calcular_media_cinco_notas(n1, n2, n3, n4, n5):
    return (n1 + n2 + n3 + n4 + n5) / 5


def q15():
    nome_professor_1 = input("nome do 1° professor: ")
    qtd_aulas_1 = get_int_number("quantidade de horas aula: ")
    valor_aula_1 = get_float_number("valor da hora: ")

    print()

    nome_professor_2 = input("nome do 2° professor: ")
    qtd_aulas_2 = get_int_number("quantidade de horas aula: ")
    valor_aula_2 = get_float_number("valor da hora: ")

    salario_1 = calcular_salario_professor(qtd_aulas_1, valor_aula_1)

    salario_2 = calcular_salario_professor(qtd_aulas_2, valor_aula_2)

    print(
        f"\nprofessor(a) {nome_professor_1}: R$ {salario_1:.2f}\nprofessor(a) {nome_professor_2}: R$ {salario_2:.2f}")

    if salario_1 > salario_2:
        print(f"\nprofessor(a) {nome_professor_1} recebe mais")

    else:
        print(f"\nprofessor(a) {nome_professor_2} recebe mais")


def calcular_salario_professor(qtd_hrs, valor_hrs):
    return qtd_hrs * valor_hrs


q15()
