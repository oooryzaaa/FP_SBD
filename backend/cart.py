class ShoppingCart:
    # [CUSTOMER] Tambahkan produk ke keranjang
    def add_to_cart(self, customer_id, product_id, quantity):
        # Placeholder for MySQL/MongoDB insert
        if customer_id not in self.cart_items:
            self.cart_items[customer_id] = []
        self.cart_items[customer_id].append({"item_id": product_id, "quantity": quantity})
        return {"status": "success", "message": "Item added to cart"}

    # [CUSTOMER] Melihat isi keranjang belanja
    def view_cart(self, customer_id):
        # Placeholder for MySQL/MongoDB select
        return self.cart_items.get(customer_id, [])

    # [CUSTOMER] Menghapus produk dari keranjang
    def remove_from_cart(self, customer_id, product_id):
        # Placeholder for MySQL/MongoDB delete
        if customer_id in self.cart_items:
            self.cart_items[customer_id] = [item for item in self.cart_items[customer_id] if item["item_id"] != product_id]
            if not self.cart_items[customer_id]:
                del self.cart_items[customer_id]
        return {"status": "success", "message": "Item removed from cart"}

    # [CUSTOMER] Checkout produk yang ada di keranjang
    def checkout(self, customer_id, payment_info):
        # Placeholder for MySQL/MongoDB transaction
        if customer_id not in self.cart_items or not self.cart_items[customer_id]:
            return {"status": "error", "message": "Cart is empty"}
        result = {"items": self.cart_items[customer_id], "total": sum(item["quantity"] for item in self.cart_items[customer_id]), "payment_info": payment_info}
        del self.cart_items[customer_id]
        return {"status": "success", "data": result}

    def __init__(self):
        self.cart_items = {}

cart = ShoppingCart()
