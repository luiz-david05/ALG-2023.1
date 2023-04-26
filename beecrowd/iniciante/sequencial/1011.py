def main():
    raio = float(input())
    
    pi = 3.14159

    volume = calcular_volume(raio, pi)

    print(f"VOLUME = {volume:.3f}")


def calcular_volume(raio, pi):
    return (4 / 3) * pi * raio ** 3


if __name__ == "__main__":
   main()

    # with open("1011.txt" , "r") as entrada:
    #   raio = float(entrada.readline())