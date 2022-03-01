import requests
import smtplib
import flask
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


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if flask.request.method == "POST":
        name = flask.request.form["name"]
        email = flask.request.form["email"]
        phone = flask.request.form["phone"]
        message = flask.request.form["message"]

        my_email = "filipe1@gmail.com"
        to_addres_email = "filipe1@gmail.com"
        password = "senha123"
        subject_msg = "Subject:New Message"

        content_msg = f"Name: {name}\nEmail: {email}\n"\
            f"Phone: {phone}\nMessage:{message}"

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=to_addres_email,
                                msg=f"{subject_msg}\n\n{content_msg}"
                                )

        return render_template("contact.html", msg_sended=True)
    return render_template("contact.html", msg_sended=False)


@app.route('/about')
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
