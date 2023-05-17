def main():
    s = 0

    for i in range(1, 40, 2):
        s += i / (2 ** ((i - 1) / 2))

    print(f'{s:.2f}')


if __name__ == "__main__":
    main()