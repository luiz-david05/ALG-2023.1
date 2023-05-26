def main():
    s, t, f = map(int, input().split())

    print((s + t + f) % 24)


if __name__ == '__main__':
    main()