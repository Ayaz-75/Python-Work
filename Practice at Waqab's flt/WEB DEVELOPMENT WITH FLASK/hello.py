from flask import Flask

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, Ayaz!</p>"

def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def make_italic(function):
    def emphasise():
        return "<em>" + function() + "</em>"
    return emphasise

def make_underlined(function):
    def underline():
        return "<u>" + function() + "</u>"
    return underline



# @app.route("/")
# def greetings():
#     return '<h1> Hello World ! </h1>'\
#            '<p> This is a paragraph <p>' \
#            '<img src="https://media.giphy.com/media/8BKRfgnUt0KvS/giphy.gif" width=200>'


@app.route("/")
@make_bold
@make_italic
@make_underlined
def say_bye():
    return f"Bye Ayaz"


if __name__ == "__main__":
    app.run(debug=True)
    
