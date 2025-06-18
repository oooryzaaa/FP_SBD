class CategoryManager:
    # [ADMIN / SYSTEM]
    # Menambahkan kategori baru ke dalam database.
    # Parameter:
    # - name (str): nama kategori yang akan ditambahkan.
    # Return: True jika berhasil, False jika nama sudah ada.
    def add_category(self, name):
        pass

    # [ALL ROLES]
    # Mengambil semua kategori produk yang tersedia di sistem.
    # Tidak menerima parameter.
    # Return: List of dicts berisi kategori produk, contoh:
    # [{'id': 1, 'name': 'Pakaian'}, {'id': 2, 'name': 'Elektronik'}, ...]
    def get_all_categories(self):
        pass

    # [ADMIN]
    # Menghapus kategori dari sistem.
    # Parameter:
    # - name (str): nama kategori yang akan dihapus.
    # Return: True jika berhasil, False jika kategori tidak ditemukan.
    def remove_category(self, name):
        pass
