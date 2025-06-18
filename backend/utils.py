import hashlib

# [SYSTEM] Hashing password dengan SHA256 sebelum disimpan ke database
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
