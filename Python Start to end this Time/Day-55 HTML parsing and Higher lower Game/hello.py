from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper():
        return f"<b>{function()} </b>"
    return wrapper


def make_emp(function):
    def wrapper():
        return f"<em>{function()}</em>"
    return wrapper


def make_underlined(function):
    def wrapper():
        return f"<u>{function()}</u>"
    return wrapper


@app.route("/")
def hello():
    return "Hello there!"


@app.route("/bye")
@make_bold
@make_emp
@make_underlined
def bye():
    return "<h1 style= 'text-align: center'> Bye </h1>"

if __name__ == "__main__":
    app.run(debug=True)


