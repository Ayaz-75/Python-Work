from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

posts = [

    {
    "author": "Ayaz",
    "title": "Post-1",
    "content": "This is first post",
    'date_posted': "22-02-2023",
    },
        {
    "author": "Aaqib",
    "title": "Post-2",
    "content": "This is second post",
    'date_posted': "23-02-2023",
    },

]

app = Flask(__name__)


app.config['SECRET_KEY'] = '014e91d5e0bd34751333b3a9f7b106a1'


@app.route("/")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="about")

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == "__main__":
    app.run(debug=True)

