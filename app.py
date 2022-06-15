from flask import Flask, jsonify
from classes.movie import Movie

# Конфигурация

DATABASE = './netflix.db'

db_movie = Movie(DATABASE)

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


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


@app.route("/rating/children/")
def rating_children():
    """ поиск фильма для детей"""
    post_children = db_movie.search_by_rating_children()
    return jsonify(post_children)

@app.route("/rating/family/")
def rating_family():
    """ поиск для семейного просмотра """
    post_family = db_movie.search_by_rating_family()
    return jsonify(post_family)

@app.route("/rating/adult/")
def rating_adult():
    """ поиск для взрослых """
    post_adult = db_movie.search_by_rating_adult()
    return jsonify(post_adult)

@app.route("/genre/<genre>/")
def rating_genre(genre):
    """ поиск по жанру.  """
    post_genre = db_movie.search_by_genre(genre)
    return jsonify(post_genre)

if __name__ == '__main__':
    app.run(debug=True)
