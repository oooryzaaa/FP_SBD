from auth import register_user, login_user

def menu_customer(user_id):
    print(f"\n[Customer Menu] (User ID: {user_id})")
    

def menu_seller(user_id):
    print(f"\n[Seller Menu] (User ID: {user_id})")
    

def menu_admin(user_id):
    print(f"\n[Admin Menu] (User ID: {user_id})")
    

while True:
    print("\n=== Sistem E-Commerce ===")
    print("1. Register")
    print("2. Login")
    print("0. Exit")
    choice = input("Pilih menu: ")

    if choice == "1":
        username = input("Username: ")
        password = input("Password: ")
        role = input("Role (buyer/seller/admin): ").lower()
        if role not in ['buyer', 'seller', 'admin']:
            print("Role tidak valid.")
            continue
        register_user(username, password, role)

    elif choice == "2":
        username = input("Username: ")
        password = input("Password: ")
        user_id, role = login_user(username, password)
        if user_id:
            if role == "buyer":
                menu_customer(user_id)
            elif role == "seller":
                menu_seller(user_id)
            elif role == "admin":
                menu_admin(user_id)
            else:
                print("Role tidak dikenali.")

    elif choice == "0":
        break
    else:
        print("Pilihan tidak valid.")
