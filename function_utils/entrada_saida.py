def mostrar_texto(texto):
    print(texto)


def mostrar_texto_maisculo(texto):
    maiusculas = ""

    for letra in texto:
        if "a" <= letra <= "z":
            maiusculas += chr(ord(letra) - 32)
        else:
            maiusculas += letra
        
    mostrar_texto(maiusculas)


def mostrar_texto_minusculo(texto):
    minusculas = ""

    for letra in texto:
        if "A" <= letra <= "Z":
            minusculas += chr(ord(letra) + 32)
        else:
            minusculas += letra
        
    mostrar_texto(minusculas)


def obter_texto(texto):
    variavel = input(texto)

    if eh_numero(variavel):
        mostrar_texto("O valor informado não é um texto.")
        
        variavel = obter_texto("Informe um texto: ")
    
    return variavel
        
def eh_numero(numero):
    try:
        float(numero)
        return True
    except ValueError:
        return False
    

def obter_texto_tamanho_minimo(texto, tamanho_minimo):
    variavel = obter_texto(texto)

    if len(variavel) < tamanho_minimo:
        mostrar_texto(f"O texto deve ter pelo menos {tamanho_minimo} caracteres.")
        
        variavel = obter_texto_tamanho_minimo(texto, tamanho_minimo)
    
    return variavel


def obter_texto_tamanho_maximo(texto, tamanho_maximo):
    variavel = obter_texto(texto)

    if len(variavel) > tamanho_maximo:
        mostrar_texto(f"O texto deve ter no máximo {tamanho_maximo} caracteres.")
        
        variavel = obter_texto_tamanho_maximo(texto, tamanho_maximo)
    
    return variavel
    

def obter_texto_tamanho(texto, tamanho_minimo, tamanho_maximo):
    variavel = obter_texto(texto)

    if len(variavel) < tamanho_minimo or len(variavel) > tamanho_maximo:
        mostrar_texto(f"O texto deve ter entre {tamanho_minimo} e {tamanho_maximo} caracteres.")
        
        variavel = obter_texto_tamanho(texto, tamanho_minimo, tamanho_maximo)
    
    return variavel


def obter_opcoes(texto, opcoes):
    variavel = obter_texto(texto)
        
    if variavel not in opcoes:
        mostrar_texto(f"Opção inválida. Opções válidas: {opcoes}")
        
        variavel = obter_opcoes(texto, opcoes)
    
    return variavel


def obter_numero(texto):
    n = input(texto)

    try:
        if "." in n:
            n = float(n)
        else:
            n = int(n)
    except ValueError:
        mostrar_texto("O valor informado não é um número.")
        
        n = obter_numero(texto)
    
    return n


def obter_numero_positivo(texto):
    n = obter_numero(texto)

    if n < 0:
        mostrar_texto("Informe um número positivo.")
        
        n = obter_numero_positivo(texto)
    
    return n


def obter_numero_negativo(texto):
    n = obter_numero(texto)

    if n > 0:
        mostrar_texto("Informe um número negativo.")
        
        n = obter_numero_negativo(texto)
    
    return n


def obter_numero_minimo(texto, minimo):
    n = obter_numero(texto)

    if n < minimo:
        mostrar_texto(f"O número deve ser maior ou igual a {minimo}.")
        
        n = obter_numero_minimo(texto, minimo)
    
    return n


def obter_numero_maximo(texto, maximo):
    n = obter_numero(texto)

    if n > maximo:
        mostrar_texto(f"O número deve ser menor ou igual a {maximo}.")
        
        n = obter_numero_maximo(texto, maximo)
    
    return n


def obter_numero_na_faixa(texto, minimo, maximo):
    n = obter_numero(texto)

    if n < minimo or n > maximo:
        mostrar_texto(f"O número deve ser entre {minimo} e {maximo}.")
        
        n = obter_numero_na_faixa(texto, minimo, maximo)
    
    return n

