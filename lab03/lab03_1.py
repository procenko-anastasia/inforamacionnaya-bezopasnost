#pip install rsa

import rsa

# Генерация ключей
(pubkey, privkey) = rsa.newkeys(512)

# Сохранение ключей в файлы
with open('pubkey.pem', 'wb') as f:
    f.write(pubkey.save_pkcs1())

with open('privkey.pem', 'wb') as f:
    f.write(privkey.save_pkcs1())

# Шифрование файла
with open('secret.txt', 'rb') as f:
    data = f.read()

encrypted_data = rsa.encrypt(data, pubkey)

with open('secret_encrypted.txt', 'wb') as f:
    f.write(encrypted_data)

print("Файл зашифрован и сохранен как 'secret_encrypted.txt'")