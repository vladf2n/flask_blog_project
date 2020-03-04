from flask import Flask, render_template, url_for
app = Flask(__name__)

# Dummy variables to use in html
posts = [
    {
        'author': 'Valmir Ferreira',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'March 01, 2020'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'March 02, 2020'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')