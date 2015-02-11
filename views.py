from get_data import ratings
from bottle import route, run, template

@route('/')
def show_movie_ratings(movies=ratings):
    return template('index.html', movies=movies)

run(host="localhost", post=8080, debug=True)
