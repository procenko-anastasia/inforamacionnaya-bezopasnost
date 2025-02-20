from cryptography.fernet import Fernet
import itertools
import string

# Загрузка зашифрованного файла
with open('secret_encrypted.txt', 'rb') as f:
    encrypted_data = f.read()

# Функция для генерации всех возможных комбинаций
def generate_keys(length):
    chars = string.ascii_letters + string.digits  # Используем буквы и цифры
    for combination in itertools.product(chars, repeat=length):
        yield ''.join(combination).encode()

# Функция для подбора ключа
def brute_force(encrypted_data, max_length=5):
    for length in range(1, max_length + 1):
        for key in generate_keys(length):
            try:
                cipher = Fernet(key)
                decrypted_data = cipher.decrypt(encrypted_data)
                print(f"Ключ найден: {key.decode()}")
                print(f"Расшифрованные данные: {decrypted_data.decode()}")
                return
            except:
                continue
    print("Ключ не найден.")

# Запуск Brute Force атаки
brute_force(encrypted_data)