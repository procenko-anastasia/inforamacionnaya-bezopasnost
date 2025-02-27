# Согласованные параметры
p = 23  # Простое число
g = 5   # Генератор

# Секретные ключи
a = 6   # Секретный ключ Алисы
b = 15  # Секретный ключ Боба

# Вычисление открытых ключей
A = (g ** a) % p  # Открытый ключ Алисы
B = (g ** b) % p  # Открытый ключ Боба
print(f"Открытый ключ Алисы: {A}")
print(f"Открытый ключ Боба: {B}")

# Вычисление общего ключа
K_alice = (B ** a) % p  # Общий ключ Алисы
K_bob = (A ** b) % p    # Общий ключ Боба

print(f"Общий ключ Алисы: {K_alice}")
print(f"Общий ключ Боба: {K_bob}")