class WishlistManager:
    # [CUSTOMER] Menambahkan produk ke wishlist
    def add_to_wishlist(self, customer_id, product_id):
        # Placeholder for MySQL/MongoDB insert
        if product_id not in [item["item_id"] for item in self.wishlist_items.get(customer_id, [])]:
            if customer_id not in self.wishlist_items:
                self.wishlist_items[customer_id] = []
            self.wishlist_items[customer_id].append({"item_id": product_id})
            return {"status": "success", "message": "Item added to wishlist"}
        return {"status": "error", "message": "Item already in wishlist"}

    # [CUSTOMER] Melihat daftar wishlist pengguna
    def get_wishlist(self, customer_id):
        # Placeholder for MySQL/MongoDB select
        return self.wishlist_items.get(customer_id, [])

    # [CUSTOMER] Menghapus produk dari wishlist
    def remove_from_wishlist(self, customer_id, product_id):
        # Placeholder for MySQL/MongoDB delete
        if customer_id in self.wishlist_items:
            self.wishlist_items[customer_id] = [item for item in self.wishlist_items[customer_id] if item["item_id"] != product_id]
            if not self.wishlist_items[customer_id]:
                del self.wishlist_items[customer_id]
        return {"status": "success", "message": "Item removed from wishlist"}

    def __init__(self):
        self.wishlist_items = {}

wishlist = WishlistManager()
