class ProductManager:
    def __init__(self):
        self.products = []
        self.next_id = 1

    # [SELLER] Menambahkan produk baru
    def add_product(self, seller_id, name, description, price, stock, category_id):
        product = {
            "id": self.next_id,
            "seller_id": seller_id,
            "name": name,
            "description": description,
            "price": price,
            "stock": stock,
            "category_id": category_id
        }
        self.products.append(product)
        self.next_id += 1
        print(f"Produk '{name}' berhasil ditambahkan.")
        return product

    # [SELLER] Mengedit informasi produk
    def edit_product(self, product_id, updated_data):
        for product in self.products:
            if product["id"] == product_id:
                product.update(updated_data)
                print(f"Produk ID {product_id} berhasil diperbarui.")
                return product
        print(f"Produk ID {product_id} tidak ditemukan.")
        return None

    # [SELLER] Menghapus produk
    def delete_product(self, product_id):
        for i, product in enumerate(self.products):
            if product["id"] == product_id:
                del self.products[i]
                print(f"Produk ID {product_id} berhasil dihapus.")
                return True
        print(f"Produk ID {product_id} tidak ditemukan.")
        return False

    # [ALL ROLES] Melihat detail produk berdasarkan ID
    def get_product_by_id(self, product_id):
        for product in self.products:
            if product["id"] == product_id:
                return product
        return None

    # [ALL ROLES] Mencari produk berdasarkan nama/kategori
    def search_products(self, keyword=None, category_id=None):
        results = self.products
        if keyword:
            results = [p for p in results if keyword.lower() in p["name"].lower()]
        if category_id:
            results = [p for p in results if p["category_id"] == category_id]
        return results
