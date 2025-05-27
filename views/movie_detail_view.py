from tkinter import *
import os
import requests
from PIL import Image, ImageTk
from io import BytesIO

class MovieDetailView:
    def __init__(self, root, movie):
        self.root = root
        self.movie = movie
        self.movie_window = None
        self.create_movie_view()

    def create_movie_view(self):
        if self.movie_window and self.movie_window.winfo_exists():
            self.update_movie(self.movie)
            return
        self.movie_window = Toplevel(self.root)
        self.movie_window.title("Z+Plus.Movie - Chi tiết phim")
        self.movie_window.geometry("600x350+160+30")
        self.movie_window["bg"] = "#222222"
        self.movie_window.resizable(False, False)

        # Logo
        image_path = os.path.join(os.path.dirname(__file__), "..", "images", "logo.png")
        image = Image.open(image_path)
        resized_image = image.resize((50, 50))
        self.img = ImageTk.PhotoImage(resized_image)
        Label(self.movie_window, image=self.img, bg="#222222").place(x=20, y=4)
        Label(self.movie_window, text="Z+ Plus", fg="white", bg="#222222", font=("Montserrat", 10, "bold")).place(x=80, y=10)
        Label(self.movie_window, text="Phim hay tại rạp", fg="white", bg="#222222", font=("Montserrat", 8)).place(x=80, y=30)

        # Khung hiển thị thông tin phim
        self.frame_movie_info = Frame(self.movie_window, bg="#222222", height=530)
        self.frame_movie_info.pack(fill="x", padx=15, pady=(60, 0))

        # Frame cho poster
        frame_poster = Frame(self.frame_movie_info, bg="#222222")
        frame_poster.pack(side="left", padx=(10, 0))

        # Thêm poster phim
        poster_url = self.movie['poster_url']
        try:
            response = requests.get(poster_url)
            if response.status_code == 200:
                image_data = response.content
                image = Image.open(BytesIO(image_data))
                image = image.resize((230, 280))
                self.photo = ImageTk.PhotoImage(image)
                Label(frame_poster, image=self.photo, bg="#222222").pack()
            else:
                raise Exception("Không thể tải ảnh")
        except Exception as e:
            print(f"Lỗi khi tải ảnh cho phim {self.movie['name']}: {e}")

        # Frame cho thông tin phim
        frame_info = Frame(self.frame_movie_info, bg="#222222")
        frame_info.pack(side="left", fill="both", expand=True, padx=(3, 0))

        # Tên phim
        Label(frame_info, text=self.movie["name"], fg="yellow", bg="#222222",
            font=("Montserrat", 15, "bold"), wraplength=400, anchor="w", justify="left").pack(anchor="w", pady=(3, 0))

        # Thể loại
        genre_frame = Frame(frame_info, bg="#222222")
        genre_frame.pack(anchor="w", pady=(0, 0))
        Label(genre_frame, text="Thể loại:", fg="white", bg="#222222",
            font=("Montserrat", 10, "bold")).pack(side="left", anchor="n")
        Label(genre_frame, text=self.movie["genre"], fg="white", bg="#222222",
            font=("Montserrat", 10), wraplength=280, anchor="nw", justify="left").pack(side="left", padx=(5, 0))
        
        # Loại suất chiếu
        showtime_type_frame = Frame(frame_info, bg="#222222")
        showtime_type_frame.pack(anchor="w", pady=(0, 0))
        Label( showtime_type_frame, text="Loại suất chiếu:", fg="white", bg="#222222",
            font=("Montserrat", 10, "bold")).pack(side="left", anchor="n")
        Label( showtime_type_frame, text=self.movie["showtime_type"], fg="white", bg="#222222",
            font=("Montserrat", 10), wraplength=280, anchor="nw", justify="left").pack(side="left", padx=(5, 0))
        # Đạo diễn
        director_frame = Frame(frame_info, bg="#222222")
        director_frame.pack(anchor="w", pady=(0, 0))
        Label(director_frame, text="Đạo diễn:", fg="white", bg="#222222",
            font=("Montserrat", 10, "bold"), anchor="w").pack(side="left")
        Label(director_frame, text=self.movie["director"], fg="white", bg="#222222",
            font=("Montserrat", 10), wraplength=400, anchor="w", justify="left").pack(side="left", padx=(5, 0))
        
        # Ngôn ngữ
        language_frame = Frame(frame_info, bg="#222222")
        language_frame.pack(anchor="w", pady=(0, 0))
        Label(language_frame, text="Ngôn ngữ:", fg="white", bg="#222222",
            font=("Montserrat", 10, "bold"), anchor="w").pack(side="left")
        Label(language_frame, text=self.movie["language"], fg="white", bg="#222222",
            font=("Montserrat", 10), wraplength=400, anchor="w", justify="left").pack(side="left", padx=(5, 0))

        # Mô tả
        description_frame = Frame(frame_info, bg="#222222")
        description_frame.pack(anchor="w", pady=(0, 0))
        Label(description_frame, text="Mô tả:", fg="white", bg="#222222",
            font=("Montserrat", 10, "bold")).pack(side="left", anchor="n")
        Label(description_frame, text=self.movie["description"], fg="white", bg="#222222",
            font=("Montserrat", 10), justify="left", wraplength=280, anchor="nw").pack(side="left", padx=(5, 0))

        # Ngày chiếu
        release_date_frame = Frame(frame_info, bg="#222222")
        release_date_frame.pack(anchor="w", pady=(0, 0))
        Label(release_date_frame, text="Ngày chiếu:", fg="white", bg="#222222",
            font=("Montserrat", 10, "bold"), anchor="w").pack(side="left")
        Label(release_date_frame, text=self.movie["release_date"], fg="white", bg="#222222",
            font=("Montserrat", 10), wraplength=400, anchor="w", justify="left").pack(side="left", padx=(5, 0))

        # Thời lượng
        duration_frame = Frame(frame_info, bg="#222222")
        duration_frame.pack(anchor="w", pady=(0, 0))
        Label(duration_frame, text="Thời lượng:", fg="white", bg="#222222",
            font=("Montserrat", 10, "bold"), anchor="w").pack(side="left")
        Label(duration_frame, text=f"{self.movie['duration_minutes']} phút", fg="white", bg="#222222",
            font=("Montserrat", 10), wraplength=400, anchor="w", justify="left").pack(side="left", padx=(5, 0))
        
        # ticket_price
        ticket_price_frame = Frame(frame_info, bg="#222222")
        ticket_price_frame.pack(anchor="w", pady=(0, 0))
        Label(ticket_price_frame, text="Gía vé:", fg="white", bg="#222222",
            font=("Montserrat", 10, "bold"), anchor="w").pack(side="left")
        Label(ticket_price_frame, text=f"{self.movie['ticket_price']} VND", fg="white", bg="#222222",
            font=("Montserrat", 10), wraplength=200, anchor="w", justify="left").pack(side="left", padx=(5, 0))

        Button(frame_info, text="Quay lại", width=40, fg="white", bg="#332D56", font=("Montserrat", 10, "bold"),
        command=self.movie_window.destroy,justify="center",bd=0,activebackground="#4E6688").pack(side="bottom",pady=(5, 3), anchor="w")
    def update_movie(self, movie):
        self.movie = movie
        self.movie_window.destroy()
        self.create_movie_view()