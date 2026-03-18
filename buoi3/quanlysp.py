from datetime import datetime
class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self. price = price
        self.stock = stock
    def purchase(self, quantily):
        if quantily <= 0:
            print ("Số lượng mua phải lớn hơn 0")
            return
        if quantily > self.stock:
            print (f"Không đủ hàng trong kho, chỉ còn {self.stock} sản phẩm")
        else:
            self.stock -= quantily
            print (f" Đã mua {quantily} sản phẩm. Số lượng còn lại {self.stock} sản phẩm")
    def restock (self, quantily):
        if quantily <= 0:
            print ("Số lượng nhập phải lớn hơn 0")
            return
        self.stock += quantily
        print (f"Đã nhập thêm {quantily} sản phẩm. Tổng số lượng hiện tại là {self.stock}")
    def get_product_info (self):
        print ("==== Thông tin sản phẩm ====")
        print (f"Mã sản phẩm: {self.product_id}")
        print (f"Tên sản phẩm: {self.name}")
        print (f"Giá: {self.price}")
        print (f"Số lượng tồn kho: {self.stock}")

class PerishableProduct(Product):
    def __init__(self, product_id, name, price, stock, expiry_date):
        super().__init__(product_id, name, price, stock)
        self.expiry_date = datetime.strptime(expiry_date, "%Y-%m-%d")
    def check_expiry(self):
        today = datetime.now()
        if (today>self.expiry_date):
            print ("Sản phẩm đã hết hạn")
        else:
            days_left = (self.expiry_date - today).days
            print (f"Sản phẩm còn hạn. Còn {days_left} ngày nữa sẽ hết hạn")
    def get_product_info(self):
        super().get_product_info()
        print (f"Ngày hết hạn: {self.expiry_date.strftime ("%d/%m/%Y")}")

Product1 = Product("A","Bàn phím", 22, 14)
Product1.get_product_info()
Product1.purchase(20)
Product1.purchase(5)
Product1.purchase(20)
Product1.restock(10)
Product1.get_product_info()