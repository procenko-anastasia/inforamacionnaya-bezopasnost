Лабораторная работа №4: Цифровая подпись (RSA, ECDSA)

Цель работы:

Изучить основы создания и проверки цифровой подписи с использованием алгоритмов RSA и ECDSA. Научиться применять цифровые подписи для обеспечения аутентичности и целостности данных.

Теоретическая часть:

Цифровая подпись — это криптографический механизм, который позволяет подтвердить подлинность и целостность данных. Она создается с использованием закрытого ключа и проверяется с помощью открытого ключа.



#!pip install cryptography - это команда для установки библиотеки cryptography, которая используется для работы с криптографическими алгоритмами.

from cryptography.hazmat.primitives import hashes - импортирует модуль hashes из библиотеки cryptography, который содержит различные хеш-функции.

from cryptography.hazmat.primitives.asymmetric import rsa, padding - импортирует модули rsa и padding из библиотеки cryptography. Модуль rsa используется для работы с алгоритмом RSA, а модуль padding - для работы с различными методами заполнения.

from cryptography.hazmat.primitives import serialization - импортирует модуль serialization из библиотеки cryptography, который используется для сериализации и десериализации ключей.

private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048) - генерирует приватный ключ RSA с экспонентой 65537 и размером ключа 2048 бит.

public_key = private_key.public_key() - создает публичный ключ из приватного ключа.

data = "Здраствуй мир!".encode('utf-8') - кодирует строку "Здраствуй мир!" в байты с использованием кодировки UTF-8.

signature = private_key.sign(data, padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH), hashes.SHA256()) - создает подпись для данных, используя приватный ключ, алгоритм подписи PSS с хеш-функцией SHA256 и максимальной длиной соли.

public_key.verify(signature, data, padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH), hashes.SHA256()) - проверяет подпись, используя публичный ключ, те же параметры подписи и данные. Если подпись верна, он выводит сообщение "Подпись верна!". Если подпись недействительна, он выводит сообщение об ошибке.