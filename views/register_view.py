from tkinter import *
from tkinter.messagebox import showinfo, showerror
from controllers.auth_controller import AuthController


class RegisterView:
    def __init__(self, root):
        self.root = root

        self.create_register_ui()

    def create_register_ui(self):
        """Mở cửa sổ đăng ký"""
        self.reg_window = Toplevel(self.root)
        self.reg_window.title('MovieAccountLogup')
        self.reg_window.geometry('450x690+550+55')
        self.reg_window.attributes('-topmost', True)
        self.reg_window.resizable(False, False)
        self.reg_window['bg'] = '#FAFAD2'
        self.reg_window.transient(self.root)
        self.reg_window.grab_set()
        winFram1 = Frame(self.reg_window, width=410, height=640, bg='White')
        winFram1.place(x=20, y=20)
        self.reg_img = PhotoImage(file='images/movie.png')
        reg_img_Label = Label(self.reg_window, image=self.reg_img, bg='White')
        reg_img_Label.place(x=150, y=25)

        self.tilSignUp = Label(self.reg_window, text='Đăng Kí Tài Khoản', font=('Arial', 15), bg='White', width=21)
        self.tilSignUp.place(x=110, y=150)

        Frame(self.reg_window, width=325, height=30, bg='White', bd=2, relief="groove").place(x=63, y=210)
        self.user = Label(self.reg_window, text='Tên tài khoản', font=('Monsterrat', 9), bg='White').place(x=70, y=195)
        self.user_En = Entry(self.reg_window, width=38, font=('Monsterrat', 10), border=0, bg='White', fg='gray')
        self.user_En.place(x=85, y=217)
        self.user_En.insert(0, 'Nhập Tên tài khoản')
        self.user_En.bind('<FocusIn>', self.on_enter_user)  # Gọi hàm khi click vào ô
        self.user_En.bind('<FocusOut>', self.on_leave_user)  # Gọi hàm khi rời khỏi ô

        Frame(self.reg_window, width=325, height=30, bg='White', bd=2, relief="groove").place(x=63, y=260)
        self.HoTen = Label(self.reg_window, text='Họ và tên', font=('Monsterrat', 9), bg='White').place(x=70, y=245)
        self.HoTen_En = Entry(self.reg_window, width=38, font=('Monsterrat', 10), fg='gray', border=0, bg='White')
        self.HoTen_En.place(x=85, y=267)
        self.HoTen_En.insert(0, 'Nhập Họ và Tên')
        self.HoTen_En.bind('<FocusIn>', self.on_enter_HoTen)
        self.HoTen_En.bind('<FocusOut>', self.on_leave_HoTen)

        Frame(self.reg_window, width=325, height=30, bg='White', bd=2, relief="groove").place(x=63, y=310)
        self.Email = Label(self.reg_window, text='Email', font=('Monsterrat', 9), bg='White').place(x=70, y=295)
        self.Email_En = Entry(self.reg_window, width=38, font=('Monsterrat', 10), fg='gray', border=0, bg='White')
        self.Email_En.place(x=85, y=317)
        self.Email_En.insert(0, 'Nhập Email')
        self.Email_En.bind('<FocusIn>', self.on_enter_Email)
        self.Email_En.bind('<FocusOut>', self.on_leave_Email)

        Frame(self.reg_window, width=325, height=30, bg='White', bd=2, relief="groove").place(x=63, y=360)
        self.SDT = Label(self.reg_window, text='Số điện thoại', font=('Monsterrat', 9), bg='White').place(x=70, y=345)
        self.SDT_En = Entry(self.reg_window, width=38, font=('Monsterrat', 10), fg='gray', border=0, bg='White')
        self.SDT_En.place(x=85, y=367)
        self.SDT_En.insert(0, 'Nhập Số điện thoại')
        self.SDT_En.bind('<FocusIn>', self.on_enter_SDT)
        self.SDT_En.bind('<FocusOut>', self.on_leave_SDT)

        Frame(self.reg_window, width=325, height=30, bg='White', bd=2, relief="groove").place(x=63, y=410)
        self.Date = Label(self.reg_window, text='Ngày sinh', font=('Monsterrat', 9), bg='White').place(x=70, y=395)
        self.Date_En = Entry(self.reg_window, width=30, font=('Monsterrat', 10), fg='gray', border=0, bg='White')
        self.Date_En.place(x=85, y=417)
        self.Date_En.insert(0, 'Nhập Ngày sinh')
        self.Date_En.bind('<FocusIn>', self.on_enter_Date)
        self.Date_En.bind('<FocusOut>', self.on_leave_Date)

        Frame(self.reg_window, width=325, height=30, bg='White', bd=2, relief="groove").place(x=63, y=460)
        self.userpass = Label(self.reg_window, text='Mật khẩu', font=('Monsterrat', 9), bg='White').place(x=70, y=445)
        self.userpass_En = Entry(self.reg_window, width=30, font=('Monsterrat', 10), fg='gray', border=0, bg='White')
        self.userpass_En.place(x=85, y=467)
        self.userpass_En.insert(0, 'Nhập Mật khẩu')
        self.userpass_En.bind('<FocusIn>', self.on_enter_userpass)
        self.userpass_En.bind('<FocusOut>', self.on_leave_userpass)

        Frame(self.reg_window, width=325, height=30, bg='White', bd=2, relief="groove").place(x=63, y=510)
        self.userpass1 = Label(self.reg_window, text='Nhập lại mật khẩu', font=('Monsterrat', 9), bg='White').place(
            x=70, y=495)
        self.userpass1_En = Entry(self.reg_window, width=30, font=('Monsterrat', 10), fg='gray', border=0, bg='White')
        self.userpass1_En.place(x=85, y=517)
        self.userpass1_En.insert(0, 'Nhập lại mật khẩu')
        self.userpass1_En.bind('<FocusIn>', self.on_enter_userpass1)
        self.userpass1_En.bind('<FocusOut>', self.on_leave_userpass1)

        self.showing_pass = BooleanVar()  # Kiểm tra trạng thái hiện mật khẩu
        self.showing_pass.set(False)
        self.showPass_But = Checkbutton(self.reg_window, text=' Show password', variable=self.showing_pass,
                                        onvalue=True, offvalue=False, bg='White',
                                        command=self.showHide_pass)  # Tạo ô check
        self.showPass_But.place(x=80, y=545)

        Button(self.reg_window, width=46, height=2, text='HOÀN THÀNH', font=('Monsterrat', 9), bg='#FFA500', border=0,
               command=self.register).place(x=61, y=580)

        self.link = Label(self.reg_window, text="Quay lại", font=("Arial", 9), fg="gray", bg="white")
        self.link.place(x=200, y=620)
        self.link.bind("<Button-1>", lambda e: self.destroy_ui())

    def on_enter_user(self, e):
        if self.user_En.get() == "Nhập Tên tài khoản":  # Nếu ô nhập có placeholder(biến tạm thời)
            self.user_En.delete(0, 'end')  # xóa
            self.user_En['fg'] = "Black"  # Màu chữ nhập liệu

    def on_leave_user(self, e):
        if not self.user_En.get().strip():  # Nếu ô nhập đang trống (không có dữ liệu)
            self.user_En.insert(0, 'Nhập Tên tài khoản')
            self.user_En['fg'] = 'gray'

    def on_enter_HoTen(self, e):
        if self.HoTen_En.get() == "Nhập Họ và Tên":
            self.HoTen_En.delete(0, 'end')
            self.HoTen_En['fg'] = 'Black'

    def on_leave_HoTen(self, e):
        if not self.HoTen_En.get().strip():
            self.HoTen_En.insert(0, 'Nhập Họ và Tên')
            self.HoTen_En['fg'] = 'gray'

    def on_enter_Email(self, e):
        if self.Email_En.get() == "Nhập Email":
            self.Email_En.delete(0, 'end')
            self.Email_En['fg'] = 'Black'

    def on_leave_Email(self, e):
        if not self.Email_En.get().strip():
            self.Email_En.insert(0, 'Nhập Email')
            self.Email_En['fg'] = 'gray'

    def on_enter_SDT(self, e):
        if self.SDT_En.get() == "Nhập Số điện thoại":
            self.SDT_En.delete(0, 'end')
            self.SDT_En['fg'] = 'Black'

    def on_leave_SDT(self, e):
        if not self.SDT_En.get().strip():
            self.SDT_En.insert(0, 'Nhập Số điện thoại')
            self.SDT_En['fg'] = 'gray'

    def on_enter_Date(self, e):
        if self.Date_En.get() == "Nhập Ngày sinh":
            self.Date_En.delete(0, 'end')
            self.Date_En['fg'] = 'Black'

    def on_leave_Date(self, e):
        if not self.Date_En.get().strip():
            self.Date_En.insert(0, 'Nhập Ngày sinh')
            self.Date_En['fg'] = 'gray'

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

    # -------------Show_pass----------------#
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

    def destroy_ui(self):
        self.reg_window.destroy()

    def register(self):
        userInfo = dict(
            username=self.user_En.get(),
            password=self.userpass_En.get(),
            password1=self.userpass1_En.get(),
            fullname=self.HoTen_En.get(),
            email=self.Email_En.get(),
            phone=self.SDT_En.get(),
            dob=self.Date_En.get()
        )
        auth_controller = AuthController(userInfo)
        is_valid, message = auth_controller.register_user()
        if is_valid:
            showinfo("Thành công", message)
            self.reg_window.destroy()
        else:
            showerror("Lỗi", message)
