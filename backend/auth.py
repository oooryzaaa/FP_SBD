# fitur khusus seller yaitu remove user
import hashlib

class AuthSystem:
    def __init__(self):
        self.users = {}  # format: {username: {"password": hashed_pw, "role": role}}

    def _hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    # [ALL ROLES] Mendaftarkan user baru
    def register_user(self, username, password, role):
        if username in self.users:
            print("Username sudah digunakan.")
            return False
        if role not in ["customer", "seller", "admin"]:
            print("Role tidak valid.")
            return False
        hashed_pw = self._hash_password(password)
        self.users[username] = {"password": hashed_pw, "role": role}
        print(f"User '{username}' berhasil didaftarkan sebagai {role}.")
        return True

    # [ALL ROLES] Login user
    def login_user(self, username, password):
        if username not in self.users:
            print("Username tidak ditemukan.")
            return False
        hashed_pw = self._hash_password(password)
        if self.users[username]["password"] == hashed_pw:
            print(f"Login berhasil. Selamat datang, {username}!")
            return True
        else:
            print("Password salah.")
            return False

    # [SELLER ONLY] Menghapus akun user lain
    def remove_user(self, current_username, target_username):
        current_role = self.get_user_role(current_username)
        if current_role != "seller":
            print("Hanya seller yang dapat menghapus akun.")
            return False
        if target_username not in self.users:
            print("User yang ingin dihapus tidak ditemukan.")
            return False
        if target_username == current_username:
            print("Seller tidak dapat menghapus akun dirinya sendiri.")
            return False
        del self.users[target_username]
        print(f"User '{target_username}' berhasil dihapus oleh seller '{current_username}'.")
        return True

    # [ALL ROLES] Mengambil role user
    def get_user_role(self, username):
        if username in self.users:
            return self.users[username]["role"]
        return None
