class AuthSystem:
    # [ALL ROLES]
    # Mendaftarkan user baru dengan username, password, dan role.
    # Parameter:
    # - username (str): nama user
    # - password (str): password (akan di-hash)
    # - role (str): salah satu dari ['customer', 'seller', 'admin']
    # Return: True jika berhasil, False jika username sudah ada.
    def register_user(self, username, password, role):
        pass

    # [ALL ROLES]
    # Melakukan login user.
    # Parameter:
    # - username (str)
    # - password (str)
    # Return: True jika login berhasil, False jika gagal.
    def login_user(self, username, password):
        pass

    # [ALL ROLES]
    # Mengambil role dari user tertentu (untuk validasi akses fitur).
    # Parameter:
    # - username (str)
    # Return: role (str) → 'customer', 'seller', atau 'admin'
    def get_user_role(self, username):
        pass

