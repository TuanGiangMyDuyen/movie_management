from tkinter import *
from io import BytesIO
from PIL import Image, ImageTk
import requests


class MovieDetailAdminView:
    def __init__(self, parent, movie, values, update_callback=None):
        self.detail_win = Toplevel(parent)
        self.detail_win.title("Chi tiết phim")
        self.detail_win.geometry("600x400+400+200")
        self.detail_win.config(bg="#213448")
        self.update_callback = update_callback  # Callback để cập nhật danh sách phim

        # Tạo frame chứa thông tin
        self.win_lab = Label(self.detail_win, text="THÔNG TIN CHI TIẾT BỘ PHIM", font=("Arial", 15, "bold"), fg="white",
                             bg="#213448").pack(fill="x", padx=10, pady=(20, 0))
        self.detail_win_fra = Frame(self.detail_win, width=500, height=370, bg="#F3F3E0")
        self.detail_win_fra.pack(fill="x", padx=(5, 5), pady=(0, 5))

        # Cấu hình font và màu sắc cho các Label
        label_title_font = ("Arial", 10, "bold")
        label_value_font = ("Arial", 9, "bold")
        label_title_color = "black"
        label_value_color = "#333333"

        # Tạo Frame và Label cho từng thông tin phim (tiêu đề và giá trị trên cùng một hàng)
        # Tạo Frame cha chứa frame pos và frame info
        main_container = Frame(self.detail_win_fra, bg="#F3F3E0")
        main_container.pack(fill="both", expand=True, padx=5, pady=5)
        # Frame chứa poster (bên trái)
        pos_frame = Frame(main_container, bg="#F3F3E0")
        pos_frame.pack(side="left", fill="y", padx=(0, 20))

        # Thêm poster phim
        poster_url = movie['poster_url']
        try:
            response = requests.get(poster_url)
            if response.status_code == 200:
                image_data = response.content
                image = Image.open(BytesIO(image_data))
                image = image.resize((220, 270))
                self.photo = ImageTk.PhotoImage(image)

                label = Label(pos_frame, image=self.photo, bg="#F3F3E0")
                label.image = self.photo  # Giữ tham chiếu
                label.pack()
            else:
                raise Exception("Không thể tải ảnh")
        except Exception as e:
            print(f"Lỗi khi tải ảnh cho phim {movie['name']}: {e}")
            Label(pos_frame, text="Poster\nKhông có ảnh", width=30, height=15, bg="gray").pack()
        # Frame chứa thông tin (bên phải)
        info_frame = Frame(main_container, bg="#F3F3E0")
        info_frame.pack(side="right", fill="both", expand=True)

        # ID_Phim
        id_frame = Frame(info_frame, bg="#DAD3BE")
        id_frame.pack(fill="x", padx=(3, 5), pady=(5, 0))
        Label(id_frame, text="ID_Phim: ", font=label_title_font, fg=label_title_color, bg="#DAD3BE").pack(side="left")
        Label(id_frame, text=f"{movie['id']}", font=label_value_font, fg=label_value_color, bg="#DAD3BE").pack(
            side="left")

        # Tên phim
        name_frame = Frame(info_frame, bg="#DAD3BE")
        name_frame.pack(fill="x", padx=(3, 5))
        Label(name_frame, text="Tên phim: ", font=label_title_font, fg=label_title_color, bg="#DAD3BE").pack(
            side="left")
        Label(name_frame, text=f"{movie['name']}", font=("Arial", 11, "bold"), fg="#B82132", bg="#DAD3BE").pack(
            side="left")
        # Mô tả
        des_frame = Frame(info_frame, bg="#DAD3BE")
        des_frame.pack(fill="x", padx=(3, 5))
        Label(des_frame, text="Mô tả: ", font=label_title_font, fg=label_title_color, bg="#DAD3BE").pack(side="left")
        Label(des_frame, text=f"{movie['description']}", font=label_value_font, fg=label_value_color,
              bg="#DAD3BE").pack(side="left")
        # Thể loại
        genre_frame = Frame(info_frame, bg="#DAD3BE")
        genre_frame.pack(fill="x", padx=(3, 5))
        Label(genre_frame, text="Thể loại: ", font=label_title_font, fg=label_title_color, bg="#DAD3BE").pack(
            side="left")
        Label(genre_frame, text=f"{movie['genre']}", font=label_value_font, fg="#F96E2A", bg="#DAD3BE").pack(
            side="left")

        # Đạo diễn
        director_frame = Frame(info_frame, bg="#DAD3BE")
        director_frame.pack(fill="x", padx=(3, 5))
        Label(director_frame, text="Đạo diễn: ", font=label_title_font, fg=label_title_color, bg="#DAD3BE").pack(
            side="left")
        Label(director_frame, text=f"{movie['director']}", font=label_value_font, fg=label_value_color,
              bg="#DAD3BE").pack(side="left")

        # Diễn viên
        actors_frame = Frame(info_frame, bg="#DAD3BE")
        actors_frame.pack(fill="x", padx=(3, 5))
        Label(actors_frame, text="Diễn viên: ", font=label_title_font, fg=label_title_color, bg="#DAD3BE").pack(
            side="left")
        Label(actors_frame, text=f"{', '.join(movie['actors'])}", font=label_value_font, fg=label_value_color,
              bg="#DAD3BE", anchor="w", justify="left").pack(side="left", fill="x")

        # Ngôn ngữ
        language_frame = Frame(info_frame, bg="#DAD3BE")
        language_frame.pack(fill="x", padx=(3, 5))
        Label(language_frame, text="Ngôn ngữ: ", font=label_title_font, fg=label_title_color, bg="#DAD3BE").pack(
            side="left")
        Label(language_frame, text=f"{movie['language']}", font=label_value_font, fg=label_value_color,
              bg="#DAD3BE").pack(side="left")

        # Thời lượng
        duration_frame = Frame(info_frame, bg="#F3F3E0")
        duration_frame.pack(fill="x", padx=(3, 5))
        Label(duration_frame, text="Thời lượng: ", font=label_title_font, fg=label_title_color, bg="#F3F3E0").pack(
            side="left")
        Label(duration_frame, text=f"{movie['duration_minutes']} phút", font=label_value_font, fg=label_value_color,
              bg="#F3F3E0").pack(side="left")

        # Suất chiếu
        showtime_frame = Frame(info_frame, bg="#F3F3E0")
        showtime_frame.pack(fill="x", padx=(3, 5))
        Label(showtime_frame, text="Suất chiếu: ", font=label_title_font, fg=label_title_color, bg="#F3F3E0").pack(
            side="left")
        Label(showtime_frame, text=f"{values[4]}", font=label_value_font, fg=label_value_color, bg="#F3F3E0").pack(
            side="left")

        # Phòng chiếu
        room_frame = Frame(info_frame, bg="#F3F3E0")
        room_frame.pack(fill="x", padx=(3, 5))
        Label(room_frame, text="Phòng chiếu: ", font=label_title_font, fg=label_title_color, bg="#F3F3E0").pack(
            side="left")
        Label(room_frame, text=f"{values[5]}", font=label_value_font, fg="#EB5B00", bg="#F3F3E0").pack(side="left")

        # Trạng thái
        status_frame = Frame(info_frame, bg="#F3F3E0")
        status_frame.pack(fill="x", padx=(3, 5))
        Label(status_frame, text="Trạng thái: ", font=label_title_font, fg=label_title_color, bg="#F3F3E0").pack(
            side="left")
        Label(status_frame, text=f"{values[6]}", font=label_value_font, fg="green", bg="#F3F3E0").pack(side="left")

        # Giá vé
        price_frame = Frame(info_frame, bg="#F3F3E0")
        price_frame.pack(fill="x", padx=(3, 5))
        Label(price_frame, text="Giá vé: ", font=label_title_font, fg=label_title_color, bg="#F3F3E0").pack(side="left")
        Label(price_frame, text=f"{movie['ticket_price']} VNĐ", font=label_value_font, fg=label_value_color,
              bg="#F3F3E0").pack(side="left")

        # Nút Đóng
        Button(self.detail_win, width=50, text="Đóng", font=("Arial", 10, "bold"), bg="#F0BB78",
               activebackground="#F0BB78", bd=0, command=self.detail_win.destroy).pack(fill="x", padx=(5, 5))