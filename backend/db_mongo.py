from pymongo import MongoClient

# [SYSTEM] Koneksi ke MongoDB untuk data non-relasional seperti review & log
def get_mongo_connection():
    client = MongoClient("mongodb://localhost:27017/")
    return client["ecommerce"]
