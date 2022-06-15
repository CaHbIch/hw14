import sqlite3
from pprint import pp

from app import DATABASE


class Movie:

    def __init__(self, DATABASE):
        self.DATABASE = DATABASE

    def connect_db(self):

        """ Устанавливает соеденение с БД"""
        conn = sqlite3.connect(self.DATABASE)
        conn.row_factory = sqlite3.Row
        return conn

    # def __repr__(self):
    #     return self.DATABASE


movie = Movie(DATABASE)
pp(movie)
