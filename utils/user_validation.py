import re
from datetime import datetime

class UserValidation:
    def __init__(self, userInfo):
        self.userInfo = userInfo

    def validation_user_register(self):

        if self.userInfo['password'] == "Nhập Mật khẩu" or self.userInfo['password1'] == "Nhập Lại Mật khẩu" or self.userInfo['email'] == "Nhập Email" or self.userInfo['username'] == "Nhập Tên tài khoản":
            return False, "Phải nhập đầy đủ thông tin"

        if len(self.userInfo['username']) < 5:
            return False, "Tên tài khoản phải có ít nhất 5 ký tự!"
        if len(self.userInfo['password']) < 3:
            return False, "Mật khẩu phải có ít nhất 3 ký tự!"

        if not re.match(r"^[a-zA-Z0-9_]+$", self.userInfo['username']):
            return False, "Tên người dùng chỉ được chứa chữ cái, sô và dấu gạch dưới!"

        if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", self.userInfo['email']):
            return False, "Email không hợp lệ!"

        if self.userInfo['phone'] != "Nhập Số điện thoại":
            if not re.match(r"^0\d{9,10}$", self.userInfo['phone']):
                return False, "Số điện thoại phải có 10 hoặc 11 chữ số và bắt đầu bằng số 0!"

        if self.userInfo['dob'] != "Nhập Ngày sinh":
            try:
                show_date = datetime.strptime(self.userInfo['dob'], "%d/%m/%Y")
            except ValueError:
                return False, "Ngày sinh phải theo định dạng DD/MM/YYYY (VD: 01/06/2025)"

        # Kiểm tra nếu người dùng không nhập thì cho rỗng
        if self.userInfo['fullname'] == "Nhập Họ và Tên":
            self.userInfo['fullname'] = ""
        if self.userInfo['phone'] == "Nhập Số điện thoại":
            self.userInfo['phone'] = ""
        if self.userInfo['dob'] == "Nhập Ngày sinh":
            self.userInfo['dob'] = ""

        return True, ""

    @staticmethod
    def validation_password(password):
        if len(password) < 3:
            return False, "Mật khẩu phải có ít nhất 3 ký tự!"
        return True, ""
