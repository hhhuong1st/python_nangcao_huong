import sqlite3

def sua_tuoi_sinh_vien(ma_sv, tuoi_moi):
    # 1. Kết nối DB và tạo con trỏ
    conn = sqlite3.connect('quanly_sinhvien.db')
    cur = conn.cursor()

    
    sql_update = "UPDATE SinhVien SET tuoi =? WHERE id = ?"

    # 3. Dữ liệu thực tế cần truyền vào (Phải là dạng Tuple)
    du_lieu = (tuoi_moi, ma_sv)

    # 4. Thực thi và Lưu lại
    cur.execute(sql_update, du_lieu)
    conn.commit() 

    print(f"Đã cập nhật tuổi mới cho sinh viên có mã: {ma_sv}")

    # 5. Đóng kết nối
    conn.close()

# Cách gọi hàm:
# sua_tuoi_sinh_vien(1,21)