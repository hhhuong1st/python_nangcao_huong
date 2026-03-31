import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import sqlite3
from datetime import datetime

class HeThongCuaHangApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hệ Thống Quản Lý Bán Hàng (Có Thanh Toán)")
        self.root.geometry("1000x600")
        self.root.configure(bg="#ecf0f1")
        menu_frame = tk.Frame(root, bg="#2c3e50", width=200)
        menu_frame.pack(side="left", fill="y")
        menu_frame.pack_propagate(False)
        self.khoi_tao_db()
        self.tao_giao_dien()
        self.hien_thi_san_pham()

    # def khoi_tao_db(self):
    #     conn = sqlite3.connect('shop_meomeo.db')
    #     cur = conn.cursor()
    #     # Bảng Khách Hàng
    #     cur.execute('''CREATE TABLE IF NOT EXISTS KhachHang (
    #         id INTEGER PRIMARY KEY AUTOINCREMENT, ten_kh TEXT, sdt TEXT)''')
    #     # Bảng Sản Phẩm
    #     cur.execute('''CREATE TABLE IF NOT EXISTS SanPham (
    #         id INTEGER PRIMARY KEY AUTOINCREMENT, ten_sp TEXT, gia REAL)''')
    #     # Bảng Hóa Đơn
    #     cur.execute('''CREATE TABLE IF NOT EXISTS HoaDon (
    #         id INTEGER PRIMARY KEY AUTOINCREMENT, khach_hang_id INTEGER, tong_tien REAL, ngay_tao TEXT)''')
    #     # Bảng Chi Tiết Hóa Đơn
    #     cur.execute('''CREATE TABLE IF NOT EXISTS ChiTietHoaDon (
    #         id INTEGER PRIMARY KEY AUTOINCREMENT, hoa_don_id INTEGER, san_pham_id INTEGER, so_luong INTEGER, don_gia REAL, thanh_tien REAL)''')
        
    #     cur.execute("SELECT COUNT(*) FROM KhachHang")
    #     if cur.fetchone()[0] == 0:
    #         cur.execute("INSERT INTO KhachHang (ten_kh, sdt) VALUES ('Khách Vãng Lai', '0000000000')")
            
    #     conn.commit()
    #     conn.close()

    def tao_giao_dien(self):
        tk.Button(self,menu_c)
        
        tk.Label(self.sidebar, text="SHOP_MEOMEO", font=("Arial", 16, "bold"), fg="#f1c40f", bg="#2c3e50").pack(pady=30)
        tk.Button(self.sidebar, text="Khách hàng").pack(fill=tk.X, pady=5, padx=10)
        tk.Button(self.sidebar, text="Đơn hàng").pack(fill=tk.X, pady=5, padx=10)
        tk.Button(self.sidebar, text="Giỏ hàng").pack(fill=tk.X, pady=5, padx=10)

    def hien_thi_san_pham(self):
        tk.Label(self.main_content, text="QUẢN LÝ SẢN PHẨM", font=("Arial", 16, "bold"), bg="#ecf0f1", fg="#333").pack(pady=20)

        frame_nhap = tk.Frame(self.main_content, bg="#ecf0f1")
        frame_nhap.pack(pady=10)

        
if __name__ =="__main__":
    root = tk.Tk()
    app = HeThongCuaHangApp(root)
    root.mainloop()