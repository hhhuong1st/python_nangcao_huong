import sqlite3

def xoa_sinh_vien(ma_sv):
    # 1. Kết nối DB
    conn = sqlite3.connect('quanly_sinhvien.db')
    cur = conn.cursor()

    # 2. Câu lệnh SQL để xóa
    sql_delete = "DELETE FROM SinhVien WHERE id = ?"
    
    # 3. Thực thi
    cur.execute(sql_delete, (ma_sv,)) # Lưu ý: ma_sv phải nằm trong tuple
    conn.commit() 

    print(f"Đã xóa sinh viên có mã: {ma_sv}")
    conn.close()

# xoa_sinh_vien(1)