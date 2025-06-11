from db_config import connect_db
import mysql.connector  
from db_config import connect_db

def register_user(username, password, role):
    db = connect_db()
    cursor = db.cursor()

    try:
        query = "INSERT INTO users (username, password_hash, role) VALUES (%s, %s, %s)"
        cursor.execute(query, (username, password, role))
        db.commit()
        print("✅ Registrasi berhasil.")
    except mysql.connector.IntegrityError:
        print("⚠️ Username sudah digunakan.")
    finally:
        cursor.close()
        db.close()

def login_user(username, password):
    db = connect_db()
    cursor = db.cursor()

    query = "SELECT role FROM users WHERE username=%s AND password_hash=%s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()

    cursor.close()
    db.close()

    if result:
        print(f"✅ Login berhasil sebagai {result[0]}")
        return result[0]
    else:
        print("❌ Login gagal. Username atau password salah.")
        return None
