#pip install cryptography
from cryptography.fernet import Fernet

# Используйте тот же ключ, что и для шифрования
with open('key.key', 'rb') as f:
    key = f.read()

cipher = Fernet(key)

# Дешифрование файла
with open('secret_encrypted.txt', 'rb') as f:
    encrypted_data = f.read()

decrypted_data = cipher.decrypt(encrypted_data)

with open('secret_decrypted.txt', 'wb') as f:
    f.write(decrypted_data)

print("Файл дешифрован и сохранен как 'secret_decrypted.txt'")