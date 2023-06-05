from flask import Flask
import random

random_num = random.randint(1, 9)

app = Flask(__name__)

@app.route("/")
def greetings():
    return '<h1>"Guess a number between 0 and 9" <br>'\
           '<img src="https://media.giphy.com/media/l41YtZOb9EUABnuqA/giphy.gif" width=200>'

@app.route("/<int:num>")
def match_num(num):
    if num == random_num:
        return f'<h1>You found me {num}</h1> <br><img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExYzU0OGYzNGFjZDVkMGY0YWMxM2RmYWFiYjNjNzgwNTEzODMxZGUzZCZjdD1n/4T7e4DmcrP9du/giphy.gif" width=200>'

    elif num <= random_num:
        return f'<h1>Too low! number was: {random_num}</h1> <br><img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMDcxYzEwOWRmMDVlZDA5YTAyYmMyYjFkMTE2NzQ1Yzg3YmY2NmJjZiZjdD1n/jD4DwBtqPXRXa/giphy-downsized-large.gif" width=200>'

    elif num >= random_num:
        return f'<h1>Too high! number was: {random_num}</h1> <br><img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMDg2ZGFjNjU0ZmE4NjIzZDI0OWU5MTJlNTNiNzJmOGFiMTUwYjBhYyZjdD1n/3o6ZtaO9BZHcOjmErm/giphy.gif">'


if __name__ == "__main__":
    app.run(debug=True)



# @app.route("/")
# def hello_world():
#     return "<p>Hello, Ayaz!</p>"

# def make_bold(function):
#     def wrapper():
#         return "<b>" + function() + "</b>"
#     return wrapper

# def make_italic(function):
#     def emphasise():
#         return "<em>" + function() + "</em>"
#     return emphasise

# def make_underlined(function):
#     def underline():
#         return "<u>" + function() + "</u>"
#     return underline


# @app.route("/")
# @make_bold
# @make_italic
# @make_underlined
# def say_bye():
#     return f"Bye Ayaz"


