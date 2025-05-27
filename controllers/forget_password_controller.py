from models.user_model import User
from utils.sendmail import SendMail
from utils.user_validation import UserValidation


class ForgetPasswordController:
    def __init__(self, email):
        self.email = email


    def verify_email(self):
        user = User.get_user_by_email(self.email)
        if user:
            return True, ""
        else: return False, "Email không tồn tại!"

    def send_code(self, code_random):
        send_mail = SendMail(self.email)
        content = {
            "subject": "Code Reset Password",
            "body": f"Xin chào bạn! \n Theo yêu cầu của bạn, chúng tôi xin gửi mã để lấy lại mật khẩu \n CODE: {code_random}"
        }
        send_mail.create_mail(content['subject'], content['body'])
        send_mail.send_mail()

    @staticmethod
    def verify_code(code, code1):
        if code1 == code:
            return True, "Xác thực thành công!"
        else:
            return False, "Mã xác thực sai!"

    @staticmethod
    def change_pass(email, password, password1):
        if password == password1:
            is_valid , message = UserValidation.validation_password(password)
            if not is_valid:
                return False, message

            user = User.get_user_by_email(email)
            user['password'] = password
            User.change_pass("users", user)
            return True, "Đổi mật khẩu thành công!"
        else: return False, "Mật khẩu không trùng khớp!"


