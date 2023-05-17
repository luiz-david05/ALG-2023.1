from get_functions import *
import math


def q16():
    emprestimo = 3000
    juros = 0.0085 
    pagamento = 200
    saldo = 0
    qtd_dias = 0
    while saldo <= emprestimo:
        emprestimo += emprestimo * juros
        saldo += pagamento

        qtd_dias += 1

        if qtd_dias % 5 == 0:
            for i in range(1, 3):
                emprestimo += emprestimo + juros
                saldo += pagamento
    print(f"quantidade dias úteis: {qtd_dias}")


def q17():
    nome = ''

    altura_mais_alta = 0
    altura_mais_baixa = math.inf
    peso_mais_magra = math.inf
    peso_mais_gorda = 0
    nome_mais_alta = ''
    nome_mais_baixa = ''
    nome_mais_gorda = ''
    nome_mais_magra = ''

    while nome != 'FIM':
        nome = input("nome ou (FIM para sair): ")

        if nome == 'FIM':
            break

        altura = get_valid_number("altura m: ")
        peso = get_valid_number("peso: ")


        if altura > altura_mais_alta:
            altura_mais_alta = altura
            nome_mais_alta = nome

        if altura < altura_mais_baixa:
            altura_mais_baixa = altura
            nome_mais_baixa = nome

        if peso > peso_mais_gorda:
            peso_mais_gorda = peso
            nome_mais_gorda = nome

        if peso < peso_mais_magra:
            peso_mais_magra = peso
            nome_mais_magra = nome
        
    print(f"\nnome da canidata mais alta: {nome_mais_alta}\taltura: {altura_mais_alta} m")
    print(f"nome da candidata mais baixa: {nome_mais_baixa}\taltura: {altura_mais_baixa} m")
    print(f"\nnome da candidata mais magra: {nome_mais_magra}\tpeso da candidata mais magra: {peso_mais_magra} kg")
    print(f"nome da candidata mais gorda: {nome_mais_gorda}\tpeso da candidata mais gorda: {peso_mais_gorda} kg")


def q18():
    populacao_a = 200000
    populacao_b = 800000

    crescimento_populacional_a = math.floor(populacao_a * (3.5 / 100))
    crescimento_populacional_b = math.floor(populacao_b * (1.35 / 100))

    qtd_anos = 0

    while populacao_a < populacao_b:
        populacao_a += crescimento_populacional_a
        populacao_b += crescimento_populacional_b
        qtd_anos += 1

    print(f"\nSerão necessários: {qtd_anos} ano(s) para a população da cidade A ultrapassar a população da cidade B")


def q19():
    id = ''

    peso_boi_mais_gordo = 0
    peso_boi_mais_magro = math.inf

    while id != 0:
        id = get_valid_number("ID: ")

        if id == 0:
            break

        peso = get_valid_number("peso kg: ")

        if peso > peso_boi_mais_gordo:
            peso_boi_mais_gordo = peso
            id_mais_gordo = id

        if peso < peso_boi_mais_magro:
            peso_boi_mais_magro = peso
            id_mais_magro = id

    print(f"\nid do boi mais gordo: {id_mais_gordo}\tpeso {peso_boi_mais_gordo} kg")
    print(f"\nid boi mais magro: {id_mais_magro}\tpeso {peso_boi_mais_magro} kg")


def q21():
    n1 = get_number("1° número: ")
    n2 = get_number("2° número: ")

    resultado = 0
    i = 0
    while i < n2:
        resultado += n1

        i += 1

    print(f"\nresultado da multiplicação de {n1} x {n2} = {resultado}")


def q22():
    n1 = get_number("1° número: ")
    n2 = get_number("2° número: ")

    quociente = 0
    resto = n1

    while resto >= n2:
        resto -= n2
        quociente += 1

    print(f"\ndivisão de {n1}/{n2}")
    print(f"quociente = {quociente}")
    print(f"resto = {resto}")


def q23():
    n = get_number("n: ")
    a0 = get_number("a0: ")
    razao = get_number("razão: ")

    i = a0
    j = 1
    print("\ntermos da pg: ")
    while j <= n:
        i *= razao
        print(f">>> {i}")

        j += 1

def q24():
    n = get_number("n: ")
    a0 = get_number("a0: ")
    razao = get_number("razão: ")

    i = a0
    j = 1
    print("\ntermos da pa: ")
    while j <= n:
        i += razao
        print(f">>> {i}")

        j += 1


def q25():
    canal = ''
    total_telespectadores = 0
    total_canal_2 = 0
    total_canal_4 = 0
    total_canal_5 = 0
    total_canal_7 = 0
    total_canal_10 = 0

    while canal != 0:
        canal = pegar_canal_valido()

        if canal == 0:
            break

        qtd_telespectadores = get_valid_number("quantidade de telespectadores: ")

        if canal == 2:
            total_canal_2 += qtd_telespectadores
        elif canal == 4:
            total_canal_4 += qtd_telespectadores
        elif canal == 5:
            total_canal_5 += qtd_telespectadores
        elif canal == 7:
            total_canal_7 += qtd_telespectadores
        elif canal == 10:
            total_canal_10 += qtd_telespectadores
        
        total_telespectadores += qtd_telespectadores

    
    percentual_canal_2 = total_canal_2 / total_telespectadores * 100
    percentual_canal_4 = total_canal_4 / total_telespectadores * 100
    percentual_canal_5 = total_canal_5 / total_telespectadores * 100
    percentual_canal_7 = total_canal_7 / total_telespectadores * 100
    percentual_canal_10 = total_canal_10 / total_telespectadores * 100

    print(f"\npercentual de cada emissora:")
    print(f"canal 2: {percentual_canal_2:.2f}%")
    print(f"canal 4: {percentual_canal_4:.2f}%")
    print(f"canal 5: {percentual_canal_5:.2f}%")
    print(f"canal 7: {percentual_canal_7:.2f}%")
    print(f"canal 10: {percentual_canal_10:.2f}%")

    print(f"\naudiência de cada emissora:")
    print(f"canal 2: {total_canal_2}")
    print(f"canal 4: {total_canal_4}")
    print(f"canal 5: {total_canal_5}")
    print(f"canal 7: {total_canal_7}")
    print(f"canal 10: {total_canal_10}")


def pegar_canal_valido(texto = "informe o canal: "):
    canal = get_valid_number(texto)
    canais = [0, 2, 4, 5, 7, 10]

    if canal not in canais:
        print("opções válidas: 2, 4, 5, 7, 10 e 0 para encerrar")

        canal = pegar_canal_valido(texto)

    return canal


def q26():
    idade = math.inf
    total_regular = 0
    media_otimo = 0
    total_idade_telespectadores = 0
    total_otimo = 0
    total_bom = 0
    total_regular = 0
    total_telespectadores = 0
    percentual_bom = 0

    while idade > 0:
        idade = get_number("idade: ")

        if idade < 0:
            break

        opiniao = pegar_opiniao_espectador()

        if opiniao == 1:
            total_otimo += 1
            total_idade_telespectadores += idade
        elif opiniao == 2:
            total_bom += 1
        elif opiniao == 3:
            total_regular += 1

        total_telespectadores += 1

    if total_otimo > 0:
        media_otimo = total_idade_telespectadores / total_otimo
    
    if total_telespectadores > 0:
        percentual_bom = total_bom / total_telespectadores * 100

    print(f"\nmédia das idades das pessoas que responderam ótimo: {media_otimo}")
    print(f"quantidade de pessoas que responderam regular: {total_regular}")
    print(f"percentual de pessoas que responderam bom entre os entrevistados: {percentual_bom:.2f}%")


def pegar_opiniao_espectador(texto = "opinião: "):
    opiniao = get_valid_number(texto)
    opiniao_valida = [1, 2, 3, 4]

    if opiniao not in opiniao_valida:
        print(f"opções válidas: 1 = ótimo, 2 = bom, 3 = regular, 4 = médio e -1 para parar a pesquisa.")

        opiniao = pegar_opiniao_espectador(texto)
    
    return opiniao


def q27():
    total_pessoas = 100
    total_mulheres = 0
    total_mulheres_divorciadas = 0
    total_homens = 0
    total_idade = 0
    percentual_mulheres_solteiras = 0
    percentual_homens_solteiros = 0
    total_mulheres_solteiras = 0
    total_homens_solteiros = 0
    total_idade_mulheres = 0
    total_idade_homens = 0
    media_idade_mulheres = 0
    media_idade_homens = 0


    while total_pessoas > 0:
        genero = pegar_genero_valido()
        idade = get_valid_number("idade: ")
        estado_civil = pegar_estado_civil_valido()
        print("próxima pessoa >>>")
        print()

        if genero == 1:
            total_homens += 1

            if estado_civil == 2:
                total_homens_solteiros += 1

            total_idade_homens += idade
        else:
            total_mulheres += 1

            total_idade_mulheres += idade

            if estado_civil == 2:
                total_mulheres_solteiras += 1
            elif estado_civil == 3:
                if idade > 30:
                    total_mulheres_divorciadas += 1
            
        total_pessoas -= 1

    if total_mulheres > 0:
        media_idade_mulheres = total_idade_mulheres / total_mulheres

        percentual_mulheres_solteiras = total_mulheres_solteiras / total_mulheres * 100

    if total_homens > 0:
        media_idade_homens = total_idade_mulheres / total_mulheres

        percentual_homens_solteiros = total_homens_solteiros / total_homens * 100

    print(f"\nmédia de idade das mulheres: {media_idade_mulheres:.1f}")
    print(f"média de idade dos homens: {media_idade_homens:.1f}")
    print(f"\npercentual de homens solteiros: {percentual_homens_solteiros:.2f}%")
    print(f"percentual de mulheres solteiras: {percentual_mulheres_solteiras:.2f}")
    print(f"\nquantidade de mulheres divorciadas acima de 30 anos: {total_mulheres_divorciadas:.2f}")

def pegar_genero_valido(texto = "gênero: "):
    genero = get_valid_number(texto)

    if genero != 1 and genero != 2:
        print("gênero inválido, opções válidas: 1 = masculino e 2 = feminino")

        genero = pegar_genero_valido(texto)
    
    return genero


def pegar_estado_civil_valido(texto = "estado civil: "):
    estado_civil = get_valid_number(texto)
    estados = [1, 2, 3, 4]

    if estado_civil not in estados:
        print("estado civil inválido, estados válidos: 1 = casado, 2 = solteiro, 3 = divorciado e 4 = viúvo")

        estado_civil = pegar_estado_civil_valido(texto)

    return estado_civil


def q28():
    import random
    numero_aleatorio = random.randint(1, 10)

    print("\tadivinhe o número (entre 1 e 10), para isso digite um número até acertar.")

    qtd_tentativas = 0

    while True:
        n = get_valid_number("seu número: ")

        qtd_tentativas += 1

        if n == numero_aleatorio:
            break

        if n > numero_aleatorio:
            print(f"digite um número menor")
        
        else:
            print(f"digite um número maior")


        
    print(f"\nvocê acertou em {qtd_tentativas} tentativa(s)")


def q30():
    nome_produto = ''
    valor_total = 0

    while nome_produto != "FIM":
        nome_produto = input("nome do produto: ")

        if nome_produto == "FIM":
            break

        preco = get_valid_number("preço do produto (ou FIM para encerrar): ")
        qtd_comprada = get_valid_number("quantidade do produto: ")

        valor_total = preco * qtd_comprada

        if qtd_comprada <= 10:
            desconto = 0
        elif qtd_comprada > 10 and qtd_comprada <= 20:
            desconto = valor_total * 0.10
        elif qtd_comprada > 20 and qtd_comprada <= 50:
            desconto = valor_total * 0.20
        elif qtd_comprada > 50:
            desconto = valor_total * 0.25

        valor_total -= desconto

        print(f"\nnome do produto comprado: {nome_produto}")
        print(f"valor total a ser pago: R$ {valor_total:.2f}")



            
