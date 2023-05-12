from string_functions import *

def q1():
    frase = input("frase: ")

    print(f"\nfrase criptografada: {criptrografar_frase(frase)}")


def criptrografar_frase(frase):
    frase_invertida = inverter_frase(frase)

    for letra in frase_invertida:
        if eh_consoante(letra):
            frase_invertida = frase_invertida.replace(letra, "#")

    return frase_invertida


def q2():
    frase = "oh my gah!"


    print(f"frase: {frase}")
    print("\npalavras que compõem a frase em linhas separadas:")
    mostrar_palavras(frase)


def mostrar_palavras(frase):
    palavras = frase.split()

    for palavra in palavras:
        print(palavra)

def q3():
    frase = "Hello everioone"

    print(f"\nnova frase: {remover_espacos(frase)}")


def remover_espacos(frase):
    nova_frase = ''

    palavras = frase.split()

    for palavra in palavras:
        nova_frase = nova_frase + palavra

    return nova_frase


def q4():
    frase = "Sank you!"
        
    print(f"frase com caracteres duplicados: {duplicar_caracteres(frase)}")


def duplicar_caracteres(frase):
    frase = remover_espacos(frase)

    nova_frase = ''

    for letra in frase:
        nova_frase = nova_frase + letra * 2

    return nova_frase


def q5():
    data = "05/05/2001"

    dd, mm, aaaa = data.split("/")

    print(dd, mm, aaaa)

q5()