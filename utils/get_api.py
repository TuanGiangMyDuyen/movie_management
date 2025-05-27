import requests
import time
class GetApi:
    def __init__(self):
        self.API_KEY = '4aa4c0549bb26992be70be72b02dda14'

    def get_movie_info_by_id(self, movie_id):
        details_url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={self.API_KEY}"
        details_response = requests.get(details_url)
        movie_details = details_response.json()

        credits_url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={self.API_KEY}"
        credits_response = requests.get(credits_url)
        credits = credits_response.json()

        base_image_url = "https://image.tmdb.org/t/p/w300"
        poster_path = movie_details.get('poster_path', '')
        poster_url = f"{base_image_url}{poster_path}" if poster_path else None

        directors = [crew['name'] for crew in credits.get('crew', []) if crew['job'] == 'Director']
        genres = [genre['name'] for genre in movie_details.get('genres', [])]

        movie_info = {
            'title': movie_details.get('title', ''),
            'original_title': movie_details.get('original_title', ''),
            'release_date': movie_details.get('release_date', ''),
            'runtime': movie_details.get('runtime', 0),
            'genres': genres,
            'directors': directors,
            'overview': movie_details.get('overview', ''),
            'poster_url': poster_url,
            'vote_average': movie_details.get('vote_average', 0)
        }

        return movie_info


    def get_top_popular_movies(self, limit):
        url = f"https://api.themoviedb.org/3/movie/popular?api_key={self.API_KEY}&language=en-US&page=1"
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