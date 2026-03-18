import sqlite3

def them_sinh_vien_moi(ten_sv, tuoi_sv, nganh_sv):
    # 1. Kết nối DB và tạo con trỏ
    conn = sqlite3.connect('quanly_sinhvien.db')
    cur = conn.cursor()

    # 2. Câu lệnh SQL (Dùng dấu ? đại diện cho dữ liệu truyền vào)
    sql_insert = "INSERT INTO SinhVien (ho_ten, tuoi, nganh_hoc) VALUES (?, ?, ?)"

    # 3. Dữ liệu thực tế cần truyền vào (Phải là dạng Tuple)
    du_lieu = (ten_sv, tuoi_sv, nganh_sv)

    # 4. Thực thi và Lưu lại
    cur.execute(sql_insert, du_lieu)
    conn.commit() 

    print(f"Đã thêm sinh viên: {ten_sv}")

    # 5. Đóng kết nối
    conn.close()

# Cách gọi hàm:
them_sinh_vien_moi("Nguyễn Văn A", 20, "CNTT")