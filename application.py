from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")


@app.route("/study")
def study():
    return render_template("study.html")

@app.route("/travel")
def travel():
    return render_template("travel.html")

@app.route("/hello")
def hello():
    return "Hello"
