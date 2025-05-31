import requests
import time
import uuid
from utils.calculate_end_time import CalculateEndTime
from datetime import datetime

class GetApi:
    def __init__(self):
        self.API_KEY = '4aa4c0549bb26992be70be72b02dda14'
        self.base_image_url = "https://image.tmdb.org/t/p/w500"

    def get_movie_info_by_id(self, movie_id):
        # Lấy thông tin chi tiết
        details_url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={self.API_KEY}&language=vi"
        details_response = requests.get(details_url)
        movie_details = details_response.json()

        # Lấy đạo diễn và diễn viên
        credits_url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={self.API_KEY}"
        credits_response = requests.get(credits_url)
        credits = credits_response.json()

        # Lấy thông tin phân loại độ tuổi
        rating_url = f"https://api.themoviedb.org/3/movie/{movie_id}/release_dates?api_key={self.API_KEY}"
        rating_response = requests.get(rating_url)
        rating_data = rating_response.json()
        rated = "Không rõ"
        for country in rating_data.get("results", []):
            if country["iso_3166_1"] == "US":
                for rel in country["release_dates"]:
                    if rel.get("certification"):
                        rated = rel["certification"]
                        break

        # Xử lý poster
        poster_path = movie_details.get('poster_path', '')
        poster_url = f"{self.base_image_url}{poster_path}" if poster_path else ""

        # Lấy đạo diễn
        directors = [crew['name'] for crew in credits.get('crew', []) if crew.get('job') == 'Director']
        director = directors[0] if directors else "Không rõ"

        # Lấy diễn viên chính
        actors = [actor['name'] for actor in credits.get('cast', [])[:3]]

        # Lấy thể loại
        genres = [genre['name'] for genre in movie_details.get('genres', [])]
        genre = genres[0] if genres else "Không rõ"

        # Ngôn ngữ
        language = movie_details.get('original_language', 'en')
        # Tạo dữ liệu phim theo định dạng chuẩn
        movie_info = {
            "id": str(uuid.uuid4()),
            "name": movie_details.get('title', ''),
            "genre": genre,
            "director": director,
            "actors": actors,
            "language": language,
            "rated": rated,
            "description": movie_details.get('overview', 'Không có mô tả.'),
            "show_date": "01/01/2001",
            "duration_minutes": movie_details.get('runtime', 0),
            "status": "Đang chiếu",  # placeholder
            "showtime": "09:00",  # placeholder
            "room": "PC001",  # placeholder
            "total_seats": 50,  # placeholder
            "available_seats": 50,  # placeholder
            "ticket_price": 120000,  # placeholder
            "showtime_type": "2D",  # placeholder
            "poster_url": poster_url,
            "showtimes": CalculateEndTime.calculate_end_time("09:00", movie_details.get('runtime', 0))
        }

        return movie_info

    def get_top_popular_movies(self, limit):
        url = f"https://api.themoviedb.org/3/movie/popular?api_key={self.API_KEY}&language=vi&page=1"
        response = requests.get(url)
        data = response.json()

        movies_data = []
        for movie in data.get('results', [])[:limit]:
            movie_id = movie['id']
            try:
                movie_info = self.get_movie_info_by_id(movie_id)
                movies_data.append(movie_info)
                time.sleep(0.2)
            except Exception as e:
                print(f"Lỗi với phim {movie['title']}: {e}")

        return movies_data
