def main():
    i = 0
    j = 1

    while i <= 2:
        for _ in range(3):
            if i == 0 or i == 1 or i > 1.8:
                print(f"I={i:.0f} J={j:.0f}")
            else:
                print(f"I={i:.1f} J={j:.1f}")
            j += 1
        i += 0.2
        j = 1 + i


if __name__ == "__main__":
    main()