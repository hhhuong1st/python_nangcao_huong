class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def get_employee_info(self):
        print(f"Mã NV: {self.employee_id} | Tên: {self.name} | Vị trí: {self.position} | Lương: {self.salary:,.0f} VNĐ")

    def apply_raise(self, percentage):
        if percentage > 0:
            increase_amount = self.salary * (percentage / 100)
            self.salary += increase_amount
            print(f"Đã tăng {percentage}% lương cho {self.name}. Lương mới cập nhật: {self.salary:,.0f} VNĐ")
        else:
            print("Phần trăm tăng lương phải lớn hơn 0.")



class Manager(Employee):
    def __init__(self, employee_id, name, position, salary, team_size):
        super().__init__(employee_id, name, position, salary)
        self.team_size = team_size

    def get_team_info(self):
        """Hiển thị thông tin về số lượng thành viên trong nhóm"""
        print(f"Quản lý {self.name} ({self.position}) đang phụ trách nhóm gồm {self.team_size} thành viên.")


if __name__ == "__main__":
    print("--- 1. TẠO ĐỐI TƯỢNG VÀ HIỂN THỊ THÔNG TIN ---")
    nv1 = Employee("NV001", "Nguyễn Văn A", "Lập trình viên", 15000000)
    nv1.get_employee_info()
    
    ql1 = Manager("QL001", "Trần Thị B", "Trưởng phòng IT", 35000000, 12)
    ql1.get_employee_info() 
    
    print("\n--- 2. TĂNG LƯƠNG CHO NHÂN VIÊN ---")
    nv1.apply_raise(10) 
    ql1.apply_raise(15) 
    
    print("\n--- 3. HIỂN THỊ THÔNG TIN NHÓM CỦA QUẢN LÝ ---")
    ql1.get_team_info()