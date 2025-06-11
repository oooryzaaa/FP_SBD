from db_config import connect_db

def register_user(username, password, role):
    db = connect_db()
    cursor = db.cursor()

    try:
        query = "INSERT INTO Users (user_username, user_password, user_email, user_address, user_phone, user_role) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (username, password, "email@example.com", "Default Address", "08123456789", role))
        db.commit()
        print("Registrasi berhasil.")
    except Exception as e:
        print("Registrasi gagal:", e)
    finally:
        cursor.close()
        db.close()

def login_user(username, password):
    db = connect_db()
    cursor = db.cursor()

    query = "SELECT user_id, user_role FROM Users WHERE user_username=%s AND user_password=%s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()

    cursor.close()
    db.close()

    if result:
        user_id, role = result
        print(f"Login berhasil sebagai {role}")
        return user_id, role
    else:
        print("Login gagal. Username atau password salah.")
        return None, None
