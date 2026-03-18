import tkinter as tk
import math

def tim_nghiem():
    try:
        a = float(txt_A.get())
        b = float(txt_B.get())
        c = float(txt_C.get())
        delta = b**2 - 4*a*c
        
        if delta < 0:
            ket_qua = "Phương trình vô nghiệm"
        elif delta == 0:
            x = -b / (2*a)
            ket_qua = f"Nghiệm kép x1 = x2 = {x:.2f}"
        else:
            x1 = (-b + math.sqrt(delta)) / (2*a)
            x2 = (-b - math.sqrt(delta)) / (2*a)
            ket_qua = f"x1 = {x1:.2f}, x2 = {x2:.2f}" 
        
        txt_hienthi.config(text=f"Delta: {delta:.2f}\n{ket_qua}")
        
    except ValueError:
        txt_hienthi.config(text="Vui lòng nhập đúng giá trị số!")

root = tk.Tk()
root.title("Phương trình bậc 2")
root.geometry("650x400")

lbl_title = tk.Label(root, text="PHƯƠNG TRÌNH BẬC 2")
lbl_title.grid(row=0, column=0, columnspan=6, pady=10)

lbl_sub = tk.Label(root, text="AX² + BX + C = 0")
lbl_sub.grid(row=1, column=0, columnspan=6, pady=5)

tk.Label(root, text="A =").grid(row=2, column=0, padx=5, sticky=tk.E)
txt_A = tk.Entry(root, width=10)
txt_A.grid(row=2, column=1, padx=5)

tk.Label(root, text="B =").grid(row=2, column=2, padx=5, sticky=tk.E)
txt_B = tk.Entry(root, width=10)
txt_B.grid(row=2, column=3, padx=5)

tk.Label(root, text="C =").grid(row=2, column=4, padx=5, sticky=tk.E)
txt_C = tk.Entry(root, width=10)
txt_C.grid(row=2, column=5, padx=5)

btn_timnghiem = tk.Button(root, text="Tìm nghiệm", command=tim_nghiem)
btn_timnghiem.grid(row=3, column=0, columnspan=6, pady=20)

# Hiển thị kết quả
txt_hienthi = tk.Label(root, text="")
txt_hienthi.grid(row=4, column=0, columnspan=6, pady=10)

root.mainloop()