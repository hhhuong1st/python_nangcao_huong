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
    def area(self):
        if self.is_valid():
            p = self.perimeter() / 2
            return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        return 0

    def output(self):
        if (not self.is_valid()):
            print ("Tam giác không hợp lệ")
        else:
            print (f"Ba cạnh ---- a: {self.a}, b: {self.b}, c: {self.c},")
            print (f"Chu vi: {self.perimeter()}")
            print (f"Diện tích: {self.area()}")
            print (self.type())

    def type(self):
        if not self.is_valid():
            return "Không hợp lệ"
        if self.a == self.b == self.c:
            return "Tam giác đều"
        a,b,c = sorted ([self.a, self.b, self.c])
        vuong = abs(a**2 + b**2 - c**2 ) < 1e-6
        if vuong and (a==b):
            return "Tam giác vuông cân"
        if vuong:
            return "Tam giác vuông"
        if (a==b or b == c):
            return "Tam giác cân"
        return "Tam giác thường"

triangle = Triangle()
triangle.input()
triangle.output()