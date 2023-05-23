def main():
    xicaras, ovos, leite = map(int, input().split())

    xicaras = xicaras // 2
    ovos = ovos // 3
    leite = leite // 5

    print(min(xicaras, ovos, leite))

if __name__ == "__main__":
    main()
    