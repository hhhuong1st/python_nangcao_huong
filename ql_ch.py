import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

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
        tk.Button(menu_frame, text="Hóa Đơn", command=lambda: self.Show_Page("hoa_don"), fg="white", bg="#8e44ad", font=("Arial", 12,"bold")).pack(fill="x", padx=10, pady=10)

        # Khung bên phải 
        self.container = tk.Frame(root, bg="white")
        self.container.pack(side="right", fill="both", expand=True)

       
        self.pages = {}
        self.pages["khach_hang"] = self.create_customer_page()
        self.pages["san_pham"] = self.create_product_page()
        self.pages["gio_hang"] = self.create_cart_page()
        self.pages["hoa_don"] = self.create_invoice_page()
    
    
        self.Show_Page('khach_hang')

    def create_customer_page(self):
        frame = tk.Frame(self.container)
        tk.Label(frame, text="TRANG KHÁCH HÀNG", font=("Arial", 14,"bold")).pack(pady=20)

        input_frame = tk.Frame(frame, bg="#ecf0f1")
        input_frame.pack(pady=20)

        tk.Label(input_frame, text="Tên Khách Hàng:", bg="#ecf0f1").grid(row=0, column=0, padx=5)
        self.entry_ten_kh = tk.Entry(input_frame, width=30)
        self.entry_ten_kh.grid(row=0, column=1, padx=20)
        
        tk.Label(input_frame, text="Số Điện Thoại:", bg="#ecf0f1").grid(row=0, column=2, padx=5)
        self.entry_sdt_kh = tk.Entry(input_frame, width=30)
        self.entry_sdt_kh.grid(row=0, column=3, padx=20)

        # Buttons
        btn_frame = tk.Frame(frame, bg="#ecf0f1")
        btn_frame.pack(pady=10)
        
        tk.Button(btn_frame, text="Thêm KH", command=self.them_kh, bg="#20BD61", fg="white", width=10, font=("Arial", 10,"bold")).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Sửa KH", command=self.sua_kh, bg="#BDB21D", fg="white", width=10, font=("Arial", 10,"bold")).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Xóa KH", command=self.xoa_kh, bg="#BE2121", fg="white", width=10, font=("Arial", 10,"bold")).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Làm Mới", command=self.lam_moi_kh, bg="#1C6DB8", fg="white", width=10, font=("Arial", 10,"bold")).pack(side="left", padx=5)

        self.tree_kh = self.create_table(frame, ["Mã KH", "Tên Khách Hàng", "Số Điện Thoại"])
        self.tree_kh.bind("<<TreeviewSelect>>", self.on_kh_select)
        return frame
    
    def create_product_page(self):
        frame = tk.Frame(self.container)
        tk.Label(frame, text="TRANG SẢN PHẨM", font=("Arial", 14,"bold")).pack(pady=20)

        input_frame = tk.Frame(frame, bg="#ecf0f1")
        input_frame.pack(pady=20)

        tk.Label(input_frame, text="Tên Sản Phẩm:", bg="#ecf0f1").grid(row=0, column=0, padx=5)
        self.entry_ten_sp = tk.Entry(input_frame, width=30)
        self.entry_ten_sp.grid(row=0, column=1, padx=20)
        
        tk.Label(input_frame, text="Giá (VNĐ):", bg="#ecf0f1").grid(row=0, column=2, padx=5)
        self.entry_gia_sp = tk.Entry(input_frame, width=30)
        self.entry_gia_sp.grid(row=0, column=3, padx=20)

        # Buttons
        btn_frame = tk.Frame(frame, bg="#ecf0f1")
        btn_frame.pack(pady=10)
        
        tk.Button(btn_frame, text="Thêm SP", command=self.them_sp, bg="#20BD61", fg="white", width=10, font=("Arial", 10,"bold")).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Sửa SP", command=self.sua_sp, bg="#BDB21D", fg="white", width=10, font=("Arial", 10,"bold")).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Xóa SP", command=self.xoa_sp, bg="#BE2121", fg="white", width=10, font=("Arial", 10,"bold")).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Thêm vào giỏ", command=self.them_vao_gio, bg="#1C6DB8", fg="white", width=10, font=("Arial", 10,"bold")).pack(side="left", padx=5)

        self.tree_sp = self.create_table(frame, ["Mã SP", "Tên Sản Phẩm", "Mức giá"])
        self.tree_sp.bind("<<TreeviewSelect>>", self.on_sp_select)
        return frame


    def create_cart_page(self):
        frame = tk.Frame(self.container)
        tk.Label(frame, text="TRANG GIỎ HÀNG", font=("Arial", 14,"bold")).pack(pady=20)

        input_frame = tk.Frame(frame, bg="#ecf0f1")
        input_frame.pack(pady=20)

        tk.Label(input_frame, text="Chọn Khách Hàng:", bg="#ecf0f1", font=("Arial", 11)).pack(side="left", padx=5)
        self.cbo_cart = ttk.Combobox(input_frame, width=50)
        self.cbo_cart['value'] = ("Chưa có khách hàng",)
        self.cbo_cart.current(0)
        self.cbo_cart.pack(side="left", padx=5)

        # Buttons
        btn_frame = tk.Frame(frame, bg="#ecf0f1")
        btn_frame.pack(pady=10)
        
        tk.Button(btn_frame, text="Xóa SP", command=self.xoa_sp_gio, bg="#BE2121", fg="white", width=10, font=("Arial", 10,"bold")).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Làm sạch giỏ", command=self.lam_sach_gio, bg="#63686D", fg="white", width=10, font=("Arial", 10,"bold")).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Thanh Toán", command=self.thanh_toan, bg="#20BD61", fg="white", width=10, font=("Arial", 10,"bold")).pack(side="left", padx=5)


        self.tree_gio = self.create_table(frame, ["Mã SP", "Tên sản phẩm", "Đơn giá", "Số lượng", "Thành tiền"])
        
        return frame
        
    def create_invoice_page(self):
        frame = tk.Frame(self.container)
        tk.Label(frame, text="TRANG HÓA ĐƠN", font=("Arial", 14,"bold")).pack(pady=20)
        self.tree_hd = self.create_table(frame, ["Mã HĐ", "Khách Hàng", "Sản Phẩm (SL)", "Tổng Tiền", "Thời gian"])
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
        return tree

    def Show_Page(self, page_name):
        for page in self.pages.values():
            page.pack_forget()
            
        if page_name == "gio_hang":
            self.update_cart_customers()
            
        self.pages[page_name].pack(fill="both", expand=True)

    def update_cart_customers(self):
        customers = []
        if hasattr(self, 'tree_kh'):
            for item in self.tree_kh.get_children():
                values = self.tree_kh.item(item, "values")
                customers.append(f"{values[0]} - {values[1]}")
            
        if not customers:
            self.cbo_cart['value'] = ("Chưa có khách hàng",)
            self.cbo_cart.current(0)
        else:
            self.cbo_cart['value'] = tuple(customers)
            if self.cbo_cart.get() not in customers:
                self.cbo_cart.current(0)

    # === Các hàm xử lý sự kiện ===
    def them_kh(self):
        ten = self.entry_ten_kh.get()
        sdt = self.entry_sdt_kh.get()
        if ten and sdt:
            if not sdt.isdigit():
                messagebox.showwarning("Cảnh báo", "Số điện thoại chỉ được chứa chữ số!")
                return
            ma_kh = f"KH{len(self.tree_kh.get_children()) + 1:02d}"
            self.tree_kh.insert("", "end", values=(ma_kh, ten, sdt))
            self.lam_moi_kh()
        else:
            messagebox.showwarning("Cảnh báo", "Vui lòng nhập đầy đủ thông tin Khách Hàng!")

    def on_kh_select(self, event):
        selected = self.tree_kh.selection()
        if selected:
            item = selected[0]
            values = self.tree_kh.item(item, "values")
            self.lam_moi_kh()
            self.entry_ten_kh.insert(0, values[1])
            self.entry_sdt_kh.insert(0, values[2])

    def sua_kh(self):
        selected = self.tree_kh.selection()
        if not selected:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn khách hàng để sửa!")
            return
            
        ten = self.entry_ten_kh.get()
        sdt = self.entry_sdt_kh.get()
        if ten and sdt:
            if not sdt.isdigit():
                messagebox.showwarning("Cảnh báo", "Số điện thoại chỉ được chứa chữ số!")
                return
            item = selected[0]
            ma_kh = self.tree_kh.item(item, "values")[0]
            self.tree_kh.item(item, values=(ma_kh, ten, sdt))
            messagebox.showinfo("Thành công", "Cập nhật khách hàng thành công!")
            self.lam_moi_kh()
        else:
            messagebox.showwarning("Cảnh báo", "Vui lòng nhập đầy đủ thông tin Khách Hàng!")
    
    def xoa_kh(self):
        selected = self.tree_kh.selection()
        if not selected:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn khách hàng để xóa!")
            return
        if messagebox.askyesno("Xác nhận", "Bạn có chắc muốn xóa khách hàng này?"):
            for item in selected:
                self.tree_kh.delete(item)
    
    def lam_moi_kh(self): 
        self.entry_ten_kh.delete(0, tk.END)
        self.entry_sdt_kh.delete(0, tk.END)

    def them_sp(self):
        ten = self.entry_ten_sp.get()
        gia = self.entry_gia_sp.get()
        if ten and gia:
            try:
                float(gia)
            except ValueError:
                messagebox.showwarning("Cảnh báo", "Giá sản phẩm phải là một số hợp lệ!")
                return
            ma_sp = f"SP{len(self.tree_sp.get_children()) + 1:02d}"
            self.tree_sp.insert("", "end", values=(ma_sp, ten, gia))
            self.entry_ten_sp.delete(0, tk.END)
            self.entry_gia_sp.delete(0, tk.END)
        else:
            messagebox.showwarning("Cảnh báo", "Vui lòng nhập đầy đủ thông tin Sản Phẩm!")
    def on_sp_select(self, event):
        selected = self.tree_sp.selection()
        if selected:
            item = selected[0]
            values = self.tree_sp.item(item, "values")
            self.entry_ten_sp.delete(0, tk.END)
            self.entry_gia_sp.delete(0, tk.END)
            self.entry_ten_sp.insert(0, values[1])
            self.entry_gia_sp.insert(0, values[2])

    def sua_sp(self):
        selected = self.tree_sp.selection()
        if not selected:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn sản phẩm để sửa!")
            return
            
        ten = self.entry_ten_sp.get()
        gia = self.entry_gia_sp.get()
        if ten and gia:
            try:
                float(gia)
            except ValueError:
                messagebox.showwarning("Cảnh báo", "Giá sản phẩm phải là một số hợp lệ!")
                return
            item = selected[0]
            ma_sp = self.tree_sp.item(item, "values")[0]
            self.tree_sp.item(item, values=(ma_sp, ten, gia))
            messagebox.showinfo("Thành công", "Cập nhật sản phẩm thành công!")
            self.entry_ten_sp.delete(0, tk.END)
            self.entry_gia_sp.delete(0, tk.END)
        else:
            messagebox.showwarning("Cảnh báo", "Vui lòng nhập đầy đủ thông tin Sản Phẩm!")
    
    def xoa_sp(self):
        selected = self.tree_sp.selection()
        if not selected:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn sản phẩm để xóa!")
            return
        if messagebox.askyesno("Xác nhận", "Bạn có chắc muốn xóa sản phẩm này?"):
            for item in selected:
                self.tree_sp.delete(item)
                
    def them_vao_gio(self):
        selected = self.tree_sp.selection()
        if not selected:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn sản phẩm để thêm vào giỏ!")
            return
            
        for item in selected:
            values = self.tree_sp.item(item, "values")
            ma_sp, ten_sp, gia = values[0], values[1], values[2]
            
            found_item = None
            for gio_item in self.tree_gio.get_children():
                gio_values = self.tree_gio.item(gio_item, "values")
                if gio_values[0] == ma_sp:
                    found_item = gio_item
                    break
                    
            if found_item:
                gio_values = self.tree_gio.item(found_item, "values")
                so_luong_moi = int(gio_values[3]) + 1
                try:
                    thanh_tien_moi = float(gia) * so_luong_moi
                except ValueError:
                    thanh_tien_moi = gia
                self.tree_gio.item(found_item, values=(ma_sp, ten_sp, gia, so_luong_moi, thanh_tien_moi))
            else:
                so_luong = 1
                try:
                    thanh_tien = float(gia) * so_luong
                except ValueError:
                    thanh_tien = gia
                self.tree_gio.insert("", "end", values=(ma_sp, ten_sp, gia, so_luong, thanh_tien))
                
        messagebox.showinfo("Thành công", "Đã thêm sản phẩm vào giỏ hàng!")

    def xoa_sp_gio(self):
        selected = self.tree_gio.selection()
        if not selected:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn sản phẩm trong giỏ để xóa!")
            return
        for item in selected:
            self.tree_gio.delete(item)

    def lam_sach_gio(self):
        if not self.tree_gio.get_children():
            messagebox.showinfo("Thông báo", "Giỏ hàng đang trống.")
            return
        if messagebox.askyesno("Xác nhận", "Bạn có chắc muốn làm sạch giỏ hàng?"):
            for item in self.tree_gio.get_children():
                self.tree_gio.delete(item)

    def thanh_toan(self):
        items = self.tree_gio.get_children()
        if not items:
            messagebox.showwarning("Cảnh báo", "Giỏ hàng đang trống, không thể thanh toán!")
            return
            
        total = 0
        ds_sp = []
        for item in items:
            values = self.tree_gio.item(item, "values")
            ds_sp.append(f"{values[1]} ({values[3]})") # Tên sản phẩm (Số lượng)
            try:
                total += float(values[4])
            except ValueError:
                pass
                
        khach_hang = self.cbo_cart.get()
        thoi_gian = datetime.now().strftime("%d/%m/%Y %H:%M")
        ma_hd = f"HD{len(self.tree_hd.get_children()) + 1:02d}"
        chi_tiet_sp = ", ".join(ds_sp)
        
        self.tree_hd.insert("", "end", values=(ma_hd, khach_hang, chi_tiet_sp, total, thoi_gian))
                
        messagebox.showinfo("Thanh Toán", f"Thanh toán thành công!\nTổng số tiền: {total}")
        for item in items:
            self.tree_gio.delete(item)
            
        self.Show_Page("hoa_don")

if __name__ =="__main__":
    root = tk.Tk()
    app = HeThongBanHang(root)
    root.mainloop()