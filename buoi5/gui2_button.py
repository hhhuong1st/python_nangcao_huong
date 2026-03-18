import tkinter as tk
root = tk.Tk()
root.geometry("500x500")

btn1 = tk.Button(root, text="Nút trái")
btn2 = tk.Button(root, text="Nút giữa")
btn3 = tk.Button(root, text="Nút phải")

btn1.pack(side=tk.LEFT, padx = 10)
btn2.pack(side=tk.LEFT, padx = 10)
btn3.pack(side=tk.LEFT, padx = 10)

root.mainloop()