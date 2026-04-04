import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class HeThongBanHang:
    def __init__(self, goc):
        self.goc = goc
        self.goc.title("Hệ Thống Quản Lý Bán Hàng")
        self.goc.geometry("1000x600")
        self.goc.configure(bg="#ecf0f1")

        # Menu bên trái
        khung_menu = tk.Frame(goc, bg="#16456b", width=200)
        khung_menu.pack(side="left", fill="y")
        khung_menu.pack_propagate(False)

        tk.Label(khung_menu, text="HƯƠNG", fg="white", bg="#16456b", font=("Arial", 14,"bold")).pack(pady=20)
        
        tk.Button(khung_menu, text="Khách Hàng", command=lambda: self.hien_trang("khach_hang"), fg="white", bg="#c4ad2b", font=("Arial", 12,"bold")).pack(fill="x", padx=10, pady=10)
        tk.Button(khung_menu, text="Sản Phẩm", command=lambda: self.hien_trang("san_pham"), fg="white", bg="#31a123", font=("Arial", 12,"bold")).pack(fill="x", padx=10, pady=10)
        tk.Button(khung_menu, text="Giỏ Hàng", command=lambda: self.hien_trang("gio_hang"), fg="white", bg="#a12323", font=("Arial", 12,"bold")).pack(fill="x", padx=10, pady=10)
        tk.Button(khung_menu, text="Hóa Đơn", command=lambda: self.hien_trang("hoa_don"), fg="white", bg="#8e44ad", font=("Arial", 12,"bold")).pack(fill="x", padx=10, pady=10)

        # Khung nội dung bên phải 
        self.khung_chinh = tk.Frame(goc, bg="white")
        self.khung_chinh.pack(side="right", fill="both", expand=True)

        self.cac_trang = {}
        self.cac_trang["khach_hang"] = self.tao_trang_khach_hang()
        self.cac_trang["san_pham"] = self.tao_trang_san_pham()
        self.cac_trang["gio_hang"] = self.tao_trang_gio_hang()
        self.cac_trang["hoa_don"] = self.tao_trang_hoa_don()
    
        self.hien_trang('khach_hang')

    def tao_trang_khach_hang(self):
        khung = tk.Frame(self.khung_chinh)
        tk.Label(khung, text="TRANG KHÁCH HÀNG", font=("Arial", 14,"bold")).pack(pady=20)

        khung_nhap = tk.Frame(khung, bg="#ecf0f1")
        khung_nhap.pack(pady=20)

        tk.Label(khung_nhap, text="Tên Khách Hàng:", bg="#ecf0f1").grid(row=0, column=0, padx=5)
        self.o_nhap_ten_kh = tk.Entry(khung_nhap, width=30)
        self.o_nhap_ten_kh.grid(row=0, column=1, padx=20)
        
        tk.Label(khung_nhap, text="Số Điện Thoại:", bg="#ecf0f1").grid(row=0, column=2, padx=5)
        self.o_nhap_sdt_kh = tk.Entry(khung_nhap, width=30)
        self.o_nhap_sdt_kh.grid(row=0, column=3, padx=20)

        # Các nút chức năng
        khung_nut = tk.Frame(khung, bg="#ecf0f1")
        khung_nut.pack(pady=10)
        
        tk.Button(khung_nut, text="Thêm KH", command=self.them_kh, bg="#20BD61", fg="white", width=10, font=("Arial", 10,"bold")).pack(side="left", padx=5)
        tk.Button(khung_nut, text="Sửa KH", command=self.sua_kh, bg="#BDB21D", fg="white", width=10, font=("Arial", 10,"bold")).pack(side="left", padx=5)
        tk.Button(khung_nut, text="Xóa KH", command=self.xoa_kh, bg="#BE2121", fg="white", width=10, font=("Arial", 10,"bold")).pack(side="left", padx=5)
        tk.Button(khung_nut, text="Làm Mới", command=self.lam_moi_kh, bg="#1C6DB8", fg="white", width=10, font=("Arial", 10,"bold")).pack(side="left", padx=5)

        self.bang_kh = self.tao_bang(khung, ["Mã KH", "Tên Khách Hàng", "Số Điện Thoại"])
        self.bang_kh.bind("<<TreeviewSelect>>", self.khi_chon_kh)
        return khung
    
    def tao_trang_san_pham(self):
        khung = tk.Frame(self.khung_chinh)
        tk.Label(khung, text="TRANG SẢN PHẨM", font=("Arial", 14,"bold")).pack(pady=20)

        khung_nhap = tk.Frame(khung, bg="#ecf0f1")
        khung_nhap.pack(pady=20)

        tk.Label(khung_nhap, text="Tên Sản Phẩm:", bg="#ecf0f1").grid(row=0, column=0, padx=5)
        self.o_nhap_ten_sp = tk.Entry(khung_nhap, width=30)
        self.o_nhap_ten_sp.grid(row=0, column=1, padx=20)
        
        tk.Label(khung_nhap, text="Giá (VNĐ):", bg="#ecf0f1").grid(row=0, column=2, padx=5)
        self.o_nhap_gia_sp = tk.Entry(khung_nhap, width=30)
        self.o_nhap_gia_sp.grid(row=0, column=3, padx=20)

        # Các nút chức năng
        khung_nut = tk.Frame(khung, bg="#ecf0f1")
        khung_nut.pack(pady=10)
        
        tk.Button(khung_nut, text="Thêm SP", command=self.them_sp, bg="#20BD61", fg="white", width=10, font=("Arial", 10,"bold")).pack(side="left", padx=5)
        tk.Button(khung_nut, text="Sửa SP", command=self.sua_sp, bg="#BDB21D", fg="white", width=10, font=("Arial", 10,"bold")).pack(side="left", padx=5)
        tk.Button(khung_nut, text="Xóa SP", command=self.xoa_sp, bg="#BE2121", fg="white", width=10, font=("Arial", 10,"bold")).pack(side="left", padx=5)
        tk.Button(khung_nut, text="Thêm vào giỏ", command=self.them_vao_gio, bg="#1C6DB8", fg="white", width=10, font=("Arial", 10,"bold")).pack(side="left", padx=5)

        self.bang_sp = self.tao_bang(khung, ["Mã SP", "Tên Sản Phẩm", "Mức giá"])
        self.bang_sp.bind("<<TreeviewSelect>>", self.khi_chon_sp)
        return khung

    def tao_trang_gio_hang(self):
        khung = tk.Frame(self.khung_chinh)
        tk.Label(khung, text="TRANG GIỎ HÀNG", font=("Arial", 14,"bold")).pack(pady=20)

        khung_nhap = tk.Frame(khung, bg="#ecf0f1")
        khung_nhap.pack(pady=20)

        tk.Label(khung_nhap, text="Chọn Khách Hàng:", bg="#ecf0f1", font=("Arial", 11)).pack(side="left", padx=5)
        self.chon_kh_gio = ttk.Combobox(khung_nhap, width=50)
        self.chon_kh_gio['value'] = ("Chưa có khách hàng",)
        self.chon_kh_gio.current(0)
        self.chon_kh_gio.pack(side="left", padx=5)

        # Các nút chức năng
        khung_nut = tk.Frame(khung, bg="#ecf0f1")
        khung_nut.pack(pady=10)
        
        tk.Button(khung_nut, text="Xóa SP", command=self.xoa_sp_khoi_gio, bg="#BE2121", fg="white", width=10, font=("Arial", 10,"bold")).pack(side="left", padx=5)
        tk.Button(khung_nut, text="Làm sạch giỏ", command=self.lam_sach_gio, bg="#63686D", fg="white", width=10, font=("Arial", 10,"bold")).pack(side="left", padx=5)
        tk.Button(khung_nut, text="Thanh Toán", command=self.thanh_toan, bg="#20BD61", fg="white", width=10, font=("Arial", 10,"bold")).pack(side="left", padx=5)

        self.bang_gio = self.tao_bang(khung, ["Mã SP", "Tên sản phẩm", "Đơn giá", "Số lượng", "Thành tiền"])
        return khung
        
    def tao_trang_hoa_don(self):
        khung = tk.Frame(self.khung_chinh)
        tk.Label(khung, text="TRANG HÓA ĐƠN", font=("Arial", 14,"bold")).pack(pady=20)
        self.bang_hd = self.tao_bang(khung, ["Mã HĐ", "Khách Hàng", "Sản Phẩm (SL)", "Tổng Tiền", "Thời gian"])
        return khung
    
    def tao_bang(self, cha, cot):
        khung_bang = tk.Frame(cha)
        khung_bang.pack(fill="both", expand=True, padx=10, pady=10)
        
        bang = ttk.Treeview(khung_bang, columns=cot, show="headings")
        for c in cot:
            bang.heading(c, text=c)
            bang.column(c, anchor="center", width=120)
        
        thanh_cuon = ttk.Scrollbar(khung_bang, orient="vertical", command=bang.yview)
        bang.configure(yscroll=thanh_cuon.set)
        
        bang.pack(side="left", fill="both", expand=True)
        thanh_cuon.pack(side="right", fill="y")
        return bang

    def hien_trang(self, ten_trang):
        for trang in self.cac_trang.values():
            trang.pack_forget()
            
        if ten_trang == "gio_hang":
            self.cap_nhat_khach_hang_vao_gio()
            
        self.cac_trang[ten_trang].pack(fill="both", expand=True)

    def cap_nhat_khach_hang_vao_gio(self):
        danh_sach_kh = []
        if hasattr(self, 'bang_kh'):
            for dong in self.bang_kh.get_children():
                gia_tri = self.bang_kh.item(dong, "values")
                danh_sach_kh.append(f"{gia_tri[0]} - {gia_tri[1]}")
            
        if not danh_sach_kh:
            self.chon_kh_gio['value'] = ("Chưa có khách hàng",)
            self.chon_kh_gio.current(0)
        else:
            self.chon_kh_gio['value'] = tuple(danh_sach_kh)
            if self.chon_kh_gio.get() not in danh_sach_kh:
                self.chon_kh_gio.current(0)

    # === Các hàm xử lý sự kiện ===
    def them_kh(self):
        ten = self.o_nhap_ten_kh.get()
        sdt = self.o_nhap_sdt_kh.get()
        if ten and sdt:
            if not sdt.isdigit():
                messagebox.showwarning("Cảnh báo", "Số điện thoại chỉ được chứa chữ số!")
                return
            ma_kh = f"KH{len(self.bang_kh.get_children()) + 1:02d}"
            self.bang_kh.insert("", "end", values=(ma_kh, ten, sdt))
            self.lam_moi_kh()
        else:
            messagebox.showwarning("Cảnh báo", "Vui lòng nhập đầy đủ thông tin Khách Hàng!")

    def khi_chon_kh(self, event):
        chon = self.bang_kh.selection()
        if chon:
            dong = chon[0]
            gia_tri = self.bang_kh.item(dong, "values")
            self.lam_moi_kh()
            self.o_nhap_ten_kh.insert(0, gia_tri[1])
            self.o_nhap_sdt_kh.insert(0, gia_tri[2])

    def sua_kh(self):
        chon = self.bang_kh.selection()
        if not chon:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn khách hàng để sửa!")
            return
            
        ten = self.o_nhap_ten_kh.get()
        sdt = self.o_nhap_sdt_kh.get()
        if ten and sdt:
            if not sdt.isdigit():
                messagebox.showwarning("Cảnh báo", "Số điện thoại chỉ được chứa chữ số!")
                return
            dong = chon[0]
            ma_kh = self.bang_kh.item(dong, "values")[0]
            self.bang_kh.item(dong, values=(ma_kh, ten, sdt))
            messagebox.showinfo("Thành công", "Cập nhật khách hàng thành công!")
            self.lam_moi_kh()
        else:
            messagebox.showwarning("Cảnh báo", "Vui lòng nhập đầy đủ thông tin Khách Hàng!")
    
    def xoa_kh(self):
        chon = self.bang_kh.selection()
        if not chon:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn khách hàng để xóa!")
            return
        if messagebox.askyesno("Xác nhận", "Bạn có chắc muốn xóa khách hàng này?"):
            for dong in chon:
                self.bang_kh.delete(dong)
    
    def lam_moi_kh(self): 
        self.o_nhap_ten_kh.delete(0, tk.END)
        self.o_nhap_sdt_kh.delete(0, tk.END)

    def them_sp(self):
        ten = self.o_nhap_ten_sp.get()
        gia = self.o_nhap_gia_sp.get()
        if ten and gia:
            try:
                float(gia)
            except ValueError:
                messagebox.showwarning("Cảnh báo", "Giá sản phẩm phải là một số hợp lệ!")
                return
            ma_sp = f"SP{len(self.bang_sp.get_children()) + 1:02d}"
            self.bang_sp.insert("", "end", values=(ma_sp, ten, gia))
            self.o_nhap_ten_sp.delete(0, tk.END)
            self.o_nhap_gia_sp.delete(0, tk.END)
        else:
            messagebox.showwarning("Cảnh báo", "Vui lòng nhập đầy đủ thông tin Sản Phẩm!")

    def khi_chon_sp(self, event):
        chon = self.bang_sp.selection()
        if chon:
            dong = chon[0]
            gia_tri = self.bang_sp.item(dong, "values")
            self.o_nhap_ten_sp.delete(0, tk.END)
            self.o_nhap_gia_sp.delete(0, tk.END)
            self.o_nhap_ten_sp.insert(0, gia_tri[1])
            self.o_nhap_gia_sp.insert(0, gia_tri[2])

    def sua_sp(self):
        chon = self.bang_sp.selection()
        if not chon:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn sản phẩm để sửa!")
            return
            
        ten = self.o_nhap_ten_sp.get()
        gia = self.o_nhap_gia_sp.get()
        if ten and gia:
            try:
                float(gia)
            except ValueError:
                messagebox.showwarning("Cảnh báo", "Giá sản phẩm phải là một số hợp lệ!")
                return
            dong = chon[0]
            ma_sp = self.bang_sp.item(dong, "values")[0]
            self.bang_sp.item(dong, values=(ma_sp, ten, gia))
            messagebox.showinfo("Thành công", "Cập nhật sản phẩm thành công!")
            self.o_nhap_ten_sp.delete(0, tk.END)
            self.o_nhap_gia_sp.delete(0, tk.END)
        else:
            messagebox.showwarning("Cảnh báo", "Vui lòng nhập đầy đủ thông tin Sản Phẩm!")
    
    def xoa_sp(self):
        chon = self.bang_sp.selection()
        if not chon:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn sản phẩm để xóa!")
            return
        if messagebox.askyesno("Xác nhận", "Bạn có chắc muốn xóa sản phẩm này?"):
            for dong in chon:
                self.bang_sp.delete(dong)
                
    def them_vao_gio(self):
        chon = self.bang_sp.selection()
        if not chon:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn sản phẩm để thêm vào giỏ!")
            return
            
        for dong in chon:
            gia_tri = self.bang_sp.item(dong, "values")
            ma_sp, ten_sp, gia = gia_tri[0], gia_tri[1], gia_tri[2]
            
            dong_ton_tai = None
            for dong_gio in self.bang_gio.get_children():
                gia_tri_gio = self.bang_gio.item(dong_gio, "values")
                if gia_tri_gio[0] == ma_sp:
                    dong_ton_tai = dong_gio
                    break
                    
            if dong_ton_tai:
                gia_tri_gio = self.bang_gio.item(dong_ton_tai, "values")
                so_luong_moi = int(gia_tri_gio[3]) + 1
                try:
                    thanh_tien_moi = float(gia) * so_luong_moi
                except ValueError:
                    thanh_tien_moi = gia
                self.bang_gio.item(dong_ton_tai, values=(ma_sp, ten_sp, gia, so_luong_moi, thanh_tien_moi))
            else:
                so_luong = 1
                try:
                    thanh_tien = float(gia) * so_luong
                except ValueError:
                    thanh_tien = gia
                self.bang_gio.insert("", "end", values=(ma_sp, ten_sp, gia, so_luong, thanh_tien))
                
        messagebox.showinfo("Thành công", "Đã thêm sản phẩm vào giỏ hàng!")

    def xoa_sp_khoi_gio(self):
        chon = self.bang_gio.selection()
        if not chon:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn sản phẩm trong giỏ để xóa!")
            return
        for dong in chon:
            self.bang_gio.delete(dong)

    def lam_sach_gio(self):
        if not self.bang_gio.get_children():
            messagebox.showinfo("Thông báo", "Giỏ hàng đang trống.")
            return
        if messagebox.askyesno("Xác nhận", "Bạn có chắc muốn làm sạch giỏ hàng?"):
            for dong in self.bang_gio.get_children():
                self.bang_gio.delete(dong)

    def thanh_toan(self):
        danh_sach_dong = self.bang_gio.get_children()
        if not danh_sach_dong:
            messagebox.showwarning("Cảnh báo", "Giỏ hàng đang trống, không thể thanh toán!")
            return
            
        tong_tien = 0
        ds_ten_sp = []
        for dong in danh_sach_dong:
            gia_tri = self.bang_gio.item(dong, "values")
            ds_ten_sp.append(f"{gia_tri[1]} ({gia_tri[3]})")
            try:
                tong_tien += float(gia_tri[4])
            except ValueError:
                pass
                
        khach_hang = self.chon_kh_gio.get()
        thoi_gian = datetime.now().strftime("%d/%m/%Y %H:%M")
        ma_hd = f"HD{len(self.bang_hd.get_children()) + 1:02d}"
        chi_tiet_sp = ", ".join(ds_ten_sp)
        
        self.bang_hd.insert("", "end", values=(ma_hd, khach_hang, chi_tiet_sp, tong_tien, thoi_gian))
                
        messagebox.showinfo("Thanh Toán", f"Thanh toán thành công!\nTổng số tiền: {tong_tien}")
        for dong in danh_sach_dong:
            self.bang_gio.delete(dong)
            
        self.hien_trang("hoa_don")

if __name__ =="__main__":
    cua_so = tk.Tk()
    ung_dung = HeThongBanHang(cua_so)
    cua_so.mainloop()