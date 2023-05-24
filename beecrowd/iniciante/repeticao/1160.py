def main():
    n = int(input())

    for i in range(n):
        pa, pb, g1, g2 = map(float, input().split())

        anos = 0
    
        while pa <= pb:
            pa += int(pa * (g1 / 100))
            pb += int(pb * (g2 / 100))
            anos += 1

            if anos > 100:
                break

        print(f'{anos} anos.' if anos <= 100 else 'Mais de 1 seculo.')

    

if __name__ == '__main__':
    main()