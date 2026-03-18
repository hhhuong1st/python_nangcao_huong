class HinhChuNhat:
    def __init__(self, Chieudai=0, Chieurong=0):
        self.Chieudai = Chieudai
        self.Chieurong = Chieurong
    
    def CVhcn(self):
        return (self.Chieurong + self.Chieudai)*2
    def DThcn(self):
        return (self.Chieurong*self.Chieudai)
    def is_square(self):
        return self.Chieurong == self.Chieudai
    def Scale(self, k):
        self.Chieudai *= k
        self.Chieurong *= k

    def show_info(self):
        # print (f"Chiều rộng là: {self.Chieurong}")
        # print (f"Chiều dài là: {self.Chieudai}")
        print (f"Chu vi hình chữ nhật là: {self.CVhcn()}")
        print (f"Diện tích hình chữ nhật là: {self.DThcn()}")
        print (f"Có phải hình vuông không:  {self.is_square()}")
    
    def nhap(self):
        while True:
            try:
                self.Chieurong = int(input("Nhập chiều rộng: "))
                self.Chieudai = int(input("Nhập chiều dài: "))
                if (self.Chieurong>0 and self.Chieudai>0):
                    break
                print("Giá trị phải > 0. Nhập lại.")
            except ValueError:
                print("Dữ liệu không hợp lệ. Nhập lại.")
        
hcn = HinhChuNhat()
hcn.nhap()
hcn.show_info()

while True:
    try:
        k = float(input("Nhập hệ số k: "))
        if k > 0:
            hcn.Scale(k)
            print (f"Lấy {k} nhân với chiều dài và chiều rộng ta có:")
            hcn.show_info()
            break
        else:
            print("k phải lớn hơn 0")
    except ValueError:
        print ("Nhập sai. Nhập lại là số")

    