import random
import string


def generate_password(length: int, use_digits=True, use_symbols=True) -> str:

    characters = string.ascii_letters

    if use_digits:
        characters += string.digits

    if use_symbols:
        characters += "!@#$%^&*()"

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def check_strength(password: str) -> str:

    length = len(password)

    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in "!@#$%^&*()" for c in password)

    if length >= 12 and has_digit and has_symbol:
        return "Сильний"
    elif length >= 8:
        return "Середній"
    else:
        return "Слабкий"

