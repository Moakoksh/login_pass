import random
import string

def generate_random_string(length):
    """Генерирует случайную строку заданной длины"""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def generate_random_password(length):
    """Генерирует случайный пароль заданной длины"""
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def generate_random_login(prefix, length):
    """Генерирует случайный логин с префиксом заданной длины"""
    characters = string.ascii_letters + string.digits
    suffix_length = length - len(prefix)
    suffix = ''.join(random.choice(characters) for _ in range(suffix_length))
    return prefix + suffix

# Пример использования программы
password_length = 8
login_length = 10

random_password = generate_random_password(password_length)
random_login = generate_random_login("user_", login_length)

print("Случайный пароль:", random_password)
print("Случайный логин:", random_login)
