from get_functions import *
import math


def q1():
    n = 1

    # primeiro loop para pedir os números até que o usuário digite 0
    while n != 0:
        n = get_number("digite o número: ")
        print()
        print(f"número = {n}")
        print()

        # segundo loop para exibir os divisores de n
        divisores = 1
        while divisores <= n:
            if eh_divisor(n, divisores):
                print(f"divisores do número {n}: >> {divisores}")

            divisores += 1


def eh_divisor(n1, n2): return n1 % n2 == 0


def q2():
    n1 = get_number("1° número: ")
    n2 = get_number("2° número: ")

    # operação ternária em python para verificar se n1 > que n2
    mmc = n1 if n1 > n2 else n2

    while not (eh_divisor(mmc, n1) and eh_divisor(mmc, n2)):
        mmc += 1

    print(f"\nmmc de {n1} e {n2} = {mmc}")


def q3():
    n1 = get_number("1° número: ")
    n2 = get_number("2° número: ")

    # averiguando maior e menor número para aplicar o teorema de euclides
    maior_numero = n1 if n1 > n2 else n2
    menor_numero = n2 if n1 > n2 else n1
    
    # aplicando teorema de euclides
    dividendo = maior_numero
    divisor = menor_numero

    while divisor != 0:
        resto = dividendo % divisor
        dividendo = divisor
        divisor = resto

    mdc = dividendo

    print(f"\nmcd de {n1} e {n2} = {mdc}")


def q4():
    n1 = get_number("número: ")

    divisao = n1 / 2
    dividendo = n1

    while divisao > 0.9:
        print(f"resultado de {dividendo} / 2 = {divisao}")
        dividendo = divisao

        divisao /= 2

    print(f"resultado da última divisão = {dividendo} / 2 = {divisao}")


def q5():
    x = get_number("x: ")
    n = get_number("n: ")

    while n >= 2:
        divisao = x / n
        print(f"resultado da divisão de {x} / {n} = {divisao}")
        print(f"n = {n}")

        x = divisao
        n -= 1

def q6():
    n = get_number("número: ")

    qtd_digitos = 0
    i = n

    while i != 0:
        i //= 10

        qtd_digitos += 1

    print(f"\no número {n} possui: {qtd_digitos} dígito(s)")


def q7():
    n = get_number("número: ")

    i = math.inf

    while i != n:
        i = get_number("digite os números: ")

    print("\nnúmero digitado = primeiro número digitado")
    print("fim do loop.")


def q8():
    x = get_number("x: ")

    soma = math.inf

    while soma != x:
        n1 = get_number("1° número: ")
        n2 = get_number("2° número: ")

        soma = n1 + n2

    print("\nsoma dos dois número = x")
    print("fim do loop.")


def q9():
    numero_prova = get_number("número da prova: ")
    qtd_nadadores = get_number("quantidade de nadadores: ")

    pontos_clube_a = 0
    pontos_clube_b = 0

    while qtd_nadadores != 0 and numero_prova != 0:
        
        # pedir dados dos nadadores
        qtd_competidores = qtd_nadadores
        while qtd_competidores != 0:
            # tempo e nome são irrelevantes 
            nome = "xx"
            classificao = pegar_classificao_valida()
            tempo = 0
            clube = pegar_clube_valido()
            print(">>> próximo competidor")

            # atribuir pontuação

            if clube == "a":
                if classificao == 1:
                    pontos_clube_a += 9
                elif classificao == 2:
                    pontos_clube_a += 6
                elif classificao == 3:
                    pontos_clube_a += 4
                elif classificao == 4:
                    pontos_clube_a += 3
            else:
                if classificao == 1:
                    pontos_clube_b += 9
                elif classificao == 2:
                    pontos_clube_b += 6
                elif classificao == 3:
                    pontos_clube_b += 4
                elif classificao == 4:
                    pontos_clube_b += 3

            qtd_competidores -= 1

        numero_prova = get_number("número da prova: ")
        qtd_nadadores = get_number("quantidade de nadadores: ")

    # verificar resultado das provas

    if pontos_clube_a == pontos_clube_b:
        resultado = "empate"
    elif pontos_clube_a > pontos_clube_b:
        resultado = "clube a venceu"
    elif pontos_clube_b > pontos_clube_a:
        resultado = "clube b venceu"

    print()
    print(4 * "-", "totais", "-" * 4)
    print(f"quantidade de pontos clube a: {pontos_clube_a}")
    print(f"quantidade de pontos clube b: {pontos_clube_b}")
    print(f"resultado: {resultado}")


def pegar_classificao_valida(texto = "classificação: "):
    classificao = get_valid_number(texto)
    opcoes_validas = [1, 2, 3, 4]

    if classificao not in opcoes_validas:
        print("opção inválida, digite uma das opções válidas: [1, 2, 3, 4]")

        classificao = pegar_classificao_valida(texto)

    return classificao


def pegar_clube_valido(texto = "clube: "):
    clube = input(texto)

    if clube != "a" and clube != "b":
        print("clube inválido: digite a ou b")

        clube = pegar_clube_valido(texto)

    return clube


def q10():
   # Leitura do número de containers e dos pesos
    qtd_containers = get_valid_number("Digite o número de containers: ")
    peso_carga = 0

    i = 1
    while i <= qtd_containers:
        peso_container = get_valid_number(f"Digite o peso do container {i} (em kg): ")
        peso_carga += peso_container

        i += 1

    # Leitura dos dados dos passageiros
    num_passageiros = 0
    peso_passageiros = 0
    vol_bagagem = 0

    while True:
        bilhete = get_valid_number("Digite o número do bilhete do passageiro (ou 0 para sair): ")
        if bilhete == 0:
            break

        qtd_bagagens = get_valid_number("Digite a quantidade de bagagens do passageiro: ")
        print("próximo passageiro >>>")
        print()
        

        peso_passageiros += 70
        vol_bagagem += qtd_bagagens * 10
        num_passageiros += 1

    # Cálculo do peso total de decolagem e da quantidade de combustível
    peso_decolagem = peso_carga + peso_passageiros + 500000
    quant_combustivel = (peso_decolagem - 500000) / 1.5

    print(f"\nQuantidade de passageiros: {num_passageiros}")
    print(f"Quantidade total de volume de bagagem: {vol_bagagem}")
    print(f"Peso dos passageiros: {peso_passageiros}")
    print(f"Peso da carga: {peso_carga}")
    print(f"Quantidade possível de combustível: {quant_combustivel:.1f}")

    # Verificação da possibilidade de decolagem
    if quant_combustivel >= 10000:
        print(f"Decolagem liberada!")
    else:
        print("Decolagem não liberada. Quantidade mínima de combustível necessária é 10.000 litros.")


def q11():
    aprovados = 0
    reprovados = 0
    num_alunos = 0
    while True:
        matricula = get_valid_number("n° da matrícula: ")

        if matricula == 0:
            break

        nota1, nota2, nota3 = [float(input(f"{i}° nota: ")) for i in range(1, 4)]
        print("próximo aluno >>>")
        print()

        # calcular media final
        media_final = calcular_media(nota1, nota2, nota3)

        if media_final >= 7:
            aprovados += 1
        else:
            reprovados += 1

        num_alunos += 1

    print(f"\ntotal de aprovados: {aprovados}")
    print(f"total de alunos reprovados: {reprovados}")
    print(f"total de alunos na turma: {num_alunos}")
                 

def calcular_media(n1, n2, n3): return ((n1 * 2) + (n2 * 3) + (n3 * 5)) / 10


def q12():
    pontos_jogador1 = 0
    pontos_jogador2 = 0
    diff_pontos = 0

    while pontos_jogador1 < 5 and pontos_jogador2 < 5:
    # Leia o código do jogador que ganhou o ponto
        codigo_jogador = ler_codigo()

    # Adicionar o ponto ao jogador correspondente
        if codigo_jogador == 1:
            pontos_jogador1 += 1
        elif codigo_jogador == 2:
            pontos_jogador2 += 1

    # Calcular a diferença de pontos atual
        diff_pontos = abs(pontos_jogador1 - pontos_jogador2)

        if diff_pontos >= 2:
            break

    vencedor = max(pontos_jogador1, pontos_jogador2)

    print()
    if pontos_jogador1 == pontos_jogador2:
        print("empate")
    elif pontos_jogador1 == vencedor:
        print("jogador 1 venceu")
    elif pontos_jogador2 == vencedor:
        print("jogador 2 venceu")
    

def ler_codigo(texto = "jogador que ganhou ponto: "):
    cod = get_valid_number(texto)

    if cod != 1 and cod != 2:
        print("informe corretamente quem ganhou o ponto: jogador 1 - [1] ou jogador 2 - [2]")

        cod = ler_codigo(texto)

    return cod


q12()