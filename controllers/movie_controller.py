from utils.movie_validation import MovieValidation
from utils.cloudinary import Cloudinary
from models.movie_model import Movie
from utils.calculate_end_time import CalculateEndTime
import uuid


class MovieController:
    def __init__(self, movieInfo):
        self.movieInfo = movieInfo

    @staticmethod
    def get_movies():
        return Movie.get_movies()

    def create_movie(self):

        # Kiểm tra các trường
        isValid, message = MovieValidation.validate_movie_info(self.movieInfo)
        if not isValid:
            return False, message

        # Kiểm tra ảnh
        isValid, message = MovieValidation.validate_image(self.movieInfo['poster_url'])
        if not isValid:
            return False, message

        # Kiểm tra có trùng lịch hay không
        movies = Movie.get_movies()
        for movie in movies:
            if self.movieInfo['showtime'] == movie['showtimes']['start_time'] \
            and self.movieInfo['room'] == movie['room'] and self.movieInfo['release_date'] == movie['release_date']:
                return False, "Đã có phim cùng lịch tồn tại!"

        url, message = Cloudinary.upload_photo(self.movieInfo['poster_url'])
        if url:
            self.movieInfo['poster_url'] = url
        else: return False, "Lỗi không thể tải ảnh!"

        # Định dạng lại diên viên
        actors1 = self.movieInfo['actors']
        self.movieInfo['actors'] = actors1.split(', ')

        # Tính thời gian bắt đầu và kết thúc phim
        showtimes = CalculateEndTime.calculate_end_time(self.movieInfo['showtime'], self.movieInfo['duration_minutes'])

        self.movieInfo['showtimes'] = showtimes

        self.movieInfo = {"id": str(uuid.uuid4()), **self.movieInfo}

        movie = Movie(self.movieInfo)
        movie.save_movie()
        return True, "Tạo phim thành công"

    @staticmethod
    def delete_movie(movie_id):
        movies = Movie.get_movies()
        for i, movie in enumerate(movies):
            if movie['id'] == movie_id:
                del movies[i]
                Movie.save_movies(movies)
                Cloudinary.delete_photo(movie['poster_url'])
                return True, 'Xóa phim thành công'
        return False, 'Phim đã bị xóa trước đó rồi!'

    def update_movie(self, id):

        # Kiểm tra phim có tồn tại hay không
        self.flag = False
        movies = Movie.get_movies()
        for movie in movies:
            if movie['id'] == id:
                self.movie = movie
                self.flag = True
                break

        if self.flag == False:
            return False, "Phim không tồn tại!"

        # Kiểm tra các trường
        isValid, message = MovieValidation.validate_movie_info(self.movieInfo)
        if not isValid:
            return False, message

        # Nếu ảnh được thay đổi thì mới upload lên cloud
        def is_local_file(path):
            return not path.startswith("http") or "cloudinary" not in path

        # Chỉ upload nếu là file trong máy, không phải URL cloud
        if self.movieInfo['poster_url'] != self.movie['poster_url'] and is_local_file(self.movieInfo['poster_url']):
            # Kiểm tra ảnh
            isValid, message = MovieValidation.validate_image(self.movieInfo['poster_url'])
            if not isValid:
                return False, message

            url, message = Cloudinary.upload_photo(self.movieInfo['poster_url'])
            if url:
                self.movieInfo['poster_url'] = url
                Cloudinary.delete_photo(self.movie['poster_url'])
            else:
                return False, "Lỗi không thể tải ảnh!"

        # Định dạng lại diên viên
        actors1 = self.movieInfo['actors']
        self.movieInfo['actors'] = actors1.split(', ')

        # Tính thời gian bắt đầu và kết thúc phim
        showtimes = CalculateEndTime.calculate_end_time(self.movieInfo['showtime'], self.movieInfo['duration_minutes'])

        self.movieInfo['showtimes'] = showtimes

        self.movieInfo = {"id": self.movie['id'], **self.movieInfo}

        #Gán dữ liệu cập nhật vào dữ liệu cũ
        for i, movie in enumerate(movies):
            if movie['id'] == id:
                movies[i] = self.movieInfo

        Movie.save_movies(movies)
        return True, "Cập nhật phim thành công"

    @staticmethod
    def search_movie(movies, search_term):

        # Lọc danh sách phim dựa trên tên và ID (không phân biệt hoa thường)
        movies_by_name = [movie for movie in movies if search_term in movie["name"].lower()]
        movies_by_id = [movie for movie in movies if search_term in movie["id"].lower()]

        # Gộp hai danh sách và loại bỏ trùng lặp (dựa trên ID phim)
        combined_movies = {movie["id"]: movie for movie in movies_by_name + movies_by_id}.values()

        # Chuyển kết quả thành danh sách để sử dụng
        movies_temp = list(combined_movies)

        return movies_temp

    @staticmethod
    def filter_movies(movies, selected_value):

        # Lọc danh sách phim dựa trên trạng thái
        if selected_value == 1:  # Đang chiếu
            filtered_movies = [movie for movie in movies if movie["status"] == "Đang chiếu"]
        elif selected_value == 2:  # Ngừng chiếu
            filtered_movies = [movie for movie in movies if movie["status"] == "Ngưng chiếu"]
        else:  # Tất cả
            filtered_movies = movies

        return filtered_movies
