import tkinter as tk
root = tk.Tk()
root.title("Listbox có Scrollbar")
root.geometry("300x200")

frame = tk.Frame(root)
frame.pack(pady=10)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(frame, yscrollcommand=scrollbar.set, height=6, width=20)
listbox.pack(side=tk.LEFT)

scrollbar.config(command=listbox.yview)

for i in range(1,16):
    listbox.insert(tk.END, f"Sản phẩm thứ {i}")

def xem_lua_chon():
    gia_tri = listbox.get(tk.ACTIVE)
    print("Bạn đang chọn: ", gia_tri)

tk.Button(root, text="Xác nhận", command=xem_lua_chon).pack(pady=10)

root.mainloop()