# Dashboard.py
from getpass import getpass
from auth_system import AuthSystem
from product_manager import ProductManager
from sales_analytics import SalesAnalytics

auth = AuthSystem()
product_manager = ProductManager()
analytics = SalesAnalytics()


def register():
    print("\n== REGISTER ==")
    username = input("Username: ")
    password = getpass("Password: ")
    role = input("Role (buyer/seller/admin): ").lower()
    auth.register_user(username, password, role)


def login():
    print("\n== LOGIN ==")
    username = input("Username: ")
    password = getpass("Password: ")
    if auth.login_user(username, password):
        return username
    return None


def buyer_menu(username):
    while True:
        print(f"\n👤 [Buyer: {username}]")
        print("1. Cari Produk")
        print("0. Logout")
        choice = input("Pilih: ")
        if choice == "1":
            keyword = input("Masukkan nama produk: ")
            results = product_manager.search_products(keyword=keyword)
            for p in results:
                print(f"- {p['name']} | Stok: {p['stock']} | Harga: {p['price']}")
        elif choice == "0":
            break


def seller_menu(username):
    while True:
        print(f"\n🛍️ [Seller: {username}]")
        print("1. Tambah Produk")
        print("2. Edit Produk")
        print("3. Hapus Produk")
        print("4. Laporan Penjualan")
        print("5. Hapus Buyer")
        print("6. Top Produk Terlaris")
        print("0. Logout")
        choice = input("Pilih: ")

        if choice == "1":
            name = input("Nama produk: ")
            desc = input("Deskripsi: ")
            price = int(input("Harga: "))
            stock = int(input("Stok: "))
            category_id = int(input("ID Kategori: "))
            catalogue_id = int(input("ID Katalog: "))
            product_manager.add_product(username, name, desc, price, stock, category_id, catalogue_id)
        elif choice == "2":
            pid = int(input("ID Produk: "))
            updated = {}
            if input("Ubah nama? (y/n): ") == "y":
                updated["name"] = input("Nama baru: ")
            if input("Ubah harga? (y/n): ") == "y":
                updated["price"] = int(input("Harga baru: "))
            product_manager.edit_product(pid, updated)
        elif choice == "3":
            pid = int(input("ID Produk: "))
            product_manager.delete_product(pid)
        elif choice == "4":
            analytics.get_sales_report(username)
        elif choice == "5":
            target = input("Username buyer yang ingin dihapus: ")
            auth.remove_user(username, target)
        elif choice == "6":
            analytics.get_top_products()
        elif choice == "0":
            break


def admin_menu(username):
    print(f"\n🛡️ [Admin: {username}]")
    print("Fitur admin belum tersedia 😅")


def main():
    while True:
        print("\n==== DASHBOARD UTAMA ====")
        print("1. Register")
        print("2. Login")
        print("0. Keluar")
        cmd = input("Pilih: ")

        if cmd == "1":
            register()
        elif cmd == "2":
            username = login()
            if username:
                role = auth.get_user_role(username)
                if role == "buyer":
                    buyer_menu(username)
                elif role == "seller":
                    seller_menu(username)
                elif role == "admin":
                    admin_menu(username)
        elif cmd == "0":
            print("Sampai jumpa!")
            break


if __name__ == "__main__":
    main()
