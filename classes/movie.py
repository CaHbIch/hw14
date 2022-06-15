import sqlite3


class Movie:

    def __init__(self, DATABASE):
        self.DATABASE = DATABASE

    def connect_db(self):
        """ Устанавливаем соединение с БД"""
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
        sql = f""" SELECT `title`, `description`, listed_in
                  FROM netflix
                  LIMIT 100             
            """
        db.execute(sql)
        get_movies = []
        for get_movie in db:
            genres = get_movie['listed_in']
            if str(genre).lower() in genres.lower():
                get_movies.append(dict(get_movie))
        return get_movies
