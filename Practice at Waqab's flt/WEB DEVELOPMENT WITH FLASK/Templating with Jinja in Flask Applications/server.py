from flask import Flask, render_template
import datetime
import requests

app = Flask(__name__)

@app.route("/")
def hello_server():

    today = datetime.datetime.now()

    #accessing the year attribute
    footer_year = today.year
    return render_template("index.html", year=footer_year)

@app.route("/guess/<name>")
def all_estimations(name):
    gender_url = f"https://api.genderize.io?name={name}"
    age_url = f"https://api.agify.io?name={name}"

    gender_response = requests.get(gender_url)
    gender_data = gender_response.json()
    gender = gender_data['gender']

    age_response = requests.get(age_url)
    age_data = age_response.json()
    age = age_data['age']
    return render_template("guess.html", person_name = name, gender=gender, age=age)


@app.route("/blog/<num>")
def get_blog(num):
    blog_url = "https://api.npoint.io/d056c115acc2f74b2f33"
    blog_response = requests.get(blog_url)
    all_posts = blog_response.json()
    return render_template("blog.html", posts = all_posts)


if __name__ == "__main__":
    app.run(debug=True)

