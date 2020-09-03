from flask import Flask, render_template

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True)