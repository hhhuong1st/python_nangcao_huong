# Gọi Class QuanLyCuaHang từ file database.py sang đây để dùng
from database import QuanLyCuaHang

# 1. Khởi tạo đối tượng quản lý cửa hàng
cuahang = QuanLyCuaHang() 
# Lưu ý: Ngay khi khởi tạo, hàm __init__ đã tự động chạy tao_bang_dulieu()

# 2. Thêm vài sản phẩm mới vào danh mục
cuahang.them_san_pham("Áo sơ mi lụa", 250000, 30)
cuahang.them_san_pham("Đầm dạ hội", 850000, 15)
cuahang.them_san_pham("Chân váy xòe", 180000, 50)

# 3. Cập nhật giá sản phẩm (Ví dụ mã ID 1)
cuahang.sua_gia_san_pham(1, 230000)

# 4. Xóa một sản phẩm (Ví dụ mã ID 3)
cuahang.xoa_san_pham(3)