# from flask import Flask, url_for
#
#
# app = Flask(__name__)
#
# @app.route("/")
# def hello():
#     return f"Hello there!"
#
#
# @app.route("/<name>")
# def greetings(name):
#     return f"Hello {name}"
#
#
# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     # show the post with the given id, the id is an integer
#     return f'Post {post_id}'
#
#
#
# if __name__ == "__main__":
#     app.run(debug=True)
#


from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))