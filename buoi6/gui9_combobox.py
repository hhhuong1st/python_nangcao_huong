def get_city(event):
    print ("Thành phố: ", combo_city.get())

import tkinter as tk
from tkinter import ttk
root = tk.Tk()



tk.Label(root, text="Chọn thành phố: ").pack()

combo_city = ttk.Combobox(root, width=20)

combo_city['values'] = ("Hà Nội", "Đà Nẵng", "TP. Hồ Chí Minh", "Cà Mau")
combo_city['state'] = 'readonly'
combo_city.pack()
combo_city.bind("<<ComboboxSelected>>", get_city)

root.mainloop()