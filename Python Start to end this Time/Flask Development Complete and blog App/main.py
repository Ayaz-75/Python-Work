from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

posts = [
    {
        'author': 'Zahoor Gabole',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 8, 2022'
    },
    {
        'author': 'Aman Shahani',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 9, 2022'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html',title='Register', form=form)


@app.route('/login')
def login():
    form = RegistrationForm()
    return render_template('login.html',title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)