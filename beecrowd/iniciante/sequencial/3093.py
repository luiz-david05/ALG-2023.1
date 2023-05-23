def main():
    n = int(input())

    for i in range(n):
        string = input()
        
        if "Q" in string and "J" in string and "K" in string and "A" in string:
            print("Aaah muleke")
        else:
            print("Ooo raca viu")


if __name__ == '__main__':
    main()