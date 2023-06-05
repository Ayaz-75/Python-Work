import random
from flask import Flask, render_template
from datetime import date

app = Flask(__name__)
year = date.today().year
print(year)

@app.route("/")
def hello():
    random_number = random.randint(1, 10)
    return render_template("index.html", num=random_number, year=year)


@app.route("/bye")
def bye():
    return "Bye"


if __name__ == "__main__":
    app.run(debug=True)

