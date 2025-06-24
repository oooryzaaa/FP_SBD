from backend.auth import AuthSystem
from backend.dashboard_customer import DashboardCustomer

# [ENTRY POINT] Sistem utama yang akan menjalankan alur menu login/register
def main():
    auth = AuthSystem()
    while True:
        print("\n=== E-Commerce System ===")
        print("1. Register")
        print("2. Login")
        print("0. Exit")
        choice = input("Pilih menu: ")

        if choice == "1":
            print("===REGIST USER===")
            username = input("Username: ")
            password = input("Password: ")
            role = input("Role: ")
            auth.register_user(username, password, role)
        elif choice == "2":
            print("===LOGIN===")
            username = input("Username: ")
            password = input("Password: ")
            auth.login_user(username, password)
        elif choice == "0":
            break

if __name__ == "__main__":
    main()
