def main():
    t = int(input())

    for i in range(1, t + 1):
        sheldon, raj = input().split()
        
        if sheldon == raj:
            print(f"Caso #{i}: De novo!")
        elif sheldon == "tesoura" and raj == "papel":
            print(f"Caso #{i}: Bazinga!")
        elif sheldon == "papel" and raj == "pedra":
            print(f"Caso #{i}: Bazinga!")
        elif sheldon == "pedra" and raj == "lagarto":
            print(f"Caso #{i}: Bazinga!")
        elif sheldon == "lagarto" and raj == "Spock":
            print(f"Caso #{i}: Bazinga!")
        elif sheldon == "Spock" and raj == "tesoura":
            print(f"Caso #{i}: Bazinga!")
        elif sheldon == "tesoura" and raj == "lagarto":
            print(f"Caso #{i}: Bazinga!")
        elif sheldon == "lagarto" and raj == "papel":
            print(f"Caso #{i}: Bazinga!")
        elif sheldon == "papel" and raj == "Spock":
            print(f"Caso #{i}: Bazinga!")
        elif sheldon == "Spock" and raj == "pedra":
            print(f"Caso #{i}: Bazinga!")
        elif sheldon == "pedra" and raj == "tesoura":
            print(f"Caso #{i}: Bazinga!")
        else:
            print(f"Caso #{i}: Raj trapaceou!")


if __name__ == "__main__":
    main()
            