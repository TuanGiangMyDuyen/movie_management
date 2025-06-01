from models.user_model import User
from utils.user_validation import UserValidation


class AuthController:
    def __init__(self, userInfo):
        self.userInfo = userInfo

    def login_user(self, role):
        userModel = User(self.userInfo)

        user = userModel.get_user(role)
        if user :
            if user['password'] == self.userInfo['password']:
                return user
            return None
        return None

    def register_user(self):
        userModel = User(self.userInfo)
        validation = UserValidation(self.userInfo)
        is_valid, message = validation.validation_user_register()

        if is_valid:
            if self.userInfo['password'] != self.userInfo['password1']:
                return False, "Mật khẩu không trùng khớp"
            else:
                del self.userInfo['password1']
            user = userModel.get_user("users")
            user1 = userModel.get_user_by_email(self.userInfo['email'])
            if user:
                return False, "Tên người dùng đã tồn tại!"
            elif user1:
                return False, "Email đã được đăng ký"
            else:
                userModel.save_user("users")
                return True, "Đăng kí thành công!"
        else: return False, message