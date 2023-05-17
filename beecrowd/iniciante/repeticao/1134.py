def main():
    alcool = 0
    gasolina = 0
    diesel = 0

    codigo = validar_codigo()

    while codigo != 4:
        if codigo == 1:
            alcool += 1
        elif codigo == 2:
            gasolina += 1
        elif codigo == 3:
            diesel += 1

        codigo = validar_codigo()
    
    print("MUITO OBRIGADO")
    print(f"Alcool: {alcool}")
    print(f"Gasolina: {gasolina}")
    print(f"Diesel: {diesel}")


def validar_codigo():
    codigo = int(input())

    if codigo != 1 and codigo != 2 and codigo != 3 and codigo != 4:
        codigo = validar_codigo()

    return codigo

    
if __name__ == "__main__":
    main()
