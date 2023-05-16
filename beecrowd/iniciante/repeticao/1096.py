def main():
    i = 1
    j = 7
    
    while i <= 9:
        print(f'I={i} J={j}')
        j -= 1
        if j == 4:
            i += 2
            j = 7


if __name__ == '__main__':
    main()