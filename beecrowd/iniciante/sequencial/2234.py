def main():
    hot_dogs, participants = map(int, input().split())

    media = calculate_media(hot_dogs, participants)

    print(f"{media:.2f}")


def calculate_media(hot_dogs, participants):
    return hot_dogs / participants


if __name__ == '__main__':
    main()