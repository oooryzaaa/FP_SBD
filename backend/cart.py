class ShoppingCart:
    # [CUSTOMER] Tambahkan produk ke keranjang
    def add_to_cart(self, customer_id, product_id, quantity):
        # Placeholder for MySQL/MongoDB insert
        if not isinstance(quantity, int) or quantity <= 0:
            return {"status": "error", "message": "Invalid quantity"}
        if customer_id not in self.cart_items:
            self.cart_items[customer_id] = []
        self.cart_items[customer_id].append({"product_id": product_id, "quantity": quantity})
        return {"status": "success", "message": "Item added to cart"}

    # [CUSTOMER] Melihat isi keranjang belanja
    def view_cart(self, customer_id):
        # Placeholder for MySQL/MongoDB select
        cart = self.cart_items.get(customer_id, [])
        return [{"product_id": item["product_id"], "quantity": item["quantity"]} for item in cart]

    # [CUSTOMER] Menghapus produk dari keranjang
    def remove_from_cart(self, customer_id, product_id):
        # Placeholder for MySQL/MongoDB delete
        if customer_id in self.cart_items:
            self.cart_items[customer_id] = [item for item in self.cart_items[customer_id] if item["product_id"] != product_id]
            if not self.cart_items[customer_id]:
                del self.cart_items[customer_id]
        return {"status": "success", "message": "Item removed from cart"}

    # [CUSTOMER] Checkout produk yang ada di keranjang
    def checkout(self, customer_id, payment_info):
        # Placeholder for MySQL/MongoDB transaction
        from datetime import date
        if customer_id not in self.cart_items or not self.cart_items[customer_id]:
            return {"status": "error", "message": "Cart is empty"}
        items = self.cart_items[customer_id]
        total_price = sum(item["quantity"] for item in items)  # Simplified total, adjust with product prices later
        order_data = {
            "user_id": customer_id,
            "order_date": date.today(),
            "total_price": total_price,
            "order_status": "pending"
        }
        # Simulate order creation
        del self.cart_items[customer_id]
        return {"status": "success", "data": {"order": order_data, "payment_info": payment_info}}

    def __init__(self):
        self.cart_items = {}

cart = ShoppingCart()
