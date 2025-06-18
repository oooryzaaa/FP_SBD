class AuthSystem:
    # [ALL ROLES]
    # Mendaftarkan user baru ke sistem
    # Parameters:
    # - username: str
    # - password: str (akan di-hash)
    # - role: str (customer, seller, admin)
    # Returns: bool (True jika sukses, False jika username sudah digunakan)
    def register_user(self, username, password, role):
        pass

    # [ALL ROLES]
    # Login user ke sistem
    # Parameters:
    # - username: str
    # - password: str
    # Returns: bool (True jika sukses, False jika gagal)
    def login_user(self, username, password):
        pass

    # [ALL ROLES]
    # Menghapus akun user
    # Parameters:
    # - username: str
    # Returns: bool
    def remove_user(self, username):
        pass

    # [ALL ROLES]
    # Mengambil role user
    # Parameters:
    # - username: str
    # Returns: str (role user)
    def get_user_role(self, username):
        pass
