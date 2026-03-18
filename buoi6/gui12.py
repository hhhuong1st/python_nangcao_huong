import tkinter as tk
from tkinter import ttk, messagebox

class movieBookingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hệ thống đặt vé xem phim")
        self.root.geometry("450x600")

        # --- Giao diện ---
        # 1. Tiêu đề
        tk.Label(self.root, text="MOVIE TICKET BOOKING", font=("Arial", 18, "bold"), fg="darkred").grid(row=0, column=0, columnspan=2, pady=20)

        # 2. Tên khách hàng
        tk.Label(self.root, text="Tên khách hàng:", font=("bold")).grid(row=1, column=0, padx=20, sticky="w")
        self.txt_ten = tk.Entry(self.root, width=30)
        self.txt_ten.grid(row=1, column=1, padx=20, sticky="w")

        # 3. Loại ghế (Sử dụng self. để các hàm khác có thể truy cập)
        tk.Label(self.root, text="Loại ghế:", font=("bold")).grid(row=2, column=0, padx=20, pady=10, sticky="nw")
        self.var_ghe = tk.IntVar(value=1)
        
        self.fr_ghe = tk.LabelFrame(self.root, text="Chọn ghế", padx=10, pady=5)
        self.fr_ghe.grid(row=2, column=1, sticky="w")
        
        tk.Radiobutton(self.fr_ghe, text="Thường (+0đ)", variable=self.var_ghe, value=1).pack(anchor="w")
        tk.Radiobutton(self.fr_ghe, text="VIP (+30k)", variable=self.var_ghe, value=2).pack(anchor="w")
        tk.Radiobutton(self.fr_ghe, text="Ghế Đôi (+60k)", variable=self.var_ghe, value=3).pack(anchor="w")

        # 4. Dịch vụ thêm
        tk.Label(self.root, text="Dịch vụ thêm:", font=("bold")).grid(row=3, column=0, padx=20, pady=10, sticky="nw")
        self.var_bap = tk.IntVar()
        self.var_nuoc = tk.IntVar()
        self.var_combo = tk.IntVar()

        self.fr_dv = tk.Frame(self.root)
        self.fr_dv.grid(row=3, column=1, sticky="w")
        tk.Checkbutton(self.fr_dv, text="Bắp rang (+25k)", variable=self.var_bap).pack(anchor="w")
        tk.Checkbutton(self.fr_dv, text="Nước ngọt (+15k)", variable=self.var_nuoc).pack(anchor="w")
        tk.Checkbutton(self.fr_dv, text="Combo (+35k)", variable=self.var_combo).pack(anchor="w")

        # 5. Suất chiếu & Số lượng
        tk.Label(self.root, text="Suất chiếu:", font=("bold")).grid(row=4, column=0, padx=20, pady=10, sticky="w")
        self.cbo_suat = ttk.Combobox(self.root, values=["09:00", "13:00", "17:00", "21:00"], state="readonly")
        self.cbo_suat.grid(row=4, column=1, sticky="w", padx=20)
        self.cbo_suat.current(1)

        tk.Label(self.root, text="Số lượng vé:", font=("bold")).grid(row=5, column=0, padx=20, pady=10, sticky="w")
        self.txt_soluong = tk.Entry(self.root, width=10)
        self.txt_soluong.grid(row=5, column=1, padx=20, sticky="w")
        self.txt_soluong.insert(0, "1")

        # 6. Nút Đặt Vé
        self.btn_datve = tk.Button(self.root, text="ĐẶT VÉ", bg="darkred", fg="white", 
                                   font=("bold", 12), width=20, command=self.thanh_toan)
        self.btn_datve.grid(row=6, column=0, columnspan=2, pady=30)

    def thanh_toan(self):
        try:
            ten = self.txt_ten.get()
            so_luong = int(self.txt_soluong.get())
            
            # Tính toán logic (tương tự các bài trước)
            # ... (phần tính toán giá tiền)
            
            messagebox.showinfo("Xác nhận", f"Chúc mừng {ten} đã đặt vé thành công!")
        except ValueError:
            messagebox.showerror("Lỗi", "Số lượng vé phải là số!")

if __name__ == "__main__":
    root = tk.Tk()
    app = movieBookingApp(root)
    root.mainloop()