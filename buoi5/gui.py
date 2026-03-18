import tkinter as tk

root = tk.Tk()
root.title("Ứng dụng đầu tiên")
root.geometry("300x200")

lbl_hello = tk.Label(root, text ="Helo, GUI World!", font=("Arial", 14))
lbl_hello.pack(pady=50)

root.mainloop()