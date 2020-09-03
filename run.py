from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "210c1f0577b484480cbade543d42ca3a"

posts = [
    {
        "author": "Tyler Lum",
        "title": "Blog Post 1",
        "content": "First post content",
        "date_posted": "August 20, 2020"
    },
    {
        "author": "Corey Schafer",
        "title": "Blog Post 2",
        "content": "Second post content",
        "date_posted": "August 21, 2020"
    }
]

@app.route("/")
@app.route("/home")
def hello():
    return render_template("home.html", posts=posts, title="My Title")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template("register.html", title="Register", form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title="Login", form=form)

if __name__ == "__main__":
    app.run(debug=True)