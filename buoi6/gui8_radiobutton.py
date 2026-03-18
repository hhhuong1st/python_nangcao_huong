import tkinter as tk
root = tk.Tk()

var_gender = tk.StringVar()
var_gender.set("Nam")

rad_male = tk.Radiobutton(root, text="Nam", variable=var_gender, value="Nam")
rad_male.pack(anchor=tk.W)
rad_famale = tk.Radiobutton(root, text="Nữ", variable=var_gender, value="Nữ")
rad_famale.pack(anchor=tk.W)

rad_khac = tk.Radiobutton(root, text="Khác", variable=var_gender, value="Khác")
rad_khac.pack(anchor=tk.W)

def xem_gioi_tinh():
    print("Giới tính đã chọn: ", var_gender.get())
tk.Button(root, text="Xác nhận", command=xem_gioi_tinh).pack()
root.mainloop()