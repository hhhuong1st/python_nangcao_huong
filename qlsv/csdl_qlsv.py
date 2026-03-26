import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

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
        conn = sqlite3.connect('quanlySV.db')
        cur = conn.cursor()
        cur.execute(''' 
                        CREATE TABLE IF NOT EXISTS SinhVien (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    ten TEXT NOT NULL,
                    tuoi INTEGER,
                    nganh TEXT
                    )
                ''')
        conn.commit()
        conn.close()


    def tao_giao_dien(self):
        frame_nhap = tk.Frame(self.root,padx=20,pady=20)
        frame_nhap.pack(side=tk.LEFT, fill=tk.Y)
        tk.Label(frame_nhap, text="THÔNG TIN SINH VIÊN",
                 font=("Arial", 14,"bold"), fg="blue").grid(row=0, column=0,columnspan=2, pady=10)
        
        tk.Label(frame_nhap, text="Họ và tên").grid(row=1, column=0, sticky=tk.W,pady=5)
        self.txt_ten = tk.Entry(frame_nhap, width=25)
        self.txt_ten.grid(row=1, column=1, pady=5)

        tk.Label(frame_nhap, text="Tuổi: ").grid(row=2, column=0, sticky=tk.W,pady=5)
        self.txt_tuoi = tk.Entry(frame_nhap, width=25)
        self.txt_tuoi.grid(row=2, column=1, pady=5)

        tk.Label(frame_nhap, text="Ngành Học: ").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.cb_nganh = ttk.Combobox(frame_nhap, width=22, state="readonly",
                                     value = ("Công nghệ thông tin", "Kế toán", "Quản trị kinh doanh", "Ngôn ngữ Anh"))
        self.cb_nganh.grid(row=3, column=1, pady=5)

        # Nút
        frame_nut = tk.Frame(frame_nhap)
        frame_nut.grid(row=4, column=0, columnspan=2, pady=20)

        tk.Button(frame_nut, text="Thêm", bg="#90ee90", width=8, command=self.them_sv).grid(row=4, column=0, sticky=tk.W, padx=5)
        tk.Button(frame_nut, text="Sửa", bg="#f5f36f", width=8, command=self.sua_sv).grid(row=4, column=1, sticky=tk.W, padx=5)
        tk.Button(frame_nut, text="Xoá", bg="#ec857d", width=8, command=self.xoa_sv).grid(row=4, column=2, sticky=tk.W, padx=5)
        tk.Button(frame_nut, text="Làm mới", bg="#65d7fa", width=8, command=self.lam_moi).grid(row=4, column=3, sticky=tk.W, padx=5)

        frame_bang = tk.Frame(self.root,padx=10, pady=10)
        frame_bang.pack (side=tk.RIGHT, fill=tk.BOTH, expand=True)
        scrollbar = tk.Scrollbar(frame_bang)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.bang_sv = ttk.Treeview(frame_bang, columns=("ID", "Ten", "Tuoi", "Nganh"),
                                    show="headings", yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.bang_sv.yview)

        self.bang_sv.column("ID", width=40, anchor=tk.CENTER)
        self.bang_sv.column("Ten", width=150, anchor=tk.W)
        self.bang_sv.column("Tuoi", width=50, anchor=tk.CENTER)
        self.bang_sv.column("Nganh", width=120, anchor=tk.CENTER)

        self.bang_sv.heading("ID", text="Mã SV")
        self.bang_sv.heading("Ten", text="Họ và tên")
        self.bang_sv.heading("Tuoi", text="Tuổi")
        self.bang_sv.heading("Nganh", text="Ngành học")

        self.bang_sv.pack(fill=tk.BOTH, expand=True)

        self.bang_sv.bind("<ButtonRelease-1>", self.chon_dong_bang)
    
    def chon_dong_bang(self, event):
        dong_chon = self.bang_sv.focus()
        if not dong_chon:
            return
        gia_tri = self.bang_sv.item(dong_chon, 'values')
        self.lam_moi()
        self.txt_ten.insert(0, gia_tri[1])
        self.txt_tuoi.insert(0, gia_tri[2])
        self.cb_nganh.set( gia_tri[3])

    def lam_moi(self):
        self.txt_ten.delete(0,tk.END)
        self.txt_tuoi.delete(0,tk.END)
        self.cb_nganh.set('')
        
    def hien_thi_du_lieu(self):
        for row in self.bang_sv.get_children():
            self.bang_sv.delete(row)

        conn = sqlite3.connect("quanlySV.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM SinhVien")
        for row in cur.fetchall():
            self.bang_sv.insert('', tk.END, values=row)
        conn.close()

    def them_sv(self):
        ten = self.txt_ten.get()
        tuoi = self.txt_tuoi.get()
        nganh = self.cb_nganh.get()

        if not ten or not tuoi or not nganh:
            messagebox.showwarning("Lỗi", "Vui lòng nhập đủ thông tin")
            return
        conn = sqlite3.connect('quanlySV.db')
        cur = conn.cursor()
        cur.execute("INSERT INTO SinhVien (ten, tuoi, nganh) VALUES (?, ?, ?)", (ten, tuoi, nganh))
        conn.commit()
        conn.close()
       
        self.hien_thi_du_lieu()
        messagebox.showinfo("Thành công", f"Đã thêm: {ten}")

    def sua_sv(self):
        dong_chon = self.bang_sv.focus()
        if not dong_chon:
            messagebox.showwarning("Lỗi","Vui lòng chọn dòng để sửa!")
            return
        ma_sv = self.bang_sv.item(dong_chon,'values')[0]
        ten = self.txt_ten.get()
        tuoi = self.txt_tuoi.get()
        nganh = self.cb_nganh.get()
        conn = sqlite3.connect('quanlySV.db')
        cur = conn.cursor()
        sql = "UPDATE SinhVien SET ten=?, tuoi=?, nganh=? WHERE id=?"
        cur.execute(sql, (ten,tuoi,nganh,ma_sv))
        conn.commit()
        conn.close()

        self.lam_moi()
        self.hien_thi_du_lieu()
        messagebox.showinfo("Thành công","Đã cập nhật thông tin")

    def xoa_sv(self):
        dong_chon = self.bang_sv.focus()
        if not dong_chon:
            messagebox.showwarning("Lỗi","Vui lòng chọn dòng để xoá!")
            return
        if messagebox.askyesno("Xác nhận","Bạn có muốn xoá sinh viên này"):


            ma_sv = self.bang_sv.item(dong_chon,'values')[0]
            
            conn = sqlite3.connect('quanlySV.db')
            cur = conn.cursor()
            sql = "DELETE FROM SinhVien WHERE id=?"
            cur.execute(sql, (ma_sv))
            conn.commit()
            conn.close()

            self.lam_moi()
            self.hien_thi_du_lieu()
            messagebox.showinfo("Thành công","Đã xoá sinh viên")

    


if __name__ =="__main__":
    root = tk.Tk()
    qlsvApp = quanlySVApp(root)

    root.mainloop()