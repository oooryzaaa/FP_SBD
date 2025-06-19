from bson.objectid import ObjectId

class AdminPanel:
    
    # [ADMIN] Melihat semua review yang dilaporkan
    def view_reported_reviews(self):
        print("Reported Reviews: ")
        reported_reviews = self.review_collection.find({"reported_status": True})
        for review in reported_reviews:
            print(f"{review['_id']} | {review['user']} | {review['content']}")


    # [ADMIN] Menghapus review yang dilaporkan
    def remove_review(self, review_id):
        try:
            result = self.review_collection.delete_one({"_id": ObjectId(review_id)})
            if result.deleted_count:
                print("Review berhasil dihapus")
            else:
                print("Review tidak ditemukan")
        except Exception as e:
            print("Error:", e)

    # [ADMIN] Melihat dan mengelola customer yang dilaporkan
    def view_reported_customers(self):
        self.mysql_cursor.execute("SELECT * FROM customers WHERE reported_status = 1")
        for row in self.mysql_cursor.fetchall():
            print(f"{row['customer_id']} | {row['customer_name']} | {row['customer_email']}")

    def remove_customer(self, customer_id):
        self.mysql_cursor.execute("DELETE FROM customers WHERE customer_id = %s", (customer_id))
        self.mysql_conn.commit()
        print("Customer berhasil dihapus,")

    # [ADMIN] Melihat dan mengelola seller yang dilaporkan
    def view_reported_sellers(self):
        self.mysql_cursor.execute("SELECT * FROM sellers WHERE reported_status = 1")
        for row in self.mysql_cursor.fetchall():
            print(f"{row['seller_id']} | {row['store_name']} | {row['store_email']}")

    def remove_seller(self, seller_id):
        self.mysql_cursor.execute("DELETE FROM sellers seller_id = %s", (seller_id))
        self.mysql_conn.commit()
        print("Seller berhasil dihapus,")
