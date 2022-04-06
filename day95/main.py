from pprint import pprint
from typing import Any, Dict
from flask import Flask, render_template, request
from flask import redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
import requests
from wtforms import SubmitField, StringField
from local_settings.local_settings import OWLBOT_API


image_name = "default.jpg"
word_to_search = 'default'
word_mean: Dict[Any, Any] = {}
OWLBOT_ENDPOINT = "https://owlbot.info/api/v4/dictionary"


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


def search_word(word_to_search):
    headers = {"Authorization": f"Token {OWLBOT_API}"}
    url_search = f"{OWLBOT_ENDPOINT}/{word_to_search}"

    try:
        response = requests.get(url=url_search, headers=headers,)
        response.raise_for_status()
        word_mean = response.json()
    except Exception as e:
        msg_error = e
        e = msg_error
        word_mean = {
            'definitions': [{
                'definition': 'not founded.',
                'type': 'not founded.',
            }],
            'word': 'not founded / invalid word',
        }

    return word_mean


class WordForm(FlaskForm):
    word_to_search = StringField(
        'Enter the word to search into the Dictionary')
    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    global image_name, word_to_search

    image_name = "default.jpg"
    word_to_search = 'default'

    word_mean = search_word(word_to_search)
    pprint(word_mean)

    return render_template("index.html")


@app.route("/dictionary_word", methods=["GET", "POST"])
def get_dictionary_word():
    global image_name, word_to_search
    form = WordForm()

    word_mean = search_word(word_to_search)

    if request.method == "POST":
        if form.validate_on_submit():

            return render_template(
                'dictionary_word.html',
                word_mean=word_mean,
                form=form)

    return render_template(
        'dictionary_word.html',
        word_mean=word_mean,
        form=form)


@app.route('/get_word', methods=["GET", "POST"])
def get_word():
    global image_name, word_to_search
    form = WordForm()

    if form.validate_on_submit():
        word_to_search = str(form.word_to_search.data).strip()
        return redirect(url_for('get_dictionary_word'))

    return render_template('add.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
