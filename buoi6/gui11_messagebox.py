import tkinter as tk
from tkinter import messagebox
root = tk.Tk()

def xac_nhan_thoat():
    traloi = messagebox.askyesno("Cảnh báo", "Bạn có chắc muốn thoát ứng dụng?")

    if traloi == True:
        root.destroy()
    else:
        messagebox.showinfo("Thông báo", "Cảm ơn bạn đã ở lại!")

tk.Button(root, text="Thoát", command=xac_nhan_thoat).pack(pady=20)

root.mainloop()