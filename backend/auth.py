import hashlib
from backend.db_mysql import get_mysql_connection

class AuthSystem:
    def __init__(self):
        self.conn = get_mysql_connection()
        self.cursor = self.conn.cursor()

    def _hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    # [ALL ROLES] Register user
    def register_user(self, username, password, role):
        try: 
            if role not in ["customer", "seller", "admin"]:
                print("Role tidak valid.")
                return False

            self.cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
            if self.cursor.fetchone():
                print("Username sudah digunakan.")
                return False

            hashed_pw = self._hash_password(password)
            self.cursor.execute(
                "INSERT INTO users (username, password, role) VALUES (%s, %s, %s)",
                (username, hashed_pw, role)
            )
            self.conn.commit()

            user_id = self.cursor.lastrowid

            if role == "customer":
                self.cursor.execute("INSERT INTO customer (user_id) VALUES (%s)", (user_id))
            elif role == "seller":
                self.cursor.execute("INSERT INTO sellers (user_id) VALUES (%s)", (user_id))
            print(f"User '{username}' berhasil didaftarkan sebagai {role}.")
            return True
        except Exception as e:
            self.conn.rollback()
            print(f"Terjadi kesalahan saat mendaftar user: {e}")
            return False
    # [ALL ROLES] Login
    def login_user(self, username, password):
        self.cursor.execute("SELECT password FROM users WHERE username = %s", (username,))
        result = self.cursor.fetchone()
        if not result:
            print("Username tidak ditemukan.")
            return False

        hashed_pw_input = self._hash_password(password)
        if result[0] == hashed_pw_input:
            print(f"Login berhasil. Selamat datang, {username}!")
            return True
        else:
            print("Password salah.")
            return False

    # [SELLER ONLY] Hapus user lain
    def remove_user(self, current_username, target_username):
        current_role = self.get_user_role(current_username)
        if current_role != "admin":
            print("Hanya admin yang dapat menghapus akun.")
            return False

        if current_username == target_username:
            print("Admin tidak dapat menghapus akun dirinya sendiri.")
            return False

        self.cursor.execute("SELECT * FROM users WHERE username = %s", (target_username,))
        if not self.cursor.fetchone():
            print("User yang ingin dihapus tidak ditemukan.")
            return False

        self.cursor.execute("DELETE FROM users WHERE username = %s", (target_username,))
        self.conn.commit()
        print(f"User '{target_username}' berhasil dihapus oleh admin '{current_username}'.")
        return True

    # [ALL ROLES] Ambil role user
    def get_user_role(self, username):
        self.cursor.execute("SELECT role FROM users WHERE username = %s", (username,))
        result = self.cursor.fetchone()
        return result[0] if result else None

    def close(self):
        self.cursor.close()
        self.conn.close()
