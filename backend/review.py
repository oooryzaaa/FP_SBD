from backend.db_mongo import get_mongo_db
from datetime import datetime
from bson.objectid import ObjectId

class ReviewSystem:
    def __init__(self):
        self.db = get_mongo_db()
        self.review_collection = self.db["reviews"]

    # [CUSTOMER] Tambah ulasan
    def add_review(self, customer_id, product_id, rating, review_text):
        review = {
            "customer_id": customer_id,
            "product_id": product_id,
            "rating": rating,
            "text": review_text,
            "timestamp": datetime.now(),
            "reported": False
        }
        self.review_collection.insert_one(review)
        print("Review berhasil disimpan.")

    # [CUSTOMER] Lihat semua ulasan produk
    def get_reviews(self, product_id):
        reviews = self.review_collection.find({"product_id": product_id, "reported": False})
        return list(reviews)

    # [CUSTOMER] Laporkan review
    def report_review(self, review_id):
        result = self.review_collection.update_one(
            {"_id": ObjectId(review_id)},
            {"$set": {"reported": True}}
        )
        if result.modified_count:
            print("Review berhasil dilaporkan.")
        else:
            print("Review tidak ditemukan atau sudah dilaporkan.")
