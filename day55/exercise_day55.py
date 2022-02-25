from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1><p>This '\
        'is a paragraph.</p>'\
        '<img src= "https://media2.giphy.com/media/4Iw2OzgiiTc4M/giphy.gif?" width=200px >'


@app.route('/bye')
def say_bye():
    return "Bye"
# Different routs using the app.route decorator


@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello, there {name}, you are {number} years old."
# creating variable paths and converting the path to a specified data type


class User:
    def __init__(self, name) -> None:
        self.name = name
        self.is_logged_in = False


def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper


@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")


if __name__ == "__main__":
    # run the app in debug mode to auto-reload
    # app.run(debug=True)
    new_user = User("Filipe")
    new_user.is_logged_in = True
    create_blog_post(new_user)
