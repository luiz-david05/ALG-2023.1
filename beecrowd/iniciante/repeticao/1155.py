def main():
    s = 0
    for i in range(1, 101):
        s += 1 / i
    
    print(f'{s:.2f}')


if __name__ == "__main__":
    main()