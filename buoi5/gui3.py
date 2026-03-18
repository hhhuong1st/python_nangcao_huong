import tkinter as tk
root = tk.Tk()

lbl_user = tk.Label(root, text="Tài khoản")
lbl_user.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)

lbl_pass = tk.Label(root, text="Mật khẩu")
lbl_pass.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)


txt_user = tk.Entry(root)
txt_user.grid(row=0, column=1, padx=5, pady=5)

txt_pass =tk.Entry(root, show="")
txt_pass.grid(row=1, column=1, padx=5, pady=5)

root.mainloop()