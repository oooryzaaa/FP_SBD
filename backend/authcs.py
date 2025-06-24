import hashlib

class AuthSystem:
    def __init__(self):
        self.users = {}  # {username: {"password": ..., "role": ..., "email": ..., "user_id": ..., "user_phone": ..., "user_address": ...}}

    def _hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    # [ALL ROLES] Mendaftarkan user baru
    def register_user(self, username, password, role, email, phone, address):
        if username in self.users or role not in ['buyer', 'seller', 'admin']:
            return {"status": "error", "message": "Invalid username or role"}
        hashed_password = self._hash_password(password)
        user_id = len(self.users) + 1
        self.users[username] = {
            "password": hashed_password,
            "role": role,
            "email": email,
            "user_id": user_id,
            "user_phone": phone,
            "user_address": address
        }
        return {"status": "success", "message": "User registered", "user_id": user_id}

    # [ALL ROLES] Login user
    def login_user(self, username, password):
        if username not in self.users:
            return {"status": "error", "message": "User not found"}
        hashed_password = self._hash_password(password)
        if self.users[username]["password"] != hashed_password:
            return {"status": "error", "message": "Invalid password"}
        return {"status": "success", "message": "Login successful", "role": self.users[username]["role"], "user_id": self.users[username]["user_id"]}

    # [CUSTOMER ONLY] Menghapus user lain
    def remove_user(self, current_username, target_username):
        if current_username not in self.users or self.users[current_username]["role"] != 'buyer':
            return {"status": "error", "message": "Unauthorized or user not found"}
        if target_username not in self.users:
            return {"status": "error", "message": "Target user not found"}
        del self.users[target_username]
        return {"status": "success", "message": "User removed"}

    # [ALL ROLES] Mengambil role user
    def get_user_role(self, username):
        if username not in self.users:
            return {"status": "error", "message": "User not found"}
        return {"status": "success", "role": self.users[username]["role"]}

auth = AuthSystem()
