from tkinter import *
from tkinter import messagebox
import requests
from PIL import Image, ImageTk

from controllers.movie_controller import MovieController
from io import BytesIO
from views import movie_detail_user_view


class MovieUserView:
    def __init__(self, root):
        self.root = root
        self.detail_movie = None
        self.create_user_ui()

    def create_user_ui(self):
        self.movie_window = Toplevel(self.root)
        self.movie_window.protocol("WM_DELETE_WINDOW", self.quit_app)
        self.movie_window.title("Z+Plus.Movie")
        self.movie_window.geometry("1100x700+160+30")
        self.movie_window["bg"] = "#000011"
        self.movie_window.resizable(False, False)
        self.main_Fr = Frame(self.movie_window, width=1090, height=74, bg="#222222")
        self.main_Fr.place(x=5, y=4)
        # --------------------------------------------------------------
        # logo
        self.img = PhotoImage(file="images/logo.png")
        Label(self.movie_window, image=self.img, bg="#222222").place(x=100, y=4)
        Label(self.movie_window, text="Z+ Plus", fg="white", bg="#222222", font=("Montserrat", 13, "bold")).place(x=180,
                                                                                                                  y=15)
        Label(self.movie_window, text="Phim hay tại rạp", fg="white", bg="#222222", font=("Montserrat", 9)).place(x=180,
                                                                                                                  y=40)

        # Tim kiem
        Frame(self.movie_window, width=390, height=39, bg="#444444", highlightbackground="white",
              highlightthickness=2).place(
            x=676, y=24)
        self.imgSearch = PhotoImage(file="images/kinhlup.png")
        Label(self.movie_window, image=self.imgSearch, bg="#444444").place(x=685, y=27)
        self.search = Entry(self.movie_window, fg="white", font=("Arial", 10), width=45, bg="#444444", bd=0)
        self.search.place(x=725, y=34)
        self.search.insert(0, "Tìm kiếm phim")
        self.search.bind("<FocusIn>", self.on_enter_search)
        self.search.bind("<FocusOut>", self.on_leave_search)

        Frame(self.movie_window, width=1090, height=40, bg="#363636").place(x=5, y=80)

        # Tài khoản
        self.account = Label(self.movie_window, text="Đăng xuất", bg="#363636", fg="white",
                             font=("Montserrat", 11, "underline"),
                             activebackground="black", activeforeground="white", border=0)
        self.account.place(x=1000, y=88)
        self.account.bind("<Button-1>", self.logout_user)
        # --------------------------------------------------------------
        # Tạo Canvas và thanh cuộn
        self.main_Ca = Frame(self.movie_window, highlightthickness=0, bd=0)
        self.main_Ca.place(x=3, y=120)

        canvas = Canvas(self.main_Ca, bg="#000011", width=1075, height=580, highlightthickness=0, bd=0)
        scrollbar = Scrollbar(self.main_Ca, orient=VERTICAL, command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=RIGHT, fill=Y)
        canvas.pack(side=LEFT, fill=BOTH, expand=True)

        # Frame cuộn bên trong Canvas
        scrollable_frame = Frame(canvas, bg="#000011", highlightthickness=0, bd=0)
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        # --------------------------------------------------
        # Đọc dữ liệu từ file JSON
        movies = MovieController.get_movies()
        # Hiển thị poster phim và tên phim dưới dạng button
        columns = 3
        for index, movie in enumerate(movies):
            row = index // columns  # 3 poster mỗi hàng, mỗi phim chiếm 3 dòng: ảnh, tên phim, đạo diễn
            col = index % columns
            poster_url = movie['poster_url']
            try:
                # Lấy ảnh từ URL
                response = requests.get(poster_url)
                if response.status_code == 200:
                    image_data = response.content
                    image = Image.open(BytesIO(image_data))
                    image = image.resize((130, 180))  # Resize ảnh poster
                    photo = ImageTk.PhotoImage(image)
                else:
                    raise Exception("Không thể tải ảnh")
            except Exception as e:
                print(f"Lỗi khi tải ảnh cho phim {movie['name']}: {e}")
                continue
            # cố định kích thước mỗi frame bộ phim
            movie_frame = Frame(scrollable_frame, width=320, height=200)
            movie_frame.grid(row=row, column=col, padx=(2, 10), pady=8)
            movie_frame.grid_propagate(False)  # Không cho tự co giãn theo nội dung

            # Tạo frame chứa poster+thông tin phim
            content_frame = Frame(movie_frame, bg="#1E2029")
            content_frame.pack(fill="both", expand=True)

            # hiển thị poster
            poster_label = Label(content_frame, image=photo, bg="#1E2029")
            poster_label.image = photo  # Lưu tham chiếu để tránh bị xóa
            poster_label.pack(side="left", padx=5, pady=5)

            # Tạo frame chứa tên,tác giả phim
            info_frame = Frame(content_frame, bg="#1E2029", width=200, height=180)
            info_frame.pack(side="right", padx=2, fill="y")
            info_frame.pack_propagate(False)  # Không cho tự co giãn theo nội dung

            # Hiển thị tên phim
            name_label = Label(info_frame, text=movie["name"], bg="#1E2029", fg="yellow",
                               font=("Montserrat", 12, "bold"), wraplength=200, justify="left")
            name_label.pack(anchor="w", padx=3, pady=(3, 3))  # khoảng cách trên 10, khoảng cách dưới 5

            # Hiển thị tên đạo diễn
            frame_director = Frame(info_frame, bg="#1E2029")
            Label(frame_director, text="Tác giả: ", bg="#1E2029", fg="white", font=("Arial", 10, "bold")).pack(
                side="left", anchor="n")
            Label(frame_director, text=movie["director"], bg="#1E2029", fg="white", font=("Arial", 9), wraplength=120,
                  anchor="nw").pack(side="left")
            frame_director.pack(anchor="w", padx=3)

            # Thể loại
            frame_type = Frame(info_frame, bg="#1E2029")
            Label(frame_type, text="Thể loại: ", bg="#1E2029", fg="white", font=("Arial", 10, "bold")).pack(side="left",
                                                                                                            anchor="n")
            Label(frame_type, text=f"{movie["genre"]}", bg="#1E2029", fg="white", font=("Arial", 9), wraplength=120,
                  justify="left", anchor="nw").pack(side="left")
            frame_type.pack(anchor="w", padx=4)

            # Mô tả
            frame_description = Frame(info_frame, bg="#1E2029")
            Label(frame_description, text="Mô tả:", bg="#1E2029", fg="white", font=("Arial", 10, "bold")).pack(
                side="left", anchor="n")
            short_description = " ".join(movie["description"].split()[:7]) + "..."
            Label(frame_description, text=short_description, bg="#1E2029", fg="white", font=("Arial", 9),
                  justify="left", wraplength=150, anchor="nw").pack(side="left")
            frame_description.pack(anchor="w", padx=3)

            # Link dẫn
            frame_see_more = Frame(info_frame, bg="#1E2029")
            frame_see_more.pack(side="bottom", pady=5, fill="x")
            label_see_more = Label(frame_see_more, text="Xem thêm", fg="yellow", bg="#1E2029", font=("Arial", 8),
                                   cursor="hand2")
            label_see_more.pack(side="right", pady=2, padx=5)
            label_see_more.bind("<Button-1>", lambda e, m=movie: self.open_link(e, m))

    def open_link(self, e, movie):
        # Nếu cửa sổ chi tiết chưa tồn tại hoặc đã bị đóng, tạo mới
        if self.detail_movie is None or not self.detail_movie.movie_window.winfo_exists():
            self.detail_movie = movie_detail_user_view.MovieDetailView(self.root, movie)
        else:
            # Nếu cửa sổ đã tồn tại, cập nhật nội dung với phim mới
            self.detail_movie.update_movie(movie)
        # Đưa cửa sổ lên trên cùng
        self.detail_movie.movie_window.lift()

    def on_enter_search(self, e):
        if self.search.get() == "Tìm kiếm phim":
            self.search.delete(0, "end")
            self.search.config(show="", fg="white")

    def on_leave_search(self, e):
        if not self.search.get().strip():
            self.search.insert(0, "Tìm kiếm phim")
            self.search["fg"] = "white"

    def logout_user(self, event):
        if messagebox.askyesno("Đăng xuất", "Bạn có chắc muốn đăng xuất?"):
            self.movie_window.destroy()
            self.root.deiconify()

    def quit_app(self):
        self.root.destroy()
