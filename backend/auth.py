class AuthSystem:
    # [ALL ROLES] Register user baru dengan role: customer, seller, atau admin
    def register_user(self, username, password, role):
        pass

    # [ALL ROLES] Login dan verifikasi user berdasarkan username & password
    def login_user(self, username, password):
        pass

    # [ALL ROLES] Ambil peran user (customer/seller/admin) setelah login
    def get_user_role(self, username):
        pass

    # [CUSTOMER or SELLER] Menghapus akun user yang sedang login
    def remove_account(self, user_id):
        pass
