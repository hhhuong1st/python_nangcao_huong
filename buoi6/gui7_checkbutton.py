import tkinter as tk
root = tk.Tk()

var_music = tk.IntVar()
var_sport = tk.IntVar()

chk_music = tk.Checkbutton(root, text="Nghe nhạc", variable=var_music)
chk_music.pack(anchor=tk.W)
chk_sport = tk.Checkbutton(root, text="Chơi thể thao", variable=var_sport)
chk_sport.pack(anchor=tk.W)

def kiem_tra():
    if var_music.get() == 1:
        print ("Bạn thích nghe nhạc!")
    if var_sport.get() == 1:
        print ("Bạn thích chơi thể thao!")

tk.Button(root, text="Kiểm tra", command=kiem_tra).pack()
root.mainloop()