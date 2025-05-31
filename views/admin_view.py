from tkinter import *
from tkinter import ttk, messagebox
from models.movie_model import Movie
from controllers.movie_controller import MovieController
from views.create_movie_view import CreateMovieView
from views.update_movie_view import UpdateMovieView
from views.movie_detail_admin_view import MovieDetailAdminView
import threading


class MovieAdminView():
    def __init__(self, root):
        self.root = root
        self.admin_win = Toplevel(self.root)
        self.admin_win.protocol("WM_DELETE_WINDOW", self.quit_app)
        self.admin_win.title("Trang Quản Lý")
        self.admin_win.geometry("1000x700+260+30")
        self.admin_win["bg"] = "#000011"
        self.admin_win.resizable(False, False)
        self.main_Fr = Frame(self.admin_win, width=990, height=74, bg="#222222")
        self.main_Fr.place(x=5, y=4)

        # Logo
        self.img = PhotoImage(file="images/logo.png")
        self.label_image = Label(self.main_Fr, image=self.img, bg="#222222")
        self.label_image.image = self.img
        self.label_image.place(x=15, y=2)
        Label(self.main_Fr, text="TRANG CHỦ QUẢN LÝ", font=("Montserrat", 15, "bold"), fg="white", bg="#222222").place(x=100, y=13)
        Label(self.main_Fr, text="Z+PlusCinema", font=("Montserrat", 9), fg="yellow", bg="#222222").place(x=100, y=39)
        # Tài khoản
        self.account = Label(self.main_Fr,text="Đăng xuất",font=("Arial",10,"underline"),bg="#222222",fg="white",
                             cursor="hand2")
        self.account.place(x=920,y=50)
        self.account.bind("<Button-1>",self.open_login_admin_view)

        # Tạo frame chứa table danh sách phim
        self.admin_frame = Frame(self.admin_win, width=990, height=612, bg="white")
        self.admin_frame.place(x=5, y=82)
        self.noteTab = ttk.Notebook(self.admin_frame)
        self.noteTab.place(x=3, y=3, width=984, height=608)

        # Tạo tab1
        self.tab1_frame = Frame(self.noteTab, bg="#D7D7D7")
        Label(self.tab1_frame, text="DANH SÁCH QUẢN LÝ", fg="Black", font=("Montserrat", 20, "bold"),
              bg="#D7D7D7").pack(padx=10)
        self.noteTab.add(self.tab1_frame, text="Trang Chủ")

        # Thông tin tìm kiếm
        Label(self.tab1_frame, text="Tên phim: ", font=("Arial", 10, "bold"), bg="#D7D7D7").place(x=460, y=80)
        self.tab1_movie_entry = Entry(self.tab1_frame, font=("Arial", 11), width=32, bg="white", border=1)
        self.tab1_movie_entry.place(x=535, y=81)
        self.tab1_movie_button = Button(self.tab1_frame, width=10, text="Tìm kiếm", font=("Arial", 9), bg="#C1BAA1",
                                        activebackground="#A59D84", bd=0, command=self.search_movie)
        self.tab1_movie_button.place(x=800, y=80)

        # Button xuất selection
        # Xóa các radio button cũ nếu có
        for widget in self.tab1_frame.winfo_children():
            if isinstance(widget, Radiobutton):
                widget.destroy()

        # Tạo biến IntVar để lưu trạng thái của Radiobutton
        self.radio_var = IntVar()
        self.radio_var.set(3)  # Mặc định chọn "Tất cả"

        # Tạo các Radiobutton
        self.frame_selection = Frame(self.tab1_frame, bg="#D7D7D7")
        self.frame_selection.pack(pady=(5, 2))
        radiobutton1 = Radiobutton(self.frame_selection, text="Đang chiếu", bg="#D7D7D7", activebackground="#D7D7D7",
                                   variable=self.radio_var, value=1, command=self.filter_movies)
        radiobutton1.pack(side="left", padx=(5, 2))

        radiobutton2 = Radiobutton(self.frame_selection, text="Ngưng chiếu", bg="#D7D7D7", activebackground="#D7D7D7",
                                   variable=self.radio_var, value=2, command=self.filter_movies)
        radiobutton2.pack(side="left", padx=(5, 2))

        radiobutton3 = Radiobutton(self.frame_selection, text="Tất cả", bg="#D7D7D7", activebackground="#D7D7D7",
                                   variable=self.radio_var, value=3, command=self.filter_movies)
        radiobutton3.pack(side="left", padx=(5, 5))

        # Danh sách phòng chiếu
        self.rooms = [f"PC00{i}" for i in range(1, 8)]  # Tối đa 7 phòng chiếu PC001 đến PC007

        # Các nút Thêm, Xóa, Sửa
        button_frame = Frame(self.tab1_frame, bg="#D7D7D7")
        button_frame.place(x=3, y=80)
        # Get API
        Button(button_frame, text="Top popular movie", font=("Arial", 9), background="#C1BAA1", bd=0,
               activebackground="#A59D84", command=self.get_top_popular_movie).pack(side="left", padx=(100, 5))
        Button(button_frame, width=10, text="Thêm", font=("Arial", 9), bg="#C1BAA1",
               activebackground="#A59D84", bd=0, command=self.open_create_view).pack(side="left", padx=(0, 5))
        Button(button_frame, width=10, text="Xóa", font=("Arial", 9), bg="#C1BAA1",
               activebackground="#A59D84", bd=0, command=self.delete_movie).pack(side="left", padx=(0, 5))
        Button(button_frame, width=10, text="Sửa", font=("Arial", 9), bg="#C1BAA1",
               activebackground="#A59D84", bd=0, command=self.open_update_view).pack(side="left", padx=(0, 10))

        # Tạo table tree widget
        self.columns = ("STT", "ID phim", "Tên phim", "Thời lượng", "Suất chiếu", "Ngày chiếu", "Phòng chiếu", "Trạng thái")
        self.tree1 = ttk.Treeview(self.tab1_frame, columns=self.columns, show='headings', height=10)

        # Đọc dữ liệu từ file
        self.movies = Movie.get_movies()
        # Thêm dữ liệu vào Treeview
        self.refresh_treeview()

        # Đặt tiêu đề và chiều rộng hợp lý
        for col in self.columns:
            self.tree1.heading(col, text=col)
            if col == "STT":
                self.tree1.column(col, width=40, anchor="center")
            elif col == "ID phim":
                self.tree1.column(col,width=0,stretch=False)
            elif col == "Tên phim":
                self.tree1.column(col, width=200, anchor="center")
            elif col == "Thời lượng":
                self.tree1.column(col, width=100, anchor="center")
            elif col == "Suất chiếu":
                self.tree1.column(col, width=150, anchor="center")
            elif col == "Ngày chiếu":
                self.tree1.column(col, width=150, anchor="center")
            elif col == "Phòng chiếu":
                self.tree1.column(col, width=100, anchor="center")
            elif col == "Trạng thái":
                self.tree1.column(col, width=100, anchor="center")
        self.tree1.place(y=110, width=962, height=471)

        # Thực hiện tương tác
        self.tree1.bind("<Button-1>", self.handle_click_anywhere)
        self.tree1.bind("<Double-1>", self.status_on_double_click)

        # Tạo scrollbar
        scrollbar = ttk.Scrollbar(self.tab1_frame, orient="vertical", command=self.tree1.yview)
        self.tree1.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(pady=(36, 0), side="right", fill="y")
        # add tab 2

        # Khởi tạo biến self.active_combobox
        self.active_combobox = None

    def refresh_treeview(self):
        # Xóa tất cả các hàng hiện tại trong Treeview
        for item in self.tree1.get_children():
            self.tree1.delete(item)

        # Sử dụng danh sách tạm (nếu có) hoặc danh sách gốc
        movies_to_display = self.movies_temp if hasattr(self, 'movies_temp') else self.movies

        # Thêm dữ liệu mới vào Treeview
        for index, movie in enumerate(movies_to_display, start=1):
            showtime = movie["showtimes"]["start_time"] + " - " + movie["showtimes"]["end_time"] if movie[
                "showtimes"] else "N/A"
            duration = f"{movie['duration_minutes']} phút"
            self.tree1.insert('', 'end', values=(index,movie["id"], movie["name"], duration, showtime, movie["show_date"], movie["room"], movie["status"]))

    def search_movie(self):
        # Lấy giá trị từ ô nhập liệu
        search_term = self.tab1_movie_entry.get().strip().lower()

        if not search_term:
            messagebox.showwarning("Cảnh báo", "Vui lòng nhập tên hoặc ID phim để tìm kiếm!")
            return

        self.movies_temp = MovieController.search_movie(self.movies, search_term)

        # Kiểm tra nếu không tìm thấy phim
        if not self.movies_temp:
            messagebox.showinfo("Thông báo", "Không tìm thấy phim nào!")
            self.movies_temp = self.movies  # Khôi phục danh sách gốc nếu không tìm thấy

        # Cập nhật Treeview
        self.refresh_treeview()
    def filter_movies(self):
        # Lấy giá trị từ radio button
        selected_value = self.radio_var.get()

        filtered_movies = MovieController.filter_movies(self.movies, selected_value)

        # Lưu danh sách tạm thời để cập nhật Treeview
        self.movies_temp = filtered_movies
        self.refresh_treeview()

    def open_create_view(self):
        CreateMovieView(self.admin_win, self)

    def delete_movie(self):
        # Lấy hàng được chọn trong Treeview
        selected_item = self.tree1.selection()
        if not selected_item:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn một phim để xóa!")
            return

        # Xác nhận xóa
        if not messagebox.askyesno("Xác nhận", "Bạn có chắc chắn muốn xóa phim này?"):
            return

        # Lấy ID của phim được chọn
        selected_item = selected_item[0]
        movie_id = self.tree1.item(selected_item)["values"][1]
        isValid, message = MovieController.delete_movie(movie_id)
        if isValid:
            messagebox.showinfo("Thành công", message)
            self.movies = Movie.get_movies()
            self.refresh_treeview()
        else: messagebox.showerror("Lỗi", message)

    def open_update_view(self):
        # Lấy hàng được chọn trong Treeview
        selected_item = self.tree1.selection()
        if not selected_item:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn một phim để sửa!")
            return

        selected_item = selected_item[0]
        values = self.tree1.item(selected_item)["values"]
        self.movie = next((m for m in self.movies if m["id"] == values[1]), None)
        UpdateMovieView(self)

    def handle_click_anywhere(self, event):
        if hasattr(self, 'active_combobox') and self.active_combobox:
            self.active_combobox.destroy()
            self.active_combobox = None

    def status_on_double_click(self, event):
        if self.active_combobox:
            self.active_combobox.destroy()
            self.active_combobox = None

        column = self.tree1.identify_column(event.x)
        selected_item = self.tree1.identify_row(event.y)
        if not selected_item:
            return
        if column in ['#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8']:
            item = self.tree1.item(selected_item)
            values = item['values']
            movie = next((m for m in self.movies if m["id"] == values[1]), None)
            if movie:
                MovieDetailAdminView(self.admin_win, movie, values)
    def open_login_admin_view(self, event):
        if messagebox.askyesno("Đăng xuất", "Bạn có chắc muốn đăng xuất?"):
            self.admin_win.destroy()  # Đóng cửa sổ admin
            master_window = self.admin_win.master
            master_window.deiconify()  # Hiển thị lại cửa sổ login

    def get_top_popular_movie(self):
        self.show_loading_screen()
        threading.Thread(target=self._get_data_and_update_ui, daemon=True).start()

    def _get_data_and_update_ui(self):
        MovieController.get_api()  # gọi API ở đây
        self.root.after(0, self.close_loading_screen)
        self.movies = Movie.get_movies()
        self.refresh_treeview()

    def show_loading_screen(self):
        self.loading_window = Toplevel(self.root)
        self.loading_window.title('Đang chờ...')
        self.loading_window.geometry('300x100')
        Label(self.loading_window, text="🔄 Đang lấy dữ liệu từ API...", font=("Arial", 12)).pack(padx=20, pady=30)
        self.loading_window.grab_set()

    def close_loading_screen(self):
        if self.loading_window:
            self.loading_window.destroy()

    # Tắt chương trình khi tắt cửa sổ này
    def quit_app(self):
        self.root.destroy()
