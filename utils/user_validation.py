import re

class UserValidation:
    def __init__(self, userInfo):
        self.userInfo = userInfo

    def validation_user_register(self):

        if self.userInfo['username'] == "Nhập Họ và Tên" or self.userInfo['password'] == "Nhập Mật khẩu" or self.userInfo['password1'] == "Nhập Lại Mật khẩu" or self.userInfo['email'] == "Nhập Email" or self.userInfo['phone'] == "Nhập Số Điện Thoại" or self.userInfo['dob'] == "Nhập Ngày sinh":
            return False, "Phải nhập đầy đủ thông tin"

        if len(self.userInfo['username']) < 5:
            return False, "Tên tài khoản phải có ít nhất 5 ký tự!"
        if len(self.userInfo['password']) < 3:
            return False, "Mật khẩu phải có ít nhất 3 ký tự!"

        if not re.match(r"^[a-zA-Z0-9_]+$", self.userInfo['username']):
            return False, "Chỉ được chứa chữ cái, sô và dấu gạch dưới!"

        if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", self.userInfo['email']):
            return False, "Email không hợp lệ!"

        return True, ""

    @staticmethod
    def validation_password(password):
        if len(password) < 3:
            return False, "Mật khẩu phải có ít nhất 3 ký tự!"
        return True, ""
