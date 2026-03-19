from password_utils import generate_password, check_strength


def test_generate_password_length():
    password = generate_password(10)
    assert len(password) == 10


def test_generate_password_with_digits():
    password = generate_password(10, use_digits=True)
    assert any(c.isdigit() for c in password)


def test_generate_password_without_digits():
    password = generate_password(10, use_digits=False)
    assert not any(c.isdigit() for c in password)


def test_check_strength():
    assert check_strength("abc") == "Слабкий"
    assert check_strength("abcdefgh") == "Середній"
    assert check_strength("Abc123!@#xyz") == "Сильний"
