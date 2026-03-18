import tkinter as tk
from tkinter import ttk, messagebox
root = tk.Tk()

def thanh_toan():
    try:
        ten = txt_ten.get()

        # giá ly
        gia_goc = 25000
        gia_size = 0
        size_ten = ""
        size_var = var_size.get()

        if size_var == 1:
            gia_size = 0
            size_ten = "Nhỏ"
        elif size_var == 2:
            gia_size = 5000
            size_ten = "Vừa"
        else:
            gia_size = 10000
            size_ten = "Lớn"

        # topping
        gia_topping = 0
        ten_topping = ""
        if var_tt.get() == 1:
            gia_topping += 5000
            ten_topping = "Trân Châu"
        if var_ttc.get() == 1:
            gia_topping += 7000
            ten_topping = "Thạch Trái Cây"
        if var_c.get() == 1:
            gia_topping += 10000
            ten_topping = "Kem Chesse"

        tong = gia_goc + gia_size + gia_topping
        tt = cbo_thanh_toan.get()
        
        noidung = (f"Khách hàng: {ten}\n"
                   f"Size: {size_ten}\n"
                   f"Topping: {ten_topping}\n"
                   f"Thanh toán: {tt}\n"
                   f"Tổng: {tong}\n")


    except ValueError:
        txt_hienthi.config(text="Lỗi tính toán!")
    messagebox.showinfo("Xác nhận đơn hàng", noidung)

root.title ("Hệ thống đặt hàng trà sữa")

lbl_title = tk.Label(root, text="MILK TEA ORDER FORM", fg="brown", font=("bold", 16))
lbl_title.grid(row=0, column=0, columnspan=6, padx=10)

# khách hàng
lbl_ten = tk.Label(root, text="Tên khách hàng: ", font=("bold"))
lbl_ten.grid(row=1, column=0, padx=10)

txt_ten = tk.Entry(root)
txt_ten.grid(row=1, column=1, padx=10)

# chọn size
var_size = tk.IntVar()
var_size.set(value=2)

lbl_size = tk.Label(root, text="Chọn size ly: ", font=("bold"))
lbl_size.grid(row=2, column=0, padx=10, sticky=tk.NW)

fr_size = tk.LabelFrame(root, text="Bảng giá Size", padx=10)

tk.Radiobutton(root, text="Nhỏ (S) (+0đ)", variable=var_size, value=1).grid(row=2, column=1, sticky="w")
tk.Radiobutton(root, text="Vừa (M) (+5k)", variable=var_size, value=2).grid(row=3, column=1, sticky="w")
tk.Radiobutton(root, text="Lớn (L) (+10k)", variable=var_size, value=3).grid(row=4, column=1, sticky="w")


# Thêm topping
var_tt = tk.IntVar()
var_ttc = tk.IntVar()
var_c = tk.IntVar()
lbl_topping = tk.Label(root, text="Thêm Topping: ", font=("bold"))
lbl_topping.grid(row=5, column=0, padx=10, sticky=tk.NW)

tk.Checkbutton(root, text="Trân châu (+5k)", variable=var_tt).grid(row=5, column=1, sticky="w")
tk.Checkbutton(root, text="Thạch trái cây (+7k)", variable=var_ttc).grid(row=6, column=1, sticky="w")
tk.Checkbutton(root, text="Kem chesse (+10k)", variable=var_c).grid(row=7, column=1, sticky="w")

# Thanh toán
lbl_thanh_toan = tk.Label(root, text="Thanh toán: ", font=("bold"))
lbl_thanh_toan.grid(row=8, column=0, padx=10, sticky=tk.NW)

cbo_thanh_toan = ttk.Combobox(root, width=20)
cbo_thanh_toan['values'] = ("Ví Momo", "VCB", "MB")
cbo_thanh_toan.grid(row=8, column=1, sticky="w")

# Nút xác nhận
btn = tk.Button(root, text="Xác nhận đặt hàng", height=1, width=15, bg="brown", font=("bold", 14), command=thanh_toan)
btn.grid(row=9, column=0, columnspan=2, padx=20, pady=10)

# hiển thị
txt_hienthi = tk.Label(root, text="")
txt_hienthi.grid(row=10, column=0, columnspan=2, pady=10)

root.mainloop()