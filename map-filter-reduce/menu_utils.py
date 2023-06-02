def criar_vetor_vazio():
    tamanho = int(input("Digite o tamanho do vetor: "))
    return [0] * tamanho


def preencher_vetor(vetor):
    for i in range(len(vetor)):
        vetor[i] = int(input(f"Digite o {i + 1}º elemento: "))
    return vetor


def preencher_vetor_automaticamente(vetor, max, min):
    for valor in range(min, max + 1):
        vetor.append(valor)
    return vetor

def mostrar_vetor(vetor):
    print(f"vetor = {vetor}")


elevar_elementos_do_vetor = lambda vetor, n: list(map(lambda x: x ** n, vetor))

