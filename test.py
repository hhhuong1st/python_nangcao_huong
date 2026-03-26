import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import sqlite3
from datetime import datetime

class HeThongBanHangApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hệ Thống Quản Lý Bán Hàng (Có Thanh Toán)")
        self.root.geometry("1000x600")
        self.root.configure(bg="#ecf0f1")

        # Biến toàn cục của ứng dụng
        self.gio_hang = {} # Lưu giỏ hàng: {ma_sp: {'ten':..., 'gia':..., 'soluong':...}}
        
        self.khoi_tao_db()
        self.tao_bo_khung_chinh()
        
        # Khởi động mở trang Sản phẩm trước
        self.hien_thi_san_pham()

    # ================= 1. CƠ SỞ DỮ LIỆU =================
    def khoi_tao_db(self):
        conn = sqlite3.connect('abc_shop.db')
        cur = conn.cursor()
        # Bảng Khách Hàng
        cur.execute('''CREATE TABLE IF NOT EXISTS KhachHang (
            id INTEGER PRIMARY KEY AUTOINCREMENT, ten_kh TEXT, sdt TEXT)''')
        # Bảng Sản Phẩm
        cur.execute('''CREATE TABLE IF NOT EXISTS SanPham (
            id INTEGER PRIMARY KEY AUTOINCREMENT, ten_sp TEXT, gia REAL)''')
        # Bảng Hóa Đơn
        cur.execute('''CREATE TABLE IF NOT EXISTS HoaDon (
            id INTEGER PRIMARY KEY AUTOINCREMENT, khach_hang_id INTEGER, tong_tien REAL, ngay_tao TEXT)''')
        # Bảng Chi Tiết Hóa Đơn
        cur.execute('''CREATE TABLE IF NOT EXISTS ChiTietHoaDon (
            id INTEGER PRIMARY KEY AUTOINCREMENT, hoa_don_id INTEGER, san_pham_id INTEGER, so_luong INTEGER, don_gia REAL, thanh_tien REAL)''')
        
        # Thêm khách vãng lai mặc định nếu chưa có
        cur.execute("SELECT COUNT(*) FROM KhachHang")
        if cur.fetchone()[0] == 0:
            cur.execute("INSERT INTO KhachHang (ten_kh, sdt) VALUES ('Khách Vãng Lai', '0000000000')")
            
        conn.commit()
        conn.close()

    # ================= 2. BỘ KHUNG GIAO DIỆN (SIDEBAR) =================
    def tao_bo_khung_chinh(self):
        # Thanh menu bên trái (Sidebar)
        self.sidebar = tk.Frame(self.root, bg="#2c3e50", width=200)
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y)
        
        tk.Label(self.sidebar, text="🛒 ABC SHOP", font=("Arial", 16, "bold"), fg="#f1c40f", bg="#2c3e50").pack(pady=30)
        
        btn_style = {"bg": "#34495e", "fg": "white", "font": ("Arial", 12), "bd": 0, "pady": 10, "activebackground": "#1abc9c", "activeforeground": "white"}
        
        tk.Button(self.sidebar, text="👥 Khách hàng", command=self.hien_thi_khach_hang, **btn_style).pack(fill=tk.X, pady=5, padx=10)
        tk.Button(self.sidebar, text="📦 Sản phẩm", command=self.hien_thi_san_pham, **btn_style).pack(fill=tk.X, pady=5, padx=10)
        tk.Button(self.sidebar, text="💳 Giỏ hàng & Thanh toán", command=self.hien_thi_gio_hang, **btn_style).pack(fill=tk.X, pady=5, padx=10)
        tk.Button(self.sidebar, text="📄 Chi tiết hóa đơn", command=self.hien_thi_hoa_don, **btn_style).pack(fill=tk.X, pady=5, padx=10)
        
        # Khu vực nội dung chính bên phải
        self.main_content = tk.Frame(self.root, bg="#ecf0f1")
        self.main_content.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    def xoa_noi_dung_cu(self):
        for widget in self.main_content.winfo_children():
            widget.destroy()

    # ================= 3. TRANG SẢN PHẨM =================
    def hien_thi_san_pham(self):
        self.xoa_noi_dung_cu()
        tk.Label(self.main_content, text="📦 QUẢN LÝ SẢN PHẨM", font=("Arial", 16, "bold"), bg="#ecf0f1", fg="#333").pack(pady=20)

        frame_nhap = tk.Frame(self.main_content, bg="#ecf0f1")
        frame_nhap.pack(pady=10)
        
        tk.Label(frame_nhap, text="Tên SP:", bg="#ecf0f1").grid(row=0, column=0, padx=5)
        self.txt_ten_sp = tk.Entry(frame_nhap, width=25)
        self.txt_ten_sp.grid(row=0, column=1, padx=5)
        
        tk.Label(frame_nhap, text="Giá (VNĐ):", bg="#ecf0f1").grid(row=0, column=2, padx=5)
        self.txt_gia_sp = tk.Entry(frame_nhap, width=20)
        self.txt_gia_sp.grid(row=0, column=3, padx=5)

        frame_nut = tk.Frame(self.main_content, bg="#ecf0f1")
        frame_nut.pack(pady=10)
        tk.Button(frame_nut, text="Thêm SP", bg="#2ecc71", fg="white", command=self.them_sp).grid(row=0, column=0, padx=5)
        tk.Button(frame_nut, text="Sửa SP", bg="#f1c40f", command=self.sua_sp).grid(row=0, column=1, padx=5)
        tk.Button(frame_nut, text="Xóa SP", bg="#e74c3c", fg="white", command=self.xoa_sp).grid(row=0, column=2, padx=5)
        tk.Button(frame_nut, text="🛒 Thêm vào Giỏ", bg="#3498db", fg="white", command=self.them_vao_gio).grid(row=0, column=3, padx=20)

        columns = ("ID", "Ten", "Gia")
        self.bang_sp = ttk.Treeview(self.main_content, columns=columns, show="headings", height=15)
        self.bang_sp.heading("ID", text="Mã SP")
        self.bang_sp.heading("Ten", text="Tên Sản Phẩm")
        self.bang_sp.heading("Gia", text="Mức Giá (VNĐ)")
        self.bang_sp.column("ID", width=50, anchor=tk.CENTER)
        self.bang_sp.column("Ten", width=400)
        self.bang_sp.column("Gia", width=150, anchor=tk.E)
        self.bang_sp.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        self.bang_sp.bind("<ButtonRelease-1>", self.chon_dong_sp)
        self.id_sp_chon = None
        self.load_data_sp()

    def load_data_sp(self):
        for row in self.bang_sp.get_children(): self.bang_sp.delete(row)
        conn = sqlite3.connect("abc_shop.db")
        for row in conn.cursor().execute("SELECT * FROM SanPham"):
            row_formatted = (row[0], row[1], f"{row[2]:,.0f}")
            self.bang_sp.insert('', tk.END, values=row_formatted)
        conn.close()

    def chon_dong_sp(self, event):
        dong = self.bang_sp.focus()
        if dong:
            gia_tri = self.bang_sp.item(dong, 'values')
            self.id_sp_chon = gia_tri[0]
            self.txt_ten_sp.delete(0, tk.END)
            self.txt_ten_sp.insert(0, gia_tri[1])
            self.txt_gia_sp.delete(0, tk.END)
            self.txt_gia_sp.insert(0, gia_tri[2].replace(",", ""))

    def them_sp(self):
        ten, gia = self.txt_ten_sp.get(), self.txt_gia_sp.get()
        if ten and gia:
            conn = sqlite3.connect('abc_shop.db')
            conn.cursor().execute("INSERT INTO SanPham (ten_sp, gia) VALUES (?, ?)", (ten, float(gia)))
            conn.commit(); conn.close()
            self.load_data_sp()
            self.txt_ten_sp.delete(0, tk.END); self.txt_gia_sp.delete(0, tk.END)

    def sua_sp(self):
        if not self.id_sp_chon:
            messagebox.showwarning("Lỗi", "Vui lòng chọn một sản phẩm trong bảng để sửa!")
            return
        ten = self.txt_ten_sp.get().strip()
        try:
            gia = float(self.txt_gia_sp.get())
        except ValueError:
            messagebox.showwarning("Lỗi", "Giá bán phải là số hợp lệ!")
            return

        conn = sqlite3.connect('abc_shop.db')
        conn.cursor().execute("UPDATE SanPham SET ten_sp=?, gia=? WHERE id=?", (ten, gia, self.id_sp_chon))
        conn.commit(); conn.close()

        self.load_data_sp()
        self.txt_ten_sp.delete(0, tk.END); self.txt_gia_sp.delete(0, tk.END)
        self.id_sp_chon = None
        messagebox.showinfo("Thành công", "Đã cập nhật thông tin sản phẩm!")

    def xoa_sp(self):
        if not self.id_sp_chon:
            messagebox.showwarning("Lỗi", "Vui lòng chọn một sản phẩm trong bảng để xóa!")
            return
        traloi = messagebox.askyesno("Xác nhận", "Bạn có chắc chắn muốn xóa sản phẩm này không?")
        if traloi:
            conn = sqlite3.connect('abc_shop.db')
            conn.cursor().execute("DELETE FROM SanPham WHERE id=?", (self.id_sp_chon,))
            conn.commit(); conn.close()
            self.load_data_sp()
            self.txt_ten_sp.delete(0, tk.END); self.txt_gia_sp.delete(0, tk.END)
            self.id_sp_chon = None

    def them_vao_gio(self):
        if not self.id_sp_chon:
            messagebox.showwarning("Lỗi", "Hãy chọn sản phẩm muốn thêm vào giỏ!")
            return
        ma_sp = self.id_sp_chon
        ten_sp = self.txt_ten_sp.get()
        gia_sp = float(self.txt_gia_sp.get())
        
        soluong = simpledialog.askinteger("Số lượng", f"Nhập số lượng cho: {ten_sp}", minvalue=1, initialvalue=1)
        if soluong:
            if ma_sp in self.gio_hang:
                self.gio_hang[ma_sp]['soluong'] += soluong
            else:
                self.gio_hang[ma_sp] = {'ten': ten_sp, 'gia': gia_sp, 'soluong': soluong}
            messagebox.showinfo("Thành công", f"Đã thêm {soluong} x {ten_sp} vào giỏ!")

    # ================= 4. TRANG KHÁCH HÀNG (HOÀN THIỆN 100%) =================
    def hien_thi_khach_hang(self):
        self.xoa_noi_dung_cu()
        tk.Label(self.main_content, text="👥 QUẢN LÝ KHÁCH HÀNG", font=("Arial", 16, "bold"), bg="#ecf0f1").pack(pady=20)
        
        frame_nhap = tk.Frame(self.main_content, bg="#ecf0f1")
        frame_nhap.pack(pady=10)
        
        tk.Label(frame_nhap, text="Tên Khách Hàng:", bg="#ecf0f1").grid(row=0, column=0, padx=5)
        self.txt_ten_kh = tk.Entry(frame_nhap, width=25)
        self.txt_ten_kh.grid(row=0, column=1, padx=5)
        
        tk.Label(frame_nhap, text="Số Điện Thoại:", bg="#ecf0f1").grid(row=0, column=2, padx=5)
        self.txt_sdt_kh = tk.Entry(frame_nhap, width=20)
        self.txt_sdt_kh.grid(row=0, column=3, padx=5)

        frame_nut = tk.Frame(self.main_content, bg="#ecf0f1")
        frame_nut.pack(pady=10)
        tk.Button(frame_nut, text="Thêm KH", bg="#2ecc71", fg="white", command=self.them_kh).grid(row=0, column=0, padx=5)
        tk.Button(frame_nut, text="Sửa KH", bg="#f1c40f", command=self.sua_kh).grid(row=0, column=1, padx=5)
        tk.Button(frame_nut, text="Xóa KH", bg="#e74c3c", fg="white", command=self.xoa_kh).grid(row=0, column=2, padx=5)
        tk.Button(frame_nut, text="Làm Mới", bg="#3498db", fg="white", command=self.lam_moi_kh).grid(row=0, column=3, padx=5)

        columns = ("ID", "Ten", "SDT")
        self.bang_kh = ttk.Treeview(self.main_content, columns=columns, show="headings", height=15)
        self.bang_kh.heading("ID", text="Mã KH")
        self.bang_kh.heading("Ten", text="Tên Khách Hàng")
        self.bang_kh.heading("SDT", text="Số Điện Thoại")
        self.bang_kh.column("ID", width=50, anchor=tk.CENTER)
        self.bang_kh.column("Ten", width=400)
        self.bang_kh.column("SDT", width=150, anchor=tk.CENTER)
        self.bang_kh.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        self.bang_kh.bind("<ButtonRelease-1>", self.chon_dong_kh)
        self.id_kh_chon = None
        self.load_data_kh()

    def load_data_kh(self):
        for row in self.bang_kh.get_children(): self.bang_kh.delete(row)
        conn = sqlite3.connect("abc_shop.db")
        for row in conn.cursor().execute("SELECT * FROM KhachHang"):
            self.bang_kh.insert('', tk.END, values=row)
        conn.close()

    def chon_dong_kh(self, event):
        dong = self.bang_kh.focus()
        if dong:
            gia_tri = self.bang_kh.item(dong, 'values')
            self.id_kh_chon = gia_tri[0]
            self.txt_ten_kh.delete(0, tk.END)
            self.txt_ten_kh.insert(0, gia_tri[1])
            self.txt_sdt_kh.delete(0, tk.END)
            self.txt_sdt_kh.insert(0, gia_tri[2])

    def lam_moi_kh(self):
        self.id_kh_chon = None
        self.txt_ten_kh.delete(0, tk.END)
        self.txt_sdt_kh.delete(0, tk.END)

    def them_kh(self):
        ten = self.txt_ten_kh.get().strip()
        sdt = self.txt_sdt_kh.get().strip()
        if not ten or not sdt:
            messagebox.showwarning("Thiếu thông tin", "Vui lòng nhập tên và số điện thoại!")
            return
        conn = sqlite3.connect('abc_shop.db')
        conn.cursor().execute("INSERT INTO KhachHang (ten_kh, sdt) VALUES (?, ?)", (ten, sdt))
        conn.commit(); conn.close()
        self.load_data_kh()
        self.lam_moi_kh()
        messagebox.showinfo("Thành công", "Đã thêm khách hàng mới!")

    def sua_kh(self):
        if not self.id_kh_chon:
            messagebox.showwarning("Lỗi", "Vui lòng chọn khách hàng để sửa!")
            return
        ten = self.txt_ten_kh.get().strip()
        sdt = self.txt_sdt_kh.get().strip()
        conn = sqlite3.connect('abc_shop.db')
        conn.cursor().execute("UPDATE KhachHang SET ten_kh=?, sdt=? WHERE id=?", (ten, sdt, self.id_kh_chon))
        conn.commit(); conn.close()
        self.load_data_kh()
        self.lam_moi_kh()
        messagebox.showinfo("Thành công", "Đã cập nhật thông tin khách hàng!")

    def xoa_kh(self):
        if not self.id_kh_chon:
            messagebox.showwarning("Lỗi", "Vui lòng chọn khách hàng để xóa!")
            return
        traloi = messagebox.askyesno("Xác nhận", "Bạn có chắc muốn xóa khách hàng này? (Lưu ý: Có thể ảnh hưởng lịch sử hóa đơn)")
        if traloi:
            conn = sqlite3.connect('abc_shop.db')
            conn.cursor().execute("DELETE FROM KhachHang WHERE id=?", (self.id_kh_chon,))
            conn.commit(); conn.close()
            self.load_data_kh()
            self.lam_moi_kh()

    # ================= 5. TRANG GIỎ HÀNG & THANH TOÁN =================
    def hien_thi_gio_hang(self):
        self.xoa_noi_dung_cu()
        tk.Label(self.main_content, text="🛒 GIỎ HÀNG & THANH TOÁN", font=("Arial", 16, "bold"), bg="#ecf0f1").pack(pady=10)

        frame_kh = tk.Frame(self.main_content, bg="#ecf0f1")
        frame_kh.pack(pady=5)
        tk.Label(frame_kh, text="👤 Chọn Khách Hàng: ", bg="#ecf0f1", font=("Arial", 10, "bold")).pack(side=tk.LEFT)
        
        self.cb_khach = ttk.Combobox(frame_kh, width=40, state="readonly")
        self.cb_khach.pack(side=tk.LEFT)
        
        conn = sqlite3.connect('abc_shop.db')
        ds_kh = [f"{row[0]} - {row[1]} - {row[2]}" for row in conn.cursor().execute("SELECT * FROM KhachHang")]
        conn.close()
        self.cb_khach['values'] = ds_kh
        if ds_kh: self.cb_khach.current(0)

        frame_nut = tk.Frame(self.main_content, bg="#ecf0f1")
        frame_nut.pack(pady=10)
        tk.Button(frame_nut, text="X Xóa SP Đã Chọn", bg="#e74c3c", fg="white", command=self.xoa_sp_gio).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_nut, text="🧹 Làm Sạch Giỏ", bg="#95a5a6", fg="white", command=self.lam_sach_gio).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_nut, text="✅ THANH TOÁN", bg="#27ae60", fg="white", font=("Arial", 10, "bold"), command=self.thanh_toan).pack(side=tk.LEFT, padx=5)

        self.bang_gio = ttk.Treeview(self.main_content, columns=("ID", "Ten", "Gia", "SL", "ThanhTien"), show="headings", height=12)
        self.bang_gio.heading("ID", text="Mã SP"); self.bang_gio.column("ID", width=50, anchor=tk.CENTER)
        self.bang_gio.heading("Ten", text="Tên sản phẩm"); self.bang_gio.column("Ten", width=300)
        self.bang_gio.heading("Gia", text="Đơn giá"); self.bang_gio.column("Gia", width=100, anchor=tk.E)
        self.bang_gio.heading("SL", text="Số lượng"); self.bang_gio.column("SL", width=70, anchor=tk.CENTER)
        self.bang_gio.heading("ThanhTien", text="Thành tiền"); self.bang_gio.column("ThanhTien", width=120, anchor=tk.E)
        self.bang_gio.pack(fill=tk.BOTH, expand=True, padx=20, pady=5)

        self.lbl_tong_tien = tk.Label(self.main_content, text="Tổng tiền: 0 VNĐ", font=("Arial", 14, "bold"), fg="red", bg="#ecf0f1")
        self.lbl_tong_tien.pack(side=tk.RIGHT, padx=20, pady=10)

        self.load_data_gio()

    def load_data_gio(self):
        for row in self.bang_gio.get_children(): self.bang_gio.delete(row)
        tong_cong = 0
        for ma_sp, info in self.gio_hang.items():
            thanh_tien = info['gia'] * info['soluong']
            tong_cong += thanh_tien
            row_val = (ma_sp, info['ten'], f"{info['gia']:,.0f}", info['soluong'], f"{thanh_tien:,.0f}")
            self.bang_gio.insert('', tk.END, values=row_val)
        self.lbl_tong_tien.config(text=f"Tổng tiền: {tong_cong:,.0f} VNĐ")

    def xoa_sp_gio(self):
        dong = self.bang_gio.focus()
        if dong:
            ma_sp = self.bang_gio.item(dong, 'values')[0]
            del self.gio_hang[ma_sp]
            self.load_data_gio()

    def lam_sach_gio(self):
        self.gio_hang.clear()
        self.load_data_gio()

    # ================= 6. XỬ LÝ THANH TOÁN & IN HÓA ĐƠN =================
    def thanh_toan(self):
        if not self.gio_hang:
            messagebox.showwarning("Giỏ hàng rỗng", "Không có sản phẩm để thanh toán!")
            return
        khach_info = self.cb_khach.get()
        if not khach_info:
            messagebox.showwarning("Lỗi", "Vui lòng chọn khách hàng!")
            return
            
        ma_kh = int(khach_info.split(" - ")[0])
        tong_cong = sum(item['gia'] * item['soluong'] for item in self.gio_hang.values())
        ngay_tao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        conn = sqlite3.connect('abc_shop.db')
        cur = conn.cursor()
        cur.execute("INSERT INTO HoaDon (khach_hang_id, tong_tien, ngay_tao) VALUES (?, ?, ?)", (ma_kh, tong_cong, ngay_tao))
        ma_hd = cur.lastrowid
        
        for ma_sp, info in self.gio_hang.items():
            thanh_tien = info['gia'] * info['soluong']
            cur.execute("INSERT INTO ChiTietHoaDon (hoa_don_id, san_pham_id, so_luong, don_gia, thanh_tien) VALUES (?, ?, ?, ?, ?)",
                        (ma_hd, ma_sp, info['soluong'], info['gia'], thanh_tien))
        conn.commit(); conn.close()

        self.in_chi_tiet_hoa_don(ma_hd, khach_info, ngay_tao, tong_cong)
        self.lam_sach_gio()

    def in_chi_tiet_hoa_don(self, ma_hd, khach_info, ngay_tao, tong_cong):
        hd_window = tk.Toplevel(self.root)
        hd_window.title(f"Hóa Đơn #{ma_hd}")
        hd_window.geometry("450x550")
        hd_window.configure(bg="white")

        tk.Label(hd_window, text="ABC SHOP", font=("Courier", 20, "bold"), bg="white").pack(pady=10)
        tk.Label(hd_window, text="HÓA ĐƠN BÁN LẺ", font=("Courier", 14), bg="white").pack()
        tk.Label(hd_window, text="-"*40, bg="white").pack()

        info_frame = tk.Frame(hd_window, bg="white")
        info_frame.pack(fill=tk.X, padx=20, pady=5)
        tk.Label(info_frame, text=f"Mã HĐ: #{ma_hd}", bg="white").pack(anchor="w")
        tk.Label(info_frame, text=f"Ngày: {ngay_tao}", bg="white").pack(anchor="w")
        tk.Label(info_frame, text=f"Khách: {khach_info.split(' - ')[1]}", bg="white").pack(anchor="w")
        tk.Label(hd_window, text="-"*40, bg="white").pack()

        for item in self.gio_hang.values():
            item_frame = tk.Frame(hd_window, bg="white")
            item_frame.pack(fill=tk.X, padx=20, pady=2)
            tk.Label(item_frame, text=f"{item['ten']}", bg="white").pack(anchor="w")
            chi_tiet = f"   {item['soluong']} x {item['gia']:,.0f}"
            thanh_tien = f"{item['soluong']*item['gia']:,.0f}"
            tk.Label(item_frame, text=chi_tiet, bg="white").pack(side=tk.LEFT)
            tk.Label(item_frame, text=thanh_tien, bg="white").pack(side=tk.RIGHT)

        tk.Label(hd_window, text="-"*40, bg="white").pack(pady=5)
        
        tk.Label(hd_window, text=f"TỔNG CỘNG: {tong_cong:,.0f} VNĐ", font=("Courier", 14, "bold"), bg="white").pack(pady=10)
        tk.Label(hd_window, text="Cảm ơn quý khách và hẹn gặp lại!", font=("Courier", 10, "italic"), bg="white").pack(pady=20)
        
        tk.Button(hd_window, text="Đóng", command=hd_window.destroy, width=15, bg="#ecf0f1").pack()

    # ================= 7. TRANG CHI TIẾT HÓA ĐƠN =================
    def hien_thi_hoa_don(self):
        self.xoa_noi_dung_cu()
        tk.Label(self.main_content, text="📄 QUẢN LÝ HÓA ĐƠN", font=("Arial", 16, "bold"), bg="#ecf0f1").pack(pady=10)

        khung_danh_sach = tk.LabelFrame(self.main_content, text="Danh sách Hóa Đơn đã bán", bg="#ecf0f1", font=("Arial", 10, "bold"))
        khung_danh_sach.pack(fill=tk.BOTH, expand=True, padx=20, pady=5)

        self.bang_hd = ttk.Treeview(khung_danh_sach, columns=("MaHD", "KhachHang", "NgayTao", "TongTien"), show="headings", height=8)
        self.bang_hd.heading("MaHD", text="Mã HĐ"); self.bang_hd.column("MaHD", width=50, anchor=tk.CENTER)
        self.bang_hd.heading("KhachHang", text="Khách Hàng"); self.bang_hd.column("KhachHang", width=250)
        self.bang_hd.heading("NgayTao", text="Ngày Giờ Tạo"); self.bang_hd.column("NgayTao", width=150, anchor=tk.CENTER)
        self.bang_hd.heading("TongTien", text="Tổng Tiền"); self.bang_hd.column("TongTien", width=150, anchor=tk.E)
        self.bang_hd.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.bang_hd.bind("<ButtonRelease-1>", self.xem_chi_tiet_hd)
        self.load_data_hoa_don()

        khung_chi_tiet = tk.LabelFrame(self.main_content, text="Chi tiết Sản phẩm", bg="#ecf0f1", font=("Arial", 10, "bold"))
        khung_chi_tiet.pack(fill=tk.BOTH, expand=True, padx=20, pady=5)

        self.bang_cthd = ttk.Treeview(khung_chi_tiet, columns=("TenSP", "SoLuong", "DonGia", "ThanhTien"), show="headings", height=8)
        self.bang_cthd.heading("TenSP", text="Tên Sản Phẩm"); self.bang_cthd.column("TenSP", width=300)
        self.bang_cthd.heading("SoLuong", text="Số Lượng"); self.bang_cthd.column("SoLuong", width=80, anchor=tk.CENTER)
        self.bang_cthd.heading("DonGia", text="Đơn Giá"); self.bang_cthd.column("DonGia", width=120, anchor=tk.E)
        self.bang_cthd.heading("ThanhTien", text="Thành Tiền"); self.bang_cthd.column("ThanhTien", width=120, anchor=tk.E)
        self.bang_cthd.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    def load_data_hoa_don(self):
        for row in self.bang_hd.get_children(): self.bang_hd.delete(row)
        conn = sqlite3.connect("abc_shop.db")
        cur = conn.cursor()
        query = '''
            SELECT HoaDon.id, KhachHang.ten_kh, HoaDon.ngay_tao, HoaDon.tong_tien
            FROM HoaDon
            LEFT JOIN KhachHang ON HoaDon.khach_hang_id = KhachHang.id
            ORDER BY HoaDon.id DESC
        '''
        for row in cur.execute(query):
            row_formatted = (row[0], row[1], row[2], f"{row[3]:,.0f} VNĐ")
            self.bang_hd.insert('', tk.END, values=row_formatted)
        conn.close()

    def xem_chi_tiet_hd(self, event):
        dong = self.bang_hd.focus()
        if not dong: return
        ma_hd = self.bang_hd.item(dong, 'values')[0]

        for row in self.bang_cthd.get_children(): self.bang_cthd.delete(row)

        conn = sqlite3.connect("abc_shop.db")
        cur = conn.cursor()
        query = '''
            SELECT SanPham.ten_sp, ChiTietHoaDon.so_luong, ChiTietHoaDon.don_gia, ChiTietHoaDon.thanh_tien
            FROM ChiTietHoaDon
            JOIN SanPham ON ChiTietHoaDon.san_pham_id = SanPham.id
            WHERE ChiTietHoaDon.hoa_don_id = ?
        '''
        for row in cur.execute(query, (ma_hd,)):
            row_formatted = (row[0], row[1], f"{row[2]:,.0f}", f"{row[3]:,.0f}")
            self.bang_cthd.insert('', tk.END, values=row_formatted)
        conn.close()
        
if __name__ =="__main__":
    root = tk.Tk()
    app = HeThongBanHangApp(root)
    root.mainloop()