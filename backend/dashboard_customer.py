from backend.cart import ShoppingCart
from backend.db_mysql import get_mysql_connection

class DashboardCustomer:
    def __init__(self, customer_id, username):
        self.customer_id = customer_id
        self.username = username
        self.conn = get_mysql_connection()
        self.cursor = self.conn.cursor(dictionary = True)
        self.cart = ShoppingCart()
    def add_product(self):
        try:
            product_id = int(input("Masukkan ID product: "))
            quantity = int(input("Jumlah: "))

            result = self.cart.add_to_cart(self.customer_id, product_id, quantity)
            print(f"{result['message']}")
        except ValueError:
            print("Input harus berupa angka")
    def browse_product(self):
        keyword = input("Masukkan kata kunci produk: ").lower()
        query = """ 
            SELECT * FROM products
            WHERE LOWER(product_name) LIKE %s OR LOWER(product_description) LIKE %s
            """
        like_keyword = f"%{keyword}%"
        self.cursor.execute(query, (like_keyword, like_keyword))
        result = self.cursor.fetchall()

        print("\n===HASIL PENCARIAN===")
        if not result:
            print("Tidak ada produk")
        else :
            for product in result:
                print(f" ID: {product['product_id']}, Nama: {product['product_name']}")
                print(f" Deskripsi: {product['product_description']}")
                print(f" Harga: {product['product_price']}")
            input("Tekan Enter untuk kembali ke dashboard...")

    def show_menu(self):
        while True:
            print(f"\n===DASHBOARD CUSTOMER===")
            print(f"Halo, {self.username}!\n")
            print("1. Lihat Keranjang")
            print("2. Lihat Profil")
            print("3. Tambahkan ke Keranjang")
            print("4. Browse produk")
            print("0. Keluar")
            choice = input("Pilih menu: ")
            if choice == "1":
                self.view_cart()
            elif choice == "2":
                print("\n===PROFILE CUSTOMER===")
                print(f"Username: {self.username}")
                print(f"Customer ID: {self.customer_id}")
            elif choice =="3":
                product = input("Produk: ")
                self.add_product()
            elif choice == "4":
                self.browse_product()
            elif choice == "0":
                break
            else:
                print("Input tidak valid")
    def close(self):
        self.cursor.close()
        self.conn.close()

                
