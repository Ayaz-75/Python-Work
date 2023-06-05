import random
from datetime import date

import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    year = date.today().year
    random_number = random.randint(1, 10)
    return render_template("index.html", num=random_number, year=year)

@app.route("/guess/<name>")
def guess(name):
    gender_url = f"https://api.genderize.io?name={name}"
    gender_response = requests.get(gender_url)
    gender_data = gender_response.json()
    gender = gender_data['gender']

    age_url = f"https://api.agify.io?name={name}"
    age_response = requests.get(age_url)
    age_data = age_response.json()
    age = age_data['age']
    return render_template("guess.html", name = name, gender=gender, age=age)

@app.route("/blog")
def blog():
    blog_url = "https://api.npoint.io/3e36db8b131651ac5239"
    blog_response = requests.get(blog_url)
    blog_data = blog_response.json()
    return render_template("blog.html", all_post = blog_data)

if __name__ == "__main__":
    app.run(debug=True)


