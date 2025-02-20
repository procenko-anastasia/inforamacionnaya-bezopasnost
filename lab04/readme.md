Лабораторная работа №3: Атака методом полного перебора (Brute Force) на зашифрованные файлы и нагрузочное тестирование
Цель работы:
Изучить основы атаки методом полного перебора (Brute Force) на зашифрованные файлы и провести нагрузочное тестирование системы, чтобы оценить её устойчивость к таким атакам.

Часть 1: Brute Force атака на зашифрованные файлы
Теоретическая часть:
Атака методом полного перебора (Brute Force) — это метод взлома, при котором злоумышленник пытается подобрать ключ или пароль, перебирая все возможные комбинации символов. В данной работе мы рассмотрим атаку на файл, зашифрованный с использованием симметричного шифрования (AES).

Практическая часть:

Задание 1: Создание зашифрованного файла
Используйте код из лабораторной работы №1 для шифрования файла с использованием алгоритма AES. Сохраните ключ в файл key.key.

Задание 2: Реализация Brute Force атаки
Напишите скрипт для подбора ключа методом полного перебора:

```
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

```