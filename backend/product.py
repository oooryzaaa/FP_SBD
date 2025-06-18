class ProductManager:
    # [SELLER]
    # Menambahkan produk baru
    def add_product(self, seller_id, name, description, price, stock, category_id):
        pass

    # [SELLER]
    # Mengedit informasi produk
    def edit_product(self, product_id, updated_data):
        pass

    # [SELLER]
    # Menghapus produk
    def delete_product(self, product_id):
        pass

    # [ALL ROLES]
    # Melihat detail produk berdasarkan ID
    def get_product_by_id(self, product_id):
        pass

    # [ALL ROLES]
    # Mencari produk berdasarkan nama/kategori
    def search_products(self, keyword=None, category_id=None):
        pass
