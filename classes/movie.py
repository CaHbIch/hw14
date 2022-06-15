import sqlite3
from pprint import pp



class Movie:

    def __init__(self, DATABASE):
        self.DATABASE = DATABASE

    def all_name_movie(self):
        """ Выводит все названия фильмом  """
        with sqlite3.connect(self.DATABASE) as conn:
            conn.row_factory = sqlite3.Row
            search_name = conn.cursor()
            search_name.execute("SELECT `title`, `country`, release_year, listed_in, description "
                                "FROM netflix ")
        return search_name.fetchall()

    def get_name_movie(self, title):
        """ выводит поиск по названию фильма"""
        get_movies = []
        for get_movie in self.all_name_movie():
            if str(title).lower() in get_movie[0].lower():
                get_movies.append(dict(get_movie))
        return get_movies

# #
# movie = Movie("DATABASE")
# pp(movie.get_name_movie('27'))
