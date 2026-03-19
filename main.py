from password_utils import generate_password, check_strength


def main():
    print("=== Password Generator ===")

    length = int(input("Введіть довжину пароля: "))

    use_digits = input("Буде мати цифри? (так/ні): ") == "так"
    use_symbols = input("Буде мати спеціальні символи? (так/ні): ") == "так"

    password = generate_password(length, use_digits, use_symbols)

    strength = check_strength(password)

    print("\nЗгенерований пароль:", password)
    print("Довжина:", strength)


if __name__ == "__main__":
    main()
