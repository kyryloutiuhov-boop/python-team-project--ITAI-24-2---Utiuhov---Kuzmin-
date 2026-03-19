from password_utils import generate_password, check_strength


def main():
    print("=== Password Generator ===")

    length = int(input("Enter password length: "))

    use_digits = input("Include digits? (y/n): ") == "y"
    use_symbols = input("Include symbols? (y/n): ") == "y"

    password = generate_password(length, use_digits, use_symbols)

    strength = check_strength(password)

    print("\nGenerated password:", password)
    print("Strength:", strength)


if __name__ == "__main__":
    main()
