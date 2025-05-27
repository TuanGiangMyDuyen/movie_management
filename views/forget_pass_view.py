from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import showerror, showinfo

from controllers.forget_password_controller import ForgetPasswordController
from utils.random_code import RandomCode


# -----------------
class ForgetPass:
    def __init__(self, root):
        # -------------------------
        self.email = None
        self.root = root
        self.forget_window = Toplevel(self.root)
        self.forget_window.title("Z+PlusCinema.ForgetPass")
        self.forget_window.geometry("500x350+520+200")
        self.forget_window.attributes('-topmost', True)
        self.forget_window.resizable(False, False)
        self.forget_window["bg"] = "#FAFAD2"
        self.forget_window.transient(self.root)
        self.forget_window.grab_set()
        # -------------------------
        Frame(self.forget_window, width=460, height=308, bg="white").place(x=20, y=20)
        self.winImg = PhotoImage(file="images/movie.png")

        Label(self.forget_window, bg="White", image=self.winImg).place(x=175, y=30)
        Label(self.forget_window, text="Quên Mật Khẩu", font=("Arial", 14, "bold"), bg="white").place(x=177, y=140)

        Label(self.forget_window, text="Vui lòng cung cấp Email đăng nhập, chúng tôi sẽ gửi mã kích hoạt cho bạn!",
              font=("Arial", 9), bg="white").place(x=45, y=170)
        # -------------------------
        Frame(self.forget_window, width=420, height=40, bg="White", highlightbackground="#FFA500", highlightthickness=2).place(
            x=40, y=212)
        Label(self.forget_window, text="Email", font=("Arial", 8), bg="white").place(x=45, y=200)
        self.winEn = Entry(self.forget_window, width=55, font=("Arial", 10), bg="white", border=0,
                           fg="gray")  # justify="center"
        self.winEn.place(x=55, y=223)
        self.winEn.insert(0, "Nhập Email")
        self.winEn.bind("<FocusIn>", self.on_enter_email)
        self.winEn.bind("<FocusOut>", self.on_leave_email)

        Button(self.forget_window, width=51, height=2, text="CẤP LẠI MẬT KHẨU", font=("Arial", 10, "bold"), border=0,
               bg="#FFA500", fg="white", activeforeground="white",
               activebackground="#FFA500", highlightbackground="#FFA500", highlightthickness=4, cursor="hand2",
               command=self.verify_email).place(x=40, y=255)
        self.link = Label(self.forget_window, text="Quay lại", font=("Arial", 9), fg="gray", bg="white")
        self.link.place(x=225, y=306)
        self.link.bind("<Button-1>", lambda e: self.return_loginWin())

    # -------------------------
    def on_enter_email(self, e):
        if self.winEn.get() == "Nhập Email":
            self.winEn.delete(0, "end")
            self.winEn.config(show="", fg="Black")

    def on_leave_email(self, e):
        if not self.winEn.get().strip():
            self.winEn.insert(0, "Nhập Email")
            self.winEn["fg"] = "gray"

    def verify_email(self):
        self.email = self.winEn.get()
        forget_controller = ForgetPasswordController(self.email)
        is_valid, message = forget_controller.verify_email()
        code_random = RandomCode().random_code()
        if is_valid:
            forget_controller.send_code(code_random)
            self.open_OTPcode(code_random)
        else: showerror("Lỗi", message)

    # -------------------------Giao diện OTP
    def open_OTPcode(self, code_random):
        # Xóa toàn bộ giao diện(widget) cũ
        for widget in self.forget_window.winfo_children():
            widget.destroy()
        self.forget_window.title("Z+PlusCinema.ForgetPass")
        self.forget_window.geometry("500x350+520+200")
        self.forget_window.resizable(False, False)
        self.forget_window["bg"] = "#FAFAD2"

        Frame(self.forget_window, width=460, height=308, bg="white").place(x=20, y=20)
        self.winImg = PhotoImage(file="images/movie.png")
        Label(self.forget_window, bg="White", image=self.winImg).place(x=175, y=30)
        Label(self.forget_window, text="Nhập Mã OTP", font=("Arial", 14, "bold"), bg="white").place(x=185, y=140)
        Label(self.forget_window, text="Vui lòng nhập mã OTP mà chúng tôi đã cung cấp qua Email của bạn!", font=("Arial", 9),
              bg="white").place(x=60, y=170)

        Frame(self.forget_window, width=410, height=40, bg="white", highlightbackground="#FFA500", highlightthickness=2).place(
            x=45, y=200)
        self.otp_entry = Entry(self.forget_window, width=42, font=("Arial", 12), justify="center", border=0, bg="white")
        self.otp_entry.place(x=60, y=210)

        Button(self.forget_window, width=50, text="XÁC NHẬN", height=2, font=("Arial", 10, "bold"), bg="#FFA500", fg="white",
               border=0,
               activebackground="#FFA500", highlightthickness=3, activeforeground="white", cursor="hand2",
               command=lambda: self.verify_otp(code_random)).place(x=45, y=243)

    # --------------------------
    def verify_otp(self, code_random):
        otp_code = self.otp_entry.get()
        is_valid, message = ForgetPasswordController.verify_code(otp_code, code_random)
        if is_valid:  # Thay bằng OTP thực tế
            messagebox.showinfo("Thành công", message)
            self.charnge_pass_ui()  # tới màn hình mật khẩu
        else:
            messagebox.showerror("Lỗi", message)

    # -------------------------Giao diện Thay đổi mật khẩu
    def charnge_pass_ui(self):
        for widget in self.forget_window.winfo_children():
            widget.destroy()
        self.forget_window.title("Z+PlusCinema.ChargPass")
        self.forget_window.geometry("500x370+520+200")
        self.forget_window.resizable(False, False)
        self.forget_window["bg"] = "#FAFAD2"

        Frame(self.forget_window, width=460, height=330, bg="white").place(x=20, y=20)
        self.winImg = PhotoImage(file="images/movie.png")
        Label(self.forget_window, bg="White", image=self.winImg).place(x=175, y=30)
        Label(self.forget_window, text="Nhập Mật Khẩu Mới", font=("Arial", 14, "bold"), bg="white").place(x=158, y=140)
        Label(self.forget_window, text="Vui lòng nhập mật khẩu mới của bạn!", font=("Arial", 9), bg="white").place(x=147,
                                                                                                            y=170)

        Frame(self.forget_window, width=293, height=30, bg="white", highlightbackground="#FFA500", highlightthickness=2).place(
            x=105, y=198)
        Label(self.forget_window, text="Mật khẩu", font=("Arial", 8), bg="white").place(x=109, y=187)
        self.userpass_En = Entry(self.forget_window, width=30, font=("Arial", 10), border=0, bg="white", fg="gray")
        self.userpass_En.place(x=115, y=204)
        self.userpass_En.insert(0, "Nhập Mật khẩu")
        self.userpass_En.bind('<FocusIn>', self.on_enter_userpass)
        self.userpass_En.bind('<FocusOut>', self.on_leave_userpass)

        Frame(self.forget_window, width=293, height=30, bg="white", highlightbackground="#FFA500", highlightthickness=2).place(
            x=105, y=239)
        Label(self.forget_window, text="Nhập lại mật khẩu", font=("Arial", 8), bg="white").place(x=109, y=228)
        self.userpass1_En = Entry(self.forget_window, width=30, font=("Arial", 10), border=0, bg="white", fg="gray")
        self.userpass1_En.place(x=115, y=245)
        self.userpass1_En.insert(0, "Nhập lại mật khẩu")
        self.userpass1_En.bind('<FocusIn>', self.on_enter_userpass1)
        self.userpass1_En.bind('<FocusOut>', self.on_leave_userpass1)

        Button(self.forget_window, width=35, text="XÁC NHẬN", font=("Arial", 10, "bold"), bg="#FFA500", fg="white", border=0,
               activebackground="#FFA500", highlightthickness=4, activeforeground="white", cursor="hand2", command=self.change_pass).place(x=105,
                                                                                                                 y=297)

        self.showing_pass = BooleanVar()  # Kiểm tra trạng thái hiện mật khẩu
        self.showing_pass.set(False)
        self.showPass_But = Checkbutton(self.forget_window, text=' Show password', variable=self.showing_pass, onvalue=True,
                                        offvalue=False, bg='White', activebackground="white",
                                        command=self.showHide_pass)  # Tạo ô check
        self.showPass_But.place(x=115, y=270)

        self.link = Label(self.forget_window, text="Quay lại đăng nhập", font=("Arial", 9), fg="gray", bg="white")
        self.link.place(x=195, y=330)
        self.link.bind("<Button-1>", lambda e: self.return_loginWin())

    def change_pass(self):
        password = self.userpass_En.get()
        password1 = self.userpass1_En.get()
        is_valid, message = ForgetPasswordController.change_pass(self.email, password, password1)
        if is_valid:
            showinfo("Thành công", message)
            self.forget_window.destroy()
        else: showerror("Lỗi", message)


    # -------------------------
    def on_enter_userpass(self, e):
        if self.userpass_En.get() == "Nhập Mật khẩu":
            self.userpass_En.delete(0, 'end')
            self.userpass_En.config(show='*', fg='Black')

    def on_leave_userpass(self, e):
        if not self.userpass_En.get().strip():
            self.userpass_En.insert(0, 'Nhập Mật khẩu')
            self.userpass_En.config(show='', fg='gray')

    def on_enter_userpass1(self, e):
        if self.userpass1_En.get() == "Nhập lại mật khẩu":
            self.userpass1_En.delete(0, 'end')
            self.userpass1_En.config(show='*', fg='Black')

    def on_leave_userpass1(self, e):
        if not self.userpass1_En.get().strip():
            self.userpass1_En.insert(0, 'Nhập lại mật khẩu')
            self.userpass1_En.config(show='', fg='gray')

    def showHide_pass(self):
        if self.showing_pass.get():  # Nếu checkbox được chọn (hiện mật khẩu)
            if self.userpass_En.get().strip() and self.userpass_En.get() != "Nhập Mật khẩu":
                self.userpass_En.config(show='')  # Hiển thị mật khẩu nếu có dữ liệu
            if self.userpass1_En.get().strip() and self.userpass1_En.get() != "Nhập lại mật khẩu":
                self.userpass1_En.config(show='')  # Hiển thị nhập lại mật khẩu nếu có dữ liệu
        else:  # Nếu checkbox không được chọn (ẩn mật khẩu)
            if self.userpass_En.get().strip() and self.userpass_En.get() != "Nhập Mật khẩu":
                self.userpass_En.config(show='*')  # Ẩn mật khẩu nếu đã nhập
            if self.userpass1_En.get().strip() and self.userpass1_En.get() != "Nhập lại mật khẩu":
                self.userpass1_En.config(show='*')  # Ẩn nhập lại mật khẩu nếu đã nhập

    # ---------------------------
    def return_loginWin(self):
        self.forget_window.destroy()