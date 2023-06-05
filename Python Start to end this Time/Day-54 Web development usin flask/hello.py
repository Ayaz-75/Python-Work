from flask import Flask

app = Flask(__name__)
@app.route("/")


def make_bold(function):
    def wrapper():
        return f"<b>{function}</b>"
    return wrapper


def make_emp(function):
    def wrapper():
        return f"<em>{function}</em>"
    return wrapper


def make_underlined(function):
    def wrapper():
        return f"<u>{function}</u>"
    return wrapper


def hello_world():
    return '<h1>Hello, World!</h1>' \
           '<p> I am paragraph </p>' \
           '<img src="https://media.giphy.com/media/uWYjSbkIE2XIMIc7gh/giphy.gif" width=200>'


@app.route("/bye")
@make_bold
@make_emp
@make_underlined

def bye():
    return "Bye"



@app.route("/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}! You are {number} years old."

app.run(debug=True)








