import tkinter as tk
from tkinter import ttk, messagebox

class HeThongBanHang:
    def __init__(self, root):
        self.root = root
        self.root.title("Hệ Thống Quản Lý Bán Hàng")
        self.root.geometry("1100x700")
        self.root.configure(bg="#ecf0f1")

        # --- Menu bên trái ---
        menu_frame = tk.Frame(root, bg="#16456b", width=200)
        menu_frame.pack(side="left", fill="y")
        menu_frame.pack_propagate(False)

        tk.Label(menu_frame, text="HƯƠNG", fg="white", bg="#16456b", font=("Arial", 16, "bold")).pack(pady=30)
        
        btn_style = {"fg": "white", "font": ("Arial", 11, "bold"), "bd": 0, "cursor": "hand2"}
        tk.Button(menu_frame, text="👥 Khách Hàng", command=lambda: self.Show_Page("khach_hang"), bg="#c4ad2b", **btn_style).pack(fill="x", padx=10, pady=10)
        tk.Button(menu_frame, text="📦 Sản Phẩm", command=lambda: self.Show_Page("san_pham"), bg="#31a123", **btn_style).pack(fill="x", padx=10, pady=10)
        tk.Button(menu_frame, text="🛒 Giỏ Hàng", command=lambda: self.Show_Page("gio_hang"), bg="#a12323", **btn_style).pack(fill="x", padx=10, pady=10)
        tk.Button(menu_frame, text="📄 Hóa Đơn", command=lambda: self.Show_Page("hoa_don"), bg="#1c5888", **btn_style).pack(fill="x", padx=10, pady=10)

        # --- Khung container bên phải ---
        self.container = tk.Frame(root, bg="#ecf0f1")
        self.container.pack(side="right", fill="both", expand=True)

        self.pages = {}
        self.pages["khach_hang"] = self.create_customer_page()
        self.pages["san_pham"] = self.create_product_page()
        self.pages["gio_hang"] = self.create_cart_page()
        self.pages["hoa_don"] = self.create_invoice_page()

        self.Show_Page('khach_hang')

    # --- 1. Trang Khách Hàng ---
    def create_customer_page(self):
        frame = tk.Frame(self.container, bg="#ecf0f1")
        
        # Input fields
        input_frame = tk.Frame(frame, bg="#ecf0f1")
        input_frame.pack(pady=20)
        
        tk.Label(input_frame, text="Tên Khách Hàng:", bg="#ecf0f1").grid(row=0, column=0, padx=5)
        tk.Entry(input_frame, width=30).grid(row=0, column=1, padx=20)
        
        tk.Label(input_frame, text="Số Điện Thoại:", bg="#ecf0f1").grid(row=0, column=2, padx=5)
        tk.Entry(input_frame, width=30).grid(row=0, column=3, padx=20)

        # Buttons
        btn_frame = tk.Frame(frame, bg="#ecf0f1")
        btn_frame.pack(pady=10)
        
        tk.Button(btn_frame, text="Thêm KH", bg="#2ecc71", fg="white", width=10).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Sửa KH", bg="#f1c40f", fg="white", width=10).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Xóa KH", bg="#e74c3c", fg="white", width=10).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Làm Mới", bg="#3498db", fg="white", width=10).pack(side="left", padx=5)

        # Table
        self.create_table(frame, ["Mã KH", "Tên Khách Hàng", "Số Điện Thoại"])
        return frame

    # --- 2. Trang Sản Phẩm ---
    def create_product_page(self):
        frame = tk.Frame(self.container, bg="#ecf0f1")
        
        input_frame = tk.Frame(frame, bg="#ecf0f1")
        input_frame.pack(pady=20)
        
        tk.Label(input_frame, text="Tên SP:", bg="#ecf0f1").grid(row=0, column=0, padx=5)
        tk.Entry(input_frame, width=30).grid(row=0, column=1, padx=20)
        
        tk.Label(input_frame, text="Giá (VNĐ):", bg="#ecf0f1").grid(row=0, column=2, padx=5)
        tk.Entry(input_frame, width=30).grid(row=0, column=3, padx=20)

        btn_frame = tk.Frame(frame, bg="#ecf0f1")
        btn_frame.pack(pady=10)
        
        tk.Button(btn_frame, text="Thêm SP", bg="#2ecc71", fg="white", width=10).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Sửa SP", bg="#f1c40f", fg="white", width=10).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Xóa SP", bg="#e74c3c", fg="white", width=10).pack(side="left", padx=5)
        tk.Button(btn_frame, text="🛒 Thêm vào Giỏ", bg="#3498db", fg="white", width=15).pack(side="left", padx=5)

        self.create_table(frame, ["Mã SP", "Tên Sản Phẩm", "Mức Giá (VNĐ)"])
        return frame

    # --- 3. Trang Giỏ Hàng ---
    def create_cart_page(self):
        frame = tk.Frame(self.container, bg="#ecf0f1")
        
        top_frame = tk.Frame(frame, bg="#ecf0f1")
        top_frame.pack(pady=20)
        
        tk.Label(top_frame, text="👤 Chọn Khách Hàng:", bg="#ecf0f1", font=("Arial", 11)).pack(side="left", padx=5)
        combo = ttk.Combobox(top_frame, width=50)
        combo['values'] = ("1 - Khách Vãng Lai - 0000000000")
        combo.current(0)
        combo.pack(side="left", padx=5)

        btn_frame = tk.Frame(frame, bg="#ecf0f1")
        btn_frame.pack(pady=10)
        
        tk.Button(btn_frame, text="X Xóa SP Đã Chọn", bg="#e74c3c", fg="white").pack(side="left", padx=10)
        tk.Button(btn_frame, text="🧹 Làm Sạch Giỏ", bg="#7f8c8d", fg="white").pack(side="left", padx=10)
        tk.Button(btn_frame, text="✅ THANH TOÁN", bg="#27ae60", fg="white", font=("Arial", 10, "bold")).pack(side="left", padx=10)

        self.create_table(frame, ["Mã SP", "Tên sản phẩm", "Đơn giá", "Số lượng", "Thành tiền"])
        return frame

    # --- 4. Trang Hóa Đơn ---
    def create_invoice_page(self):
        frame = tk.Frame(self.container, bg="#ecf0f1")
        
        # Danh sách hóa đơn
        lb1 = tk.LabelFrame(frame, text="Danh sách Hóa Đơn đã bán", bg="#ecf0f1")
        lb1.pack(fill="both", expand=True, padx=10, pady=10)
        self.create_table(lb1, ["Mã HĐ", "Khách Hàng", "Ngày Giờ Tạo", "Tổng Tiền"])

        # Chi tiết sản phẩm
        lb2 = tk.LabelFrame(frame, text="Chi tiết Sản phẩm", bg="#ecf0f1")
        lb2.pack(fill="both", expand=True, padx=10, pady=10)
        self.create_table(lb2, ["Tên Sản Phẩm", "Số Lượng", "Đơn Giá", "Thành Tiền"])
        
        return frame

    # --- Hàm bổ trợ tạo bảng ---
    def create_table(self, parent, columns):
        table_frame = tk.Frame(parent)
        table_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        tree = ttk.Treeview(table_frame, columns=columns, show="headings")
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor="center", width=120)
        
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        
        tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def Show_Page(self, page_name):
        for page in self.pages.values():
            page.pack_forget()
        self.pages[page_name].pack(fill="both", expand=True)

if __name__ == "__main__":
    root = tk.Tk()
    # Tuỳ chỉnh style cho Treeview để giống ảnh hơn
    style = ttk.Style()
    style.configure("Treeview.Heading", font=("Arial", 10, "bold"))
    style.configure("Treeview", rowheight=25)
    
    app = HeThongBanHang(root)
    root.mainloop()