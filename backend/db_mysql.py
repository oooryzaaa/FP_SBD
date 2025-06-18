import mysql.connector

# [SYSTEM] Koneksi ke MySQL untuk data relasional seperti user, produk, order
def get_mysql_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="yourpassword",
        database="ecommerce"
    )
