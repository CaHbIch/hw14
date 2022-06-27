import sqlite3
from pprint import pp


class Movie:

    def __init__(self, DATABASE):
        self.DATABASE = DATABASE

    def connect_db(self):
        """ Устанавливаем соединение с курсором БД"""
        with sqlite3.connect(self.DATABASE) as conn:
            conn.row_factory = sqlite3.Row
            conn = conn.cursor()
        return conn

    def all_name_movie(self, title):
        """ выводит поиск по названию фильма"""
        db = self.connect_db()
        db.execute("SELECT `title`, `country`, release_year, listed_in, description "
                   "FROM netflix "
                   "WHERE `title` != '' "
                   "ORDER BY release_year DESC ")
        get_movies = []
        for get_movie in db:
            if str(title).lower() in get_movie['title'].lower():
                get_movies.append(dict(get_movie))
        return get_movies

    def search_by_years(self, year, years):
        """ Поиск по диапазону лет выпуска фильма """
        db = self.connect_db()
        sql = f""" SELECT `title`, release_year
                  FROM netflix
                  WHERE `release_year` BETWEEN {year} AND {years}
                  ORDER BY release_year
                  LIMIT 100
            """
        db.execute(sql)
        get_movies = []
        for get_movie in db:
            get_movies.append(dict(get_movie))
        return get_movies

    def search_by_rating_children(self):
        """ поиск по рейтингу, для детей"""
        db = self.connect_db()
        sql = f""" SELECT `title`, rating, description
                  FROM netflix
                  WHERE `rating` = 'G'
            """
        db.execute(sql)
        get_movies = []
        for get_movie in db:
            get_movies.append(dict(get_movie))
        return get_movies

    def search_by_rating_family(self):
        """ поиск для семейного просмотра """
        db = self.connect_db()
        sql = f""" SELECT `title`, rating, description
                  FROM netflix
                  WHERE `rating` IN ('G','PG', 'PG-13')
            """
        db.execute(sql)
        get_movies = []
        for get_movie in db:
            get_movies.append(dict(get_movie))
        return get_movies

    def search_by_rating_adult(self):
        """ поиск для взрослых. """
        db = self.connect_db()
        sql = f""" SELECT `title`, rating, description
                  FROM netflix
                  WHERE `rating` IN ('R', 'NC-17')
            """
        db.execute(sql)
        get_movies = []
        for get_movie in db:
            get_movies.append(dict(get_movie))
        return get_movies

    def search_by_genre(self, genre):
        """ поиск по жанру. """
        db = self.connect_db()
        sql = f"""SELECT `title`, description, listed_in
                  FROM netflix
                    """
        db.execute(sql)
        get_movies = []
        for get_movie in db:
            genres = get_movie['listed_in']
            if str(genre).lower() in genres.lower():
                gets_movie = {
                    "title": get_movie['title'],
                    "description": get_movie['description']
                }
                get_movies.append(dict(gets_movie))
        return get_movies

    def get_actors(self, actor, actros):
        """ Возвращает список актеров """
        db = self.connect_db()
        sql = f"""SELECT `cast`
                  FROM netflix
                  """
        db.execute(sql)
        add_actors = []
        for get_actors in db:
            get_actor = get_actors['cast']
            if actor.lower() and actros.lower() in get_actor.lower():
                add_actors.append(get_actor)
        return add_actors

    def paintings(self, types, release_year, listed_in):
        """ список названий картин """
        db = self.connect_db()
        sql = f"""SELECT *
                  FROM netflix
                  WHERE `release_year` = {release_year}
                           """
        db.execute(sql)
        get_movies = []
        for get_movie in db:
            genres = get_movie['listed_in']
            type_of = get_movie['type']
            if str(listed_in).lower() in genres.lower() and str(types).lower() in type_of.lower():
                gets_movie = {
                    "title": get_movie['title'],
                    "description": get_movie['description']
                }
                get_movies.append(dict(gets_movie))
        return get_movies
