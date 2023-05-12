def main():
    categoria = input()
    classe = input()
    alimentacao = input()

    animal = definir_animal(categoria, classe, alimentacao)

    print(animal)


def definir_animal(categoria, classe, alimentacao):
    animal = ''
    if categoria == "vertebrado":
        if classe == "ave":
            if alimentacao == "carnivoro":
                animal = "aguia"
            elif alimentacao == "onivoro":
                animal = "pomba"
        elif classe == "mamifero":
            if alimentacao == "onivoro":
                animal = "homem"
            elif alimentacao == "herbivoro":
                animal = "vaca"
    elif categoria == "invertebrado":
        if classe == "inseto":
            if alimentacao == "hematofago":
                animal = "pulga"
            elif alimentacao == "herbivoro":
                animal = "lagarta"
        elif classe == "anelideo":
            if alimentacao == "hematofago":
                animal = "sanguessuga"
            elif alimentacao == "onivoro":
                animal = "minhoca"

    return animal

main()
