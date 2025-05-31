from tkinter import *
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk
from controllers.movie_controller import MovieController
from models.movie_model import Movie
from tkinter.ttk import Combobox
from tkcalendar import DateEntry


class CreateMovieView:
    def __init__(self, root, admin_view):
        self.admin_view = admin_view
        self.SHOW_TIMES = [
    "09:00", "11:30", "14:00", "16:30", "19:00", "21:30"
]
        self.ROOMS = ['PC001', 'PC002', 'PC003', 'PC004', 'PC005', 'PC006', 'PC007']
        self.STATUS = ['Đang chiếu', 'Ngưng chiếu']
        self.add_win = Toplevel(root)
        self.add_win.title("Thêm phim mới")
        self.add_win.geometry("700x600+350+150")
        self.add_win.resizable(False,False)
        self.add_win.config(bg="#213448")
        # Frame chính bao bọc toàn bộ nội dung
        self.frame_win = Frame(self.add_win, bg="white")
        self.frame_win.pack(fill="both", expand=True, padx=10, pady=10)

        # Frame bên trái chứa img_frame và nút ADD
        left_frame = Frame(self.frame_win, bg="white")
        left_frame.pack(side="left", padx=(5, 0), pady=(2, 0))

        # Frame chứa poster phim
        self.img_frame = Frame(left_frame, width=200, height=250, bg="#A2B9A7")
        self.img_frame.pack_propagate(False)
        self.img_frame.pack(side="top")

        # Button add poster phim
        img_button = Button(left_frame, width=15, text="ADD", font=("Arial", 9, "bold"), bg="#F4631E",
                            activebackground="#F0BB78", bd=0, command=self.add_poster)
        img_button.pack(fill="x", side="top", pady=(1, 0))

        # Frame bên phải chứa tiêu đề và các Entry
        right_frame = Frame(self.frame_win, bg="#F3F3E0")
        right_frame.pack(side="right", fill="both", expand=True, padx=(5, 5), pady=(10, 10))

        # Frame chứa tiêu đề
        title_frame = Frame(right_frame, bg="#F4631E")
        title_frame.pack(fill="x")

        # Tiêu đề
        Label(title_frame, text="NHẬP THÔNG TIN CHI TIẾT PHIM", font=("Arial", 10, "bold"), bg="#F4631E").pack(fill="x",
        padx=(20, 5),pady=(5, 0))

        # Tạo Canvas và Scrollbar để chứa các Entry
        self.canvas = Canvas(right_frame, bg="#F3F3E0")
        scrollbar = ttk.Scrollbar(right_frame, orient="vertical", command=self.canvas.yview)
        add_frame = Frame(self.canvas, bg="#F3F3E0")  # Frame chứa các Entry

        # Liên kết Canvas với Scrollbar
        self.canvas.configure(yscrollcommand=scrollbar.set)

        # Đặt Canvas và Scrollbar vào giao diện
        scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)

        # Tạo một cửa sổ trong Canvas để chứa add_frame
        canvas_frame = self.canvas.create_window((0, 0), window=add_frame, anchor="nw")

        # Cấu hình font
        label_font = ("Arial", 10, "bold")
        entry_font = ("Arial", 10)

        # Tên phim
        Label(add_frame, text="Tên phim: ", font=label_font, bg="#F3F3E0").grid(row=1, column=0, padx=5, pady=5,
                                                                                sticky="w")
        self.name_entry = Entry(add_frame, font=entry_font, width=30)
        self.name_entry.grid(row=1, column=1, padx=5, pady=5)

        # Thể loại
        Label(add_frame, text="Thể loại: ", font=label_font, bg="#F3F3E0").grid(row=2, column=0, padx=5, pady=5,
                                                                                sticky="w")
        self.genre_entry = Entry(add_frame, font=entry_font, width=30)
        self.genre_entry.grid(row=2, column=1, padx=5, pady=5)

        # Đạo diễn
        Label(add_frame, text="Đạo diễn: ", font=label_font, bg="#F3F3E0").grid(row=3, column=0, padx=5, pady=5,
                                                                                sticky="w")
        self.director_entry = Entry(add_frame, font=entry_font, width=30)
        self.director_entry.grid(row=3, column=1, padx=5, pady=5)

        # Diễn viên
        Label(add_frame, text="Diễn viên: ", font=label_font, bg="#F3F3E0").grid(row=4, column=0, padx=5, pady=5,
                                                                                 sticky="w")
        self.actors_entry = Entry(add_frame, font=entry_font, width=30)
        self.actors_entry.grid(row=4, column=1, padx=5, pady=5)

        # Ngôn ngữ
        Label(add_frame, text="Ngôn ngữ: ", font=label_font, bg="#F3F3E0").grid(row=5, column=0, padx=5, pady=5,
                                                                                sticky="w")
        self.language_entry = Entry(add_frame, font=entry_font, width=30)
        self.language_entry.grid(row=5, column=1, padx=5, pady=5)

        # Thời lượng
        Label(add_frame, text="Thời lượng (phút): ", font=label_font, bg="#F3F3E0").grid(row=6, column=0, padx=5,
                                                                                         pady=5, sticky="w")
        self.duration_entry = Entry(add_frame, font=entry_font, width=30)
        self.duration_entry.grid(row=6, column=1, padx=5, pady=5)

        # Giá vé
        Label(add_frame, text="Giá vé (VNĐ): ", font=label_font, bg="#F3F3E0").grid(row=7, column=0, padx=5, pady=5,
                                                                                    sticky="w")
        self.price_entry = Entry(add_frame, font=entry_font, width=30)
        self.price_entry.grid(row=7, column=1, padx=5, pady=5)

        # Mô tả
        Label(add_frame, text="Mô tả: ", font=label_font, bg="#F3F3E0").grid(row=8, column=0, padx=5, pady=5,
                                                                             sticky="w")
        self.description_entry = Entry(add_frame, font=entry_font, width=30)
        self.description_entry.grid(row=8, column=1, padx=5, pady=5)

        # Xếp hạng (rated)
        Label(add_frame, text="Xếp hạng: ", font=label_font, bg="#F3F3E0").grid(row=9, column=0, padx=5, pady=5,
                                                                                 sticky="w")
        self.rated_entry = Entry(add_frame, font=entry_font, width=30)
        self.rated_entry.grid(row=9, column=1, padx=5, pady=5)

        # Trạng thái
        Label(add_frame, text="Trạng thái: ", font=label_font, bg="#F3F3E0").grid(row=10, column=0, padx=5, pady=5,
                                                                                  sticky="w")
        self.status_combobox = Combobox(add_frame, font=entry_font, width=28, state="readonly")
        self.status_combobox['values'] = self.STATUS
        self.status_combobox.grid(row=10, column=1, padx=5, pady=5)
        self.status_combobox.current(0)  # Mặc định chọn trạng thái đang chiếu

        # Ngày chiếu
        Label(add_frame, text="Ngày chiếu: ", font=label_font, bg="#F3F3E0").grid(row=11, column=0, padx=5, pady=5,sticky="w")
        self.release_date_entry = DateEntry(add_frame, font=entry_font, width=28, background='darkblue',foreground='white', borderwidth=2, date_pattern='dd/mm/yyyy')
        self.release_date_entry.grid(row=11, column=1, padx=5, pady=5)

        # Phòng chiếu
        Label(add_frame, text="Phòng chiếu: ", font=label_font, bg="#F3F3E0").grid(row=13, column=0, padx=5, pady=5,
                                                                                   sticky="w")
        self.room_combobox = Combobox(add_frame, font=entry_font, width=28, state="readonly")
        self.room_combobox['values'] = self.ROOMS
        self.room_combobox.grid(row=13, column=1, padx=5, pady=5)
        self.room_combobox.current(0)  # Mặc định chọn phòng đầu tiên

        # Loại suất chiếu
        Label(add_frame, text="Loại suất chiếu: ", font=label_font, bg="#F3F3E0").grid(row=14, column=0, padx=5, pady=5,
                                                                                       sticky="w")
        self.showtime_type_entry = Entry(add_frame, font=entry_font, width=30)
        self.showtime_type_entry.grid(row=14, column=1, padx=5, pady=5)

        # Suất chiếu
        Label(add_frame, text="Suất chiếu: ", font=label_font, bg="#F3F3E0").grid(row=15, column=0, padx=5, pady=5,sticky="w")
        self.showtime_combobox = Combobox(add_frame, font=entry_font, width=28, state="readonly")
        self.showtime_combobox['values'] = self.SHOW_TIMES
        self.showtime_combobox.grid(row=15, column=1, padx=5, pady=5)
        self.showtime_combobox.current(0)  # Mặc định chọn khung giờ đầu tiên

        # Tổng số ghế
        Label(add_frame, text="Tổng số ghế: ", font=label_font, bg="#F3F3E0").grid(row=16, column=0, padx=5, pady=5,
                                                                                   sticky="w")
        self.total_seats_entry = Entry(add_frame, font=entry_font, width=30)
        self.total_seats_entry.grid(row=16, column=1, padx=5, pady=5)

        # Số ghế trống
        Label(add_frame, text="Số ghế trống: ", font=label_font, bg="#F3F3E0").grid(row=17, column=0, padx=5, pady=5,
                                                                                    sticky="w")
        self.available_seats_entry = Entry(add_frame, font=entry_font, width=30)
        self.available_seats_entry.grid(row=17, column=1, padx=5, pady=5)



        # Cấu hình trọng số cho cột để canh giữa nút
        add_frame.grid_columnconfigure(0, weight=1)
        add_frame.grid_columnconfigure(1, weight=1)
        add_frame.grid_rowconfigure(18, weight=1)

        # Đặt nút với sticky="ew" để kéo giãn theo chiều ngang nhưng vẫn canh giữa
        Button(add_frame, text="Lưu", font=("Arial", 10, "bold"), bg="#F4631E", fg="white", command=self.create_movie,activebackground="#E78B48",bd=0,activeforeground="white").grid(row=18, column=0, columnspan=2, pady=10,padx=10, sticky="ew")

        # Cập nhật vùng cuộn của Canvas khi kích thước của add_frame thay đổi
        def configure_canvas(event):
            self.canvas.configure(scrollregion=self.canvas.bbox("all"))

        add_frame.bind("<Configure>", configure_canvas)

        # Cập nhật kích thước của Canvas khi cửa sổ thay đổi
        def configure_frame(event):
            self.canvas.itemconfig(canvas_frame, width=event.width)

        self.canvas.bind("<Configure>", configure_frame)

        # Thêm sự kiện cuộn chuột
        def on_mousewheel(event):
            self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        self.canvas.bind_all("<MouseWheel>", on_mousewheel)

    def add_poster(self):
        # Xóa các widget cũ (ảnh cũ) trong img_frame
        for widget in self.img_frame.winfo_children():
            widget.destroy()

        self.filepath = filedialog.askopenfilename(
            title="Chọn ảnh",
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif *.bmp")]
        )

        if not self.filepath:
            messagebox.showwarning("Thông báo", "Bạn chưa chọn ảnh.")
            return

        try:
            # Mở ảnh bằng PIL
            image = Image.open(self.filepath)

            # Lấy kích thước frame
            self.img_frame.update()
            frame_width = self.img_frame.winfo_width()
            frame_height = self.img_frame.winfo_height()

            # Resize ảnh để vừa với frame
            resized_image = image.resize((frame_width, frame_height), Image.Resampling.LANCZOS)
            self.poster_img = ImageTk.PhotoImage(resized_image)

            # Hiển thị ảnh trong label
            self.poster_label = Label(self.img_frame, image=self.poster_img)
            self.poster_label.image = self.poster_img  # Giữ tham chiếu để ảnh không bị xóa
            self.poster_label.pack(expand=True, fill="both")

        except Exception as e:
            Label(self.img_frame, text="Không thể tải ảnh", bg="blue", fg="white").pack(expand=True)
            print("Lỗi ảnh:", e)


    def create_movie(self):
        movieInfo = {
            "name": self.name_entry.get(),
            "genre": self.genre_entry.get(),
            "actors": self.actors_entry.get(),
            "director": self.director_entry.get(),
            "language": self.language_entry.get(),
            "rated": self.rated_entry.get(),
            "description": self.description_entry.get(),
            "show_date": self.release_date_entry.get(),
            "duration_minutes": self.duration_entry.get(),
            "status": self.status_combobox.get(),
            "showtime": self.showtime_combobox.get(),
            "room": self.room_combobox.get(),
            "total_seats": self.total_seats_entry.get(),
            "available_seats": self.available_seats_entry.get(),
            "ticket_price": self.price_entry.get(),
            "showtime_type": self.showtime_type_entry.get(),
            "poster_url": getattr(self, "filepath", "")
        }
        movie_controller = MovieController(movieInfo)
        isValid, message = movie_controller.create_movie()
        if not isValid:
            messagebox.showerror("Lỗi", message)
        else:
            messagebox.showinfo("Thành công", message)
            # Reload lại danh sách mới
            self.admin_view.movies = Movie.get_movies()
            self.admin_view.refresh_treeview()
            self.canvas.unbind_all("<MouseWheel>")
            # Xóa giao diện
            self.add_win.destroy()