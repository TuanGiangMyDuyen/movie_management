from tkinter import *
from tkinter import messagebox
from controllers.auth_controller import AuthController
from views.admin_view import MovieAdminView

class AdminLogin:
    def __init__(self, root):
        self.root = root

        self.admin_login()

    def admin_login(self):
        self.admin_window = Toplevel(self.root)
        self.admin_window.title("Z+PlusCinema.AdminLogin")
        self.admin_window.geometry("500x350+520+200")
        self.admin_window.attributes('-topmost', True)
        self.admin_window.resizable(False, False)
        self.admin_window["bg"] = "#FAFAD2"
        self.admin_window.transient(self.root)
        self.admin_window.grab_set()
        # --------------------------------------------------
        Label(self.admin_window, text="ĐĂNG NHẬP", font=("Arial", 15, "bold"), bg="#FAFAD2", fg="red").pack(
            pady=(50, 3))
        Label(self.admin_window, text="Đăng nhập với tư cách là Admin!!", font=("Arial", 9), bg="#FAFAD2").pack(
            pady=(0, 15))

        self.admin_name_frame = Frame(self.admin_window, width=300, height=35, bg="white", highlightbackground="black",
                                      highlightthickness=2,
                                      highlightcolor="Black")  # dùng highlightcolor để kh đổi màu viền do entry gây ra
        self.admin_name_frame.pack(pady=(2, 4))
        self.admin_name = Entry(self.admin_name_frame, width=32, bg="white", font=("Arial", 13), fg="gray",
                                highlightbackground="white", bd=0, cursor="hand2")
        self.admin_name.place(x=3, y=5)
        self.admin_name.insert(0, "Nhập tên tài khoản")
        self.admin_name.bind("<FocusIn>", self.on_enter_admin_name)
        self.admin_name.bind("<FocusOut>", self.on_leave_admin_name)

        self.admin_pass_frame = Frame(self.admin_window, width=300, height=35, bg="white", highlightbackground="black",
                                      highlightthickness=2, highlightcolor="Black")
        self.admin_pass_frame.pack(pady=(2, 6))
        self.admin_pass = Entry(self.admin_pass_frame, width=32, bg="white", font=("Arial", 13), fg="gray",
                                highlightbackground="white", bd=0, cursor="hand2")
        self.admin_pass.place(x=3, y=5)
        self.admin_pass.insert(0, "Nhập mật khẩu")
        self.admin_pass.bind("<FocusIn>", self.on_enter_admin_pass)
        self.admin_pass.bind("<FocusOut>", self.on_leave_admin_pass)

        self.showing_pass = BooleanVar()  # Kiểm tra trạng thái hiện mật khẩu
        self.showing_pass.set(False)
        self.showPass_But = Checkbutton(self.admin_window, text='Show password', variable=self.showing_pass,
                                        onvalue=True,
                                        offvalue=False, bg='#FAFAD2', activebackground="#FAFAD2",
                                        command=self.showHide_pass)  # Tạo ô check
        self.showPass_But.pack(pady=(0, 3))

        self.submit_btn = Button(self.admin_window, width=42, height=2, text='HOÀN THÀNH',
                                 font=('Monsterrat', 9, "bold"), fg="black", bg='#FFD700', border=0,
                                 activebackground="#FFA500", state="disabled", command=self.verify_login)
        self.submit_btn.pack(pady=(3, 10))  # Tạo hiệu ứng khi nhập đủ dữ liệu thì button sẽ sẵn sàng bấm

    # Liên kết sự kiện nhập liệu
        self.admin_name.bind("<KeyRelease>", self.check_entries)
        self.admin_pass.bind("<KeyRelease>", self.check_entries)

    def check_entries(self, event=None):#kiểm tra dữ liệu nhập
        admin = self.admin_name.get().strip()# gán dữ liệu nhập đã loại bỏ khoảng trắng đầu và cuối chuỗi
        password = self.admin_pass.get().strip()
    # nếu không nhập dữ liệu mới hoặc dữ liệu = giá trị mặc định (name)
    # nếu không nhập dữ liệu mới hoặc dữ liệu = giá trị mặc định (mật khẩu)
        if not admin or admin == "Nhập tên tài khoản" or not password or password == "Nhập mật khẩu":
            self.submit_btn.config(bg="#FFD700",fg="gray",state="disabled") #button có màu vàng nhạt và bị vô hiệu hóa (disabled)
        else:
            self.submit_btn.config(bg="#FFA500",fg="black",state="normal") # button sẵn sàng nhập(normal)

    def on_enter_admin_name(self, e):  # kiểm tra dữ liệu khi nhấp vào entry name
        if self.admin_name.get() == "Nhập tên tài khoản":  # nếu giá trị được lấy hiện tại(get()) == dữ liệu ban đầu (đã insert)
            self.admin_name.delete(0, "end")
            self.admin_name.config(fg="black")

    def on_leave_admin_name(self, e):
        if not self.admin_name.get().strip():
            self.admin_name.insert(0, "Nhập tên tài khoản")
            self.admin_name["fg"] = "gray"

    def on_enter_admin_pass(self, e):
        if self.admin_pass.get() == "Nhập mật khẩu":
            self.admin_pass.delete(0, "end")
            self.admin_pass.config(show="*", fg="black")

    def on_leave_admin_pass(self, e):
        if not self.admin_pass.get().strip():
            self.admin_pass.insert(0, "Nhập mật khẩu")
            self.admin_pass.config(show="", fg="gray")

    def showHide_pass(self):
        if self.showing_pass.get():
            if self.admin_pass.get().strip() and self.admin_pass.get() != "Nhập mật khẩu":
                self.admin_pass.config(show="")
        else:
            if self.admin_pass.get().strip() and self.admin_pass.get() != "Nhập mật khẩu":
                self.admin_pass.config(show="*")

    def verify_login(self):
        adminname = self.admin_name.get()
        adminpass = self.admin_pass.get()
        adminInfo = dict(username=adminname, password=adminpass)
        auth_controller = AuthController(adminInfo)
        admin = auth_controller.login_user("admins")
        if admin:
            messagebox.showinfo("Thành công", "Đăng nhập thành công")
            self.admin_window.destroy()
            self.root.withdraw()
            MovieAdminView(self.root)
        else:
            messagebox.showerror("Lỗi", "Sai tên người dùng hoặc mật khẩu")

