from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def index():
    return render_template("index.html")

@app.route("/portfolio.html")
def portfolio():
    return render_template("portfolio.html")


@app.route("/study.html")
def study():
    return render_template("study.html")

@app.route("/travel.html")
def travel():
    return render_template("travel.html")