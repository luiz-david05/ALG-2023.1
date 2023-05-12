def main():
    salario = float(input())

    imposto = calcular_imposto(salario)

    if imposto == 0:
        print("Isento")
    else:
        print(f"R$ {imposto:.2f}")

def calcular_imposto(salario):
    if salario <= 2000:
        return 0
    elif salario <= 3000:
        return (salario - 2000) * 0.08
    elif salario <= 4500:
        return (salario - 3000) * 0.18 + 1000 * 0.08
    else:
        return (salario - 4500) * 0.28 + 1500 * 0.18 + 1000 * 0.08
    

if __name__ == '__main__': 
    main()