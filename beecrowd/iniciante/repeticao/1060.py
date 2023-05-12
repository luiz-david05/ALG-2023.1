def main():
    valores = [float(input()) for _ in range(6)]

    valores_positivos = [valor for valor in valores if valor > 0]

    print(f'{len(valores_positivos)} valores positivos')
    

if __name__ == '__main__':
    main()