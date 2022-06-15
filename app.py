from flask import Flask, jsonify
from classes.movie import Movie

# Конфигурация

DATABASE = './netflix.db'

db_movie = Movie(DATABASE)

app = Flask(__name__)


@app.route("/movie/<title>/")
def data_movie(title):
    """ поиск по названию """
    post_movie = db_movie.all_name_movie(title)
    return jsonify(post_movie)


@app.route("/movie/<int:year>/to/<int:years>/")
def data_year(year, years):
    """ поиск по диапазону лет выпуска. """
    post_year = db_movie.search_by_years(year, years)
    return jsonify(post_year)



if __name__ == '__main__':
    app.run(debug=True)
