import requests
from flask import Flask, render_template
import random
from datetime import date
app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1, 10)
    year_current = date.today().year
    return render_template("index.html", num=random_number, year=year_current)


@app.route('/guess/<name>')
def guess(name):
    gender_url = f"https://api.genderize.io/?name={name}"
    age_url = f"https://api.agify.io/?name={name}"
    gender_response = requests.get(gender_url)
    gender_data = gender_response.json()

    age_response = requests.get(age_url)
    age_data = age_response.json()

    age = age_data["age"]
    gender = gender_data["gender"]
    return render_template("guess.html", name=name, age=age, gender=gender)


@app.route("/blog/<num>")
def get_blog(num):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)

    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
