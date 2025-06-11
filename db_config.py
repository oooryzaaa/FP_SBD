import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",         # Ganti dengan password MySQL-mu
        database="fpsbd"     # Sesuaikan dengan nama DB-mu
    )
