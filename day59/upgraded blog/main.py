import requests
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)

    all_posts = response.json()
    return render_template("index.html", posts=all_posts)


@app.route('/post/<int:id>')
def get_post(id):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)

    all_posts = response.json()
    print(id)

    for post in all_posts:
        if post['id'] == id:
            return render_template("post.html", posts=post)

    return home()


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
