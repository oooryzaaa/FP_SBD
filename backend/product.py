class ProductManager:
    def __init__(self):
        self.products = []
        self.next_id = 1

    def add_product(self, seller_id, name, description, price, stock, category_id, catalogue_id, image_path=None):
        product = {
            "id": self.next_id,
            "seller_id": seller_id,
            "name": name,
            "description": description,
            "price": price,
            "stock": stock,
            "category_id": category_id,
            "catalogue_id": catalogue_id,
            "image": image_path
        }
        self.products.append(product)
        self.next_id += 1
        print(f"Produk '{name}' berhasil ditambahkan.")
        return product

    def edit_product(self, product_id, updated_data):
        for product in self.products:
            if product["id"] == product_id:
                product.update(updated_data)
                print(f"Produk ID {product_id} berhasil diperbarui.")
                return product
        print(f"Produk ID {product_id} tidak ditemukan.")
        return None

    def delete_product(self, product_id):
        for i, product in enumerate(self.products):
            if product["id"] == product_id:
                del self.products[i]
                print(f"Produk ID {product_id} berhasil dihapus.")
                return True
        print(f"Produk ID {product_id} tidak ditemukan.")
        return False

    def get_product_by_id(self, product_id):
        for product in self.products:
            if product["id"] == product_id:
                return product
        return None

    def search_products(self, keyword=None, category_id=None):
        results = self.products
        if keyword:
            results = [p for p in results if keyword.lower() in p["name"].lower()]
        if category_id:
            results = [p for p in results if p["category_id"] == category_id]
        return results
