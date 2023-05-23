def main():
    n = int(input())

    for i in range(n):
        pessoas = int(input())

        for j in range(pessoas):
            idioma = input()

            if j == 0:
                idioma_final = idioma

            if idioma_final != idioma:
                idioma_final = "ingles"

        print(idioma_final)
    
if __name__ == "__main__":
    main()