from tkinter import *
from tkinter import messagebox

from controllers.auth_controller import AuthController
from views.login_admin_view import AdminLogin
from views.register_view import RegisterView
from views.forget_pass_view import ForgetPass
from views.user_view import MovieUserView


class LoginView:
    def __init__(self, root):
        self.root = root
        self.root.title("Z+PlusCinema.Login")
        self.root.geometry("450x690+550+55")
        self.root.attributes("-topmost", True)
        self.root["bg"] = "#FAFAD2"
        self.root.resizable(False, False)

        self.create_login_ui()

    def create_login_ui(self):
        # -----------------------
        self.winFr = Frame(self.root, width=410, height=650, bg="white").place(x=20, y=20)
        # -----------------------
        self.winPic = PhotoImage(file="images/movie.png")
        Label(self.root, image=self.winPic, bg='White').place(x=150, y=25)
        # -----------------------
        self.winTit = Label(self.root, text="Đăng Nhập Tài Khoản", font=("Arial", 15, "bold"), bg="White").place(
            x=123, y=150)
        # -----------------------
        Frame(self.root, width=325, height=30, bg='White', bd=2, relief="groove").place(x=63, y=210)
        self.user = Label(self.root, text='Tên tài khoản', font=('Arial', 9), bg='White').place(x=70, y=195)
        self.user_En = Entry(self.root, width=38, font=('Arial', 10), border=0, bg='White', fg='gray')
        self.user_En.place(x=85, y=217)
        self.user_En.insert(0, 'Nhập Tên tài khoản')
        self.user_En.bind('<FocusIn>', self.on_enter_user)  # Gọi hàm khi click vào ô
        self.user_En.bind('<FocusOut>', self.on_leave_user)  # Gọi hàm khi rời khỏi ô

        Frame(self.root, width=325, height=30, bg='White', bd=2, relief="groove").place(x=63, y=260)
        self.userpass = Label(self.root, text='Mật khẩu', font=('Arial', 9), bg='White').place(x=70, y=245)
        self.userpass_En = Entry(self.root, width=38, font=('Arial', 10), fg='gray', border=0, bg='White')
        self.userpass_En.place(x=85, y=267)
        self.userpass_En.insert(0, 'Nhập Mật khẩu')
        self.userpass_En.bind('<FocusIn>', self.on_enter_userpass)
        self.userpass_En.bind('<FocusOut>', self.on_leave_userpass)

        self.showing_pass = BooleanVar()  # Kiểm tra trạng thái hiện mật khẩu
        self.showing_pass.set(False)
        self.showPass_But = Checkbutton(self.root, text=' Show password', variable=self.showing_pass, onvalue=True,
                                        offvalue=False, bg='White', activebackground="white",
                                        command=self.showHide_pass)  # Tạo ô check
        self.showPass_But.place(x=80, y=295)

        self.winBut = Button(self.root, width=35, height=1, text="HOÀN THÀNH", font=("Arial", 13), bg="#FFA500",
                             border=0, cursor="hand2", activebackground="#FFA500", command=self.verify_login)
        self.winBut.place(x=64, y=325)

        self.link = Label(self.root, text="Quên Mật khẩu?", font=("Arial", 8), fg="gray", bg="white", cursor="hand2")
        self.link.place(x=185, y=363)
        self.link.bind("<Button-1>", lambda e: self.open_forget_pass_ui())

        Frame(self.winFr, width=320, height=2, bg="#D9D9D9").place(x=64, y=390)

        Frame(self.winFr, width=319, height=35, bg="white", highlightbackground="#FFA500", highlightthickness=3).place(
            x=64, y=400)
        self.winSign = Button(self.root, text="Đăng Kí", width=34, height=1,
                              font=("Arial", 13), fg="#FFA500", activeforeground="#FFA500", border=0, bg='white',
                              cursor="hand2", activebackground="white",
                              command=self.open_register_ui).place(x=67, y=403)

        Frame(self.winFr, width=319, height=35, bg="white", highlightbackground="#FFA500", highlightthickness=3).place(
            x=64, y=440)
        self.winSign = Button(self.root, text="Quản Trị Viên", width=34, height=1,
                              font=("Arial", 13), fg="#FFA500", activeforeground="#FFA500", border=0, bg='white',
                              cursor="hand2",
                              activebackground="white", command=self.open_login_admin_ui).place(x=67, y=443)

    def on_enter_user(self, e):
        if self.user_En.get() == "Nhập Tên tài khoản":
            self.user_En.delete(0, "end")
            self.user_En.config(show="", fg="black")

    def on_leave_user(self, e):
        if not self.user_En.get().strip():
            self.user_En.insert(0, "Nhập Tên tài khoản")
            self.user_En["fg"] = "gray"

    def on_enter_userpass(self, e):
        if self.userpass_En.get() == "Nhập Mật khẩu":
            self.userpass_En.delete(0, "end")
            self.userpass_En.config(show="*", fg="black")

    def on_leave_userpass(self, e):
        if not self.userpass_En.get().strip():
            self.userpass_En.insert(0, "Nhập Mật khẩu")
            self.userpass_En.config(show="", fg="gray")

    def showHide_pass(self):
        if self.showing_pass.get():
            if self.user_En.get().strip() and self.userpass_En.get() != "Nhập Mật khẩu":
                self.userpass_En.config(show="")
        else:
            if self.userpass_En.get().strip() and self.userpass_En.get() != "Nhập Mật khẩu":
                self.userpass_En.config(show="*")

    def verify_login(self):
        username = self.user_En.get()
        password = self.userpass_En.get()
        userInfo = dict(username= username, password= password)
        auth_controller = AuthController(userInfo)
        user = auth_controller.login_user("users")

        if user:
            messagebox.showinfo("Thành công", "Đăng nhập thành công")
            self.root.withdraw()
            MovieUserView(self.root)
        else:
            messagebox.showerror("Lỗi", "Sai tên người dùng hoặc mật khẩu")

    def open_register_ui(self):
        RegisterView(self.root)

    def open_forget_pass_ui(self):
        ForgetPass(self.root)

    def open_login_admin_ui(self):
        AdminLogin(self.root)
