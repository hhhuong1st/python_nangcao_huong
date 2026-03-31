import tkinter as tk
from tkinter import ttk, messagebox

class HeThongBanHang:
    def __init__(self, root):
        self.root = root
        self.root.title("Hệ Thống Quản Lý Bán Hàng")
        self.root.geometry("1000x600")
        self.root.configure(bg="#ecf0f1")

        # Menu bên trái
        menu_frame = tk.Frame(root, bg="#16456b", width=200)
        menu_frame.pack(side="left", fill="y")
        menu_frame.pack_propagate(False)

        tk.Label(menu_frame, text="HƯƠNG", fg="white", bg="#16456b", font=("Arial", 14,"bold")).pack(pady=20)
        
        tk.Button(menu_frame, text="Khách Hàng", command=lambda: self.Show_Page("khach_hang"), fg="white", bg="#c4ad2b", font=("Arial", 12,"bold")).pack(fill="x", padx=10, pady=10)
        tk.Button(menu_frame, text="Sản Phẩm", command=lambda: self.Show_Page("san_pham"), fg="white", bg="#31a123", font=("Arial", 12,"bold")).pack(fill="x", padx=10, pady=10)
        tk.Button(menu_frame, text="Giỏ Hàng", command=lambda: self.Show_Page("gio_hang"), fg="white", bg="#a12323", font=("Arial", 12,"bold")).pack(fill="x", padx=10, pady=10)

        # Khung bên phải 
        self.container = tk.Frame(root, bg="white")
        self.container.pack(side="right", fill="both", expand=True)

       
        self.pages = {}
        self.pages["khach_hang"] = self.create_customer_page()
        self.pages["san_pham"] = self.create_product_page()
        self.pages["gio_hang"] = self.create_cart_page()
    
    
        self.Show_Page('khach_hang')

    def create_customer_page(self):
        frame = tk.Frame(self.container)
        tk.Label(frame, text="TRANG KHÁCH HÀNG", font=("Arial", 14,"bold")).pack(pady=20)

        input_frame = tk.Frame(frame, bg="#ecf0f1")
        input_frame.pack(pady=20)

        tk.Label(input_frame, text="Tên Khách Hàng:", bg="#ecf0f1").grid(row=0, column=0, padx=5)
        tk.Entry(input_frame, width=30).grid(row=0, column=1, padx=20)
        
        tk.Label(input_frame, text="Số Điện Thoại:", bg="#ecf0f1").grid(row=0, column=2, padx=5)
        tk.Entry(input_frame, width=30).grid(row=0, column=3, padx=20)

        # Buttons
        btn_frame = tk.Frame(frame, bg="#ecf0f1")
        btn_frame.pack(pady=10)
        
        tk.Button(btn_frame, text="Thêm KH", bg="#20BD61", fg="white", width=10, font=("Arial", 10,"bold")).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Sửa KH", bg="#BDB21D", fg="white", width=10, font=("Arial", 10,"bold")).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Xóa KH", bg="#BE2121", fg="white", width=10, font=("Arial", 10,"bold")).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Làm Mới", bg="#1C6DB8", fg="white", width=10, font=("Arial", 10,"bold")).pack(side="left", padx=5)

        self.create_table(frame, ["Mã KH", "Tên Khách Hàng", "Số Điện Thoại"])
        return frame
    
    def create_product_page(self):
        frame = tk.Frame(self.container)
        tk.Label(frame, text="TRANG SẢN PHẨM", font=("Arial", 14,"bold")).pack(pady=20)

        input_frame = tk.Frame(frame, bg="#ecf0f1")
        input_frame.pack(pady=20)

        tk.Label(input_frame, text="Tên Sản Phẩm:", bg="#ecf0f1").grid(row=0, column=0, padx=5)
        tk.Entry(input_frame, width=30).grid(row=0, column=1, padx=20)
        
        tk.Label(input_frame, text="Giá (VNĐ):", bg="#ecf0f1").grid(row=0, column=2, padx=5)
        tk.Entry(input_frame, width=30).grid(row=0, column=3, padx=20)

        # Buttons
        btn_frame = tk.Frame(frame, bg="#ecf0f1")
        btn_frame.pack(pady=10)
        
        tk.Button(btn_frame, text="Thêm SP", bg="#20BD61", fg="white", width=10, font=("Arial", 10,"bold")).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Sửa SP", bg="#BDB21D", fg="white", width=10, font=("Arial", 10,"bold")).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Xóa SP", bg="#BE2121", fg="white", width=10, font=("Arial", 10,"bold")).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Thêm vào giỏ", bg="#1C6DB8", fg="white", width=10, font=("Arial", 10,"bold")).pack(side="left", padx=5)

        self.create_table(frame, ["Mã SP", "Tên Sản Phẩm", "Mức giá"])
        return frame


    def create_cart_page(self):
        frame = tk.Frame(self.container)
        tk.Label(frame, text="TRANG GIỎ HÀNG", font=("Arial", 14,"bold")).pack(pady=20)

        input_frame = tk.Frame(frame, bg="#ecf0f1")
        input_frame.pack(pady=20)

        tk.Label(input_frame, text="Chọn Khách Hàng:", bg="#ecf0f1", font=("Arial", 11)).pack(side="left", padx=5)
        cbo_cart = ttk.Combobox(input_frame, width=50)
        cbo_cart['value'] = ("Khoa", "Hương", "Trang")
        cbo_cart.current(0)
        cbo_cart.pack(side="left", padx=5)

        # Buttons
        btn_frame = tk.Frame(frame, bg="#ecf0f1")
        btn_frame.pack(pady=10)
        
        tk.Button(btn_frame, text="Xóa SP", bg="#BE2121", fg="white", width=10, font=("Arial", 10,"bold")).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Làm sạch giỏ", bg="#63686D", fg="white", width=10, font=("Arial", 10,"bold")).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Thanh Toán", bg="#20BD61", fg="white", width=10, font=("Arial", 10,"bold")).pack(side="left", padx=5)


        self.create_table(frame, ["Mã SP", "Tên sản phẩm", "Đơn giá", "Số lượng", "Thành tiền"])
        
        return frame
    
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

if __name__ =="__main__":
    root = tk.Tk()
    app = HeThongBanHang(root)
    root.mainloop()