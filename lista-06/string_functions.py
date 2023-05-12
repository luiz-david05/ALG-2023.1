# usando a técnica de slicing
def inverter_frase(frase):
   return frase[::-1]


# usando a tabela ASCII
def eh_letra_maiscula(letra):
    return ord(letra) >= 65 and ord(letra) <= 90


def eh_letra_minuscula(letra):
    return ord(letra) >= 97 and ord(letra) <= 122


def eh_vogal(letra):
    vogais = "aeiouAEIOU"
    return letra in vogais


def eh_consoante(letra):
    return not eh_vogal(letra) and eh_letra(letra)


def eh_letra(letra):
    return eh_letra_maiscula(letra) or eh_letra_minuscula(letra)


def retirar_espacos(frase):
    return frase.split()