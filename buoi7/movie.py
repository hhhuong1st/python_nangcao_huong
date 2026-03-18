import tkinter as tk
from tkinter import ttk, messagebox

class movieBookingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hệ thống đặt vé xem phim")
        self.root.geometry("500x650")
        self.root.configure(bg="white")

        self.base_price = 70000
        
        self.seat_price = {"Thường": 0, "VIP": 30000, "Ghế Đôi": 60000}
        self.service_price = {"Bắp rang": 25000, "Nước ngọt": 15000, "Combo": 35000}

        self.create_widgets()

    def create_widgets(self):
        title = tk.Label(self.root, text="MOVIE TICKET BOOKING", font=("Arial", 18, "bold"), fg="darkred", bg="white")
        title.pack(pady=20)

        frame = tk.Frame(self.root, bg="white")
        frame.pack(padx=20, pady=10)
        
        # 1. Tên khách hàng
        tk.Label(frame, text="Tên khách hàng: ", font=("Arial", 12, "bold"), bg="white").grid(row=0, column=0, sticky="w", pady=5)
        self.entry_name = tk.Entry(frame, width=30)
        self.entry_name.grid(row=0, column=1, sticky="w", pady=5)

        # 2. Loại ghế
        tk.Label(frame, text="Loại ghế: ", font=("Arial", 12, "bold"), bg="white").grid(row=1, column=0, sticky="w", pady=10)
        
        self.var_seat = tk.StringVar(value="Thường") 
        
        fr_seat = tk.LabelFrame(frame, text="Chọn ghế", bg="white", padx=10, pady=5)
        fr_seat.grid(row=1, column=1, sticky="w")

        tk.Radiobutton(fr_seat, text="Thường (+0đ)", variable=self.var_seat, value="Thường", bg="white").grid(row=0, column=0, sticky="w")
        tk.Radiobutton(fr_seat, text="VIP (+30k)", variable=self.var_seat, value="VIP", bg="white").grid(row=1, column=0, sticky="w")
        tk.Radiobutton(fr_seat, text="Ghế Đôi (+60k)", variable=self.var_seat, value="Ghế Đôi", bg="white").grid(row=2, column=0, sticky="w")

        # 3. Dịch vụ thêm
        tk.Label(frame, text="Dịch vụ thêm: ", font=("Arial", 12, "bold"), bg="white").grid(row=4, column=0, sticky="w", pady=10)
        self.var_br = tk.IntVar()
        self.var_nn = tk.IntVar()
        self.var_cb = tk.IntVar()

        fr_service = tk.Frame(frame, bg="white", padx=10, pady=5)
        fr_service.grid(row=4, column=1, sticky="w")
        tk.Checkbutton(fr_service, text="Bắp rang (+25k)", variable=self.var_br, bg="white").grid(row=0, column=0, sticky="w")
        tk.Checkbutton(fr_service, text="Nước ngọt (+15k)", variable=self.var_nn, bg="white").grid(row=1, column=0, sticky="w")
        tk.Checkbutton(fr_service, text="Combo (+35k)", variable=self.var_cb, bg="white").grid(row=2, column=0, sticky="w")

        # Suất chiếu
        tk.Label(frame, text="Suất chiếu: ", font=("Arial", 12, "bold"), bg="white").grid(row=7, column=0, sticky="w", pady=10)
        self.time_var = tk.StringVar()
        cbo_time = ttk.Combobox(frame, width=30, textvariable=self.time_var, state="readonly")
        cbo_time['value'] = ("13:00", "15:00", "17:00")
        cbo_time.current(0)
        cbo_time.grid(row=7, column=1, sticky="w")

        # Số lượng vé
        tk.Label(frame, text="Số lượng vé: ", font=("Arial", 12, "bold"), bg="white").grid(row=8, column=0, sticky="w", pady=10)
        self.entry_ticket = tk.Entry(frame, width=30)
        self.entry_ticket.grid(row=8, column=1, sticky="w", pady=5)

        # Nút Đặt vé
        self.book_btn = tk.Button(frame, text="Đặt vé", bg="brown", fg="white", font=("bold", 14), command=self.pay)
        self.book_btn.grid(row=9, column=0, columnspan=2, pady=20)

    def pay(self):
        name = self.entry_name.get().strip()
        if not name:
            messagebox.showwarning("Lỗi", "Vui lòng nhập tên")
            return
        
        try:
            quantity = int(self.entry_ticket.get())
            if quantity <= 0: raise ValueError
        except:
            messagebox.showwarning("Lỗi", "Số lượng vé phải là số nguyên dương")
            return


        seat_type = self.var_seat.get()
        

        ticket_price = (self.base_price + self.seat_price[seat_type]) * quantity
        total = ticket_price

        services = []
        if self.var_br.get():
            total += self.service_price["Bắp rang"]
            services.append("Bắp rang")
        if self.var_nn.get():
            total += self.service_price["Nước ngọt"]
            services.append("Nước ngọt")
        if self.var_cb.get():
            total += self.service_price["Combo"]
            services.append("Combo")

        result = (
            f"Khách hàng: {name}\n"
            f"Suất chiếu: {self.time_var.get()}\n"
            f"Loại ghế: {seat_type}\n"
            f"Số lượng vé: {quantity}\n"
            f"Dịch vụ: {', '.join(services) if services else "Không"}\n"
            f"Tổng tiền: {total:,} đ"
        )
        messagebox.showinfo("Đặt vé thành công", result)
        
if __name__ == "__main__":
    root = tk.Tk()
    app = movieBookingApp(root)
    root.mainloop()