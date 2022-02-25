from random import randint
from flask import Flask
app = Flask(__name__)

random_number = randint(0, 9)
print(random_number)


@app.route('/')
def guess_a_number():
    return '<h1 style="font-family: sans-serif">Adivinhe um numero entre 0 e 9</h1>'\
        '<img src= "https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width=400px >'


@app.route('/<int:number>')
def number_choosed(number):
    if number == random_number:
        return '<h1 style="font-family: sans-serif">Voce me encontrou, acertou!</h1>'\
            '<img src= "https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" width=400px >'
    elif number < random_number:
        return '<h1 style="font-family: sans-serif">Muito baixo, tente novamente! :(</h1>'\
            '<img src= "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" width=400px >'
    else:
        return '<h1 style="font-family: sans-serif">Muito alto, tente novamente! :(</h1>'\
            '<img src= "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" width=400px >'


if __name__ == "__main__":
    app.run(debug=True)
