import sqlite3
from pprint import pp



class Movie:

    def __init__(self, DATABASE):
        self.DATABASE = DATABASE

    def all_name_movie(self):
        """ Выводит все названия фильмом  """
        with sqlite3.connect(self.DATABASE) as conn:
            search_name = conn.cursor()
            search_name.execute("SELECT `title`, `country`, release_year, listed_in, description "
                                "FROM netflix ")
        return search_name.fetchall()

    def get_name_movie(self, title):
        """ выводит поиск по названию фильма"""
        get_movies = []
        for get_movie in self.all_name_movie():
            if str(title).lower() in get_movie[0].lower():
                gets_movie = {
                    "title": get_movie[0],
                    "country": get_movie[1],
                    "release_year": get_movie[2],
                    "listed_in": get_movie[3],
                    "description": get_movie[4]
                }
                get_movies.append(gets_movie)
        return get_movies

# #
# movie = Movie("DATABASE")
# pp(movie.get_name_movie('27'))
