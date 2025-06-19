import mysql.connector
from pymongo import MongoClient
from bson.objectid import ObjectId
class AdminPanel:
    def __init__(self):
        #koneksinya mysql taruh sini, tinggal ubah ubah aja
        self.mysql_conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "password",
            database = "nama database"
        )
        self.mysql_cursor = self.mysql_conn.cursor(dictionary = True)

        #koneksi mongodb taruh sini, tinggal ubah2
        self.mongo_client = MongoClient("")
        self.mongo_db = self.mongo_client["nama database"]
        self.review_collection = self.mongo_db["reviews"]


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
            print(f"{row['id']} | {row['name']} | {row['email']}")

    def remove_customer(self, customer_id):
        self.mysql_cursor.execute("DELETE FROM customers WHERE id = %s", (customer_id))
        self.mysql_conn.commit()
        print("Customer berhasil dihapus,")

    # [ADMIN] Melihat dan mengelola seller yang dilaporkan
    def view_reported_sellers(self):
        self.mysql_cursor.execute("SELECT * FROM sellers WHERE reported_status = 1")
        for row in self.mysql_cursor.fetchall():
            print(f"{row['id']} | {row['store_name']} | {row['email']}")

    def remove_seller(self, seller_id):
        self.mysql_cursor.execute("DELETE FROM customers WHERE id = %s", (seller_id))
        self.mysql_conn.commit()
        print("Seller berhasil dihapus,")

    def close(self):
        self.mysql_cursor.close()
        self.mysql_conn.close()
        self.mongo_client.close()
