from backend.db_mysql import get_mysql_connection
from datetime import date

class OrderManager:
    # [CUSTOMER] Buat pesanan berdasarkan keranjang
    def create_order(self, customer_id, cart_items):
        """
        cart_items: list of dict {product_id, quantity}
        """
        conn = get_mysql_connection()
        cursor = conn.cursor()

        total_price = 0
        for item in cart_items:
            cursor.execute("SELECT product_price FROM Products WHERE product_id = %s", (item["product_id"],))
            price = cursor.fetchone()[0]
            total_price += price * item["quantity"]

        cursor.execute("SELECT MAX(order_id) + 1 FROM Orders")
        new_order_id = cursor.fetchone()[0] or 1

        cursor.execute("""
            INSERT INTO Orders (order_id, user_id, order_date, total_price, order_status)
            VALUES (%s, %s, %s, %s, %s)
        """, (new_order_id, customer_id, date.today(), total_price, "Pending"))

        # Insert ke Order_Items
        cursor.execute("SELECT MAX(order_item_id) + 1 FROM Order_Items")
        next_item_id = cursor.fetchone()[0] or 1

        for item in cart_items:
            cursor.execute("SELECT product_price FROM Products WHERE product_id = %s", (item["product_id"],))
            price = cursor.fetchone()[0]

            cursor.execute("""
                INSERT INTO Order_Items (order_item_id, order_id, product_id, order_item_quantity, order_item_price_at_purchase)
                VALUES (%s, %s, %s, %s, %s)
            """, (next_item_id, new_order_id, item["product_id"], item["quantity"], price))

            # Update stok
            cursor.execute("""
                UPDATE Products SET product_stock = product_stock - %s WHERE product_id = %s
            """, (item["quantity"], item["product_id"]))

            next_item_id += 1

        conn.commit()
        conn.close()
        print("Order berhasil dibuat.")

    # [CUSTOMER] Melihat histori pesanan
    def get_order_history(self, customer_id):
        conn = get_mysql_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT order_id, order_date, total_price, order_status
            FROM Orders
            WHERE user_id = %s
            ORDER BY order_date DESC
        """, (customer_id,))

        orders = cursor.fetchall()
        conn.close()
        return orders

    # [SELLER] Menampilkan pesanan untuk seller
    def get_orders_for_seller(self, seller_id):
        conn = get_mysql_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT O.order_id, O.order_date, U.user_username, P.product_name, OI.order_item_quantity
            FROM Orders O
            JOIN Order_Items OI ON O.order_id = OI.order_id
            JOIN Products P ON OI.product_id = P.product_id
            JOIN Users U ON O.user_id = U.user_id
            WHERE P.seller_id = %s
            ORDER BY O.order_date DESC
        """, (seller_id,))

        orders = cursor.fetchall()
        conn.close()
        return orders
