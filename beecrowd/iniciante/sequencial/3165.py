def main():
    n = int(input())

    i = 1
    gemeo_menor = 0
    gemeo_maior = 0
    while i <= n:
        if eh_primo(i):
            if gemeo_menor == 0:
                gemeo_menor = i
            else:
                gemeo_maior = i

                if gemeo_maior - gemeo_menor == 2:
                    penultimo = gemeo_menor
                    ultimo = gemeo_maior

                gemeo_menor = gemeo_maior
        i += 1
        
    print(f"{penultimo} {ultimo}")
def eh_primo(n):
    if n <= 1:
        return False
    
    i = 2

    while i < n:
        if eh_multiplo(n, i):
            return False
        
        i += 1

    return True


def eh_multiplo(n1, n2): return n1 % n2 == 0


if __name__ == '__main__':
    main()