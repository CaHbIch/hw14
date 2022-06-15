from flask import Flask, jsonify
from classes.movie import Movie

# Конфигурация

DATABASE = './netflix.db'

db_movie = Movie(DATABASE)

app = Flask(__name__)


@app.route("/movie/<title>/")
def data_movie(title):
    """ Выводит даные о фильме"""
    post_movie = db_movie.get_name_movie(title)
    return jsonify(post_movie)


if __name__ == '__main__':
    app.run(debug=True)
