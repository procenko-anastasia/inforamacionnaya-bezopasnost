import hashlib

def calculate_hash(data, algorithm='sha256'):
    if algorithm == 'sha256':
        hash_object = hashlib.sha256(data.encode())
    elif algorithm == 'md5':
        hash_object = hashlib.md5(data.encode())
    else:
        raise ValueError("Unsupported algorithm")
    return hash_object.hexdigest()

# Пример использования
data = "Hello, Information Security!"
sha256_hash = calculate_hash(data, 'sha256')
md5_hash = calculate_hash(data, 'md5')

print(f"SHA-256: {sha256_hash}")
print(f"MD5: {md5_hash}")