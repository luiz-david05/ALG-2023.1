def main():
    n = int(input())

    while n > 0:
        text = input()

        text = criptografar_texto(text)
    
        print(text)

        n -= 1


def criptografar_texto(text):
    for i in range(len(text)):
            if text[i].isalpha():
                text = text[:i] + chr(ord(text[i]) + 3) + text[i+1:]
        
    text = inverter_texto(text)
    half = metade_texto(text)

    for i in range(half, len(text)):
        text = text[:i] + chr(ord(text[i]) - 1) + text[i+1:]
    
    return text


def inverter_texto(text):
    return text[::-1]


def metade_texto(text):
     return len(text) // 2


if __name__ == '__main__':
    main()