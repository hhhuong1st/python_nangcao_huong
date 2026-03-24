import sqlite3

class QuanLyCuaHang:
    def __init__(self, ten_db='quanly_cuahang.db'):
        # Khởi tạo tên database và tự động tạo bảng nếu chưa có
        self.ten_db = ten_db
        self.tao_bang_dulieu()

    def _ket_noi(self):
        # Hàm hỗ trợ kết nối database dùng chung cho class
        return sqlite3.connect(self.ten_db)

    def tao_bang_dulieu(self):
        conn = self._ket_noi()
        cur = conn.cursor()
        cur.execute(''' 
            CREATE TABLE IF NOT EXISTS SanPham (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ten_sp TEXT NOT NULL,
                gia REAL,
                so_luong INTEGER
            )
        ''')
        conn.commit()
        conn.close()

    def them_san_pham(self, ten_sp, gia, so_luong):
        conn = self._ket_noi()
        cur = conn.cursor()
        sql_insert = "INSERT INTO SanPham (ten_sp, gia, so_luong) VALUES (?, ?, ?)"
        
        cur.execute(sql_insert, (ten_sp, gia, so_luong))
        conn.commit() 
        print(f"[+] Đã thêm sản phẩm: {ten_sp}")
        conn.close()

    def sua_gia_san_pham(self, ma_sp, gia_moi):
        conn = self._ket_noi()
        cur = conn.cursor()
        sql_update = "UPDATE SanPham SET gia = ? WHERE id = ?"
        
        cur.execute(sql_update, (gia_moi, ma_sp))
        conn.commit() 
        print(f"[*] Đã cập nhật giá thành {gia_moi} cho sản phẩm có mã: {ma_sp}")
        conn.close()

    def xoa_san_pham(self, ma_sp):
        conn = self._ket_noi()
        cur = conn.cursor()
        sql_delete = "DELETE FROM SanPham WHERE id = ?"
        
        cur.execute(sql_delete, (ma_sp,))
        conn.commit() 
        print(f"[-] Đã xóa hoàn toàn sản phẩm có mã: {ma_sp}")
        conn.close()