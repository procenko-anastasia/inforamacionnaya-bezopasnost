#pip install cryptography

from cryptography.fernet import Fernet

# Генерация ключа
key = Fernet.generate_key()
cipher = Fernet(key)

# Сохранение ключа в файл
with open('key.key', 'wb') as key_file:  # 'wb' = запись в бинарном режиме
    key_file.write(key)

print("[+] Ключ сохранён в key.key")

# Шифрование файла
with open('secret.txt', 'rb') as f:
    data = f.read()

encrypted_data = cipher.encrypt(data)

with open('secret_encrypted.txt', 'wb') as f:
    f.write(encrypted_data)

print("Файл зашифрован и сохранен как 'secret_encrypted.txt'")
