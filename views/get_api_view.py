from tkinter import *
from tkinter.ttk import Treeview
from utils.get_api import GetApi
from PIL import Image, ImageTk
import requests
import io
import threading


class GetApiView:
    def __init__(self, root):
        self.root = root
        self.images_cache = {}
        self.loading_window = None
        self.movies = []

        self.show_loading_screen()
        threading.Thread(target=self.load_movies).start()

    def show_loading_screen(self):
        self.loading_window = Toplevel(self.root)
        self.loading_window.title('Đang chờ...')
        self.loading_window.geometry('300x100')
        Label(self.loading_window, text="🔄 Đang lấy dữ liệu từ API...", font=("Arial", 12)).pack(padx=20, pady=30)

    def load_movies(self):
        get_api = GetApi()
        self.movies = get_api.get_top_popular_movies(5)

        self.root.after(0, self.show_movie_window)

    def show_movie_window(self):
        if self.loading_window:
            self.loading_window.destroy()

        self.top_movie = Toplevel(self.root)
        self.top_movie.title('Top Popular Movies')
        self.top_movie.geometry("1000x600")
        self.top_movie.configure(bg="white")

        self.tree = Treeview(self.top_movie, columns=("Title", "Release Date", "Rating"), show="headings", height=25)
        self.tree.heading("Title", text="Title")
        self.tree.heading("Release Date", text="Release Date")
        self.tree.heading("Rating", text="Rating")
        self.tree.column("Title", width=300)
        self.tree.column("Release Date", width=100)
        self.tree.column("Rating", width=80)
        self.tree.pack(side="left", fill="y", padx=10, pady=10)

        scrollbar = Scrollbar(self.top_movie, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="left", fill="y")

        self.detail_frame = Frame(self.top_movie, bg="white")
        self.detail_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        self.poster_label = Label(self.detail_frame, bg="white")
        self.poster_label.pack(pady=10)

        self.detail_text = Text(self.detail_frame, wrap="word", bg="white", font=("Arial", 12), height=25)
        self.detail_text.pack(fill="both", expand=True, padx=10)

        for movie in self.movies:
            self.tree.insert("", "end", values=(movie["title"], movie["release_date"], movie["vote_average"]))

        self.tree.bind("<<TreeviewSelect>>", self.show_movie_details)

    def show_movie_details(self, event):
        selected_item = self.tree.selection()
        if not selected_item:
            return
        index = self.tree.index(selected_item[0])
        movie = self.movies[index]

        self.detail_text.delete(1.0, "end")
        self.detail_text.insert("end", f"🎬 Title: {movie['title']}\n")
        self.detail_text.insert("end", f"🎥 Original Title: {movie['original_title']}\n")
        self.detail_text.insert("end", f"📅 Release Date: {movie['release_date']}\n")
        self.detail_text.insert("end", f"⏱️ Runtime: {movie['runtime']} minutes\n")
        self.detail_text.insert("end", f"🎭 Genres: {', '.join(movie['genres'])}\n")
        self.detail_text.insert("end", f"🎬 Director(s): {', '.join(movie['directors'])}\n\n")
        self.detail_text.insert("end", f"📝 Overview:\n{movie['overview']}\n")

        poster_url = movie.get("poster_url")
        if poster_url:
            if poster_url not in self.images_cache:
                try:
                    response = requests.get(poster_url)
                    img_data = response.content
                    img = Image.open(io.BytesIO(img_data))
                    img.thumbnail((250, 350))
                    photo = ImageTk.PhotoImage(img)
                    self.images_cache[poster_url] = photo
                except Exception as e:
                    print(f"Lỗi tải ảnh: {e}")
                    self.poster_label.config(image='', text='Không có ảnh')
                    return
            self.poster_label.config(image=self.images_cache[poster_url], text='')
        else:
            self.poster_label.config(image='', text='Không có ảnh')