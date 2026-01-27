import math
class Hinhtron:
    def __init__(self, Radius=0):
        self.Bankinh = Radius
    def DK(self):
        return (self.Bankinh *2)
    def CV(self):
        return (self.Bankinh * 2 * math.pi)
    def DT(self):
        return (self.Bankinh **2 )* math.pi
    def Scale(self,k):
        self.Bankinh *= k
    def show(self):
        print (f"Bán kính là: {self.Bankinh}")
        print (f"Đường kính là: {self.DK()}")
        print (f"Chu vi hình tròn là: {self.CV()}")
        print (f"Diện hình tròn là: {self.CV()}")
    def nhap(self):
        while True:
            try:
                self.Bankinh = float(input("Nhập bán kính: "))
                if (self.Bankinh > 0):
                    break
                print ("Giá trị phải lớn hơn 0. Nhập lại")
            except ValueError:
                print("Sai kiểu dữ liệu. Nhập lại")

ht = Hinhtron()
ht.nhap()
ht.show()

while True:
    try:
        k = float(input("Nhập hệ số k: "))
        if k > 0:
            ht.Scale(k)
            print (f"Lấy {k} nhân với bán kính ta có:")
            ht.show()
            break
        else:
            print("k phải lớn hơn 0")
    except ValueError:
        print ("Nhập sai. Nhập lại là số")
