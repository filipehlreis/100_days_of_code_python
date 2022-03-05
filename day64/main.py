from typing import Any, List
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests
from local_setings.local_settings import API_TMDB


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


MOVIE_DB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
MOVIE_DB_INFO_URL = "https://api.themoviedb.org/3/movie"
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"


# CREATE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies.db"
# Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# CREATE TABLE
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)


class EditForm(FlaskForm):
    edit_rating = FloatField('Rating: e.g. 7.5', validators=[DataRequired()])
    edit_review = StringField('Review', validators=[DataRequired()])
    submit = SubmitField(label="Update")


# db.create_all()
all_movies: List[Any] = []


@app.route('/delete',  methods=["GET", "POST"])
def delete():
    movie_id = request.args.get('id')

    # # Delete A Particular Record By PRIMARY KEY
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()

    return redirect(url_for('home'))


@app.route("/")
def home():
    # This line creates a list of all the movies sorted by rating
    all_movies = Movie.query.order_by(Movie.rating).all()

    # This line loops through all the movies
    for i in range(len(all_movies)):
        # This line gives each movie a new ranking reversed from their order
        # in all_movies
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movies=all_movies)

# @app.route("/add", methods=["GET", "POST"])
# def add():
#     if request.method == "POST":
#         # CREATE RECORD
#         new_movie = Movie(
#             title=request.form["title"],
#             year=request.form["year"],
#             description=request.form["description"],
#             rating=request.form["rating"],
#             ranking=request.form["ranking"],
#             review=request.form["review"],
#             img_url=request.form["img_url"],

#         )
#         db.session.add(new_movie)
#         db.session.commit()
#         return redirect(url_for('home'))
#     return render_template("add.html")


class FindMovieForm(FlaskForm):
    new_movie = StringField(label="Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")


@app.route("/add", methods=["GET", "POST"])
def add():
    form = FindMovieForm()

    if form.validate_on_submit():
        movie_title = form.new_movie.data
        response = requests.get(MOVIE_DB_SEARCH_URL, params={
                                "api_key": API_TMDB, "query": movie_title})
        response.raise_for_status()
        data = response.json()
        data = data["results"]
        return render_template("select.html", options=data)

    return render_template("add.html", form=form)


@app.route("/find")
def find_movie():
    movie_api_id = request.args.get("id")
    if movie_api_id:
        movie_api_url = f"{MOVIE_DB_INFO_URL}/{movie_api_id}"

        response = requests.get(movie_api_url, params={
                                "api_key": API_TMDB,
                                "language": "en-US"})
        data = response.json()

        new_movie = Movie(
            title=data["title"],
            # The data in release_date includes month and day, we will want to
            # get rid of.
            year=data["release_date"].split("-")[0],
            img_url=f"{MOVIE_DB_IMAGE_URL}{data['poster_path']}",
            description=data["overview"]
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("edit", id=new_movie.id))


@app.route("/edit", methods=["GET", "POST"])
def edit():
    edit_form = EditForm()
    movie_id = request.args.get('id')
    movie_selected = Movie.query.get(movie_id)

    if request.method == "POST":
        if edit_form.validate_on_submit:
            # UPDATE RECORD
            movie_to_update = Movie.query.get(movie_id)
            movie_to_update.rating = float(edit_form.edit_rating.data)
            movie_to_update.review = edit_form.edit_review.data
            db.session.commit()
            return redirect(url_for('home'))

    return render_template("edit.html", movie=movie_selected, form=edit_form)


if __name__ == '__main__':
    app.run(debug=True)
