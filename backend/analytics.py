class SalesAnalytics:
    def __init__(self):
        self.sales = []

    # Menambahkan data penjualan (untuk simulasi)
    def add_sale(self, product_id, seller_id, quantity, price_per_item):
        total_price = quantity * price_per_item
        self.sales.append({
            "product_id": product_id,
            "seller_id": seller_id,
            "quantity": quantity,
            "total_price": total_price
        })

    # [SELLER] Laporan penjualan seller
    def get_sales_report(self, seller_id):
        report = [s for s in self.sales if s["seller_id"] == seller_id]
        total_qty = sum(s["quantity"] for s in report)
        total_income = sum(s["total_price"] for s in report)

        print(f"Laporan Penjualan Seller ID {seller_id}")
        print(f"Total Transaksi: {len(report)}")
        print(f"Total Barang Terjual: {total_qty}")
        print(f"Total Pendapatan: Rp{total_income:,}")
        return report

    # [SYSTEM] Menampilkan produk terlaris
    def get_top_products(self, top_n=3):
        from collections import defaultdict

        product_sales = defaultdict(int)
        for s in self.sales:
            product_sales[s["product_id"]] += s["quantity"]

        # Urutkan berdasarkan jumlah terjual terbanyak
        sorted_products = sorted(product_sales.items(), key=lambda x: x[1], reverse=True)

        print(f"Top {top_n} Produk Terlaris:")
        for i, (product_id, qty) in enumerate(sorted_products[:top_n], 1):
            print(f"{i}. Produk ID {product_id} - Terjual {qty} unit")
        
        return sorted_products[:top_n]
