import rsa

# Загрузка закрытого ключа
with open('privkey.pem', 'rb') as f:
    privkey = rsa.PrivateKey.load_pkcs1(f.read())

# Дешифрование файла
with open('secret_encrypted.txt', 'rb') as f:
    encrypted_data = f.read()

decrypted_data = rsa.decrypt(encrypted_data, privkey)

with open('secret_decrypted.txt', 'wb') as f:
    f.write(decrypted_data)

print("Файл дешифрован и сохранен как 'secret_decrypted.txt'")