class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.status = "Có sẵn"

    def get_book_info(self):
        print("----------Thông tin sách----------")
        print(f"Mã sách: {self.book_id}")
        print(f"Tiêu đề: {self.title}")
        print(f"Tác giả: {self.author}")
        print(f"Tình trạng: {self.status}")

    def borrow(self):
        if self.status == "Có sẵn":
            self.status = "Đã mượn"
            print(f"Đã mượn sách: {self.title}")
        else:
            print(f"Sách {self.title} đã có người mượn")
    def return_book(self):
        if (self.status == "Đã mượn"):
            self.status == "Có sẵn"
            print ("Đã trả sách")
        else:
            print(f"Sách {self.title} chưa được mượn!")

class Ebook(Book):
    def __init__(self, book_id, title, author, file_size, format):
        super().__init__(book_id, title, author)
        self.file_size = file_size
        self.format = format

    def get_book_info(self):
        super().get_book_info()
        print(f"Kích thước file: {self.file_size}")
        print(f"Định dạng file: {self.format}")

book = Book(123, "Dế mèn phiêu lưu ký", "Tô Hoài")
# book.get_book_info()
# book.borrow()
# book.get_book_info()
# book.return_book()
# book.get_book_info()

ebook = Ebook(123, "Dế mèn phiêu lưu ký", "Tô Hoài", 1000, "pdf")
book.get_book_info()