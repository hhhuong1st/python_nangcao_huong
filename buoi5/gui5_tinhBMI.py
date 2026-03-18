import tkinter as tk

def tinh_BMI():
    try:
        h = float(txt_height.get())
        w = float(txt_weight.get())

        bmi = w / (h * h)

        if bmi < 18:
            loai = "Thiếu cân"
        elif bmi < 23:
            loai = "Bình thường"
        elif bmi < 30:
            loai = "Thừa cân"
        else:
            loai = "Béo"
        txt_hienthi.config(text=f"BMI của bạn là {bmi:.1f} - Bạn thuộc loại {loai}")
    except ValueError:
        txt_hienthi.config("Vui lòng nhập đúng giá trị")


root = tk.Tk()
root.title ("Tính chỉ số BMI")

# Tiêu đề
lbl_title = tk.Label(root, text="Tính chỉ số BMI")
lbl_title.grid(row=0, column=0, columnspan=2)

# Chiều cao
lbl_height = tk.Label(root, text="Chiều cao (m): ")
lbl_height.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

# Nhập chiều cao
txt_height = tk.Entry(root)
txt_height.grid(row=1, column=1, padx=10, pady=10)

# Cân nặng
lbl_weight = tk.Label(root, text="Cân nặng (kg): ")
lbl_weight.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

# Nhập cân nặng
txt_weight = tk.Entry(root)
txt_weight.grid(row=2, column=1, padx=10, pady=10)

# Button tính
btn_tinh = tk.Button(root, text="Tính BMI", command=tinh_BMI)
btn_tinh.grid(row=3, column=0, columnspan=2, pady=15)

# Text hiển thị kết quả
txt_hienthi = tk.Label(root, text="")
txt_hienthi.grid(row=4, column=0, columnspan=2, pady=15)

root.mainloop()