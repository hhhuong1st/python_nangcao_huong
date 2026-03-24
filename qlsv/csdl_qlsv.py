import tkinter as tk

class quanlySVApp:
    def __init__(self,root):
        self.root = root
        self.root.title("Quản lý sinh viên")
        self.root.geometry("800x450")
        # Khởi tạo CSDL
        self.khoi_tao_db()
        # Tạo giao diện
        self.tao_giao_dien()
        # Hiển thị CSDL -> Giao diện
        self.hien_thi_du_lieu()

    def khoi_tao_db(self):
        pass
    def tao_giao_dien(self):
        pass
    def hien_thi_du_lieu(self):
        pass


if __name__ =="__main__":
    root = tk.Tk()
    qlsvApp = quanlySVApp(root)

    root.mainloop()