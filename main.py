from auth import register_user, login_user

while True:
    print("\n=== Sistem E-Commerce ===")
    print("1. Register")
    print("2. Login")
    print("0. Exit")
    choice = input("Pilih menu: ")

    if choice == "1":
        username = input("Username: ")
        password = input("Password: ")
        role = input("Role (customer/seller): ")
        register_user(username, password, role)

    elif choice == "2":
        username = input("Username: ")
        password = input("Password: ")
        login_user(username, password)

    elif choice == "0":
        break
    else:
        print("Pilihan tidak valid.")
