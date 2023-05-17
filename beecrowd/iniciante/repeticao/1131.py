def main():
    grenais = 0
    vitorias_inter = 0
    vitorias_gremio = 0
    empates = 0

    resposta = 0
    while resposta != "2":
        gols_inter, gols_gremio = map(int, input().split())
        grenais += 1

        if gols_inter > gols_gremio:
            vitorias_inter += 1
        elif gols_gremio > gols_inter:
            vitorias_gremio += 1
        else:
            empates += 1

        resposta = validar_resposta()
    
    print(f"{grenais} grenais")
    print(f"Inter:{vitorias_inter}")
    print(f"Gremio:{vitorias_gremio}")
    print(f"Empates:{empates}")
    verificar_vencedor(vitorias_inter, vitorias_gremio)


def verificar_vencedor(vitorias_inter, vitorias_gremio):
    if vitorias_inter > vitorias_gremio:
        print("Inter venceu mais")
    elif vitorias_gremio > vitorias_inter:
        print("Gremio venceu mais")
    else:
        print("Nao houve vencedor")


def validar_resposta():
    resposta = input("Novo grenal (1-sim 2-nao)\n")

    if resposta != "1" and resposta != "2":
        resposta = validar_resposta()

    return resposta
    

if __name__ == "__main__":
    main()