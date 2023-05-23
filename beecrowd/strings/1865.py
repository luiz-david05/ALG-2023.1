def main():
    t = int(input())

    for i in range(t):
        hero, force = input().split()

        print('Y' if hero == 'Thor' else 'N')


if __name__ == '__main__':
    main()  