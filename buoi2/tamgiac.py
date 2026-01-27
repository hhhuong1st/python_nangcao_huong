import math
class Triangle:
    def __init__(self, a=0, b=0, c=0):
        self.a = a
        self.b = b
        self.c = c

    def input(self):
        while True:
            try:
                self.a = int(input("Nhập a: "))
                self.b = int(input("Nhập b: "))
                self.c = int(input("Nhập c: "))
                if (self.a > 0 and self.b >0 and self.c > 0):
                    break
                print ("Giá trị phải lớn hơn 0")
            except ValueError:
                print("Dữ liệu không hợp lệ. Nhập lại.")

    def is_valid(self):
        if (self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a):
            return True
        return False
    def perimeter(self):
        if (self.is_valid()):
            return self.a + self.b + self.c
        return
    def type(self):
        if not self.is_valid():
            return "Không hợp lệ"
        if self.a == self.b == self.c:
            return "Tam giác đều"
        if self.a == self.b or self.b > self.c or self.a > self.c:
            return "Tam giác cân"
        return "Tam giác thường"
    def output(self):
        print ("Thông tin hình tam giác")
        print (f"Ba cạnh a = {self.a}, b = {self.b}, c = {self.c}")
        if (self.is_valid()):
            print (f"Chu vi là: {self.perimeter()}")
            print (f"Diện tích là: {self.perimeter}")
        else:
            print ("Các cạnh không tạo thành hành tam giác")

triangle = Triangle()
triangle.input()
triangle.output()