import tkinter as tk
from tkinter import ttk, messagebox

class movieBookingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hệ thống đặt vé xem phim")
        self.root.geometry("450x650")
        
        # Giá cơ bản cho 1 vé thường
        self.GIA_VE_GOC = 80000
        
        # --- Giao diện ---
        # 1. Tiêu đề
        tk.Label(self.root, text="MOVIE TICKET BOOKING", font=("Arial", 18, "bold"), fg="darkred").grid(row=0, column=0, columnspan=2, pady=20)
        
        # 2. Tên khách hàng
        tk.Label(self.root, text="Tên khách hàng:", font=("Arial", 10, "bold")).grid(row=1, column=0, padx=20, sticky="w")
        self.txt_ten = tk.Entry(self.root, width=30)
        self.txt_ten.grid(row=1, column=1, padx=20, sticky="w")
        
        # 3. Loại ghế
        tk.Label(self.root, text="Loại ghế:", font=("Arial", 10, "bold")).grid(row=2, column=0, padx=20, pady=10, sticky="nw")
        self.var_ghe = tk.IntVar(value=1)
        self.fr_ghe = tk.LabelFrame(self.root, text="Chọn ghế", padx=10, pady=5)
        self.fr_ghe.grid(row=2, column=1, sticky="w")
        
        tk.Radiobutton(self.fr_ghe, text="Thường (+0đ)", variable=self.var_ghe, value=1).pack(anchor="w")
        tk.Radiobutton(self.fr_ghe, text="VIP (+30k)", variable=self.var_ghe, value=2).pack(anchor="w")
        tk.Radiobutton(self.fr_ghe, text="Ghế Đôi (+60k)", variable=self.var_ghe, value=3).pack(anchor="w")
        
        # 4. Dịch vụ thêm
        tk.Label(self.root, text="Dịch vụ thêm:", font=("Arial", 10, "bold")).grid(row=3, column=0, padx=20, pady=10, sticky="nw")
        self.var_bap = tk.IntVar()
        self.var_nuoc = tk.IntVar()
        self.var_combo = tk.IntVar()
        
        self.fr_dv = tk.Frame(self.root)
        self.fr_dv.grid(row=3, column=1, sticky="w")
        tk.Checkbutton(self.fr_dv, text="Bắp rang (+25k)", variable=self.var_bap).pack(anchor="w")
        tk.Checkbutton(self.fr_dv, text="Nước ngọt (+15k)", variable=self.var_nuoc).pack(anchor="w")
        tk.Checkbutton(self.fr_dv, text="Combo (+35k)", variable=self.var_combo).pack(anchor="w")
        
        # 5. Suất chiếu & Số lượng
        tk.Label(self.root, text="Suất chiếu:", font=("Arial", 10, "bold")).grid(row=4, column=0, padx=20, pady=10, sticky="w")
        self.cbo_suat = ttk.Combobox(self.root, values=["09:00", "13:00", "17:00", "21:00"], state="readonly")
        self.cbo_suat.grid(row=4, column=1, sticky="w", padx=20)
        self.cbo_suat.current(1)
        
        tk.Label(self.root, text="Số lượng vé:", font=("Arial", 10, "bold")).grid(row=5, column=0, padx=20, pady=10, sticky="w")
        self.txt_soluong = tk.Entry(self.root, width=10)
        self.txt_soluong.grid(row=5, column=1, padx=20, sticky="w")
        self.txt_soluong.insert(0, "1")
        
        # 6. Hiển thị tổng tiền (Nhãn này sẽ cập nhật khi nhấn Đặt vé)
        self.lbl_tongtien = tk.Label(self.root, text="Tổng tiền: 0đ", font=("Arial", 12, "bold"), fg="blue")
        self.lbl_tongtien.grid(row=6, column=0, columnspan=2, pady=10)

        # 7. Nút Đặt Vé
        self.btn_datve = tk.Button(self.root, text="ĐẶT VÉ", bg="darkred", fg="white", 
                                   font=("Arial", 12, "bold"), width=20, command=self.thanh_toan)
        self.btn_datve.grid(row=7, column=0, columnspan=2, pady=10)

    def thanh_toan(self):
        try:
            # Lấy thông tin cơ bản
            ten = self.txt_ten.get().strip()
            if not ten:
                messagebox.showwarning("Thông báo", "Vui lòng nhập tên khách hàng!")
                return

            so_luong = int(self.txt_soluong.get())
            if so_luong <= 0:
                raise ValueError
            
            # Tính phụ phí ghế
            phu_phi_ghe = 0
            loai_ghe = ""
            if self.var_ghe.get() == 1:
                phu_phi_ghe = 0
                loai_ghe = "Thường"
            elif self.var_ghe.get() == 2:
                phu_phi_ghe = 30000
                loai_ghe = "VIP"
            elif self.var_ghe.get() == 3:
                phu_phi_ghe = 60000
                loai_ghe = "Đôi"

            # Tính tiền dịch vụ
            tien_dich_vu = 0
            ds_dich_vu = []
            if self.var_bap.get():
                tien_dich_vu += 25000
                ds_dich_vu.append("Bắp rang")
            if self.var_nuoc.get():
                tien_dich_vu += 15000
                ds_dich_vu.append("Nước ngọt")
            if self.var_combo.get():
                tien_dich_vu += 35000
                ds_dich_vu.append("Combo")

            # Công thức tổng tiền: (Giá gốc + Phụ phí ghế) * Số lượng + Tiền dịch vụ
            tong_tien = (self.GIA_VE_GOC + phu_phi_ghe) * so_luong + tien_dich_vu
            
            # Cập nhật nhãn hiển thị
            self.lbl_tongtien.config(text=f"Tổng tiền: {tong_tien:,}đ")

            # Hiển thị thông báo chi tiết
            thong_tin = f"""
            --- HÓA ĐƠN ĐẶT VÉ ---
            Khách hàng: {ten}
            Suất chiếu: {self.cbo_suat.get()}
            Loại ghế: {loai_ghe}
            Số lượng: {so_luong}
            Dịch vụ: {', '.join(ds_dich_vu) if ds_dich_vu else 'Không'}
            ----------------------
            TỔNG CỘNG: {tong_tien:,} VNĐ
            """
            messagebox.showinfo("Xác nhận đặt vé", thong_tin)

        except ValueError:
            messagebox.showerror("Lỗi", "Số lượng vé phải là số nguyên dương!")

if __name__ == "__main__":
    root = tk.Tk()
    app = movieBookingApp(root)
    root.mainloop()