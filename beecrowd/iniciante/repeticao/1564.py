def main():
    while True:
        try:
            n = int(input())

            print("vai ter copa!" if n > 0 else "vai ter duas!")
            
        except EOFError:
            break


if __name__ == "__main__":
    main()