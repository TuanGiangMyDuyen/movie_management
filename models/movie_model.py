from models.json_model import JSONHandler


class Movie:
    def __init__(self, movieInfo):
        self.movieInfo = movieInfo

    @staticmethod
    def get_movies():
        handler_json = JSONHandler('movies.json')
        return handler_json.read_json()

    def save_movie(self):
        handler_json = JSONHandler('movies.json')
        movies = Movie.get_movies()
        movies.insert(0, self.movieInfo)
        handler_json.write_json(movies)

    @staticmethod
    def save_movies(movies):
        handler_json = JSONHandler('movies.json')
        handler_json.write_json(movies)

