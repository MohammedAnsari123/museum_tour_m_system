# auth.py

import hashlib

# Dummy user database (in practice, use a database like MongoDB, SQLite, etc.)
users = {
    "admin": {"password": "81dc9bdb52d04dc20036dbd8313ed055", "role": "admin"},  # 1234
    "visitor": {"password": "202cb962ac59075b964b07152d234b70", "role": "visitor"}  # 123
}

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

def authenticate(username, password):
    if username in users:
        hashed = hash_password(password)
        if users[username]["password"] == hashed:
            return users[username]["role"]
    return None
