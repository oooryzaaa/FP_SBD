from backend.auth import AuthSystem

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
            pass  # implementasi register
        elif choice == "2":
            pass  # login dan lanjut ke menu berdasarkan role
        elif choice == "0":
            break

if __name__ == "__main__":
    main()
