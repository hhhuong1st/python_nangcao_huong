import tkinter as tk
root = tk.Tk()
root.title("Ví dụ cửa sổ")
root.geometry("500x500")
root.resizable(False,False)
root.configure(bg="lightyellow")

lbl_hello = tk.Label(root, text ="Helo, GUI World!", font=("Arial", 14))
lbl_hello.pack(pady=50)

root.mainloop()